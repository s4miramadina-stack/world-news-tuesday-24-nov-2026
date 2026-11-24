// Tuesday 24 November 2026 on one page.
// The picture is painted ahead of time by draw.py (Pillow) and committed as entry.png.
// This entry point only hands that file to the judge, using Node 22's standard library
// and no network, so every run writes the very same bytes.
import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const folder = dirname(fileURLToPath(import.meta.url));
const picture = join(folder, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";

if (!existsSync(picture)) {
  console.error("entry.png is missing: run `python3 draw.py` first");
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
const target = join(outDir, "entry.png");
copyFileSync(picture, target);
console.log(`wrote ${target}, ${statSync(target).size} bytes`);
