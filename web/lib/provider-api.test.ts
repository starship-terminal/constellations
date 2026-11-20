// Unit tests for the server-held provider key (lib/provider-api.ts and
// lib/provider-store.ts): it is tested before it is saved, saved 0600 outside
// the checkout, never returned, resolved saved-then-env, and kept out of every
// response and log line. listModels is a stub, so no provider is called.
// Run with `pnpm test`.
import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { promises as fs, lstatSync, mkdtempSync, realpathSync, rmSync, statSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import { afterEach, beforeEach, describe, it, mock } from "node:test";
import {
  carriesKey,
  handleGet,
  handleRemove,
  handleSave,
  handleTest,
  providerState,
  resolveProvider,
  type ListModels,
} from "./provider-api.ts";
import {
  CONFIG_DIR_ENV,
  configDir,
  discardDamaged,
  insideCheckout,
  LOCK_NAME,
  loadSaved,
  providerFile,
  recoveryLock,
  removeSaved,
  saveProvider,
  updateModel,
  StoreError,
} from "./provider-store.ts";
import { ROOT } from "./repo.ts";

const KEY = "sk-test-0123456789abcdef";
const KEY2 = "sk-test-rotated-fedcba9876";
const ENV_KEY = "sk-env-test-5555555555";
const GOOD = { api: "openai", base_url: "https://models.example/v1", model: "m1", name: "example" };

let dir = "";
let logged: string[] = [];
const calls: { api_key: string; base_url: string }[] = [];

const okModels: ListModels = async (cfg) => {
  calls.push({ api_key: cfg.api_key, base_url: cfg.base_url });
  return { ok: true, models: [{ id: "m1", label: "Model one" }] };
};
const failModels: ListModels = async (cfg) => {
  calls.push({ api_key: cfg.api_key, base_url: cfg.base_url });
  // A provider that echoes the key back in its error text.
  return { ok: false, error: `https://models.example/v1/models answered HTTP 401 for key ${cfg.api_key}` };
};

/** Every string a test produced: response bodies and console output. */
const everything = (...bodies: unknown[]) => [...bodies.map((b) => JSON.stringify(b)), ...logged].join("\n");

beforeEach(() => {
  // Real path: the store resolves links in the folder (macOS's /var is one).
  dir = realpathSync(mkdtempSync(path.join(os.tmpdir(), "ds-provider-test-")));
  process.env[CONFIG_DIR_ENV] = path.join(dir, "config");
  delete process.env.ANTHROPIC_API_KEY;
  delete process.env.DS_CHAT_MODEL;
  calls.length = 0;
  logged = [];
  for (const m of ["log", "error", "warn", "info", "debug"] as const)
    mock.method(console, m, (...args: unknown[]) => void logged.push(args.map(String).join(" ")));
});

afterEach(() => {
  mock.restoreAll();
  delete process.env[CONFIG_DIR_ENV];
  delete process.env.ANTHROPIC_API_KEY;
  rmSync(dir, { recursive: true, force: true });
});

const savedFile = async () => (await loadSaved()) ?? ({} as Record<string, string>);

describe("the config folder", () => {
  it("resolves every shared case as server/provider_store.py does", async () => {
    const { cases } = JSON.parse(await fs.readFile(path.join(ROOT, "server", "provider-config-cases.json"), "utf8"));
    const home = path.join(dir, "home");
    await fs.mkdir(home, { recursive: true });
    const swapcase = path.join(
      path.dirname(ROOT),
      [...path.basename(ROOT)].map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase())).join(""),
    );
    const link = path.join(home, "repo-link");
    await fs.symlink(ROOT, link, "dir");
    const outLink = path.join(home, "out-link");
    await fs.mkdir(path.join(home, "outside"));
    await fs.symlink(path.join(home, "outside"), outLink, "dir");
    const linkDirs: Record<string, string> = {};
    for (const [tag, name] of [
      ["<DB_LINK_DIR>", "provider.db"],
      ["<JOURNAL_LINK_DIR>", "provider.db-journal"],
      ["<LOCK_LINK_DIR>", LOCK_NAME],
    ]) {
      const d = path.join(home, `linked-${name}`);
      await fs.mkdir(d);
      // Dangling on purpose: a link is refused whether or not its target exists.
      await fs.symlink(path.join(home, "elsewhere", name), path.join(d, name));
      linkDirs[tag] = d;
    }
    let caseInsensitive = false;
    try {
      const [a, b] = [statSync(ROOT), statSync(swapcase)];
      caseInsensitive = a.dev === b.dev && a.ino === b.ino;
    } catch {}
    const savedHome = process.env.HOME;
    process.env.HOME = home;
    try {
      for (const c of cases as { value: string; expect: string }[]) {
        let value = c.value;
        for (const [tag, d] of Object.entries(linkDirs)) value = value.replaceAll(tag, d);
        value = value
          .replaceAll("<OUT_LINK>", outLink)
          .replaceAll("<HOME>", home)
          .replaceAll("<REPO_SWAPCASE>", swapcase)
          .replaceAll("<REPO>", ROOT)
          .replaceAll("<LINK>", link);
        let expect = c.expect;
        if (expect === "error-if-case-insensitive") expect = caseInsensitive ? "error" : path.normalize(value);
        process.env[CONFIG_DIR_ENV] = value;
        if (expect === "error") {
          assert.throws(() => configDir(), (e: unknown) => e instanceof StoreError && /absolute path outside the checkout/.test(e.message), value);
          // A refused folder is an error the chat reports, never "nothing saved".
          process.env.ANTHROPIC_API_KEY = ENV_KEY;
          const held = await resolveProvider();
          assert.deepEqual([held.cfg, held.source], [null, "saved"], value);
          delete process.env.ANTHROPIC_API_KEY;
        } else if (expect === "error-link") {
          assert.throws(() => configDir(), (e: unknown) => e instanceof StoreError && /is a symbolic link/.test(e.message), value);
          process.env.ANTHROPIC_API_KEY = ENV_KEY;
          const held = await resolveProvider();
          assert.deepEqual([held.cfg, held.source], [null, "saved"], value);
          assert.match(String(held.error), /symbolic link/, value);
          delete process.env.ANTHROPIC_API_KEY;
        } else {
          assert.equal(configDir(), expect.replaceAll("<HOME>", home), value);
        }
      }
    } finally {
      process.env.HOME = savedHome;
    }
  });

  it("applies the checkout rule only to a real checkout", async () => {
    const root = path.join(dir, "srv");
    await fs.mkdir(path.join(root, "cfg"), { recursive: true });
    // A server started from a folder that is not a checkout refuses nothing.
    assert.equal(insideCheckout(path.join(root, "cfg"), root), false);
    await fs.mkdir(path.join(root, ".git"));
    assert.equal(insideCheckout(path.join(root, "cfg"), root), true);
    await fs.rmdir(path.join(root, ".git"));
    await fs.writeFile(path.join(root, "catalog.json"), "{}");
    assert.equal(insideCheckout(path.join(root, "cfg"), root), true);
    assert.equal(insideCheckout(path.join(dir, "elsewhere"), root), false);
  });
});

