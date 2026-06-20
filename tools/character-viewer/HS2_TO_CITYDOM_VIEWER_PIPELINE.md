# HS2 to City Dom Character Viewer Pipeline

This document records the working Maria pipeline as of 2026-06-20. The order matters. Do not replace category-specific conversion stages with one generic bake.

## Working Result

- Blender source: `C:\Users\mihai\Desktop\maria_production\maria_production_baked.blend`
- Final 1K test blend: `C:\Users\mihai\Desktop\maria_production\maria_skin_1k_uv3_correct_eyes.blend`
- Final 1K test GLB: `C:\Users\mihai\Desktop\maria_pbr_bake\maria_skin_1k_uv3_correct_eyes.glb`
- Standalone viewer asset: `tools\character-viewer\src-tauri\target\release\assets_3d\characters\maria\Base.glb`
- Game viewer asset: `tools\character-viewer\src-tauri\target_warm\release\assets_3d\characters\maria\Base.glb`

The standalone debug viewer is the test target. Do not replace the game asset until the debug result is approved.

## 1. Import and Initial Material Corrections

Import the HS2/Gray FBX through SKLX. Confirm the character looks correct in Blender Material Preview before baking.

Run these scripts, in this order:

```python
exec(open(r"H:\hs2_blender_export\tools\apply_sklx_hair_colors.py", encoding="utf-8").read())
exec(open(r"H:\hs2_blender_export\tools\apply_sklx_hs2rig_eye_material.py", encoding="utf-8").read())
exec(open(r"H:\hs2_blender_export\tools\apply_sklx_safe_cleanup.py", encoding="utf-8").read())
exec(open(r"H:\hs2_blender_export\tools\apply_sklx_material_cleanup.py", encoding="utf-8").read())
```

For a fresh Maria import, the corrections, both geometry optimizers, SKLX bake, validation, and save are now wrapped in one command:

```python
exec(open(r"H:\renpy-8.5.0-sdk\City Dom\tools\blender_maria_prepare_lowpoly.py", encoding="utf-8").read())
```

This is the preferred command. The individual commands below remain documented for diagnosis.

What they do:

- Apply hair colors from the HS2 appearance export.
- Replace the broken SKLX eye interpretation with the known-good HS2Rig eye material.
- Hide tears without modifying eyelashes, eyeshadow, or eyebase materials.
- Apply conservative glasses, nails, and material cleanup.

## 2. Geometry Optimization

Run the conservative optimizer, then level 2:

```python
exec(open(r"H:\renpy-8.5.0-sdk\City Dom\tools\blender_optimize_character_safe.py", encoding="utf-8").read())
exec(open(r"H:\renpy-8.5.0-sdk\City Dom\tools\blender_optimize_character_level2.py", encoding="utf-8").read())
```

These commands must run before the SKLX Texture Baker. The wrapper in section 1 includes both. Expected Maria result is approximately 315K to 124K triangles with all 150 morph targets preserved.

Maria went from about 315K triangles to about 124K while preserving one skin and 150 morph targets. These optimization scripts currently use Maria-specific output names and must be parameterized before using them as unattended production tools for other characters.

## 3. SKLX Native Texture Bake

Use SKLX's own baker for clothes and accessories:

```python
bpy.ops.sna.sklx_texture_baker_c3310()
```

SKLX produces these maps for supported materials:

- `_Diffuse_BK`
- `_Normal_BK`
- `_RoughSpecMetal_BK`
- `_EmissionColor_BK`

Observed resolutions are material-dependent. Examples:

- Camisole: 1024x512
- Bracelet: 1024x1024
- Watch: 512x512
- Other clothes/accessories: generally 512 to 2048

SKLX native baking is correct for clothes and accessories. It does not convert the complex head/body skin shader into valid glTF PBR.

## 4. Skin-Only Bake

Bake only these materials through `blender_bake_pbr_batch.py`:

- `cf_m_skin_head_01`
- `cf_m_skin_body_00`

Components:

- Base color
- Tangent-space normal
- Roughness

The tested lower resolution is 1024x1024. It was visually indistinguishable from the earlier 2048x2048 skin bake in the viewer. Keep 1K unless a later close-up demonstrates visible degradation.

After `blender_maria_prepare_lowpoly.py` finishes, run the final skin/eye/export stage:

```python
exec(open(r"H:\renpy-8.5.0-sdk\City Dom\tools\blender_maria_finalize_viewer.py", encoding="utf-8").read())
```

This saves `C:\Users\mihai\Desktop\maria_production\maria_lowpoly_skin1k_eyes.blend` and exports `C:\Users\mihai\Desktop\maria_pbr_bake\maria_lowpoly_skin1k_eyes.glb`.

Critical UV requirement:

