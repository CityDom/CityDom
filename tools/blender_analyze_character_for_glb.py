"""Analyze the current Blender character scene without modifying it."""

import collections
import datetime
import hashlib
import json
import os
from pathlib import Path

import bpy


OUTPUT_DIR = Path(
    os.environ.get(
        "CITYDOM_CHARACTER_ANALYSIS_DIR",
        str(Path.home() / "Desktop" / "maria_blender_analysis"),
    )
)
REPORT_JSON = OUTPUT_DIR / "character_analysis.json"
REPORT_TEXT = OUTPUT_DIR / "character_analysis.txt"


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as source:
        while True:
            block = source.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def image_source_info(image):
    width, height = image.size[:]
    absolute_path = ""
    file_size = 0
    content_hash = None
    hash_error = None

    try:
        absolute_path = bpy.path.abspath(image.filepath, library=image.library)
    except Exception:
        absolute_path = bpy.path.abspath(image.filepath)

    try:
        if image.packed_file:
            data = bytes(image.packed_file.data)
            file_size = len(data)
            content_hash = hashlib.sha256(data).hexdigest()
        elif absolute_path and os.path.isfile(absolute_path):
            file_size = os.path.getsize(absolute_path)
            content_hash = sha256_file(absolute_path)
    except Exception as exc:
        hash_error = repr(exc)

    # Three.js commonly uploads decoded images as four-channel textures.
    gpu_bytes_rgba8 = int(width) * int(height) * 4
    gpu_bytes_with_mips = int(gpu_bytes_rgba8 * 4 / 3)

    return {
        "name": image.name,
        "source": image.source,
        "filepath": image.filepath,
        "absolute_path": absolute_path,
        "exists": bool(absolute_path and os.path.isfile(absolute_path)),
        "packed": bool(image.packed_file),
        "width": int(width),
        "height": int(height),
        "channels": int(image.channels),
        "colorspace": image.colorspace_settings.name,
        "alpha_mode": image.alpha_mode,
        "users": int(image.users),
        "file_bytes": file_size,
        "sha256": content_hash,
        "hash_error": hash_error,
        "estimated_gpu_bytes_rgba8": gpu_bytes_rgba8,
        "estimated_gpu_bytes_with_mips": gpu_bytes_with_mips,
    }


def material_info(material):
    image_nodes = []
    if material and material.use_nodes and material.node_tree:
        for node in material.node_tree.nodes:
            if node.type != "TEX_IMAGE":
                continue
            image_nodes.append(
                {
                    "node": node.name,
                    "label": node.label,
                    "image": node.image.name if node.image else None,
                    "interpolation": node.interpolation,
                    "extension": node.extension,
                }
            )

    return {
        "name": material.name,
        "users": int(material.users),
        "use_nodes": bool(material.use_nodes),
        "blend_method": getattr(material, "surface_render_method", None),
        "image_nodes": image_nodes,
    }


def shape_key_info(obj):
    if not obj.data.shape_keys:
        return []

    animation_data = obj.data.shape_keys.animation_data
    driven_paths = set()
    if animation_data and animation_data.drivers:
        driven_paths = {driver.data_path for driver in animation_data.drivers}

    keys = []
    for index, key in enumerate(obj.data.shape_keys.key_blocks):
        data_path = 'key_blocks["%s"].value' % key.name.replace('"', '\\"')
        keys.append(
            {
                "index": index,
                "name": key.name,
                "value": float(key.value),
                "slider_min": float(key.slider_min),
                "slider_max": float(key.slider_max),
                "mute": bool(key.mute),
                "relative_key": key.relative_key.name if key.relative_key else None,
                "driven": data_path in driven_paths,
            }
        )
    return keys


def mesh_object_info(obj):
    mesh = obj.data
    mesh.calc_loop_triangles()
    materials = [slot.material.name if slot.material else None for slot in obj.material_slots]
    shape_keys = shape_key_info(obj)

    return {
        "name": obj.name,
        "data_name": mesh.name,
        "collection_names": [collection.name for collection in obj.users_collection],
        "visible_viewport": bool(obj.visible_get()),
        "hide_viewport": bool(obj.hide_viewport),
        "hide_render": bool(obj.hide_render),
        "vertices": len(mesh.vertices),
        "edges": len(mesh.edges),
        "polygons": len(mesh.polygons),
        "triangles": len(mesh.loop_triangles),
        "uv_layers": [layer.name for layer in mesh.uv_layers],
        "color_attributes": [attribute.name for attribute in mesh.color_attributes],
        "materials": materials,
        "modifiers": [
            {
                "name": modifier.name,
                "type": modifier.type,
                "show_viewport": bool(modifier.show_viewport),
                "show_render": bool(modifier.show_render),
            }
            for modifier in obj.modifiers
        ],
        "shape_keys": shape_keys,
        "shape_key_count": len(shape_keys),
        "active_shape_key_count": sum(
            1 for key in shape_keys[1:] if abs(key["value"]) > 0.000001
        ),
        "estimated_shape_key_position_bytes": max(0, len(shape_keys) - 1)
        * len(mesh.vertices)
        * 3
        * 4,
    }


