import {
  ACESFilmicToneMapping,
  AmbientLight,
  Color,
  DirectionalLight,
  PCFSoftShadowMap,
  PerspectiveCamera,
  PMREMGenerator,
  Scene,
  SRGBColorSpace,
  WebGLRenderer
} from "three";
import { RoomEnvironment } from "three/examples/jsm/environments/RoomEnvironment.js";

export interface ViewerSceneContext {
  scene: Scene;
  render: (camera: PerspectiveCamera) => void;
  resize: (camera: PerspectiveCamera) => void;
  dispose: () => void;
}

export interface ViewerSceneOptions {
  transparent: boolean;
}

export function createViewerScene(canvas: HTMLCanvasElement, options: ViewerSceneOptions): ViewerSceneContext {
  const scene = new Scene();
  scene.background = options.transparent ? null : new Color("#cfd3d6");

  const ambient = new AmbientLight("#ffffff", 0.75);
  scene.add(ambient);

  const keyLight = new DirectionalLight("#fff4d8", 1.15);
  keyLight.position.set(3, 7, 5);
  keyLight.castShadow = true;
  scene.add(keyLight);

  const rimLight = new DirectionalLight("#dbe9ff", 0.45);
  rimLight.position.set(-4, 4, -4);
  scene.add(rimLight);

  const renderer = new WebGLRenderer({
    antialias: true,
    alpha: options.transparent,
    canvas
  });

  if (options.transparent) {
    renderer.setClearAlpha(0);
  }

  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputColorSpace = SRGBColorSpace;
  renderer.toneMapping = ACESFilmicToneMapping;
  renderer.toneMappingExposure = 0.78;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = PCFSoftShadowMap;

  const pmrem = new PMREMGenerator(renderer);
  const roomEnvironment = new RoomEnvironment();
  const environment = pmrem.fromScene(roomEnvironment, 0.04).texture;
  scene.environment = environment;
  roomEnvironment.dispose();
  pmrem.dispose();

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
      environment.dispose();
      renderer.dispose();
    }
  };
}
