import { afterEach, describe, expect, it } from "vitest";
import { promises as fs } from "node:fs";
import path from "node:path";
import os from "node:os";
import {
  getReference,
  getSourceStats,
  listLibrary,
  parseReferenceId,
  readExport,
  readReferenceImage,
} from "../src/server/sources";
import {
  boundedFile,
  readLocalImage,
  remoteUrl,
  repoRoot,
  resolveMedia,
} from "../src/server/sources/files";
import { parseByteRange } from "../src/app/media/[...path]/route";
const originalRepo = process.env.DESIGN_SYSTEMS_REPO;
const originalMedia = process.env.DESIGN_SYSTEMS_MEDIA;
const temp: string[] = [];
afterEach(async () => {
  if (originalRepo === undefined) delete process.env.DESIGN_SYSTEMS_REPO;
  else process.env.DESIGN_SYSTEMS_REPO = originalRepo;
  if (originalMedia === undefined) delete process.env.DESIGN_SYSTEMS_MEDIA;
  else process.env.DESIGN_SYSTEMS_MEDIA = originalMedia;
  await Promise.all(
    temp.splice(0).map((dir) => fs.rm(dir, { recursive: true, force: true })),
  );
});
async function fixture() {
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), "design-sources-"));
  temp.push(dir);
  return dir;
}

describe("source identifiers and file boundaries", () => {
  it("accepts known source IDs and rejects traversal or extra separators", () => {
    expect(parseReferenceId("systems:linear")).toEqual({
      source: "systems",
      slug: "linear",
    });
    for (const id of [
      "systems:../secret",
      "refero:a/b",
      "systems:a:b",
      "unknown:linear",
      "refero:",
      "systems:%2e%2e",
    ])
      expect(parseReferenceId(id)).toBeNull();
  });
  it("rejects lexical traversal and symlinks that escape an allowed root", async () => {
    const dir = await fixture(),
      outside = await fixture();
    await fs.writeFile(path.join(outside, "secret.png"), "private");
    await fs.symlink(
      path.join(outside, "secret.png"),
      path.join(dir, "link.png"),
    );
    await fs.writeFile(path.join(dir, "valid.png"), "image");
    expect(await boundedFile(dir, "../secret.png")).toBeNull();
    expect(await boundedFile(dir, "link.png")).toBeNull();
    expect(await boundedFile(dir, "valid.png")).toBe(
      await fs.realpath(path.join(dir, "valid.png")),
    );
  });
  it("serves hydrated media only and never exposes text or LFS pointers", async () => {
    const dir = await fixture();
    process.env.DESIGN_SYSTEMS_REPO = dir;
    await fs.mkdir(path.join(dir, "systems/test"), { recursive: true });
    await fs.writeFile(path.join(dir, "systems/test/README.md"), "secret");
    await fs.writeFile(
      path.join(dir, "systems/test/icon.png"),
      "version https://git-lfs.github.com/spec/v1\noid sha256:test",
    );
    expect(await resolveMedia(["systems", "test", "README.md"])).toBeNull();
    expect(await resolveMedia(["systems", "test", "icon.png"])).toBeNull();
    expect(await resolveMedia(["systems", "..", "catalog.json"])).toBeNull();
    expect(await readLocalImage("https://example.com/a.png")).toBeNull();
  });
  it("accepts only safe remote web URLs", () => {
    expect(remoteUrl("https://example.com/image.png")).toBe(
      "https://example.com/image.png",
    );
    for (const value of [
      "javascript:alert(1)",
      "file:///etc/passwd",
      "data:image/png;base64,abc",
      "https://user:pass@example.com/a",
    ])
      expect(remoteUrl(value)).toBeNull();
  });
});

describe("HTTP range parsing", () => {
  it("supports closed, open and suffix ranges, clamps end, rejects invalid ranges", () => {
    expect(parseByteRange("bytes=0-9", 100)).toEqual({ start: 0, end: 9 });
    expect(parseByteRange("bytes=90-", 100)).toEqual({ start: 90, end: 99 });
    expect(parseByteRange("bytes=-10", 100)).toEqual({ start: 90, end: 99 });
    expect(parseByteRange("bytes=90-1000", 100)).toEqual({
      start: 90,
      end: 99,
    });
    for (const input of [
      "bytes=100-",
      "bytes=5-4",
      "bytes=-0",
      "bytes=0-1,3-4",
      "bytes=-",
      "garbage",
    ])
      expect(parseByteRange(input, 100)).toBeNull();
  });
});

