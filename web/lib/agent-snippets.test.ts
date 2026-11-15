// Unit tests for the agent setup snippets. Run with `pnpm test`.
import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { agentSnippets, ORIGIN_PLACEHOLDER } from "./agent-snippets.ts";

describe("agentSnippets", () => {
  it("builds every snippet from the origin", () => {
    const list = agentSnippets("http://127.0.0.1:8800");
    assert.deepEqual(
      list.map((s) => s.label),
      ["CLI", "MCP URL", "Claude", "swe", "Codex", "OpenCode"],
    );
    assert.equal(list[1].text, "http://127.0.0.1:8800/api/mcp");
    assert.equal(list[2].text, "claude mcp add --transport http design-systems http://127.0.0.1:8800/api/mcp");
    assert.equal(list[4].text, '[mcp_servers.design-systems] url = "http://127.0.0.1:8800/api/mcp"');
    assert.ok(list.every((s) => s.text.includes("http://127.0.0.1:8800")));
  });

  it("uses the placeholder until the origin is known", () => {
    const list = agentSnippets("");
    assert.ok(list.every((s) => s.text.includes(ORIGIN_PLACEHOLDER)));
    assert.ok(list.every((s) => !s.text.includes("undefined")));
  });
});
