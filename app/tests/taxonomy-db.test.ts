import { afterEach, expect, test, vi } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import {
  createResearchStore,
  RESEARCH_DB_VERSION,
  type ResearchStore,
} from "@/server/db";
import { taxonomyGroups, taxonomySnapshots } from "@/contracts/taxonomy";
import assignments from "@/data/system-categories.json";
import mediaSeed from "@/data/media-taxonomy.json";

// These suites open real SQLite databases, run migrations and seed the whole
// catalog. On a busy machine that takes longer than the unit suite's 15 s
// default, so only the database suites get a longer limit.
vi.setConfig({ testTimeout: 120_000 });

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
  await store.updateSettings(() => ({
    provider: "openai",
    model: "preserved",
  }));
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
  ).toBe(RESEARCH_DB_VERSION);
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

test("category detail reads stay narrow, deduplicate IDs, and include current SQLite labels", async () => {
  const { store } = await open();
  const group = taxonomyGroups.find(
    (candidate) => candidate.id === "web-categories",
  )!;
  const term = group.terms[0];
  await store.assignReferenceCategories("systems:narrow", group.id, [
    term.label,
  ]);
  await store.assignReferenceCategories("systems:other", group.id, [
    term.label,
  ]);
  await store.client.execute({
    sql: "UPDATE taxonomy_terms SET label=? WHERE id=?",
    args: ["Current database label", term.id],
  });
  const expected = [
    {
      referenceId: "systems:narrow",
      termId: term.id,
      label: "Current database label",
    },
  ];
  expect(
    await store.listReferenceCategoryDetails([
      "systems:narrow",
      "systems:narrow",
    ]),
  ).toEqual(expected);
  expect(await store.listReferenceCategoryDetails([])).toEqual([]);
  expect(await store.listReferenceCategoryDetails(["missing"])).toEqual([]);
  expect(await store.listReferenceCategoryDetails()).toEqual(
    expect.arrayContaining(expected),
  );
  await store.assignReferenceCategories("systems:narrow", group.id, []);
  expect(await store.listReferenceCategoryDetails(["systems:narrow"])).toEqual(
    [],
  );
});

test("category detail reads bound large ID filters without dropping matching references", async () => {
  const { store } = await open();
  const group = taxonomyGroups.find(
    (candidate) => candidate.id === "web-categories",
  )!;
  const term = group.terms[0];
  const ids = Array.from(
    { length: 1001 },
    (_, index) => `systems:batch-${index}`,
  );
  await store.assignReferenceCategories(ids[0], group.id, [term.label]);
  await store.assignReferenceCategories(ids[1000], group.id, [term.label]);
  expect(await store.listReferenceCategoryDetails(ids)).toEqual([
    { referenceId: ids[0], termId: term.id, label: term.label },
    { referenceId: ids[1000], termId: term.id, label: term.label },
  ]);
});

