import {
  Box3,
  Group,
  MathUtils,
  PerspectiveCamera,
  Vector3
} from "three";
import type { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

export type CameraPreset = "full_body";

const boundingBox = new Box3();
const center = new Vector3();
const size = new Vector3();

export function createViewerCamera(canvas: HTMLCanvasElement): PerspectiveCamera {
  const aspect = (canvas.clientWidth || window.innerWidth) / Math.max(canvas.clientHeight || window.innerHeight, 1);
  const camera = new PerspectiveCamera(35, aspect, 0.1, 100);
  camera.position.set(0, 1.55, 4.5);
  return camera;
}

export function applyCameraPreset(
  camera: PerspectiveCamera,
  controls: OrbitControls,
  model: Group,
  preset: CameraPreset
): void {
  if (preset !== "full_body") {
    throw new Error(`Unsupported camera preset: ${preset}`);
  }

  boundingBox.setFromObject(model);

  if (boundingBox.isEmpty()) {
    camera.position.set(0, 1.55, 4.5);
    controls.target.set(0, 1.2, 0);
    controls.saveState();
    return;
  }

  boundingBox.getCenter(center);
  boundingBox.getSize(size);

  const fitHeight = Math.max(size.y, 1.6);
  const fitWidth = Math.max(size.x, 0.8);
  const maxDimension = Math.max(fitHeight, fitWidth);
  const halfFov = MathUtils.degToRad(camera.fov * 0.5);
  const distance = Math.max(maxDimension / (2 * Math.tan(halfFov)), 2.4);
  const targetY = center.y + fitHeight * 0.1;

  controls.minDistance = Math.max(distance * 0.12, 0.25);
  controls.maxDistance = Math.max(distance * 4.0, 12.0);
  controls.target.set(center.x, targetY, center.z);
  camera.position.set(
    center.x + distance * 0.28,
    center.y + fitHeight * 0.06,
    center.z + distance * 1.15
  );
  camera.near = 0.1;
  camera.far = Math.max(distance * 8, 40);
  camera.updateProjectionMatrix();
  controls.update();
  controls.saveState();
}
