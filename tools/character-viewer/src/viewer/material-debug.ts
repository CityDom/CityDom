import {
  Group,
  Material,
  Mesh,
  MeshStandardMaterial,
  Texture
} from "three";

type MapKey = "map" | "normalMap" | "roughnessMap" | "metalnessMap" | "aoMap" | "alphaMap";

interface StoredMaterialState {
  color: string;
  roughness: number;
  metalness: number;
  envMapIntensity: number;
  opacity: number;
  transparent: boolean;
  normalScale: number;
  maps: Partial<Record<MapKey, Texture | null>>;
}

const mapKeys: MapKey[] = ["map", "normalMap", "roughnessMap", "metalnessMap", "aoMap", "alphaMap"];

const storedStates = new WeakMap<MeshStandardMaterial, StoredMaterialState>();

function getMaterialMap(material: MeshStandardMaterial, key: MapKey): Texture | null {
  return material[key] ?? null;
}

function setMaterialMap(material: MeshStandardMaterial, key: MapKey, texture: Texture | null): void {
  material[key] = texture;
  material.needsUpdate = true;
}

function materialState(material: MeshStandardMaterial): StoredMaterialState {
  const existing = storedStates.get(material);
  if (existing) {
    return existing;
  }

  const maps: Partial<Record<MapKey, Texture | null>> = {};
  for (const key of mapKeys) {
    maps[key] = getMaterialMap(material, key);
  }

  const state = {
    color: `#${material.color.getHexString()}`,
    roughness: material.roughness,
    metalness: material.metalness,
    envMapIntensity: material.envMapIntensity,
    opacity: material.opacity,
    transparent: material.transparent,
    normalScale: material.normalScale.x,
    maps
  };
  storedStates.set(material, state);
  return state;
}

function collectStandardMaterials(root: Group): MeshStandardMaterial[] {
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
        materialState(material);
      }
    }
  });

  return materials.sort((a, b) => a.name.localeCompare(b.name));
}

function formatMaterialLabel(material: MeshStandardMaterial, index: number): string {
  return material.name ? `${index + 1}. ${material.name}` : `${index + 1}. unnamed material`;
}

function isClothingMaterial(material: MeshStandardMaterial): boolean {
  return /(^|_)(top|bot|shorts?|pants?|panty|bra|camisole|socks?|shoes?|boots?|cloth|clothes|wetlook)(_|$)/i.test(material.name);
}

function applyClothingWetness(materials: MeshStandardMaterial[], wetness: number): void {
  for (const material of materials) {
    material.roughness = 0.92 - wetness * 0.84;
    material.metalness = wetness * 0.18;
    material.envMapIntensity = 0.08 + wetness * 1.72;
    material.needsUpdate = true;
  }
}

function resetMaterials(materials: MeshStandardMaterial[]): void {
  for (const material of materials) {
    resetMaterial(material);
  }
}

function createField(labelText: string): HTMLLabelElement {
  const label = document.createElement("label");
  label.className = "material-debug-field";

  const span = document.createElement("span");
  span.textContent = labelText;
  label.append(span);
  return label;
}

function createRange(
  labelText: string,
  min: number,
  max: number,
  step: number,
  getValue: () => number,
  setValue: (value: number) => void
): HTMLLabelElement {
  const label = createField(labelText);
  const input = document.createElement("input");
  input.type = "range";
  input.min = String(min);
  input.max = String(max);
  input.step = String(step);

  const output = document.createElement("output");

  function refresh(): void {
    const value = getValue();
    input.value = String(value);
    output.textContent = value.toFixed(step < 0.01 ? 3 : 2);
  }

  input.addEventListener("input", () => {
    setValue(Number(input.value));
    refresh();
  });

  label.append(input, output);
  refresh();
  return label;
}

function materialSnapshot(material: MeshStandardMaterial): string {
  const activeMaps = mapKeys.filter((key) => getMaterialMap(material, key)).join(", ") || "none";
  return JSON.stringify(
    {
      name: material.name,
      color: `#${material.color.getHexString()}`,
      roughness: Number(material.roughness.toFixed(3)),
      metalness: Number(material.metalness.toFixed(3)),
      envMapIntensity: Number(material.envMapIntensity.toFixed(3)),
      opacity: Number(material.opacity.toFixed(3)),
      transparent: material.transparent,
      normalScale: Number(material.normalScale.x.toFixed(3)),
      activeMaps
    },
    null,
    2
  );
}

