import { afterEach, expect, test, vi } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { pathToFileURL } from "node:url";
import categorySeed from "@/data/system-categories.json";
import mediaSeed from "@/data/media-taxonomy.json";
import { createClient } from "@libsql/client";
import {
  createResearchStore,
  RESEARCH_DB_VERSION,
  type ResearchStore,
} from "@/server/db";

// These suites open real SQLite databases, run migrations and seed the whole
// catalog. On a busy machine that takes longer than the unit suite's 15 s
// default, so only the database suites get a longer limit.
vi.setConfig({ testTimeout: 120_000 });
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
  await store.updateSettings(() => ({
    provider: "openai",
    model: "test-model",
  }));
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
  await store.updateSettings(() => ({
    provider: "openai",
    model: "kept-model",
  }));
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
  ).toBe(RESEARCH_DB_VERSION);
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

test("a version-5 store gains Dub and keeps a manual Linear category", async () => {
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
  ).toBe(RESEARCH_DB_VERSION);
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

// Each per-package migration (v7-v43) must still deliver its packages to a
// store opened below it, and leave alone a package the user cleared before.
// [rewind to, packages it gains, a cleared package that must stay cleared]
const topUps: [number, string[], string | null][] = [
  [7, ["systems:digg"], null],
  [8, ["systems:discord"], null],
  [9, ["systems:district"], null],
  [10, ["systems:dji"], null],
  [11, ["systems:framer"], null],
  [12, ["systems:fourthwall"], null],
  [12, ["systems:frame"], null],
  [13, ["systems:calm"], null],
  [14, ["systems:chargetrip", "systems:fresha"], "systems:digg"],
  [
    15,
    [
      "systems:classpass",
      "systems:frame",
      "systems:front",
      "systems:gladia",
      "systems:glassnode",
    ],
    "systems:digg",
  ],
  [16, ["systems:clay-earth"], "systems:digg"],
  [19, ["systems:clearful"], "systems:digg"],
  [22, ["systems:grok"], "systems:digg"],
  [23, ["systems:clipchamp"], "systems:digg"],
  [24, ["systems:hashnode"], "systems:discord"],
  [25, ["systems:gumroad"], "systems:digg"],
  [26, ["systems:cofounder"], "systems:digg"],
  [27, ["systems:joinhandshake"], "systems:digg"],
  [28, ["systems:cohere"], "systems:digg"],
  [29, ["systems:helloivy"], "systems:digg"],
  [31, ["systems:hbomax"], "systems:digg"],
  [32, ["systems:grow"], "systems:digg"],
  [33, ["systems:headspace"], "systems:discord"],
  [35, ["systems:httpie"], "systems:digg"],
  [36, ["systems:coinbase"], "systems:digg"],
  [37, ["systems:column"], "systems:digg"],
  [38, ["systems:hume"], "systems:digg"],
  [
    39,
    [
      "systems:forhers",
      "systems:huddlekit",
      "systems:ifttt",
      "systems:intercom",
      "systems:leonardo",
    ],
    "systems:digg",
  ],
];
test.each(
  topUps.map(([from, gained, cleared]) => ({
    from,
    gained,
    cleared,
    what: `${gained.join(", ")}${cleared ? `, and keeps ${cleared} cleared` : ""}`,
  })),
)("a version-$from store gains $what", async ({ from, gained, cleared }) => {
  const { dir, store } = await open();
  for (const referenceId of [...gained, ...(cleared ? [cleared] : [])])
    for (const table of ["reference_categories", "media_term_assignments"])
      await store.client.execute({
        sql: `DELETE FROM ${table} WHERE reference_id=?`,
        args: [referenceId],
      });
  await store.client.execute(`PRAGMA user_version=${from}`);
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(RESEARCH_DB_VERSION);
  const media = await migrated.listMediaTermAssignments();
  for (const referenceId of gained) {
    const seeded = categorySeed.find((row) => row.referenceId === referenceId)!;
    expect(
      (await migrated.listReferenceCategoryDetails([referenceId]))
        .map((row) => row.label)
        .sort(),
      referenceId,
    ).toEqual([...new Set(seeded.labels)].sort());
    expect(
      media.filter((row) => row.referenceId === referenceId).length,
      referenceId,
    ).toBe(
      mediaSeed.assignments
        .filter((row) => row.referenceId === referenceId)
        .reduce((count, row) => count + row.terms.length, 0),
    );
  }
  if (cleared) {
    expect(await migrated.listReferenceCategoryDetails([cleared])).toEqual([]);
    expect(media.filter((row) => row.referenceId === cleared)).toEqual([]);
  }
});
test("a version-25 store gains HTTPie and a Hashnode crop the v35 top-up adds, and keeps Discord cleared", async () => {
  const { dir, store } = await open();
  // A v25 store opened before the HTTPie rows existed (the v36 top-up).
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:httpie'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:httpie'",
  );
  // A user who cleared another package's labels: the scoped top-up must not
  // resurrect them (an empty assignment reads as "never labelled" to the
  // unscoped seed).
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:discord'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:discord'",
  );
  // The v35 top-up seeds five Hashnode crops by media ID: a store below v35
  // that lacks one gains it, and only that pair.
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE media_id='systems/hashnode/components/crops/app-sidebar-dark.png'",
  );
  await store.client.execute("PRAGMA user_version=25");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(RESEARCH_DB_VERSION);
  const categories = await migrated.listReferenceCategories();
  // The seed label (Development Tools) lands as one row.
  expect(
    categories.filter((row) => row.referenceId === "systems:httpie"),
  ).toHaveLength(1);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:httpie"])).map(
      (row) => row.label,
    ),
  ).toEqual(["Development Tools"]);
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:httpie").length,
  ).toBeGreaterThan(0);
  // The stranded Hashnode media pair lands too.
  expect(
    media.filter(
      (row) =>
        row.mediaId ===
        "systems/hashnode/components/crops/app-sidebar-dark.png",
    ).length,
  ).toBeGreaterThan(0);
  // The cleared discord rows stay cleared — the top-up seeds only its own
  // batch.
  expect(
    categories.filter((row) => row.referenceId === "systems:discord"),
  ).toHaveLength(0);
  expect(
    media.filter((row) => row.referenceId === "systems:discord"),
  ).toHaveLength(0);
});

