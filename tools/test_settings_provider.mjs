// Runs the docs-site Settings page's provider script (tools/site.py,
// SETTINGS_BODY) against a stub DOM, localStorage and fetch. tools/test_site.py
// writes the script to a file and passes its path as SETTINGS_SCRIPT.
// The page must never store a key in the browser: with a server it sends a
// key once to /api/provider and keeps nothing; on the published copy (no
// /api/) it stores nothing at all. A key an older version left in
// localStorage is moved to the server once, or just deleted, and the page says so.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import vm from "node:vm";

const SCRIPT = readFileSync(process.env.SETTINGS_SCRIPT, "utf8");
const KEY = "sk-old-browser-key-1234567";

class El {
  constructor(id) {
    this.id = id;
    // The form starts hidden, as in the page's markup.
    this.hidden = id === "pf";
    this.value = "";
    this.textContent = "";
    this.placeholder = "";
    this.disabled = false;
    this.dataset = {};
    this.children = [];
    this.attrs = {};
    this.innerHTML = "";
  }
  addEventListener() {}
  appendChild(c) {
    this.children.push(c);
  }
  setAttribute(k, v) {
    this.attrs[k] = v;
  }
  querySelectorAll() {
    return [];
  }
}

const IDS = ["pf-base", "pf-key", "pf-model", "pf-models", "pf-status", "pf", "pf-off", "pf-templates", "pf-test", "pf-save",
  "pf-clear", "pf-source", "pf-badge", "pf-using", "pf-notice"];

/** Run the page with `stored` in localStorage and `server` answering fetch
    (null: no server, every fetch fails as on the published copy). */
async function run(stored, server) {
  const els = Object.fromEntries(IDS.map((id) => [id, new El(id)]));
  const store = new Map(stored === undefined ? [] : [["ds-provider", stored]]);
  const writes = [];
  const requests = [];
  const sandbox = {
    document: { getElementById: (id) => els[id], createElement: () => new El("") },
    localStorage: {
      getItem: (k) => store.get(k) ?? null,
      setItem: (k, v) => {
        writes.push([k, v]);
        store.set(k, v);
      },
      removeItem: (k) => void store.delete(k),
    },
    fetch: async (url, opts = {}) => {
      requests.push({ url, method: opts.method || "GET", body: opts.body ? JSON.parse(opts.body) : undefined });
      if (!server) return { ok: false, status: 404, json: async () => { throw new Error("not json"); } };
      // A server may answer with a promise, to hold a reply back.
      const out = await server(url, opts.method || "GET", opts.body ? JSON.parse(opts.body) : undefined);
      if (out === "reject") throw new TypeError("Failed to fetch");
      // { status, html: true } stands for a proxy's error page.
      if (out && out.status) return { ok: false, status: out.status, json: async () => { if (out.html) throw new Error("not json"); return out.body; } };
      return { ok: true, status: 200, json: async () => out };
    },
    JSON,
    Object,
    String,
    Promise,
  };
  vm.runInNewContext(SCRIPT, sandbox);
  for (let i = 0; i < 20; i++) await new Promise((r) => setImmediate(r));
  return { els, store, writes, requests };
}

const legacy = JSON.stringify({ name: "openai", api: "openai", base_url: "https://api.openai.com/v1", api_key: KEY, model: "m1" });

test("with no server it hides the form, deletes an old browser key and stores nothing", async () => {
  const { els, store, writes, requests } = await run(legacy, null);
  assert.equal(els.pf.hidden, true);
  assert.equal(els["pf-off"].hidden, false);
  assert.equal(store.has("ds-provider"), false);
  assert.deepEqual(writes, []);
  assert.match(els["pf-notice"].textContent, /^Deleted an API key/);
  assert.ok(requests.every((r) => r.method === "GET"), "no key is posted anywhere");
});

test("with a server it moves an old browser key to the server once, then deletes it", async () => {
  let saved = false;
  const { els, store, writes, requests } = await run(legacy, (url, method, body) => {
    if (method === "POST" && url.endsWith("api/provider")) {
      saved = true;
      return { ok: true, source: "saved", provider: { api: body.api, base_url: body.base_url, model: body.model } };
    }
    return saved
      ? { ok: true, source: "saved", configured: true, provider: { api: "openai", base_url: "https://api.openai.com/v1", model: "m1", name: "openai" } }
      : { ok: true, source: "none", configured: false, provider: null };
  });
  const posts = requests.filter((r) => r.method === "POST");
  assert.equal(posts.length, 1);
  assert.equal(posts[0].body.api_key, KEY);
  assert.equal(posts[0].body.migrate, true, "a migration never replaces a saved provider");
  assert.equal(store.has("ds-provider"), false);
  assert.deepEqual(writes, []);
  assert.match(els["pf-notice"].textContent, /^Moved the API key/);
  assert.equal(els["pf-badge"].textContent, "Saved on the server");
  assert.equal(els["pf-key"].value, "", "the key field never holds the saved key");
  assert.equal(els["pf-clear"].hidden, false);
});

test("a refused move still deletes the browser copy and never quotes the key", async () => {
  const { els, store } = await run(legacy, (url, method) =>
    method === "POST" ? { ok: false, error: `HTTP 401 for ${KEY}` } : { ok: true, source: "none", provider: null },
  );
  assert.equal(store.has("ds-provider"), false);
  assert.match(els["pf-notice"].textContent, /^Deleted the API key/);
  assert.ok(!els["pf-notice"].textContent.includes(KEY));
});

