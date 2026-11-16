import { afterEach, expect, test } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { pathToFileURL } from "node:url";
import { createClient } from "@libsql/client";
import { createResearchStore, type ResearchStore } from "@/server/db";
const stores: ResearchStore[] = [],
  directories: string[] = [];
async function open() {
  const dir = await mkdtemp(join(tmpdir(), "research-db-"));
  directories.push(dir);
  const store = await createResearchStore(dir);
  stores.push(store);
  return { dir, store };
}
afterEach(async () => {
  for (const store of stores.splice(0)) store.close();
  for (const dir of directories.splice(0))
    await rm(dir, { recursive: true, force: true });
});
test("messages, selection, notes and settings survive reopening the database", async () => {
  const { dir, store } = await open();
  const conversation = await store.createConversation("A durable brief");
  await store.saveMessages(conversation.id, [
    {
      id: "user-1",
      role: "user",
      parts: [{ type: "text", text: "Compare layouts" }],
    },
    {
      id: "assistant-1",
      role: "assistant",
      parts: [
        {
          type: "tool-searchLibrary",
          toolCallId: "tool-1",
          state: "output-available",
          input: { query: "layouts" },
          output: { kind: "candidates", items: [] },
        },
      ],
    },
  ]);
  await store.updateConversation(conversation.id, {
    pinnedIds: ["systems:linear"],
    excludedIds: ["refero:example"],
    archived: true,
  });
  const collection = await store.createCollection("Layouts");
  await store.updateCollection(collection.id, { notes: "A useful pattern" });
  await store.putItem(collection.id, "systems:linear", "Keep the density");
  await store.putItem(collection.id, "systems:linear", "Changed my note");
  await store.saveSettings({ provider: "openai", model: "test-model" });
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const reopened = await createResearchStore(dir);
  stores.push(reopened);
  const saved = await reopened.getConversation(conversation.id);
  expect(saved).toMatchObject({
    title: "A durable brief",
    archived: true,
    pinnedIds: ["systems:linear"],
    excludedIds: ["refero:example"],
  });
  expect(saved?.messages[1].parts[0]).toMatchObject({
    type: "tool-searchLibrary",
    output: { kind: "candidates" },
  });
  const board = await reopened.getCollection(collection.id);
  expect(board?.collection.notes).toBe("A useful pattern");
  expect(board?.items).toHaveLength(1);
  expect(board?.items[0].note).toBe("Changed my note");
  expect(await reopened.getSettings()).toEqual({
    provider: "openai",
    model: "test-model",
  });
});
test("collection items enforce foreign keys and delete cascade", async () => {
  const { store } = await open();
  await expect(
    store.putItem("missing", "systems:linear", "note"),
  ).rejects.toThrow();
  const collection = await store.createCollection("Delete test");
  await store.putItem(collection.id, "systems:linear");
  await store.client.execute({
    sql: "DELETE FROM collections WHERE id=?",
    args: [collection.id],
  });
  expect(
    (await store.client.execute("SELECT * FROM collection_items")).rows,
  ).toHaveLength(0);
});

test("saving a bookmark again preserves its note unless a note is explicitly supplied", async () => {
  const { store } = await open();
  const collection = await store.createCollection("Bookmark notes");
  await store.putItem(collection.id, "systems:linear", "Keep this detail");
  await store.putItem(collection.id, "systems:linear");
  expect((await store.getCollection(collection.id))?.items[0].note).toBe(
    "Keep this detail",
  );
  await store.putItem(collection.id, "systems:linear", "");
  expect((await store.getCollection(collection.id))?.items[0].note).toBe("");
});

test("a conversation and its initial prompt survive reopening as one durable creation", async () => {
  const { dir, store } = await open();
  const row = await store.createConversation(
    "A saved first prompt",
    "Find thoughtful onboarding references",
  );
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const reopened = await createResearchStore(dir);
  stores.push(reopened);
  const saved = await reopened.getConversation(row.id);
  expect(saved?.messages).toHaveLength(1);
  expect(saved?.messages[0]).toMatchObject({
    role: "user",
    parts: [{ type: "text", text: "Find thoughtful onboarding references" }],
  });
  expect(saved?.messages[0].id).toMatch(/^[0-9a-f-]{36}$/);
});