function materialSnapshotObject(material: MeshStandardMaterial): Record<string, unknown> {
  const enabledMaps = Object.fromEntries(
    mapKeys.map((key) => [key, Boolean(getMaterialMap(material, key))])
  );
  const availableMaps = Object.fromEntries(
    mapKeys.map((key) => [key, Boolean(materialState(material).maps[key])])
  );

  return {
    name: material.name,
    uuid: material.uuid,
    color: `#${material.color.getHexString()}`,
    roughness: Number(material.roughness.toFixed(4)),
    metalness: Number(material.metalness.toFixed(4)),
    envMapIntensity: Number(material.envMapIntensity.toFixed(4)),
    opacity: Number(material.opacity.toFixed(4)),
    transparent: material.transparent,
    alphaTest: Number(material.alphaTest.toFixed(4)),
    depthWrite: material.depthWrite,
    depthTest: material.depthTest,
    normalScale: Number(material.normalScale.x.toFixed(4)),
    enabledMaps,
    availableMaps
  };
}

function materialSnapshotDocument(materials: MeshStandardMaterial[]): string {
  return JSON.stringify(
    {
      exportedAt: new Date().toISOString(),
      materialCount: materials.length,
      materials: materials.map(materialSnapshotObject)
    },
    null,
    2
  );
}

