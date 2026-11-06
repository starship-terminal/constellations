import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { promises as fs } from "node:fs";
import path from "node:path";
import os from "node:os";
import { DatabaseSync } from "node:sqlite";
import { createRequire } from "node:module";
import { readExport } from "../src/server/sources";
import { repoRoot } from "../src/server/sources/files";
import { GET } from "../src/app/api/library/[source]/[slug]/export/route";

const originalRepo = process.env.DESIGN_SYSTEMS_REPO;
const generatorPath = path.join(repoRoot(), "tools/refero/generators.js");
let fixture: string;
const extraction = {
  meta: {
    siteName: "Sample",
    url: "https://example.com",
    extractedAt: "2026-10-20T00:00:00Z",
  },
  screenshot: { url: "https://example.com/preview.jpg" },
  designSystem: {
    description: "Quiet product pages.",
    northStar: "Let the product lead.",
    theme: "light",
    colors: [{ name: "Ink", hex: "#111111", role: "Text" }],
    typography: [
      {
        family: "Arial",
        role: "Body",
        weight: "400",
        sizes: "16px",
        lineHeight: "1.5",
      },
    ],
    typeScale: [
      { role: "Body", family: "Arial", weight: 400, size: 16, lineHeight: 1.5 },
    ],
    spacing: { pageMaxWidth: "1200px", radius: { card: "8px" } },
    components: [
      { name: "Card", role: "Content", description: "Keep cards flat." },
    ],
    dos: ["Use generous spacing."],
    donts: ["Add decorative shadows."],
    surfaces: [{ name: "Canvas", hex: "#ffffff", level: 0, purpose: "Page" }],
    customSections: [
      { title: "Agent Prompt Guide", content: "Use these values." },
    ],
  },
  raw: {
    typography: {
      fonts: [{ family: "Arial", weights: [400, 700] }],
      steps: [
        {
          family: "Arial",
          size: 16,
          weight: 400,
          lineHeight: 1.5,
          letterSpacing: 0,
          frequency: 3,
        },
      ],
    },
    spacing: {
      baseUnit: 4,
      density: "comfortable",
      tokens: [{ value: 8, frequency: 5 }],
    },
    shapes: {
      radii: [{ value: 8, frequency: 3 }],
      shadows: [{ value: "0px 2px 8px #00000020", frequency: 2 }],
    },
  },
};

const storedMarkdown = createRequire(import.meta.url)(
  generatorPath,
).generateDesignMd(extraction, "extended") as string;

beforeEach(async () => {
  fixture = await fs.mkdtemp(path.join(os.tmpdir(), "style-export-"));
  await fs.mkdir(path.join(fixture, "refero/sample"), { recursive: true });
  await fs.mkdir(path.join(fixture, "tools/refero"), { recursive: true });
  await fs.copyFile(
    generatorPath,
    path.join(fixture, "tools/refero/generators.js"),
  );
  await fs.writeFile(path.join(fixture, "catalog.json"), '{"systems":[]}');
  await fs.writeFile(
    path.join(fixture, "refero/catalog.json"),
    JSON.stringify({ styles: [{ slug: "sample", name: "Sample" }] }),
  );
  for (const format of [
    "DESIGN.md",
    "tokens.json",
    "variables.css",
    "theme.css",
  ])
    await fs.writeFile(
      path.join(fixture, "refero/sample", format),
      format === "DESIGN.md" ? storedMarkdown : `stored ${format}\n`,
    );
  const db = new DatabaseSync(path.join(fixture, "refero/refero.db"));
  db.exec("CREATE TABLE styles (slug TEXT PRIMARY KEY, result_json TEXT)");
  const rawExtraction = structuredClone(extraction);
  rawExtraction.designSystem.customSections[0].content = "$1e";
  db.prepare("INSERT INTO styles VALUES (?, ?)").run(
    "sample",
    JSON.stringify(rawExtraction),
  );
  db.close();
  process.env.DESIGN_SYSTEMS_REPO = fixture;
});
afterEach(async () => {
  if (originalRepo === undefined) delete process.env.DESIGN_SYSTEMS_REPO;
  else process.env.DESIGN_SYSTEMS_REPO = originalRepo;
  await fs.rm(fixture, { recursive: true, force: true });
});
const request = (query: string) =>
  GET(
    new Request(`http://localhost/api/library/refero/sample/export?${query}`),
    {
      params: Promise.resolve({ source: "refero", slug: "sample" }),
    },
  );

