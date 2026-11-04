"""The design-systems MCP server: the gallery chat's tool layer over JSON-RPC,
so a coding agent (Devin, Claude, Cursor) becomes another chat UI for the
library. Two transports, one handler:

    python3 server/mcp.py           # stdio, for a client that spawns a process
    POST /api/mcp                   # streamable HTTP, served by routes.py

Hand-rolled against the 2025-03-26 MCP shape: initialize, tools/list,
tools/call and ping. Notifications get no reply. Every call is read-only;
view_media returns an MCP image block.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "agent_library", Path(__file__).resolve().parent / "library.py")
library = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(library)

SERVER_INFO = {"name": "design-systems", "version": "1.0.0"}
INSTRUCTIONS = ("Read-only search over the design-systems library: "
                "measured systems/ packages first, refero for breadth. Media url "
                "fields are site-relative; prefix them with the server origin.")


def _send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def _result(req: dict, result) -> dict | None:
    if "id" not in req:
        return None
    return {"jsonrpc": "2.0", "id": req["id"], "result": result}


def _error(req: dict, code: int, message: str) -> dict | None:
    if "id" not in req:
        return None
    return {"jsonrpc": "2.0", "id": req["id"],
            "error": {"code": code, "message": message}}


def _tool_specs() -> list[dict]:
    return [{"name": s["name"], "description": s["description"], "inputSchema": s["parameters"]}
            for s in library.SPECS]


def _call(name: str, args: dict) -> dict:
    try:
        result = library.call(name, args or {})
    except Exception as e:
        # One malformed call must never end the session: report it as a tool
        # error and keep the caller's loop alive.
        return {"content": [{"type": "text", "text": str(e)[:400]}], "isError": True}
    if "_image" in result:
        img = result["_image"]
        return {"content": [{"type": "text", "text": json.dumps({"url": img["url"], "name": img["name"]})},
                            {"type": "image", "data": img["data"], "mimeType": img["media_type"]}]}
    return {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False)}]}


def handle(req: dict) -> dict | None:
    """The JSON-RPC reply for one request, or None when it is a notification
    (or a reply with no id to answer). The stdio main() prints the return;
    routes.py's /api/mcp serialises it as the HTTP body."""
    method = req.get("method", "")
    if method == "initialize":
        return _result(req, {"protocolVersion": req.get("params", {}).get("protocolVersion", "2025-03-26"),
                             "capabilities": {"tools": {"listChanged": False}},
                             "serverInfo": SERVER_INFO,
                             "instructions": INSTRUCTIONS})
    if method == "ping":
        return _result(req, {})
    if method == "tools/list":
        return _result(req, {"tools": _tool_specs()})
    if method == "tools/call":
        params = req.get("params") or {}
        name = params.get("name", "")
        if name not in {s["name"] for s in library.SPECS}:
            return _error(req, -32602, f"unknown tool '{name}'")
        return _result(req, _call(name, params.get("arguments")))
    if method.startswith("notifications/"):
        return None
    return _error(req, -32601, f"no method '{method}'")


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except ValueError:
            _send({"jsonrpc": "2.0", "id": None,
                   "error": {"code": -32700, "message": "unparseable JSON"}})
            continue
        if isinstance(req, dict):
            out = handle(req)
            if out is not None:
                _send(out)


if __name__ == "__main__":
    main()
