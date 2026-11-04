import { afterEach, describe, expect, it, vi } from "vitest";
import { promises as fs } from "node:fs";
import os from "node:os";
import path from "node:path";
import type { LibraryItem } from "../src/contracts/library";
import type { ScreenItem } from "../src/contracts/screens";
import { listScreens, queryScreens } from "../src/server/sources/screens";
import { GET } from "../src/app/api/library/screens/route";
import { categoryGroup } from "../src/contracts/categories";

const originalRepo = process.env.DESIGN_SYSTEMS_REPO;
const temp: string[] = [];
afterEach(async () => {
  vi.restoreAllMocks();
  if (originalRepo === undefined) delete process.env.DESIGN_SYSTEMS_REPO;
  else process.env.DESIGN_SYSTEMS_REPO = originalRepo;
  await Promise.all(
    temp.splice(0).map((dir) => fs.rm(dir, { recursive: true, force: true })),
  );
});
const reference: LibraryItem = {
  id: "systems:workspace",
  source: "systems",
  slug: "workspace",
  name: "Workspace",
  description: "Project management",
  platform: "web",
  category: "productivity",
  tags: ["dense"],
  themes: ["light", "dark"],
  image: null,
  icon: null,
  video: null,
  evidence: "measured",
  captured: "2026-11-01",
};
function screen(
  name: string,
  kind: "screenshot" | "crop" = "screenshot",
  tags = ["dark"],
): ScreenItem {
  const mediaId = `systems/workspace/${kind === "crop" ? "components" : "screenshots"}/${name}.png`;
  return {
    id: `${reference.id}:${mediaId}`,
    reference,
    media: {
      id: mediaId,
      path: mediaId,
      name,
      kind,
      tags,
      type: "image",
      group: kind === "crop" ? "components/crops" : "screenshots/dark",
      url: `/media/${mediaId}`,
    },
  };
}

describe("capture search", () => {
  it.each([
    ["learning", "education"],
    ["fintech", "finance"],
    ["ecommerce", "commerce"],
    ["entertainment", "media"],
  ])(
    "preserves the Apps category group %s when browsing Screens as %s",
    (raw, group) => {
      const capture = {
        ...screen("capture"),
        reference: { ...reference, category: raw },
      };
      const appsCategory = categoryGroup(raw);
      expect(appsCategory).toBe(group);
      expect(queryScreens([capture], { category: appsCategory }).items).toEqual(
        [capture],
      );
      expect(queryScreens([capture], { category: raw }).items).toEqual([
        capture,
      ]);
      const facet = queryScreens([capture]).facets.categories[0];
      expect(facet).toEqual({ value: group, count: 1 });
      expect(queryScreens([capture], { category: facet.value }).items).toEqual([
        capture,
      ]);
      const canonicalCapture = {
        ...capture,
        reference: { ...capture.reference, category: group },
      };
      expect(
        queryScreens([capture, canonicalCapture]).facets.categories,
      ).toEqual([{ value: group, count: 2 }]);
    },
  );
  it("recovers an exact screenshot or crop beyond the first page while preserving explicit filters", () => {
    const items = Array.from({ length: 130 }, (_, index) =>
      screen(`capture-${String(index).padStart(3, "0")}`),
    );
    const target = items[120];
    expect(queryScreens(items).items).not.toContain(target);
    expect(
      queryScreens(items, { screenId: target.id, offset: 500, limit: 0 }).items,
    ).toEqual([target]);
    expect(
      queryScreens(items, { screenId: target.id, platform: "mobile" }).items,
    ).toEqual([]);
    expect(
      queryScreens(items, { screenId: `${target.id}-missing` }).total,
    ).toBe(0);
    const crop = screen("button-hover", "crop");
    expect(queryScreens([crop], { screenId: crop.id }).items).toEqual([crop]);
    expect(
      queryScreens([crop], { screenId: crop.id, kind: "screenshot" }).items,
    ).toEqual([]);
  });
  it("keeps package descriptions and tags out of searches scoped to captured names", () => {
    const unrelated = {
      ...screen("repo-agents-list"),
      reference: {
        ...reference,
        description: "Dashboard workspaces",
        tags: ["dashboard"],
      },
    };
    const dashboard = screen("dashboard-filter-menu");
    expect(
      queryScreens([unrelated, dashboard], { query: "dashboard" }).total,
    ).toBe(2);
    expect(
      queryScreens([unrelated, dashboard], {
        query: "dashboard",
        scope: "media",
      }).items,
    ).toEqual([dashboard]);
  });
  it("finds actual screens across package boundaries and preserves original identity", () => {
    const dashboard = screen("dashboard-filter-menu");
    const profile = screen("profile-settings");
    const result = queryScreens([dashboard, profile], {
      query: "dashboard filter",
    });
    expect(result.items).toEqual([dashboard]);
    expect(result.total).toBe(1);
    expect(result.taxonomy).toEqual({
      pageTypes: [],
      uiElements: [],
      uxPatterns: [],
    });
    expect(
      queryScreens([dashboard, profile], { query: "invented pattern" }).items,
    ).toEqual([]);
  });
  it("applies actual capture facets, prefers capture theme over a mixed package, and separates components", () => {
    const items = [
      screen("home-dark"),
      screen("home-light", "screenshot", ["light"]),
      screen("button-hover", "crop"),
    ];
    expect(queryScreens(items, { theme: "dark" }).total).toBe(1);
    expect(
      queryScreens(items, {
        category: "productivity",
        tag: "dense",
        platform: "web",
      }).total,
    ).toBe(2);
    expect(queryScreens(items, { group: "missing" }).total).toBe(0);
    expect(
      queryScreens(items, { kind: "crop", query: "button" }).items[0].media
        .kind,
    ).toBe("crop");
    expect(queryScreens(items).facets.kinds).toEqual([
      { value: "screenshot", count: 2 },
      { value: "crop", count: 1 },
    ]);
  });
  it("orders the complete result before pagination and bounds payload sizes", () => {
    const older = {
      ...screen("zebra"),
      reference: { ...reference, captured: "2026-10-01" },
    };
    const newer = screen("alpha");
    expect(queryScreens([older, newer], { offset: 1, limit: 1 }).items).toEqual(
      [older],
    );
    expect(
      queryScreens([older, newer], { sort: "name", limit: 1 }).items,
    ).toEqual([newer]);
    expect(
      queryScreens(
        Array.from({ length: 230 }, (_, i) => screen(`capture-${i}`)),
        { limit: 1000 },
      ).items,
    ).toHaveLength(200);
    expect(queryScreens([newer], { limit: 0 }).items).toEqual([]);
  });
});

