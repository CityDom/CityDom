import "./styles.css";

import type { Group } from "three";
import { LogicalPosition, LogicalSize, PhysicalPosition, PhysicalSize, getCurrentWindow } from "@tauri-apps/api/window";
import type { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
import type { PerspectiveCamera } from "three";

import {
  applyCameraPreset,
  createViewerCamera
} from "./viewer/camera";
import { createViewerControls } from "./viewer/controls";
import { createMaterialDebugPanel } from "./viewer/material-debug";
import { loadBundledModel } from "./viewer/model-loader";
import type { LoadedModel } from "./viewer/model-loader";
import { loadViewerRequest, loadViewerRuntimeOptions } from "./protocol/viewer-request";
import { createViewerBridge } from "./protocol/viewer-bridge";
import type { ShowCharacterCommand, ViewerCommand } from "./protocol/viewer-bridge";
import { createViewerScene } from "./viewer/scene";
import type { ViewerRuntimeOptions } from "./protocol/viewer-request";

const canvasEl = document.querySelector<HTMLCanvasElement>("#viewer-canvas");
const titleElement = document.querySelector<HTMLElement>("#viewer-title");
const statusElement = document.querySelector<HTMLElement>("#viewer-status");
const errorElement = document.querySelector<HTMLElement>("#error-banner");
const resetCameraButton = document.querySelector<HTMLButtonElement>("#reset-camera");

if (!canvasEl || !titleElement || !statusElement || !errorElement || !resetCameraButton) {
  throw new Error("Viewer bootstrap failed because the root DOM nodes were not found.");
}

const canvas = canvasEl;
const titleEl = titleElement;
const statusEl = statusElement;
const errorBanner = errorElement;
const resetButton = resetCameraButton;

function setStatus(message: string): void {
  statusEl.textContent = message;
}

function showError(message: string): void {
  errorBanner.hidden = false;
  errorBanner.textContent = message;
}

function clearError(): void {
  errorBanner.hidden = true;
  errorBanner.textContent = "";
}

async function configureWindow(options: ViewerRuntimeOptions): Promise<void> {
  if (!options.embedded) {
    return;
  }

  document.body.classList.add("embed-mode");
  document.documentElement.classList.add("embed-mode");

  const window = getCurrentWindow();

  const safeWindowCall = async (label: string, action: () => Promise<void>): Promise<void> => {
    try {
      await action();
    } catch (error) {
      console.warn(`Embedded viewer window call failed: ${label}`, error);
    }
  };

  await safeWindowCall("setDecorations", () => window.setDecorations(false));
  await safeWindowCall("setShadow", () => window.setShadow(false));
  await safeWindowCall("setResizable", () => window.setResizable(true));
  await safeWindowCall("setAlwaysOnTop", () => window.setAlwaysOnTop(options.alwaysOnTop));
  await safeWindowCall("setSkipTaskbar", () => window.setSkipTaskbar(true));

  if (options.width && options.height) {
    const width = options.width;
    const height = options.height;
    await safeWindowCall("setSize", () => window.setSize(new LogicalSize(width, height)));
  }

  if (typeof options.x === "number" && typeof options.y === "number") {
    const x = options.x;
    const y = options.y;
    await safeWindowCall("setPosition", () => window.setPosition(new LogicalPosition(x, y)));
  }
}

function cameraDistance(camera: PerspectiveCamera, controls: OrbitControls): number {
  return camera.position.distanceTo(controls.target);
}

function formatNumber(value: number): string {
  return Number.isFinite(value) ? value.toFixed(0) : "?";
}

function formatDecimal(value: number): string {
  return Number.isFinite(value) ? value.toFixed(2) : "?";
}

function applyRuntimeCameraTuning(
  camera: PerspectiveCamera,
  controls: OrbitControls,
  options: ViewerRuntimeOptions
): void {
  if (typeof options.minDistance === "number") {
    controls.minDistance = Math.max(0.05, options.minDistance);
  }

  if (typeof options.maxDistance === "number") {
    controls.maxDistance = Math.max(controls.minDistance + 0.5, options.maxDistance);
  }

  if (typeof options.zoom === "number") {
    const direction = camera.position.clone().sub(controls.target);
    if (direction.lengthSq() <= 0.000001) {
      direction.set(0, 0, 1);
    }

    const distance = Math.max(
      controls.minDistance,
      Math.min(controls.maxDistance, options.zoom)
    );
    camera.position.copy(controls.target).add(direction.normalize().multiplyScalar(distance));
  }

  controls.update();
  controls.saveState();
}

async function createEmbedTuningPanel(
  camera: PerspectiveCamera,
  controls: OrbitControls,
  onResize: () => void
): Promise<void> {
  if (!document.body.classList.contains("embed-mode")) {
    return;
  }

  const appWindow = getCurrentWindow();
  const panel = document.createElement("section");
  panel.className = "embed-tuning-panel";

  const readout = document.createElement("pre");
  readout.className = "embed-tuning-readout";
  panel.append(readout);

  const buttons = document.createElement("div");
  buttons.className = "embed-tuning-buttons";
  panel.append(buttons);

  document.body.append(panel);

  let position = await appWindow.outerPosition();
  let size = await appWindow.outerSize();

  async function refresh(): Promise<void> {
    try {
      position = await appWindow.outerPosition();
      size = await appWindow.outerSize();
    } catch (error) {
      console.warn("Could not read embedded viewer window geometry.", error);
    }

    readout.textContent = [
      `x=${formatNumber(position.x)} y=${formatNumber(position.y)}`,
      `w=${formatNumber(size.width)} h=${formatNumber(size.height)}`,
      `zoom=${formatDecimal(cameraDistance(camera, controls))}`,
      `min=${formatDecimal(controls.minDistance)} max=${formatDecimal(controls.maxDistance)}`,
      "arrows move | shift+arrows resize",
      "+/- zoom | [ ] max | { } min | D hide"
    ].join("\n");
  }

  async function moveBy(dx: number, dy: number): Promise<void> {
    await appWindow.setPosition(new PhysicalPosition(position.x + dx, position.y + dy));
    await refresh();
  }

  async function resizeBy(dw: number, dh: number): Promise<void> {
    const width = Math.max(120, size.width + dw);
    const height = Math.max(160, size.height + dh);
    await appWindow.setSize(new PhysicalSize(width, height));
    onResize();
    await refresh();
  }

  function zoomBy(delta: number): void {
    const direction = camera.position.clone().sub(controls.target).normalize();
    const current = cameraDistance(camera, controls);
    const next = Math.max(controls.minDistance, Math.min(controls.maxDistance, current + delta));
    camera.position.copy(controls.target).add(direction.multiplyScalar(next));
    controls.update();
    void refresh();
  }

  function adjustLimit(kind: "min" | "max", delta: number): void {
    if (kind === "min") {
      controls.minDistance = Math.max(0.05, controls.minDistance + delta);
      controls.maxDistance = Math.max(controls.maxDistance, controls.minDistance + 0.5);
    } else {
      controls.maxDistance = Math.max(controls.minDistance + 0.5, controls.maxDistance + delta);
    }
    controls.update();
    void refresh();
  }

  function addButton(label: string, action: () => void | Promise<void>): void {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = label;
    button.addEventListener("click", (event) => {
      event.stopPropagation();
      void action();
    });
    buttons.append(button);
  }

  addButton("left", () => moveBy(-2, 0));
  addButton("right", () => moveBy(2, 0));
  addButton("up", () => moveBy(0, -2));
  addButton("down", () => moveBy(0, 2));
  addButton("w-", () => resizeBy(-4, 0));
  addButton("w+", () => resizeBy(4, 0));
  addButton("h-", () => resizeBy(0, -4));
  addButton("h+", () => resizeBy(0, 4));
  addButton("zoom-", () => zoomBy(0.08));
  addButton("zoom+", () => zoomBy(-0.08));
  addButton("min-", () => adjustLimit("min", -0.05));
  addButton("min+", () => adjustLimit("min", 0.05));
  addButton("max-", () => adjustLimit("max", -0.20));
  addButton("max+", () => adjustLimit("max", 0.20));
  addButton("hide", () => {
    panel.classList.toggle("is-hidden");
  });

  window.addEventListener("keydown", (event) => {
    if (event.key.toLowerCase() === "d") {
      panel.classList.toggle("is-hidden");
      return;
    }

    if (event.key === "+" || event.key === "=") {
      zoomBy(-0.35);
      return;
    }

    if (event.key === "-" || event.key === "_") {
      zoomBy(0.35);
      return;
    }

    if (event.key === "[") {
      adjustLimit("max", -1.0);
      return;
    }

    if (event.key === "]") {
      adjustLimit("max", 1.0);
      return;
    }

    if (event.key === "{") {
      adjustLimit("min", -0.25);
      return;
    }

    if (event.key === "}") {
      adjustLimit("min", 0.25);
      return;
    }

    const step = event.ctrlKey ? 10 : 2;
    const resizeStep = event.ctrlKey ? 20 : 4;
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      void (event.shiftKey ? resizeBy(-resizeStep, 0) : moveBy(-step, 0));
    } else if (event.key === "ArrowRight") {
      event.preventDefault();
      void (event.shiftKey ? resizeBy(resizeStep, 0) : moveBy(step, 0));
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      void (event.shiftKey ? resizeBy(0, -resizeStep) : moveBy(0, -step));
    } else if (event.key === "ArrowDown") {
      event.preventDefault();
      void (event.shiftKey ? resizeBy(0, resizeStep) : moveBy(0, step));
    }
  });

  setInterval(() => {
    void refresh();
  }, 500);

  await refresh();
}

