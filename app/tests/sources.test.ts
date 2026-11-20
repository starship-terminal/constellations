import { afterEach, describe, expect, it, vi } from "vitest";
import { promises as fs } from "node:fs";
import path from "node:path";
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
import {
  parseByteRange,
  notModifiedSince,
  rangeValidatorMatches,
} from "../src/app/media/[...path]/route";
import { tempDir } from "./helpers";
afterEach(() => vi.restoreAllMocks());
const fixture = () => tempDir("design-sources-");

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
    vi.stubEnv("DESIGN_SYSTEMS_REPO", dir);
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
  it("treats If-Modified-Since and If-Range at second precision", () => {
    const mtime = Date.parse("Tue, 04 Nov 2026 12:00:00.900 GMT");
    expect(notModifiedSince("Tue, 04 Nov 2026 12:00:00 GMT", mtime)).toBe(true);
    expect(notModifiedSince("Tue, 04 Nov 2026 11:59:59 GMT", mtime)).toBe(
      false,
    );
    expect(notModifiedSince("Tue, 04 Nov 2026 12:00:01 GMT", mtime)).toBe(true);
    expect(notModifiedSince("not-a-date", mtime)).toBe(false);
    expect(notModifiedSince("", mtime)).toBe(false);
  });
  it("requires an exact date match for If-Range", () => {
    const mtime = Date.parse("Tue, 04 Nov 2026 12:00:00.900 GMT");
    expect(rangeValidatorMatches("Tue, 04 Nov 2026 12:00:00 GMT", mtime)).toBe(
      true,
    );
    expect(rangeValidatorMatches("Tue, 04 Nov 2026 12:00:01 GMT", mtime)).toBe(
      false,
    );
    expect(rangeValidatorMatches("Tue, 04 Nov 2026 11:59:59 GMT", mtime)).toBe(
      false,
    );
    expect(rangeValidatorMatches("not-a-date", mtime)).toBe(false);
  });
});

