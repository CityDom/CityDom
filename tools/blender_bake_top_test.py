import os
import time
import traceback

import bpy


DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
LOG_PATH = os.path.join(DESKTOP, "maria_bake_top_test.log")
BAKE_IMAGE_PATH = os.path.join(DESKTOP, "maria_top_baked_basecolor.png")
OUT_PATH = os.path.join(DESKTOP, "maria_bake_top_test.glb")

TARGET_OBJECT_NAMES = ("o_top_camisole2_a",)
TARGET_MATERIAL_NAME = "cf_m_top_camisole2"
BAKE_SIZE = 2048


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


def find_target_object():
    for name in TARGET_OBJECT_NAMES:
        obj = bpy.data.objects.get(name)
        if obj and obj.type == "MESH":
            return obj

    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        for slot in obj.material_slots:
            if slot.material and slot.material.name == TARGET_MATERIAL_NAME:
                return obj

    raise RuntimeError("Could not find target object/material for %s" % TARGET_MATERIAL_NAME)


def ensure_object_mode():
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode="OBJECT")


def set_active_only(obj):
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def create_bake_image():
    old = bpy.data.images.get("Maria_Top_Baked_BaseColor")
    if old:
        bpy.data.images.remove(old)

    image = bpy.data.images.new(
        "Maria_Top_Baked_BaseColor",
        width=BAKE_SIZE,
        height=BAKE_SIZE,
        alpha=True,
        float_buffer=False,
    )
    image.generated_color = (0, 0, 0, 0)
    return image


def select_bake_node(material, image):
    if not material.use_nodes:
        material.use_nodes = True

    nodes = material.node_tree.nodes
    bake_node = nodes.new("ShaderNodeTexImage")
    bake_node.name = "Maria_Top_Bake_Target"
    bake_node.label = "Maria Top Bake Target"
    bake_node.image = image

    for node in nodes:
        node.select = False
    bake_node.select = True
    nodes.active = bake_node
    return bake_node


def configure_cycles_for_bake():
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 64
    scene.cycles.use_denoising = False

    scene.render.bake.use_clear = True
    scene.render.bake.margin = 16
    scene.render.bake.target = "IMAGE_TEXTURES"

    if hasattr(scene.view_settings, "view_transform"):
        scene.view_settings.view_transform = "Standard"
    if hasattr(scene.view_settings, "look"):
        scene.view_settings.look = "None"
    if hasattr(scene.view_settings, "exposure"):
        scene.view_settings.exposure = 0
    if hasattr(scene.view_settings, "gamma"):
        scene.view_settings.gamma = 1


def bake_top_base_color(obj, material):
    image = create_bake_image()
    select_bake_node(material, image)
    configure_cycles_for_bake()

    set_active_only(obj)
    log("Starting DIFFUSE/COLOR bake for %s / %s" % (obj.name, material.name))
    started = time.time()
    bpy.ops.object.bake(type="DIFFUSE", pass_filter={"COLOR"})
    log("Bake returned after %.2fs" % (time.time() - started))

    image.filepath_raw = BAKE_IMAGE_PATH
    image.file_format = "PNG"
    image.save()
    log("Saved baked texture: %s" % BAKE_IMAGE_PATH)
    return image


def replace_material_with_baked(obj, source_material, image):
    baked = bpy.data.materials.new(TARGET_MATERIAL_NAME + "__baked_glb_test")
    baked.use_nodes = True
    baked.diffuse_color = (0.02, 0.02, 0.02, 1)

    nodes = baked.node_tree.nodes
    principled = nodes.get("Principled BSDF")
    image_node = nodes.new("ShaderNodeTexImage")
    image_node.name = "Maria_Top_Baked_BaseColor"
    image_node.image = image

    if principled:
        baked.node_tree.links.new(image_node.outputs["Color"], principled.inputs["Base Color"])
        if "Alpha" in principled.inputs:
            baked.node_tree.links.new(image_node.outputs["Alpha"], principled.inputs["Alpha"])
        if "Roughness" in principled.inputs:
            principled.inputs["Roughness"].default_value = 0.62
        if "Metallic" in principled.inputs:
            principled.inputs["Metallic"].default_value = 0

    baked.use_nodes = True
    baked.blend_method = "BLEND"
    baked.use_screen_refraction = False

    replaced = 0
    for slot in obj.material_slots:
        if slot.material == source_material:
            slot.material = baked
            replaced += 1

    log("Replaced %d material slot(s) on %s with %s" % (replaced, obj.name, baked.name))
    return baked


def export_visible_glb():
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

    log("Starting visible GLB export: %s" % OUT_PATH)
    log("Export kwargs: %r" % kwargs)
    started = time.time()
    result = bpy.ops.export_scene.gltf(**kwargs)
    log("Export returned after %.2fs: %r" % (time.time() - started, result))
    if os.path.exists(OUT_PATH):
        log("Wrote GLB bytes: %d" % os.path.getsize(OUT_PATH))
    else:
        log("No GLB was written.")


def main():
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)

    log("Blender %s" % bpy.app.version_string)
    log("Bake image: %s" % BAKE_IMAGE_PATH)
    log("Output GLB: %s" % OUT_PATH)

    ensure_object_mode()
    obj = find_target_object()
    source_material = bpy.data.materials.get(TARGET_MATERIAL_NAME)
    if not source_material:
        raise RuntimeError("Missing material: %s" % TARGET_MATERIAL_NAME)

    log("Target object: %s" % obj.name)
    log("Target material: %s" % source_material.name)
    log("UV layers: %s" % ", ".join(layer.name for layer in obj.data.uv_layers))

    image = bake_top_base_color(obj, source_material)
    replace_material_with_baked(obj, source_material, image)
    export_visible_glb()
    log("Done.")


try:
    main()
except Exception:
    log("FAILED")
    log(traceback.format_exc())
    raise
