import { afterEach, describe, expect, it, vi } from "vitest";
import { promises as fs } from "node:fs";
import path from "node:path";
import { getReference } from "../src/server/sources";
import {
  listPackageDocuments,
  readPackageDocument,
  readPackageGuide,
} from "../src/server/sources/files";
import {
  filterPackageMedia,
  mediaDetailHref,
  packageDocumentLink,
  researchDocumentHref,
  safeDecode,
} from "../src/features/package-detail-data";
import { GET as guideGet } from "../src/app/api/packages/[slug]/guide/[...path]/route";
import { repoFixture } from "./helpers";
async function fixture() {
  const dir = await repoFixture("package-parity-");
  await fs.mkdir(path.join(dir, "systems/demo/components/crops"), {
    recursive: true,
  });
  await fs.mkdir(path.join(dir, "systems/demo/screenshots/dark"), {
    recursive: true,
  });
  await fs.mkdir(path.join(dir, "systems/demo/icons"), { recursive: true });
  await fs.mkdir(path.join(dir, "web/data"), { recursive: true });
  await fs.writeFile(
    path.join(dir, "catalog.json"),
    JSON.stringify({
      systems: [
        {
          slug: "demo",
          name: "Demo",
          entry: "systems/demo/README.md",
          styleGuide: "systems/demo/style-guide.html",
          themes: ["light", "dark-experimental"],
          widths: [1440, 1000, 390],
        },
      ],
    }),
  );
  await fs.writeFile(
    path.join(dir, "systems/demo/README.md"),
    "# Complete README\n\n## Capture\n\nA paragraph the bullet extractor lost.\n\n[Patterns](patterns.md)",
  );
  await fs.writeFile(path.join(dir, "systems/demo/patterns.md"), "# Patterns");
  await fs.writeFile(path.join(dir, "systems/demo/tokens.json"), "{}");
  await fs.writeFile(
    path.join(dir, "systems/demo/style-guide.html"),
    "<html><script>window.guide=true</script><p>Guide</p></html>",
  );
  const shot = "systems/demo/screenshots/dark/settings.png",
    crop = "systems/demo/components/crops/menu-hover.svg";
  await fs.writeFile(path.join(dir, shot), "hydrated image");
  await fs.writeFile(path.join(dir, crop), "<svg></svg>");
  // Deliberately exceed the old 96-icon generated preview limit.
  await Promise.all(
    Array.from({ length: 100 }, (_, i) =>
      fs.writeFile(
        path.join(dir, `systems/demo/icons/${String(i).padStart(3, "0")}.svg`),
        "<svg></svg>",
      ),
    ),
  );
  await fs.writeFile(
    path.join(dir, "web/data/data.json"),
    JSON.stringify({
      systems: [
        {
          slug: "demo",
          screenshots: [
            {
              path: shot,
              name: "Settings",
              group: "screenshots/dark",
              tags: ["dark"],
            },
          ],
          components: [
            {
              path: crop,
              name: "Menu hover",
              group: "components/crops",
              tags: ["light"],
            },
          ],
          typeStyles: [{ name: "body", size: "14px", lineHeight: "20px" }],
          shadows: [{ token: "light.shadow", css: "0 1px 2px #000" }],
          swatches: {
            light: [{ role: "text", token: "light.text", value: "#111111" }],
          },
          tokenTheme: "light",
          icons: { total: 100, items: [] },
        },
      ],
    }),
  );
  return dir;
}
afterEach(() => vi.restoreAllMocks());
describe("measured package parity", () => {
  it("reads the README once and never reads an export just to link it", async () => {
    const dir = await fixture();
    await fs.writeFile(
      path.join(dir, "systems/demo/README.md"),
      "# Demo\n\n- Keep the density\n",
    );
    await fs.writeFile(path.join(dir, "systems/demo/DESIGN.md"), "# Demo");
    const reads = vi.spyOn(fs, "readFile");
    const detail = await getReference("systems:demo");
    expect(detail?.guidelines).toEqual(["Keep the density"]);
    expect(Object.keys(detail?.exports || {}).sort()).toEqual([
      "DESIGN.md",
      "tokens.json",
    ]);
    const read = (name: string) =>
      reads.mock.calls.filter(([file]) =>
        String(file).endsWith(`systems/demo/${name}`),
      ).length;
    expect(read("README.md")).toBe(1);
    expect(read("DESIGN.md")).toBe(0);
    expect(read("tokens.json")).toBe(1);
  });
  it("preserves all media kinds, stable original identity and structured previews", async () => {
    await fixture();
    const detail = await getReference("systems:demo");
    expect(detail?.measured?.screenshots).toHaveLength(1);
    expect(detail?.measured?.screenshots[0]).toMatchObject({
      id: "systems/demo/screenshots/dark/settings.png",
      kind: "screenshot",
      group: "screenshots/dark",
      tags: ["dark"],
    });
    expect(detail?.measured?.crops[0]).toMatchObject({
      kind: "crop",
      name: "Menu hover",
    });
    expect(detail?.measured?.icons).toHaveLength(100);
    expect(detail?.measured?.readme).toContain(
      "A paragraph the bullet extractor lost",
    );
    expect(detail?.measured?.typeStyles[0]).toMatchObject({
      size: "14px",
      lineHeight: "20px",
    });
    expect(detail?.measured?.shadows[0].css).toBe("0 1px 2px #000");
    expect(detail?.measured?.widths).toEqual(["1440", "1000", "390"]);
    expect(detail?.measured?.styleGuide).toBe(
      "/api/packages/demo/guide/style-guide.html",
    );
  });
  it("lists readable documents and rejects private paths, traversal, foreign roots and escaped symlinks", async () => {
    const dir = await fixture();
    await fs.mkdir(path.join(dir, "systems/demo/raw"));
    await fs.writeFile(path.join(dir, "systems/demo/raw/secret.json"), "{}");
    await fs.writeFile(path.join(dir, "systems/demo/.env"), "SECRET=x");
    await fs.writeFile(path.join(dir, "outside.md"), "private");
    await fs.symlink(
      path.join(dir, "outside.md"),
      path.join(dir, "systems/demo/leak.md"),
    );
    const docs = await listPackageDocuments("systems:demo");
    expect(docs.some((d) => d.path === "tokens.json")).toBe(true);
    expect(docs.some((d) => /raw|env|leak/.test(d.path))).toBe(false);
    for (const name of [
      "../outside.md",
      "raw/secret.json",
      ".env",
      "leak.md",
      "/etc/passwd",
      "patterns.md\0",
    ])
      expect(await readPackageDocument("systems:demo", name)).toBeNull();
    expect(
      await readPackageDocument("systems:unknown", "README.md"),
    ).toBeNull();
    expect(await readPackageDocument("refero:demo", "README.md")).toBeNull();
    expect(
      (await readPackageDocument("systems:demo", "README.md"))?.format,
    ).toBe("markdown");
  });
  it("serves HTML in an opaque sandbox and never serves raw, scripts or traversal as guide resources", async () => {
    await fixture();
    const response = await guideGet(
      new Request("http://localhost/api/packages/demo/guide/style-guide.html"),
      { params: Promise.resolve({ slug: "demo", path: ["style-guide.html"] }) },
    );
    expect(response.status).toBe(200);
    const policy = response.headers.get("Content-Security-Policy")!;
    expect(policy).toContain("sandbox allow-scripts");
    expect(policy).not.toContain("allow-same-origin");
    expect(policy).toContain("connect-src 'none'");
    const readme = await readPackageGuide("systems:demo", "README.md");
    expect(readme?.mime).toBe("text/plain; charset=utf-8");
    expect(
      (
        await readPackageGuide(
          "systems:demo",
          "components/crops/menu-hover.svg",
        )
      )?.mime,
    ).toBe("image/svg+xml");
    expect(new TextDecoder().decode(readme?.body)).toContain("Complete README");
    expect((await readPackageGuide("systems:demo", "tokens.json"))?.mime).toBe(
      "text/plain; charset=utf-8",
    );
    for (const relative of [
      "../outside.md",
      "raw/secret.json",
      "tools/private.env",
      ".env",
    ])
      expect(await readPackageGuide("systems:demo", relative)).toBeNull();
  });
});
describe("package navigation", () => {
  it("filters every media item, including named states beyond the first page", () => {
    const items = Array.from({ length: 80 }, (_, i) => ({
      id: `shot-${i}`,
      name: `screen-${i}${i === 79 ? " hover" : ""}`,
      url: `/media/${i}.png`,
      type: "image" as const,
      tags: i % 2 ? ["dark"] : ["light"],
      group: "screenshots",
    }));
    expect(filterPackageMedia(items, "hover", "dark").map((m) => m.id)).toEqual(
      ["shot-79"],
    );
    expect(mediaDetailHref("demo", items[79])).toBe(
      "/library/demo?tab=screenshots&media=shot-79",
    );
  });
  it("links research document tools to the package file reader, not the JSON API", () => {
    expect(
      researchDocumentHref(
        "systems:linear",
        "components.md",
        "/api/packages/linear/files?path=components.md",
      ),
    ).toBe("/library/linear?tab=files&file=components.md");
    expect(researchDocumentHref("refero:x", "a.md", "/fallback")).toBe(
      "/fallback",
    );
    expect(researchDocumentHref(undefined, "a.md", "/fallback")).toBe(
      "/fallback",
    );
  });
  it("resolves package markdown files and images, keeping unsafe URLs and traversal out", () => {
    expect(packageDocumentLink("demo", "README.md", "patterns.md#menus")).toBe(
      "/library/demo?tab=files&file=patterns.md#menus",
    );
    expect(
      packageDocumentLink(
        "demo",
        "components/notes.md",
        "../screenshots/light/home.png",
        true,
      ),
    ).toBe("/media/systems/demo/screenshots/light/home.png");
    expect(
      packageDocumentLink("demo", "README.md", "javascript:alert(1)"),
    ).toBeUndefined();
    expect(
      packageDocumentLink("demo", "README.md", "../../.env"),
    ).toBeUndefined();
    expect(
      packageDocumentLink(
        "demo",
        "README.md",
        "https://tracker.test/image",
        true,
      ),
    ).toBeUndefined();
  });
  it("keeps a malformed percent escape in a package link instead of throwing", () => {
    expect(packageDocumentLink("demo", "README.md", "50%off.md")).toBe(
      "/library/demo?tab=files&file=50%25off.md",
    );
    expect(packageDocumentLink("demo", "README.md", "50%off.png", true)).toBe(
      "/media/systems/demo/50%25off.png",
    );
    expect(safeDecode("a%20b")).toBe("a b");
    expect(safeDecode("50%off")).toBe("50%off");
  });
});

