import { MOUSE, PerspectiveCamera } from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

export function createViewerControls(
  camera: PerspectiveCamera,
  canvas: HTMLCanvasElement
): OrbitControls {
  const controls = new OrbitControls(camera, canvas);
  controls.enableDamping = true;
  controls.dampingFactor = 0.08;
  controls.enablePan = true;
  controls.screenSpacePanning = true;
  controls.rotateSpeed = 0.8;
  controls.zoomSpeed = 0.9;
  controls.panSpeed = 0.7;
  controls.mouseButtons = {
    LEFT: MOUSE.ROTATE,
    MIDDLE: MOUSE.DOLLY,
    RIGHT: MOUSE.PAN
  };
  controls.minDistance = 1.0;
  controls.maxDistance = 9.0;
  controls.target.set(0, 1.2, 0);
  controls.update();
  controls.saveState();
  canvas.addEventListener("contextmenu", (event) => event.preventDefault());
  return controls;
}
