// Unit tests for the copy button's state logic. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { COPY_RESET_MS, copyLabel, copyOutcome } from "./copy-state.ts";

describe("copyOutcome", () => {
  it("hands the exact text to the copier and reports copied", async () => {
    const seen: string[] = [];
    const r = await copyOutcome("claude mcp add x", async (t) => void seen.push(t));
    assert.equal(r, "copied");
    assert.deepEqual(seen, ["claude mcp add x"]);
  });

  it("reports failed when the copier rejects", async () => {
    assert.equal(await copyOutcome("x", () => Promise.reject(new Error("blocked"))), "failed");
  });
});

describe("copyLabel", () => {
  it("labels each state", () => {
    assert.equal(copyLabel("idle"), "Copy");
    assert.equal(copyLabel("copied"), "Copied");
    assert.equal(copyLabel("failed"), "Copy failed");
  });

  it("reverts after 1800 ms", () => {
    assert.equal(COPY_RESET_MS, 1800);
  });
});
