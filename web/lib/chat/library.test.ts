// Unit tests for call()'s error contract: a tool's own ToolError text reaches
// the caller; any other failure reaches it only as its type, because the
// caller may be an MCP client or, through the chat, a third-party model.
// Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it, mock } from "node:test";
import { call, SPECS, ToolError } from "./library.ts";

const spec = SPECS.find((s) => s.name === "get_style")!;

async function failure(err: unknown): Promise<string> {
  const original = spec.fn;
  spec.fn = async () => {
    throw err;
  };
  const log = mock.method(console, "error", () => {});
  try {
    await call("get_style", { slug: "linear" });
    return "no error";
  } catch (e) {
    assert.ok(e instanceof ToolError);
    return e.message;
  } finally {
    spec.fn = original;
    log.mock.restore();
  }
}

describe("call errors", () => {
  it("passes a ToolError's own text through", async () => {
    assert.equal(await failure(new ToolError("no systems package 'x'")), "no systems package 'x'");
  });

  it("reports a filesystem error by type only", async () => {
    const e = Object.assign(new Error("ENOENT: no such file or directory, open '/srv/private/checkout/catalog.json'"), { code: "ENOENT" });
    assert.equal(await failure(e), "get_style failed (Error)");
  });

  it("reports a server-file JSON.parse error by type only", async () => {
    let parseError: unknown;
    try {
      JSON.parse('{"secret": internal-value}');
    } catch (e) {
      parseError = e;
    }
    assert.equal(await failure(parseError), "get_style failed (SyntaxError)");
  });

  it("names the tool for an unknown one and a missing argument", async () => {
    await assert.rejects(call("rm_rf", {}), /unknown tool 'rm_rf'/);
    await assert.rejects(call("get_style", {}), /get_style needs slug/);
  });
});
