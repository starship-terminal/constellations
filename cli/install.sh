#!/bin/sh
# install.sh — install `ds`, the design-systems CLI, from this server.
#
#   curl -fsSL @DS_BASE@/api/install.sh | sh
#
# Downloads the client from @DS_BASE@/api/ds into ~/.local/bin (DS_BIN
# overrides), writes the server URL to ~/.config/design-systems/url, and
# prints the MCP endpoint to hand to agents.
set -eu

BASE="@DS_BASE@"
BIN="${DS_BIN:-$HOME/.local/bin}"
CFG="$HOME/.config/design-systems"

mkdir -p "$BIN" "$CFG"
curl -fsSL "$BASE/api/ds" -o "$BIN/ds.new" && mv "$BIN/ds.new" "$BIN/ds"
chmod +x "$BIN/ds"
printf '%s\n' "$BASE" > "$CFG/url"

echo "ds -> $BIN/ds"
case ":$PATH:" in
    *":$BIN:"*) ;;
    *) echo "note: $BIN is not on your PATH — add it, or run $BIN/ds directly" ;;
esac
"$BIN/ds" status || true

cat <<EOF

For agents, the MCP endpoint is:

    $BASE/api/mcp

    claude mcp add --transport http design-systems $BASE/api/mcp
    swe mcp add design-systems --url=$BASE/api/mcp
    codex (~/.codex/config.toml):
        [mcp_servers.design-systems]
        url = "$BASE/api/mcp"
    opencode/cursor: remote MCP, url $BASE/api/mcp
EOF
