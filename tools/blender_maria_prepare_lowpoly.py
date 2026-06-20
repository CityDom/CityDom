import os
from pathlib import Path

import bpy


OUTPUT_DIR = Path.home() / "Desktop" / "maria_production"
FINAL_BLEND = OUTPUT_DIR / "maria_lowpoly_sklx_baked.blend"

CORRECTION_SCRIPTS = [
    r"H:\hs2_blender_export\tools\apply_sklx_hair_colors.py",
    r"H:\hs2_blender_export\tools\apply_sklx_hs2rig_eye_material.py",
    r"H:\hs2_blender_export\tools\apply_sklx_safe_cleanup.py",
    r"H:\hs2_blender_export\tools\apply_sklx_material_cleanup.py",
]

OPTIMIZATION_SCRIPTS = [
    r"H:\renpy-8.5.0-sdk\City Dom\tools\blender_optimize_character_safe.py",
    r"H:\renpy-8.5.0-sdk\City Dom\tools\blender_optimize_character_level2.py",
]


def run_script(path):
    print("RUNNING:", path, flush=True)
    source = Path(path).read_text(encoding="utf-8")
    exec(compile(source, path, "exec"), {"__name__": "__main__"})


def triangle_count(obj):
    return sum(len(poly.vertices) - 2 for poly in obj.data.polygons)


def scene_triangles():
    return sum(
        triangle_count(obj)
        for obj in bpy.context.scene.objects
        if obj.type == "MESH"
    )


def shape_key_count():
    return sum(
        len(obj.data.shape_keys.key_blocks)
        for obj in bpy.context.scene.objects
        if obj.type == "MESH" and obj.data.shape_keys
    )


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    triangles_before = scene_triangles()
    shape_keys_before = shape_key_count()

    for path in CORRECTION_SCRIPTS:
        run_script(path)

    for path in OPTIMIZATION_SCRIPTS:
        run_script(path)

    triangles_after = scene_triangles()
    shape_keys_after = shape_key_count()
    if shape_keys_after != shape_keys_before:
        raise RuntimeError(
            "Shape-key count changed during optimization: %d -> %d"
            % (shape_keys_before, shape_keys_after)
        )

    texture_dir = OUTPUT_DIR / "sklx_textures"
    texture_dir.mkdir(parents=True, exist_ok=True)
    if hasattr(bpy.context.scene, "sna_texture_path"):
        bpy.context.scene.sna_texture_path = str(texture_dir)

    print("STARTING SKLX TEXTURE BAKER", flush=True)
    result = bpy.ops.sna.sklx_texture_baker_c3310()
    if "FINISHED" not in result:
        raise RuntimeError("SKLX Texture Baker did not finish: %r" % (result,))

    baked_images = [
        image
        for image in bpy.data.images
        if "_BK" in image.name and image.size[0] > 0 and image.size[1] > 0
    ]
    if not baked_images:
        raise RuntimeError("SKLX finished without producing loaded _BK images.")

    bpy.ops.wm.save_as_mainfile(filepath=str(FINAL_BLEND))
    print("MARIA LOW-POLY SKLX PREPARATION COMPLETE", flush=True)
    print("TRIANGLES: %d -> %d" % (triangles_before, triangles_after), flush=True)
    print("SHAPE KEYS:", shape_keys_after, flush=True)
    print("LOADED SKLX BK IMAGES:", len(baked_images), flush=True)
    print("SAVED:", FINAL_BLEND, flush=True)


main()