describe("capture source and API", () => {
  it("shares cached metadata reads, scans missing manifests, rejects escaping assets, and never reads package docs/tokens", async () => {
    const dir = await fs.mkdtemp(path.join(os.tmpdir(), "screen-index-"));
    temp.push(dir);
    process.env.DESIGN_SYSTEMS_REPO = dir;
    const screenshots = path.join(dir, "systems/workspace/screenshots");
    await fs.mkdir(screenshots, { recursive: true });
    await fs.writeFile(
      path.join(screenshots, "dashboard-dark.png"),
      "hydrated image",
    );
    await fs.writeFile(
      path.join(screenshots, "unavailable.png"),
      "version https://git-lfs.github.com/spec/v1\noid sha256:test",
    );
    await fs.writeFile(path.join(dir, "outside.png"), "private image");
    await fs.symlink(
      path.join(dir, "outside.png"),
      path.join(screenshots, "escape.png"),
    );
    await fs.writeFile(
      path.join(dir, "catalog.json"),
      JSON.stringify({
        systems: [
          {
            slug: "workspace",
            name: "Workspace",
            platform: "web",
            category: "productivity",
          },
        ],
      }),
    );
    await fs.mkdir(path.join(dir, "refero"));
    await fs.writeFile(
      path.join(dir, "refero/catalog.json"),
      JSON.stringify({ styles: [] }),
    );
    const reads = vi.spyOn(fs, "readFile");
    const [first, second] = await Promise.all([
      listScreens({ query: "dashboard" }),
      listScreens(),
    ]);
    expect(first.total).toBe(1);
    expect(second.items[0].media.id).toBe(
      "systems/workspace/screenshots/dashboard-dark.png",
    );
    const readCount = reads.mock.calls.length;
    await listScreens({ query: "dark" });
    expect(reads.mock.calls.length).toBe(readCount);
    expect(
      reads.mock.calls.some(([file]) =>
        /(?:tokens\.json|README\.md)$/.test(String(file)),
      ),
    ).toBe(false);
    const response = await GET(
      new Request(
        "http://studio.test/api/library/screens?q=dashboard&limit=1&order=name",
      ),
    );
    expect(response.status).toBe(200);
    expect((await response.json()).items).toHaveLength(1);
    const recovered = await GET(
      new Request(
        `http://studio.test/api/library/screens?screenId=${encodeURIComponent(first.items[0].id)}&offset=999&limit=0`,
      ),
    );
    expect(recovered.status).toBe(200);
    expect((await recovered.json()).items[0].id).toBe(first.items[0].id);
  });
  it("rejects invalid pagination, kind, order and non-capture source IDs before loading", async () => {
    for (const query of [
      "offset=-1",
      "limit=NaN",
      "offset=1.5",
      "kind=flow",
      "sort=popular",
      "scope=visual",
      "referenceId=refero:apple",
      "referenceId=systems:../secret",
      "screenId=refero:apple:shot",
      "screenId=systems:one:systems/two/screenshots/image.png",
      "screenId=systems:one:systems/one/screenshots/../private.png",
    ])
      expect(
        (
          await GET(
            new Request(`http://studio.test/api/library/screens?${query}`),
          )
        ).status,
      ).toBe(400);
  });
});