test("a version-30 store gains Hitchd and two Handshake screenshots by media ID, and keeps a cleared Handshake label cleared", async () => {
  const { dir, store } = await open();
  // A v30 store opened before the Hitchd rows existed (the v31 top-up).
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:hitchd'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:hitchd'",
  );
  // The media seed also grew two joinhandshake screenshots after v28 shipped.
  // v31 tops up just those media IDs — simulate the v30 store by deleting
  // them, plus one joinhandshake media row standing in for a label the user
  // cleared: the scoped top-up must not resurrect the cleared one.
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:joinhandshake' AND media_id IN ('systems/joinhandshake/screenshots/home-light-consent.png','systems/joinhandshake/screenshots/mobile-home-light-drawer.png')",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:joinhandshake' AND media_id = (SELECT media_id FROM media_term_assignments WHERE reference_id='systems:joinhandshake' AND media_id NOT IN ('systems/joinhandshake/screenshots/home-light-consent.png','systems/joinhandshake/screenshots/mobile-home-light-drawer.png') LIMIT 1)",
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
  await store.client.execute("PRAGMA user_version=30");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(RESEARCH_DB_VERSION);
  const categories = await migrated.listReferenceCategories();
  // The seed labels (Fundraising + Marketplace) land as two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:hitchd"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:hitchd"])).map(
      (row) => row.label,
    ),
  ).toEqual(["Fundraising", "Marketplace"]);
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:hitchd").length,
  ).toBeGreaterThan(0);
  // The two new joinhandshake media arrived through the media-scoped top-up,
  // while the media cleared above stays cleared and every other row keeps
  // whatever the v28 pass already wrote.
  const jhMedia = new Set(
    media
      .filter((row) => row.referenceId === "systems:joinhandshake")
      .map((row) => row.mediaId),
  );
  expect(
    jhMedia.has("systems/joinhandshake/screenshots/home-light-consent.png"),
  ).toBe(true);
  expect(
    jhMedia.has(
      "systems/joinhandshake/screenshots/mobile-home-light-drawer.png",
    ),
  ).toBe(true);
  const remaining = await migrated.client.execute(
    "SELECT COUNT(DISTINCT media_id) AS n FROM media_term_assignments WHERE reference_id='systems:joinhandshake'",
  );
  // seed count for the reference minus the one cleared media
  const seedCount = new Set(
    (
      await import("@/data/media-taxonomy.json").then((m) => m.default)
    ).assignments
      .filter((a) => a.referenceId === "systems:joinhandshake")
      .map((a) => a.mediaId),
  ).size;
  expect(Number(remaining.rows[0].n)).toBe(seedCount - 1);

  // The cleared digg rows stay cleared — the top-up seeds only its own batch.
  expect(
    categories.filter((row) => row.referenceId === "systems:digg"),
  ).toHaveLength(0);
  expect(
    media.filter((row) => row.referenceId === "systems:digg"),
  ).toHaveLength(0);
});

