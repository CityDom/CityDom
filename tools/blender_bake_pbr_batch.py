import os
import re
import time
import traceback

import bmesh
import bpy


DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
OUT_DIR = os.path.join(DESKTOP, "maria_pbr_bake")
LOG_PATH = os.path.join(OUT_DIR, "maria_pbr_bake.log")
GLB_IMAGE_FORMAT = os.environ.get("MARIA_GLTF_IMAGE_FORMAT", "AUTO").strip().upper()
GLB_IMAGE_QUALITY = int(os.environ.get("MARIA_GLTF_IMAGE_QUALITY", "95"))
DEFAULT_OUT_FILENAME = "maria_pbr_bake_webp.glb" if GLB_IMAGE_FORMAT == "WEBP" else "maria_pbr_bake.glb"
OUT_FILENAME = os.environ.get("MARIA_GLTF_OUTPUT_NAME", DEFAULT_OUT_FILENAME)
OUT_PATH = os.path.join(OUT_DIR, OUT_FILENAME)

BAKE_SIZE = int(os.environ.get("MARIA_BAKE_DEFAULT_SIZE", "1024"))
BAKE_SAMPLES = int(os.environ.get("MARIA_BAKE_SAMPLES", "32"))

# Preserve extra detail where it is actually visible. Everything else uses the
# default 1K target; accessory-only runs use 512 unless overridden here.
MATERIAL_BAKE_SIZES = {
    "cf_m_skin_head_01": 2048,
    "cf_m_skin_body_00": 2048,
    "HS2Rig Eyes2 for SKLX": 2048,
    "cf_m_socks14": 2048,
}
ACCESSORY_BAKE_SIZE = int(os.environ.get("MARIA_ACCESSORY_BAKE_SIZE", "512"))

TARGET_SETS = {
    "clothes": [
        ("o_top_camisole2_a", "cf_m_top_camisole2"),
        ("o_shorts_a", "cf_m_shorts_00"),
        ("o_bot_pants_sports1_a", "cf_m_bot_pantssports1"),
        ("o_socks_thigh1", "cf_m_socks14"),
        ("s4studio_mesh_3", "1_WetLook_BootL"),
    ],
    "face": [
        ("o_head", "cf_m_skin_head_01"),
        ("o_body", "cf_m_skin_body_00", "Body_uv1"),
        ("o_eyebase_L", "HS2Rig Eyes2 for SKLX"),
        ("o_eyelashes", "c_m_eyelashes"),
    ],
    "body": [
        ("o_body", "cf_m_skin_body_00", "Body_uv1"),
    ],
    "problem_clothes": [
        ("o_top_camisole2_a", "cf_m_top_camisole2"),
        ("o_bot_pants_sports1_a", "cf_m_bot_pantssports1"),
        ("o_socks_thigh1", "cf_m_socks14"),
    ],
    "accessories": [
        ("O_singlering_00_00", "acs_M_ring02_00"),
        ("O_skull_ring_00_00", "acs_M_ring01_00"),
        ("O_bracelet_00_00", "acs_M_bracelet_simple_00"),
        ("tokei2_de_tokei2", "acs_M_tokei02_d_00"),
        ("tokei2_re", "acs_M_tokei02_r_00"),
        ("BeadedBangle.Shape", "string.002"),
        ("ring6.Shape", "ring6_base"),
        ("ring6.Shape", "ring6_stone"),
        ("ring10.Shape", "ring10_base"),
        ("O_shushu", "acs_M_bracelet_shushu"),
        ("o_earring_cristal2", "acs_05"),
        ("o_earring_cristal2", "acs_07"),
    ],
}
TARGET_SETS["all"] = (
    TARGET_SETS["clothes"]
    + TARGET_SETS["face"]
    + TARGET_SETS["accessories"]
)

ACCESSORY_MATERIAL_NAMES = {
    target[1] for target in TARGET_SETS["accessories"]
}

# Keep appearance-critical color maps lossless. WebP remains enabled for the
# larger clothing color maps and non-color data maps where it tested cleanly.
PNG_BASECOLOR_MATERIAL_NAMES = {
    "cf_m_skin_head_01",
    "cf_m_skin_body_00",
    "HS2Rig Eyes2 for SKLX",
    "c_m_eyelashes",
}

# These targets either have no saved bake or produced a fully empty bake.
# Preserve their original material instead of replacing it with blank output.
SKIP_EXISTING_BAKE_MATERIAL_NAMES = {
    "acs_M_ring01_00",
    "acs_M_ring02_00",
    "string.002",
    "acs_M_bracelet_shushu",
}