describe("the key store", () => {
  it("lives under the override folder, outside the checkout, mode 0600 in a 0700 folder", async () => {
    const r = await handleSave({ ...GOOD, api_key: KEY }, okModels);
    assert.equal(r.status, 200);
    assert.equal(providerFile(), path.join(dir, "config", "provider.db"));
    assert.equal((await fs.stat(providerFile())).mode & 0o777, 0o600);
    assert.equal((await fs.stat(path.join(dir, "config"))).mode & 0o777, 0o700);
    assert.equal((await savedFile()).api_key, KEY);
    // SQLite's side files get the database file's mode.
    for (const f of await fs.readdir(path.join(dir, "config")))
      assert.equal((await fs.stat(path.join(dir, "config", f))).mode & 0o777, 0o600, f);
  });
});

describe("saving a key", () => {
  it("tests the key with one model-list call before saving it", async () => {
    const r = await handleSave({ ...GOOD, api_key: KEY }, okModels);
    assert.deepEqual(calls, [{ api_key: KEY, base_url: GOOD.base_url }]);
    assert.equal(r.body.ok, true);
    assert.equal(r.body.source, "saved");
    assert.deepEqual(r.body.models, [{ id: "m1", label: "Model one" }]);
  });

  it("never returns the key, only where it comes from", async () => {
    const saved = await handleSave({ ...GOOD, api_key: KEY }, okModels);
    const got = await handleGet();
    const status = await providerState();
    assert.equal(got.body.source, "saved");
    assert.deepEqual(got.body.provider, GOOD);
    assert.ok(!everything(saved.body, got.body, status).includes(KEY));
    assert.ok(!JSON.stringify(got.body).includes("api_key"));
  });

  it("does not save a key that fails its test, and redacts it from the error", async () => {
    const r = await handleSave({ ...GOOD, api_key: KEY }, failModels);
    assert.equal(r.body.ok, false);
    assert.equal(r.body.saved, false);
    assert.match(String(r.body.error), /HTTP 401 for key \[redacted\]/);
    assert.equal(await loadSaved(), null);
    assert.ok(!everything(r.body).includes(KEY));
  });

  it("rotates: the old key stays until the new one passes, then one write replaces it", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    const bad = await handleSave({ ...GOOD, api_key: KEY2 }, failModels);
    assert.equal(bad.body.ok, false);
    assert.equal((await savedFile()).api_key, KEY);
    const good = await handleSave({ ...GOOD, api_key: KEY2 }, okModels);
    assert.equal(good.body.ok, true);
    assert.equal((await savedFile()).api_key, KEY2);
    assert.ok(!everything(bad.body, good.body).includes(KEY2));
  });

  it("changes the model without the key, but not the endpoint", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    calls.length = 0;
    const model = await handleSave({ ...GOOD, model: "m2" }, okModels);
    assert.equal(model.status, 200);
    assert.deepEqual(calls, []);
    assert.deepEqual([(await savedFile()).model, (await savedFile()).api_key], ["m2", KEY]);
    for (const change of [{ base_url: "https://elsewhere.example/v1" }, { api: "anthropic" }, { key_header: "x-other" }, { models_url: "https://models.example/list" }]) {
      const r = await handleSave({ ...GOOD, ...change }, okModels);
      assert.equal(r.status, 400, JSON.stringify(change));
      assert.match(String(r.body.error), /needs the API key again/);
    }
    assert.equal((await savedFile()).base_url, GOOD.base_url);
  });

  it("refuses a save with no model, or with no key and nothing saved", async () => {
    assert.equal((await handleSave({ ...GOOD, model: "", api_key: KEY }, okModels)).status, 400);
    assert.equal((await handleSave({ ...GOOD }, okModels)).status, 400);
    assert.deepEqual(calls, []);
  });

  it("refuses ill-typed fields and a key with whitespace, without quoting the key", async () => {
    for (const body of [null, [], "x", { ...GOOD, base_url: 1 }, { ...GOOD, api_key: ["k"] }, { ...GOOD, api: "other" }]) {
      const r = await handleSave(body, okModels);
      assert.equal(r.status, 400, JSON.stringify(body));
    }
    const r = await handleSave({ ...GOOD, api_key: `${KEY}\nx-injected: 1` }, okModels);
    assert.equal(r.status, 400);
    assert.ok(!everything(r.body).includes(KEY));
    assert.deepEqual(calls, []);
  });

  it("logs only an error's type when something unexpected fails", async () => {
    const r = await handleSave({ ...GOOD, api_key: KEY }, async () => {
      throw new TypeError(`Headers.append: "Bearer ${KEY}" is an invalid header value.`);
    });
    // listModels' own throw is a failed test, its text redacted.
    assert.equal(r.body.ok, false);
    assert.ok(!everything(r.body).includes(KEY));
    // A failure in the store itself: the folder is a file, so the write fails.
    await fs.writeFile(path.join(dir, "config"), "not a folder");
    const broken = await handleSave({ ...GOOD, api_key: KEY }, okModels);
    assert.equal(broken.status, 500);
    assert.ok(!everything(broken.body).includes(KEY));
    assert.ok(!logged.join("\n").includes(KEY));
  });
});