interface CachedCharacter {
  characterId: string;
  modelPath: string;
  loaded: LoadedModel;
  lastUsed: number;
}

const CHARACTER_CACHE_SIZE = 3;

async function start(): Promise<void> {
  const runtimeOptions = await loadViewerRuntimeOptions();
  const appWindow = getCurrentWindow();
  const bridge = createViewerBridge(runtimeOptions);
  const cache = new Map<string, CachedCharacter>();
  const pendingLoads = new Map<string, Promise<CachedCharacter>>();
  let activeCharacter: CachedCharacter | null = null;
  let requestedCharacterVersion = 0;
  let commandPollBusy = false;

  await bridge.setState("shell_starting");
  await bridge.timing("js_ready");

  async function revealWindow(characterId: string): Promise<void> {
    try {
      await bridge.setState("visible", characterId);
      await appWindow.show();
      await bridge.timing("viewer_shown", `character=${characterId}`);
    } catch (error) {
      console.warn("Viewer window show failed.", error);
    }
  }

  async function hideWindow(): Promise<void> {
    try {
      await appWindow.hide();
    } catch (error) {
      console.warn("Viewer window hide failed.", error);
    }
  }

  if (runtimeOptions.debugMaterials) {
    document.body.classList.add("debug-materials-mode");
  }

  await configureWindow(runtimeOptions);

  const viewerScene = createViewerScene(canvas, {
    transparent: runtimeOptions.embedded || runtimeOptions.debugMaterials
  });
  const camera = createViewerCamera(canvas);
  const controls = createViewerControls(camera, canvas);
  viewerScene.resize(camera);
  await bridge.timing("three_renderer_ready");
  if (runtimeOptions.debugGeometry) {
    await createEmbedTuningPanel(camera, controls, () => viewerScene.resize(camera));
  }

  function resetCamera(): void {
    controls.reset();
  }

  resetButton.addEventListener("click", resetCamera);
  window.addEventListener("keydown", (event) => {
    if (event.key.toLowerCase() === "r") {
      resetCamera();
    }
  });

  window.addEventListener("resize", () => {
    viewerScene.resize(camera);
  });

  window.addEventListener("beforeunload", () => {
    controls.dispose();
    for (const entry of cache.values()) {
      entry.loaded.dispose();
    }
    viewerScene.dispose();
  });

  function evictOldCharacters(): void {
    while (cache.size > CHARACTER_CACHE_SIZE) {
      const candidate = [...cache.values()]
        .filter((entry) => entry !== activeCharacter)
        .sort((left, right) => left.lastUsed - right.lastUsed)[0];
      if (!candidate) {
        return;
      }

      viewerScene.scene.remove(candidate.loaded.group);
      candidate.loaded.dispose();
      cache.delete(candidate.characterId);
      void bridge.timing("cache_eviction", `character=${candidate.characterId}`);
    }
  }

  async function getOrLoadCharacter(command: ShowCharacterCommand): Promise<CachedCharacter> {
    const cached = cache.get(command.character_id);
    if (cached && cached.modelPath === command.model_path) {
      cached.lastUsed = performance.now();
      await bridge.timing("cache_hit", `character=${command.character_id}`);
      return cached;
    }
    if (cached) {
      viewerScene.scene.remove(cached.loaded.group);
      cached.loaded.dispose();
      cache.delete(command.character_id);
    }

    const pending = pendingLoads.get(command.character_id);
    if (pending) {
      await bridge.timing("cache_hit_pending", `character=${command.character_id}`);
      return pending;
    }

    await bridge.timing("cache_miss", `character=${command.character_id}`);
    const loadPromise = (async () => {
      await bridge.setState("character_loading", command.character_id);
      await bridge.timing("glb_load_start", `character=${command.character_id}`);
      const loaded = await loadBundledModel(command.model_path, {
        applyHs2Overrides: true,
        renderer: viewerScene.renderer
      });
      await bridge.timing("glb_load_complete", `character=${command.character_id}`);
      const entry: CachedCharacter = {
        characterId: command.character_id,
        modelPath: command.model_path,
        loaded,
        lastUsed: performance.now()
      };
      cache.set(command.character_id, entry);
      pendingLoads.delete(command.character_id);
      evictOldCharacters();
      await bridge.setState("character_loaded", command.character_id);
      return entry;
    })().catch((error) => {
      pendingLoads.delete(command.character_id);
      throw error;
    });

    pendingLoads.set(command.character_id, loadPromise);
    return loadPromise;
  }

  async function parkViewer(): Promise<void> {
    requestedCharacterVersion += 1;
    await bridge.setState("parked");
    await hideWindow();
    if (activeCharacter) {
      viewerScene.scene.remove(activeCharacter.loaded.group);
      activeCharacter = null;
    }
    await bridge.timing("viewer_parked");
  }

  async function showCharacter(command: ShowCharacterCommand): Promise<void> {
    const requestVersion = ++requestedCharacterVersion;
    clearError();
    titleEl.textContent = `City Dom 3D Viewer - ${command.character_id}`;
    setStatus(`Loading model for ${command.character_id}...`);
    await bridge.setState("character_loading", command.character_id);
    await hideWindow();
    await bridge.timing("character_load_requested", `character=${command.character_id}`);

    const entry = await getOrLoadCharacter(command);
    if (requestVersion !== requestedCharacterVersion) {
      return;
    }

    if (activeCharacter && activeCharacter !== entry) {
      viewerScene.scene.remove(activeCharacter.loaded.group);
    }
    activeCharacter = entry;
    entry.lastUsed = performance.now();
    if (!entry.loaded.group.parent) {
      viewerScene.scene.add(entry.loaded.group);
    }
    await bridge.timing("model_added_to_scene", `character=${command.character_id}`);

    applyCameraPreset(
      camera,
      controls,
      entry.loaded.group,
      command.camera_preset ?? "full_body"
    );
    applyRuntimeCameraTuning(camera, controls, runtimeOptions);
    if (runtimeOptions.debugMaterials) {
      createMaterialDebugPanel(entry.loaded.group);
    }

    await bridge.setState("character_warming", command.character_id);
    viewerScene.resize(camera);
    viewerScene.render(camera);
    await new Promise<void>((resolve) => requestAnimationFrame(() => resolve()));
    viewerScene.render(camera);
    await bridge.timing("first_hidden_render_complete", `character=${command.character_id}`);
    await bridge.setState("character_ready", command.character_id);
    await bridge.timing("character_ready", `character=${command.character_id}`);

    if (requestVersion !== requestedCharacterVersion) {
      return;
    }
    setStatus(`Loaded ${command.character_id}`);
    await revealWindow(command.character_id);
  }

  async function handleCommand(command: ViewerCommand): Promise<void> {
    try {
      if (command.action === "park") {
        await parkViewer();
      } else if (command.action === "shutdown") {
        await appWindow.close();
      } else if (command.action === "preload_character") {
        await bridge.timing("preload_requested", `character=${command.character_id}`);
        await getOrLoadCharacter(command);
      } else {
        await showCharacter(command as ShowCharacterCommand);
      }
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      setStatus("Viewer failed to load the character.");
      showError(message);
      await bridge.setState("error", "character_id" in command ? command.character_id : undefined, message);
      await bridge.timing("error", message);
      await hideWindow();
    }
  }

  function animate(): void {
    requestAnimationFrame(animate);
    controls.update();
    viewerScene.render(camera);
  }

  animate();
  await bridge.setState("shell_ready");
  await bridge.timing("viewer_shell_ready");

  if (runtimeOptions.shellOnly && runtimeOptions.commandPath) {
    await hideWindow();
    await bridge.setState("parked");
    setInterval(() => {
      if (commandPollBusy) {
        return;
      }
      commandPollBusy = true;
      void bridge.readNextCommand()
        .then((command) => {
          commandPollBusy = false;
          if (command) {
            void handleCommand(command);
          }
        })
        .catch((error) => {
          commandPollBusy = false;
          console.warn("Viewer command poll failed.", error);
        });
    }, 100);
    return;
  }

  try {
    const request = await loadViewerRequest();
    await showCharacter({
      sequence: 0,
      action: "show_character",
      character_id: request.characterId,
      model_path: request.modelPath,
      camera_preset: request.cameraPreset
    });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown viewer startup failure.";
    setStatus("Viewer failed to start.");
    showError(message);
    await appWindow.show();
  }
}

start().catch((error) => {
  const message = error instanceof Error ? error.message : "Unknown viewer startup failure.";
  document.body.classList.remove("embed-mode");
  setStatus("Viewer failed to start.");
  showError(message);
  void getCurrentWindow().show();
});
