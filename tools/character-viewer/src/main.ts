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
import { loadBundledModel } from "./viewer/model-loader";
import { loadViewerRequest, loadViewerRuntimeOptions } from "./protocol/viewer-request";
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

let loadedModel: Group | null = null;
let disposeModel: (() => void) | null = null;

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

  const window = getCurrentWindow();

  const safeWindowCall = async (label: string, action: () => Promise<void>): Promise<void> => {
    try {
      await action();
    } catch (error) {
      console.warn(`Embedded viewer window call failed: ${label}`, error);
    }
  };

  await safeWindowCall("setDecorations", () => window.setDecorations(false));
  await safeWindowCall("setResizable", () => window.setResizable(true));
  await safeWindowCall("setAlwaysOnTop", () => window.setAlwaysOnTop(options.alwaysOnTop));

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

async function start(): Promise<void> {
  const runtimeOptions = await loadViewerRuntimeOptions();
  await configureWindow(runtimeOptions);

  const viewerScene = createViewerScene(canvas, { transparent: runtimeOptions.embedded });
  const camera = createViewerCamera(canvas);
  const controls = createViewerControls(camera, canvas);
  viewerScene.resize(camera);
  await createEmbedTuningPanel(camera, controls, () => viewerScene.resize(camera));

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
    disposeModel?.();
    viewerScene.dispose();
  });

  async function bootstrap(): Promise<void> {
    try {
      clearError();
      setStatus("Loading viewer request...");

      const request = await loadViewerRequest();
      titleEl.textContent = `City Dom 3D Viewer - ${request.characterId}`;
      setStatus(`Loading model for ${request.characterId}...`);

      const loaded = await loadBundledModel(request.modelPath);
      loadedModel = loaded.group;
      disposeModel = loaded.dispose;

      viewerScene.scene.add(loadedModel);
      applyCameraPreset(camera, controls, loadedModel, request.cameraPreset);

      setStatus(`Loaded ${request.characterId}`);
    } catch (error) {
      const message =
        error instanceof Error ? error.message : "Unknown viewer startup failure.";
      setStatus("Viewer failed to start.");
      showError(message);
    }
  }

  function animate(): void {
    requestAnimationFrame(animate);
    controls.update();
    viewerScene.render(camera);
  }

  void bootstrap();
  animate();
}

start().catch((error) => {
  const message =
    error instanceof Error ? error.message : "Unknown viewer startup failure.";
  document.body.classList.remove("embed-mode");
  setStatus("Viewer failed to start.");
  showError(message);
});
