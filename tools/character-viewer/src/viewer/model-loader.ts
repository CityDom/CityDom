import {
  Box3,
  FrontSide,
  Group,
  Material,
  Mesh,
  MeshStandardMaterial,
  Object3D,
  Texture,
  Vector3,
  WebGLRenderer
} from "three";
import { FBXLoader } from "three/examples/jsm/loaders/FBXLoader.js";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { KTX2Loader } from "three/examples/jsm/loaders/KTX2Loader.js";
import { MeshoptDecoder } from "three/examples/jsm/libs/meshopt_decoder.module.js";
import { resolveResource } from "@tauri-apps/api/path";
import { readFile } from "@tauri-apps/plugin-fs";

export interface LoadedModel {
  group: Group;
  dispose: () => void;
}

export interface ModelLoadOptions {
  applyHs2Overrides: boolean;
  renderer?: WebGLRenderer;
}

const boundingBox = new Box3();
const center = new Vector3();

interface MaterialOverride {
  color: string;
  roughness: number;
  metalness?: number;
  envMapIntensity?: number;
}

interface MariaAppearance {
  raw?: {
    hair_material_color?: number[];
    hair_material_specular_color?: number[];
    eyelash_material_color?: number[];
  };
  appearance?: {
    eyebrow_color?: number[];
    eyelash_color?: number[];
  };
}

