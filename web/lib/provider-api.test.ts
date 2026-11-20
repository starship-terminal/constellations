// Unit tests for the server-held provider key (lib/provider-api.ts and
// lib/provider-store.ts): it is tested before it is saved, saved 0600 outside
// the checkout, never returned, resolved saved-then-env, and kept out of every
// response and log line. listModels is a stub, so no provider is called.
// Run with `pnpm test`.
import assert from "node:assert/strict";
import { promises as fs, mkdtempSync, rmSync } from "node:fs";
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
import { CONFIG_DIR_ENV, loadSaved, providerFile, saveProvider, updateModel } from "./provider-store.ts";

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
  dir = mkdtempSync(path.join(os.tmpdir(), "ds-provider-test-"));
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
    assert.ok(logged.length > 0);
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

describe("testing a key", () => {
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
