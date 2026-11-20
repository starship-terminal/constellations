import { afterEach, expect, test, vi } from "vitest";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import before from "@/data/seed-before-v9.json";
import { packageTopUps } from "@/server/db/package-top-ups";

// The seed files are mocked so a test can add what a later release would:
// entries pushed into these arrays are part of the seed until the test ends.
const seed = vi.hoisted(() => ({
  categories: [] as {
    referenceId: string;
    groupId: string;
    labels: string[];
    reason: string;
  }[],
  media: [] as {
    referenceId: string;
    mediaId: string;
    terms: { termId: string; rule: string; reason: string }[];
  }[],
  // The real seed, restored after every test, so a test can also remove
  // what a later release would.
  baseCategories: [] as unknown[],
  baseMedia: [] as unknown[],
}));
vi.mock("@/data/system-categories.json", async (importOriginal) => {
  const actual = (await importOriginal()) as {
    default: typeof seed.categories;
  };
  seed.categories.push(...actual.default);
  seed.baseCategories = [...actual.default];
  return { default: seed.categories };
});
vi.mock("@/data/media-taxonomy.json", async (importOriginal) => {
  const actual = (await importOriginal()) as {
    default: { assignments: typeof seed.media };
  };
  seed.media.push(...actual.default.assignments);
  seed.baseMedia = [...actual.default.assignments];
  return { default: { ...actual.default, assignments: seed.media } };
});

// Load the mocks now, so the arrays hold the real seed before any test reads it.
await import("@/data/system-categories.json");
await import("@/data/media-taxonomy.json");
const { createResearchStore } = await import("@/server/db");
type Store = Awaited<ReturnType<typeof createResearchStore>>;
const stores: Store[] = [];
const directories: string[] = [];
async function open(directory?: string) {
  const dir = directory ?? (await mkdtemp(join(tmpdir(), "seed-matrix-")));
  if (!directory) directories.push(dir);
  const store = await createResearchStore(dir);
  stores.push(store);
  return { dir, store };
}
function close(store: Store) {
  store.close();
  stores.splice(stores.indexOf(store), 1);
}
afterEach(async () => {
  seed.categories.splice(
    0,
    seed.categories.length,
    ...(seed.baseCategories as typeof seed.categories),
  );
  seed.media.splice(
    0,
    seed.media.length,
    ...(seed.baseMedia as typeof seed.media),
  );
  for (const store of stores.splice(0)) store.close();
  for (const dir of directories.splice(0))
    await rm(dir, { recursive: true, force: true });
});

// Two packages under test: Intercom, which a migration (v40) seeded, and
// Figma, which merged with no migration, so only rows show a store had it.
const MIGRATED = "systems:intercom";
const UNLISTED = "systems:figma";
const NEW_PACKAGE = "systems:zz-later";
const renumbered = packageTopUps
  .filter((step) => step.version >= 40 && step.version <= 42)
  .flatMap((step) => step.references);
const offeredByMigrations = new Set([
  ...before.references,
  ...packageTopUps.flatMap((step) => step.references),
]);

type Start = "fresh" | "v40" | "v43-later-build" | "v43-first-build";
type Cleared = "nothing" | "categories" | "media" | "everything";
type Added = "nothing" | "ios-group" | "screenshot" | "package";
const starts: Start[] = ["fresh", "v40", "v43-later-build", "v43-first-build"];
const clears: Cleared[] = ["nothing", "categories", "media", "everything"];
const adds: Added[] = ["nothing", "ios-group", "screenshot", "package"];

const newShot = (referenceId: string) =>
  `systems/${referenceId.slice("systems:".length)}/screenshots/zz-later.png`;