describe("captured Refero export variants", () => {
  it("preserves existing materialized files when no variant is requested", async () => {
    expect(await readExport("refero:sample", "DESIGN.md")).toBe(storedMarkdown);
    expect(await (await request("format=tokens.json")).text()).toBe(
      "stored tokens.json\n",
    );
  });

  it("keeps narrative/components in Compact Markdown and includes token guidance in Extended", async () => {
    const compact = await readExport("refero:sample", "DESIGN.md", "compact");
    const extended = await readExport("refero:sample", "DESIGN.md", "extended");
    expect(compact).toContain("## Components\n\n### Card");
    expect(compact).toContain("### Type Scale");
    expect(compact).toContain("## Do's and Don'ts");
    expect(compact).not.toContain("--color-ink");
    expect(compact).not.toContain("## Quick Start");
    expect(extended).toContain("--color-ink");
    expect(extended).toContain("## Agent Prompt Guide\n\nUse these values.");
    expect(extended).toBe(storedMarkdown);
    expect(extended).not.toContain("$1e");
    expect(extended).toContain("## Quick Start");
    expect(extended).toContain("--spacing-8: 8px");
  });

  it("exports real CSS and Tailwind scales only in Extended", async () => {
    for (const format of ["variables.css", "theme.css"] as const) {
      const compact = await readExport("refero:sample", format, "compact");
      const extended = await readExport("refero:sample", format, "extended");
      expect(compact).toContain("--color-ink: #111111");
      expect(compact).toContain("--font-arial");
      expect(compact).not.toContain("--spacing-8");
      expect(extended).toContain("--text-body: 16px");
      expect(extended).toContain("--spacing-8: 8px");
      expect(extended).toContain("--radius-lg: 8px");
      expect(extended).toContain("--shadow-sm: 0px 2px 8px #00000020");
    }
  });

  it("adds typography, spacing, radii, shadows and surfaces to Extended tokens", async () => {
    const compact = JSON.parse(
      (await readExport("refero:sample", "tokens.json", "compact"))!,
    );
    const extended = JSON.parse(
      (await readExport("refero:sample", "tokens.json", "extended"))!,
    );
    expect(Object.keys(compact)).toEqual(["color", "font", "$extensions"]);
    expect(compact.$extensions["com.refero.extraction"].variant).toBe(
      "compact",
    );
    expect(extended.typography.base.$value.fontSize).toBe("16px");
    expect(extended.spacing["8"].$value).toBe("8px");
    expect(extended.radius.lg.$value).toBe("8px");
    expect(extended.shadow.sm.$value).toBe("0px 2px 8px #00000020");
    expect(extended.surface.canvas.$value).toBe("#ffffff");
    expect(extended.$extensions["com.refero.extraction"].variant).toBe(
      "extended",
    );
  });

  it("validates variants and returns the requested format through the API", async () => {
    for (const variant of ["", "unknown", "COMPACT"])
      expect((await request(`variant=${variant}`)).status).toBe(400);
    const response = await request("format=theme.css&variant=extended");
    expect(response.status).toBe(200);
    expect(response.headers.get("Content-Type")).toBe(
      "text/css; charset=utf-8",
    );
    expect(await response.text()).toContain("@theme {");
  });

  it("never substitutes stored Compact files when the raw extraction is unavailable", async () => {
    await fs.rm(path.join(fixture, "refero/refero.db"));
    const unavailable = await request("format=tokens.json&variant=extended");
    expect(unavailable.status).toBe(404);
    expect((await unavailable.json()).error).toContain("Captured source");
    expect(await readExport("refero:sample", "tokens.json")).toBe(
      "stored tokens.json\n",
    );
    expect(
      await readExport("refero:sample", "../../.env", "extended"),
    ).toBeNull();
  });
});