const materialOverrides: Array<[RegExp, MaterialOverride]> = [
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

type MaterialTextureKey = (typeof materialTextureKeys)[number];

interface MariaMaterialPreset {
  color?: string;
  roughness?: number;
  metalness?: number;
  envMapIntensity?: number;
  opacity?: number;
  transparent?: boolean;
  alphaTest?: number;
  depthWrite?: boolean;
  depthTest?: boolean;
  normalScale?: number;
  enabledMaps?: Partial<Record<MaterialTextureKey, boolean>>;
}

const mariaSavedMaterialDefaults = new Map<string, MariaMaterialPreset>([
  ["1_wetlook_bootl", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["1_wetlook_bootl__pbr_baked", {"color":"#ffffff","roughness":1,"metalness":0,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["acs_05", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["acs_07", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["acs_m_bracelet_shushu", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["acs_m_bracelet_simple_00", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["acs_m_ring01_00", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["acs_m_ring02_00", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["acs_m_tokei02_d_00", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["acs_m_tokei02_r_00", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["c_m_eyelashes", {"color":"#000000","roughness":0.5,"metalness":0,"envMapIntensity":0.25,"opacity":0.95,"transparent":true,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":false,"roughnessMap":false,"metalnessMap":false,"aoMap":false,"alphaMap":false}}],
  ["c_m_eyelashes__pbr_baked", {"color":"#545050","roughness":1,"metalness":0,"envMapIntensity":0.25,"opacity":0.99,"transparent":true,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["c_m_tang", {"color":"#ffffff","roughness":1,"metalness":0,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["c_m_tooth", {"color":"#ffffff","roughness":1,"metalness":0,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["cf_m_bot_pantssports1", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":false,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["cf_m_bot_pantssports1__pbr_baked", {"color":"#ffffff","roughness":1,"metalness":0,"envMapIntensity":0.16,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1.01,"enabledMaps":{"map":true,"normalMap":false,"roughnessMap":false,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["cf_m_shorts_00", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["cf_m_shorts_00__pbr_baked", {"color":"#ffffff","roughness":1,"metalness":0,"envMapIntensity":0.25,"opacity":0,"transparent":true,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["cf_m_skin_body_00__pbr_baked", {"color":"#ffffff","roughness":0.88,"metalness":0,"envMapIntensity":0.07,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":false,"roughnessMap":false,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["cf_m_skin_head_01__pbr_baked", {"color":"#ffffff","roughness":0.86,"metalness":0,"envMapIntensity":0.08,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":false,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["cf_m_top_camisole2", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":false,"roughnessMap":false,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["cf_m_top_camisole2__pbr_baked", {"color":"#ffffff","roughness":1,"metalness":0,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":false,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["hair_material_b_31_00", {"color":"#7e4235","roughness":1,"metalness":0,"envMapIntensity":0.46,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":0,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":false,"metalnessMap":true,"aoMap":true,"alphaMap":false}}],
  ["hair_material_b_31_01", {"color":"#af857c","roughness":0.65,"metalness":0,"envMapIntensity":0.46,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":0,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":false,"metalnessMap":true,"aoMap":true,"alphaMap":false}}],
  ["hair_material_f_26_00", {"color":"#7b3728","roughness":1,"metalness":0,"envMapIntensity":0.46,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":0,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":false,"metalnessMap":true,"aoMap":true,"alphaMap":false}}],
  ["hs2 black nails", {"color":"#010101","roughness":0.34,"metalness":0,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":false,"normalMap":false,"roughnessMap":false,"metalnessMap":false,"aoMap":false,"alphaMap":false}}],
  ["hs2 glasses frame", {"color":"#4b4b4b","roughness":0.42,"metalness":0,"envMapIntensity":0.25,"opacity":1,"transparent":true,"alphaTest":0,"depthWrite":false,"depthTest":true,"normalScale":1,"enabledMaps":{"map":false,"normalMap":false,"roughnessMap":false,"metalnessMap":false,"aoMap":false,"alphaMap":false}}],
  ["hs2 glasses lens", {"color":"#323232","roughness":0.02,"metalness":0,"envMapIntensity":0.25,"opacity":0.12,"transparent":true,"alphaTest":0,"depthWrite":false,"depthTest":true,"normalScale":1,"enabledMaps":{"map":false,"normalMap":false,"roughnessMap":false,"metalnessMap":false,"aoMap":false,"alphaMap":false}}],
  ["hs2rig eyes2 for sklx__pbr_baked", {"color":"#ffffff","roughness":0.42,"metalness":0,"envMapIntensity":0.18,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["new material", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["new material 1", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":false,"normalMap":false,"roughnessMap":false,"metalnessMap":false,"aoMap":false,"alphaMap":false}}],
  ["new material 2", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":false,"normalMap":false,"roughnessMap":false,"metalnessMap":false,"aoMap":false,"alphaMap":false}}],
  ["ring10_base", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["ring6_base", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0.35,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":true,"normalMap":true,"roughnessMap":true,"metalnessMap":true,"aoMap":false,"alphaMap":false}}],
  ["ring6_stone", {"color":"#ffffff","roughness":1,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":false,"normalMap":false,"roughnessMap":false,"metalnessMap":false,"aoMap":false,"alphaMap":false}}],
  ["string", {"color":"#b2b2b2","roughness":0.5,"metalness":1,"envMapIntensity":0.25,"opacity":1,"transparent":false,"alphaTest":0,"depthWrite":true,"depthTest":true,"normalScale":1,"enabledMaps":{"map":false,"normalMap":false,"roughnessMap":false,"metalnessMap":false,"aoMap":false,"alphaMap":false}}]
]);

function normalizeModelPath(modelPath: string): string {
  return modelPath.replace(/\\/g, "/").replace(/^\/+/, "");
}

function modelDirectory(modelPath: string): string {
  const normalized = normalizeModelPath(modelPath);
  const lastSlash = normalized.lastIndexOf("/");
  return lastSlash >= 0 ? normalized.slice(0, lastSlash) : "";
}

async function readCharacterText(modelPath: string, relativePath: string): Promise<string | null> {
  try {
    const resourcePath = await resolveResource(`assets_3d/${modelDirectory(modelPath)}/${relativePath}`);
    const bytes = await readFile(resourcePath);
    return new TextDecoder("utf-8").decode(bytes);
  } catch {
    return null;
  }
}

function setColorFromArray(material: MeshStandardMaterial, color: number[] | undefined): void {
  if (!color || color.length < 3) {
    return;
  }

  material.color.setRGB(color[0], color[1], color[2]);
}

function clearBrokenHs2Maps(material: MeshStandardMaterial): void {
  material.map = null;
  material.normalMap = null;
  material.aoMap = null;
  material.roughnessMap = null;
  material.metalnessMap = null;
  material.alphaMap = null;
}

function canonicalMaterialName(name: string): string {
  return name
    .toLowerCase()
    .replace(/\.\d+$/, "")
    .replace(/(?:__pbr_baked)+/g, "__pbr_baked");
}

function applyMariaSavedMaterialDefault(material: MeshStandardMaterial): void {
  if (/socks14/i.test(material.name)) {
    return;
  }

  const preset = mariaSavedMaterialDefaults.get(canonicalMaterialName(material.name));
  if (!preset) {
    return;
  }

  if (preset.color !== undefined) {
    material.color.set(preset.color);
  }
  if (preset.roughness !== undefined) {
    material.roughness = preset.roughness;
  }
  if (preset.metalness !== undefined) {
    material.metalness = preset.metalness;
  }
  if (preset.envMapIntensity !== undefined) {
    material.envMapIntensity = preset.envMapIntensity;
  }
  if (preset.opacity !== undefined) {
    material.opacity = preset.opacity;
  }
  if (preset.transparent !== undefined) {
    material.transparent = preset.transparent;
  }
  if (preset.alphaTest !== undefined) {
    material.alphaTest = preset.alphaTest;
  }
  if (preset.depthWrite !== undefined) {
    material.depthWrite = preset.depthWrite;
  }
  if (preset.depthTest !== undefined) {
    material.depthTest = preset.depthTest;
  }
  if (preset.normalScale !== undefined) {
    material.normalScale.setScalar(preset.normalScale);
  }

  const materialWithTextures = material as MeshStandardMaterial & Record<MaterialTextureKey, Texture | null>;
  for (const key of materialTextureKeys) {
    if (preset.enabledMaps?.[key] === false) {
      materialWithTextures[key] = null;
    }
  }

  material.needsUpdate = true;
}

function applyMariaAccessoryMaterialDefault(material: MeshStandardMaterial): void {
  const name = canonicalMaterialName(material.name);

  if (
    /^acs_m_(bracelet|tokei|ring)/i.test(name)
    || /^ring\d+_/i.test(name)
    || /^acs_0[57]$/i.test(name)
  ) {
    material.color.set("#ffffff");
    material.metalness = 0.05;
    material.roughness = 0.62;
    material.envMapIntensity = 0.12;
    material.transparent = false;
    material.opacity = 1;
    material.needsUpdate = true;
  }
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

function isGlassLikeMaterial(material: MeshStandardMaterial): boolean {
  return /glass|lens/i.test(material.name);
}

function applyDepthProfile(material: MeshStandardMaterial): void {
  material.depthTest = true;

  if (isGlassLikeMaterial(material)) {
    material.transparent = true;
    material.depthWrite = false;
    material.needsUpdate = true;
    return;
  }

  if (material.transparent || material.opacity < 1 || material.alphaMap) {
    material.transparent = false;
    material.opacity = 1;
    material.depthWrite = true;
    material.alphaTest = Math.max(material.alphaTest, 0.35);
    material.needsUpdate = true;
  }
}

function applyMaterialDepthProfiles(material: Material | Material[]): void {
  const materials = Array.isArray(material) ? material : [material];

  for (const item of materials) {
    if (item instanceof MeshStandardMaterial) {
      applyDepthProfile(item);
    }
  }
}

function applyNodeSpecificOverrides(node: Mesh): void {
  if (node.material instanceof MeshStandardMaterial) {
    node.material.envMapIntensity = 0.25;
  }
}

function collectMaterials(root: Object3D): MeshStandardMaterial[] {
  const materials: MeshStandardMaterial[] = [];
  const seen = new Set<string>();

  root.traverse((node) => {
    if (!(node instanceof Mesh)) {
      return;
    }

    const nodeMaterials = Array.isArray(node.material) ? node.material : [node.material];
    for (const material of nodeMaterials) {
      if (material instanceof MeshStandardMaterial && !seen.has(material.uuid)) {
        materials.push(material);
        seen.add(material.uuid);
      }
    }
  });

  return materials;
}

async function applyMariaHs2TextureOverrides(root: Object3D, modelPath: string): Promise<void> {
  if (!/characters\/maria\//i.test(normalizeModelPath(modelPath))) {
    return;
  }

  const appearanceText = await readCharacterText(modelPath, "hs2/Maria_appearance.json");
  const appearance: MariaAppearance | null = appearanceText ? JSON.parse(appearanceText) : null;

  for (const material of collectMaterials(root)) {
    if (/^cf_m_skin_head_01(?!.*__pbr_baked)/i.test(material.name)) {
      clearBrokenHs2Maps(material);
      material.color.set("#f0d3cc");
      material.roughness = 0.86;
      material.metalness = 0;
      material.envMapIntensity = 0.06;
      material.transparent = false;
      material.opacity = 1;
      material.needsUpdate = true;
    } else if (/^cf_m_skin_body_00(?!.*__pbr_baked)/i.test(material.name)) {
      clearBrokenHs2Maps(material);
      material.color.set("#f0c2b8");
      material.roughness = 0.88;
      material.metalness = 0;
      material.envMapIntensity = 0.05;
      material.transparent = false;
      material.opacity = 1;
      material.needsUpdate = true;
    } else if (/^cf_m_skin_head_01.*__pbr_baked/i.test(material.name)) {
      material.color.set("#ffffff");
      material.roughness = 0.86;
      material.metalness = 0;
      material.envMapIntensity = 0.08;
      material.transparent = false;
      material.opacity = 1;
      material.needsUpdate = true;
    } else if (/^cf_m_skin_body_00.*__pbr_baked/i.test(material.name)) {
      material.color.set("#ffffff");
      material.roughness = 0.88;
      material.metalness = 0;
      material.envMapIntensity = 0.07;
      material.transparent = false;
      material.opacity = 1;
      material.needsUpdate = true;
    } else if (/HS2Rig Eyes2.*__pbr_baked/i.test(material.name)) {
      material.color.set("#ffffff");
      material.roughness = 0.42;
      material.metalness = 0;
      material.envMapIntensity = 0.18;
      material.transparent = false;
      material.opacity = 1;
      material.needsUpdate = true;
    } else if (/^cf_m_socks14/i.test(material.name)) {
      material.color.set("#ffffff");
      material.roughness = 0.9;
      material.metalness = 0;
      material.envMapIntensity = 0.04;
      material.transparent = true;
      material.opacity = 0.98;
      material.alphaTest = 0.02;
      material.depthWrite = false;
      material.depthTest = true;
      material.side = FrontSide;
      material.normalScale.setScalar(0.35);
      material.needsUpdate = true;
    } else if (/^hair_material_/i.test(material.name)) {
      setColorFromArray(material, appearance?.raw?.hair_material_color);
      material.roughness = 0.65;
      material.metalness = 0;
      material.envMapIntensity = 0.46;
      material.opacity = 1;
      material.normalScale.setScalar(0);
      material.roughnessMap = null;
      material.needsUpdate = true;
    } else if (/eyelashes/i.test(material.name)) {
      setColorFromArray(
        material,
        appearance?.raw?.eyelash_material_color ?? appearance?.appearance?.eyelash_color
      );
      material.needsUpdate = true;
    }

    applyMariaSavedMaterialDefault(material);
    applyMariaAccessoryMaterialDefault(material);
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
        applyMaterialDepthProfiles(node.material);
        applyNodeSpecificOverrides(node);
      }
    }
  });

  boundingBox.setFromObject(group);

  if (!boundingBox.isEmpty()) {
    const modelHeight = boundingBox.max.y - boundingBox.min.y;
    if (modelHeight > 4 || modelHeight < 0.5) {
      root.scale.multiplyScalar(1.8 / modelHeight);
      root.updateMatrixWorld(true);
      boundingBox.setFromObject(group);
    }
  }

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
  const objectUrls = [objectUrl];

  try {
    const lowerPath = normalizedModelPath.toLowerCase();
    let group: Group;

    if (lowerPath.endsWith(".fbx")) {
      const object = await new FBXLoader().loadAsync(objectUrl);
      group = prepareModel(object, options);
    } else {
      const gltfLoader = new GLTFLoader();
      gltfLoader.setMeshoptDecoder(MeshoptDecoder);
      let ktx2Loader: KTX2Loader | null = null;
      if (options.renderer) {
        ktx2Loader = new KTX2Loader()
          .setTranscoderPath("./basis/")
          .detectSupport(options.renderer);
        gltfLoader.setKTX2Loader(ktx2Loader);
      }
      const gltf = await gltfLoader.loadAsync(objectUrl);
      ktx2Loader?.dispose();
      group = prepareModel(gltf.scene, options);
    }

    if (options.applyHs2Overrides) {
      await applyMariaHs2TextureOverrides(group, normalizedModelPath);
    }

    return {
      group,
      dispose() {
        disposeModelResources(group);
        for (const url of objectUrls) {
          URL.revokeObjectURL(url);
        }
      }
    };
  } catch (error) {
    for (const url of objectUrls) {
      URL.revokeObjectURL(url);
    }
    throw error;
  }
}
