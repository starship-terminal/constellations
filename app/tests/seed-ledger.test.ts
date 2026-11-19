import { afterEach, expect, test } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import {
  createResearchStore,
  RESEARCH_DB_VERSION,
  type ResearchStore,
} from "@/server/db";
import mediaSeed from "@/data/media-taxonomy.json";
import frozen from "@/data/seed-ledger-v43.json";

const stores: ResearchStore[] = [];
const directories: string[] = [];
async function open(directory?: string) {
  const dir = directory ?? (await mkdtemp(join(tmpdir(), "seed-ledger-")));
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

const offeredByV43 = new Set(frozen.references);
// Seed rows for packages that landed after migration v43 shipped.
const laterRows = mediaSeed.assignments.filter(
  (row) => !offeredByV43.has(row.referenceId),
);
const laterReferences = [...new Set(laterRows.map((row) => row.referenceId))];
const laterTermCount = laterRows.reduce(
  (count, row) => count + row.terms.length,
  0,
);

async function version(store: ResearchStore) {
  return Number(
    (await store.client.execute("PRAGMA user_version")).rows[0].user_version,
  );
}
async function mediaRows(store: ResearchStore, referenceId: string) {
  return (await store.listMediaTermAssignments()).filter(
    (row) => row.referenceId === referenceId,
  );
}
async function categoryRows(store: ResearchStore, referenceId: string) {
  return (await store.listReferenceCategories()).filter(
    (row) => row.referenceId === referenceId,
  );
}

test("the frozen v43 list names packages the seed still holds, and later packages exist", () => {
  const seeded = new Set(mediaSeed.assignments.map((row) => row.referenceId));
  expect(frozen.references.length).toBe(212);
  expect(frozen.references.every((id) => seeded.has(id))).toBe(true);
  expect(laterReferences.length).toBeGreaterThan(0);
});

test("a v43 store with user rows gains the packages seeded since, and keeps its own state and cleared labels", async () => {
  const { dir, store } = await open();
  // User state of every kind the store holds.
  const conversation = await store.createConversation(
    "Onboarding study",
    "Compare first-run screens",
  );
  const collection = await store.createCollection("Keepers");
  await store.updateCollection(collection.id, { notes: "Dense layouts" });
  await store.putItem(collection.id, "systems:linear", "Sidebar density");
  const savedPair = mediaSeed.assignments[0];
  await store.putCollectionMedia(
    collection.id,
    savedPair.referenceId,
    savedPair.mediaId,
  );
  await store.saveMedia(savedPair.referenceId, savedPair.mediaId);
  await store.updateSettings(() => ({ provider: "openai", model: "m-1" }));
  await store.assignReferenceCategories(
    "systems:linear",
    "web-categories",
    ["Design & Media Editing"],
    "My own call",
  );
  // Labels the user cleared on packages v43 had already seeded.
  await store.assignReferenceCategories("systems:digg", "ios-categories", []);
  await store.assignReferenceCategories("systems:digg", "web-categories", []);
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:digg'",
  );
  const clearedPair = mediaSeed.assignments.find(
    (row) =>
      row.referenceId === "systems:linear" && row.mediaId !== savedPair.mediaId,
  )!;
  await store.client.execute({
    sql: "DELETE FROM media_term_assignments WHERE reference_id=? AND media_id=?",
    args: [clearedPair.referenceId, clearedPair.mediaId],
  });
  // Rewind to a v43 store: no ledger, and none of the later packages' rows.
  await store.client.execute("DROP TABLE category_seed_ledger");
  await store.client.execute("DROP TABLE media_seed_ledger");
  for (const table of ["media_term_assignments", "reference_categories"])
    await store.client.execute({
      sql: `DELETE FROM ${table} WHERE reference_id IN (SELECT value FROM json_each(?))`,
      args: [JSON.stringify(laterReferences)],
    });
  await store.client.execute("PRAGMA user_version=43");
  const before = (await store.listMediaTermAssignments()).length;
  close(store);

  const { store: migrated } = await open(dir);
  expect(await version(migrated)).toBe(RESEARCH_DB_VERSION);
  // Every later package's seed rows arrived.
  const arrived = await migrated.listMediaTermAssignments();
  expect(arrived.length).toBe(before + laterTermCount);
  const labelled = new Set(arrived.map((row) => row.referenceId));
  expect(laterReferences.filter((id) => !labelled.has(id))).toEqual([]);
  // Intercom's migration was renumbered below v43 after v43 first shipped,
  // so a store already at v43 skipped it: the ledger still delivers it.
  expect(laterReferences).toContain("systems:intercom");
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:intercom"])).map(
      (row) => row.label,
    ),
  ).toEqual(["Business", "Communication Tools"]);
  // Cleared labels stay cleared.
  expect(await mediaRows(migrated, "systems:digg")).toEqual([]);
  expect(await categoryRows(migrated, "systems:digg")).toEqual([]);
  expect(
    (await mediaRows(migrated, "systems:linear")).some(
      (row) => row.mediaId === clearedPair.mediaId,
    ),
  ).toBe(false);
  // User state survives.
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:linear"])).map(
      (row) => row.label,
    ),
  ).toEqual(["Design & Media Editing"]);
  expect(
    (await migrated.getConversation(conversation.id))?.messages[0].parts[0],
  ).toEqual({ type: "text", text: "Compare first-run screens" });
  const board = await migrated.getCollection(collection.id);
  expect(board?.collection.notes).toBe("Dense layouts");
  expect(board?.items.map((item) => item.note)).toEqual(["Sidebar density"]);
  expect(board?.mediaItems.map((item) => item.mediaId)).toEqual([
    savedPair.mediaId,
  ]);
  expect((await migrated.listSavedMedia()).map((row) => row.mediaId)).toEqual([
    savedPair.mediaId,
  ]);
  expect(await migrated.getSettings()).toEqual({
    provider: "openai",
    model: "m-1",
  });
  // Reopening seeds nothing more.
  const after = (await migrated.listMediaTermAssignments()).length;
  close(migrated);
  const { store: reopened } = await open(dir);
  expect((await reopened.listMediaTermAssignments()).length).toBe(after);
  // Four store opens over the full seed: more than the default 15 s on CI.
}, 120_000);