describe("review fixes", () => {
  const noList: ListModels = async (cfg) => {
    calls.push({ api_key: cfg.api_key, base_url: cfg.base_url });
    return { ok: true, models: [], note: "no model list at this endpoint; type the model name" };
  };

  it("a migration never replaces a saved provider", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    calls.length = 0;
    const r = await handleSave({ ...GOOD, api_key: KEY2, migrate: true }, failModels);
    assert.deepEqual([r.body.ok, r.body.existing], [false, true]);
    assert.deepEqual(calls, [], "no provider call for a migration that cannot be saved");
    assert.equal((await savedFile()).api_key, KEY);
    assert.ok(!everything(r.body).includes(KEY2));
  });

  it("a migration never brings back a key the user removed", async () => {
    // The server saved a migrated key but the reply was lost, so the browser
    // kept its copy; the user then removed the key on the server.
    await handleSave({ ...GOOD, api_key: KEY, migrate: true }, okModels);
    await handleRemove();
    const again = await handleSave({ ...GOOD, api_key: KEY, migrate: true }, okModels);
    assert.deepEqual([again.body.ok, again.body.existing], [false, true]);
    assert.equal(await loadSaved(), null);
    // A save the user makes still works.
    assert.equal((await handleSave({ ...GOOD, api_key: KEY2 }, okModels)).body.ok, true);
  });

  it("a file from before the meta backfill still blocks a revived key", async () => {
    // A provider.db made by an earlier version: a saved row, an empty meta.
    const { DatabaseSync } = await import("node:sqlite");
    await fs.mkdir(path.join(dir, "config"), { recursive: true });
    const old = new DatabaseSync(providerFile());
    old.exec(`CREATE TABLE provider (id INTEGER PRIMARY KEY CHECK (id = 1), api TEXT NOT NULL, base_url TEXT NOT NULL,
      key_header TEXT NOT NULL DEFAULT '', models_url TEXT NOT NULL DEFAULT '', model TEXT NOT NULL,
      name TEXT NOT NULL DEFAULT '', api_key TEXT NOT NULL);
      CREATE TABLE meta (k TEXT PRIMARY KEY);
      INSERT INTO provider VALUES (1, 'openai', 'https://models.example/v1', '', '', 'm1', '', '${KEY}');`);
    old.close();
    await handleRemove();
    const again = await handleSave({ ...GOOD, api_key: KEY, migrate: true }, okModels);
    assert.deepEqual([again.body.ok, again.body.existing], [false, true]);
    assert.equal(await loadSaved(), null);
  });

  it("a migration saves when nothing is saved, and needs a key", async () => {
    const r = await handleSave({ ...GOOD, api_key: KEY, migrate: true }, okModels);
    assert.equal(r.body.ok, true);
    assert.equal((await savedFile()).api_key, KEY);
    assert.equal((await handleSave({ ...GOOD, migrate: true }, okModels)).status, 400);
    assert.equal((await handleSave({ ...GOOD, api_key: KEY, migrate: "yes" }, okModels)).status, 400);
  });

  it("an unchecked key (no model list) never replaces a working one", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    const r = await handleSave({ ...GOOD, api_key: KEY2 }, noList);
    assert.equal(r.body.ok, false);
    assert.match(String(r.body.error), /could not be checked/);
    assert.equal((await savedFile()).api_key, KEY);
    // With nothing saved it may be saved, flagged as unchecked.
    await handleRemove();
    const first = await handleSave({ ...GOOD, api_key: KEY2 }, noList);
    assert.deepEqual([first.body.ok, first.body.verified], [true, false]);
  });

  it("treats a blank key header as its API's default", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    const r = await handleSave({ ...GOOD, key_header: "Authorization", model: "m3" }, okModels);
    assert.equal(r.status, 200);
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    await handleRemove();
    const env = await handleTest({ api: "anthropic", base_url: "https://api.anthropic.com", key_header: "x-api-key" }, okModels);
    assert.equal(env.body.ok, true);
  });

  it("a model-only save never writes back a key that changed or went away", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    const seen = (await loadSaved())!;
    // Another request replaces the key after this one read it.
    await saveProvider({ ...seen, api_key: KEY2 }, "replace");
    assert.equal(await updateModel(seen, "m9", ""), false);
    assert.deepEqual([(await savedFile()).api_key, (await savedFile()).model], [KEY2, GOOD.model]);
    // Or removes it.
    const now = (await loadSaved())!;
    await handleRemove();
    assert.equal(await updateModel(now, "m9", ""), false);
    assert.equal(await loadSaved(), null);
  });

  it("decides and writes in one statement for each save mode", async () => {
    const a = { ...GOOD, api_key: KEY };
    assert.equal(await saveProvider(a, "create"), true);
    assert.equal(await saveProvider({ ...a, api_key: KEY2 }, "create"), false);
    assert.equal(await saveProvider({ ...a, api_key: KEY2 }, "same-key"), false);
    assert.equal(await saveProvider({ ...a, model: "m5" }, "same-key"), true);
    assert.equal(await saveProvider({ ...a, api_key: KEY2 }, "replace"), true);
    assert.equal((await savedFile()).api_key, KEY2);
  });
});

