import { NodeIO } from "@gltf-transform/core";
import {
  ALL_EXTENSIONS,
  EXTMeshoptCompression
} from "@gltf-transform/extensions";
import { MeshoptEncoder } from "meshoptimizer";


const [, , inputPath, outputPath] = process.argv;

if (!inputPath || !outputPath) {
  console.error(
    "Usage: node scripts/compress-meshopt-lossless.mjs <input.glb> <output.glb>"
  );
  process.exit(2);
}

await MeshoptEncoder.ready;

const io = new NodeIO()
  .registerExtensions(ALL_EXTENSIONS)
  .registerDependencies({
    "meshopt.encoder": MeshoptEncoder
  });

const document = await io.read(inputPath);
document
  .createExtension(EXTMeshoptCompression)
  .setRequired(true)
  .setEncoderOptions({
    // No quantize/reorder transform is run. Existing accessor bytes remain exact.
    method: EXTMeshoptCompression.EncoderMethod.QUANTIZE
  });

await io.write(outputPath, document);

console.log(`Lossless Meshopt GLB written: ${outputPath}`);