test("version-one stores migrate without losing conversations and persist distinct screenshot bookmarks", async () => {
  const { dir, store } = await open();
  const conversation = await store.createConversation("Preserve me");
  await store.client.execute("DROP TABLE saved_media");
  await store.client.execute("PRAGMA user_version=1");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect((await migrated.getConversation(conversation.id))?.title).toBe(
    "Preserve me",
  );
  await migrated.saveMedia(
    "systems:linear",
    "systems/linear/screenshots/one.png",
  );
  await migrated.saveMedia(
    "systems:linear",
    "systems/linear/screenshots/two.png",
  );
  await migrated.saveMedia(
    "systems:linear",
    "systems/linear/screenshots/one.png",
  );
  expect(await migrated.listSavedMedia()).toHaveLength(2);
  await migrated.removeSavedMedia(
    "systems:linear",
    "systems/linear/screenshots/one.png",
  );
  expect((await migrated.listSavedMedia())[0].mediaId).toContain("two.png");
});

test("version-two stores preserve existing state while adding independent screenshot boards", async () => {
  const { dir, store } = await open();
  const conversation = await store.createConversation("Keep research");
  const first = await store.createCollection("First board");
  const second = await store.createCollection("Second board");
  await store.putItem(first.id, "systems:linear", "Existing package note");
  await store.saveMedia("systems:linear", "screenshots/one.png");
  await store.saveSettings({ provider: "openai", model: "kept-model" });
  await store.client.execute("DROP TABLE collection_media");
  await store.client.execute("PRAGMA user_version=2");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  expect((await migrated.getConversation(conversation.id))?.title).toBe(
    "Keep research",
  );
  expect((await migrated.getCollection(first.id))?.items[0].note).toBe(
    "Existing package note",
  );
  expect(await migrated.listSavedMedia()).toHaveLength(1);
  expect(await migrated.getSettings()).toEqual({
    provider: "openai",
    model: "kept-model",
  });
  await migrated.putCollectionMedia(
    first.id,
    "systems:linear",
    "screenshots/one.png",
  );
  await migrated.putCollectionMedia(
    first.id,
    "systems:linear",
    "screenshots/one.png",
  );
  await migrated.putCollectionMedia(
    first.id,
    "systems:linear",
    "screenshots/two.png",
  );
  await migrated.putCollectionMedia(
    second.id,
    "systems:linear",
    "screenshots/one.png",
  );
  await migrated.putCollectionMedia(first.id, "refero:linear", "shot");
  expect((await migrated.getCollection(first.id))?.mediaItems).toHaveLength(3);
  expect((await migrated.getCollection(second.id))?.mediaItems).toHaveLength(1);
  expect(
    new Set(
      await migrated.mediaCollectionIds(
        "systems:linear",
        "screenshots/one.png",
      ),
    ),
  ).toEqual(new Set([first.id, second.id]));
  expect(
    (await migrated.listCollections()).find((row) => row.id === first.id),
  ).toMatchObject({ mediaCount: 3, referenceCount: 1 });
  await migrated.removeCollectionMedia(
    first.id,
    "systems:linear",
    "screenshots/one.png",
  );
  expect(
    await migrated.mediaCollectionIds("systems:linear", "screenshots/one.png"),
  ).toEqual([second.id]);
  expect(await migrated.listSavedMedia()).toHaveLength(1);
  expect((await migrated.getCollection(first.id))?.items).toHaveLength(1);
  await expect(
    migrated.putCollectionMedia("missing", "systems:linear", "shot"),
  ).rejects.toThrow();
  await migrated.client.execute({
    sql: "DELETE FROM collections WHERE id=?",
    args: [second.id],
  });
  expect(
    await migrated.mediaCollectionIds("systems:linear", "screenshots/one.png"),
  ).toEqual([]);
  migrated.close();
  stores.splice(stores.indexOf(migrated), 1);
  const reopened = await createResearchStore(dir);
  stores.push(reopened);
  expect((await reopened.getCollection(first.id))?.mediaItems).toHaveLength(2);
  expect((await reopened.getCollection(first.id))?.items[0].note).toBe(
    "Existing package note",
  );
  expect(await reopened.listSavedMedia()).toHaveLength(1);
});