test("v5 seeds only existing media identities with recorded rules and leaves unverified flows empty", async () => {
  const { store } = await open();
  const terms = new Map(
    taxonomyGroups.flatMap((group) =>
      group.terms.map((term) => [term.id, group.id] as const),
    ),
  );
  const rows = await store.listMediaTermAssignments();
  expect(rows).toHaveLength(
    mediaSeed.assignments.reduce(
      (total, media) => total + media.terms.length,
      0,
    ),
  );
  for (const row of rows) {
    expect(terms.has(row.termId)).toBe(true);
    expect(terms.get(row.termId)).not.toMatch(
      /flows|categories|search-presets/,
    );
    expect(
      row.mediaId.startsWith(
        `systems/${row.referenceId.slice("systems:".length)}/`,
      ),
    ).toBe(true);
  }
  const sample = mediaSeed.assignments.find((media) =>
    media.terms.some((term) => term.rule === "ui-button"),
  )!;
  expect(rows).toContainEqual({
    referenceId: sample.referenceId,
    mediaId: sample.mediaId,
    termId: sample.terms.find((term) => term.rule === "ui-button")!.termId,
  });
  // Font terms come only from a package's recorded primary family. Checked
  // across the seed rather than one package's current fonts, which a
  // recapture may change; tools/test_media_taxonomy.py checks that a fallback
  // family in an invented stack never becomes a term.
  const labels = new Map(
    taxonomyGroups.flatMap((group) =>
      group.terms.map((term) => [term.id, term.label] as const),
    ),
  );
  const fontTerms = mediaSeed.assignments.flatMap((media) =>
    media.terms.filter((term) => term.termId.startsWith("web-fonts:")),
  );
  expect(fontTerms.length).toBeGreaterThan(0);
  for (const term of fontTerms) {
    expect(term.rule).toBe("font-primary");
    expect(term.reason).toContain(
      `Exact primary family ${labels.get(term.termId)} from `,
    );
  }
  expect(
    rows.filter((row) => row.termId.startsWith("web-fonts:")),
  ).toHaveLength(fontTerms.length);
  const recorded = await store.client.execute(
    "SELECT reason,origin FROM media_term_assignments LIMIT 1",
  );
  expect(recorded.rows[0].reason).toMatch(/Rule: .+\. Source: systems\//);
  expect(recorded.rows[0].origin).toBe("curated");
  // A context/menu state alone must never classify the whole page as a profile.
  expect(
    mediaSeed.assignments
      .filter((media) => /\/(?:[a-z]?\d+-)?account-menu\./.test(media.mediaId))
      .flatMap((media) => media.terms)
      .some((term) => term.termId.endsWith(":profile-account")),
  ).toBe(false);
});

test("v4 upgrade preserves manual categories and v5 reopening preserves manual media edits", async () => {
  const { dir, store } = await open();
  const category = taxonomyGroups.find(
    (group) => group.id === "web-categories",
  )!.terms[0];
  await store.assignReferenceCategories(
    "systems:linear",
    "web-categories",
    [category.label],
    "My v4 classification",
  );
  await store.client.execute("DROP TABLE media_term_assignments");
  await store.client.execute("PRAGMA user_version=4");
  close(store);
  const { store: migrated } = await open(dir);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(RESEARCH_DB_VERSION);
  expect(
    (await migrated.listReferenceCategories()).filter(
      (row) => row.referenceId === "systems:linear",
    ),
  ).toEqual([{ referenceId: "systems:linear", termId: category.id }]);
  const sample = mediaSeed.assignments[0];
  const manualTerm = taxonomyGroups
    .find((group) => group.id === "web-ui-elements")!
    .terms.find(
      (term) => !sample.terms.some((known) => known.termId === term.id),
    )!;
  await migrated.client.execute({
    sql: "DELETE FROM media_term_assignments WHERE reference_id=? AND media_id=?",
    args: [sample.referenceId, sample.mediaId],
  });
  await migrated.client.execute({
    sql: "INSERT INTO media_term_assignments(reference_id,media_id,term_id,reason,origin) VALUES(?,?,?,?,'manual')",
    args: [
      sample.referenceId,
      sample.mediaId,
      manualTerm.id,
      "My media classification",
    ],
  });
  close(migrated);
  const { store: reopened } = await open(dir);
  expect(
    (await reopened.listMediaTermAssignments()).filter(
      (row) =>
        row.referenceId === sample.referenceId &&
        row.mediaId === sample.mediaId,
    ),
  ).toEqual([
    {
      referenceId: sample.referenceId,
      mediaId: sample.mediaId,
      termId: manualTerm.id,
    },
  ]);
  await reopened.client.execute({
    sql: "DELETE FROM media_term_assignments WHERE reference_id=? AND media_id=?",
    args: [sample.referenceId, sample.mediaId],
  });
  close(reopened);
  const { store: cleared } = await open(dir);
  expect(
    (await cleared.listMediaTermAssignments()).some(
      (row) =>
        row.referenceId === sample.referenceId &&
        row.mediaId === sample.mediaId,
    ),
  ).toBe(false);
});

test("media term assignments enforce taxonomy membership and cascade removed terms", async () => {
  const { store } = await open();
  const row = mediaSeed.assignments[0];
  for (const termId of [
    "missing-term",
    taxonomyGroups.find((group) => group.id === "web-categories")!.terms[0].id,
    taxonomyGroups.find((group) => group.kind === "search-preset")!.terms[0].id,
  ]) {
    await expect(
      store.client.execute({
        sql: "INSERT INTO media_term_assignments(reference_id,media_id,term_id,origin) VALUES(?,?,?,'manual')",
        args: [row.referenceId, row.mediaId, termId],
      }),
    ).rejects.toThrow();
  }
  const termId = row.terms[0].termId;
  await store.client.execute({
    sql: "DELETE FROM taxonomy_terms WHERE id=?",
    args: [termId],
  });
  expect(
    (await store.listMediaTermAssignments()).some(
      (assignment) => assignment.termId === termId,
    ),
  ).toBe(false);
  expect((await store.client.execute("PRAGMA foreign_key_check")).rows).toEqual(
    [],
  );
});

test("v4 upgrade skips deleted vocabulary terms without blocking research or restoring user edits", async () => {
  const { dir, store } = await open();
  const conversation = await store.createConversation(
    "Research remains accessible",
    "Keep this prompt",
  );
  const category = taxonomyGroups.find(
    (group) => group.id === "web-categories",
  )!.terms[0];
  await store.assignReferenceCategories(
    "systems:linear",
    "web-categories",
    [category.label],
    "My category edit",
  );
  const removedTermId = mediaSeed.assignments[0].terms[0].termId;
  const renamedTermId = mediaSeed.assignments
    .flatMap((media) => media.terms)
    .find((term) => term.termId !== removedTermId)!.termId;
  await store.client.execute("DROP TABLE media_term_assignments");
  await store.client.execute({
    sql: "DELETE FROM taxonomy_terms WHERE id=?",
    args: [removedTermId],
  });
  await store.client.execute({
    sql: "UPDATE taxonomy_terms SET label=? WHERE id=?",
    args: ["My vocabulary label", renamedTermId],
  });
  await store.client.execute("PRAGMA user_version=4");
  close(store);
  const { store: migrated } = await open(dir);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(RESEARCH_DB_VERSION);
  expect(
    (await migrated.getConversation(conversation.id))?.messages[0].parts[0],
  ).toEqual({ type: "text", text: "Keep this prompt" });
  expect(
    (await migrated.listReferenceCategories()).filter(
      (row) => row.referenceId === "systems:linear",
    ),
  ).toEqual([{ referenceId: "systems:linear", termId: category.id }]);
  const vocabulary = (await migrated.listTaxonomyGroups()).flatMap(
    (group) => group.terms,
  );
  expect(vocabulary.some((term) => term.id === removedTermId)).toBe(false);
  expect(vocabulary.find((term) => term.id === renamedTermId)?.label).toBe(
    "My vocabulary label",
  );
  const rows = await migrated.listMediaTermAssignments();
  const expectedSeedCount = mediaSeed.assignments.reduce(
    (count, media) =>
      count +
      media.terms.filter((term) => term.termId !== removedTermId).length,
    0,
  );
  expect(rows).toHaveLength(expectedSeedCount);
  expect(rows.some((row) => row.termId === removedTermId)).toBe(false);
  expect(rows.some((row) => row.termId === renamedTermId)).toBe(true);
  expect(
    (await migrated.client.execute("PRAGMA foreign_key_check")).rows,
  ).toEqual([]);
  close(migrated);
  const { store: reopened } = await open(dir);
  expect(
    (await reopened.listMediaTermAssignments()).some(
      (row) => row.termId === removedTermId,
    ),
  ).toBe(false);
  expect((await reopened.getConversation(conversation.id))?.title).toBe(
    "Research remains accessible",
  );
});
