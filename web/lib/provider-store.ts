// The chat's model provider, held server-side. The browser submits a key
// once (Settings > Model provider); the server tests it, writes it here and
// never sends it back. server/provider_store.py reads and writes the same
// database with the same statements, so the gallery and the home server's
// Python /api/ share one saved provider.
//
// Where: $DESIGN_SYSTEMS_CONFIG_DIR/provider.db, default
// ~/.config/design-systems/provider.db. Outside the checkout, so no key can
// be committed; tests point the variable at a throwaway folder. The folder is
// created 0700 and the database file 0600 (SQLite gives its -wal and -shm
// files the same mode).
//
// Why SQLite for one row: every change is a single statement, so SQLite's
// own locking (released when a process dies, so a crash never leaves a lock
// behind) makes each one atomic across both servers' processes. A model-only
// save only applies while the row still holds the key and endpoint it read
// (compare and swap), a migration only inserts when no row exists, and an
// unchecked key only replaces a row that holds the same key.
import { promises as fs } from "node:fs";
import os from "node:os";
import path from "node:path";
import type { DatabaseSync } from "node:sqlite";

export const CONFIG_DIR_ENV = "DESIGN_SYSTEMS_CONFIG_DIR";
export const FILE_NAME = "provider.db";

/** The provider fields that are safe to show: everything but the key. */
export const PUBLIC_FIELDS = ["api", "base_url", "key_header", "models_url", "model", "name"] as const;
/** The fields that say where the key is sent. A saved key only ever goes to
    the endpoint it was saved with; changing any of these needs the key again. */
export const ENDPOINT_FIELDS = ["api", "base_url", "key_header", "models_url"] as const;

export type PublicProvider = Partial<Record<(typeof PUBLIC_FIELDS)[number], string>>;
export type SavedProvider = PublicProvider & { api: string; base_url: string; model: string; api_key: string };

export class StoreError extends Error {
  // The saved provider exists but cannot be used. Never carries its contents.
}

export function configDir(): string {
  const dir = process.env[CONFIG_DIR_ENV];
  return path.resolve(dir && dir.trim() ? dir : path.join(os.homedir(), ".config", "design-systems"));
}

export const providerFile = (): string => path.join(configDir(), FILE_NAME);

// The same schema server/provider_store.py creates.
const SCHEMA = `CREATE TABLE IF NOT EXISTS provider (
  id INTEGER PRIMARY KEY CHECK (id = 1),
  api TEXT NOT NULL,
  base_url TEXT NOT NULL,
  key_header TEXT NOT NULL DEFAULT '',
  models_url TEXT NOT NULL DEFAULT '',
  model TEXT NOT NULL,
  name TEXT NOT NULL DEFAULT '',
  api_key TEXT NOT NULL
)`;

const COLUMNS = "api, base_url, key_header, models_url, model, name, api_key";

/** Open the database, or null when none has been created (nothing saved).
    `create` makes the folder (0700) and the file (0600) first. node:sqlite is
    loaded here, not at import, so nothing else in the app depends on it. */
async function open(create: boolean): Promise<DatabaseSync | null> {
  const file = providerFile();
  if (create) {
    await fs.mkdir(configDir(), { recursive: true, mode: 0o700 });
    const fh = await fs.open(file, "a", 0o600);
    await fh.close();
    await fs.chmod(file, 0o600);
  } else {
    try {
      await fs.access(file);
    } catch {
      return null;
    }
  }
  try {
    const { DatabaseSync } = await import("node:sqlite");
    const db = new DatabaseSync(file);
    db.exec("PRAGMA busy_timeout = 5000");
    db.exec("PRAGMA journal_mode = WAL");
    db.exec(SCHEMA);
    return db;
  } catch {
    throw new StoreError("The saved provider file cannot be read.");
  }
}

function run<T>(db: DatabaseSync, fn: () => T): T {
  try {
    return fn();
  } catch {
    throw new StoreError("The saved provider file cannot be used.");
  } finally {
    db.close();
  }
}

