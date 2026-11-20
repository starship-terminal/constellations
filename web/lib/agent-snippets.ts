// The "For agents" setup snippets on the Settings page. One list feeds both
// the text shown and the text the copy buttons put on the clipboard, so the
// two cannot drift apart.

export const ORIGIN_PLACEHOLDER = "https://<this-site>";

export type AgentSnippet = { label: string; text: string };

/** Setup snippets for `origin`; falls back to a placeholder before it is known. */
export function agentSnippets(origin: string): AgentSnippet[] {
  const base = origin || ORIGIN_PLACEHOLDER;
  return [
    { label: "CLI", text: `curl -fsSL ${base}/api/install.sh | sh` },
    { label: "MCP URL", text: `${base}/api/mcp` },
    { label: "Claude", text: `claude mcp add --transport http design-systems ${base}/api/mcp` },
    { label: "swe", text: `swe mcp add design-systems --url=${base}/api/mcp` },
    // A TOML table header and its key must sit on separate lines.
    { label: "Codex", text: `[mcp_servers.design-systems]\nurl = "${base}/api/mcp"` },
    { label: "OpenCode", text: `"design-systems": { "type": "remote", "url": "${base}/api/mcp" }` },
  ];
}
