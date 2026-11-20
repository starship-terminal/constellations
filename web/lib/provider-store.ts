// The chat's model provider, held server-side. The browser submits a key
// once (Settings > Model provider); the server tests it, writes it here and
// never sends it back. server/provider_store.py reads and writes the same
// database with the same statements, so the gallery and the home server's
// Python /api/ share one saved provider.
//
// Where: $DESIGN_SYSTEMS_CONFIG_DIR/provider.db, default
// ~/.config/design-systems/provider.db. Outside the checkout, so no key can
// be committed; tests point the variable at a throwaway folder. The folder is
// created 0700 and the database file 0600. It uses the rollback journal
// (journal_mode DELETE), not the WAL the stack conventions default to: with
// secure_delete on, a replaced or removed key is overwritten in place and the
// journal file is deleted at commit, so no copy of an old key survives in a
// -wal file that a reader could keep from being checkpointed. Writes are rare
// and the table has one row, so WAL's concurrency buys nothing here.
//
// Why SQLite for one row: every change is a single statement, so SQLite's
// own locking (released when a process dies, so a crash never leaves a lock
// behind) makes each one atomic across both servers' processes. A model-only
// save only applies while the row still holds the key and endpoint it read
// (compare and swap), a migration only inserts when no row exists, and an
// unchecked key only replaces a row that holds the same key.
import { promises as fs, realpathSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import type { DatabaseSync } from "node:sqlite";
import { ROOT } from "./repo.ts";

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
  /** SQLite said the file is not a database or is corrupt. Only then may a
      remove or a checked save delete it; a busy lock, a full disk or a
      permission error must never cost a working provider. */
  damaged = false;
}

/** SQLite's primary result codes for a file that is not a usable database. */
const SQLITE_CORRUPT = 11;
const SQLITE_NOTADB = 26;

function storeError(message: string, cause: unknown): StoreError {
  const err = new StoreError(message);
  const code = (cause as { errcode?: unknown } | null)?.errcode;
  if (typeof code === "number") err.damaged = [SQLITE_CORRUPT, SQLITE_NOTADB].includes(code & 0xff);
  return err;
}

const CONFIG_DIR_HELP = `${CONFIG_DIR_ENV} must be an absolute path outside the checkout (a leading ~/ is expanded), for example ~/.config/design-systems.`;

const inside = (child: string, parent: string): boolean => {
  const rel = path.relative(parent, child);
  return rel === "" || (!rel.startsWith("..") && !path.isAbsolute(rel));
};

/** The folder that holds provider.db. server/provider_store.py applies the
    same rules, and server/provider-config-cases.json holds the cases both
    test suites run, so the gallery and the Python API always name the same
    file: a leading ~ or ~/ is the home folder (systemd's Environment= and
    a .env file do not expand it); a relative path, a ~user path or a path
    inside the checkout is refused with a StoreError that says how to set it,
    never resolved against whatever folder the server started in. */
