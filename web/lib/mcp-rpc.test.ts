// Unit tests for POST /api/mcp's JSON-RPC handling (lib/mcp-rpc.ts), the
// cases tools/test_mcp.py runs against server/mcp.py. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it, mock } from "node:test";
import { SPECS, ToolError } from "./chat/library.ts";
import { ROOT } from "./repo.ts";
import { handle, SERVER_INFO } from "./mcp-rpc.ts";

const rpc = (method: unknown, params?: unknown, id: unknown = 1) => handle({ jsonrpc: "2.0", id, method, params });
const err = async (p: Promise<unknown>) => (await p as { error: { code: number; message: string } }).error;

/** Run tools/call get_style with its implementation swapped for `fn`. */
async function callWith(fn: () => Promise<Record<string, unknown>>) {
  const spec = SPECS.find((s) => s.name === "get_style")!;
  const original = spec.fn;
  spec.fn = fn;
  const log = mock.method(console, "error", () => {});
  try {
    const out = (await rpc("tools/call", { name: "get_style", arguments: { slug: "linear" } })) as { result: Record<string, unknown> };
    return out.result;
  } finally {
    spec.fn = original;
    log.mock.restore();
  }
}

describe("mcp dispatch", () => {
  it("initialize echoes a string protocolVersion only", async () => {
    const init = async (v: unknown) => ((await rpc("initialize", { protocolVersion: v })) as { result: Record<string, unknown> }).result;
    assert.equal((await init("2025-06-18")).protocolVersion, "2025-06-18");
    assert.equal((await init(5)).protocolVersion, "2025-03-26");
    assert.deepEqual((await init(null)).serverInfo, SERVER_INFO);
  });

  it("answers ping and lists every tool with its schema", async () => {
    assert.deepEqual(await rpc("ping"), { jsonrpc: "2.0", id: 1, result: {} });
    const list = ((await rpc("tools/list")) as { result: { tools: { name: string; inputSchema: unknown }[] } }).result.tools;
    assert.deepEqual(list.map((t) => t.name), SPECS.map((s) => s.name));
    assert.ok(list.every((t) => t.inputSchema));
  });

  it("refuses malformed messages with the JSON-RPC codes", async () => {
    assert.deepEqual(await err(rpc(5)), { code: -32600, message: "method must be a string" });
    assert.deepEqual(await err(rpc("initialize", [1])), { code: -32602, message: "params must be an object" });
    assert.deepEqual(await err(rpc("tools/call", { name: "rm_rf" })), { code: -32602, message: "unknown tool 'rm_rf'" });
    assert.deepEqual(await err(rpc("tools/call", { name: 5 })), { code: -32602, message: "unknown tool ''" });
    assert.deepEqual(await err(rpc("tools/call", { name: "get_style", arguments: ["linear"] })), {
      code: -32602,
      message: "arguments must be an object",
    });
    assert.deepEqual(await err(rpc("resources/list")), { code: -32601, message: "no method 'resources/list'" });
  });

  it("answers no notification, but does answer a method-less message", async () => {
    assert.equal(await handle({ jsonrpc: "2.0", method: "notifications/initialized" }), null);
    assert.equal(await handle({ jsonrpc: "2.0", method: "ping" }), null);
    assert.deepEqual(await handle({ jsonrpc: "2.0", method: 5 }), {
      jsonrpc: "2.0",
      id: null,
      error: { code: -32600, message: "method must be a string" },
    });
  });

  it("reports a tool's ToolError text as the tool result", async () => {
    assert.deepEqual(await callWith(async () => { throw new ToolError("no systems package 'x'"); }), {
      content: [{ type: "text", text: "no systems package 'x'" }],
      isError: true,
    });
  });

  it("turns view_media's image into an MCP image block", async () => {
    const out = await callWith(async () => ({ _image: { url: "/media/a.png", name: "a.png", data: "QUJD", media_type: "image/png" } }));
    assert.deepEqual(out.content, [
      { type: "text", text: JSON.stringify({ url: "/media/a.png", name: "a.png" }) },
      { type: "image", data: "QUJD", mimeType: "image/png" },
    ]);
  });

  it("keeps a real tool's path-like slug refusal free of the checkout path", async () => {
    for (const slug of ["../../etc/passwd", "/etc/passwd", "x".repeat(50_000)]) {
      const out = ((await rpc("tools/call", { name: "get_style", arguments: { slug } })) as { result: { isError?: boolean; content: { text: string }[] } }).result;
      assert.equal(out.isError, true, slug.slice(0, 20));
      // ROOT is the checkout the tools resolve files against (web/'s parent).
      assert.ok(!out.content[0].text.includes(ROOT), slug.slice(0, 20));
      assert.ok(out.content[0].text.length <= 400);
    }
  });
});
