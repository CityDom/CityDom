# City Dom Character Viewer Prototype

This is the first standalone Tauri-based 3D viewer prototype for the Ren'Py project. It is intentionally small and only proves the offline sidecar viewer architecture.

## First milestone

On launch, the app:

1. Loads a viewer request.
2. Resolves one bundled local GLB.
3. Opens a single native Tauri window.
4. Renders the model with neutral lighting and a neutral background.
5. Supports orbit, zoom, and reset camera.

The app does not do outfit switching, body zones, animation playback, or Ren'Py integration yet.

## Version 1 request contract

Primary contract: a tiny JSON file.

```json
{
  "character_id": "mhyrorin",
  "model_path": "characters/mhyrorin/Base.glb",
  "camera_preset": "full_body"
}
```

Fields:

- `character_id`: opaque string used for display and later integration.
- `model_path`: resource-relative path inside `assets_3d/`.
- `camera_preset`: currently only `full_body`.

CLI support is included for prototype convenience:

- `--request <path>`
- `--character-id <value>`
- `--model-path <value>`
- `--camera-preset <value>`

Precedence:

1. Start from bundled `requests/example-request.json`.
2. If `--request` is provided, load that JSON instead.
3. Apply any direct CLI overrides last.

## Files the prototype expects

- `assets_3d/characters/mhyrorin/Base.glb`
- `requests/example-request.json`

The scaffold includes the request JSON and a placeholder character manifest, but not the real GLB. Drop the exported GLB at the path above before the first real run.

## Controls

- Left mouse drag: orbit
- Mouse wheel: zoom
- `R` or the toolbar button: reset camera

## Success criteria

The first milestone is successful when:

- `npm install`
- `npm run tauri:dev`
- the app opens a native window
- it loads the bundled GLB without network access
- the model can be rotated, zoomed, and reset

Packaging installers is intentionally out of scope for this first scaffold. The current config is aimed at `tauri dev` and the first local executable path. When you move to packaged builds, add the app icon set and switch `bundle.active` back on.

## Prototype stack

- Tauri 2
- Vite
- TypeScript
- Three.js
- `GLTFLoader`
- `OrbitControls`

Why this stack:

- Vite keeps iteration fast during development.
- TypeScript keeps the request contract and viewer boundaries explicit.
- Three.js is enough for the current viewer scope.
- Tauri bundles the desktop app and local resources without a shipped browser-tab workflow.

## Bundled asset strategy

- `assets_3d/` is bundled as a Tauri resource directory.
- `requests/` is bundled as a Tauri resource directory.
- Both directories currently live at the repo root, so `src-tauri/tauri.conf.json` points to them with `../../../assets_3d/` and `../../../requests/`.
- The frontend resolves resource paths through Tauri and reads the files through the fs plugin.
- The GLB is read as bytes and loaded through a Blob URL, which keeps the first milestone simple for single-file `.glb` assets.

## Development workflow

Development:

- Use Vite hot reload through `npm run tauri:dev`.
- Replace placeholder manifests with real GLBs as they are exported.
- Use `--request` or direct CLI overrides when you want to test another model contract.

Shipped workflow later:

- Ren'Py launches the packaged viewer executable.
- Ren'Py passes a request file or direct args.
- The player sees only the game and the viewer window, fully offline.

## Folder layout

```text
tools/character-viewer/
  index.html
  package.json
  tsconfig.json
  vite.config.ts
  src/
    main.ts
    protocol/
      viewer-request.ts
    viewer/
      camera.ts
      controls.ts
      model-loader.ts
      scene.ts
  src-tauri/
    build.rs
    Cargo.toml
    tauri.conf.json
    capabilities/
      default.json
    src/
      main.rs
assets_3d/
  characters/
    mhyrorin/
      manifest.json
requests/
  example-request.json
```

## Current limitations

- The prototype assumes a self-contained `.glb`. If later exports depend on external textures, the loader strategy should move from Blob URL loading to resource URL resolution for the whole asset tree.
- There is no Ren'Py launcher code yet.
- There is no result channel back to the game yet.