function addToSeed(added: Added) {
  const template = seed.media.find((row) => row.referenceId === UNLISTED)!;
  if (added === "ios-group")
    for (const referenceId of [MIGRATED, UNLISTED])
      seed.categories.push({
        referenceId,
        groupId: "ios-categories",
        labels: ["Productivity"],
        reason: "Test: a group a later seed adds.",
      });
  if (added === "screenshot")
    for (const referenceId of [MIGRATED, UNLISTED])
      seed.media.push({
        referenceId,
        mediaId: newShot(referenceId),
        terms: template.terms,
      });
  if (added === "package") {
    seed.categories.push({
      referenceId: NEW_PACKAGE,
      groupId: "web-categories",
      labels: ["Productivity"],
      reason: "Test: a package a later seed adds.",
    });
    seed.media.push({
      referenceId: NEW_PACKAGE,
      mediaId: newShot(NEW_PACKAGE),
      terms: template.terms,
    });
  }
}

const cells = starts.flatMap((start) =>
  clears.flatMap((cleared) => adds.map((added) => ({ start, cleared, added }))),
);
test.each(cells)(
  "start $start, user cleared $cleared, seed adds $added",
  async ({ start, cleared, added }) => {
    const baseMedia = new Map(
      [MIGRATED, UNLISTED].map((referenceId) => [
        referenceId,
        seed.media
          .filter((row) => row.referenceId === referenceId)
          .reduce((count, row) => count + row.terms.length, 0),
      ]),
    );
    const shotTerms = seed.media.find((row) => row.referenceId === UNLISTED)!
      .terms.length;
    const { dir, store } = await open();
    const users = [MIGRATED, UNLISTED];
    // A store that reached v43 with the first Huddlekit build never ran the
    // renumbered v40-v42 top-ups, and was migrated, not created, so it never
    // saw a package that merged without a migration either.
    const absent =
      start === "v43-first-build"
        ? [
            ...renumbered,
            ...new Set(
              seed.media
                .map((row) => row.referenceId)
                .filter((id) => !offeredByMigrations.has(id)),
            ),
          ]
        : [];
    for (const table of ["reference_categories", "media_term_assignments"])
      await store.client.execute({
        sql: `DELETE FROM ${table} WHERE reference_id IN (SELECT value FROM json_each(?))`,
        args: [JSON.stringify(absent)],
      });
    const offered = (id: string) => !absent.includes(id);
    for (const referenceId of users.filter(offered)) {
      if (cleared === "categories" || cleared === "everything")
        await store.assignReferenceCategories(
          referenceId,
          "web-categories",
          [],
        );
      if (cleared === "media" || cleared === "everything")
        await store.client.execute({
          sql: "DELETE FROM media_term_assignments WHERE reference_id=?",
          args: [referenceId],
        });
    }
    if (start !== "fresh") {
      await store.client.execute("DROP TABLE category_seed_ledger");
      await store.client.execute("DROP TABLE media_seed_ledger");
      await store.client.execute(
        `PRAGMA user_version=${start === "v40" ? 40 : 43}`,
      );
    }
    close(store);
    addToSeed(added);
    const { store: upgraded } = await open(dir);
    const categories = await upgraded.listReferenceCategoryDetails([
      ...users,
      NEW_PACKAGE,
    ]);
    const media = await upgraded.listMediaTermAssignments();
    for (const referenceId of users) {
      const had = offered(referenceId);
      // Offered before: the user's choice stands. Exception, with no way to
      // tell the cases apart: a package with no migration whose every label
      // was cleared on a store without a ledger looks never offered, so it
      // is offered again (the app has no route that clears labels).
      const restored =
        referenceId === UNLISTED &&
        cleared === "everything" &&
        start !== "fresh";
      // Never offered: a package with no migration is delivered; the
      // renumbered ones are not (the first-build trade-off).
      const delivered = had || referenceId === UNLISTED;
      const keepsCategories =
        delivered &&
        (!had ||
          restored ||
          (cleared !== "categories" && cleared !== "everything"));
      const keepsMedia =
        delivered &&
        (!had || restored || (cleared !== "media" && cleared !== "everything"));
      const groups = categories
        .filter((row) => row.referenceId === referenceId)
        .map((row) => row.termId.split(":")[0]);
      const label = `${referenceId} in ${start}`;
      expect(groups.includes("web-categories"), label).toBe(keepsCategories);
      expect(groups.includes("ios-categories"), label).toBe(
        added === "ios-group",
      );
      const rows = media.filter((row) => row.referenceId === referenceId);
      const shot = rows.filter((row) => row.mediaId === newShot(referenceId));
      expect(shot.length, label).toBe(added === "screenshot" ? shotTerms : 0);
      expect(rows.length - shot.length, label).toBe(
        keepsMedia ? baseMedia.get(referenceId) : 0,
      );
    }
    expect(categories.some((row) => row.referenceId === NEW_PACKAGE)).toBe(
      added === "package",
    );
    expect(media.some((row) => row.referenceId === NEW_PACKAGE)).toBe(
      added === "package",
    );
  },
  120_000,
);

