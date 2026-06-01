import {
  AmbientLight,
  Color,
  DirectionalLight,
  PCFSoftShadowMap,
  PerspectiveCamera,
  Scene,
  SRGBColorSpace,
  WebGLRenderer
} from "three";

export interface ViewerSceneContext {
  scene: Scene;
  render: (camera: PerspectiveCamera) => void;
  resize: (camera: PerspectiveCamera) => void;
  dispose: () => void;
}

export function createViewerScene(canvas: HTMLCanvasElement): ViewerSceneContext {
  const scene = new Scene();
  scene.background = new Color("#cfd3d6");

  const ambient = new AmbientLight("#ffffff", 1.65);
  scene.add(ambient);

  const keyLight = new DirectionalLight("#fff4d8", 2.25);
  keyLight.position.set(3, 7, 5);
  keyLight.castShadow = true;
  scene.add(keyLight);

  const rimLight = new DirectionalLight("#dbe9ff", 1.1);
  rimLight.position.set(-4, 4, -4);
  scene.add(rimLight);

  const renderer = new WebGLRenderer({
    antialias: true,
    alpha: false,
    canvas
  });

  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputColorSpace = SRGBColorSpace;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = PCFSoftShadowMap;

  function resize(camera: PerspectiveCamera): void {
    const width = canvas.clientWidth || window.innerWidth;
    const height = canvas.clientHeight || window.innerHeight;

    camera.aspect = width / Math.max(height, 1);
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  }

  renderer.setSize(canvas.clientWidth || window.innerWidth, canvas.clientHeight || window.innerHeight, false);

  return {
    scene,
    render(camera) {
      renderer.render(scene, camera);
    },
    resize(camera) {
      resize(camera);
    },
    dispose() {
      renderer.dispose();
    }
  };
}
