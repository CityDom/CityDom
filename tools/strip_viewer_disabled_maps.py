import argparse
import json
import re
import struct
from copy import deepcopy
from pathlib import Path


JSON_CHUNK_TYPE = 0x4E4F534A
FRAME_MESH = "o_glasses_typeH_00_03"
LENS_MESH = "o_glasses_typeH_00_03_r"

DEFAULT_FRAME_MATERIAL = {
    "doubleSided": True,
    "extensions": {
        "KHR_materials_specular": {
            "specularFactor": 0.1599999964237213,
        },
    },
    "name": "HS2 Glasses Frame",
    "pbrMetallicRoughness": {
        "baseColorFactor": [
            0.06955760717391968,
            0.06955760717391968,
            0.06955760717391968,
            1,
        ],
        "metallicFactor": 0,
        "roughnessFactor": 0.41999998688697815,
    },
}


def canonical_material_name(name):
    name = re.sub(r"\.\d+$", "", name.lower())
    return re.sub(r"(?:__pbr_baked)+", "__pbr_baked", name)


def read_glb(path):
    data = path.read_bytes()
    magic, version, _total_length = struct.unpack_from("<4sII", data, 0)
    if magic != b"glTF" or version != 2:
        raise RuntimeError("Expected a GLB 2.0 input")

    json_length, json_type = struct.unpack_from("<II", data, 12)
    if json_type != JSON_CHUNK_TYPE:
        raise RuntimeError("First GLB chunk is not JSON")
    document = json.loads(data[20 : 20 + json_length].decode("utf-8"))
    return document, data[20 + json_length :]


def write_glb(path, document, remaining_chunks):
    json_bytes = json.dumps(document, separators=(",", ":")).encode("utf-8")
    json_bytes += b" " * ((-len(json_bytes)) % 4)
    total_length = 12 + 8 + len(json_bytes) + len(remaining_chunks)
    output = (
        struct.pack("<4sII", b"glTF", 2, total_length)
        + struct.pack("<II", len(json_bytes), JSON_CHUNK_TYPE)
        + json_bytes
        + remaining_chunks
    )
    path.write_bytes(output)


def load_presets(profile_path):
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    return {
        canonical_material_name(material["name"]): material
        for material in profile["materials"]
    }


def remove_disabled_map_references(document, presets):
    removed = []
    for material in document.get("materials", []):
        material_name = material.get("name", "")
        preset = presets.get(canonical_material_name(material_name))
        if not preset:
            continue

        enabled = preset.get("enabledMaps", {})
        pbr = material.get("pbrMetallicRoughness", {})

        if pbr.get("baseColorTexture") and enabled.get("map") is False:
            del pbr["baseColorTexture"]
            removed.append((material_name, "baseColorTexture"))

        if material.get("normalTexture") and (
            enabled.get("normalMap") is False
            or preset.get("normalScale") == 0
        ):
            del material["normalTexture"]
            removed.append((material_name, "normalTexture"))

        if material.get("occlusionTexture") and enabled.get("aoMap") is False:
            del material["occlusionTexture"]
            removed.append((material_name, "occlusionTexture"))

        if (
            pbr.get("metallicRoughnessTexture")
            and enabled.get("roughnessMap") is False
            and enabled.get("metalnessMap") is False
        ):
            del pbr["metallicRoughnessTexture"]
            removed.append((material_name, "metallicRoughnessTexture"))

        if material.get("emissiveTexture") and enabled.get("emissiveMap") is False:
            del material["emissiveTexture"]
            removed.append((material_name, "emissiveTexture"))

    return removed


def find_material_index(document, name):
    expected = canonical_material_name(name)
    for index, material in enumerate(document.get("materials", [])):
        if canonical_material_name(material.get("name", "")) == expected:
            return index
    return None


def assign_mesh_material(document, mesh_name, material_index):
    changed = 0
    for mesh in document.get("meshes", []):
        if mesh.get("name") != mesh_name:
            continue
        for primitive in mesh.get("primitives", []):
            primitive["material"] = material_index
            changed += 1
    return changed


def enforce_glasses_split(document):
    lens_index = find_material_index(document, "HS2 Glasses Lens")
    if lens_index is None:
        return 0

    frame_index = find_material_index(document, "HS2 Glasses Frame")
    if frame_index is None:
        frame_index = len(document["materials"])
        document["materials"].append(deepcopy(DEFAULT_FRAME_MATERIAL))

    changed = assign_mesh_material(document, FRAME_MESH, frame_index)
    changed += assign_mesh_material(document, LENS_MESH, lens_index)
    if changed not in (0, 2):
        raise RuntimeError(f"Expected zero or two glasses primitives, changed {changed}")
    return changed


def parse_args():
    parser = argparse.ArgumentParser(
        description="Remove texture slots disabled by a saved viewer material profile."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--profile", required=True, type=Path)
    return parser.parse_args()


def main():
    args = parse_args()
    document, remaining_chunks = read_glb(args.input)
    presets = load_presets(args.profile)
    removed = remove_disabled_map_references(document, presets)
    glasses_assignments = enforce_glasses_split(document)
    write_glb(args.output, document, remaining_chunks)

    print(f"Removed {len(removed)} disabled texture references:")
    for material_name, slot_name in removed:
        print(f"  {material_name}: {slot_name}")
    print(f"Validated glasses assignments: {glasses_assignments}")
    print(f"Wrote: {args.output}")


if __name__ == "__main__":
    main()
