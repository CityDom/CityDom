"""Conservative Blender optimization for the City Dom character viewer.

Preserves armatures, vertex groups, materials, and every shape key. Only known
static bracelet meshes are decimated. Exact duplicate images are consolidated
when their color-space interpretation also matches.
"""

import datetime
import hashlib
import json
import os
from pathlib import Path

import bpy


OUTPUT_DIR = Path.home() / "Desktop" / "maria_blender_optimized"
REPORT_PATH = OUTPUT_DIR / "optimization_report.json"

# These targets reduce the bracelet set from roughly 200k triangles to about
# 40k while leaving all deforming character meshes untouched.
STATIC_ACCESSORY_TARGETS = {
    "BeadedBangle.Shape": 10000,
    "SmallTwistBangle.Shape": 7000,
    "SmallTwistBangle_dup_2.Shape": 7000,
    "SmallTwistBangle_dup_3.Shape": 7000,
    "BeadedSmallBangle.Shape": 7000,
    "BigBangle.Shape": 4000,
}


def timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def triangle_count(obj):
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def shape_key_signature():
    signature = {}
    for obj in bpy.data.objects:
        if obj.type != "MESH" or not obj.data.shape_keys:
            continue
        signature[obj.name] = [key.name for key in obj.data.shape_keys.key_blocks]
    return signature


def armature_signature():
    signature = {}
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        modifiers = [modifier.name for modifier in obj.modifiers if modifier.type == "ARMATURE"]
        if modifiers:
            signature[obj.name] = {
                "modifiers": modifiers,
                "vertex_groups": sorted(group.name for group in obj.vertex_groups),
            }
    return signature


def image_bytes_and_hash(image):
    try:
        if image.packed_file:
            data = bytes(image.packed_file.data)
            return len(data), hashlib.sha256(data).hexdigest()

        path = bpy.path.abspath(image.filepath, library=image.library)
        if not path or not os.path.isfile(path):
            return 0, None

        digest = hashlib.sha256()
        size = 0
        with open(path, "rb") as source:
            while True:
                block = source.read(1024 * 1024)
                if not block:
                    break
                size += len(block)
                digest.update(block)
        return size, digest.hexdigest()
    except Exception:
        return 0, None


def image_compatibility_key(image, digest):
    return (
        digest,
        tuple(image.size[:]),
        int(image.channels),
        image.colorspace_settings.name,
        image.alpha_mode,
        image.source,
    )


def consolidate_duplicate_images(report):
    canonical_by_key = {}
    duplicates = []

    for image in list(bpy.data.images):
        _size, digest = image_bytes_and_hash(image)
        if not digest:
            continue

        key = image_compatibility_key(image, digest)
        canonical = canonical_by_key.get(key)
        if canonical is None:
            canonical_by_key[key] = image
            continue

        if canonical == image:
            continue

        duplicate_record = {
            "duplicate": image.name,
            "canonical": canonical.name,
            "users_before": int(image.users),
            "colorspace": image.colorspace_settings.name,
        }
        image.user_remap(canonical)
        duplicate_record["users_after"] = int(image.users)
        if image.users == 0:
            bpy.data.images.remove(image)
            duplicate_record["removed"] = True
        else:
            duplicate_record["removed"] = False
        duplicates.append(duplicate_record)

    report["consolidated_images"] = duplicates


def remove_zero_user_datablocks(report):
    removed_materials = []
    removed_images = []

    for material in list(bpy.data.materials):
        if material.users == 0:
            removed_materials.append(material.name)
            bpy.data.materials.remove(material)

    for image in list(bpy.data.images):
        if image.users != 0 or image.source not in {"FILE", "GENERATED"}:
            continue
        removed_images.append(image.name)
        bpy.data.images.remove(image)

    report["removed_zero_user_materials"] = removed_materials
    report["removed_zero_user_images"] = removed_images


def has_armature_modifier(obj):
    return any(modifier.type == "ARMATURE" for modifier in obj.modifiers)


