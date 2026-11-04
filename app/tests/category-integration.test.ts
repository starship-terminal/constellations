import { describe, expect, it } from "vitest";
import { getStore } from "@/server/db";
import { withReferenceCategories } from "@/server/taxonomy/library";
import { matchesCategory } from "@/contracts/categories";
import { queryScreens } from "@/server/sources/screens";
import type { LibraryItem } from "@/contracts/library";
import assignments from "@/data/system-categories.json";
import catalog from "../../catalog.json";

const item = (slug: string, platform = "web"): LibraryItem => ({
  id: `systems:${slug}`,
  source: "systems",
  slug,
  name: slug,
  platform,
  description: "",
  themes: [],
  tags: [],
  category: "legacy-tag",
  image: null,
  icon: null,
  video: null,
  evidence: "measured",
  captured: null,
});

describe("database categories across apps and screens", () => {
  it("covers each existing measured system once with platform-correct assignments", () => {
    const rows = catalog.systems;
    expect(new Set(assignments.map((entry) => entry.referenceId))).toEqual(
      new Set(rows.map((entry: { slug: string }) => `systems:${entry.slug}`)),
    );
    expect(assignments).toHaveLength(rows.length);
    for (const row of rows) {
      const assignment = assignments.find(
        (entry) => entry.referenceId === `systems:${row.slug}`,
      )!;
      expect(assignment.groupId).toBe(
        row.platform === "mobile" ? "ios-categories" : "web-categories",
      );
    }
  });
  it("keeps each existing package reachable through its former category link", async () => {
    const references = await withReferenceCategories(
      catalog.systems.map((row) => item(row.slug, row.platform)),
    );
    for (const row of catalog.systems) {
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
    const store = await getStore();
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