test("a store already at the latest version gains a package the seed added later, with no migration", async () => {
  const { dir, store } = await open();
  const [referenceId] = laterReferences;
  // The seed gaining a package looks like this to a store: no rows and no
  // ledger entry for it.
  for (const table of ["media_term_assignments", "media_seed_ledger"])
    await store.client.execute({
      sql: `DELETE FROM ${table} WHERE reference_id=?`,
      args: [referenceId],
    });
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:dub'",
  );
  await store.client.execute(
    "DELETE FROM category_seed_ledger WHERE reference_id='systems:dub'",
  );
  close(store);
  const { store: reopened } = await open(dir);
  expect(await version(reopened)).toBe(RESEARCH_DB_VERSION);
  expect((await mediaRows(reopened, referenceId)).length).toBe(
    laterRows
      .filter((row) => row.referenceId === referenceId)
      .reduce((count, row) => count + row.terms.length, 0),
  );
  expect(
    (await reopened.listReferenceCategoryDetails(["systems:dub"])).map(
      (row) => row.label,
    ),
  ).toEqual(["Productivity"]);
});

test("labels cleared on a store at the latest version stay cleared across reopens", async () => {
  const { dir, store } = await open();
  const [referenceId] = laterReferences;
  await store.client.execute({
    sql: "DELETE FROM media_term_assignments WHERE reference_id=?",
    args: [referenceId],
  });
  await store.assignReferenceCategories("systems:dub", "web-categories", []);
  close(store);
  const { dir: same, store: reopened } = await open(dir);
  expect(await mediaRows(reopened, referenceId)).toEqual([]);
  expect(await categoryRows(reopened, "systems:dub")).toEqual([]);
  close(reopened);
  const { store: again } = await open(same);
  expect(await mediaRows(again, referenceId)).toEqual([]);
  expect(await categoryRows(again, "systems:dub")).toEqual([]);
});

test("an empty manual category choice is never overridden by a seed row that arrives later", async () => {
  const { dir, store } = await open();
  // As if the Dub seed row had not reached this store yet.
  await store.client.execute(
    "DELETE FROM category_seed_ledger WHERE reference_id='systems:dub'",
  );
  await store.assignReferenceCategories("systems:dub", "web-categories", []);
  close(store);
  const { store: reopened } = await open(dir);
  expect(await categoryRows(reopened, "systems:dub")).toEqual([]);
});
