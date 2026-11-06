import { createRequire } from "node:module";
import { DatabaseSync } from "node:sqlite";
import { boundedFile, readText, repoRoot } from "./files";
import type { ExportFormat } from "./index";

export type ExportVariant = "compact" | "extended";
export const isExportVariant = (value: string): value is ExportVariant =>
  value === "compact" || value === "extended";

type Generator = (result: unknown, variant: ExportVariant) => string;
type Generators = Record<string, Generator>;
const generatorNames: Record<ExportFormat, string> = {
  "DESIGN.md": "generateDesignMd",
  "variables.css": "generateCssVariables",
  "theme.css": "generateTailwindConfig",
  "tokens.json": "generateTokensJson",
};
const requireGenerator = createRequire(import.meta.url);

/** Use the library's existing serializers with the complete stored extraction.
 * The materialized design-system.json omits raw scales, radii and shadows, so
 * reconstructing an extraction from it would silently lose Extended values.
 * These files remain runtime library inputs, like the other source documents.
 */
export async function readStyleExport(
  slug: string,
  format: ExportFormat,
  variant: ExportVariant,
): Promise<string | null> {
  if (!/^[a-z0-9][a-z0-9-]*$/i.test(slug) || !isExportVariant(variant))
    return null;
  // The captured Extended Markdown resolves flight references that can remain
  // placeholders in result_json (including custom section text). Keep it intact.
  if (format === "DESIGN.md" && variant === "extended")
    return readText(`refero/${slug}/DESIGN.md`);
  const root = repoRoot();
  const [database, generatorFile] = await Promise.all([
    boundedFile(root, "refero/refero.db"),
    boundedFile(root, "tools/refero/generators.js"),
  ]);
  if (!database || !generatorFile) return null;
  let db: DatabaseSync | undefined;
  try {
    db = new DatabaseSync(/* turbopackIgnore: true */ database, {
      readOnly: true,
    });
    const row = db
      .prepare("SELECT result_json FROM styles WHERE slug = ?")
      .get(slug);
    if (typeof row?.result_json !== "string") return null;
    const result = JSON.parse(row.result_json);
    // createRequire keeps the existing CommonJS serializers cached in-process.
    // Neither user input nor extraction data selects executable code.
    const generators = requireGenerator(
      /* turbopackIgnore: true */ generatorFile,
    ) as Generators;
    const generate = generators[generatorNames[format]];
    return typeof generate === "function" ? generate(result, variant) : null;
  } catch {
    // Missing/LFS-only databases and incomplete extractions are unavailable,
    // never substituted with another variant or a truncated document.
    return null;
  } finally {
    db?.close();
  }
}