test("a version-34 store gains Homerun and the five Hashnode crops by media ID, and keeps Discord cleared", async () => {
  const { dir, store } = await open();
  // A v34 store opened before the Homerun rows existed (the v35 top-up).
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:homerun'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:homerun'",
  );
  // A store below v35 also lacks the five Hashnode crops that top-up adds by
  // media ID: drop them so it runs.
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE media_id IN (" +
      "'systems/hashnode/components/crops/app-sidebar-dark.png'," +
      "'systems/hashnode/components/crops/app-sidebar-default.png'," +
      "'systems/hashnode/components/crops/feed-trending-default.png'," +
      "'systems/hashnode/components/crops/post-card-dark.png'," +
      "'systems/hashnode/components/crops/post-comments-link-default.png')",
  );
  // A user who cleared another package's labels: the scoped top-up must not
  // resurrect them (an empty assignment reads as "never labelled" to the
  // unscoped seed).
  await store.client.execute(
    "DELETE FROM reference_categories WHERE reference_id='systems:discord'",
  );
  await store.client.execute(
    "DELETE FROM media_term_assignments WHERE reference_id='systems:discord'",
  );
  await store.client.execute("PRAGMA user_version=34");
  store.close();
  stores.splice(stores.indexOf(store), 1);
  const migrated = await createResearchStore(dir);
  stores.push(migrated);
  expect(
    Number(
      (await migrated.client.execute("PRAGMA user_version")).rows[0]
        .user_version,
    ),
  ).toBe(RESEARCH_DB_VERSION);
  const categories = await migrated.listReferenceCategories();
  // The seed labels (Business + Productivity) land as two rows.
  expect(
    categories.filter((row) => row.referenceId === "systems:homerun"),
  ).toHaveLength(2);
  expect(
    (await migrated.listReferenceCategoryDetails(["systems:homerun"])).map(
      (row) => row.label,
    ),
  ).toEqual(["Business", "Productivity"]);
  const media = await migrated.listMediaTermAssignments();
  expect(
    media.filter((row) => row.referenceId === "systems:homerun").length,
  ).toBeGreaterThan(0);
  // The same migration backfills the five Hashnode crop assignments the
  // regenerated seed gained after v25 — media ids no store could have
  // cleared, so a scoped-by-reference pass is not needed for them.
  const hashnodeMedia = media
    .filter((row) => row.referenceId === "systems:hashnode")
    .map((row) => row.mediaId);
  for (const mediaId of [
    "systems/hashnode/components/crops/app-sidebar-dark.png",
    "systems/hashnode/components/crops/app-sidebar-default.png",
    "systems/hashnode/components/crops/feed-trending-default.png",
    "systems/hashnode/components/crops/post-card-dark.png",
    "systems/hashnode/components/crops/post-comments-link-default.png",
  ]) {
    expect(hashnodeMedia).toContain(mediaId);
  }
  // The cleared discord rows stay cleared — the top-up seeds only its own
  // batch.
  expect(
    categories.filter((row) => row.referenceId === "systems:discord"),
  ).toHaveLength(0);
  expect(
    media.filter((row) => row.referenceId === "systems:discord"),
  ).toHaveLength(0);
});

test("future database versions are rejected without downgrading their schema", async () => {
  const { dir, store } = await open();
  await store.client.execute(`PRAGMA user_version=${RESEARCH_DB_VERSION + 1}`);
  await expect(createResearchStore(dir)).rejects.toThrow("newer application");
  expect(
    Number(
      (await store.client.execute("PRAGMA user_version")).rows[0].user_version,
    ),
  ).toBe(RESEARCH_DB_VERSION + 1);
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
