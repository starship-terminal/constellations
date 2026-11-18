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
} from "./taxonomy";

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
    if (version > 43)
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
      await seedNewCuratedCategories(tx);
      await seedNewCuratedMediaTerms(tx);
      await tx.execute("PRAGMA user_version = 6");
    }
    if (version < 7) {
      // The top-up is idempotent: a store already at v6 never re-seeds, so
      // curated rows added to the seed JSON since (new packages' category
      // and media assignments) would never arrive. Re-running it seeds only
      // references the user has not labelled; manual choices are never
      // overwritten.
      await seedNewCuratedCategories(tx);
      await seedNewCuratedMediaTerms(tx);
      await tx.execute("PRAGMA user_version = 7");
    }
    if (version < 8) {
      // Same one-shot top-up: a store already at v7 never re-seeds, so
      // curated rows added to the seed JSON since (new packages' category
      // and media assignments) would never arrive. Idempotent; manual
      // choices are never overwritten.
      await seedNewCuratedCategories(tx);
      await seedNewCuratedMediaTerms(tx);
      await tx.execute("PRAGMA user_version = 8");
    }
    if (version < 9) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v8 never re-seeds, so the Discord rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:discord"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:discord"]));
      await tx.execute("PRAGMA user_version = 9");
    }
    if (version < 10) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v9 never re-seeds, so the District rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:district"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:district"]));
      await tx.execute("PRAGMA user_version = 10");
    }
    if (version < 11) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v10 never re-seeds, so the DJI rows would never arrive.
      // Scoping keeps cleared labels on older packages cleared — an empty
      // assignment reads as "never labelled", so an unscoped pass would
      // restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:dji"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:dji"]));
      await tx.execute("PRAGMA user_version = 11");
    }
    if (version < 12) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v11 never re-seeds, so the Framer rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:framer"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:framer"]));
      await tx.execute("PRAGMA user_version = 12");
    }
    if (version < 13) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v12 never re-seeds, so the Frame.io and Fourthwall rows
      // would never arrive. Scoping keeps cleared labels on older packages
      // cleared — an empty assignment reads as "never labelled", so an
      // unscoped pass would restore rows the user deleted.
      await seedNewCuratedCategories(
        tx,
        new Set(["systems:frame", "systems:fourthwall"]),
      );
      await seedNewCuratedMediaTerms(
        tx,
        new Set(["systems:frame", "systems:fourthwall"]),
      );
      await tx.execute("PRAGMA user_version = 13");
    }
    if (version < 14) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v13 never re-seeds, so the Calm rows would never arrive.
      // Scoping keeps cleared labels on older packages cleared — an empty
      // assignment reads as "never labelled", so an unscoped pass would
      // restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:calm"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:calm"]));
      await tx.execute("PRAGMA user_version = 14");
    }
    if (version < 15) {
      // Same one-shot top-up, scoped to this batch's new references: a store
      // already at v14 never re-seeds, so the Chargetrip rows would never
      // arrive. systems:fresha is included because it merged without a
      // migration and its rows are stranded on v13/v14 stores. Scoping keeps
      // cleared labels on older packages cleared — an empty assignment
      // reads as "never labelled", so an unscoped pass would restore rows
      // the user deleted.
      await seedNewCuratedCategories(
        tx,
        new Set(["systems:fresha", "systems:chargetrip"]),
      );
      await seedNewCuratedMediaTerms(
        tx,
        new Set(["systems:fresha", "systems:chargetrip"]),
      );
      await tx.execute("PRAGMA user_version = 15");
    }
    if (version < 16) {
      // Same one-shot top-up, scoped to this batch's new references: a store
      // already at v15 never re-seeds, so the ClassPass rows would never
      // arrive. systems:frame is included because its v13 top-up only runs
      // below v13, leaving v13-v15 stores without the rows; systems:gladia,
      // systems:glassnode and systems:front merged without a migration and
      // are stranded entirely. Scoping keeps cleared labels on older
      // packages cleared — an empty assignment reads as "never labelled",
      // so an unscoped pass would restore rows the user deleted.
      await seedNewCuratedCategories(
        tx,
        new Set([
          "systems:classpass",
          "systems:frame",
          "systems:front",
          "systems:gladia",
          "systems:glassnode",
        ]),
      );
      await seedNewCuratedMediaTerms(
        tx,
        new Set([
          "systems:classpass",
          "systems:frame",
          "systems:front",
          "systems:gladia",
          "systems:glassnode",
        ]),
      );
      await tx.execute("PRAGMA user_version = 16");
    }
    if (version < 17) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v16 never re-seeds, so the Clay/Mesh rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:clay-earth"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:clay-earth"]));
      await tx.execute("PRAGMA user_version = 17");
    }
    if (version < 18) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v17 never re-seeds, so the GoFundMe rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:gofundme"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:gofundme"]));
      await tx.execute("PRAGMA user_version = 18");
    }
    if (version < 19) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v18 never re-seeds, so the Grammarly rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:grammarly"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:grammarly"]));
      await tx.execute("PRAGMA user_version = 19");
    }
    if (version < 20) {
      // v20: systems:clearful package rows.
      await seedNewCuratedCategories(tx, new Set(["systems:clearful"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:clearful"]));
      await tx.execute("PRAGMA user_version = 20");
    }
    if (version < 21) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v20 never re-seeds, so the Glorify rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:glorify"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:glorify"]));
      await tx.execute("PRAGMA user_version = 21");
    }
    if (version < 22) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v21 never re-seeds, so the GlossGenius rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:glossgenius"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:glossgenius"]));
      await tx.execute("PRAGMA user_version = 22");
    }
    if (version < 23) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v22 never re-seeds, so the Grok rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:grok"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:grok"]));
      await tx.execute("PRAGMA user_version = 23");
    }
    if (version < 24) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v23 never re-seeds, so the Clipchamp rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:clipchamp"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:clipchamp"]));
      await tx.execute("PRAGMA user_version = 24");
    }
    if (version < 25) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v24 never re-seeds, so the Hashnode rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:hashnode"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:hashnode"]));
      await tx.execute("PRAGMA user_version = 25");
    }
    if (version < 26) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v25 never re-seeds, so the Gumroad rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:gumroad"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:gumroad"]));
      await tx.execute("PRAGMA user_version = 26");
    }
    if (version < 27) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v26 never re-seeds, so the Cofounder rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:cofounder"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:cofounder"]));
      await tx.execute("PRAGMA user_version = 27");
    }
    if (version < 28) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v27 never re-seeds, so the Handshake rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:joinhandshake"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:joinhandshake"]));
      await tx.execute("PRAGMA user_version = 28");
    }
    if (version < 29) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v28 never re-seeds, so the Cohere rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:cohere"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:cohere"]));
      await tx.execute("PRAGMA user_version = 29");
    }
    if (version < 30) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v29 never re-seeds, so the Hello Ivy rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:helloivy"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:helloivy"]));
      await tx.execute("PRAGMA user_version = 30");
    }
    if (version < 31) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v30 never re-seeds, so the Hitchd rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:hitchd"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:hitchd"]));
      // The media seed also gained two joinhandshake screenshots since v28
      // shipped. A v28 store already labelled that package's other media, so
      // re-seeding the whole reference would resurrect any rows a user
      // cleared; the two media IDs are new and cannot have been cleared, so
      // top up just those.
      await seedNewCuratedMediaTerms(
        tx,
        new Set(["systems:joinhandshake"]),
        new Set([
          "systems/joinhandshake/screenshots/home-light-consent.png",
          "systems/joinhandshake/screenshots/mobile-home-light-drawer.png",
        ]),
      );
      await tx.execute("PRAGMA user_version = 31");
    }
    if (version < 32) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v31 never re-seeds, so the HBO Max rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:hbomax"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:hbomax"]));
      await tx.execute("PRAGMA user_version = 32");
    }
    if (version < 33) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v32 never re-seeds, so the Grow with Google rows would
      // never arrive. Scoping keeps cleared labels on older packages cleared
      // — an empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:grow"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:grow"]));
      await tx.execute("PRAGMA user_version = 33");
    }
    if (version < 34) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v33 never re-seeds, so the Headspace rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:headspace"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:headspace"]));
      await tx.execute("PRAGMA user_version = 34");
    }
    if (version < 35) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v34 never re-seeds, so the Homerun rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:homerun"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:homerun"]));
      // The regenerated seed also gained five Hashnode crop assignments no
      // store has labelled yet (they entered the seed file with this batch).
      // Backfill just those media ids: scoping the pass to the whole
      // systems:hashnode reference would restore labels a user cleared.
      await seedNewCuratedMediaTerms(
        tx,
        new Set(["systems:hashnode"]),
        new Set([
          "systems/hashnode/components/crops/app-sidebar-dark.png",
          "systems/hashnode/components/crops/app-sidebar-default.png",
          "systems/hashnode/components/crops/feed-trending-default.png",
          "systems/hashnode/components/crops/post-card-dark.png",
          "systems/hashnode/components/crops/post-comments-link-default.png",
        ]),
      );
      await tx.execute("PRAGMA user_version = 35");
    }
    if (version < 36) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v35 never re-seeds, so the HTTPie rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:httpie"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:httpie"]));
      await tx.execute("PRAGMA user_version = 36");
    }
    if (version < 37) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v36 never re-seeds, so the Coinbase rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:coinbase"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:coinbase"]));
      await tx.execute("PRAGMA user_version = 37");
    }
    if (version < 38) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v37 never re-seeds, so the Column rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:column"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:column"]));
      await tx.execute("PRAGMA user_version = 38");
    }
    if (version < 39) {
      // Same one-shot top-up, scoped to this batch's new reference: a store
      // already at v38 never re-seeds, so the Hume rows would never
      // arrive. Scoping keeps cleared labels on older packages cleared — an
      // empty assignment reads as "never labelled", so an unscoped pass
      // would restore rows the user deleted.
      await seedNewCuratedCategories(tx, new Set(["systems:hume"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:hume"]));
      await tx.execute("PRAGMA user_version = 39");
    }
    if (version < 40) {
      // Same one-shot top-up, scoped to this package: a store already at
      // v39 never re-seeds, so the IFTTT rows would never arrive.
      // Scoping keeps cleared labels on older packages cleared.
      await seedNewCuratedCategories(tx, new Set(["systems:ifttt"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:ifttt"]));
      await tx.execute("PRAGMA user_version = 40");
    }
    if (version < 43) {
      // Versions 41 and 42 stay reserved for Hers and Leonardo. This top-up
      // is scoped so a store already at v40 still gains Huddlekit.
      await seedNewCuratedCategories(tx, new Set(["systems:huddlekit"]));
      await seedNewCuratedMediaTerms(tx, new Set(["systems:huddlekit"]));
      await tx.execute("PRAGMA user_version = 43");
    }
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
    async saveSettings(value: Record<string, unknown>) {
      await db
        .insert(schema.settings)
        .values({ id: "provider", value: JSON.stringify(value) })
        .onConflictDoUpdate({
          target: schema.settings.id,
          set: { value: JSON.stringify(value) },
        });
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