describe("real library normalization", () => {
  it("retains sampled and derived evidence across source formats", async () => {
    const [hevy, telegram, manus, duolingo, linear] = await Promise.all([
      getReference("systems:hevy"),
      getReference("systems:telegram"),
      getReference("systems:manus"),
      getReference("systems:duolingo"),
      getReference("systems:linear"),
    ]);
    expect(
      hevy?.colors.find((v) => v.name === "light.color.bg.page")?.evidence,
    ).toBe("Sampled");
    expect(
      telegram?.colors.find((v) => v.name === "core.color.iconTile.blue")
        ?.evidence,
    ).toBe("Derived");
    expect(
      manus?.colors.find((v) => v.name === "core.palette.neutral.50")?.evidence,
    ).toBe("Derived");
    expect(
      duolingo?.colors.find((v) => v.name === "light.ramp.neutral.100")
        ?.evidence,
    ).toBe("Derived");
    expect(linear?.typography.some((v) => v.evidence === "Measured")).toBe(
      true,
    );
  });
  it("counts the actual measured packages and Refero styles", async () => {
    const catalog = JSON.parse(
      await fs.readFile(path.join(repoRoot(), "catalog.json"), "utf8"),
    );
    const refero = JSON.parse(
      await fs.readFile(path.join(repoRoot(), "refero/catalog.json"), "utf8"),
    );
    expect(await getSourceStats()).toEqual({
      systems: catalog.systems.length,
      refero: refero.styles.length,
    });
    expect(
      (await listLibrary({ source: "systems" })).every(
        (item) => item.evidence === "measured",
      ),
    ).toBe(true);
    expect(
      (await listLibrary({ source: "refero", limit: 20 })).every(
        (item) => item.evidence === "interpreted",
      ),
    ).toBe(true);
  });
  it("filters before paginating and returns actual source evidence", async () => {
    const items = await listLibrary({ source: "systems", query: "linear" });
    expect(items.some((item) => item.id === "systems:linear")).toBe(true);
    expect(
      await listLibrary({
        source: "systems",
        query: "linear",
        offset: 1,
        limit: 1,
      }),
    ).toEqual(items.slice(1, 2));
    const detail = await getReference("systems:linear");
    expect(detail?.colors.length).toBeGreaterThan(0);
    expect(
      detail?.typography.some((value) => value.evidence === "Measured"),
    ).toBe(true);
    expect(await getReference("systems:not-a-real-package")).toBeNull();
    expect(await getReference("systems:../catalog")).toBeNull();
    const exported = await readExport("systems:linear", "tokens.json");
    expect(exported).toBe(
      await fs.readFile(
        path.join(repoRoot(), "systems/linear/tokens.json"),
        "utf8",
      ),
    );
    expect(await readExport("systems:linear", "../../.env")).toBeNull();
    if (detail?.image) {
      const vision = await readReferenceImage(detail);
      if (vision)
        expect(vision.data.byteLength).toBeLessThanOrEqual(5 * 1024 * 1024);
    }
  });
  it("uses canonical Refero artifacts when generated files are absent", async () => {
    const dir = await fixture();
    process.env.DESIGN_SYSTEMS_REPO = dir;
    await fs.mkdir(path.join(dir, "refero/real-style"), { recursive: true });
    await fs.writeFile(
      path.join(dir, "catalog.json"),
      JSON.stringify({ systems: [] }),
    );
    await fs.writeFile(
      path.join(dir, "refero/catalog.json"),
      JSON.stringify({
        styles: [
          {
            slug: "real-style",
            name: "Real",
            theme: "dark",
            source_url: "https://example.com",
          },
        ],
      }),
    );
    await fs.writeFile(
      path.join(dir, "refero/real-style/meta.json"),
      JSON.stringify({
        screenshot_url: "https://example.com/actual.jpg",
        source_url: "https://example.com",
      }),
    );
    await fs.writeFile(
      path.join(dir, "refero/real-style/DESIGN.md"),
      "# Stored reference",
    );
    await fs.writeFile(
      path.join(dir, "refero/real-style/design-system.json"),
      JSON.stringify({
        description: "Stored description",
        colors: [{ name: "Ink", hex: "#112233" }],
      }),
    );
    const items = await listLibrary();
    expect(items).toHaveLength(1);
    expect(items[0].image).toBe("https://example.com/actual.jpg");
    const detail = await getReference("refero:real-style");
    expect(detail?.descriptionLong).toBe("Stored description");
    expect(detail?.colors[0]).toMatchObject({
      value: "#112233",
      evidence: "interpreted",
    });
    expect(await readExport("refero:real-style", "DESIGN.md")).toBe(
      "# Stored reference",
    );
    expect(detail?.exports).not.toHaveProperty("variables.css");
  });
});
