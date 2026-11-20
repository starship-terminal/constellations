// Unit tests for the copy button's state logic. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { COPY_RESET_MS, copyLabel, copyOutcome, flash, type CopyState } from "./copy-state.ts";

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
});

describe("flash", () => {
  it("shows the outcome, then reverts to idle after COPY_RESET_MS", (t) => {
    t.mock.timers.enable({ apis: ["setTimeout"] });
    const seen: CopyState[] = [];
    flash((s) => seen.push(s), "copied");
    t.mock.timers.tick(COPY_RESET_MS - 1);
    assert.deepEqual(seen, ["copied"]);
    t.mock.timers.tick(1);
    assert.deepEqual(seen, ["copied", "idle"]);
  });

  it("restarts the countdown on a second click instead of reverting early", (t) => {
    t.mock.timers.enable({ apis: ["setTimeout"] });
    const seen: CopyState[] = [];
    const show = (s: CopyState) => seen.push(s);
    const first = flash(show, "copied");
    t.mock.timers.tick(COPY_RESET_MS - 100);
    flash(show, "failed", first);
    t.mock.timers.tick(COPY_RESET_MS - 1);
    assert.deepEqual(seen, ["copied", "failed"]);
    t.mock.timers.tick(1);
    assert.deepEqual(seen, ["copied", "failed", "idle"]);
  });
});