const rowToProvider = (row: Record<string, unknown> | undefined): SavedProvider | null => {
  if (!row) return null;
  const out: Record<string, string> = {};
  for (const k of [...PUBLIC_FIELDS, "api_key"]) if (typeof row[k] === "string" && row[k]) out[k] = row[k] as string;
  if (!out.api_key || !out.api || !out.base_url || !out.model)
    throw new StoreError("The saved provider is missing its key, endpoint or model.");
  return out as SavedProvider;
};

const values = (cfg: SavedProvider): string[] => [
  cfg.api,
  cfg.base_url,
  cfg.key_header ?? "",
  cfg.models_url ?? "",
  cfg.model,
  cfg.name ?? "",
  cfg.api_key,
];

/** The saved provider, or null when none is saved. Throws StoreError when
    the database is there but unusable: that is a broken saved key, and the
    env key must not quietly stand in for it. */
export async function loadSaved(): Promise<SavedProvider | null> {
  const db = await open(false);
  if (!db) return null;
  const row = run(db, () => db.prepare(`SELECT ${COLUMNS} FROM provider WHERE id = 1`).get() as Record<string, unknown> | undefined);
  return rowToProvider(row);
}

/** How a save may treat a provider that is already saved:
    - "replace": always (a key the provider checked);
    - "create": only when none is saved (a migration from a browser);
    - "same-key": only when none is saved or it holds this same key (a key
      the provider could not check must not replace a different one).
    Returns whether the row was written. One statement, so it is atomic. */
export async function saveProvider(cfg: SavedProvider, mode: "replace" | "create" | "same-key"): Promise<boolean> {
  const db = (await open(true))!;
  const placeholders = "1, ?, ?, ?, ?, ?, ?, ?";
  const update =
    "api = excluded.api, base_url = excluded.base_url, key_header = excluded.key_header, models_url = excluded.models_url, model = excluded.model, name = excluded.name, api_key = excluded.api_key";
  const sql =
    mode === "create"
      ? `INSERT INTO provider (id, ${COLUMNS}) VALUES (${placeholders}) ON CONFLICT(id) DO NOTHING`
      : mode === "same-key"
        ? `INSERT INTO provider (id, ${COLUMNS}) VALUES (${placeholders}) ON CONFLICT(id) DO UPDATE SET ${update} WHERE provider.api_key = excluded.api_key`
        : `INSERT INTO provider (id, ${COLUMNS}) VALUES (${placeholders}) ON CONFLICT(id) DO UPDATE SET ${update}`;
  return run(db, () => Number(db.prepare(sql).run(...values(cfg)).changes) > 0);
}

/** Change the model and label of the saved provider, only while it still
    holds exactly the key and endpoint `seen` (what the caller read). Returns
    false when it changed or was removed meanwhile; nothing is written then. */
export async function updateModel(seen: SavedProvider, model: string, name: string): Promise<boolean> {
  const db = await open(false);
  if (!db) return false;
  return run(
    db,
    () =>
      Number(
        db
          .prepare(
            "UPDATE provider SET model = ?, name = ? WHERE id = 1 AND api_key = ? AND api = ? AND base_url = ? AND key_header = ? AND models_url = ?",
          )
          .run(model, name, seen.api_key, seen.api, seen.base_url, seen.key_header ?? "", seen.models_url ?? "").changes,
      ) > 0,
  );
}

/** Delete the saved provider. True when there was one. */
export async function removeSaved(): Promise<boolean> {
  const db = await open(false);
  if (!db) return false;
  return run(db, () => Number(db.prepare("DELETE FROM provider WHERE id = 1").run().changes) > 0);
}

/** The fields of a provider that may leave the server. */
export function publicView(cfg: PublicProvider | null | undefined): PublicProvider | null {
  if (!cfg) return null;
  const out: PublicProvider = {};
  for (const k of PUBLIC_FIELDS) if (typeof cfg[k] === "string" && cfg[k]) out[k] = cfg[k];
  return out;
}

/** `text` with every occurrence of each key replaced. Provider errors name a
    URL, and a URL or an upstream message can echo the key back. */
export function redact(text: string, ...keys: (string | undefined | null)[]): string {
  let out = text;
  for (const k of keys) if (k && k.length >= 4) out = out.split(k).join("[redacted]");
  return out;
}
