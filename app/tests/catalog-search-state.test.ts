import { describe, expect, it } from "vitest";
import { taxonomyGroups } from "@/contracts/taxonomy";
import type { LibraryItem } from "@/contracts/library";
import {
  legacyCategoryLabels,
  pickerGroups,
  productSearchPlatform,
  selectProductSearch,
  platformSearch,
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