describe("recovery and key bytes", () => {
  const rawBytes = async () => {
    let all = "";
    for (const f of await fs.readdir(path.join(dir, "config")))
      all += (await fs.readFile(path.join(dir, "config", f))).toString("latin1");
    return all;
  };

  it("leaves no copy of a removed or replaced key in the files", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    await handleSave({ ...GOOD, api_key: KEY2 }, okModels);
    assert.ok(!(await rawBytes()).includes(KEY), "the replaced key is gone");
    await handleRemove();
    assert.ok(!(await rawBytes()).includes(KEY2), "the removed key is gone");
  });

  it("Remove and a checked replacement recover a damaged file", async () => {
    await fs.mkdir(path.join(dir, "config"), { recursive: true });
    await fs.writeFile(providerFile(), `damaged ${KEY} `.repeat(300));
    await fs.writeFile(`${providerFile()}-journal`, `old key ${KEY}`);
    assert.equal((await providerState()).configured, false);
    const removed = await handleRemove();
    assert.deepEqual([removed.status, removed.body.removed, removed.body.source], [200, true, "none"]);
    // Only the recovery lock stays: an empty file that never holds a key.
    assert.deepEqual(await fs.readdir(path.join(dir, "config")), [LOCK_NAME]);
    assert.equal((await fs.stat(path.join(dir, "config", LOCK_NAME))).size, 0);
    await fs.writeFile(providerFile(), `damaged ${KEY} `.repeat(300));
    const saved = await handleSave({ ...GOOD, api_key: KEY2 }, okModels);
    assert.equal(saved.body.ok, true);
    assert.equal((await savedFile()).api_key, KEY2);
    // A migration never replaces what it cannot read.
    await fs.writeFile(providerFile(), `damaged ${KEY} `.repeat(300));
    const moved = await handleSave({ ...GOOD, api_key: KEY2, migrate: true }, okModels);
    assert.equal(moved.body.ok, false);
  });

  it("tightens a loose existing file before saving a key into it", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    await fs.chmod(providerFile(), 0o644);
    await handleSave({ ...GOOD, api_key: KEY2 }, okModels);
    assert.equal((await fs.stat(providerFile())).mode & 0o777, 0o600);
  });

  it("reads a file made read-only after a save, and refuses a save into it without the env key", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    await fs.chmod(providerFile(), 0o400);
    try {
      const st = await providerState();
      assert.deepEqual([st.source, st.configured, st.provider?.model], ["saved", true, GOOD.model]);
      const held = await resolveProvider();
      assert.deepEqual([held.source, held.cfg?.api_key], ["saved", KEY]);
      const r = await handleSave({ ...GOOD, api_key: KEY2 }, okModels);
      assert.equal(r.status, 500);
      assert.match(String(r.body.error), /read-only/);
      assert.equal((await handleRemove()).status, 500);
      assert.equal((await fs.stat(providerFile())).mode & 0o777, 0o400, "a read-only file stays read-only");
      assert.equal((await resolveProvider()).cfg?.api_key, KEY, "still the saved key, never the env key");
      assert.ok(!everything(r.body).includes(KEY2));
    } finally {
      await fs.chmod(providerFile(), 0o600);
    }
  });

  it("never deletes a working database because it is busy", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    const { DatabaseSync } = await import("node:sqlite");
    const other = new DatabaseSync(providerFile());
    other.exec("BEGIN EXCLUSIVE");
    try {
      const r = await handleSave({ ...GOOD, api_key: KEY2 }, okModels);
      assert.equal(r.status, 500);
      const removed = await handleRemove();
      assert.equal(removed.status, 500);
    } finally {
      other.exec("ROLLBACK");
      other.close();
    }
    assert.equal((await savedFile()).api_key, KEY, "the working provider is still there");
  });

  it("reports an unreadable folder instead of falling back to the env key", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    await fs.chmod(path.join(dir, "config"), 0o000);
    try {
      const held = await resolveProvider();
      assert.equal(held.cfg, null);
      assert.equal(held.source, "saved");
      assert.ok(held.error);
    } finally {
      await fs.chmod(path.join(dir, "config"), 0o700);
    }
  });
});