- Head uses its normal/default UV set.
- Body is baked with `Body_uv1`.
- On Maria's merged `o_head` mesh, `Body_uv1` is UV index 3.
- The exported body base-color, metallic/roughness, and normal texture entries must all contain `texCoord: 3`.

The material generator now creates a Blender `ShaderNodeUVMap` node for requested bake UV layers. Do not remove it. Without it, glTF omits `texCoord`, Three.js uses `TEXCOORD_0`, and the body appears brick/orange even though the baked PNG is correct.

## 5. Eyes

Do not export the live SKLX/HS2Rig eye shader directly. Blender's glTF exporter otherwise chooses `ShadeScleraTex` as the base map and the eyes break.

Use the known-good PBR eye outputs:

- `HS2Rig_Eyes2_for_SKLX_basecolor.png`
- `HS2Rig_Eyes2_for_SKLX_normal.png`
- `HS2Rig_Eyes2_for_SKLX_roughness.png`

The final GLB material must be named like `HS2Rig Eyes2 for SKLX__pbr_baked` and reference those maps.

Fresh Blender imports may rename the assigned material to `HS2Rig Eyes2 for SKLX.001`. The finalizer must still load the canonical filenames above. `load_existing_bake_images()` therefore accepts a separate canonical bake-material name; do not derive the filenames from Blender's `.001` alias.

## 6. Viewer Material Defaults

Maria's exact final 32-material profile is preserved at:

`tools\character-viewer\assets_3d\characters\maria\material-profile.json`

Important final settings:

- Eyelashes: black, roughness 0.5, opacity 0.95, transparent, alpha test 0.35, only base map enabled.
- Socks: opacity 0.98, transparent, alpha test 0.02, depth write disabled, front side, normal strength 0.35, low environment intensity.
- Body: white material factor, no tint, normal map disabled, roughness map disabled.
- Head: white material factor, normal map disabled.
- Hair: HS2-exported colors; roughness map disabled and normal strength zero where recorded.
- Clothes/accessories: use their SKLX `_BK` maps plus saved material controls.

Defaults must match both native SKLX names (for example `cf_m_socks14`) and `__pbr_baked` names where both forms can occur.

## 7. GLB Validation

Before installing an export, verify:

- No texture entry lacks a source.
- One skin remains.
- All 150 Maria morph targets remain.
- Body base color, roughness, and normal use `texCoord: 3`.
- Eyes reference `HS2Rig_Eyes2_for_SKLX_*`, not sclera/shade source maps.
- Clothes/accessories reference SKLX `_BK` textures.
- No unexpected material uses a missing/zero-size Blender image.

## 8. Viewer Build and Test

Build the standalone debug viewer:

```powershell
$env:CARGO_TARGET_DIR="H:\renpy-8.5.0-sdk\City Dom\tools\character-viewer\src-tauri\target"
npx tauri build --no-bundle
```

After every build, copy the test GLB into the target's release resources again because the build can restore the source asset.

Launch:

```powershell
& "H:\renpy-8.5.0-sdk\City Dom\tools\character-viewer\src-tauri\target\release\city-dom-character-viewer.exe" --character-id maria --model-path characters/maria/Base.glb --debug-materials true
```

Only after approval should the GLB and rebuilt executable be copied to `target_warm` for the game.

## 9. Optimization After Correctness

- Keep PNG during material/UV validation.
- Convert selected textures to WebP only after the PNG GLB is visually correct.
- Lossy WebP quality 95 worked for suitable color maps.
- Use lossless WebP for normal and roughness data.
- Keep appearance-critical skin, face, eye, and eyelash color maps as PNG unless independently verified.
- Blender's forced all-WebP export produced invalid empty texture references. Use mixed PNG/WebP and validate the resulting GLB.
- The approved all-lossless-WebP repack reduced Maria from 73.30 MiB to 47.53 MiB without changing dimensions or decoded appearance.
- The approved low-poly geometry contains 124,006 triangles, one skin, and 150 morph targets.
- Install the official tools once:

```powershell
npm install --global @gltf-transform/cli
```

KTX2 encoding also requires the official Khronos KTX-Software package and `toktx.exe` on `PATH`.

Exact texture-only deduplication, deliberately preserving geometry/accessors/materials/skins:

```powershell
gltf-transform dedup input.glb maria_dedup.glb --accessors false --materials false --meshes false --skins false --textures true
```

Maria's tested conservative selective reduction leaves hair, eyes, skin, socks, shirt, and pants unchanged:

```powershell
gltf-transform resize maria_dedup.glb step1.glb --pattern '1_WetLook_BootL_*' --width 1024 --height 2048
gltf-transform resize step1.glb step2.glb --pattern '{acs_*,ring*}' --width 512 --height 512
gltf-transform resize step2.glb step3.glb --pattern '{c_m_tang_*,c_m_tooth_*}' --width 512 --height 512
gltf-transform resize step3.glb maria_selective.glb --pattern 'c_m_eyelashes_*' --width 1024 --height 1024
```