describe("real library normalization", () => {
  it("shares cold catalog reads between concurrent list and stats requests", async () => {
    const dir = await fixture();
    vi.stubEnv("DESIGN_SYSTEMS_REPO", dir);
    await fs.writeFile(
      path.join(dir, "catalog.json"),
      JSON.stringify({ systems: [] }),
    );
    const catalogPath = await fs.realpath(path.join(dir, "catalog.json"));
    const reads = vi.spyOn(fs, "readFile");
    const [items, stats, again] = await Promise.all([
      listLibrary(),
      getSourceStats(),
      listLibrary(),
    ]);
    expect(items).toEqual([]);
    expect(again).toEqual(items);
    expect(stats).toEqual({ systems: 0, refero: 0 });
    expect(
      reads.mock.calls.filter(([file]) => String(file) === catalogPath),
    ).toHaveLength(1);
  });
  it("clears a rejected shared load so later requests can retry", async () => {
    const dir = await fixture();
    vi.stubEnv("DESIGN_SYSTEMS_REPO", dir);
    await fs.writeFile(
      path.join(dir, "catalog.json"),
      JSON.stringify({ systems: {} }),
    );
    const failed = await Promise.allSettled([listLibrary(), getSourceStats()]);
    expect(failed.every((result) => result.status === "rejected")).toBe(true);
    await fs.writeFile(
      path.join(dir, "catalog.json"),
      JSON.stringify({ systems: [] }),
    );
    expect(await listLibrary()).toEqual([]);
    expect(await getSourceStats()).toEqual({ systems: 0, refero: 0 });
  });
  it("discovers nested canonical screenshots in stable order without escaping the package", async () => {
    const dir = await fixture(),
      outside = await fixture();
    vi.stubEnv("DESIGN_SYSTEMS_REPO", dir);
    const screenshots = path.join(dir, "systems/nested/screenshots");
    await fs.mkdir(path.join(screenshots, "light/deeper"), { recursive: true });
    await fs.mkdir(path.join(screenshots, "dark"), { recursive: true });
    await fs.writeFile(
      path.join(dir, "catalog.json"),
      JSON.stringify({
        systems: [{ slug: "nested", name: "Nested", platform: "mobile" }],
      }),
    );
    const png = Buffer.from(
      "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Wl6Xh8AAAAASUVORK5CYII=",
      "base64",
    );
    // Distinct trailing bytes tell the captures apart.
    const capture = (name: string) => Buffer.concat([png, Buffer.from(name)]);
    for (const name of ["light/z-last.png", "light/deeper/a.png", "dark/b.png"])
      await fs.writeFile(path.join(screenshots, name), capture(name));
    await fs.writeFile(path.join(screenshots, "README.md"), "Not an image");
    await fs.writeFile(path.join(outside, "outside.png"), png);
    await fs.symlink(outside, path.join(screenshots, "escape"));
    await fs.symlink(
      path.join(outside, "outside.png"),
      path.join(screenshots, "linked.png"),
    );
    const detail = await getReference("systems:nested");
    expect(detail?.media.map((m) => m.url)).toEqual([
      "/media/systems/nested/screenshots/dark/b.png",
      "/media/systems/nested/screenshots/light/deeper/a.png",
      "/media/systems/nested/screenshots/light/z-last.png",
    ]);
    expect(detail?.media.map((m) => m.tags)).toEqual([
      ["dark"],
      ["light"],
      ["light"],
    ]);
    // The model receives the first readable capture's bytes as a PNG.
    const vision = await readReferenceImage(detail!);
    expect(vision?.mediaType).toBe("image/png");
    expect(Buffer.from(vision!.data)).toEqual(capture("dark/b.png"));
    // The screenshots root itself must not be a symlink outside this package either.
    await fs.rm(screenshots, { recursive: true });
    await fs.symlink(outside, screenshots);
    expect((await getReference("systems:nested"))?.media).toEqual([]);
  });
  it("retains sampled and derived evidence across source formats", async () => {
    // One invented package holding each provenance shape the captured
    // packages use, so a recapture cannot change what this test reads.
    const dir = await fixture();
    vi.stubEnv("DESIGN_SYSTEMS_REPO", dir);
    await fs.mkdir(path.join(dir, "systems/formats"), { recursive: true });
    await fs.writeFile(
      path.join(dir, "catalog.json"),
      JSON.stringify({
        systems: [{ slug: "formats", name: "Formats", platform: "web" }],
      }),
    );
    const color = (extensions: object) => ({
      $value: "#123456",
      $type: "color",
      $extensions: extensions,
    });
    await fs.writeFile(
      path.join(dir, "systems/formats/tokens.json"),
      JSON.stringify({
        color: {
          sourceObject: color({ source: { evidence: "Sampled" } }),
          sourceString: color({ source: "Derived: nearest declared neutral" }),
          screenshot: color({ source: "Estimated from screenshot pixels" }),
          namespaced: color({
            "com.design-systems.evidence": { status: "Observed" },
          }),
          unstated: color({ source: "Picked by hand" }),
          alias: { $value: "{color.sourceObject}", $type: "color" },
        },
        typography: {
          body: {
            $value: "Inter",
            $type: "fontFamily",
            $extensions: { evidence: "Measured" },
          },
        },
      }),
    );
    const detail = await getReference("systems:formats");
    const evidence = (name: string) =>
      detail?.colors.find((v) => v.name === name)?.evidence;
    expect(evidence("color.sourceObject")).toBe("Sampled");
    expect(evidence("color.sourceString")).toBe("Derived");
    expect(evidence("color.screenshot")).toBe("Sampled");
    expect(evidence("color.namespaced")).toBe("Observed");
    expect(evidence("color.unstated")).toBeUndefined();
    expect(detail?.colors.find((v) => v.name === "color.alias")).toMatchObject({
      value: "#123456",
      evidence: undefined,
    });
    expect(detail?.typography).toEqual([
      expect.objectContaining({
        name: "typography.body",
        evidence: "Measured",
      }),
    ]);
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
  });
  it("never takes a favicon service URL from generated style media", async () => {
    const dir = await fixture();
    vi.stubEnv("DESIGN_SYSTEMS_REPO", dir);
    await fs.mkdir(path.join(dir, "refero/real-style"), { recursive: true });
    await fs.mkdir(path.join(dir, "web/data/refero/style"), {
      recursive: true,
    });
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
    // What tools/catalog.py writes: the favicon's remote is the gstatic URL.
    const gstatic =
      "https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&url=https%3A%2F%2Fexample.com";
    await fs.writeFile(
      path.join(dir, "web/data/refero/style/real-style.json"),
      JSON.stringify({
        media: {
          shot: {
            local: "/refero-media/shots/real-style.jpg",
            remote: "https://example.com/actual.jpg",
          },
          favicon: {
            local: "/refero-media/favicons/real-style.png",
            remote: gstatic,
          },
        },
      }),
    );
    const detail = await getReference("refero:real-style");
    expect(detail?.media.map((item) => item.id)).toEqual(["shot"]);
    expect(JSON.stringify(detail)).not.toContain("gstatic");
  });
  it("uses canonical Refero artifacts when generated files are absent", async () => {
    const dir = await fixture();
    vi.stubEnv("DESIGN_SYSTEMS_REPO", dir);
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
    // No favicon service learns which entries are browsed: with no recorded
    // favicon there is no remote fallback at all.
    expect(items[0].iconFallback).toBeNull();
    expect(JSON.stringify([items, detail])).not.toContain("gstatic");
  });
});
