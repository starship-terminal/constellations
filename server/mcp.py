"""The design-systems MCP server: the gallery chat's tool layer over stdio
JSON-RPC, so a coding agent (Devin, Claude, Cursor) becomes another chat UI for
the library. Point a client at it with, for example:

    python3 server/mcp.py

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


def _send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def _result(req: dict, result) -> None:
    if "id" in req:
        _send({"jsonrpc": "2.0", "id": req["id"], "result": result})


def _error(req: dict, code: int, message: str) -> None:
    if "id" in req:
        _send({"jsonrpc": "2.0", "id": req["id"], "error": {"code": code, "message": message}})


def _tool_specs() -> list[dict]:
    return [{"name": s["name"], "description": s["description"], "inputSchema": s["parameters"]}
            for s in library.SPECS]


def _call(name: str, args: dict) -> dict:
    try:
        result = library.call(name, args or {})
    except Exception as e:
        # One malformed call must never end the session: report it as a tool
        # error and keep the input loop alive.
        return {"content": [{"type": "text", "text": str(e)[:400]}], "isError": True}
    if "_image" in result:
        img = result["_image"]
        return {"content": [{"type": "text", "text": json.dumps({"url": img["url"], "name": img["name"]})},
                            {"type": "image", "data": img["data"], "mimeType": img["media_type"]}]}
    return {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False)}]}


def handle(req: dict) -> None:
    method = req.get("method", "")
    if method == "initialize":
        _result(req, {"protocolVersion": req.get("params", {}).get("protocolVersion", "2025-03-26"),
                      "capabilities": {"tools": {"listChanged": False}},
                      "serverInfo": SERVER_INFO,
                      "instructions": "Read-only search over the design-systems library: "
                                      "measured systems/ packages first, refero for breadth."})
    elif method == "ping":
        _result(req, {})
    elif method == "tools/list":
        _result(req, {"tools": _tool_specs()})
    elif method == "tools/call":
        params = req.get("params") or {}
        name = params.get("name", "")
        if name not in {s["name"] for s in library.SPECS}:
            _error(req, -32602, f"unknown tool '{name}'")
        else:
            _result(req, _call(name, params.get("arguments")))
    elif not method.startswith("notifications/"):
        _error(req, -32601, f"no method '{method}'")


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
            handle(req)


if __name__ == "__main__":
    main()
