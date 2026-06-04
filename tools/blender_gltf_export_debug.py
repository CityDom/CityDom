import os
import time
import traceback

import bpy


DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
OUT_PATH = os.path.join(DESKTOP, "maria_debug_export.glb")
LOG_PATH = os.path.join(DESKTOP, "maria_debug_export.log")
DEBUG_SCRIPT_VERSION = "2026-06-01-visible-export"

# Use VISIBLE for a complete character export. Use SELECTED only for small tests.
EXPORT_SCOPE = "VISIBLE"


def log(message):
    text = "[%s] %s" % (time.strftime("%H:%M:%S"), message)
    print(text, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as handle:
        handle.write(text + "\n")
        handle.flush()


def operator_props():
    return {
        prop.identifier
        for prop in bpy.ops.export_scene.gltf.get_rna_type().properties
        if prop.identifier != "rna_type"
    }


def add_arg(kwargs, props, name, value):
    if name in props:
        kwargs[name] = value


def image_path_status(image):
    if image.packed_file:
        return "packed"
    if not image.filepath:
        return "generated/no-path"
    try:
        return "exists" if os.path.exists(bpy.path.abspath(image.filepath)) else "missing"
    except Exception:
        return "path-error"


def material_image_names(material):
    names = []
    if material and material.use_nodes and material.node_tree:
        for node in material.node_tree.nodes:
            if node.bl_idname == "ShaderNodeTexImage" and getattr(node, "image", None):
                names.append(node.image.name)
    return names


def count_mesh_triangles(objects):
    total = 0
    for obj in objects:
        if obj.type != "MESH":
            continue
        mesh = obj.data
        for poly in mesh.polygons:
            total += max(len(poly.vertices) - 2, 1)
    return total


def main():
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)
    if os.path.exists(OUT_PATH):
        os.remove(OUT_PATH)

    log("Blender %s" % bpy.app.version_string)
    log("Debug script version: %s" % DEBUG_SCRIPT_VERSION)
    log("Output: %s" % OUT_PATH)

    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode="OBJECT")

    visible = [obj for obj in bpy.context.scene.objects if obj.visible_get()]
    selected = list(bpy.context.selected_objects)
    export_objects = selected if EXPORT_SCOPE == "SELECTED" else visible

    log("Scene objects: %d" % len(bpy.context.scene.objects))
    log("Export scope: %s" % EXPORT_SCOPE)
    log("Selected objects: %d" % len(selected))
    log("Visible objects: %d" % len(visible))
    log("Export target objects: %d" % len(export_objects))
    log("Export target meshes: %d" % sum(1 for obj in export_objects if obj.type == "MESH"))
    log("Approx selected/visible triangles: %d" % count_mesh_triangles(export_objects))
    log("Total materials in file: %d" % len(bpy.data.materials))
    log("Total images in file: %d" % len(bpy.data.images))

    for image in bpy.data.images:
        log("Image: %s | %s | filepath=%s" % (image.name, image_path_status(image), image.filepath or ""))

    used_materials = []
    for obj in export_objects:
        if obj.type != "MESH":
            continue
        for slot in obj.material_slots:
            if slot.material and slot.material not in used_materials:
                used_materials.append(slot.material)

    log("Materials used by export target: %d" % len(used_materials))
    for material in used_materials:
        names = material_image_names(material)
        log("Material: %s | use_nodes=%s | image_nodes=%s" % (material.name, material.use_nodes, ", ".join(names) or "none"))

    props = operator_props()
    log("Exporter image-related props: %s" % ", ".join(sorted(p for p in props if "image" in p.lower() or "texture" in p.lower())))
    log("Exporter material-related props: %s" % ", ".join(sorted(p for p in props if "material" in p.lower())))
    log("Exporter animation-related props: %s" % ", ".join(sorted(p for p in props if "anim" in p.lower())))

    kwargs = {"filepath": OUT_PATH}
    add_arg(kwargs, props, "export_format", "GLB")
    add_arg(kwargs, props, "use_selection", EXPORT_SCOPE == "SELECTED")
    add_arg(kwargs, props, "use_visible", EXPORT_SCOPE == "VISIBLE")
    add_arg(kwargs, props, "export_materials", "EXPORT")
    add_arg(kwargs, props, "export_image_format", "AUTO")
    add_arg(kwargs, props, "export_image_quality", 100)
    add_arg(kwargs, props, "export_unused_images", False)
    add_arg(kwargs, props, "export_unused_textures", False)
    add_arg(kwargs, props, "export_yup", True)
    add_arg(kwargs, props, "export_apply", False)
    add_arg(kwargs, props, "export_texcoords", True)
    add_arg(kwargs, props, "export_normals", True)
    add_arg(kwargs, props, "export_tangents", False)
    add_arg(kwargs, props, "export_skins", True)
    add_arg(kwargs, props, "export_morph", True)
    add_arg(kwargs, props, "export_lights", False)
    add_arg(kwargs, props, "export_cameras", False)
    add_arg(kwargs, props, "export_animations", False)

    log("Export kwargs: %r" % kwargs)
    log("Starting glTF export...")
    started = time.time()

    result = bpy.ops.export_scene.gltf(**kwargs)

    log("Export returned after %.2fs: %r" % (time.time() - started, result))
    if os.path.exists(OUT_PATH):
        log("Wrote GLB bytes: %d" % os.path.getsize(OUT_PATH))
    else:
        log("No GLB was written.")


try:
    main()
except Exception:
    log("FAILED")
    log(traceback.format_exc())
    raise
