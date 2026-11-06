import { describe, expect, it } from "vitest";
import { taxonomyGroups } from "@/contracts/taxonomy";
import type { LibraryItem } from "@/contracts/library";
import {
  legacyCategoryLabels,
  canSwitchPlatform,
  pickerGroups,
  productSearchPlatform,
  selectProductSearch,
  platformSearch,
  inferredProductPlatform,
} from "@/features/catalog-search-state";
const products = [
  { id: "systems:web", platform: "web" },
  { id: "systems:ios", platform: "mobile" },
] as LibraryItem[];

describe("catalog search platform state", () => {
  it("suggests every product in Gallery and respects screen or explicit platform scope", () => {
    expect(productSearchPlatform(new URLSearchParams())).toBe("");
    expect(productSearchPlatform(new URLSearchParams("view=screens"))).toBe(
      "web",
    );
    expect(productSearchPlatform(new URLSearchParams("platform=mobile"))).toBe(
      "mobile",
    );
    expect(
      productSearchPlatform(
        new URLSearchParams("view=screens&platform=desktop"),
      ),
    ).toBe("desktop");
  });
  it("opens selected Gallery products in their own platform while preserving explicit filters", () => {
    for (const platform of ["mobile", "desktop", "web"]) {
      const next = selectProductSearch(new URLSearchParams("q=editor"), {
        id: `systems:${platform}`,
        platform,
      });
      expect(next.get("platform")).toBe(platform);
      expect(next.getAll("referenceId")).toEqual([`systems:${platform}`]);
      expect(next.get("q")).toBe("editor");
    }
    const scoped = new URLSearchParams(
      "platform=mobile&referenceId=systems:one",
    );
    const next = selectProductSearch(scoped, {
      id: "systems:two",
      platform: "mobile",
    });
    expect(next.get("platform")).toBe("mobile");
    expect(next.getAll("referenceId")).toEqual(["systems:one", "systems:two"]);
    expect(
      selectProductSearch(next, {
        id: "systems:two",
        platform: "mobile",
      }).getAll("referenceId"),
    ).toEqual(["systems:one", "systems:two"]);
  });
  it("maps exact term meanings across platform groups and drops unsupported terms", () => {
    const params = new URLSearchParams(
      "platform=web&view=screens&term=web-page-types:log-in&term=web-categories:education&term=web-fonts:inter&q=editor&mode=flows&screen=old&offset=60",
    );
    const next = platformSearch(params, "mobile", taxonomyGroups, products);
    expect(next.getAll("term")).toEqual([
      "ios-screen-types:log-in",
      "ios-categories:education",
    ]);
    expect(next.get("q")).toBe("editor");
    expect(next.get("view")).toBe("screens");
    expect(next.get("mode")).toBe("flows");
    expect(next.has("screen")).toBe(false);
    expect(next.has("offset")).toBe(false);
    expect(params.get("platform")).toBe("web");
  });
  it("preserves selected filters while taxonomy and product data are loading", () => {
    const params = new URLSearchParams(
      "term=web-page-types:log-in&term=web-categories:education&category=education&referenceId=systems:ios",
    );
    const next = platformSearch(params, "mobile", [], []);
    expect(next.getAll("term")).toEqual(params.getAll("term"));
    expect(next.get("category")).toBe("education");
    expect(next.getAll("referenceId")).toEqual(["systems:ios"]);
  });
  it("keeps unknown filters with partial data and drops only known incompatible products", () => {
    const params = new URLSearchParams(
      "term=web-page-types:log-in&term=web-categories:education&category=education&referenceId=systems:web&referenceId=systems:ios&referenceId=systems:not-loaded",
    );
    const sourceOnly = taxonomyGroups.filter(
      (group) => group.id === "web-page-types",
    );
    const next = platformSearch(params, "mobile", sourceOnly, [products[0]]);
    expect(next.getAll("term")).toEqual(params.getAll("term"));
    expect(next.get("category")).toBe("education");
    expect(next.getAll("referenceId")).toEqual([
      "systems:ios",
      "systems:not-loaded",
    ]);
    const partial = taxonomyGroups.filter((group) =>
      ["web-page-types", "ios-screen-types"].includes(group.id),
    );
    const mapped = platformSearch(params, "mobile", partial, products);
    expect(mapped.getAll("term")).toEqual([
      "ios-screen-types:log-in",
      "web-categories:education",
    ]);
    expect(mapped.get("category")).toBe("education");
    expect(mapped.getAll("referenceId")).toEqual([
      "systems:ios",
      "systems:not-loaded",
    ]);
  });
  it("maps Home Page and Home in both directions without changing same-platform terms", () => {
    const web = new URLSearchParams(
      "platform=web&term=web-page-types:home-page",
    );
    const ios = platformSearch(web, "mobile", taxonomyGroups, products);
    expect(ios.getAll("term")).toEqual(["ios-screen-types:home"]);
    expect(
      platformSearch(ios, "web", taxonomyGroups, products).getAll("term"),
    ).toEqual(["web-page-types:home-page"]);
    expect(
      platformSearch(web, "web", taxonomyGroups, products).getAll("term"),
    ).toEqual(["web-page-types:home-page"]);
    expect(
      platformSearch(ios, "mobile", taxonomyGroups, products).getAll("term"),
    ).toEqual(["ios-screen-types:home"]);
  });
  it("infers legacy product platform only when every selected product is known and compatible", () => {
    const desktop = {
      id: "systems:desktop",
      platform: "desktop",
    } as LibraryItem;
    const items = [...products, desktop];
    expect(
      inferredProductPlatform(
        new URLSearchParams("referenceId=systems:ios"),
        items,
      ),
    ).toBe("mobile");
    expect(
      inferredProductPlatform(
        new URLSearchParams("referenceId=systems:desktop"),
        items,
      ),
    ).toBe("desktop");
    expect(
      inferredProductPlatform(
        new URLSearchParams("referenceId=systems:ios&referenceId=systems:ios"),
        items,
      ),
    ).toBe("mobile");
    expect(
      inferredProductPlatform(
        new URLSearchParams("referenceId=systems:ios&referenceId=systems:web"),
        items,
      ),
    ).toBeUndefined();
    expect(
      inferredProductPlatform(
        new URLSearchParams(
          "referenceId=systems:ios&referenceId=systems:unknown",
        ),
        items,
      ),
    ).toBeUndefined();
    expect(
      inferredProductPlatform(
        new URLSearchParams("referenceId=systems:ios"),
        [],
      ),
    ).toBeUndefined();
    expect(
      inferredProductPlatform(new URLSearchParams(), items),
    ).toBeUndefined();
    expect(
      inferredProductPlatform(
        new URLSearchParams("platform=web&referenceId=systems:ios"),
        items,
      ),
    ).toBe("web");
  });
  it("retains compatible product OR selections and old filters", () => {
    const params = new URLSearchParams(
      "referenceId=systems:web&referenceId=systems:ios&theme=dark&group=boards&scope=media&kind=crop",
    );
    const next = platformSearch(params, "mobile", taxonomyGroups, products);
    expect(next.getAll("referenceId")).toEqual(["systems:ios"]);
    for (const key of ["theme", "group", "scope", "kind"])
      expect(next.get(key)).toBe(params.get(key));
    expect(
      platformSearch(params, "", taxonomyGroups, products).getAll(
        "referenceId",
      ),
    ).toEqual(params.getAll("referenceId"));
  });
  it("keeps broad legacy category alternatives as OR instead of AND terms", () => {
    const params = new URLSearchParams("category=media");
    const next = platformSearch(params, "mobile", taxonomyGroups, products);
    expect(next.get("category")).toBe("media");
    expect(next.getAll("term")).toEqual([]);
    expect(legacyCategoryLabels(taxonomyGroups, "media")).toContain(
      "Video Streaming",
    );
    expect(legacyCategoryLabels(taxonomyGroups, "media")).toContain(
      "Entertainment",
    );
    expect(
      platformSearch(
        new URLSearchParams("category=education"),
        "mobile",
        taxonomyGroups,
        products,
      ).get("category"),
    ).toBe("ios-categories:education");
  });
  it("uses only the selected platform's ordered recorded vocabulary", () => {
    expect(
      pickerGroups(taxonomyGroups, "mobile").map((group) => group.id),
    ).toEqual([
      "ios-screen-types",
      "ios-flows",
      "ios-ux-patterns",
      "ios-ui-elements",
      "ios-categories",
    ]);
    expect(pickerGroups(taxonomyGroups, "web")[0].id).toBe("web-page-types");
    expect(
      legacyCategoryLabels(
        taxonomyGroups,
        "ios-categories:dating-relationships",
      ),
    ).toBe("Dating & Relationships");
    expect(legacyCategoryLabels(taxonomyGroups, "unknown-category")).toBe(
      "unknown-category",
    );
  });
});

it("waits for selected filter lookups before enabling platform navigation", () => {
  const selected = new URLSearchParams(
    "term=web-page-types:log-in&referenceId=systems:web",
  );
  expect(canSwitchPlatform(selected, false, products)).toBe(false);
  expect(canSwitchPlatform(selected, true, [])).toBe(false);
  expect(canSwitchPlatform(selected, true, products)).toBe(true);
  expect(canSwitchPlatform(new URLSearchParams(), false, [])).toBe(true);
});

it("recovers platform navigation when a selected product was removed", () => {
  const stale = new URLSearchParams("platform=web&referenceId=systems:removed");
  expect(canSwitchPlatform(stale, true, products, true)).toBe(false);
  expect(canSwitchPlatform(stale, true, products, false)).toBe(true);
  expect(
    platformSearch(stale, "mobile", taxonomyGroups, products, true).getAll(
      "referenceId",
    ),
  ).toEqual([]);
  expect(
    platformSearch(stale, "mobile", taxonomyGroups, products, false).getAll(
      "referenceId",
    ),
  ).toEqual(["systems:removed"]);
});
