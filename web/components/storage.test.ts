// Unit tests for the browser-storage readers. Run with `pnpm test`.
import assert from "node:assert/strict";
import { afterEach, describe, it } from "node:test";
import { migrateStoredProvider, readSavedPaths, readStoredProvider, saveReplyOf } from "./storage.ts";

const store = new Map<string, string>();
Object.defineProperty(globalThis, "localStorage", {
  configurable: true,
  value: {
    getItem: (k: string) => store.get(k) ?? null,
    setItem: (k: string, v: string) => void store.set(k, v),
    removeItem: (k: string) => void store.delete(k),
  },
});

describe("readStoredProvider", () => {
  afterEach(() => store.clear());

  it("keeps string fields and turns numbers into text", () => {
    store.set("ds-provider", JSON.stringify({ api: "openai", model: 1, api_key: "k", name: null, extra: { a: 1 }, on: true }));
    const p = readStoredProvider();
    assert.deepEqual(p, { api: "openai", model: "1", api_key: "k", on: "true" });
    // What Settings' Save does with it: must not throw.
    const cfg: Record<string, string> = Object.assign({ model: "" }, p);
    assert.equal(cfg.model.trim(), "1");
  });

  it("drops a null model so the form's empty default applies", () => {
    store.set("ds-provider", JSON.stringify({ model: null }));
    const cfg: Record<string, string> = Object.assign({ model: "" }, readStoredProvider());
    assert.deepEqual(cfg, { model: "" });
  });

  it("is null for a missing, malformed or non-object value", () => {
    assert.equal(readStoredProvider(), null);
    for (const raw of ["nope{", "[1]", "5", '"x"']) {
      store.set("ds-provider", raw);
      assert.equal(readStoredProvider(), null, raw);
    }
  });
});

describe("readSavedPaths", () => {
  afterEach(() => store.clear());

  it("keeps only strings", () => {
    store.set("ds-saved", JSON.stringify(["a.png", 3, null, "b.png"]));
    assert.deepEqual(readSavedPaths(), ["a.png", "b.png"]);
  });
});

describe("saveReplyOf", () => {
  it("counts only a JSON answer below 500 as the server's decision", () => {
    assert.deepEqual(saveReplyOf(200, { ok: true }), { ok: true, existing: false, definite: true, error: undefined });
    assert.equal(saveReplyOf(200, { ok: false, error: "HTTP 401" }).definite, true);
    assert.equal(saveReplyOf(200, { ok: false, existing: true }).existing, true);
    assert.equal(saveReplyOf(400, { ok: false, error: "Send a JSON object." }).definite, true);
    assert.equal(saveReplyOf(500, { ok: false, error: "busy" }).definite, false);
    assert.deepEqual(saveReplyOf(502, null), { ok: false, existing: false, definite: false, error: "HTTP 502" });
    assert.equal(saveReplyOf(200, null).definite, false);
  });
});

describe("migrateStoredProvider", () => {
  afterEach(() => store.clear());
  const KEY = "sk-old-browser-key-1234567";
  const old = { api: "openai", base_url: "https://models.example/v1", api_key: KEY, model: "m1", name: "x" };

  it("sends a stored key to the server once, then deletes it", async () => {
    store.set("ds-provider", JSON.stringify(old));
    const sent: Record<string, string | boolean>[] = [];
    const note = await migrateStoredProvider(async (b) => {
      sent.push(b);
      assert.ok(store.has("ds-provider"), "deleted only after the save answered");
      return { ok: true };
    });
    assert.deepEqual(sent, [{ migrate: true, ...old }]);
    assert.equal(store.has("ds-provider"), false);
    assert.match(String(note), /^Moved the API key/);
    assert.ok(!String(note).includes(KEY));
    // Nothing left to move on the next load.
    assert.equal(await migrateStoredProvider(async () => assert.fail("no second save")), null);
  });

  it("deletes the stored key once the server has decided against it, and says so without quoting it", async () => {
    // A failed key test (a JSON 200) and a refused body (a JSON 4xx) are decisions.
    for (const reply of [{ ok: false, definite: true, error: `HTTP 401 for ${KEY}` }, { ok: false, definite: true, error: "Send a JSON object." }]) {
      store.set("ds-provider", JSON.stringify(old));
      const note = await migrateStoredProvider(async () => reply);
      assert.equal(store.has("ds-provider"), false);
      assert.match(String(note), /^Deleted the API key .*enter it again/);
      assert.ok(!String(note).includes(KEY));
    }
  });

  it("keeps the stored key when the server did not answer, answered 5xx or not in JSON", async () => {
    const outcomes: (() => Promise<{ ok: boolean; definite?: boolean; error?: string }>)[] = [
      async () => {
        throw new TypeError("Failed to fetch");
      },
      // What saveProvider returns for a proxy's 502 page or a busy store's 500.
      async () => ({ ok: false, definite: false, error: "HTTP 502" }),
      async () => ({ ok: false, definite: false, error: "The saved provider file cannot be used." }),
    ];
    for (const save of outcomes) {
      store.set("ds-provider", JSON.stringify(old));
      const note = await migrateStoredProvider(save);
      assert.equal(store.get("ds-provider"), JSON.stringify(old), "the only copy stays");
      assert.match(String(note), /stays here for now/);
      assert.ok(!String(note).includes(KEY));
    }
    // The next page load tries again and, once the server saves it, deletes it.
    const note = await migrateStoredProvider(async () => ({ ok: true, definite: true }));
    assert.match(String(note), /^Moved the API key/);
    assert.equal(store.has("ds-provider"), false);
  });

  it("keeps the server's own key when it already has one, and says so", async () => {
    store.set("ds-provider", JSON.stringify(old));
    const note = await migrateStoredProvider(async () => ({ ok: false, existing: true, error: "kept" }));
    assert.equal(store.has("ds-provider"), false);
    assert.match(String(note), /already has, or had, its own saved key/);
  });

  it("runs once for calls that overlap", async () => {
    store.set("ds-provider", JSON.stringify(old));
    let calls = 0;
    const save = async () => {
      calls++;
      await new Promise((r) => setTimeout(r, 10));
      return { ok: true };
    };
    const [a, b] = await Promise.all([migrateStoredProvider(save), migrateStoredProvider(save)]);
    assert.equal(calls, 1);
    assert.equal(a, b);
  });

  it("drops a leftover value with no key silently, and does nothing when there is none", async () => {
    assert.equal(await migrateStoredProvider(async () => assert.fail("nothing to send")), null);
    for (const raw of [JSON.stringify({ model: "m" }), "nope{"]) {
      store.set("ds-provider", raw);
      assert.equal(await migrateStoredProvider(async () => assert.fail("nothing to send")), null);
      assert.equal(store.has("ds-provider"), false);
    }
  });
});
