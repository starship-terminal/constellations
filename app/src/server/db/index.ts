import { createClient, type Client } from "@libsql/client";
import { drizzle } from "drizzle-orm/libsql";
import { eq, desc, sql, getTableColumns } from "drizzle-orm";
import { chmod, mkdir } from "node:fs/promises";
import { homedir } from "node:os";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { randomUUID } from "node:crypto";
import type { UIMessage } from "ai";
import type { Conversation, Collection } from "@/contracts/research";
import * as schema from "./schema";
import {
  taxonomyMigration,
  seedTaxonomy,
  taxonomyStore,
  mediaTaxonomyMigration,
  seedMediaTaxonomy,
  seedNewCuratedCategories,
  seedNewCuratedMediaTerms,
  seedLedgerMigration,
  backfillSeedLedger,
  topUpSeeds,
  pruneRemovedSeeds,
  referencesWithoutMedia,
  mediaTermsRevisionMigration,
} from "./taxonomy";
import { packageTopUps } from "./package-top-ups";

/** The schema version this build writes. A newer store is refused. */
export const RESEARCH_DB_VERSION = 45;

// Versioned migrations apply atomically, and never touch the canonical library.
const migrations = [
  `CREATE TABLE conversations (id TEXT PRIMARY KEY, title TEXT NOT NULL, messages TEXT NOT NULL DEFAULT '[]', pinned_ids TEXT NOT NULL DEFAULT '[]', excluded_ids TEXT NOT NULL DEFAULT '[]', archived INTEGER NOT NULL DEFAULT 0, created_at INTEGER NOT NULL, updated_at INTEGER NOT NULL)`,
  `CREATE TABLE collections (id TEXT PRIMARY KEY, name TEXT NOT NULL, notes TEXT NOT NULL DEFAULT '', created_at INTEGER NOT NULL, updated_at INTEGER NOT NULL)`,
  `CREATE TABLE collection_items (collection_id TEXT NOT NULL REFERENCES collections(id) ON DELETE CASCADE, reference_id TEXT NOT NULL, note TEXT NOT NULL DEFAULT '', added_at INTEGER NOT NULL, PRIMARY KEY(collection_id, reference_id))`,
  `CREATE TABLE settings (id TEXT PRIMARY KEY, value TEXT NOT NULL)`,
  `CREATE INDEX conversations_updated ON conversations(updated_at DESC)`,
];
function decode(row: typeof schema.conversations.$inferSelect): Conversation {
  return {
    ...row,
    messages: JSON.parse(row.messages),
    pinnedIds: JSON.parse(row.pinnedIds),
    excludedIds: JSON.parse(row.excludedIds),
  };
}
// The store holds saved provider keys and personal research. mkdir's mode only
// applies when it creates the directory and SQLite follows the umask, so set
// owner-only access on every open. SQLite gives later -wal/-shm files the
// database file's mode.
async function restrictPermissions(directory: string) {
  await chmod(directory, 0o700);
  for (const name of ["app.db", "app.db-wal", "app.db-shm"]) {
    try {
      await chmod(resolve(directory, name), 0o600);
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error;
    }
  }
}
// A row that is not a JSON object reads as no settings. Older builds wrote the
// literal string "provider" into a fresh row, and every read then threw; the
// next save replaces it with valid JSON.
function parseSettings(value: string): Record<string, unknown> {
  try {
    const parsed: unknown = JSON.parse(value);
    return parsed && typeof parsed === "object" && !Array.isArray(parsed)
      ? (parsed as Record<string, unknown>)
      : {};
  } catch {
    return {};
  }
}
export async function createResearchStore(directory: string) {
  await mkdir(directory, { recursive: true, mode: 0o700 });
  // Before anything can fail, so a store that will not open is still locked
  // down; again after opening, for files SQLite has just created.
  await restrictPermissions(directory);
  const client = createClient({
    url: pathToFileURL(resolve(directory, "app.db")).href,
  });
  await client.execute("PRAGMA foreign_keys = ON");
  await client.execute("PRAGMA busy_timeout = 5000");
  await client.execute("PRAGMA journal_mode = WAL");
  const tx = await client.transaction("write");
  try {
    const version = Number(
      (await tx.execute("PRAGMA user_version")).rows[0].user_version,
    );
    if (version > RESEARCH_DB_VERSION)
      throw new Error("Research database was created by a newer application.");
    if (version === 0) {
      for (const sql of migrations) await tx.execute(sql);
      await tx.execute("PRAGMA user_version = 1");
    }
    if (version < 2) {
      await tx.execute(
        "CREATE TABLE saved_media (reference_id TEXT NOT NULL, media_id TEXT NOT NULL, saved_at INTEGER NOT NULL, PRIMARY KEY(reference_id, media_id))",
      );
      await tx.execute("PRAGMA user_version = 2");
    }
    if (version < 3) {
      await tx.execute(
        "CREATE TABLE IF NOT EXISTS collection_media (collection_id TEXT NOT NULL REFERENCES collections(id) ON DELETE CASCADE, reference_id TEXT NOT NULL, media_id TEXT NOT NULL, added_at INTEGER NOT NULL, PRIMARY KEY(collection_id, reference_id, media_id))",
      );
      await tx.execute("PRAGMA user_version = 3");
    }
    if (version < 4) {
      for (const statement of taxonomyMigration) await tx.execute(statement);
      await seedTaxonomy(tx);
      await tx.execute("PRAGMA user_version = 4");
    }
    if (version < 5) {
      for (const statement of mediaTaxonomyMigration)
        await tx.execute(statement);
      await seedMediaTaxonomy(tx);
      await tx.execute("PRAGMA user_version = 5");
    }
    if (version < 6) {
      // The v4/v5 seeds run once, guarded, so a store already at v5 never saw
      // curated rows added to the seed JSON since. Top up only references and
      // media the user has not labelled; manual choices are never overwritten.
      // Media is topped up only for packages with no media rows at all, so
      // rows a user cleared on a labelled package stay cleared.
      await seedNewCuratedCategories(tx);
      await seedNewCuratedMediaTerms(tx, await referencesWithoutMedia(tx));
      await tx.execute("PRAGMA user_version = 6");
    }
    if (version < 7) {
      // The top-up is idempotent: a store already at v6 never re-seeds, so
      // curated rows added to the seed JSON since (new packages' category
      // and media assignments) would never arrive. Re-running it seeds only
      // references the user has not labelled; manual choices are never
      // overwritten.
      await seedNewCuratedCategories(tx);
      await seedNewCuratedMediaTerms(tx, await referencesWithoutMedia(tx));
      await tx.execute("PRAGMA user_version = 7");
    }
    if (version < 8) {
      // Same one-shot top-up: a store already at v7 never re-seeds, so
      // curated rows added to the seed JSON since (new packages' category
      // and media assignments) would never arrive. Idempotent; manual
      // choices are never overwritten.
      await seedNewCuratedCategories(tx);
      await seedNewCuratedMediaTerms(tx, await referencesWithoutMedia(tx));
      await tx.execute("PRAGMA user_version = 8");
    }
    // v9-v43: one top-up per package batch, listed in package-top-ups.ts.
    for (const step of packageTopUps) {
      if (version >= step.version) continue;
      await seedNewCuratedCategories(tx, new Set(step.references));
      await seedNewCuratedMediaTerms(tx, new Set(step.references));
      for (const media of step.media ?? [])
        await seedNewCuratedMediaTerms(
          tx,
          new Set([media.reference]),
          new Set(media.ids),
        );
      await tx.execute(`PRAGMA user_version = ${step.version}`);
    }
    if (version < 44) {
      // The per-package top-ups above end here. The seed ledger records what
      // each store has been offered, and topUpSeeds below offers the rest.
      for (const statement of seedLedgerMigration) await tx.execute(statement);
      await backfillSeedLedger(tx, version);
      await tx.execute("PRAGMA user_version = 44");
    }
    if (version < 45) {
      for (const statement of mediaTermsRevisionMigration)
        await tx.execute(statement);
      await tx.execute("PRAGMA user_version = 45");
    }
    // Every open: seed rows for packages and media the seed JSON gained since
    // this store last opened. Never add a per-package migration for this.
    await topUpSeeds(tx);
    // Every open, in the same transaction: remove the seed rows of packages
    // the library no longer has. User state is never touched.
    await pruneRemovedSeeds(tx);
    await tx.commit();
  } catch (error) {
    await tx.rollback();
    client.close();
    throw error;
  }
  await restrictPermissions(directory);
  const db = drizzle(client, { schema });
  return {
    client,
    db,
    close: () => client.close(),
    ...taxonomyStore(client),
    async listConversations() {
      return db
        .select({
          id: schema.conversations.id,
          title: schema.conversations.title,
          archived: schema.conversations.archived,
          createdAt: schema.conversations.createdAt,
          updatedAt: schema.conversations.updatedAt,
        })
        .from(schema.conversations)
        .orderBy(desc(schema.conversations.updatedAt));
    },
    async getConversation(id: string) {
      const [row] = await db
        .select()
        .from(schema.conversations)
        .where(eq(schema.conversations.id, id));
      return row ? decode(row) : null;
    },
    async createConversation(title = "New research", initialText?: string) {
      const now = Date.now();
      const row = { id: randomUUID(), title, createdAt: now, updatedAt: now };
      const messages: UIMessage[] = initialText
        ? [
            {
              id: randomUUID(),
              role: "user",
              parts: [{ type: "text", text: initialText }],
            },
          ]
        : [];
      // One insert commits the conversation and its first prompt together.
      await db
        .insert(schema.conversations)
        .values({ ...row, messages: JSON.stringify(messages) });
      return row;
    },
    async updateConversation(
      id: string,
      patch: {
        title?: string;
        archived?: boolean;
        pinnedIds?: string[];
        excludedIds?: string[];
      },
    ) {
      await db
        .update(schema.conversations)
        .set({
          ...patch,
          pinnedIds: patch.pinnedIds
            ? JSON.stringify(patch.pinnedIds)
            : undefined,
          excludedIds: patch.excludedIds
            ? JSON.stringify(patch.excludedIds)
            : undefined,
          updatedAt: Date.now(),
        })
        .where(eq(schema.conversations.id, id));
    },
    async saveMessages(id: string, messages: UIMessage[]) {
      await db
        .update(schema.conversations)
        .set({ messages: JSON.stringify(messages), updatedAt: Date.now() })
        .where(eq(schema.conversations.id, id));
    },
    async listCollections() {
      return db
        .select({
          ...getTableColumns(schema.collections),
          mediaCount: sql<number>`(SELECT COUNT(*) FROM collection_media WHERE collection_id = ${schema.collections.id})`,
          referenceCount: sql<number>`(SELECT COUNT(*) FROM collection_items WHERE collection_id = ${schema.collections.id})`,
        })
        .from(schema.collections)
        .orderBy(desc(schema.collections.updatedAt));
    },
    async createCollection(name: string): Promise<Collection> {
      const now = Date.now();
      const row = {
        id: randomUUID(),
        name,
        notes: "",
        createdAt: now,
        updatedAt: now,
      };
      await db.insert(schema.collections).values(row);
      return row;
    },
    async getCollection(id: string) {
      const [collection] = await db
        .select()
        .from(schema.collections)
        .where(eq(schema.collections.id, id));
      if (!collection) return null;
      const items = await db
        .select()
        .from(schema.collectionItems)
        .where(eq(schema.collectionItems.collectionId, id))
        .orderBy(desc(schema.collectionItems.addedAt));
      const mediaItems = await db
        .select()
        .from(schema.collectionMedia)
        .where(eq(schema.collectionMedia.collectionId, id))
        .orderBy(desc(schema.collectionMedia.addedAt));
      return { collection, items, mediaItems };
    },
    async updateCollection(
      id: string,
      patch: { name?: string; notes?: string },
    ) {
      await db
        .update(schema.collections)
        .set({ ...patch, updatedAt: Date.now() })
        .where(eq(schema.collections.id, id));
    },
    /** Delete a collection; its items and saved media cascade with it. */
    async deleteCollection(id: string) {
      await db.delete(schema.collections).where(eq(schema.collections.id, id));
    },
    async putItem(collectionId: string, referenceId: string, note?: string) {
      await client.batch(
        [
          {
            sql: "INSERT INTO collection_items (collection_id,reference_id,note,added_at) VALUES (?,?,?,?) ON CONFLICT(collection_id,reference_id) DO UPDATE SET note=CASE WHEN ? THEN excluded.note ELSE collection_items.note END",
            args: [
              collectionId,
              referenceId,
              note ?? "",
              Date.now(),
              note === undefined ? 0 : 1,
            ],
          },
          {
            sql: "UPDATE collections SET updated_at=? WHERE id=?",
            args: [Date.now(), collectionId],
          },
        ],
        "write",
      );
    },
    async removeItem(collectionId: string, referenceId: string) {
      await client.batch(
        [
          {
            sql: "DELETE FROM collection_items WHERE collection_id=? AND reference_id=?",
            args: [collectionId, referenceId],
          },
          {
            sql: "UPDATE collections SET updated_at=? WHERE id=?",
            args: [Date.now(), collectionId],
          },
        ],
        "write",
      );
    },
    async putCollectionMedia(
      collectionId: string,
      referenceId: string,
      mediaId: string,
    ) {
      await client.batch(
        [
          {
            sql: "INSERT INTO collection_media (collection_id,reference_id,media_id,added_at) VALUES (?,?,?,?) ON CONFLICT(collection_id,reference_id,media_id) DO NOTHING",
            args: [collectionId, referenceId, mediaId, Date.now()],
          },
          {
            sql: "UPDATE collections SET updated_at=? WHERE id=?",
            args: [Date.now(), collectionId],
          },
        ],
        "write",
      );
    },
    async removeCollectionMedia(
      collectionId: string,
      referenceId: string,
      mediaId: string,
    ) {
      await client.batch(
        [
          {
            sql: "DELETE FROM collection_media WHERE collection_id=? AND reference_id=? AND media_id=?",
            args: [collectionId, referenceId, mediaId],
          },
          {
            sql: "UPDATE collections SET updated_at=? WHERE id=?",
            args: [Date.now(), collectionId],
          },
        ],
        "write",
      );
    },
    async mediaCollectionIds(
      referenceId: string,
      mediaId: string,
    ): Promise<string[]> {
      const rows = await client.execute({
        sql: "SELECT collection_id FROM collection_media WHERE reference_id=? AND media_id=? ORDER BY collection_id",
        args: [referenceId, mediaId],
      });
      return rows.rows.map((row) => String(row.collection_id));
    },
    async listSavedMedia() {
      const result = await client.execute(
        "SELECT reference_id AS referenceId, media_id AS mediaId, saved_at AS savedAt FROM saved_media ORDER BY saved_at DESC",
      );
      return result.rows.map((row) => ({
        referenceId: String(row.referenceId),
        mediaId: String(row.mediaId),
        savedAt: Number(row.savedAt),
      }));
    },
    async saveMedia(referenceId: string, mediaId: string) {
      await client.execute({
        sql: "INSERT INTO saved_media(reference_id,media_id,saved_at) VALUES(?,?,?) ON CONFLICT(reference_id,media_id) DO NOTHING",
        args: [referenceId, mediaId, Date.now()],
      });
    },
    async removeSavedMedia(referenceId: string, mediaId: string) {
      await client.execute({
        sql: "DELETE FROM saved_media WHERE reference_id=? AND media_id=?",
        args: [referenceId, mediaId],
      });
    },
    async getSettings(): Promise<Record<string, unknown>> {
      const [row] = await db
        .select()
        .from(schema.settings)
        .where(eq(schema.settings.id, "provider"));
      return row ? parseSettings(row.value) : {};
    },
    // Read-modify-write inside one write transaction so concurrent updates
    // cannot merge a stale row back over another request's change.
    async updateSettings(
      mutate: (saved: Record<string, unknown>) => Record<string, unknown>,
    ) {
      const tx = await client.transaction("write");
      try {
        const result = await tx.execute(
          "SELECT value FROM settings WHERE id='provider'",
        );
        const saved = result.rows.length
          ? parseSettings(String(result.rows[0].value))
          : {};
        await tx.execute({
          sql: "INSERT INTO settings(id,value) VALUES('provider',?) ON CONFLICT(id) DO UPDATE SET value=excluded.value",
          args: [JSON.stringify(mutate(saved))],
        });
        await tx.commit();
      } catch (error) {
        await tx.rollback();
        throw error;
      }
    },
  };
}
export type ResearchStore = Awaited<ReturnType<typeof createResearchStore>>;
let cached: Promise<ResearchStore> | undefined;
// A failed open (locked file, unwritable directory) must not stick: forget the
// rejected promise so the next request tries again.
export function getStore() {
  if (!cached) {
    const opening = createResearchStore(
      process.env.DESIGN_RESEARCH_DATA_DIR ||
        resolve(homedir(), ".local/share/design-research"),
    );
    cached = opening;
    opening.catch(() => {
      if (cached === opening) cached = undefined;
    });
  }
  return cached;
}
