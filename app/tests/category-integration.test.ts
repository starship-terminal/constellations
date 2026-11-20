import { execFileSync } from "node:child_process";
import { describe, expect, it } from "vitest";
import { withReferenceCategories } from "@/server/taxonomy/library";
import {
  categorySeedGaps,
  matchesCategory,
  UNCATEGORISED,
  type CatalogCategoryRow,
  type CuratedCategory,
} from "@/contracts/categories";
import { queryScreens } from "@/server/sources/screens";
import { platformSearch } from "@/features/catalog-search-state";
import { taxonomyGroups } from "@/contracts/taxonomy";
import assignments from "@/data/system-categories.json";
import catalog from "../../catalog.json";
import { libraryItem, tempStore } from "./helpers";

const item = (slug: string, platform = "web") =>
  libraryItem(slug, { platform, category: "legacy-tag" });

describe("database categories across apps and screens", () => {
  function catalogRows(): CatalogCategoryRow[] {
    return catalog.systems as CatalogCategoryRow[];
  }

  function previousSeed(): CuratedCategory[] {
    const base = process.env.GITHUB_BASE_REF;
    if (!base) return assignments;
    try {
      const raw = execFileSync(
        "git",
        ["show", `origin/${base}:app/src/data/system-categories.json`],
        { encoding: "utf8" },
      );
      const parsed = JSON.parse(raw) as CuratedCategory[];
      return Array.isArray(parsed) ? parsed : assignments;
    } catch {
      return assignments;
    }
  }

  it("covers each existing measured system once with platform-correct assignments", () => {
    const rows = catalogRows();
    // On main, previous is the committed seed, so a deleted curated row fails.
    // On a pull request, previous is the base seed, so a new slug may stay
    // unseeded and a row the base already had may not disappear.
    expect(categorySeedGaps(rows, assignments, previousSeed())).toEqual([]);
  });
  it("accepts an add-only slug when the seed has no row for it yet", () => {
    const rows = catalogRows();
    const added = {
      slug: "clay-not-in-catalog",
      platform: "web",
      category: "productivity",
    };
    // The committed seed has no row. The check accepts that, on a pull
    // request and after the merge. A seed row whose package is gone, or a
    // row in the wrong platform group, still fails.
    expect(categorySeedGaps([...rows, added], assignments)).toEqual([]);
    // A slug the previous seed already curated cannot lose its row. A slug
    // the previous seed never had can stay unseeded.
    const dropped = assignments.filter(
      (entry) => entry.referenceId !== "systems:linear",
    );
    expect(categorySeedGaps(rows, dropped, assignments)).toContain(
      "linear: curated category row was deleted",
    );
    expect(categorySeedGaps([...rows, added], dropped, assignments)).toContain(
      "linear: curated category row was deleted",
    );
    const orphan = [
      ...assignments,
      {
        referenceId: "systems:removed-package",
        groupId: "web-categories",
        labels: ["Productivity"],
        reason: "left behind",
      },
    ];
    expect(categorySeedGaps(rows, orphan)).toContain(
      "systems:removed-package: category seed row has no catalog package",
    );
    const wrongGroup = assignments.map((entry) =>
      entry.referenceId === "systems:linear"
        ? { ...entry, groupId: "ios-categories" }
        : entry,
    );
    expect(categorySeedGaps(rows, wrongGroup)).toContain(
      "linear: category group ios-categories does not match platform web",
    );
  });
  it("keeps each existing package reachable through its former category link", async () => {
    // Every catalog package, curated or not: one the seed never curated
    // keeps its catalog category, so its old link still finds it.
    const rows = catalogRows();
    const references = await withReferenceCategories(
      rows.map((row) =>
        libraryItem(row.slug, {
          platform: row.platform,
          category: row.category ?? "",
        }),
      ),
    );
    for (const row of rows) {
      const reference = references.find(
        (candidate) => candidate.slug === row.slug,
      )!;
      expect(
        matchesCategory(reference, row.category ?? ""),
        `${row.slug}: ${row.category ?? ""}`,
      ).toBe(true);
    }
  });
  it("lists a package the seed never curated as uncategorised, not under no filter at all", async () => {
    const seeded = new Set(assignments.map((entry) => entry.referenceId));
    const uncurated = catalogRows().find(
      (row) => !seeded.has(`systems:${row.slug}`) && row.category,
    );
    expect(uncurated).toBeDefined();
    const { store } = await tempStore("category-uncurated-");
    const [reference, curated] = await withReferenceCategories(
      [
        libraryItem(uncurated!.slug, { category: uncurated!.category }),
        item("linear"),
      ],
      store,
    );
    expect(reference.category).toBe(uncurated!.category);
    expect(reference.categoryIds).toBeUndefined();
    expect(matchesCategory(reference, uncurated!.category!)).toBe(true);
    expect(matchesCategory(reference, UNCATEGORISED)).toBe(true);
    expect(matchesCategory(curated, UNCATEGORISED)).toBe(false);
    // A curated package the user cleared shows no category, and lists as
    // uncategorised too.
    await store.assignReferenceCategories(
      "systems:linear",
      "web-categories",
      [],
    );
    const [cleared] = await withReferenceCategories([item("linear")], store);
    expect(cleared.category).toBe("");
    expect(cleared.categoryIds).toEqual([]);
    expect(matchesCategory(cleared, UNCATEGORISED)).toBe(true);
  });
  it("keeps an uncurated package under its category when a platform switch rewrites the link", async () => {
    const seeded = new Set(assignments.map((entry) => entry.referenceId));
    const finance = catalogRows().find(
      (row) =>
        !seeded.has(`systems:${row.slug}`) &&
        row.category === "finance" &&
        row.platform === "web",
    );
    expect(finance).toBeDefined();
    const [reference] = await withReferenceCategories([
      libraryItem(finance!.slug, { category: "finance" }),
    ]);
    const rewritten = platformSearch(
      new URLSearchParams("category=finance"),
      "web",
      taxonomyGroups,
      [],
    ).get("category")!;
    expect(rewritten).toBe("web-categories:finance");
    expect(matchesCategory(reference, "finance")).toBe(true);
    expect(matchesCategory(reference, rewritten)).toBe(true);
    // A link naming several labels is never rewritten, so a package with
    // only that catalog category is not spread across those labels' terms.
    const productivity = libraryItem("uncurated-planner", {
      category: "productivity",
    });
    expect(matchesCategory(productivity, "productivity")).toBe(true);
    expect(
      matchesCategory(productivity, "web-categories:development-tools"),
    ).toBe(false);
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
