import os
import re
import time
import traceback

import bmesh
import bpy


DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
OUT_DIR = os.path.join(DESKTOP, "maria_pbr_bake")
LOG_PATH = os.path.join(OUT_DIR, "maria_pbr_bake.log")
OUT_PATH = os.path.join(OUT_DIR, "maria_pbr_bake.glb")

BAKE_SIZE = 2048
BAKE_SAMPLES = 64

TARGETS = [
    ("o_head", "cf_m_skin_head_01"),
    ("o_head", "cf_m_skin_body_00"),
    ("o_top_camisole2_a", "cf_m_top_camisole2"),
    ("o_shorts_a", "cf_m_shorts_00"),
    ("o_bot_pants_sports1_a", "cf_m_bot_pantssports1"),
    ("o_socks_thigh1", "cf_m_socks14"),
    ("s4studio_mesh_3", "1_WetLook_BootL"),
]

COMPONENTS = [
    ("basecolor", "DIFFUSE", {"COLOR"}, "sRGB"),
    ("normal", "NORMAL", None, "Non-Color"),
    ("roughness", "ROUGHNESS", None, "Non-Color"),
]


def log(message):
    text = "[%s] %s" % (time.strftime("%H:%M:%S"), message)
    print(text, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as handle:
        handle.write(text + "\n")
        handle.flush()


def safe_name(value):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value)


def operator_props():
    return {
        prop.identifier
        for prop in bpy.ops.export_scene.gltf.get_rna_type().properties
        if prop.identifier != "rna_type"
    }


def add_arg(kwargs, props, name, value):
    if name in props:
        kwargs[name] = value


def ensure_object_mode():
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode="OBJECT")


def set_active_only(obj):
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def make_single_material_bake_object(source_obj, material):
    material_slot_index = None
    for index, slot in enumerate(source_obj.material_slots):
        if slot.material == material:
            material_slot_index = index
            break

    if material_slot_index is None:
        raise RuntimeError("Material %s is not assigned to %s" % (material.name, source_obj.name))

    mesh = source_obj.data.copy()
    bake_obj = bpy.data.objects.new("__maria_bake_%s_%s" % (source_obj.name, safe_name(material.name)), mesh)
    bpy.context.collection.objects.link(bake_obj)
    bake_obj.matrix_world = source_obj.matrix_world.copy()

    bm = bmesh.new()
    bm.from_mesh(mesh)
    faces_to_delete = [face for face in bm.faces if face.material_index != material_slot_index]
    if faces_to_delete:
        bmesh.ops.delete(bm, geom=faces_to_delete, context="FACES")

    for face in bm.faces:
        face.material_index = 0

    bm.to_mesh(mesh)
    bm.free()
    mesh.update()

    mesh.materials.clear()
    mesh.materials.append(material)
    return bake_obj


def remove_bake_object(obj):
    mesh = obj.data
    bpy.data.objects.remove(obj, do_unlink=True)
    if mesh.users == 0:
        bpy.data.meshes.remove(mesh)


def configure_cycles_for_bake():
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = BAKE_SAMPLES
    scene.cycles.use_denoising = False
    scene.render.bake.use_clear = True
    scene.render.bake.margin = 16
    scene.render.bake.target = "IMAGE_TEXTURES"

    if hasattr(scene.render.bake, "normal_space"):
        scene.render.bake.normal_space = "TANGENT"

    if hasattr(scene.view_settings, "view_transform"):
        scene.view_settings.view_transform = "Standard"
    if hasattr(scene.view_settings, "look"):
        scene.view_settings.look = "None"
    if hasattr(scene.view_settings, "exposure"):
        scene.view_settings.exposure = 0
    if hasattr(scene.view_settings, "gamma"):
        scene.view_settings.gamma = 1


def find_object_material(object_name, material_name):
    obj = bpy.data.objects.get(object_name)
    material = bpy.data.materials.get(material_name)

    if obj and obj.type == "MESH" and material:
        return obj, material

    for candidate in bpy.data.objects:
        if candidate.type != "MESH":
            continue
        for slot in candidate.material_slots:
            if slot.material and slot.material.name == material_name:
                return candidate, slot.material

    raise RuntimeError("Could not find object/material: %s / %s" % (object_name, material_name))


def create_bake_image(material_name, component_name, color_space):
    image_name = "Maria_%s_%s" % (safe_name(material_name), component_name)
    old = bpy.data.images.get(image_name)
    if old:
        bpy.data.images.remove(old)

    image = bpy.data.images.new(
        image_name,
        width=BAKE_SIZE,
        height=BAKE_SIZE,
        alpha=True,
        float_buffer=False,
    )

    try:
        image.colorspace_settings.name = color_space
    except Exception:
        log("Could not set color space %s for %s" % (color_space, image_name))

    image.generated_color = (0, 0, 0, 0)
    return image


