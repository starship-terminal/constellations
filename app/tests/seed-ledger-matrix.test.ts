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
  baseCategories: 0,
  baseMedia: 0,
}));
vi.mock("@/data/system-categories.json", async (importOriginal) => {
  const actual = (await importOriginal()) as {
    default: typeof seed.categories;
  };
  seed.categories.push(...actual.default);
  seed.baseCategories = seed.categories.length;
  return { default: seed.categories };
});
vi.mock("@/data/media-taxonomy.json", async (importOriginal) => {
  const actual = (await importOriginal()) as {
    default: { assignments: typeof seed.media };
  };
  seed.media.push(...actual.default.assignments);
  seed.baseMedia = seed.media.length;
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
  seed.categories.splice(seed.baseCategories);
  seed.media.splice(seed.baseMedia);
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