describe("the recovery lock", () => {
  const damage = async () => {
    await fs.mkdir(path.join(dir, "config"), { recursive: true });
    await fs.writeFile(providerFile(), `damaged ${KEY} `.repeat(300));
  };
  /** The StoreError a request sees on the damaged file, as it would before recovering. */
  const seenDamage = async (): Promise<StoreError> => {
    const e = await loadSaved().then(
      () => null,
      (err: unknown) => err,
    );
    assert.ok(e instanceof StoreError && e.damaged && e.file, "the error names the damaged file");
    return e;
  };
  const identity = (f: string) => {
    const st = lstatSync(f, { bigint: true });
    return { dev: st.dev, ino: st.ino };
  };

  it("two recoveries of one damaged file never delete a save made in between, nor its live journal", async () => {
    await damage();
    // Two requests both find the file damaged.
    const first = await seenDamage();
    const second = await seenDamage();
    assert.equal(await discardDamaged(first), true);
    // A fresh save lands, and another write to it is in flight.
    assert.equal((await handleSave({ ...GOOD, api_key: KEY2 }, okModels)).body.ok, true);
    const { DatabaseSync } = await import("node:sqlite");
    const writer = new DatabaseSync(providerFile());
    writer.exec("BEGIN IMMEDIATE");
    writer.exec("UPDATE provider SET name = 'in flight' WHERE id = 1");
    const journal = `${providerFile()}-journal`;
    assert.ok((await fs.stat(journal)).isFile(), "the write has a live journal");
    try {
      // The second recovery still holds its old error: it must do nothing.
      assert.equal(await discardDamaged(second), false);
      assert.equal(await removeSaved().catch(() => "busy"), "busy", "a busy file is reported, not deleted");
      assert.ok((await fs.stat(journal)).isFile(), "the live journal is still there");
    } finally {
      writer.exec("COMMIT");
      writer.close();
    }
    const saved = await savedFile();
    assert.deepEqual([saved.api_key, saved.name], [KEY2, "in flight"]);
  });

  it("never deletes a healthy file, even one with the damaged file's identity", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    const forged = new StoreError("forged");
    forged.damaged = true;
    forged.file = identity(providerFile());
    assert.equal(await discardDamaged(forged), false);
    forged.file = undefined;
    assert.equal(await discardDamaged(forged), false);
    assert.equal((await savedFile()).api_key, KEY);
    // Only damage is a reason to delete anything.
    await assert.rejects(discardDamaged(new StoreError("busy")), /busy/);
  });

  it("waits for a recovery that holds the lock, then goes ahead", async () => {
    await damage();
    const { DatabaseSync } = await import("node:sqlite");
    const other = new DatabaseSync(path.join(dir, "config", LOCK_NAME));
    other.exec("BEGIN EXCLUSIVE");
    const removing = removeSaved();
    await new Promise((r) => setTimeout(r, 200));
    assert.ok((await fs.stat(providerFile())).isFile(), "nothing is deleted while another recovery holds the lock");
    other.exec("ROLLBACK");
    other.close();
    assert.equal(await removing, true);
    await assert.rejects(fs.stat(providerFile()), { code: "ENOENT" });
  });

  it("gives up while another process holds it, deleting nothing, and takes it once that process dies", async (t) => {
    // The other process is the Python store's own lock, so this also checks
    // that both languages exclude each other.
    const py = process.env.PYTHON ?? "python3";
    await damage();
    const lockFile = path.join(dir, "config", LOCK_NAME);
    const child = spawn(
      py,
      ["-c", "import sqlite3,sys\nc=sqlite3.connect(sys.argv[1],isolation_level=None)\nc.execute('BEGIN EXCLUSIVE')\nprint('held',flush=True)\nsys.stdin.read()", lockFile],
      { stdio: ["pipe", "pipe", "inherit"] },
    );
    const held = await new Promise<boolean>((resolve) => {
      child.on("error", () => resolve(false));
      child.stdout.on("data", (b: Buffer) => b.toString().includes("held") && resolve(true));
      child.on("exit", () => resolve(false));
    });
    if (!held) {
      t.skip(`${py} is required`);
      return;
    }
    const wait = recoveryLock.waitMs;
    recoveryLock.waitMs = 300;
    try {
      await assert.rejects(removeSaved(), (e: unknown) => e instanceof StoreError && !e.damaged && /being repaired/.test(e.message));
      assert.ok((await fs.stat(providerFile())).isFile(), "nothing was deleted");
      // A crash while holding the lock: the operating system drops it.
      const exited = new Promise((r) => child.on("exit", r));
      child.kill("SIGKILL");
      await exited;
      assert.equal(await removeSaved(), true);
      await assert.rejects(fs.stat(providerFile()), { code: "ENOENT" });
      assert.equal((await fs.stat(lockFile)).mode & 0o777, 0o600, "the lock file is tightened");
      assert.equal((await fs.stat(lockFile)).size, 0, "the lock file holds nothing");
    } finally {
      recoveryLock.waitMs = wait;
      child.kill("SIGKILL");
    }
  });
});

