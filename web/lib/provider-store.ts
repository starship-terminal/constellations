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
//
// The one step that is not a statement is recovering from a damaged file:
// deleting it and writing its replacement. That runs under a second lock,
// BEGIN EXCLUSIVE on an empty provider.lock next to the database, which both
// servers take, and deletes only the file the damage was seen on (see
// discardDamaged).
import {
  chmodSync,
  closeSync,
  constants,
  existsSync,
  lstatSync,
  mkdirSync,
  openSync,
  realpathSync,
  rmSync,
  statSync,
  unlinkSync,
} from "node:fs";
import os from "node:os";
import path from "node:path";
import type { DatabaseSync } from "node:sqlite";
import { ROOT } from "./repo.ts";

export const CONFIG_DIR_ENV = "DESIGN_SYSTEMS_CONFIG_DIR";
export const FILE_NAME = "provider.db";
/** SQLite's side files next to the database. */
export const SIDE_FILES = ["-journal", "-wal", "-shm"] as const;
/** The recovery lock: an empty SQLite file next to the database that both
    servers hold with BEGIN EXCLUSIVE while they delete a damaged database
    and write its replacement. It never holds a table, let alone a key. */
export const LOCK_NAME = "provider.lock";

/** The provider fields that are safe to show: everything but the key. */
export const PUBLIC_FIELDS = ["api", "base_url", "key_header", "models_url", "model", "name"] as const;
/** The fields that say where the key is sent. A saved key only ever goes to
    the endpoint it was saved with; changing any of these needs the key again. */
export const ENDPOINT_FIELDS = ["api", "base_url", "key_header", "models_url"] as const;

export type PublicProvider = Partial<Record<(typeof PUBLIC_FIELDS)[number], string>>;
export type SavedProvider = PublicProvider & { api: string; base_url: string; model: string; api_key: string };

/** Which file an error was about: its device and inode, as lstat gives them. */
export type FileIdentity = { dev: bigint; ino: bigint };

export class StoreError extends Error {
  // The saved provider exists but cannot be used. Never carries its contents.
  /** SQLite said the file is not a database or is corrupt. Only then may a
      remove or a checked save delete it; a busy lock, a full disk or a
      permission error must never cost a working provider. */
  damaged = false;
  /** The database file the error came from, so a recovery deletes only that
      file and never one that replaced it meanwhile. */
  file?: FileIdentity;
}

/** SQLite's primary result codes. */
const SQLITE_BUSY = 5;
const SQLITE_LOCKED = 6;
/** Extended codes: a plain read-only file, and a file deleted (by a
    recovery) while this connection held it, which SQLite refuses to write. */
const SQLITE_READONLY = 8;
const SQLITE_READONLY_DBMOVED = 1032;
const SQLITE_CORRUPT = 11;
const SQLITE_NOTADB = 26;

const primaryCode = (cause: unknown): number | null => {
  const code = (cause as { errcode?: unknown } | null)?.errcode;
  return typeof code === "number" ? code & 0xff : null;
};

function storeError(message: string, cause: unknown, file?: FileIdentity): StoreError {
  const code = primaryCode(cause);
  const full = (cause as { errcode?: unknown } | null)?.errcode;
  const err = new StoreError(full === SQLITE_READONLY ? READ_ONLY : full === SQLITE_READONLY_DBMOVED ? MOVED : message);
  if (code !== null) err.damaged = [SQLITE_CORRUPT, SQLITE_NOTADB].includes(code);
  if (file) err.file = file;
  return err;
}

