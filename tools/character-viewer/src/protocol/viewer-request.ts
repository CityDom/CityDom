import { resolveResource } from "@tauri-apps/api/path";
import { invoke } from "@tauri-apps/api/core";
import { getMatches } from "@tauri-apps/plugin-cli";
import { readTextFile } from "@tauri-apps/plugin-fs";

import type { CameraPreset } from "../viewer/camera";

export interface ViewerRequest {
  characterId: string;
  modelPath: string;
  cameraPreset: CameraPreset;
}

export interface ViewerRuntimeOptions {
  embedded: boolean;
  shellOnly: boolean;
  debugMaterials: boolean;
  debugGeometry: boolean;
  commandPath?: string;
  statusPath?: string;
  timingLogPath?: string;
  x?: number;
  y?: number;
  width?: number;
  height?: number;
  zoom?: number;
  minDistance?: number;
  maxDistance?: number;
  alwaysOnTop: boolean;
}

interface CliArgumentValue {
  value?: string | boolean | string[] | null;
}

interface CliMatchesShape {
  args?: Record<string, CliArgumentValue>;
}

interface NativeBridgeOptions {
  embedded: boolean;
  shellOnly: boolean;
  commandPath?: string;
  statusPath?: string;
  timingLogPath?: string;
  zoom?: number;
  minDistance?: number;
  maxDistance?: number;
  alwaysOnTop: boolean;
}

function looksAbsolutePath(value: string): boolean {
  return (
    value.startsWith("/") ||
    value.startsWith("\\\\") ||
    /^[A-Za-z]:[\\/]/.test(value) ||
    value.startsWith("asset://")
  );
}

function getCliStringArg(matches: CliMatchesShape, name: string): string | undefined {
  const camelCaseName = name.replace(/-([a-z])/g, (_, letter: string) => letter.toUpperCase());
  const value = matches.args?.[name]?.value ?? matches.args?.[camelCaseName]?.value;

  if (typeof value === "string" && value.trim() !== "") {
    return value.trim();
  }

  if (Array.isArray(value) && value.length > 0 && typeof value[0] === "string") {
    return value[0].trim();
  }

  return undefined;
}

function normalizeViewerRequest(raw: unknown): ViewerRequest {
  if (!raw || typeof raw !== "object") {
    throw new Error("Viewer request must be a JSON object.");
  }

  const record = raw as Record<string, unknown>;
  const characterId = String(record.character_id ?? "").trim();
  const modelPath = String(record.model_path ?? "").trim();
  const cameraPreset = String(record.camera_preset ?? "full_body").trim();

  if (!characterId) {
    throw new Error("Viewer request is missing character_id.");
  }

  if (!modelPath) {
    throw new Error("Viewer request is missing model_path.");
  }

  if (cameraPreset !== "full_body") {
    throw new Error(`Unsupported camera_preset: ${cameraPreset}`);
  }

  return {
    characterId,
    modelPath,
    cameraPreset
  };
}

async function readJsonFile(path: string): Promise<ViewerRequest> {
  const json = await readTextFile(path);
  return normalizeViewerRequest(JSON.parse(json));
}

async function loadBundledDefaultRequest(): Promise<ViewerRequest> {
  const bundledPath = await resolveResource("requests/example-request.json");
  return readJsonFile(bundledPath);
}

async function resolveRequestPath(requestPath: string): Promise<string> {
  if (looksAbsolutePath(requestPath)) {
    return requestPath;
  }

  return resolveResource(requestPath);
}

export async function loadViewerRequest(): Promise<ViewerRequest> {
  const defaultRequest = await loadBundledDefaultRequest();
  const matches = (await getMatches()) as CliMatchesShape;

  let request = defaultRequest;
  const requestPath = getCliStringArg(matches, "request");

  if (requestPath) {
    request = await readJsonFile(await resolveRequestPath(requestPath));
  }

  const characterIdOverride = getCliStringArg(matches, "character-id");
  const modelPathOverride = getCliStringArg(matches, "model-path");
  const cameraPresetOverride = getCliStringArg(matches, "camera-preset");

  return normalizeViewerRequest({
    character_id: characterIdOverride ?? request.characterId,
    model_path: modelPathOverride ?? request.modelPath,
    camera_preset: cameraPresetOverride ?? request.cameraPreset
  });
}

function getCliNumberArg(matches: CliMatchesShape, name: string): number | undefined {
  const value = getCliStringArg(matches, name);

  if (!value) {
    return undefined;
  }

  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : undefined;
}

function truthyCliValue(value: string | undefined): boolean {
  if (!value) {
    return false;
  }

  return ["1", "true", "yes", "embed", "embedded"].includes(value.toLowerCase());
}

export async function loadViewerRuntimeOptions(): Promise<ViewerRuntimeOptions> {
  let nativeBridge: NativeBridgeOptions = {
    embedded: false,
    shellOnly: false,
    alwaysOnTop: false
  };
  try {
    nativeBridge = await invoke<NativeBridgeOptions>("get_native_bridge_options");
  } catch (error) {
    console.warn("Native viewer bridge options were unavailable.", error);
  }

  if (nativeBridge.shellOnly) {
    return {
      embedded: nativeBridge.embedded,
      shellOnly: true,
      debugMaterials: false,
      debugGeometry: false,
      commandPath: nativeBridge.commandPath,
      statusPath: nativeBridge.statusPath,
      timingLogPath: nativeBridge.timingLogPath,
      zoom: nativeBridge.zoom,
      minDistance: nativeBridge.minDistance,
      maxDistance: nativeBridge.maxDistance,
      alwaysOnTop: nativeBridge.alwaysOnTop
    };
  }

  let matches: CliMatchesShape = {};
  try {
    matches = (await getMatches()) as CliMatchesShape;
  } catch (error) {
    console.warn("Tauri CLI matches were unavailable; using native runtime options.", error);
  }

  return {
    embedded: nativeBridge.embedded || truthyCliValue(getCliStringArg(matches, "embed")),
    shellOnly: nativeBridge.shellOnly || truthyCliValue(getCliStringArg(matches, "shell-only")),
    debugMaterials: truthyCliValue(getCliStringArg(matches, "debug-materials")),
    debugGeometry: truthyCliValue(getCliStringArg(matches, "debug-geometry")),
    commandPath: nativeBridge.commandPath ?? getCliStringArg(matches, "command-path"),
    statusPath: nativeBridge.statusPath ?? getCliStringArg(matches, "status-path"),
    timingLogPath: nativeBridge.timingLogPath ?? getCliStringArg(matches, "timing-log-path"),
    x: getCliNumberArg(matches, "x"),
    y: getCliNumberArg(matches, "y"),
    width: getCliNumberArg(matches, "width"),
    height: getCliNumberArg(matches, "height"),
    zoom: nativeBridge.zoom ?? getCliNumberArg(matches, "zoom"),
    minDistance: nativeBridge.minDistance ?? getCliNumberArg(matches, "min-distance"),
    maxDistance: nativeBridge.maxDistance ?? getCliNumberArg(matches, "max-distance"),
    alwaysOnTop: nativeBridge.alwaysOnTop || truthyCliValue(getCliStringArg(matches, "always-on-top"))
  };
}