describe("a link in the store's folder", () => {
  it("is refused, and nothing is written through it", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    await fs.mkdir(path.join(dir, "config"), { recursive: true });
    const target = path.join(dir, "target.db");
    await fs.writeFile(target, "");
    await fs.symlink(target, path.join(dir, "config", "provider.db"));
    const r = await handleSave({ ...GOOD, api_key: KEY }, okModels);
    assert.equal(r.status, 500);
    assert.match(String(r.body.error), /symbolic link/);
    assert.equal((await fs.stat(target)).size, 0, "the link's target was not written");
    // Reported, not replaced by the env key.
    const held = await resolveProvider();
    assert.deepEqual([held.cfg, held.source], [null, "saved"]);
    // Remove does not delete through it either.
    assert.equal((await handleRemove()).status, 500);
    assert.ok(lstatSync(path.join(dir, "config", "provider.db")).isSymbolicLink());
    assert.ok(!everything(r.body).includes(KEY));
  });

  it("is refused for a side file too, before a key is written next to it", async () => {
    await fs.mkdir(path.join(dir, "config"), { recursive: true });
    const target = path.join(dir, "journal-target");
    await fs.symlink(target, path.join(dir, "config", "provider.db-journal"));
    const r = await handleSave({ ...GOOD, api_key: KEY }, okModels);
    assert.equal(r.status, 500);
    await assert.rejects(fs.stat(target), { code: "ENOENT" });
    await assert.rejects(fs.stat(path.join(dir, "config", "provider.db")), { code: "ENOENT" });
  });

  it("in the folder's own path is resolved, so the file is opened by its real path", async () => {
    await fs.mkdir(path.join(dir, "real"), { recursive: true });
    await fs.symlink(path.join(dir, "real"), path.join(dir, "via"), "dir");
    process.env[CONFIG_DIR_ENV] = path.join(dir, "via", "cfg");
    assert.equal(providerFile(), path.join(dir, "real", "cfg", "provider.db"));
    assert.equal((await handleSave({ ...GOOD, api_key: KEY }, okModels)).body.ok, true);
    assert.ok((await fs.stat(path.join(dir, "real", "cfg", "provider.db"))).isFile());
    assert.equal((await savedFile()).api_key, KEY);
  });
});

