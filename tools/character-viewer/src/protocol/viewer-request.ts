import { resolveResource } from "@tauri-apps/api/path";
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
  x?: number;
  y?: number;
  width?: number;
  height?: number;
  alwaysOnTop: boolean;
}

interface CliArgumentValue {
  value?: string | boolean | string[] | null;
}

interface CliMatchesShape {
  args?: Record<string, CliArgumentValue>;
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
  const value = matches.args?.[name]?.value;

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
  const matches = (await getMatches()) as CliMatchesShape;

  return {
    embedded: truthyCliValue(getCliStringArg(matches, "embed")),
    x: getCliNumberArg(matches, "x"),
    y: getCliNumberArg(matches, "y"),
    width: getCliNumberArg(matches, "width"),
    height: getCliNumberArg(matches, "height"),
    alwaysOnTop: truthyCliValue(getCliStringArg(matches, "always-on-top"))
  };
}