export function configDir(): string {
  const raw = (process.env[CONFIG_DIR_ENV] ?? "").trim();
  const home = os.homedir();
  let dir: string;
  if (!raw) dir = path.join(home, ".config", "design-systems");
  else if (raw === "~") dir = home;
  else if (raw.startsWith("~/")) dir = path.join(home, raw.slice(2));
  else if (path.isAbsolute(raw)) dir = raw;
  else throw new StoreError(CONFIG_DIR_HELP);
  dir = path.resolve(dir);
  const roots = [path.resolve(ROOT)];
  try {
    roots.push(realpathSync(ROOT));
  } catch {}
  if (roots.some((r) => inside(dir, r))) throw new StoreError(CONFIG_DIR_HELP);
  return dir;
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
    `create` makes the folder (0700) and the file (0600) first. Any other
    failure (a permission change, a damaged file) is a StoreError, never
    "nothing saved", so the env key cannot quietly take over. node:sqlite is
    loaded here, not at import, so nothing else in the app depends on it.
    secure_delete overwrites a replaced or removed key's bytes in the file. */
async function open(create: boolean): Promise<DatabaseSync | null> {
  const file = providerFile();
  try {
    if (create) {
      await fs.mkdir(configDir(), { recursive: true, mode: 0o700 });
      // Create the file 0600 only when it is new. Opening and closing an
      // existing database outside SQLite would drop the POSIX locks another
      // connection in this process holds on it.
      try {
        const fh = await fs.open(file, "wx", 0o600);
        await fh.close();
      } catch (e) {
        if ((e as NodeJS.ErrnoException).code !== "EEXIST") throw e;
      }
      // By path, so no descriptor is opened: a restored or copied file with a
      // looser mode is tightened before a key is written into it.
      await fs.chmod(file, 0o600);
    } else {
      await fs.access(file);
    }
  } catch (e) {
    if (!create && (e as NodeJS.ErrnoException).code === "ENOENT") return null;
    throw new StoreError("The saved provider file cannot be read.");
  }
  let db: DatabaseSync | null = null;
  try {
    const { DatabaseSync } = await import("node:sqlite");
    db = new DatabaseSync(file);
    db.exec("PRAGMA busy_timeout = 5000");
    db.exec("PRAGMA secure_delete = ON");
    db.exec("PRAGMA journal_mode = DELETE");
    db.exec(SCHEMA);
    return db;
  } catch (e) {
    try {
      db?.close();
    } catch {}
    throw storeError("The saved provider file cannot be read.", e);
  }
}

function run<T>(db: DatabaseSync, fn: () => T): T {
  try {
    return fn();
  } catch (e) {
    if (e instanceof StoreError) throw e;
    throw storeError("The saved provider file cannot be used.", e);
  } finally {
    db.close();
  }
}

/** Delete the database and its side files: the way out of a damaged one. */
async function discardFiles(): Promise<void> {
  const file = providerFile();
  for (const f of [file, `${file}-journal`, `${file}-wal`, `${file}-shm`]) await fs.rm(f, { force: true });
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
  const placeholders = "1, ?, ?, ?, ?, ?, ?, ?";
  const update =
    "api = excluded.api, base_url = excluded.base_url, key_header = excluded.key_header, models_url = excluded.models_url, model = excluded.model, name = excluded.name, api_key = excluded.api_key";
  const sql =
    mode === "create"
      ? `INSERT INTO provider (id, ${COLUMNS}) VALUES (${placeholders}) ON CONFLICT(id) DO NOTHING`
      : mode === "same-key"
        ? `INSERT INTO provider (id, ${COLUMNS}) VALUES (${placeholders}) ON CONFLICT(id) DO UPDATE SET ${update} WHERE provider.api_key = excluded.api_key`
        : `INSERT INTO provider (id, ${COLUMNS}) VALUES (${placeholders}) ON CONFLICT(id) DO UPDATE SET ${update}`;
  const attempt = async () => {
    const db = (await open(true))!;
    return run(db, () => Number(db.prepare(sql).run(...values(cfg)).changes) > 0);
  };
  try {
    return await attempt();
  } catch (e) {
    // A checked key may replace a file SQLite calls damaged; the other modes
    // must not, since they only write when they can see what is there, and
    // no other failure (busy, disk full) is a reason to delete anything.
    if (!(e instanceof StoreError) || !e.damaged || mode !== "replace") throw e;
    await discardFiles();
    return attempt();
  }
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

/** Delete the saved provider. True when there was one. The row is deleted
    with secure_delete on, so its bytes are overwritten; a file SQLite calls
    damaged is deleted outright, so Remove recovers from it. */
export async function removeSaved(): Promise<boolean> {
  try {
    const db = await open(false);
    if (!db) return false;
    return run(db, () => Number(db.prepare("DELETE FROM provider WHERE id = 1").run().changes) > 0);
  } catch (e) {
    if (!(e instanceof StoreError) || !e.damaged) throw e;
    try {
      await discardFiles();
    } catch {
      throw new StoreError("The saved provider file cannot be removed.");
    }
    return true;
  }
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
