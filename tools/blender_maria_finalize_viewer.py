import os
from pathlib import Path

import bpy


OUTPUT_DIR = Path.home() / "Desktop" / "maria_production"
BAKE_SCRIPT = Path(r"H:\renpy-8.5.0-sdk\City Dom\tools\blender_bake_pbr_batch.py")
FINAL_BLEND = OUTPUT_DIR / "maria_lowpoly_skin1k_eyes.blend"
FINAL_GLB_NAME = "maria_lowpoly_skin1k_eyes.glb"


def load_bake_functions():
    os.environ["MARIA_GLTF_OUTPUT_NAME"] = FINAL_GLB_NAME
    os.environ["MARIA_GLTF_IMAGE_FORMAT"] = "AUTO"
    source = BAKE_SCRIPT.read_text(encoding="utf-8")
    source = source.rsplit("\ntry:\n    main()", 1)[0]
    namespace = {"__name__": "__main__"}
    exec(compile(source, str(BAKE_SCRIPT), "exec"), namespace)
    return namespace


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    bake = load_bake_functions()
    bake["TARGET_MODE"] = "skin_1k"
    bake["BAKE_SIZE"] = 1024
    bake["MATERIAL_BAKE_SIZES"]["cf_m_skin_head_01"] = 1024
    bake["MATERIAL_BAKE_SIZES"]["cf_m_skin_body_00"] = 1024

    bake["ensure_object_mode"]()
    bake["configure_cycles_for_bake"]()
    skin_targets = [
        ("o_head", "cf_m_skin_head_01", None),
        ("o_body", "cf_m_skin_body_00", "Body_uv1"),
    ]
    for object_name, material_name, uv_layer_name in skin_targets:
        bake["bake_target"](object_name, material_name, uv_layer_name)

    bake["apply_existing_bake"](
        "o_eyebase_L",
        "HS2Rig Eyes2 for SKLX",
        None,
        "HS2Rig Eyes2 for SKLX",
    )

    bpy.ops.wm.save_as_mainfile(filepath=str(FINAL_BLEND))
    bake["export_visible_glb"]()

    print("MARIA VIEWER FINALIZATION COMPLETE", flush=True)
    print("SAVED BLEND:", FINAL_BLEND, flush=True)
    print("EXPORTED GLB:", bake["OUT_PATH"], flush=True)
    print("VERIFY BODY TEXTURES EXPORT WITH TEXCOORD_3", flush=True)


main()
