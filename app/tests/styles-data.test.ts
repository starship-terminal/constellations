import { describe, expect, it } from "vitest";
import type { LibraryItem } from "../src/contracts/library";
import { libraryItem } from "./helpers";
import {
  filterStyles,
  orderStyles,
  hasComponentMarkup,
  isUnresolvedCapture,
  styleCounts,
  type StyleFilters,
} from "../src/features/styles-data";

const empty: StyleFilters = {
  q: "",
  theme: "",
  type: "",
  style: "",
  industry: "",
  tags: [],
  video: false,
};
const style = (slug: string, extra: Partial<LibraryItem> = {}) =>
  libraryItem(slug, { source: "refero", themes: ["light"], ...extra });

describe("dedicated style discovery", () => {
  it("orders captures by date while keeping unknown dates last and ties stable", () => {
    const rows = [
      style("unknown"),
      style("older", { captured: "2026-01-01" }),
      style("broken", { captured: "invalid" }),
      style("new", { captured: "2026-10-01" }),
    ];
    expect(orderStyles(rows, "newest").map((row) => row.slug)).toEqual([
      "new",
      "older",
      "broken",
      "unknown",
    ]);
    expect(rows[0].slug).toBe("unknown");
    expect(orderStyles(rows, "name").map((row) => row.slug)).toEqual([
      "broken",
      "new",
      "older",
      "unknown",
    ]);
  });
  it("keeps measured packages out even when callers supply both stores", () => {
    const rows = [
      style("one"),
      style("two", { source: "systems", evidence: "measured" }),
    ];
    expect(filterStyles(rows, empty).map((row) => row.slug)).toEqual(["one"]);
  });
  it("combines independent type/style/industry/mixed-theme/tag/video filters", () => {
    const full = style("full", {
      productType: "saas",
      designStyle: "editorial",
      industry: "Finance",
      themes: ["mixed"],
      tags: ["swiss", "minimal"],
      video: "/clip.mp4",
    });
    const rows = [
      full,
      { ...full, slug: "wrong-industry", industry: "Design" },
      { ...full, slug: "no-video", video: null },
      { ...full, slug: "missing-tag", tags: ["swiss"] },
    ];
    expect(
      filterStyles(rows, {
        ...empty,
        type: "saas",
        style: "editorial",
        industry: "Finance",
        theme: "mixed",
        tags: ["swiss", "minimal"],
        video: true,
      }).map((row) => row.slug),
    ).toEqual(["full"]);
    expect(styleCounts(rows, "theme")).toContainEqual(["mixed", 4]);
  });
  it("searches source domains and primary facets, with facet matches ranked first", () => {
    const rows = [
      style("word-in-description", { description: "A swiss aesthetic" }),
      style("facet", {
        designStyle: "swiss",
        sourceUrl: "https://www.example.test/landing",
      }),
    ];
    expect(
      filterStyles(rows, { ...empty, q: "swiss website" }).map(
        (row) => row.slug,
      ),
    ).toEqual(["facet", "word-in-description"]);
    expect(
      filterStyles(rows, { ...empty, q: "example.test" }).map(
        (row) => row.slug,
      ),
    ).toEqual(["facet"]);
  });
});
describe("reconstructed component availability", () => {
  it("distinguishes actual markup from unresolved upstream references", () => {
    expect(hasComponentMarkup("$1e")).toBe(false);
    expect(isUnresolvedCapture(" $1e ")).toBe(true);
    expect(isUnresolvedCapture("Keep spacing at $4 per unit")).toBe(false);
    expect(hasComponentMarkup(null)).toBe(false);
    expect(
      hasComponentMarkup(
        "<style>:root{color:#000}</style><button>Continue</button>",
      ),
    ).toBe(true);
  });
});
