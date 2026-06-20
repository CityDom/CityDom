"""Second conservative static-accessory optimization pass.

Run only after blender_optimize_character_safe.py. Armature-driven meshes and
all meshes with shape keys are rejected automatically.
"""

import datetime
import json
from pathlib import Path

import bpy


OUTPUT_DIR = Path.home() / "Desktop" / "maria_blender_optimized"
REPORT_PATH = OUTPUT_DIR / "optimization_level2_report.json"

STATIC_TARGETS = {
    "BeadedBangle.Shape": 6000,
    "SmallTwistBangle.Shape": 4000,
    "SmallTwistBangle_dup_2.Shape": 4000,
    "SmallTwistBangle_dup_3.Shape": 4000,
    "BeadedSmallBangle.Shape": 4000,
    "BigBangle.Shape": 2500,
    "SimpleBangle.Shape": 1500,
    "SimpleBangle_dup_2.Shape": 1500,
    "o_glasses_typeH_00_03": 2000,
    "tokei2_de_tokei2": 1000,
    "ring6.Shape": 1100,
    "ring10.Shape": 800,
}


def triangle_count(obj):
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def shape_key_signature():
    return {
        obj.name: [key.name for key in obj.data.shape_keys.key_blocks]
        for obj in bpy.data.objects
        if obj.type == "MESH" and obj.data.shape_keys
    }


def armature_signature():
    result = {}
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        modifiers = [modifier.name for modifier in obj.modifiers if modifier.type == "ARMATURE"]
        if modifiers:
            result[obj.name] = {
                "modifiers": modifiers,
                "vertex_groups": sorted(group.name for group in obj.vertex_groups),
            }
    return result


def total_triangles():
    return sum(
        triangle_count(obj)
        for obj in bpy.context.scene.objects
        if obj.type == "MESH"
    )


def prepare_object_mode():
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="DESELECT")


def decimate_object(obj, target):
    before = triangle_count(obj)
    if before <= target:
        return {
            "object": obj.name,
            "status": "unchanged",
            "triangles_before": before,
            "triangles_after": before,
            "target_triangles": target,
        }

    if obj.data.shape_keys:
        return {"object": obj.name, "status": "skipped", "reason": "shape keys present"}
    if any(modifier.type == "ARMATURE" for modifier in obj.modifiers):
        return {"object": obj.name, "status": "skipped", "reason": "armature modifier present"}

    if obj.data.users > 1:
        obj.data = obj.data.copy()

    ratio = max(0.05, min(1.0, target / float(before)))
    modifier = obj.modifiers.new("CityDom_Level2_Decimate", "DECIMATE")
    modifier.decimate_type = "COLLAPSE"
    modifier.ratio = ratio
    modifier.use_collapse_triangulate = True

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    try:
        bpy.ops.object.modifier_apply(modifier=modifier.name)
        after = triangle_count(obj)
        return {
            "object": obj.name,
            "status": "decimated",
            "target_triangles": target,
            "ratio": ratio,
            "triangles_before": before,
            "triangles_after": after,
            "triangles_saved": before - after,
        }
    except Exception as exc:
        if modifier.name in obj.modifiers:
            obj.modifiers.remove(modifier)
        return {"object": obj.name, "status": "failed", "reason": repr(exc)}
    finally:
        obj.select_set(False)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    before_shape_keys = shape_key_signature()
    before_armatures = armature_signature()
    before_triangles = total_triangles()

    backup_path = OUTPUT_DIR / (
        "maria_level1_backup_%s.blend" % datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    )
    bpy.ops.wm.save_as_mainfile(filepath=str(backup_path), copy=True)

    prepare_object_mode()
    operations = []
    for object_name, target in STATIC_TARGETS.items():
        obj = bpy.data.objects.get(object_name)
        if obj is None or obj.type != "MESH":
            operations.append(
                {"object": object_name, "status": "skipped", "reason": "mesh object not found"}
            )
            continue
        operations.append(decimate_object(obj, target))

    after_shape_keys = shape_key_signature()
    after_armatures = armature_signature()
    if before_shape_keys != after_shape_keys:
        raise RuntimeError("Shape-key validation failed; level-2 file was not saved.")
    if before_armatures != after_armatures:
        raise RuntimeError("Armature/vertex-group validation failed; level-2 file was not saved.")

    after_triangles = total_triangles()
    optimized_path = OUTPUT_DIR / "maria_optimized_level2.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(optimized_path))

    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_blend": str(backup_path),
        "optimized_blend": str(optimized_path),
        "triangles_before": before_triangles,
        "triangles_after": after_triangles,
        "triangles_saved": before_triangles - after_triangles,
        "shape_keys_preserved": len(before_shape_keys) == len(after_shape_keys),
        "shape_key_count": sum(len(keys) for keys in after_shape_keys.values()),
        "armatures_and_vertex_groups_preserved": before_armatures == after_armatures,
        "operations": operations,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("City Dom level-2 optimization complete")
    print("  Backup: %s" % backup_path)
    print("  Optimized: %s" % optimized_path)
    print("  Report: %s" % REPORT_PATH)
    print("  Triangles: %d -> %d" % (before_triangles, after_triangles))
    print("  Shape keys preserved: %d" % report["shape_key_count"])
    print("  Inspect bracelets, glasses, watch and rings closely.")


main()