TARGET_MODE = os.environ.get("MARIA_BAKE_TARGETS", "clothes").strip().lower()
TARGETS = TARGET_SETS.get(TARGET_MODE, TARGET_SETS["clothes"])
SKIP_BAKE = os.environ.get("MARIA_BAKE_SKIP_BAKE", "").strip().lower() in {
    "1", "true", "yes"
}
APPLY_EXISTING_BAKES = os.environ.get("MARIA_APPLY_EXISTING_BAKES", "").strip().lower() in {
    "1", "true", "yes"
}
USE_CONVERTED_WEBP = os.environ.get("MARIA_USE_CONVERTED_WEBP", "").strip().lower() in {
    "1", "true", "yes"
}
XNCONVERT_ROOT = os.path.join(OUT_DIR, "webp_xnconvert_input")

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


def make_single_material_bake_object(source_obj, material, material_name=None):
    material_slot_index = None
    for index, slot in enumerate(source_obj.material_slots):
        if slot.material == material or material_matches(slot.material, material_name or material.name):
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


def set_active_uv_layer(obj, uv_layer_name):
    if not uv_layer_name:
        return

    uv_layers = obj.data.uv_layers
    layer = uv_layers.get(uv_layer_name)
    if not layer:
        log("Requested UV layer not found on %s: %s" % (obj.name, uv_layer_name))
        return

    uv_layers.active = layer
    try:
        uv_layers.active_render = layer
    except Exception:
        pass
    log("Using UV layer for %s: %s" % (obj.name, uv_layer_name))


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


def set_input_if_present(node, names, value):
    changed = 0
    for name in names:
        if name in node.inputs:
            try:
                node.inputs[name].default_value = value
                changed += 1
            except Exception:
                pass
    return changed


def prepare_accessory_material_for_bake(material):
    if not material or material.name not in ACCESSORY_MATERIAL_NAMES:
        return

    try:
        material.diffuse_color[3] = 1.0
        material.blend_method = "OPAQUE"
        material.show_transparent_back = False
        material.use_screen_refraction = False
    except Exception:
        pass

    if not material.use_nodes or not material.node_tree:
        return

    changed = 0
    for node in material.node_tree.nodes:
        if getattr(node, "type", None) in ("BSDF_PRINCIPLED", "GROUP"):
            changed += set_input_if_present(node, ("Alpha", "Opacity", "Transparent", "Transparency"), 1.0)
            changed += set_input_if_present(node, ("Metallic", "Metalness"), 0.0)
        if getattr(node, "type", None) == "BSDF_PRINCIPLED":
            changed += set_input_if_present(node, ("Roughness",), 0.62)

    if changed:
        log("Prepared accessory material for opaque bake: %s changed_inputs=%d" % (material.name, changed))


def material_matches(material, material_name):
    if not material:
        return False

    name = material.name
    return (
        name == material_name
        or name.startswith(material_name + "__")
        or name.startswith(material_name + ".")
    )


def find_matching_slot_material(obj, material_name):
    if not obj or obj.type != "MESH":
        return None

    for slot in obj.material_slots:
        if material_matches(slot.material, material_name):
            return slot.material

    return None


def find_object_material(object_name, material_name):
    obj = bpy.data.objects.get(object_name)
    exact_material = bpy.data.materials.get(material_name)

    assigned_material = find_matching_slot_material(obj, material_name)
    if assigned_material:
        if exact_material:
            if assigned_material != exact_material:
                log("Using original material %s on assigned slot alias %s" % (material_name, assigned_material.name))
            return obj, exact_material
        if assigned_material.name != material_name:
            log("Using assigned material alias for %s: %s" % (material_name, assigned_material.name))
        return obj, assigned_material

    for candidate in bpy.data.objects:
        if candidate.type != "MESH":
            continue

        assigned_material = find_matching_slot_material(candidate, material_name)
        if assigned_material:
            if exact_material:
                if assigned_material != exact_material:
                    log("Using original material %s on assigned slot alias %s" % (material_name, assigned_material.name))
                return candidate, exact_material
            if assigned_material.name != material_name:
                log("Using assigned material alias for %s: %s" % (material_name, assigned_material.name))
            return candidate, assigned_material

    raise RuntimeError("Could not find object/material: %s / %s" % (object_name, material_name))