test("version-five stores gain curated rows added since, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A manual relabelling replaces the curated rows and must survive the
  // top-up; only references carrying no labels at all are seeded.
  await store.assignReferenceCategories(
    "systems:linear",
    "web-categories",
    ["Design & Media Editing"],
    "user's own call",
  );
  // A v5 store opened before the Dub rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:dub'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:dub'",
  );
  await store.client.execute("PRAGMA user_version=5");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  expect(
    categories.filter((row) => row.referenceId === "systems:dub"),
  ).toHaveLength(1);
  expect(
    categories.filter((row) => row.referenceId === "systems:linear"),
  ).toHaveLength(1);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:linear"]))[0].label,
  ).toBe("Design & Media Editing");
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:dub"]))[0].label,
  ).toBe("Productivity");
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:dub").length,
  ).toBeGreaterThan(0);
});

test("version-seven stores gain curated rows added since, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v7 store opened before the Digg rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:digg'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:digg'",
  );
  await store.client.execute("PRAGMA user_version=7");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // Two seed labels (Magazines & Newspapers + News) land as two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:digg"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:digg"]))[0].label,
  ).toBe("Magazines & Newspapers");
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:digg").length,
  ).toBeGreaterThan(0);
});

test("version-eight stores gain curated rows added since, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v8 store opened before the Discord rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:discord'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:discord'",
  );
  await store.client.execute("PRAGMA user_version=8");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // Two seed labels (Communication Tools + Social Networking) land as two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:discord"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:discord"]))[0].label,
  ).toBe("Communication Tools");
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:discord").length,
  ).toBeGreaterThan(0);
});

test("version-nine stores gain the District rows, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v9 store opened before the District rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:district'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:district'",
  );
  await store.client.execute("PRAGMA user_version=9");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // Two seed labels (Entertainment + Travel & Booking) land as two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:district"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:district"]))[0]
      .label,
  ).toBe("Entertainment");
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:district").length,
  ).toBeGreaterThan(0);
});

test("version-ten stores gain the DJI rows, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v10 store opened before the DJI rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:dji'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:dji'",
  );
  await store.client.execute("PRAGMA user_version=10");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // Two seed labels (Electronic & Devices + Marketplace) land as two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:dji"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:dji"]))[0].label,
  ).toBe("Electronic & Devices");
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:dji").length,
  ).toBeGreaterThan(0);
});

test("version-eleven stores gain the Framer rows, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v11 store opened before the Framer rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:framer'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:framer'",
  );
  await store.client.execute("PRAGMA user_version=11");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // Two seed labels (Design & Media Editing + Productivity) land as two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:framer"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:framer"]))[0].label,
  ).toBe("Design & Media Editing");
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:framer").length,
  ).toBeGreaterThan(0);
});

test("version-twelve stores gain the Frame.io rows, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v12 store opened before the Frame.io rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:frame'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:frame'",
  );
  await store.client.execute("PRAGMA user_version=12");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // Two seed labels (Collaboration Tools + Design & Media Editing) land as
  // two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:frame"),
  ).toHaveLength(2);
  expect(
    (
      await migrated.listReferenceCategoryDetails(["systems:frame"])
    ).map((row) => row.label),
  ).toEqual(
    expect.arrayContaining(["Collaboration Tools", "Design & Media Editing"]),
  );
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:frame").length,
  ).toBeGreaterThan(0);
});

test("version-twelve stores gain the Fourthwall rows, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v12 store opened before the Fourthwall rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:fourthwall'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:fourthwall'",
  );
  await store.client.execute("PRAGMA user_version=12");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // Two seed labels (Business + Marketplace) land as two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:fourthwall"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:fourthwall"]))[0]
      .label,
  ).toBe("Business");
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:fourthwall").length,
  ).toBeGreaterThan(0);
});

test("version-thirteen stores gain the Calm rows, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v13 store opened before the Calm rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:calm'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:calm'",
  );
  await store.client.execute("PRAGMA user_version=13");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // One seed label (Health & Wellness) lands as one row.
  expect(
    categories.filter((row) => row.referenceId === "systems:calm"),
  ).toHaveLength(1);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:calm"]))[0].label,
  ).toBe("Health & Wellness");
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:calm").length,
  ).toBeGreaterThan(0);
});

