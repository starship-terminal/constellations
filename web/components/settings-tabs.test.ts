// Unit tests for the Settings tab rules. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { TABS, tabForKey, tabFromHash } from "./settings-tabs.ts";

describe("tabFromHash", () => {
  it("opens the tab a deep link names, including the older section hashes", () => {
    assert.equal(tabFromHash("#model-provider"), "model-provider");
    assert.equal(tabFromHash("#preferences"), "appearance");
    assert.equal(tabFromHash("#appearance"), "appearance");
    assert.equal(tabFromHash("#for-agents"), "agents");
    assert.equal(tabFromHash("data"), "data");
  });

  it("ignores an empty, unknown or malformed hash", () => {
    for (const h of ["", "#", "#nope", "#%E0%A4%A"]) assert.equal(tabFromHash(h), null, h);
  });
});

describe("tabForKey", () => {
  it("moves with both arrow pairs and wraps", () => {
    assert.equal(tabForKey("model-provider", "ArrowDown"), "appearance");
    assert.equal(tabForKey("model-provider", "ArrowRight"), "appearance");
    assert.equal(tabForKey("model-provider", "ArrowUp"), "data");
    assert.equal(tabForKey("data", "ArrowDown"), "model-provider");
    assert.equal(tabForKey("appearance", "ArrowLeft"), "model-provider");
  });

  it("jumps with Home and End and ignores other keys", () => {
    assert.equal(tabForKey("agents", "Home"), TABS[0].id);
    assert.equal(tabForKey("agents", "End"), TABS[TABS.length - 1].id);
    assert.equal(tabForKey("agents", "Enter"), null);
    assert.equal(tabForKey("agents", "a"), null);
  });

  it("gives every tab a distinct id and label, none in capitals", () => {
    assert.equal(new Set(TABS.map((t) => t.id)).size, TABS.length);
    for (const t of TABS) assert.notEqual(t.label, t.label.toUpperCase());
  });
});
