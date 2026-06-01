import {
  Box3,
  Group,
  Mesh,
  Object3D,
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

const boundingBox = new Box3();
const center = new Vector3();

function normalizeModelPath(modelPath: string): string {
  return modelPath.replace(/\\/g, "/").replace(/^\/+/, "");
}

function prepareModel(root: Object3D): Group {
  const group = new Group();
  group.add(root);

  root.traverse((node) => {
    if (node instanceof Mesh) {
      node.castShadow = true;
      node.receiveShadow = true;
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

export async function loadBundledModel(modelPath: string): Promise<LoadedModel> {
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
      group = prepareModel(object);
    } else {
      const gltf = await new GLTFLoader().loadAsync(objectUrl);
      group = prepareModel(gltf.scene);
    }

    return {
      group,
      dispose() {
        URL.revokeObjectURL(objectUrl);
      }
    };
  } catch (error) {
    URL.revokeObjectURL(objectUrl);
    throw error;
  }
}
