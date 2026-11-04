import { afterEach, expect, test } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createResearchStore, type ResearchStore } from "@/server/db";
import { taxonomyGroups, taxonomySnapshots } from "@/contracts/taxonomy";
import assignments from "@/data/system-categories.json";

const stores: ResearchStore[] = [];
const directories: string[] = [];
async function open(directory?: string) {
  const dir = directory ?? (await mkdtemp(join(tmpdir(), "taxonomy-db-")));
  if (!directory) directories.push(dir);
  const store = await createResearchStore(dir);
  stores.push(store);
  return { dir, store };
}
function close(store: ResearchStore) {
  store.close();
  stores.splice(stores.indexOf(store), 1);
}
afterEach(async () => {
  for (const store of stores.splice(0)) store.close();
  for (const dir of directories.splice(0))
    await rm(dir, { recursive: true, force: true });
});

test("SQLite retains every captured term, order, scope, subgroup and source", async () => {
  const { store } = await open();
  expect(await store.listTaxonomyGroups()).toEqual(taxonomyGroups);
  expect(await store.listTaxonomySnapshots()).toEqual(taxonomySnapshots);
  const classifications = await store.listReferenceCategories();
  const expected = assignments.flatMap((assignment) =>
    assignment.labels.map((label) => ({
      referenceId: assignment.referenceId,
      termId: taxonomyGroups
        .find((group) => group.id === assignment.groupId)!
        .terms.find((term) => term.label === label)!.id,
    })),
  );
  expect(classifications).toEqual(expect.arrayContaining(expected));
  expect(classifications).toHaveLength(expected.length);
});

test("v3 migration preserves research state and seeds vocabulary atomically", async () => {
  const { dir, store } = await open();
  const conversation = await store.createConversation(
    "Keep this discussion",
    "Keep this prompt",
  );
  const collection = await store.createCollection("Keep this board");
  await store.putItem(collection.id, "systems:linear", "Keep this note");
  await store.putCollectionMedia(collection.id, "systems:linear", "screen.png");
  await store.saveMedia("systems:linear", "screen.png");
  await store.saveSettings({ provider: "openai", model: "preserved" });
  for (const table of [
    "reference_categories",
    "taxonomy_terms",
    "taxonomy_groups",
    "taxonomy_snapshots",
  ]) {
    await store.client.execute(`DROP TABLE ${table}`);
  }
  await store.client.execute("PRAGMA user_version=3");
  close(store);
  const { store: migrated } = await open(dir);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(4);
  expect(await migrated.listTaxonomyGroups()).toEqual(taxonomyGroups);
  expect(
    (await migrated.getConversation(conversation.id))?.messages[0].parts[0],
  ).toEqual({ type: "text", text: "Keep this prompt" });
  expect((await migrated.getCollection(collection.id))?.items[0].note).toBe(
    "Keep this note",
  );
  expect(
    (await migrated.getCollection(collection.id))?.mediaItems,
  ).toHaveLength(1);
  expect(await migrated.listSavedMedia()).toHaveLength(1);
  expect(await migrated.getSettings()).toEqual({
    provider: "openai",
    model: "preserved",
  });
});

test("reopening preserves manual category changes and SQLite vocabulary instead of reseeding", async () => {
  const { dir, store } = await open();
  const assignment = assignments[0];
  expect(assignment).toBeDefined();
  const group = taxonomyGroups.find(
    (candidate) => candidate.id === assignment.groupId,
  )!;
  const replacement = group.terms.find(
    (term) => !assignment.labels.includes(term.label),
  )!;
  await store.assignReferenceCategories(
    assignment.referenceId,
    group.id,
    [replacement.label],
    "Manual review",
  );
  await store.client.execute({
    sql: "UPDATE taxonomy_groups SET label=? WHERE id=?",
    args: ["SQLite category title", group.id],
  });
  close(store);
  const { store: reopened } = await open(dir);
  const categoryIds = new Set(group.terms.map((term) => term.id));
  expect(
    (await reopened.listReferenceCategories()).filter(
      (row) =>
        row.referenceId === assignment.referenceId &&
        categoryIds.has(row.termId),
    ),
  ).toEqual([{ referenceId: assignment.referenceId, termId: replacement.id }]);
  expect(
    (await reopened.listTaxonomyGroups()).find(
      (candidate) => candidate.id === group.id,
    )?.label,
  ).toBe("SQLite category title");
  await reopened.assignReferenceCategories(
    assignment.referenceId,
    group.id,
    [],
  );
  close(reopened);
  const { store: cleared } = await open(dir);
  expect(
    (await cleared.listReferenceCategories()).filter(
      (row) =>
        row.referenceId === assignment.referenceId &&
        categoryIds.has(row.termId),
    ),
  ).toEqual([]);
});

test("category assignments reject unknown and non-category terms without losing prior choices", async () => {
  const { store } = await open();
  const group = taxonomyGroups.find(
    (candidate) => candidate.id === "web-categories",
  )!;
  await store.assignReferenceCategories("systems:test", group.id, [
    group.terms[0].label,
    group.terms[0].label,
  ]);
  const before = await store.listReferenceCategories();
  await expect(
    store.assignReferenceCategories("systems:test", group.id, [
      group.terms[1].label,
      "Unknown label",
    ]),
  ).rejects.toThrow("Unknown category");
  expect(await store.listReferenceCategories()).toEqual(before);
  await expect(
    store.assignReferenceCategories("systems:test", "styles-search-presets", [
      "Like Airbnb",
    ]),
  ).rejects.toThrow("Only category groups");
  await expect(
    store.assignReferenceCategories("systems:test", "web-page-types", [
      "About",
    ]),
  ).rejects.toThrow("Only category groups");
  await expect(
    store.client.execute({
      sql: "INSERT INTO reference_categories(reference_id,term_id,origin) VALUES('systems:test',?,'manual')",
      args: ["missing-term"],
    }),
  ).rejects.toThrow();
  const pageType = taxonomyGroups.find(
    (candidate) => candidate.id === "web-page-types",
  )!.terms[0];
  await expect(
    store.client.execute({
      sql: "INSERT INTO reference_categories(reference_id,term_id,origin) VALUES('systems:test',?,'manual')",
      args: [pageType.id],
    }),
  ).rejects.toThrow("category terms");
  const categoryId = group.terms[0].id;
  await store.client.execute({
    sql: "DELETE FROM taxonomy_terms WHERE id=?",
    args: [categoryId],
  });
  expect(
    (await store.listReferenceCategories()).some(
      (row) => row.termId === categoryId,
    ),
  ).toBe(false);
  expect((await store.client.execute("PRAGMA foreign_key_check")).rows).toEqual(
    [],
  );
});