describe("a key in a URL field", () => {
  it("is refused at parse on save and test, without quoting it", async () => {
    for (const extra of [
      { base_url: `https://models.example/v1?key=${KEY}` },
      { models_url: `https://models.example/v1/models?key=${encodeURIComponent(KEY)}` },
      { name: `mine ${KEY}` },
    ]) {
      for (const handler of [handleSave, handleTest]) {
        const r = await handler({ ...GOOD, ...extra, api_key: KEY }, okModels);
        assert.equal(r.status, 400, JSON.stringify(extra));
        assert.match(String(r.body.error), /API key field only/);
        assert.ok(!everything(r.body).includes(KEY));
      }
    }
    assert.deepEqual(calls, []);
    assert.equal(await loadSaved(), null);
  });

  it("is refused for every shared case, decoding %XX as Python does", async () => {
    const spec = JSON.parse(await fs.readFile(path.join(ROOT, "server", "provider-key-url-cases.json"), "utf8"));
    const key: string = spec.key;
    // Every character Python's quote(safe="") encodes, upper case hex.
    const upper = [...new TextEncoder().encode(key)]
      .map((b) => (/[A-Za-z0-9_.~-]/.test(String.fromCharCode(b)) ? String.fromCharCode(b) : `%${b.toString(16).toUpperCase().padStart(2, "0")}`))
      .join("");
    const lower = upper.replace(/%[0-9A-F]{2}/g, (m) => m.toLowerCase());
    assert.notEqual(upper, lower);
    for (const c of spec.cases as Record<string, string>[]) {
      const fields: Record<string, string> = {};
      for (const [k, v] of Object.entries(c))
        if (k !== "expect") fields[k] = v.replaceAll("<KEY_UPPER>", upper).replaceAll("<KEY_LOWER>", lower).replaceAll("<KEY>", key);
      const r = await handleSave({ ...GOOD, ...fields, api_key: key }, okModels);
      if (c.expect === "refuse") {
        assert.equal(r.status, 400, JSON.stringify(fields));
        assert.match(String(r.body.error), /API key field only/);
      } else {
        assert.deepEqual([r.status, r.body.ok], [200, true], JSON.stringify(fields));
      }
      assert.ok(!JSON.stringify(r.body).includes(key));
    }
  });

  it("is redacted from the public fields if it was saved some other way", async () => {
    await saveProvider({ ...GOOD, base_url: `https://models.example/v1?key=${KEY}`, api_key: KEY }, "replace");
    const got = await handleGet();
    assert.equal((got.body.provider as Record<string, string>).base_url, "https://models.example/v1?key=[redacted]");
    assert.ok(!everything(got.body, await providerState()).includes(KEY));
  });
});

