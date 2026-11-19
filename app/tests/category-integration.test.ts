import { execFileSync } from "node:child_process";
import { describe, expect, it } from "vitest";
import { withReferenceCategories } from "@/server/taxonomy/library";
import {
  addedCatalogSlugs,
  categorySeedGaps,
  derivedCategoryAssignment,
  matchesCategory,
  type CatalogCategoryRow,
  type CuratedCategory,
} from "@/contracts/categories";
import { queryScreens } from "@/server/sources/screens";
import assignments from "@/data/system-categories.json";
import catalog from "../../catalog.json";
import { libraryItem, tempStore } from "./helpers";

const item = (slug: string, platform = "web") =>
  libraryItem(slug, { platform, category: "legacy-tag" });

describe("database categories across apps and screens", () => {
  function catalogRows(): CatalogCategoryRow[] {
    return catalog.systems as CatalogCategoryRow[];
  }

  function pullRequestBaseRows(): CatalogCategoryRow[] | null {
    const base = process.env.GITHUB_BASE_REF;
    if (!base) return null;
    try {
      const raw = execFileSync("git", ["show", `origin/${base}:catalog.json`], {
        encoding: "utf8",
      });
      const parsed = JSON.parse(raw) as { systems?: CatalogCategoryRow[] };
      return parsed.systems ?? null;
    } catch {
      return null;
    }
  }

  it("covers each existing measured system once with platform-correct assignments", () => {
    const rows = catalogRows();
    const baseRows = pullRequestBaseRows();
    const added = baseRows ? addedCatalogSlugs(rows, baseRows) : null;
    const baseSlugs = added
      ? new Set(baseRows!.map((row) => row.slug))
      : undefined;
    expect(categorySeedGaps(rows, assignments, baseSlugs)).toEqual([]);
    if (!added) expect(assignments).toHaveLength(rows.length);
  });
  it("accepts an add-only slug when the seed is derived from the base catalog", () => {
    const rows = catalog.systems as {
      slug: string;
      platform?: string;
      category?: string;
    }[];
    const baseSlugs = new Set(rows.map((row) => row.slug));
    const added = {
      slug: "clay",
      platform: "web",
      category: "productivity",
    };
    const derived = derivedCategoryAssignment(added);
    // Without the base, a new slug still needs a pre-seeded row. With the
    // base, the check derives that row and accepts the addition.
    expect(categorySeedGaps([...rows, added], assignments)).toContain(
      "clay: missing from the category seed",
    );
    expect(categorySeedGaps([...rows, added], assignments, baseSlugs)).toEqual(
      [],
    );
    const handEdited: CuratedCategory = {
      ...derived,
      reason: "typed by hand",
    };
    expect(
      categorySeedGaps(
        [...rows, added],
        [...assignments, handEdited],
        baseSlugs,
      ),
    ).toEqual(["clay: added category seed row was hand-edited"]);
    // A package that was already on the base still needs its committed row.
    const dropped = assignments.filter(
      (entry) => entry.referenceId !== "systems:linear",
    );
    expect(categorySeedGaps(rows, dropped, baseSlugs)).toContain(
      "linear: missing from the category seed",
    );
  });
  it("keeps each existing package reachable through its former category link", async () => {
    const seeded = new Set(assignments.map((entry) => entry.referenceId));
    const rows = catalogRows().filter((row) =>
      seeded.has(`systems:${row.slug}`),
    );
    const references = await withReferenceCategories(
      rows.map((row) => item(row.slug, row.platform)),
    );
    for (const row of rows) {
      const reference = references.find(
        (candidate) => candidate.slug === row.slug,
      )!;
      expect(
        matchesCategory(reference, row.category),
        `${row.slug}: ${row.category}`,
      ).toBe(true);
    }
  });
  it("hydrates from SQLite and shares the same assignments with screen filters", async () => {
    // Edit a private store: the shared one feeds the other tests in this file.
    const { store } = await tempStore("category-integration-");
    const [reference] = await withReferenceCategories([item("linear")], store);
    expect(reference.categories?.map((term) => term.label)).toContain(
      "Project Management",
    );
    const query = "web-categories:project-management";
    expect(matchesCategory(reference, query)).toBe(true);
    const response = queryScreens(
      [
        {
          id: "capture",
          reference,
          media: {
            id: "one",
            name: "One",
            url: "/one.png",
            type: "image",
            tags: [],
            kind: "screenshot",
          },
        },
      ],
      { category: query },
    );
    expect(response.total).toBe(1);
    expect(response.facets.categories.map((facet) => facet.value)).toContain(
      query,
    );
    await store.assignReferenceCategories(
      reference.id,
      "web-categories",
      ["Business"],
      "test edit",
    );
    const [edited] = await withReferenceCategories([item("linear")], store);
    expect(matchesCategory(edited, query)).toBe(false);
    expect(matchesCategory(edited, "web-categories:business")).toBe(true);
    await store.assignReferenceCategories(
      reference.id,
      "web-categories",
      [],
      "clear categories",
    );
    const [cleared] = await withReferenceCategories([item("linear")], store);
    expect(cleared.category).toBe("");
    expect(cleared.categoryIds).toEqual([]);
    expect(cleared.categories).toEqual([]);
  });
  it("keeps empty assignments empty and supports old deep links", async () => {
    const [reference] = await withReferenceCategories([item("brilliant")]);
    expect(matchesCategory(reference, "learning")).toBe(true);
    for (const unknown of [
      "constructor",
      "toString",
      "__proto__",
      "unknown-category",
    ]) {
      expect(matchesCategory(reference, unknown)).toBe(false);
    }

    expect(matchesCategory(reference, "education")).toBe(true);
    expect(
      matchesCategory(
        { category: "", categoryIds: ["ios-categories:scheduling-tools"] },
        "events",
      ),
    ).toBe(true);
    expect(
      matchesCategory(
        { category: "", categoryIds: ["ios-categories:travel-booking"] },
        "super-app",
      ),
    ).toBe(true);

    expect(
      matchesCategory({ ...reference, categoryIds: [] }, "education"),
    ).toBe(false);
    expect(
      matchesCategory(
        { ...reference, categoryIds: ["ios-categories:education"] },
        "web-categories:education",
      ),
    ).toBe(true);
  });
});