describe("interpreted source contract", () => {
  it("keeps all six media kinds, poster/fallback links and canonical design data without generated artifacts", async () => {
    const dir = await fixture();
    await fs.mkdir(path.join(dir, "refero/actual"), { recursive: true });
    await fs.writeFile(
      path.join(dir, "refero/catalog.json"),
      JSON.stringify({
        styles: [
          {
            slug: "actual",
            name: "Actual",
            product_type: "saas",
            design_style: "swiss",
            theme: "mixed",
            tags: ["editorial"],
          },
          {
            slug: "similar",
            name: "Similar Product",
            product_type: "saas",
            design_style: "swiss",
            theme: "light",
          },
        ],
      }),
    );
    await fs.writeFile(
      path.join(dir, "refero/actual/meta.json"),
      JSON.stringify({
        source_url: "https://example.com",
        page_url: "https://styles.refero.design/style/actual",
        screenshot_url: "https://example.com/shot.jpg",
        video_url: "https://example.com/video.mp4",
        video_poster_url: "https://example.com/poster.jpg",
        video_detail_url: "https://example.com/detail.mp4",
        video_detail_poster_url: "https://example.com/detail-poster.jpg",
        // The favicon Refero recorded; with none there is no favicon entry
        // (no favicon service fallback).
        favicon_url: "https://example.com/favicon.png",
      }),
    );
    const design = {
      description: "Complete",
      typeScale: [{ role: "display", size: "64px" }],
      components: [{ name: "Button", html: "<button>Start</button>" }],
      similar: [{ business: "Similar Product", why: "Same rhythm" }],
      elevationPhilosophy: "Flat",
    };
    await fs.writeFile(
      path.join(dir, "refero/actual/design-system.json"),
      JSON.stringify(design),
    );
    const detail = await getReference("refero:actual");
    expect(detail?.media.map((m) => m.kind)).toEqual([
      "shot",
      "poster",
      "video",
      "detail",
      "detail_poster",
      "favicon",
    ]);
    expect(detail?.media.find((m) => m.kind === "video")).toMatchObject({
      poster: "https://example.com/poster.jpg",
      fallback: "https://example.com/video.mp4",
    });
    expect(detail?.media.find((m) => m.kind === "detail")?.poster).toBe(
      "https://example.com/detail-poster.jpg",
    );
    expect(detail?.interpreted?.designSystem).toEqual(design);
    expect(detail?.interpreted?.similar).toEqual([
      { slug: "similar", name: "Similar Product", why: "Same rhythm" },
    ]);
    expect(detail?.productType).toBe("saas");
    expect(detail?.designStyle).toBe("swiss");
    expect(detail?.themes).toEqual(["mixed"]);
    expect(detail?.imageFallback).toBe("https://example.com/poster.jpg");
  });
});