def decimate_static_accessories(report):
    results = []
    bpy.ops.object.mode_set(mode="OBJECT") if bpy.context.object and bpy.context.object.mode != "OBJECT" else None
    bpy.ops.object.select_all(action="DESELECT")

    for object_name, target_triangles in STATIC_ACCESSORY_TARGETS.items():
        obj = bpy.data.objects.get(object_name)
        record = {"object": object_name, "target_triangles": target_triangles}
        if obj is None or obj.type != "MESH":
            record.update({"status": "skipped", "reason": "mesh object not found"})
            results.append(record)
            continue
        if obj.data.shape_keys:
            record.update({"status": "skipped", "reason": "object has shape keys"})
            results.append(record)
            continue
        if has_armature_modifier(obj):
            record.update({"status": "skipped", "reason": "object has an armature modifier"})
            results.append(record)
            continue

        before = triangle_count(obj)
        record["triangles_before"] = before
        if before <= target_triangles:
            record.update({"status": "unchanged", "triangles_after": before})
            results.append(record)
            continue

        if obj.data.users > 1:
            obj.data = obj.data.copy()

        ratio = max(0.05, min(1.0, target_triangles / float(before)))
        modifier = obj.modifiers.new(name="CityDom_ConservativeDecimate", type="DECIMATE")
        modifier.decimate_type = "COLLAPSE"
        modifier.ratio = ratio
        modifier.use_collapse_triangulate = True

        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)
        try:
            bpy.ops.object.modifier_apply(modifier=modifier.name)
            after = triangle_count(obj)
            record.update(
                {
                    "status": "decimated",
                    "ratio": ratio,
                    "triangles_after": after,
                    "triangles_saved": before - after,
                }
            )
        except Exception as exc:
            if modifier.name in obj.modifiers:
                obj.modifiers.remove(modifier)
            record.update({"status": "failed", "reason": repr(exc)})
        finally:
            obj.select_set(False)
        results.append(record)

    report["static_accessories"] = results


def total_scene_triangles():
    return sum(
        triangle_count(obj)
        for obj in bpy.context.scene.objects
        if obj.type == "MESH"
    )


def save_baseline_copy():
    baseline_path = OUTPUT_DIR / ("maria_baseline_%s.blend" % timestamp())
    bpy.ops.wm.save_as_mainfile(filepath=str(baseline_path), copy=True)
    return baseline_path


def save_optimized_copy():
    optimized_path = OUTPUT_DIR / "maria_optimized_work.blend"
    bpy.ops.wm.save_as_mainfile(filepath=str(optimized_path))
    return optimized_path


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    before_shape_keys = shape_key_signature()
    before_armatures = armature_signature()
    report = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "blender_version": bpy.app.version_string,
        "source_blend": bpy.data.filepath,
        "triangles_before": total_scene_triangles(),
        "shape_key_objects_before": len(before_shape_keys),
        "shape_keys_before": sum(len(keys) for keys in before_shape_keys.values()),
    }

    baseline_path = save_baseline_copy()
    report["baseline_blend"] = str(baseline_path)

    decimate_static_accessories(report)
    consolidate_duplicate_images(report)
    remove_zero_user_datablocks(report)

    after_shape_keys = shape_key_signature()
    after_armatures = armature_signature()
    if before_shape_keys != after_shape_keys:
        raise RuntimeError("Shape-key validation failed; optimized file was not saved.")
    if before_armatures != after_armatures:
        raise RuntimeError("Armature/vertex-group validation failed; optimized file was not saved.")

    report["triangles_after"] = total_scene_triangles()
    report["triangles_saved"] = report["triangles_before"] - report["triangles_after"]
    report["shape_keys_after"] = sum(len(keys) for keys in after_shape_keys.values())
    report["shape_keys_preserved"] = True
    report["armatures_and_vertex_groups_preserved"] = True

    optimized_path = save_optimized_copy()
    report["optimized_blend"] = str(optimized_path)
    REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("City Dom conservative optimization complete")
    print("  Baseline: %s" % baseline_path)
    print("  Optimized: %s" % optimized_path)
    print("  Report: %s" % REPORT_PATH)
    print("  Triangles: %d -> %d" % (report["triangles_before"], report["triangles_after"]))
    print("  Shape keys preserved: %d" % report["shape_keys_after"])
    print("  Inspect all bracelets closely before exporting the optimized GLB.")


main()
