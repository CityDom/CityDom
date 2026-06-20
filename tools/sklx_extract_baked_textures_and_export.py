import os
import time
import traceback

import bpy


DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
OUT_DIR = os.path.join(DESKTOP, "sklx_baked_maria")
TEXTURE_DIR = os.path.join(OUT_DIR, "textures")
LOG_PATH = os.path.join(OUT_DIR, "sklx_baked_export.log")
OUT_PATH = os.path.join(OUT_DIR, "maria_sklx_baked.glb")

BAKED_SUFFIXES = (
    "_Diffuse_BK",
    "_EmissionColor_BK",
    "_Normal_BK",
    "_RoughSpecMetal_BK",
)


def log(message):
    text = "[%s] %s" % (time.strftime("%H:%M:%S"), message)
    print(text, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as handle:
        handle.write(text + "\n")
        handle.flush()


def safe_filename(name):
    bad = '<>:"/\\|?*'
    clean = "".join("_" if ch in bad else ch for ch in name)
    return clean.strip() or "unnamed"


def operator_props():
    return {
        prop.identifier
        for prop in bpy.ops.export_scene.gltf.get_rna_type().properties
        if prop.identifier != "rna_type"
    }


def add_arg(kwargs, props, name, value):
    if name in props:
        kwargs[name] = value


def is_baked_image(image):
    return image.name.endswith(BAKED_SUFFIXES)


def save_baked_images():
    os.makedirs(TEXTURE_DIR, exist_ok=True)
    baked_images = [image for image in bpy.data.images if is_baked_image(image)]

    log("Found baked images: %d" % len(baked_images))
    for image in baked_images:
        path = os.path.join(TEXTURE_DIR, safe_filename(image.name) + ".png")
        image.filepath_raw = path
        image.file_format = "PNG"
        image.save()
        log("Saved image: %s (%dx%d packed=%s)" % (
            path,
            image.size[0],
            image.size[1],
            bool(image.packed_file),
        ))

    return baked_images


def log_baked_materials():
    for material in bpy.data.materials:
        if not material or not material.use_nodes or not material.node_tree:
            continue

        baked_nodes = []
        for node in material.node_tree.nodes:
            image = getattr(node, "image", None)
            if image and is_baked_image(image):
                baked_nodes.append("%s=%s" % (node.name, image.name))

        if baked_nodes:
            log("Baked material: %s | %s" % (material.name, ", ".join(baked_nodes)))


def export_visible_glb():
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode="OBJECT")

    props = operator_props()
    kwargs = {"filepath": OUT_PATH}
    add_arg(kwargs, props, "export_format", "GLB")
    add_arg(kwargs, props, "use_selection", False)
    add_arg(kwargs, props, "use_visible", True)
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

    if os.path.exists(OUT_PATH):
        os.remove(OUT_PATH)

    log("Starting GLB export: %s" % OUT_PATH)
    log("Export kwargs: %r" % kwargs)
    started = time.time()
    result = bpy.ops.export_scene.gltf(**kwargs)
    log("Export returned after %.2fs: %r" % (time.time() - started, result))

    if os.path.exists(OUT_PATH):
        log("Wrote GLB bytes: %d" % os.path.getsize(OUT_PATH))
    else:
        log("No GLB was written.")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)

    log("Blender %s" % bpy.app.version_string)
    log("Output dir: %s" % OUT_DIR)
    save_baked_images()
    log_baked_materials()
    export_visible_glb()
    log("Done.")


try:
    main()
except Exception:
    log("FAILED")
    log(traceback.format_exc())
    raise
