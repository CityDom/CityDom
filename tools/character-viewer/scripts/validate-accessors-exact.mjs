import { NodeIO } from "@gltf-transform/core";
import { ALL_EXTENSIONS } from "@gltf-transform/extensions";
import { MeshoptDecoder } from "meshoptimizer";
import { createHash } from "node:crypto";


const [, , baselinePath, candidatePath] = process.argv;

if (!baselinePath || !candidatePath) {
  console.error(
    "Usage: node scripts/validate-accessors-exact.mjs <baseline.glb> <candidate.glb>"
  );
  process.exit(2);
}

await MeshoptDecoder.ready;

const io = new NodeIO()
  .registerExtensions(ALL_EXTENSIONS)
  .registerDependencies({
    "meshopt.decoder": MeshoptDecoder
  });

const [baseline, candidate] = await Promise.all([
  io.read(baselinePath),
  io.read(candidatePath)
]);

const baselineRoot = baseline.getRoot();
const candidateRoot = candidate.getRoot();
const baselineAccessors = baselineRoot.listAccessors();
const candidateAccessors = candidateRoot.listAccessors();

if (baselineAccessors.length !== candidateAccessors.length) {
  throw new Error(
    `Accessor count changed: ${baselineAccessors.length} -> ${candidateAccessors.length}`
  );
}

function accessorSignature(accessor) {
  const array = accessor.getArray();
  if (!array) {
    return "empty";
  }
  const bytes = new Uint8Array(array.buffer, array.byteOffset, array.byteLength);
  const digest = createHash("sha256").update(bytes).digest("hex");
  return [
    array.constructor.name,
    accessor.getType(),
    accessor.getComponentType(),
    accessor.getNormalized(),
    accessor.getCount(),
    digest
  ].join(":");
}

function primitiveIndices(root) {
  return new Set(
    root.listMeshes().flatMap((mesh) =>
      mesh.listPrimitives().map((primitive) => primitive.getIndices()).filter(Boolean)
    )
  );
}

const baselineIndexAccessors = primitiveIndices(baselineRoot);
const candidateIndexAccessors = primitiveIndices(candidateRoot);
const baselineSignatures = baselineAccessors
  .filter((accessor) => !baselineIndexAccessors.has(accessor))
  .map(accessorSignature)
  .sort();
const candidateSignatures = candidateAccessors
  .filter((accessor) => !candidateIndexAccessors.has(accessor))
  .map(accessorSignature)
  .sort();
const baselineCounts = new Map();
const candidateCounts = new Map();
for (const signature of baselineSignatures) {
  baselineCounts.set(signature, (baselineCounts.get(signature) ?? 0) + 1);
}
for (const signature of candidateSignatures) {
  candidateCounts.set(signature, (candidateCounts.get(signature) ?? 0) + 1);
}
const missing = [];
const added = [];
for (const [signature, count] of baselineCounts) {
  const difference = count - (candidateCounts.get(signature) ?? 0);
  if (difference > 0) missing.push(`${difference}x ${signature}`);
}
for (const [signature, count] of candidateCounts) {
  const difference = count - (baselineCounts.get(signature) ?? 0);
  if (difference > 0) added.push(`${difference}x ${signature}`);
}
if (missing.length || added.length) {
  throw new Error(
    `Decoded accessor content changed. Missing:\n${missing.slice(0, 5).join("\n")}`
    + `\nAdded:\n${added.slice(0, 5).join("\n")}`
  );
}

function canonicalTriangles(primitive) {
  const indices = primitive.getIndices()?.getArray();
  if (!indices) return [];
  const triangles = [];
  for (let index = 0; index < indices.length; index += 3) {
    triangles.push(
      [indices[index], indices[index + 1], indices[index + 2]]
        .sort((left, right) => left - right)
        .join(",")
    );
  }
  return triangles.sort();
}

const baselinePrimitives = baselineRoot.listMeshes().flatMap((mesh) => mesh.listPrimitives());
const candidatePrimitives = candidateRoot.listMeshes().flatMap((mesh) => mesh.listPrimitives());
if (baselinePrimitives.length !== candidatePrimitives.length) {
  throw new Error(
    `Primitive count changed: ${baselinePrimitives.length} -> ${candidatePrimitives.length}`
  );
}
for (let index = 0; index < baselinePrimitives.length; index += 1) {
  const baselineTriangles = canonicalTriangles(baselinePrimitives[index]);
  const candidateTriangles = canonicalTriangles(candidatePrimitives[index]);
  if (
    baselineTriangles.length !== candidateTriangles.length
    || baselineTriangles.some((triangle, triangleIndex) =>
      triangle !== candidateTriangles[triangleIndex]
    )
  ) {
    throw new Error(`Primitive ${index} triangle topology changed`);
  }
}

for (const [label, baselineItems, candidateItems] of [
  ["meshes", baselineRoot.listMeshes(), candidateRoot.listMeshes()],
  ["nodes", baselineRoot.listNodes(), candidateRoot.listNodes()],
  ["skins", baselineRoot.listSkins(), candidateRoot.listSkins()],
  ["animations", baselineRoot.listAnimations(), candidateRoot.listAnimations()]
]) {
  if (baselineItems.length !== candidateItems.length) {
    throw new Error(
      `${label} count changed: ${baselineItems.length} -> ${candidateItems.length}`
    );
  }
}

console.log(
  `Exact attribute/topology validation passed: ${baselineAccessors.length} accessors, `
  + `${baselineRoot.listSkins().length} skin(s), `
  + `${baselineRoot.listMeshes().length} meshes.`
);