Remove texture slots that the saved viewer material profile always disables, then prune orphaned resources and convert truly solid textures into material factors:

```powershell
python "H:\renpy-8.5.0-sdk\City Dom\tools\strip_viewer_disabled_maps.py" maria_selective.glb maria_cleanup_stage.glb --profile "H:\renpy-8.5.0-sdk\City Dom\tools\character-viewer\assets_3d\characters\maria\material-profile.json"
gltf-transform prune maria_cleanup_stage.glb maria_clean.glb --keep-attributes true --keep-indices true --keep-leaves true --keep-solid-textures false
```

This cleanup is profile-driven. For Maria it removes seven normal-map references whose final `normalScale` is zero, then pruning removes a total of 20 orphaned/solid texture resources. It also validates the known glasses frame/lens split.

High-quality UASTC KTX2 conversion:

```powershell
$env:PATH='C:\Program Files\KTX-Software\bin;'+$env:PATH
gltf-transform uastc maria_clean.glb maria_clean_uastc.glb --level 2 --rdo --rdo-lambda 0.5 --zstd 18 --jobs 8
```

Apply lossless Meshopt **after KTX2** from the character-viewer directory:

```powershell
node ".\scripts\compress-meshopt-lossless.mjs" maria_clean_uastc.glb maria_final_meshopt_ktx2.glb
node ".\scripts\validate-accessors-exact.mjs" maria_clean.glb maria_final_meshopt_ktx2.glb
```

Order is mandatory: cleanup -> KTX2 -> lossless Meshopt. Running KTX2 after Meshopt decodes and discards the existing Meshopt compression.

Do not substitute `gltf-transform meshopt`. Its broader reorder/quantize pipeline changed Maria from one skin to 18 skins. The local `compress-meshopt-lossless.mjs` script registers compression without quantizing attributes. Validation requires byte-exact decoded non-index accessors and topology-equivalent triangle indices.

Tested June 20, 2026 results:

- Corrected low-poly PNG GLB: 64.89 MB.
- Texture-only deduplicated PNG GLB: 64.26 MB, 103 images reduced to 78 exact unique images.
- Deduplicated UASTC GLB without resizing: 51.08 MB.
- Selectively reduced UASTC GLB: 42.12 MB.
- Profile-cleaned PNG GLB: 46.06 MB and 58 unique images.
- Profile-cleaned UASTC GLB: 38.30 MB.
- Final profile-cleaned UASTC + lossless Meshopt GLB: 29.04 MB.
- Final GLB retains 124,006 triangles, one skin, 150 morph targets, 36 meshes, and body base/MR texture coordinates 3/3. The body normal texture is intentionally removed because the approved profile sets its strength to zero.
- Cold GLB parse/load improved from approximately 1.11 seconds to 0.81 seconds in the local smoke test.

The viewer registers both `KTX2Loader` and `MeshoptDecoder`. It detects KTX2 support using its actual renderer and bundles Three.js's `basis_transcoder.js` and `basis_transcoder.wasm` from `public/basis/`. The final model will not load in older viewer executables lacking either decoder.

## Known Failure Modes

- Brick/orange body: body texture exported without `texCoord: 3`.
- Broken eyes/yellow sclera: live eye shader exported instead of the HS2Rig PBR eye maps.
- White accessories: SKLX baker was skipped, or source textures were missing/zero-size.
- Opaque black socks: viewer treated lace as opaque/hard cutout.
- Red eyelashes: saved black eyelash default did not match the native material name.
- Frame opacity follows lens opacity: both glasses meshes were classified as lenses because generic `"glass"` matching also matched `o_glasses_*`. The cleanup rule now assigns `o_glasses_typeH_00_03` to `HS2 Glasses Frame` and the `_r` mesh to `HS2 Glasses Lens`. This is a material-assignment fix and does not require rebaking textures.
- Extreme zoom: fixed absolute camera distance was used with a differently scaled GLB. Prefer bounds-based framing.
- Regressed materials after rebuilding: the build recopied an older source `Base.glb` into the release resource folder.
- Meshopt output has 18 skins: the broad `gltf-transform meshopt` command was used. Reject it and use the local lossless compression script instead.

## Production Direction

The final reusable pipeline must automate category-specific handling:

1. Import and HS2 correction scripts.
2. Geometry optimization with character-parameterized output paths.
3. SKLX bake for clothes/accessories.
4. 1K skin-only PBR bake with preserved UV bindings.
5. HS2Rig PBR eye conversion.
6. Character material-profile import.
7. GLB export and structural validation.
8. Optional mixed WebP optimization.
9. Debug viewer installation, visual approval, then game installation.

Do not return to one generic bake for every material category.