def format_mib(byte_count):
    return byte_count / (1024 * 1024)


def build_report():
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    objects = [mesh_object_info(obj) for obj in mesh_objects]
    images = [image_source_info(image) for image in bpy.data.images]
    materials = [material_info(material) for material in bpy.data.materials]

    hashes = collections.defaultdict(list)
    for image in images:
        if image["sha256"]:
            hashes[image["sha256"]].append(image["name"])
    duplicate_groups = [names for names in hashes.values() if len(names) > 1]

    total_triangles = sum(obj["triangles"] for obj in objects)
    total_vertices = sum(obj["vertices"] for obj in objects)
    total_shape_keys = sum(obj["shape_key_count"] for obj in objects)
    total_image_file_bytes = sum(image["file_bytes"] for image in images)
    total_gpu_bytes = sum(image["estimated_gpu_bytes_with_mips"] for image in images)

    recommendations = []
    if duplicate_groups:
        recommendations.append("Consolidate exact duplicate images before export.")
    if total_shape_keys > 20:
        recommendations.append(
            "Review shape keys. Bake the current appearance before removing keys only if runtime expressions are not required."
        )
    if any(max(image["width"], image["height"]) >= 2048 for image in images):
        recommendations.append(
            "Keep face/eyes/hair-critical maps at 2K; test 1K for clothing/body and 512 for small accessories."
        )
    if any(not image["exists"] and not image["packed"] for image in images if image["source"] == "FILE"):
        recommendations.append("Resolve missing external image files before cleanup or export.")
    recommendations.append(
        "Do not delete hidden objects automatically; confirm whether each is hidden by the outfit or required by another outfit."
    )

    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "blend_file": bpy.data.filepath,
        "blender_version": bpy.app.version_string,
        "scene": bpy.context.scene.name,
        "summary": {
            "mesh_objects": len(objects),
            "vertices": total_vertices,
            "triangles": total_triangles,
            "materials": len(materials),
            "images": len(images),
            "shape_keys_including_basis": total_shape_keys,
            "image_file_mib": round(format_mib(total_image_file_bytes), 2),
            "estimated_texture_gpu_mib_with_mips": round(format_mib(total_gpu_bytes), 2),
            "duplicate_image_groups": len(duplicate_groups),
            "hidden_render_meshes": sum(1 for obj in objects if obj["hide_render"]),
        },
        "duplicate_images": duplicate_groups,
        "missing_images": [
            image["name"]
            for image in images
            if image["source"] == "FILE" and not image["exists"] and not image["packed"]
        ],
        "objects": objects,
        "materials": materials,
        "images": images,
        "recommendations": recommendations,
    }


def write_text_summary(report):
    summary = report["summary"]
    lines = [
        "City Dom Blender Character Analysis",
        "===================================",
        "Blend file: %s" % (report["blend_file"] or "<unsaved>"),
        "Blender: %s" % report["blender_version"],
        "",
        "Mesh objects: %d" % summary["mesh_objects"],
        "Vertices: %d" % summary["vertices"],
        "Triangles: %d" % summary["triangles"],
        "Materials: %d" % summary["materials"],
        "Images: %d" % summary["images"],
        "Shape keys including Basis: %d" % summary["shape_keys_including_basis"],
        "Image source size: %.2f MiB" % summary["image_file_mib"],
        "Estimated texture GPU memory with mipmaps: %.2f MiB"
        % summary["estimated_texture_gpu_mib_with_mips"],
        "Exact duplicate image groups: %d" % summary["duplicate_image_groups"],
        "Missing images: %d" % len(report["missing_images"]),
        "",
        "Largest mesh objects:",
    ]

    for obj in sorted(report["objects"], key=lambda item: item["triangles"], reverse=True)[:20]:
        lines.append(
            "- %s: %d triangles, %d vertices, %d shape keys, hide_render=%s"
            % (
                obj["name"],
                obj["triangles"],
                obj["vertices"],
                obj["shape_key_count"],
                obj["hide_render"],
            )
        )

    lines.extend(["", "Largest images:"])
    for image in sorted(
        report["images"],
        key=lambda item: item["estimated_gpu_bytes_with_mips"],
        reverse=True,
    )[:30]:
        lines.append(
            "- %s: %dx%d, %.2f MiB estimated GPU, users=%d"
            % (
                image["name"],
                image["width"],
                image["height"],
                format_mib(image["estimated_gpu_bytes_with_mips"]),
                image["users"],
            )
        )

    lines.extend(["", "Recommendations:"])
    lines.extend("- %s" % recommendation for recommendation in report["recommendations"])
    REPORT_TEXT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report = build_report()
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_text_summary(report)

    summary = report["summary"]
    print("City Dom character analysis complete")
    print("  JSON: %s" % REPORT_JSON)
    print("  Text: %s" % REPORT_TEXT)
    print("  Triangles: %d" % summary["triangles"])
    print("  Images: %d" % summary["images"])
    print("  Shape keys: %d" % summary["shape_keys_including_basis"])
    print(
        "  Estimated texture GPU memory: %.2f MiB"
        % summary["estimated_texture_gpu_mib_with_mips"]
    )


main()