test("version-fourteen stores gain the Chargetrip and Fresha rows, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v14 store opened before the Chargetrip rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:chargetrip'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:chargetrip'",
  );
  // Fresha merged without a migration, so v13/v14 stores never got its rows
  // either; drop them to simulate a store that predates this top-up.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:fresha'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:fresha'",
  );
  // A user who cleared another package's labels: the scoped top-up must not
  // resurrect them (an empty assignment reads as "never labelled" to the
  // unscoped seed).
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:digg'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:digg'",
  );
  await store.client.execute("PRAGMA user_version=14");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // The Chargetrip seed labels (Development Tools + Travel & Booking) land as
  // two rows; Fresha's three labels land as three rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:chargetrip"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:chargetrip"])).map(
      (row) => row.label,
    ),
  ).toEqual(["Development Tools", "Travel & Booking"]);
  expect(
    categories.filter((row) => row.referenceId === "systems:fresha"),
  ).toHaveLength(3);
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:chargetrip").length,
  ).toBeGreaterThan(0);
  expect(
    media.filter((row) => row.referenceId === "systems:fresha").length,
  ).toBeGreaterThan(0);
  // The cleared digg rows stay cleared — the top-up seeds only its own batch.
  expect(
    categories.filter((row) => row.referenceId === "systems:digg"),
  ).toHaveLength(0);
  expect(
    media.filter((row) => row.referenceId === "systems:digg"),
  ).toHaveLength(0);
});

test("version-fifteen stores gain the ClassPass rows and the stranded Frame.io/Gladia rows, without touching their own labels", async () => {
  const { dir, store } = await open();
  // A v15 store opened before the ClassPass rows existed: drop them and rewind.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:classpass'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:classpass'",
  );
  // Frame.io's v13 top-up only runs below v13 and Gladia merged without a
  // migration, so a v13-v15 store never received their rows either.
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:frame'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:frame'",
  );
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:gladia'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:gladia'",
  );
  // A user who cleared another package's labels: the scoped top-up must not
  // resurrect them (an empty assignment reads as "never labelled" to the
  // unscoped seed).
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:digg'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:digg'",
  );
  await store.client.execute("PRAGMA user_version=15");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(16);
  const categories = await migrated.listReferenceCategories();
  // The seed labels (Health & Wellness + Marketplace) land as two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:classpass"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:classpass"])).map(
      (row) => row.label,
    ),
  ).toEqual(["Health & Wellness", "Marketplace"]);
  expect(
    categories.filter((row) => row.referenceId === "systems:frame"),
  ).toHaveLength(2);
  expect(
    categories.filter((row) => row.referenceId === "systems:gladia"),
  ).toHaveLength(2);
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:classpass").length,
  ).toBeGreaterThan(0);
  expect(
    media.filter((row) => row.referenceId === "systems:frame").length,
  ).toBeGreaterThan(0);
  expect(
    media.filter((row) => row.referenceId === "systems:gladia").length,
  ).toBeGreaterThan(0);
  // The cleared digg rows stay cleared — the top-up seeds only its own batch.
  expect(
    categories.filter((row) => row.referenceId === "systems:digg"),
  ).toHaveLength(0);
  expect(
    media.filter((row) => row.referenceId === "systems:digg"),
  ).toHaveLength(0);
});

test("future database versions are rejected without downgrading their schema", async () => {
  const { dir, store } = await open();
  await store.client.execute("PRAGMA user_version=17");
  await expect(createResearchStore(dir)).rejects.toThrow("newer application");
  expect(
    Number(
      (await store.client.execute("PRAGMA user_version")).rows[0].user_version,
    ),
  ).toBe(17);
});

test("updateSettings writes JSON on a fresh row and on a conflicting row", async () => {
  const { store } = await open();
  await store.updateSettings((saved) => ({ ...saved, provider: "anthropic" }));
  expect(await store.getSettings()).toEqual({ provider: "anthropic" });
  await store.updateSettings((saved) => ({ ...saved, model: "test-model" }));
  expect(await store.getSettings()).toEqual({
    provider: "anthropic",
    model: "test-model",
  });
});

test("a settings row that is not a JSON object reads as empty and is repaired by the next update", async () => {
  const { dir, store } = await open();
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const raw = createClient({
    url: pathToFileURL(join(dir, "app.db")).href,
  });
  await raw.execute(
    "INSERT INTO settings(id,value) VALUES('provider','provider')",
  );
  raw.close();
  const reopened = await createResearchStore(dir);
  stores.push(reopened);
  expect(await reopened.getSettings()).toEqual({});
  await reopened.updateSettings((saved) => ({ ...saved, provider: "openai" }));
  expect(await reopened.getSettings()).toEqual({ provider: "openai" });
});