def select_bake_node(material, image):
    if not material.use_nodes:
        material.use_nodes = True

    nodes = material.node_tree.nodes
    bake_node = nodes.new("ShaderNodeTexImage")
    bake_node.name = "Maria_Bake_Target"
    bake_node.label = image.name
    bake_node.image = image

    for node in nodes:
        node.select = False
    bake_node.select = True
    nodes.active = bake_node
    return bake_node


def bake_component(obj, material, component_name, bake_type, pass_filter, color_space):
    image = create_bake_image(material.name, component_name, color_space)
    select_bake_node(material, image)
    set_active_only(obj)

    log("Bake start: object=%s material=%s component=%s type=%s" % (
        obj.name,
        material.name,
        component_name,
        bake_type,
    ))
    started = time.time()

    if pass_filter is None:
        bpy.ops.object.bake(type=bake_type)
    else:
        bpy.ops.object.bake(type=bake_type, pass_filter=pass_filter)

    log("Bake done: %s / %s after %.2fs" % (material.name, component_name, time.time() - started))

    path = os.path.join(OUT_DIR, "%s_%s.png" % (safe_name(material.name), component_name))
    image.filepath_raw = path
    image.file_format = "PNG"
    image.save()
    log("Saved: %s" % path)
    return image


def new_principled_material(source_material, images):
    baked = bpy.data.materials.new(source_material.name + "__pbr_baked")
    baked.use_nodes = True
    baked.diffuse_color = source_material.diffuse_color
    baked.blend_method = "OPAQUE"
    baked.use_screen_refraction = False

    nodes = baked.node_tree.nodes
    principled = nodes.get("Principled BSDF")
    if not principled:
        return baked

    base = images.get("basecolor")
    if base:
        node = nodes.new("ShaderNodeTexImage")
        node.name = base.name
        node.image = base
        baked.node_tree.links.new(node.outputs["Color"], principled.inputs["Base Color"])

    normal = images.get("normal")
    if normal:
        image_node = nodes.new("ShaderNodeTexImage")
        image_node.name = normal.name
        image_node.image = normal
        normal_node = nodes.new("ShaderNodeNormalMap")
        normal_node.inputs["Strength"].default_value = 1.0
        baked.node_tree.links.new(image_node.outputs["Color"], normal_node.inputs["Color"])
        baked.node_tree.links.new(normal_node.outputs["Normal"], principled.inputs["Normal"])

    roughness = images.get("roughness")
    if roughness:
        node = nodes.new("ShaderNodeTexImage")
        node.name = roughness.name
        node.image = roughness
        baked.node_tree.links.new(node.outputs["Color"], principled.inputs["Roughness"])
    elif "Roughness" in principled.inputs:
        principled.inputs["Roughness"].default_value = 0.65

    if "Metallic" in principled.inputs:
        principled.inputs["Metallic"].default_value = 0

    return baked


def replace_material_slots(source_material, baked_material):
    replaced = 0
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        for slot in obj.material_slots:
            if slot.material == source_material:
                slot.material = baked_material
                replaced += 1
    log("Replaced %d slot(s): %s -> %s" % (replaced, source_material.name, baked_material.name))


def bake_target(object_name, material_name):
    obj, material = find_object_material(object_name, material_name)
    log("Target: object=%s material=%s uv_layers=%s" % (
        obj.name,
        material.name,
        ", ".join(layer.name for layer in obj.data.uv_layers),
    ))

    images = {}
    bake_obj = make_single_material_bake_object(obj, material)
    log("Isolated bake object: %s polygons=%d" % (bake_obj.name, len(bake_obj.data.polygons)))

    try:
        for component_name, bake_type, pass_filter, color_space in COMPONENTS:
            try:
                images[component_name] = bake_component(bake_obj, material, component_name, bake_type, pass_filter, color_space)
            except Exception:
                log("Component bake failed: %s / %s" % (material.name, component_name))
                log(traceback.format_exc())
    finally:
        remove_bake_object(bake_obj)

    baked_material = new_principled_material(material, images)
    replace_material_slots(material, baked_material)


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
    log("Bake size: %d" % BAKE_SIZE)
    log("Bake samples: %d" % BAKE_SAMPLES)

    ensure_object_mode()
    configure_cycles_for_bake()

    for object_name, material_name in TARGETS:
        bake_target(object_name, material_name)

    export_visible_glb()
    log("Done.")


try:
    main()
except Exception:
    log("FAILED")
    log(traceback.format_exc())
    raise
