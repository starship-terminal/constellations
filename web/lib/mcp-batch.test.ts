// Unit tests for the POST /api/mcp batch rules. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { handleBatch, MCP_BODY_LIMIT, tooLarge } from "./mcp-batch.ts";

const ping = { jsonrpc: "2.0", id: 1, method: "ping" };
const note = { jsonrpc: "2.0", method: "notifications/initialized" };
// A stand-in for the route's handle(): notifications get nothing.
const handle = async (m: Record<string, unknown>) =>
  m.id === undefined ? null : { jsonrpc: "2.0", id: m.id, result: {} };
const code = (r: unknown) => (r as { error?: { code: number } }).error?.code;

describe("handleBatch", () => {
  it("answers an empty batch with one Invalid Request", async () => {
    const out = await handleBatch([], handle);
    assert.equal(Array.isArray(out), false);
    assert.equal(code(out), -32600);
    assert.equal((out as { id: unknown }).id, null);
  });

  it("gives each non-object member its own Invalid Request", async () => {
    const out = (await handleBatch([1, "x", null, [], ping], handle)) as unknown[];
    assert.deepEqual(out.map(code), [-32600, -32600, -32600, -32600, undefined]);
  });

  it("sends nothing for notifications only", async () => {
    assert.equal(await handleBatch([note, note], handle), null);
    assert.equal(await handleBatch(note, handle), null);
  });

  it("returns a bare reply for an object and an array for a batch", async () => {
    assert.deepEqual(await handleBatch(ping, handle), { jsonrpc: "2.0", id: 1, result: {} });
    assert.deepEqual(await handleBatch([ping], handle), [{ jsonrpc: "2.0", id: 1, result: {} }]);
  });

  it("treats a scalar payload as one Invalid Request", async () => {
    assert.equal(code(await handleBatch(5, handle)), -32600);
  });
});

describe("tooLarge", () => {
  it("is a JSON-RPC Invalid Request naming the limit", () => {
    const r = tooLarge() as { error: { code: number; message: string } };
    assert.equal(r.error.code, -32600);
    assert.match(r.error.message, new RegExp(String(MCP_BODY_LIMIT)));
  });
});