const CONFIG_DIR_HELP = `${CONFIG_DIR_ENV} must be an absolute path outside the checkout (a leading ~/ is expanded), for example ~/.config/design-systems.`;
const LINK_HELP = `${FILE_NAME} or a file next to it in ${CONFIG_DIR_ENV} is a symbolic link. The store never follows one: a link has no use here, and it could send the saved key into the checkout or anywhere else. Replace the link with the file itself, or remove it.`;
const OPENED_ELSEWHERE = `The saved provider file opened somewhere other than ${CONFIG_DIR_ENV}: the folder changed while it was being opened. Nothing was written.`;
const RECOVERY_BUSY = "The saved provider file is being repaired by another request. Try again in a moment.";
const READ_ONLY = "The saved provider file is read-only, so nothing can be saved or removed. It is still used as saved.";
const MOVED = "The saved provider file was replaced while this request used it. Nothing was written; try again.";

const inside = (child: string, parent: string): boolean => {
  const rel = path.relative(parent, child);
  // Outside only through a ".." segment: a child named "..cfg" is inside.
  return rel === "" || (rel !== ".." && !rel.startsWith(`..${path.sep}`) && !path.isAbsolute(rel));
};

/** `p` with its nearest existing ancestor replaced by that ancestor's real
    path (symlinks resolved), and the part that does not exist yet appended. */
function realOfNearest(p: string): string {
  let cur = path.resolve(p);
  const rest: string[] = [];
  for (;;) {
    try {
      return path.join(realpathSync(cur), ...rest.reverse());
    } catch {
      const up = path.dirname(cur);
      if (up === cur) return path.resolve(p);
      rest.push(path.basename(cur));
      cur = up;
    }
  }
}

/** Whether the filesystem holding `existing` ignores letter case, found by
    testing it rather than by platform: the same path with the case of its
    last lettered part swapped is the same file. macOS's default disk is
    case-insensitive, a Linux disk usually is not. */
export function caseInsensitiveAt(existing: string): boolean {
  const parts = existing.split(path.sep);
  for (let i = parts.length - 1; i >= 0; i--) {
    const swapped = [...parts[i]].map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase())).join("");
    if (swapped === parts[i]) continue;
    const variant = [...parts.slice(0, i), swapped, ...parts.slice(i + 1)].join(path.sep);
    try {
      const [a, b] = [statSync(existing), statSync(variant)];
      return a.dev === b.dev && a.ino === b.ino;
    } catch {
      return false;
    }
  }
  return false;
}

/** Whether `root` really is a checkout (it holds catalog.json or .git). A
    server started from / or /home has a fallback root that is not, and then
    the "inside the checkout" rule does not apply. */
export const isCheckout = (root: string): boolean =>
  existsSync(path.join(root, "catalog.json")) || existsSync(path.join(root, ".git"));

/** Whether `dir` is inside the checkout at `root`: compared as typed, and as
    real paths (a symlink into the checkout counts), case-folded where the
    filesystem ignores case. server/provider_store.py has the same rule. */
export function insideCheckout(dir: string, root: string): boolean {
  if (!isCheckout(root)) return false;
  if (inside(path.resolve(dir), path.resolve(root))) return true;
  const realRoot = realOfNearest(root);
  let d = realOfNearest(dir);
  let r = realRoot;
  if (caseInsensitiveAt(realRoot)) {
    d = d.toLowerCase();
    r = r.toLowerCase();
  }
  return inside(d, r);
}

/** The store's own file names in the folder: the database, its side files
    and the recovery lock. None of them may be a symbolic link. */
const STORE_NAMES = [FILE_NAME, ...SIDE_FILES.map((s) => FILE_NAME + s), LOCK_NAME];

/** The folder that holds provider.db. server/provider_store.py applies the
    same rules, and server/provider-config-cases.json holds the cases both
    test suites run, so the gallery and the Python API always name the same
    file: a leading ~ or ~/ is the home folder (systemd's Environment= and
    a .env file do not expand it); a relative path, a ~user path or a path
    inside the checkout (see insideCheckout) is refused with a StoreError
    that says how to set it, never resolved against whatever folder the
    server started in. The part of the folder that exists is returned with
    its symlinks resolved, so the database is opened by its real path, and a
    store file that is itself a symbolic link is refused. */
