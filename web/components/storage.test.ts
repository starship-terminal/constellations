// Unit tests for the browser-storage readers. Run with `pnpm test`.
import assert from "node:assert/strict";
import { afterEach, describe, it } from "node:test";
import { readSavedPaths, readStoredProvider } from "./storage.ts";

const store = new Map<string, string>();
Object.defineProperty(globalThis, "localStorage", {
  configurable: true,
  value: { getItem: (k: string) => store.get(k) ?? null, setItem: (k: string, v: string) => void store.set(k, v) },
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
