import { afterEach, expect, test, vi } from "vitest";
import { promises as fs } from "node:fs";
import os from "node:os";
import path from "node:path";
import {
  getReferenceMedia,
  getReferenceSummary,
  listLibrary,
} from "@/server/sources";
import { validateReferences } from "@/server/research/references";
import { listScreens } from "@/server/sources/screens";

const originalRepo = process.env.DESIGN_SYSTEMS_REPO;
const originalMedia = process.env.DESIGN_SYSTEMS_MEDIA;
const dirs: string[] = [];
afterEach(async () => {
  vi.restoreAllMocks();
  if (originalRepo === undefined) delete process.env.DESIGN_SYSTEMS_REPO;
  else process.env.DESIGN_SYSTEMS_REPO = originalRepo;
  if (originalMedia === undefined) delete process.env.DESIGN_SYSTEMS_MEDIA;
  else process.env.DESIGN_SYSTEMS_MEDIA = originalMedia;
  await Promise.all(
    dirs.splice(0).map((dir) => fs.rm(dir, { recursive: true, force: true })),
  );
});
const PNG = new Uint8Array([137, 80, 78, 71, 13, 10, 26, 10, 1]);
async function fixture(systems: string[]) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), "source-cache-"));
  dirs.push(root);
  process.env.DESIGN_SYSTEMS_REPO = root;
  process.env.DESIGN_SYSTEMS_MEDIA = path.join(root, "media");
  for (const slug of systems) {
    await fs.mkdir(path.join(root, `systems/${slug}/screenshots`), {
      recursive: true,
    });
    await fs.writeFile(
      path.join(root, `systems/${slug}/screenshots/home.png`),
      PNG,
    );
  }
  await writeCatalog(root, systems);
  return root;
}
async function writeCatalog(root: string, systems: string[]) {
  await fs.writeFile(
    path.join(root, "catalog.json"),
    JSON.stringify({
      systems: systems.map((slug) => ({
        slug,
        name: slug[0].toUpperCase() + slug.slice(1),
        platform: "web",
      })),
    }),
  );
}

test("the normalized library stays cached until a catalog changes", async () => {
  const root = await fixture(["alpha"]);
  expect((await listLibrary()).map((item) => item.id)).toEqual([
    "systems:alpha",
  ]);
  const stat = vi.spyOn(fs, "stat"),
    open = vi.spyOn(fs, "open");
  await listLibrary();
  // A cached read stats only the catalog stamps and opens no media file.
  expect(open).not.toHaveBeenCalled();
  expect(stat.mock.calls.length).toBeLessThan(12);
  vi.restoreAllMocks();
  await fs.mkdir(path.join(root, "systems/beta/screenshots"), {
    recursive: true,
  });
  await writeCatalog(root, ["alpha", "beta"]);
  expect((await listLibrary()).map((item) => item.id)).toEqual([
    "systems:alpha",
    "systems:beta",
  ]);
});

test("summary and media lookups answer without building the full detail", async () => {
  await fixture(["alpha"]);
  const summary = await getReferenceSummary("systems:alpha");
  expect(summary).toMatchObject({ id: "systems:alpha", name: "Alpha" });
  expect(summary).not.toHaveProperty("media");
  expect(await getReferenceSummary("systems:missing")).toBeNull();
  expect(await getReferenceSummary("systems:../alpha")).toBeNull();
  const media = await getReferenceMedia("systems:alpha");
  expect(media?.reference.id).toBe("systems:alpha");
  expect(media?.media.map((item) => item.id)).toEqual([
    "systems/alpha/screenshots/home.png",
  ]);
  await expect(
    validateReferences(["systems:alpha"], []),
  ).resolves.toBeUndefined();
  await expect(
    validateReferences(["systems:alpha"], ["systems:missing"]),
  ).rejects.toThrow("Unknown reference: systems:missing");
});

test("a file hydrated in place shows once the cache ages out, with no stamp change", async () => {
  const root = await fixture([]);
  await fs.mkdir(path.join(root, "systems/alpha/screenshots"), {
    recursive: true,
  });
  const cover = path.join(root, "systems/alpha/screenshots/cover.png");
  // An LFS pointer is not usable media, so the card has no image yet.
  await fs.writeFile(
    cover,
    "version https://git-lfs.github.com/spec/v1\noid sha256:00\nsize 9\n",
  );
  await fs.writeFile(
    path.join(root, "catalog.json"),
    JSON.stringify({
      systems: [
        {
          slug: "alpha",
          name: "Alpha",
          platform: "web",
          preview: { cover: "systems/alpha/screenshots/cover.png" },
        },
      ],
    }),
  );
  const start = Date.now();
  const clock = vi.spyOn(Date, "now").mockReturnValue(start);
  expect((await getReferenceSummary("systems:alpha"))?.image).toBeNull();
  await fs.writeFile(cover, PNG);
  clock.mockReturnValue(start + 4 * 60_000);
  expect((await getReferenceSummary("systems:alpha"))?.image).toBeNull();
  clock.mockReturnValue(start + 5 * 60_000 + 1);
  expect((await getReferenceSummary("systems:alpha"))?.image).toBe(
    "/media/systems/alpha/screenshots/cover.png",
  );
});

test("the capture list outlives 30 seconds and rescans when the catalog changes", async () => {
  const root = await fixture(["alpha"]);
  const now = Date.now();
  const clock = vi.spyOn(Date, "now").mockReturnValue(now);
  expect((await listScreens()).total).toBe(1);
  const open = vi.spyOn(fs, "open");
  clock.mockReturnValue(now + 60_000);
  // A minute later the captures are still cached: no screenshot is opened.
  expect((await listScreens()).total).toBe(1);
  expect(open).not.toHaveBeenCalled();
  await fs.mkdir(path.join(root, "systems/beta/screenshots"), {
    recursive: true,
  });
  await fs.writeFile(path.join(root, "systems/beta/screenshots/home.png"), PNG);
  await writeCatalog(root, ["alpha", "beta"]);
  expect((await listScreens()).total).toBe(2);
});
