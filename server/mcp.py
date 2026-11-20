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


def _send(obj) -> None:
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
    except library.ToolError as e:
        # One malformed call must never end the session: report it as a tool
        # error and keep the caller's loop alive. A ToolError's text is written
        # for the caller (library.call strips server detail from it).
        return {"content": [{"type": "text", "text": str(e)[:400]}], "isError": True}
    except Exception as e:  # noqa: BLE001 - the session must outlive any bug
        # Not a ToolError: a bug. The detail goes to stderr, never the client.
        print(f"mcp: {name}: {type(e).__name__}: {e}", file=sys.stderr)
        return {"content": [{"type": "text", "text": f"{name} failed"}], "isError": True}
    if "_image" in result:
        img = result["_image"]
        return {"content": [{"type": "text", "text": json.dumps({"url": img["url"], "name": img["name"]})},
                            {"type": "image", "data": img["data"], "mimeType": img["media_type"]}]}
    return {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False)}]}


def handle(req) -> dict | None:
    """The JSON-RPC reply for one request, or None when it is a notification
    (or a reply with no id to answer). The stdio main() prints the return;
    routes.py's /api/mcp serialises it as the HTTP body. A malformed message
    (not an object, a non-string method, params that are not an object) gets
    a JSON-RPC error instead of an exception, and anything unexpected inside
    a handler is -32603, so one bad line can never end a stdio session."""
    if not isinstance(req, dict):
        return {"jsonrpc": "2.0", "id": None,
                "error": {"code": -32600, "message": "a JSON-RPC request must be an object"}}
    try:
        return _dispatch(req)
    except Exception as e:  # noqa: BLE001 - the session must outlive any bug
        # The detail goes to stderr (stdout is the protocol stream), never to
        # the client.
        print(f"mcp: {type(e).__name__}: {e}", file=sys.stderr)
        return _error(req, -32603, "internal error")


def handle_batch(raw) -> dict | list | None:
    """The reply body for one parsed JSON-RPC payload, shared by the stdio loop
    and POST /api/mcp (web/lib/mcp-batch.ts mirrors it). None means nothing to
    send back: a lone notification, or a batch of only notifications (HTTP 202).
    An object gets one reply. A batch gets an array with one reply per member
    that has one, a non-object member counting as its own Invalid Request. An
    empty batch is a single Invalid Request, per JSON-RPC 2.0 section 6."""
    if isinstance(raw, list):
        if not raw:
            return {"jsonrpc": "2.0", "id": None,
                    "error": {"code": -32600, "message": "an empty batch is not a valid request"}}
        return [r for r in (handle(m) for m in raw) if r is not None] or None
    return handle(raw)


def _dispatch(req: dict) -> dict | None:
    method = req.get("method")
    if not isinstance(method, str):
        # Without a method it is not a notification either, so it is answered
        # even when it carries no id.
        return {"jsonrpc": "2.0", "id": req.get("id"),
                "error": {"code": -32600, "message": "method must be a string"}}
    params = req.get("params")
    if params is None:
        params = {}
    if not isinstance(params, dict):
        return _error(req, -32602, "params must be an object")
    if method == "initialize":
        version = params.get("protocolVersion")
        return _result(req, {"protocolVersion": version if isinstance(version, str) else "2025-03-26",
                             "capabilities": {"tools": {"listChanged": False}},
                             "serverInfo": SERVER_INFO,
                             "instructions": INSTRUCTIONS})
    if method == "ping":
        return _result(req, {})
    if method == "tools/list":
        return _result(req, {"tools": _tool_specs()})
    if method == "tools/call":
        name = params.get("name")
        if not isinstance(name, str) or name not in {s["name"] for s in library.SPECS}:
            return _error(req, -32602, f"unknown tool '{name if isinstance(name, str) else ''}'")
        args = params.get("arguments")
        if args is not None and not isinstance(args, dict):
            return _error(req, -32602, "arguments must be an object")
        return _result(req, _call(name, args))
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
        out = handle_batch(req)
        if out is not None:
            _send(out)


if __name__ == "__main__":
    main()
