import {
  Box3,
  Group,
  Material,
  Mesh,
  MeshStandardMaterial,
  Object3D,
  Texture,
  Vector3
} from "three";
import { FBXLoader } from "three/examples/jsm/loaders/FBXLoader.js";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { resolveResource } from "@tauri-apps/api/path";
import { readFile } from "@tauri-apps/plugin-fs";

export interface LoadedModel {
  group: Group;
  dispose: () => void;
}

export interface ModelLoadOptions {
  applyHs2Overrides: boolean;
}

const boundingBox = new Box3();
const center = new Vector3();

interface MaterialOverride {
  color: string;
  roughness: number;
  metalness?: number;
  envMapIntensity?: number;
}

const materialOverrides: Array<[RegExp, MaterialOverride]> = [
  [/^cf_m_skin_head_01$/i, { color: "#d59a8e", roughness: 0.86, envMapIntensity: 0.06 }],
  [/^cf_m_skin_body_00$/i, { color: "#dfa99f", roughness: 0.88, envMapIntensity: 0.05 }],
  [/^cf_m_top_camisole2$/i, { color: "#17191c", roughness: 0.58, envMapIntensity: 0.32 }],
  [/^cf_m_shorts_00$/i, { color: "#15171a", roughness: 0.56, envMapIntensity: 0.32 }],
  [/^cf_m_bot_pantssports1$/i, { color: "#15171a", roughness: 0.56, envMapIntensity: 0.32 }]
];

const materialTextureKeys = [
  "map",
  "normalMap",
  "aoMap",
  "roughnessMap",
  "metalnessMap",
  "alphaMap",
  "emissiveMap",
  "bumpMap",
  "displacementMap",
  "envMap"
] as const;

function normalizeModelPath(modelPath: string): string {
  return modelPath.replace(/\\/g, "/").replace(/^\/+/, "");
}

function clearBrokenHs2Maps(material: MeshStandardMaterial): void {
  material.map = null;
  material.normalMap = null;
  material.aoMap = null;
  material.roughnessMap = null;
  material.metalnessMap = null;
  material.alphaMap = null;
}

function createHs2OverrideMaterial(source: Material, override: MaterialOverride): MeshStandardMaterial {
  const material = new MeshStandardMaterial({
    color: override.color,
    roughness: override.roughness,
    metalness: override.metalness ?? 0
  });

  material.name = `${source.name || "hs2_material"}__viewer_override`;
  material.envMapIntensity = override.envMapIntensity ?? 0.25;
  material.side = source.side;
  material.transparent = false;
  material.opacity = 1;
  return material;
}

function overrideHs2Material(material: Material): Material {
  const override = materialOverrides.find(([pattern]) => pattern.test(material.name))?.[1];
  if (!override) {
    return material;
  }

  if (material instanceof MeshStandardMaterial) {
    clearBrokenHs2Maps(material);
  }

  return createHs2OverrideMaterial(material, override);
}

function overrideHs2Materials(material: Material | Material[]): Material | Material[] {
  if (Array.isArray(material)) {
    return material.map(overrideHs2Material);
  }

  return overrideHs2Material(material);
}

function applyNodeSpecificOverrides(node: Mesh): void {
  const nodeName = node.name.toLowerCase();

  if (nodeName === "o_shorts_a" || nodeName === "o_bot_pants_sports1_a") {
    node.material = new MeshStandardMaterial({
      color: "#121316",
      roughness: 0.54,
      metalness: 0
    });
  }

  if (node.material instanceof MeshStandardMaterial) {
    node.material.envMapIntensity = 0.25;
  }
}

function prepareModel(root: Object3D, options: ModelLoadOptions): Group {
  const group = new Group();
  group.add(root);

  root.traverse((node) => {
    if (node instanceof Mesh) {
      node.castShadow = true;
      node.receiveShadow = true;

      if (options.applyHs2Overrides) {
        node.material = overrideHs2Materials(node.material);
        applyNodeSpecificOverrides(node);
      }
    }
  });

  boundingBox.setFromObject(group);

  if (!boundingBox.isEmpty()) {
    boundingBox.getCenter(center);
    root.position.x -= center.x;
    root.position.z -= center.z;
    root.position.y -= boundingBox.min.y;
  }

  return group;
}

function contentTypeForModel(modelPath: string): string {
  if (modelPath.toLowerCase().endsWith(".glb")) {
    return "model/gltf-binary";
  }

  if (modelPath.toLowerCase().endsWith(".fbx")) {
    return "application/octet-stream";
  }

  return "application/octet-stream";
}

function disposeMaterial(material: Material): void {
  const materialWithTextures = material as Material & Record<string, unknown>;

  for (const key of materialTextureKeys) {
    const value = materialWithTextures[key];
    if (value instanceof Texture) {
      value.dispose();
    }
  }

  material.dispose();
}

function disposeModelResources(root: Object3D): void {
  const disposedMaterials = new Set<string>();
  const disposedGeometries = new Set<string>();

  root.traverse((node) => {
    if (!(node instanceof Mesh)) {
      return;
    }

    if (node.geometry && !disposedGeometries.has(node.geometry.uuid)) {
      node.geometry.dispose();
      disposedGeometries.add(node.geometry.uuid);
    }

    const materials = Array.isArray(node.material) ? node.material : [node.material];
    for (const material of materials) {
      if (material && !disposedMaterials.has(material.uuid)) {
        disposeMaterial(material);
        disposedMaterials.add(material.uuid);
      }
    }
  });
}

export async function loadBundledModel(
  modelPath: string,
  options: ModelLoadOptions = { applyHs2Overrides: true }
): Promise<LoadedModel> {
  const normalizedModelPath = normalizeModelPath(modelPath);
  const resourcePath = await resolveResource(`assets_3d/${normalizedModelPath}`);
  const bytes = await readFile(resourcePath);

  const blob = new Blob([bytes], { type: contentTypeForModel(normalizedModelPath) });
  const objectUrl = URL.createObjectURL(blob);

  try {
    const lowerPath = normalizedModelPath.toLowerCase();
    let group: Group;

    if (lowerPath.endsWith(".fbx")) {
      const object = await new FBXLoader().loadAsync(objectUrl);
      group = prepareModel(object, options);
    } else {
      const gltf = await new GLTFLoader().loadAsync(objectUrl);
      group = prepareModel(gltf.scene, options);
    }

    return {
      group,
      dispose() {
        disposeModelResources(group);
        URL.revokeObjectURL(objectUrl);
      }
    };
  } catch (error) {
    URL.revokeObjectURL(objectUrl);
    throw error;
  }
}