def bake_size_for_material(material_name):
    if material_name in ACCESSORY_MATERIAL_NAMES:
        return MATERIAL_BAKE_SIZES.get(material_name, ACCESSORY_BAKE_SIZE)
    return MATERIAL_BAKE_SIZES.get(material_name, BAKE_SIZE)


def create_bake_image(material_name, component_name, color_space, bake_size):
    image_name = "Maria_%s_%s" % (safe_name(material_name), component_name)
    old = bpy.data.images.get(image_name)
    if old:
        bpy.data.images.remove(old)

    image = bpy.data.images.new(
        image_name,
        width=bake_size,
        height=bake_size,
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


def bake_component(obj, material, component_name, bake_type, pass_filter, color_space, bake_size):
    image = create_bake_image(material.name, component_name, color_space, bake_size)
    select_bake_node(material, image)
    set_active_only(obj)

    log("Bake start: object=%s material=%s component=%s type=%s size=%d" % (
        obj.name,
        material.name,
        component_name,
        bake_type,
        bake_size,
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


def new_principled_material(source_material, images, uv_layer_name=None):
    baked = bpy.data.materials.new(source_material.name + "__pbr_baked")
    baked.use_nodes = True
    baked.diffuse_color = source_material.diffuse_color
    is_alpha_cutout = "socks" in source_material.name.lower()
    baked.blend_method = "CLIP" if is_alpha_cutout else "OPAQUE"
    if is_alpha_cutout:
        baked.alpha_threshold = 0.35
        baked.show_transparent_back = False
    baked.use_screen_refraction = False

    nodes = baked.node_tree.nodes
    principled = nodes.get("Principled BSDF")
    if not principled:
        return baked

    uv_node = None
    if uv_layer_name:
        uv_node = nodes.new("ShaderNodeUVMap")
        uv_node.name = "CityDom_Baked_UV"
        uv_node.uv_map = uv_layer_name

    def connect_uv(image_node):
        if uv_node and "UV" in uv_node.outputs and "Vector" in image_node.inputs:
            baked.node_tree.links.new(uv_node.outputs["UV"], image_node.inputs["Vector"])

    base = images.get("basecolor")
    if base:
        node = nodes.new("ShaderNodeTexImage")
        node.name = base.name
        node.image = base
        connect_uv(node)
        baked.node_tree.links.new(node.outputs["Color"], principled.inputs["Base Color"])
        if is_alpha_cutout and "Alpha" in node.outputs and "Alpha" in principled.inputs:
            baked.node_tree.links.new(node.outputs["Alpha"], principled.inputs["Alpha"])

    normal = images.get("normal")
    if normal:
        image_node = nodes.new("ShaderNodeTexImage")
        image_node.name = normal.name
        image_node.image = normal
        connect_uv(image_node)
        normal_node = nodes.new("ShaderNodeNormalMap")
        normal_node.inputs["Strength"].default_value = 1.0
        baked.node_tree.links.new(image_node.outputs["Color"], normal_node.inputs["Color"])
        baked.node_tree.links.new(normal_node.outputs["Normal"], principled.inputs["Normal"])

    roughness = images.get("roughness")
    if roughness:
        node = nodes.new("ShaderNodeTexImage")
        node.name = roughness.name
        node.image = roughness
        connect_uv(node)
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


def load_existing_bake_images(material, bake_material_name=None):
    images = {}
    bake_material_name = bake_material_name or material.name
    color_spaces = {
        "basecolor": "sRGB",
        "normal": "Non-Color",
        "roughness": "Non-Color",
    }
    for component_name, color_space in color_spaces.items():
        png_path = os.path.join(
            OUT_DIR,
            "%s_%s.png" % (safe_name(bake_material_name), component_name),
        )
        webp_folder = "color_quality95" if component_name == "basecolor" else "data_lossless"
        webp_path = os.path.join(
            XNCONVERT_ROOT,
            webp_folder,
            "%s_%s.webp" % (safe_name(bake_material_name), component_name),
        )
        use_webp = (
            USE_CONVERTED_WEBP
            and os.path.isfile(webp_path)
            and not (
                component_name == "basecolor"
                and bake_material_name in PNG_BASECOLOR_MATERIAL_NAMES
            )
        )
        path = webp_path if use_webp else png_path
        if not os.path.isfile(path):
            log("Existing bake is missing: %s" % path)
            continue
        image = bpy.data.images.load(path, check_existing=False)
        image.name = "Maria_%s_%s" % (safe_name(bake_material_name), component_name)
        try:
            image.colorspace_settings.name = color_space
        except Exception:
            pass
        images[component_name] = image
        log("Loaded existing bake: %s" % path)
    return images


def apply_existing_bake(
    object_name,
    material_name,
    uv_layer_name=None,
    bake_material_name=None,
):
    if material_name in SKIP_EXISTING_BAKE_MATERIAL_NAMES:
        log("Preserved original material; existing bake is unavailable or empty: %s" % material_name)
        return

    _obj, material = find_object_material(object_name, material_name)
    images = load_existing_bake_images(material, bake_material_name)
    if "basecolor" not in images:
        log("Preserved original material; existing basecolor bake is missing: %s" % material.name)
        return
    baked_material = new_principled_material(material, images, uv_layer_name)
    replace_material_slots(material, baked_material)


def bake_target(object_name, material_name, uv_layer_name=None):
    obj, material = find_object_material(object_name, material_name)
    bake_size = bake_size_for_material(material_name)
    prepare_accessory_material_for_bake(material)
    log("Target: object=%s material=%s bake_size=%d uv_layers=%s" % (
        obj.name,
        material.name,
        bake_size,
        ", ".join(layer.name for layer in obj.data.uv_layers),
    ))

    images = {}
    bake_obj = make_single_material_bake_object(obj, material, material_name)
    set_active_uv_layer(bake_obj, uv_layer_name)
    log("Isolated bake object: %s polygons=%d" % (bake_obj.name, len(bake_obj.data.polygons)))

    try:
        for component_name, bake_type, pass_filter, color_space in COMPONENTS:
            try:
                images[component_name] = bake_component(
                    bake_obj,
                    material,
                    component_name,
                    bake_type,
                    pass_filter,
                    color_space,
                    bake_size,
                )
            except Exception:
                log("Component bake failed: %s / %s" % (material.name, component_name))
                log(traceback.format_exc())
    finally:
        remove_bake_object(bake_obj)

    baked_material = new_principled_material(material, images, uv_layer_name)
    replace_material_slots(material, baked_material)


def export_visible_glb():
    props = operator_props()
    kwargs = {"filepath": OUT_PATH}
    add_arg(kwargs, props, "export_format", "GLB")
    add_arg(kwargs, props, "use_selection", False)
    add_arg(kwargs, props, "use_visible", True)
    add_arg(kwargs, props, "export_materials", "EXPORT")
    add_arg(kwargs, props, "export_image_format", GLB_IMAGE_FORMAT)
    add_arg(kwargs, props, "export_image_quality", GLB_IMAGE_QUALITY)
    add_arg(kwargs, props, "export_image_webp_fallback", False)
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
    add_arg(kwargs, props, "export_animations", True)

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
    log("Bake target mode: %s" % TARGET_MODE)
    log("Default bake size: %d" % BAKE_SIZE)
    log("High-detail material sizes: %r" % MATERIAL_BAKE_SIZES)
    log("Bake samples: %d" % BAKE_SAMPLES)
    log("GLB image format: %s quality=%d" % (GLB_IMAGE_FORMAT, GLB_IMAGE_QUALITY))
    log("Skip bake: %s" % SKIP_BAKE)
    log("Apply existing bakes: %s" % APPLY_EXISTING_BAKES)
    log("Use converted WebP: %s" % USE_CONVERTED_WEBP)

    if not SKIP_BAKE:
        ensure_object_mode()
        configure_cycles_for_bake()

        for target in TARGETS:
            object_name, material_name = target[:2]
            uv_layer_name = target[2] if len(target) > 2 else None
            try:
                bake_target(object_name, material_name, uv_layer_name)
            except RuntimeError as error:
                if "Could not find object/material" in str(error):
                    log("Skipped missing target: %s / %s" % (object_name, material_name))
                    continue
                raise
    elif APPLY_EXISTING_BAKES:
        ensure_object_mode()
        for target in TARGETS:
            object_name, material_name = target[:2]
            uv_layer_name = target[2] if len(target) > 2 else None
            try:
                apply_existing_bake(object_name, material_name, uv_layer_name)
            except RuntimeError as error:
                if "Could not find object/material" in str(error):
                    log("Skipped missing target: %s / %s" % (object_name, material_name))
                    continue
                raise

    export_visible_glb()
    log("Done.")


try:
    main()
except Exception:
    log("FAILED")
    log(traceback.format_exc())
    raise