export function configDir(): string {
  const raw = (process.env[CONFIG_DIR_ENV] ?? "").trim();
  const home = os.homedir();
  let dir: string;
  if (!raw) dir = path.join(home, ".config", "design-systems");
  else if (raw === "~") dir = home;
  else if (raw.startsWith("~/")) dir = path.join(home, raw.slice(2));
  else if (path.isAbsolute(raw)) dir = raw;
  else throw new StoreError(CONFIG_DIR_HELP);
  dir = realOfNearest(path.resolve(dir));
  if (insideCheckout(dir, ROOT)) throw new StoreError(CONFIG_DIR_HELP);
  for (const name of STORE_NAMES) {
    let link = false;
    try {
      link = lstatSync(path.join(dir, name)).isSymbolicLink();
    } catch {
      // Missing (or unreadable: opening it reports that).
    }
    if (link) throw new StoreError(LINK_HELP);
  }
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
);
-- Set by the first save and kept by Remove: a one-time migration from a
-- browser only fills a store that has never held a provider, so a browser
-- that kept its old key after a lost reply cannot bring back a key the user
-- has since removed.
CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY);
CREATE TRIGGER IF NOT EXISTS provider_saved AFTER INSERT ON provider
BEGIN INSERT OR IGNORE INTO meta (k) VALUES ('saved'); END;`;

// A file made before meta existed, or by the first version of it, can hold a
// provider with an empty meta table: mark it as having held one. Written only
// when a read shows it is needed, so opening a complete file never writes and
// a read-only file (mode 0400, a read-only volume) still reads.
const NEEDS_BACKFILL =
  "SELECT EXISTS (SELECT 1 FROM provider) AND NOT EXISTS (SELECT 1 FROM meta WHERE k = 'saved') AS needed";
const BACKFILL = "INSERT OR IGNORE INTO meta (k) SELECT 'saved' FROM provider";

const COLUMNS = "api, base_url, key_header, models_url, model, name, api_key";

type Sqlite = typeof import("node:sqlite");
let sqliteModule: Sqlite | null = null;
/** node:sqlite, loaded on first use, not at import, so nothing else in the
    app depends on it. Everything below that touches the files is
    synchronous once it is loaded, so no other request in this process can
    run between a check and the step that relies on it. */
const sqlite = async (): Promise<Sqlite> => (sqliteModule ??= await import("node:sqlite"));

const errno = (e: unknown): string | undefined => (e as NodeJS.ErrnoException | null)?.code;

/** The identity of `file` without following a link; null when it is
    missing. A link is refused: configDir() checked, and this re-checks at
    the moment it matters. */
function identityOf(file: string): FileIdentity | null {
  let st;
  try {
    st = lstatSync(file, { bigint: true });
  } catch (e) {
    if (errno(e) === "ENOENT") return null;
    throw new StoreError("The saved provider file cannot be read.");
  }
  if (st.isSymbolicLink()) throw new StoreError(LINK_HELP);
  if (!st.isFile()) throw new StoreError("The saved provider file cannot be read.");
  return { dev: st.dev, ino: st.ino };
}

const sameFile = (a: FileIdentity | null | undefined, b: FileIdentity | null | undefined): boolean =>
  !!a && !!b && a.dev === b.dev && a.ino === b.ino;

/** Create `file` 0600 when it is new, never through a link (O_EXCL and
    O_NOFOLLOW), and take group and other access off an existing one.
    Opening and closing an existing database outside SQLite would drop the
    POSIX locks another connection in this process holds on it, so an
    existing file is only chmod-ed by path. */
function createPrivate(file: string): void {
  try {
    closeSync(openSync(file, constants.O_CREAT | constants.O_EXCL | constants.O_WRONLY | (constants.O_NOFOLLOW ?? 0), 0o600));
  } catch (e) {
    if (errno(e) !== "EEXIST") throw e;
  }
  identityOf(file);
  // By path, so no descriptor is opened: a restored or copied file with a
  // looser mode is tightened before a key is written into it. The owner's
  // own bits are kept, so a file the operator made read-only stays so.
  const mode = lstatSync(file).mode & 0o777;
  if (mode & 0o077) chmodSync(file, mode & 0o600);
}

/** Confirm that `db` opened `file` itself. Neither node:sqlite nor Python's
    sqlite3 can pass SQLITE_OPEN_NOFOLLOW, so the store checks before it
    opens and again after: SQLite resolves links when it opens a file and
    reports that resolved path in PRAGMA database_list, so a link swapped in
    between the check and the open shows up as a different path here.
    Returns the file's identity. */
function checkOpened(db: DatabaseSync, file: string): FileIdentity {
  const before = identityOf(file);
  let opened: unknown;
  try {
    opened = (db.prepare("PRAGMA database_list").all() as { name?: unknown; file?: unknown }[]).find((r) => r.name === "main")?.file;
  } catch (e) {
    throw storeError("The saved provider file cannot be read.", e, before ?? undefined);
  }
  const id = identityOf(file);
  if (opened !== file || !id || !sameFile(id, before)) throw new StoreError(OPENED_ELSEWHERE);
  return id;
}

type Opened = { db: DatabaseSync; file: FileIdentity };

/** Open the database, or null when none has been created (nothing saved).
    `create` makes the folder (0700) and the file (0600) first. Any other
    failure (a permission change, a damaged file, a link) is a StoreError,
    never "nothing saved", so the env key cannot quietly take over.
    secure_delete overwrites a replaced or removed key's bytes in the file. */
function open(M: Sqlite, create: boolean): Opened | null {
  const file = providerFile();
  try {
    if (create) {
      mkdirSync(path.dirname(file), { recursive: true, mode: 0o700 });
      createPrivate(file);
    } else if (!identityOf(file)) {
      return null;
    }
  } catch (e) {
    if (e instanceof StoreError) throw e;
    throw new StoreError("The saved provider file cannot be read.");
  }
  let db: DatabaseSync | null = null;
  try {
    db = new M.DatabaseSync(file);
    const id = checkOpened(db, file);
    try {
      db.exec("PRAGMA busy_timeout = 5000");
      db.exec("PRAGMA secure_delete = ON");
      db.exec("PRAGMA journal_mode = DELETE");
      db.exec(SCHEMA);
      if ((db.prepare(NEEDS_BACKFILL).get() as { needed?: unknown } | undefined)?.needed) db.exec(BACKFILL);
    } catch (e) {
      throw storeError("The saved provider file cannot be read.", e, id);
    }
    return { db, file: id };
  } catch (e) {
    try {
      db?.close();
    } catch {}
    if (e instanceof StoreError) throw e;
    throw storeError("The saved provider file cannot be read.", e);
  }
}

function run<T>(o: Opened, fn: (db: DatabaseSync) => T): T {
  try {
    return fn(o.db);
  } catch (e) {
    if (e instanceof StoreError) throw e;
    throw storeError("The saved provider file cannot be used.", e, o.file);
  } finally {
    o.db.close();
  }
}

/** How long a recovery waits for one already running, in this server or the
    other, before it gives up with an error. Tests shorten it. */
export const recoveryLock = { waitMs: 10_000 };

/** Run `fn` while holding the recovery lock: BEGIN EXCLUSIVE on
    provider.lock, which server/provider_store.py takes the same way. SQLite
    holds it as a POSIX lock, so it excludes the other server's processes
    and other connections in this one, and the operating system drops it
    when a process dies: a crash never leaves the store locked, and a lock
    file left behind is simply taken. `fn` must be synchronous, so nothing
    else in this process runs while the lock is held; waiting for it does
    not block the event loop. */
async function underRecoveryLock<T>(fn: (M: Sqlite) => T): Promise<T> {
  const M = await sqlite();
  const lockFile = path.join(configDir(), LOCK_NAME);
  let lock: DatabaseSync | null = null;
  try {
    mkdirSync(path.dirname(lockFile), { recursive: true, mode: 0o700 });
    createPrivate(lockFile);
    lock = new M.DatabaseSync(lockFile);
    checkOpened(lock, lockFile);
  } catch (e) {
    try {
      lock?.close();
    } catch {}
    if (e instanceof StoreError) throw e;
    throw new StoreError("The saved provider file cannot be repaired.");
  }
  try {
    const deadline = Date.now() + recoveryLock.waitMs;
    for (;;) {
      try {
        lock.exec("BEGIN EXCLUSIVE");
        break;
      } catch (e) {
        const code = primaryCode(e);
        if (code !== SQLITE_BUSY && code !== SQLITE_LOCKED) throw new StoreError("The saved provider file cannot be repaired.");
        if (Date.now() >= deadline) throw new StoreError(RECOVERY_BUSY);
        await new Promise((r) => setTimeout(r, 25));
      }
    }
    try {
      return fn(M);
    } finally {
      try {
        lock.exec("ROLLBACK");
      } catch {}
    }
  } finally {
    lock.close();
  }
}

/** Whether SQLite still calls `file` damaged. A busy or unreadable file is
    an error, never damage. */
function stillDamaged(M: Sqlite, file: string): boolean {
  let db: DatabaseSync | null = null;
  try {
    db = new M.DatabaseSync(file);
    checkOpened(db, file);
    db.exec("PRAGMA busy_timeout = 5000");
    const row = db.prepare("PRAGMA quick_check(1)").get() as Record<string, unknown> | undefined;
    return Object.values(row ?? {})[0] !== "ok";
  } catch (e) {
    if (e instanceof StoreError) {
      if (e.damaged) return true;
      throw e;
    }
    if (storeError("", e).damaged) return true;
    throw new StoreError("The saved provider file cannot be read.");
  } finally {
    try {
      db?.close();
    } catch {}
  }
}

/** Delete the damaged database `seen` names, with its side files, if the
    path still names that file and SQLite still calls it damaged. Only call
    it under the recovery lock. The side files go first and the database
    last: no new database can be created at the path until the damaged one
    is gone, so nothing deleted here can belong to a healthy one. */
function discardIfStillDamaged(M: Sqlite, seen: FileIdentity | undefined): "discarded" | "replaced" | "gone" {
  const file = providerFile();
  const now = identityOf(file);
  if (!now) return "gone";
  if (!sameFile(now, seen) || !stillDamaged(M, file)) return "replaced";
  try {
    for (const s of SIDE_FILES) rmSync(file + s, { force: true });
    if (!sameFile(identityOf(file), seen)) return "replaced";
    unlinkSync(file);
  } catch (e) {
    if (e instanceof StoreError) throw e;
    throw new StoreError("The saved provider file cannot be removed.");
  }
  return "discarded";
}

/** Delete the damaged database `err` was raised for: the way out of one.
    Under the recovery lock, and only while the path still names that same
    file (device and inode) and SQLite still calls it damaged, so two
    recoveries at once, or one in each server, never delete a database that
    a save created in between, nor its journal. True when this call deleted
    it; false when it was already gone or replaced. */
export async function discardDamaged(err: StoreError): Promise<boolean> {
  if (!err.damaged) throw err;
  return underRecoveryLock((M) => discardIfStillDamaged(M, err.file) === "discarded");
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
  const o = open(await sqlite(), false);
  if (!o) return null;
  const row = run(o, (db) => db.prepare(`SELECT ${COLUMNS} FROM provider WHERE id = 1`).get() as Record<string, unknown> | undefined);
  return rowToProvider(row);
}

// Why a plain save takes no lock beyond SQLite's own: only a recovery ever
// deletes provider.db (discardIfStillDamaged, under the recovery lock), a new
// file is only ever created with O_EXCL, and a writer still holding a file
// that a recovery deleted gets an error from SQLite, not a save that quietly
// went into the deleted file. So a save either lands in the file at the path
// or fails visibly. Keep those three true before adding a lock here.

/** How a save may treat a provider that is already saved:
    - "replace": always (a key the provider checked);
    - "create": only when the store has never held a provider (a migration
      from a browser; a provider saved and later removed still counts);
    - "same-key": only when none is saved or it holds this same key (a key
      the provider could not check must not replace a different one).
    Returns whether the row was written. One statement, so it is atomic. */
export async function saveProvider(cfg: SavedProvider, mode: "replace" | "create" | "same-key"): Promise<boolean> {
  const placeholders = "1, ?, ?, ?, ?, ?, ?, ?";
  const update =
    "api = excluded.api, base_url = excluded.base_url, key_header = excluded.key_header, models_url = excluded.models_url, model = excluded.model, name = excluded.name, api_key = excluded.api_key";
  const sql =
    mode === "create"
      ? `INSERT INTO provider (id, ${COLUMNS}) SELECT ${placeholders} WHERE NOT EXISTS (SELECT 1 FROM meta WHERE k = 'saved') ON CONFLICT(id) DO NOTHING`
      : mode === "same-key"
        ? `INSERT INTO provider (id, ${COLUMNS}) VALUES (${placeholders}) ON CONFLICT(id) DO UPDATE SET ${update} WHERE provider.api_key = excluded.api_key`
        : `INSERT INTO provider (id, ${COLUMNS}) VALUES (${placeholders}) ON CONFLICT(id) DO UPDATE SET ${update}`;
  const attempt = (M: Sqlite) => run(open(M, true)!, (db) => Number(db.prepare(sql).run(...values(cfg)).changes) > 0);
  try {
    return attempt(await sqlite());
  } catch (e) {
    // A checked key may replace a file SQLite calls damaged; the other modes
    // must not, since they only write when they can see what is there, and
    // no other failure (busy, disk full) is a reason to delete anything.
    // The delete and the write that follows happen under the recovery lock.
    if (!(e instanceof StoreError) || !e.damaged || mode !== "replace") throw e;
    return underRecoveryLock((M) => {
      discardIfStillDamaged(M, e.file);
      return attempt(M);
    });
  }
}

/** Change the model and label of the saved provider, only while it still
    holds exactly the key and endpoint `seen` (what the caller read). Returns
    false when it changed or was removed meanwhile; nothing is written then. */
export async function updateModel(seen: SavedProvider, model: string, name: string): Promise<boolean> {
  const o = open(await sqlite(), false);
  if (!o) return false;
  return run(
    o,
    (db) =>
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
    damaged is deleted outright (see discardDamaged), so Remove recovers
    from it. */
export async function removeSaved(): Promise<boolean> {
  try {
    const o = open(await sqlite(), false);
    if (!o) return false;
    return run(o, (db) => Number(db.prepare("DELETE FROM provider WHERE id = 1").run().changes) > 0);
  } catch (e) {
    if (!(e instanceof StoreError) || !e.damaged) throw e;
    return discardDamaged(e);
  }
}

/** The fields of a provider that may leave the server, each passed through
    redact() with the provider's own key: parsing already refuses a key in
    any of them, and this guards anything saved some other way. */
export function publicView(cfg: (PublicProvider & { api_key?: string }) | null | undefined): PublicProvider | null {
  if (!cfg) return null;
  const out: PublicProvider = {};
  for (const k of PUBLIC_FIELDS) {
    const v = cfg[k];
    if (typeof v === "string" && v) out[k] = redact(v, cfg.api_key, cfg.api_key ? encodeURIComponent(cfg.api_key) : null);
  }
  return out;
}

/** `text` with every occurrence of each key replaced. Provider errors name a
    URL, and a URL or an upstream message can echo the key back. */
export function redact(text: string, ...keys: (string | undefined | null)[]): string {
  let out = text;
  for (const k of keys) if (k && k.length >= 4) out = out.split(k).join("[redacted]");
  return out;
}