// A package leaves the library (its folder is deleted, and the regenerated
// seed files drop it): the rows the seed gave it go, the user's own state
// stays. Both packages under test are removed at once.
const REMOVED = [MIGRATED, UNLISTED];
type Kept = "untouched" | "cleared" | "manual";
const kepts: Kept[] = ["untouched", "cleared", "manual"];

function removeFromSeed(referenceIds: readonly string[]) {
  const gone = new Set(referenceIds);
  const categories = seed.categories.filter(
    (row) => !gone.has(row.referenceId),
  );
  const media = seed.media.filter((row) => !gone.has(row.referenceId));
  seed.categories.splice(0, seed.categories.length, ...categories);
  seed.media.splice(0, seed.media.length, ...media);
}

/** Every seed-related row and ledger key a store holds for these references. */
async function seedState(store: Store, referenceIds: readonly string[]) {
  const read = async (sql: string) => {
    const result = await store.client.execute({
      sql,
      args: [JSON.stringify(referenceIds)],
    });
    return result.rows.map((row) =>
      Object.fromEntries(result.columns.map((column) => [column, row[column]])),
    );
  };
  const only = "reference_id IN (SELECT value FROM json_each(?))";
  return {
    categories: await read(
      `SELECT reference_id,term_id,origin FROM reference_categories WHERE ${only} ORDER BY 1,2`,
    ),
    media: await read(
      `SELECT reference_id,media_id,term_id,origin FROM media_term_assignments WHERE ${only} ORDER BY 1,2,3`,
    ),
    categoryLedger: await read(
      `SELECT reference_id,group_id FROM category_seed_ledger WHERE ${only} ORDER BY 1,2`,
    ),
    mediaLedger: await read(
      `SELECT reference_id,media_id FROM media_seed_ledger WHERE ${only} ORDER BY 1,2`,
    ),
  };
}