describe("testing a key", () => {
  it("answers an empty or missing body with the same 400 as server/routes.py", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    for (const body of [undefined, null, {}, [], "x"])
      for (const handler of [handleTest, handleSave]) {
        const r = await handler(body, okModels);
        assert.deepEqual([r.status, r.body.error], [400, "JSON body required"], JSON.stringify(body));
      }
    assert.deepEqual(calls, [], "no provider call, not even with an env key held");
  });

  it("tests a typed key against the typed endpoint", async () => {
    const r = await handleTest({ ...GOOD, api_key: KEY }, okModels);
    assert.equal(r.body.ok, true);
    assert.deepEqual(calls, [{ api_key: KEY, base_url: GOOD.base_url }]);
    assert.ok(!everything(r.body).includes(KEY));
  });

  it("tests the held key only against the endpoint it is held for", async () => {
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    calls.length = 0;
    const same = await handleTest({ ...GOOD, base_url: GOOD.base_url + "/" }, okModels);
    assert.equal(same.body.ok, true);
    assert.deepEqual(calls, [{ api_key: KEY, base_url: GOOD.base_url }]);
    calls.length = 0;
    const other = await handleTest({ ...GOOD, base_url: "https://attacker.example/v1" }, okModels);
    assert.equal(other.status, 400);
    assert.deepEqual(calls, []);
  });

  it("tests the env key only against Anthropic's own API", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    const ok = await handleTest({ api: "anthropic" }, okModels);
    assert.equal(ok.body.ok, true);
    assert.deepEqual(calls, [{ api_key: ENV_KEY, base_url: "https://api.anthropic.com" }]);
    const other = await handleTest({ api: "openai", base_url: "https://attacker.example/v1" }, okModels);
    assert.equal(other.status, 400);
    assert.ok(!everything(ok.body, other.body).includes(ENV_KEY));
  });

  it("asks for a key when none is held", async () => {
    const r = await handleTest({ ...GOOD }, okModels);
    assert.equal(r.status, 400);
    assert.deepEqual(calls, []);
  });
});

describe("precedence", () => {
  it("is none with nothing saved and no env key", async () => {
    const s = await providerState();
    assert.deepEqual([s.source, s.configured, s.provider], ["none", false, null]);
    assert.equal((await resolveProvider()).cfg, null);
  });

  it("uses the env key while nothing is saved", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    process.env.DS_CHAT_MODEL = "claude-env";
    const s = await providerState();
    assert.deepEqual([s.source, s.configured, s.provider?.model], ["env", true, "claude-env"]);
    assert.equal((await resolveProvider()).cfg?.api_key, ENV_KEY);
    assert.ok(!everything(s, await handleGet()).includes(ENV_KEY));
  });

  it("prefers the saved key, and goes back to env once it is removed", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    await handleSave({ ...GOOD, api_key: KEY }, okModels);
    assert.equal((await resolveProvider()).cfg?.api_key, KEY);
    assert.equal((await providerState()).envAvailable, true);
    const removed = await handleRemove();
    assert.deepEqual([removed.body.removed, removed.body.source], [true, "env"]);
    assert.equal(await loadSaved(), null);
    assert.equal((await resolveProvider()).cfg?.api_key, ENV_KEY);
    assert.equal((await handleRemove()).body.removed, false);
  });

  it("reports a broken saved file instead of falling back to env", async () => {
    process.env.ANTHROPIC_API_KEY = ENV_KEY;
    await fs.mkdir(path.join(dir, "config"), { recursive: true });
    await fs.writeFile(providerFile(), `not a database, key ${KEY} `.repeat(200));
    const s = await providerState();
    assert.deepEqual([s.source, s.configured], ["saved", false]);
    assert.match(String(s.error), /cannot be (read|used)/);
    const held = await resolveProvider();
    assert.equal(held.cfg, null);
    assert.ok(held.error);
    assert.ok(!everything(s, held).includes(KEY));
  });
});

describe("carriesKey", () => {
  it("spots a chat body that still sends its key", () => {
    assert.equal(carriesKey({ messages: [], provider: { api_key: KEY } }), true);
    for (const body of [{ messages: [] }, { provider: null }, { provider: { model: "m" } }, { provider: { api_key: "" } }, null, "x"])
      assert.equal(carriesKey(body), false, JSON.stringify(body));
  });
});
