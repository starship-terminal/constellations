import { afterEach, describe, expect, it, vi } from "vitest";
import { promises as fs } from "node:fs";
import path from "node:path";
import type { ScreenItem } from "../src/contracts/screens";
import { listScreens, queryScreens } from "../src/server/sources/screens";
import { GET } from "../src/app/api/library/screens/route";
import { categoryGroup } from "../src/contracts/categories";
import { getStore } from "../src/server/db";
import { libraryItem, repoFixture } from "./helpers";

afterEach(() => vi.restoreAllMocks());
const reference = libraryItem("workspace", {
  name: "Workspace",
  description: "Project management",
  category: "productivity",
  tags: ["dense"],
  themes: ["light", "dark"],
  captured: "2026-11-01",
});
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
  it("requires every selected term on the same capture, including terms in one group", () => {
    const signup = "web-page-types:sign-up";
    const login = "web-page-types:log-in";
    const button = "web-ui-elements:button";
    const first = { ...screen("signup"), termIds: [signup, button] };
    const second = { ...screen("login"), termIds: [login] };
    const both = {
      ...screen("combined-auth"),
      termIds: [signup, login, button],
    };
    expect(
      queryScreens([first, second, both], { termIds: [signup, login] }).items,
    ).toEqual([both]);
    expect(
      queryScreens([first, second, both], { termIds: [signup, button] }).items,
    ).toEqual([both, first]);
    expect(
      queryScreens([first, second], { termIds: [signup, login] }).total,
    ).toBe(0);
    expect(queryScreens([both], { termIds: [signup, signup] }).total).toBe(1);
  });
  it("combines reference categories with exact capture fonts and media classifications", () => {
    const category = "web-categories:productivity";
    const font = "web-fonts:inter";
    const button = "web-ui-elements:button";
    const capture = {
      ...screen("settings"),
      reference: { ...reference, categoryIds: [category] },
      termIds: [font, button],
    };
    const unrelated = { ...screen("different-settings"), termIds: [button] };
    expect(
      queryScreens([capture, unrelated], { termIds: [category, font, button] })
        .items,
    ).toEqual([capture]);
    expect(
      queryScreens([capture], { termIds: ["ios-categories:productivity"] })
        .total,
    ).toBe(0);
  });
  it("combines selected packages with OR and keeps picker counts global within platform and kind", () => {
    const term = "web-ui-elements:button";
    const first = { ...screen("one"), termIds: [term, term] };
    const second = {
      ...screen("two"),
      reference: { ...reference, id: "systems:second" },
      termIds: [term],
    };
    const mobile = {
      ...screen("phone"),
      reference: { ...reference, platform: "mobile", id: "systems:phone" },
      termIds: [term],
    };
    const crop = { ...screen("button", "crop"), termIds: [term] };
    const items = [first, second, mobile, crop];
    const result = queryScreens(items, {
      platform: "web",
      referenceIds: [reference.id, "systems:second"],
      termIds: [term],
      limit: 1,
    });
    expect(result.total).toBe(2);
    expect(result.items).toHaveLength(1);
    expect(result.termCounts).toEqual({ [term]: 2 });
    expect(
      queryScreens(items, {
        platform: "web",
        referenceIds: [reference.id],
        query: "missing",
        termIds: ["web-page-types:dashboard"],
      }).termCounts,
    ).toEqual({ [term]: 2 });
    expect(queryScreens(items, { platform: "mobile" }).termCounts).toEqual({
      [term]: 1,
    });
    expect(queryScreens(items, { kind: "crop" }).termCounts).toEqual({
      [term]: 1,
    });
    expect(
      queryScreens(items, {
        referenceIds: [reference.id, "systems:second"],
      }).total,
    ).toBe(2);
  });
  it("returns no flows or flow counts without verified ordered sequences", () => {
    const screenshot = {
      ...screen("onboarding-step"),
      termIds: ["web-flows:onboarding"],
    };
    const crop = screen("form", "crop");
    const result = queryScreens([screenshot, crop], { mode: "flows" });
    expect(result.items).toEqual([]);
    expect(result.total).toBe(0);
    expect(result.termCounts).toEqual({});
    expect(result.facets.kinds).toEqual([]);
  });
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
    expect(result).not.toHaveProperty("taxonomy");
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
    const dir = await repoFixture("screen-index-");
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
    const store = await getStore();
    const mediaId = first.items[0].media.id;
    const dashboardTerm = "web-page-types:dashboard";
    const buttonTerm = "web-ui-elements:button";
    try {
      for (const termId of [dashboardTerm, buttonTerm])
        await store.client.execute({
          sql: "INSERT INTO media_term_assignments(reference_id,media_id,term_id,reason,origin) VALUES(?,?,?,'Verified test fixture','manual')",
          args: [reference.id, mediaId, termId],
        });
      const filtered = await GET(
        new Request(
          `http://studio.test/api/library/screens?term=${dashboardTerm}&term=${buttonTerm}&referenceId=systems:missing&referenceId=${reference.id}`,
        ),
      );
      expect(filtered.status).toBe(200);
      const filteredBody = await filtered.json();
      expect(filteredBody.total).toBe(1);
      expect(filteredBody.termCounts).toEqual({
        [dashboardTerm]: 1,
        [buttonTerm]: 1,
      });
      await store.client.execute({
        sql: "DELETE FROM media_term_assignments WHERE reference_id=? AND media_id=? AND term_id=?",
        args: [reference.id, mediaId, buttonTerm],
      });
      // Classification changes must bypass the longer-lived capture metadata cache.
      const changed = await GET(
        new Request(
          `http://studio.test/api/library/screens?term=${dashboardTerm}&term=${buttonTerm}`,
        ),
      );
      const changedBody = await changed.json();
      expect(changedBody.total).toBe(0);
      expect(changedBody.termCounts).toEqual({ [dashboardTerm]: 1 });
      const flows = await GET(
        new Request("http://studio.test/api/library/screens?mode=flows"),
      );
      expect(flows.status).toBe(200);
      expect(await flows.json()).toMatchObject({
        items: [],
        total: 0,
        termCounts: {},
      });
    } finally {
      await store.client.execute({
        sql: "DELETE FROM media_term_assignments WHERE reference_id=? AND media_id=?",
        args: [reference.id, mediaId],
      });
    }
  });
  it("rejects invalid pagination, kind, order and non-capture source IDs before loading", async () => {
    for (const query of [
      "offset=-1",
      "limit=NaN",
      "offset=1.5",
      "kind=flow",
      "sort=popular",
      "scope=visual",
      "mode=components",
      "term=not-namespaced",
      "term=web-page-types:../private",
      "term=web-page-types:missing-capture-filter",
      "referenceId=refero:apple",
      "referenceId=systems:workspace&referenceId=refero:apple",
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
