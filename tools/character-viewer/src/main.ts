import "./styles.css";

import type { Group } from "three";

import {
  applyCameraPreset,
  createViewerCamera
} from "./viewer/camera";
import { createViewerControls } from "./viewer/controls";
import { loadBundledGlb } from "./viewer/model-loader";
import { loadViewerRequest } from "./protocol/viewer-request";
import { createViewerScene } from "./viewer/scene";

const canvas = document.querySelector<HTMLCanvasElement>("#viewer-canvas");
const titleEl = document.querySelector<HTMLElement>("#viewer-title");
const statusEl = document.querySelector<HTMLElement>("#viewer-status");
const errorBanner = document.querySelector<HTMLElement>("#error-banner");
const resetButton = document.querySelector<HTMLButtonElement>("#reset-camera");

if (!canvas || !titleEl || !statusEl || !errorBanner || !resetButton) {
  throw new Error("Viewer bootstrap failed because the root DOM nodes were not found.");
}

const viewerScene = createViewerScene(canvas);
const camera = createViewerCamera(canvas);
const controls = createViewerControls(camera, canvas);
viewerScene.resize(camera);

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

    const loaded = await loadBundledGlb(request.modelPath);
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