test("a server that already has a key keeps it, and the page says so", async () => {
  const { els, store } = await run(legacy, (url, method) =>
    method === "POST" ? { ok: false, existing: true, error: "kept" } : { ok: true, source: "saved", provider: { api: "openai", model: "m" } },
  );
  assert.equal(store.has("ds-provider"), false);
  assert.match(els["pf-notice"].textContent, /already has, or had, its own saved key/);
});

test("saving posts the typed key to the server and keeps no copy", async () => {
  const { els, writes, requests } = await run(undefined, (url, method, body) => {
    if (url.endsWith("provider/test")) return { ok: true, models: [{ id: "m1" }] };
    if (method === "POST") return { ok: true, source: "saved", provider: { api: body.api, base_url: body.base_url, model: body.model } };
    return { ok: true, source: "none", provider: null };
  });
  els["pf-key"].value = KEY;
  els["pf-test"].onclick();
  for (let i = 0; i < 10; i++) await new Promise((r) => setImmediate(r));
  els["pf-save"].onclick();
  for (let i = 0; i < 10; i++) await new Promise((r) => setImmediate(r));
  const save = requests.find((r) => r.method === "POST" && r.url.endsWith("api/provider"));
  assert.equal(save.body.api_key, KEY);
  assert.deepEqual(writes, []);
  assert.equal(els["pf-key"].value, "", "the key field empties once the server has it");
  assert.match(els["pf-status"].textContent, /^Saved on the server/);
});

test("a save reply that lands after the form changed leaves the newer edits alone", async () => {
  const NEWER = "sk-typed-after-saving-7654321";
  let release;
  const held = new Promise((r) => (release = r));
  const { els } = await run(undefined, (url, method, body) => {
    if (url.endsWith("provider/test")) return { ok: true, models: [{ id: "m1" }] };
    if (method === "POST") return held.then(() => ({ ok: true, source: "saved", provider: { api: body.api, base_url: body.base_url, model: body.model } }));
    return { ok: true, source: "none", provider: null };
  });
  els["pf-key"].value = KEY;
  els["pf-test"].onclick();
  for (let i = 0; i < 10; i++) await new Promise((r) => setImmediate(r));
  els["pf-save"].onclick();
  for (let i = 0; i < 5; i++) await new Promise((r) => setImmediate(r));
  // Remove waits for the save, so a Remove cannot be undone by it.
  assert.deepEqual([els["pf-save"].disabled, els["pf-clear"].disabled], [true, true]);
  // The reader types another key while the save is in flight.
  els["pf-key"].value = NEWER;
  release();
  for (let i = 0; i < 10; i++) await new Promise((r) => setImmediate(r));
  assert.equal(els["pf-key"].value, NEWER, "the newer key is not erased");
  assert.deepEqual([els["pf-save"].disabled, els["pf-clear"].disabled], [false, false]);
  assert.equal(els["pf-badge"].textContent, "Saved on the server");
  assert.match(els["pf-status"].textContent, /The form has changed since/);
  assert.ok(!els["pf-status"].textContent.includes(NEWER) && !els["pf-status"].textContent.includes(KEY));
});

test("the form stays hidden until a slow migration and the read after it have filled it", async () => {
  let release;
  const held = new Promise((r) => (release = r));
  const { els } = await run(legacy, (url, method, body) => {
    if (method === "POST") return held.then(() => ({ ok: true, source: "saved", provider: { api: body.api, base_url: body.base_url, model: body.model } }));
    return { ok: true, source: "none", configured: false, provider: null };
  });
  assert.equal(els.pf.hidden, true, "nothing to type into while the move is in flight");
  release();
  for (let i = 0; i < 20; i++) await new Promise((r) => setImmediate(r));
  assert.equal(els.pf.hidden, false, "shown once filled");
  assert.equal(els["pf-badge"].textContent, "No key");
});

test("a server that does not answer keeps the old browser key and never posts it", async () => {
  for (const down of [() => ({ status: 502, html: true }), () => "reject", () => ({ status: 503, html: true })]) {
    const { els, store, requests } = await run(legacy, down);
    assert.equal(store.get("ds-provider"), legacy, "the only copy stays");
    assert.ok(requests.every((r) => r.method === "GET"));
    assert.match(els["pf-notice"].textContent, /stays here for now/);
  }
});

test("a save that fails with 5xx or a non-JSON page keeps the old browser key", async () => {
  for (const fail of [{ status: 502, html: true }, { status: 500, body: { ok: false, error: "busy" } }, "reject"]) {
    const { els, store } = await run(legacy, (url, method) =>
      method === "POST" ? fail : { ok: true, source: "none", configured: false, provider: null },
    );
    assert.equal(store.get("ds-provider"), legacy);
    assert.match(els["pf-notice"].textContent, /stays here for now/);
    assert.ok(!els["pf-notice"].textContent.includes(KEY));
  }
});

test("a refused body (4xx JSON) is a decision: the browser key is deleted", async () => {
  const { els, store } = await run(legacy, (url, method) =>
    method === "POST" ? { status: 400, body: { ok: false, error: "That API key has characters a key cannot hold." } } : { ok: true, source: "none", provider: null },
  );
  assert.equal(store.has("ds-provider"), false);
  assert.match(els["pf-notice"].textContent, /^Deleted the API key/);
});
