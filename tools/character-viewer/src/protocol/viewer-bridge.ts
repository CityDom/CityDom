import { invoke } from "@tauri-apps/api/core";

import type { CameraPreset } from "../viewer/camera";
import type { ViewerRuntimeOptions } from "./viewer-request";

export type ViewerState =
  | "cold"
  | "shell_starting"
  | "shell_ready"
  | "character_loading"
  | "character_loaded"
  | "character_warming"
  | "character_ready"
  | "visible"
  | "parked"
  | "error";

export interface ShowCharacterCommand {
  sequence: number;
  action: "show_character" | "preload_character";
  character_id: string;
  model_path: string;
  camera_preset?: CameraPreset;
}

export interface ParkCommand {
  sequence: number;
  action: "park" | "shutdown";
}

export type ViewerCommand = ShowCharacterCommand | ParkCommand;

interface ViewerStatus {
  state: ViewerState;
  timestamp: string;
  character_id?: string;
  detail?: string;
}

export interface ViewerBridge {
  timing(event: string, detail?: string): Promise<void>;
  setState(state: ViewerState, characterId?: string, detail?: string): Promise<void>;
  readNextCommand(): Promise<ViewerCommand | null>;
}

function normalizeCommand(raw: unknown): ViewerCommand | null {
  if (!raw || typeof raw !== "object") {
    return null;
  }

  const value = raw as Record<string, unknown>;
  const sequence = Number(value.sequence);
  const action = String(value.action ?? "");
  if (!Number.isFinite(sequence)) {
    return null;
  }

  if (action === "park" || action === "shutdown") {
    return { sequence, action };
  }

  if (action !== "show_character" && action !== "preload_character") {
    return null;
  }

  const characterId = String(value.character_id ?? "").trim();
  const modelPath = String(value.model_path ?? "").trim();
  if (!characterId || !modelPath) {
    return null;
  }

  return {
    sequence,
    action,
    character_id: characterId,
    model_path: modelPath,
    camera_preset: value.camera_preset === "full_body" ? "full_body" : undefined
  };
}

export function createViewerBridge(options: ViewerRuntimeOptions): ViewerBridge {
  const startedAt = performance.now();
  let lastSequence = -1;

  async function timing(event: string, detail?: string): Promise<void> {
    const elapsed = (performance.now() - startedAt).toFixed(1);
    const line = `[${new Date().toISOString()} +${elapsed}ms] ${event}${detail ? ` ${detail}` : ""}\n`;
    console.info(line.trim());
    if (!options.timingLogPath) {
      return;
    }

    try {
      await invoke("append_bridge_timing", {
        path: options.timingLogPath,
        line
      });
    } catch (error) {
      console.warn("Viewer timing log write failed.", error);
    }
  }

  async function setState(
    state: ViewerState,
    characterId?: string,
    detail?: string
  ): Promise<void> {
    const status: ViewerStatus = {
      state,
      timestamp: new Date().toISOString(),
      character_id: characterId,
      detail
    };
    if (options.statusPath) {
      try {
        await invoke("write_bridge_status", {
          path: options.statusPath,
          contents: JSON.stringify(status)
        });
      } catch (error) {
        console.warn("Viewer status write failed.", error);
      }
    }
  }

  async function readNextCommand(): Promise<ViewerCommand | null> {
    if (!options.commandPath) {
      return null;
    }

    let text: string | null;
    try {
      text = await invoke<string | null>("read_bridge_command", {
        path: options.commandPath
      });
    } catch {
      return null;
    }
    if (!text) {
      return null;
    }

    let command: ViewerCommand | null;
    try {
      command = normalizeCommand(JSON.parse(text));
    } catch {
      return null;
    }
    if (!command || command.sequence <= lastSequence) {
      return null;
    }

    lastSequence = command.sequence;
    return command;
  }

  return { timing, setState, readNextCommand };
}