const removalCells = starts.flatMap((start) =>
  kepts.map((kept) => ({ start, kept })),
);
test.each(removalCells)(
  "start $start, user left the package $kept, seed removes it",
  async ({ start, kept }) => {
    const { dir, store } = await open();
    const absent =
      start === "v43-first-build"
        ? [
            ...renumbered,
            ...new Set(
              seed.media
                .map((row) => row.referenceId)
                .filter((id) => !offeredByMigrations.has(id)),
            ),
          ]
        : [];
    for (const table of ["reference_categories", "media_term_assignments"])
      await store.client.execute({
        sql: `DELETE FROM ${table} WHERE reference_id IN (SELECT value FROM json_each(?))`,
        args: [JSON.stringify(absent)],
      });
    const offered = (id: string) => !absent.includes(id);
    for (const referenceId of REMOVED.filter(offered)) {
      if (kept === "cleared") {
        await store.assignReferenceCategories(
          referenceId,
          "web-categories",
          [],
        );
        await store.client.execute({
          sql: "DELETE FROM media_term_assignments WHERE reference_id=?",
          args: [referenceId],
        });
      }
      if (kept === "manual")
        await store.assignReferenceCategories(
          referenceId,
          "web-categories",
          ["Productivity"],
          "My own call",
        );
    }
    // User state that points at the removed packages.
    const pair = seed.media.find((row) => row.referenceId === MIGRATED)!;
    const board = await store.createCollection("Removed later");
    await store.putItem(board.id, MIGRATED, "Kept note");
    await store.putCollectionMedia(board.id, pair.referenceId, pair.mediaId);
    await store.saveMedia(pair.referenceId, pair.mediaId);
    const chat = await store.createConversation("Study", "Compare these");
    await store.updateConversation(chat.id, { pinnedIds: REMOVED });
    if (start !== "fresh") {
      await store.client.execute("DROP TABLE category_seed_ledger");
      await store.client.execute("DROP TABLE media_seed_ledger");
      await store.client.execute(
        `PRAGMA user_version=${start === "v40" ? 40 : 43}`,
      );
    }
    close(store);
    removeFromSeed(REMOVED);
    const { store: upgraded } = await open(dir);
    const state = await seedState(upgraded, REMOVED);
    // No row the seed gave a removed package is left.
    expect(state.categories.filter((row) => row.origin === "curated")).toEqual(
      [],
    );
    expect(state.media).toEqual([]);
    // The user's own category choice stays, and so does its ledger key.
    const manual = REMOVED.filter(
      (id) => kept === "manual" && offered(id),
    ).sort();
    expect(state.categories.map((row) => row.reference_id)).toEqual(manual);
    expect(state.categories.every((row) => row.origin === "manual")).toBe(true);
    // A key that held only seed rows leaves the ledger, so the package is
    // seeded afresh if it comes back. A key that holds a user choice stays.
    // A cleared choice is known only to a store that had a ledger: a store
    // without one has no rows to show it, as for any cleared package.
    const cleared = REMOVED.filter(
      (id) => kept === "cleared" && offered(id) && start === "fresh",
    );
    expect(state.categoryLedger.map((row) => row.reference_id)).toEqual(
      [...manual, ...cleared].sort(),
    );
    expect(
      state.categoryLedger.every((row) => row.group_id === "web-categories"),
    ).toBe(true);
    expect(new Set(state.mediaLedger.map((row) => row.reference_id))).toEqual(
      new Set(cleared),
    );
    // User state survives and still points at the removed package.
    const saved = await upgraded.getCollection(board.id);
    expect(saved?.items.map((item) => [item.referenceId, item.note])).toEqual([
      [MIGRATED, "Kept note"],
    ]);
    expect(saved?.mediaItems.map((item) => item.mediaId)).toEqual([
      pair.mediaId,
    ]);
    expect((await upgraded.listSavedMedia()).map((row) => row.mediaId)).toEqual(
      [pair.mediaId],
    );
    expect((await upgraded.getConversation(chat.id))?.pinnedIds).toEqual(
      REMOVED,
    );
    // Other packages keep their seed rows.
    expect((await upgraded.listMediaTermAssignments()).length).toBeGreaterThan(
      0,
    );
    // Opening again changes nothing.
    close(upgraded);
    const { store: again } = await open(dir);
    expect(await seedState(again, REMOVED)).toEqual(state);
  },
  120_000,
);

test("a removed package that comes back is seeded again, and a choice the user made before stays", async () => {
  const { dir, store } = await open();
  const before = await seedState(store, REMOVED);
  await store.assignReferenceCategories(UNLISTED, "web-categories", []);
  close(store);
  removeFromSeed(REMOVED);
  const { store: removed } = await open(dir);
  expect((await seedState(removed, REMOVED)).media).toEqual([]);
  close(removed);
  seed.categories.splice(
    0,
    seed.categories.length,
    ...(seed.baseCategories as typeof seed.categories),
  );
  seed.media.splice(
    0,
    seed.media.length,
    ...(seed.baseMedia as typeof seed.media),
  );
  const { store: restored } = await open(dir);
  const after = await seedState(restored, REMOVED);
  expect(after.media).toEqual(before.media);
  expect(after.mediaLedger).toEqual(before.mediaLedger);
  expect(after.categoryLedger).toEqual(before.categoryLedger);
  // Intercom was untouched, so its seed rows return; Figma's cleared
  // category stays cleared.
  expect(after.categories).toEqual(
    before.categories.filter((row) => row.reference_id !== UNLISTED),
  );
}, 120_000);