function downloadText(filename: string, text: string): void {
  const blob = new Blob([text], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.append(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

function resetMaterial(material: MeshStandardMaterial): void {
  const state = materialState(material);
  material.color.set(state.color);
  material.roughness = state.roughness;
  material.metalness = state.metalness;
  material.envMapIntensity = state.envMapIntensity;
  material.opacity = state.opacity;
  material.transparent = state.transparent;
  material.normalScale.setScalar(state.normalScale);

  for (const key of mapKeys) {
    setMaterialMap(material, key, state.maps[key] ?? null);
  }

  material.needsUpdate = true;
}

function setMaterialOpacity(material: MeshStandardMaterial, value: number): void {
  material.opacity = value;
  material.transparent = value < 1;
  material.needsUpdate = true;
}

function renderMaterialControls(container: HTMLElement, material: MeshStandardMaterial): void {
  container.replaceChildren();

  const heading = document.createElement("h2");
  heading.textContent = material.name || "Unnamed material";
  container.append(heading);

  const colorField = createField("Base color");
  const colorInput = document.createElement("input");
  colorInput.type = "color";
  colorInput.value = `#${material.color.getHexString()}`;
  colorInput.addEventListener("input", () => {
    material.color.set(colorInput.value);
    material.needsUpdate = true;
  });
  colorField.append(colorInput);
  container.append(colorField);

  container.append(
    createRange("Roughness", 0, 1, 0.01, () => material.roughness, (value) => {
      material.roughness = value;
      material.needsUpdate = true;
    }),
    createRange("Metalness", 0, 1, 0.01, () => material.metalness, (value) => {
      material.metalness = value;
      material.needsUpdate = true;
    }),
    createRange("Env intensity", 0, 4, 0.01, () => material.envMapIntensity, (value) => {
      material.envMapIntensity = value;
      material.needsUpdate = true;
    }),
    createRange("Opacity", 0, 1, 0.01, () => material.opacity, (value) => {
      setMaterialOpacity(material, value);
    }),
    createRange("Normal strength", 0, 3, 0.01, () => material.normalScale.x, (value) => {
      material.normalScale.setScalar(value);
      material.needsUpdate = true;
    })
  );

  const mapGroup = document.createElement("fieldset");
  mapGroup.className = "material-debug-map-group";
  const legend = document.createElement("legend");
  legend.textContent = "Texture maps";
  mapGroup.append(legend);

  for (const key of mapKeys) {
    const state = materialState(material);
    const originalMap = state.maps[key] ?? null;
    const label = document.createElement("label");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = Boolean(getMaterialMap(material, key));
    checkbox.disabled = !originalMap;
    checkbox.addEventListener("change", () => {
      setMaterialMap(material, key, checkbox.checked ? originalMap : null);
    });
    label.append(checkbox, document.createTextNode(` ${key}${originalMap ? "" : " (none)"}`));
    mapGroup.append(label);
  }

  container.append(mapGroup);

  const actions = document.createElement("div");
  actions.className = "material-debug-actions";

  const resetButton = document.createElement("button");
  resetButton.type = "button";
  resetButton.textContent = "Reset";
  resetButton.addEventListener("click", () => {
    resetMaterial(material);
    renderMaterialControls(container, material);
  });

  const copyButton = document.createElement("button");
  copyButton.type = "button";
  copyButton.textContent = "Copy JSON";
  copyButton.addEventListener("click", () => {
    void navigator.clipboard?.writeText(materialSnapshot(material));
  });

  actions.append(resetButton, copyButton);
  container.append(actions);

  const snapshot = document.createElement("pre");
  snapshot.className = "material-debug-snapshot";
  container.append(snapshot);

  function refreshSnapshot(): void {
    snapshot.textContent = materialSnapshot(material);
    requestAnimationFrame(refreshSnapshot);
  }
  refreshSnapshot();
}

function createClothingGroupControls(materials: MeshStandardMaterial[]): HTMLElement | null {
  const clothingMaterials = materials.filter(isClothingMaterial);
  if (clothingMaterials.length === 0) {
    return null;
  }

  const section = document.createElement("section");
  section.className = "material-debug-global";

  const heading = document.createElement("h2");
  heading.textContent = "Clothes wet/gloss";

  const note = document.createElement("p");
  note.textContent = `${clothingMaterials.length} clothing materials`;

  let wetness = 0;
  const wetnessField = createRange("Wetness", 0, 1, 0.01, () => wetness, (value) => {
    wetness = value;
    applyClothingWetness(clothingMaterials, wetness);
  });

  const actions = document.createElement("div");
  actions.className = "material-debug-actions";

  const dryButton = document.createElement("button");
  dryButton.type = "button";
  dryButton.textContent = "Dry";
  dryButton.addEventListener("click", () => {
    wetness = 0;
    applyClothingWetness(clothingMaterials, wetness);
    wetnessField.querySelector<HTMLInputElement>("input")!.value = String(wetness);
    wetnessField.querySelector<HTMLOutputElement>("output")!.textContent = wetness.toFixed(2);
  });

  const resetButton = document.createElement("button");
  resetButton.type = "button";
  resetButton.textContent = "Reset clothes";
  resetButton.addEventListener("click", () => {
    wetness = 0;
    resetMaterials(clothingMaterials);
    wetnessField.querySelector<HTMLInputElement>("input")!.value = String(wetness);
    wetnessField.querySelector<HTMLOutputElement>("output")!.textContent = wetness.toFixed(2);
  });

  actions.append(dryButton, resetButton);
  section.append(heading, note, wetnessField, actions);
  return section;
}

export function createMaterialDebugPanel(root: Group): void {
  const materials = collectStandardMaterials(root);
  if (materials.length === 0) {
    return;
  }

  const panel = document.createElement("aside");
  panel.className = "material-debug-panel";

  const title = document.createElement("h1");
  title.textContent = "Material Debug";

  const panelActions = document.createElement("div");
  panelActions.className = "material-debug-panel-actions";

  const saveAllButton = document.createElement("button");
  saveAllButton.type = "button";
  saveAllButton.textContent = "Save all JSON";
  saveAllButton.addEventListener("click", () => {
    const json = materialSnapshotDocument(materials);
    void navigator.clipboard?.writeText(json);
    downloadText("maria-material-debug.json", json);
  });

  panelActions.append(saveAllButton);

  const select = document.createElement("select");
  materials.forEach((material, index) => {
    const option = document.createElement("option");
    option.value = String(index);
    option.textContent = formatMaterialLabel(material, index);
    select.append(option);
  });

  const controls = document.createElement("div");
  controls.className = "material-debug-controls";

  const globalControls = createClothingGroupControls(materials);

  select.addEventListener("change", () => {
    renderMaterialControls(controls, materials[Number(select.value)]);
  });

  if (globalControls) {
    panel.append(title, panelActions, globalControls, select, controls);
  } else {
    panel.append(title, panelActions, select, controls);
  }
  document.body.append(panel);
  renderMaterialControls(controls, materials[0]);
}
