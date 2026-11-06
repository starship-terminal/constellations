"""Tests for server/mcp.py's JSON-RPC handling: malformed messages get a
JSON-RPC error and never end the stdio session. Run with `make test`."""
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

SERVER = Path(__file__).resolve().parent.parent / "server"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, SERVER / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mcp = _load("agent_mcp_test", "mcp.py")


class MalformedRequestTest(unittest.TestCase):
    def _code(self, req):
        out = mcp.handle(req)
        self.assertIsNotNone(out)
        self.assertIn("error", out, out)
        return out["error"]["code"]

    def test_null_params(self):
        out = mcp.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": None})
        self.assertEqual(out["result"]["protocolVersion"], "2025-03-26")
        self.assertEqual(self._code({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": None}),
                         -32602)

    def test_non_object_params_and_arguments(self):
        self.assertEqual(self._code({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": [1]}),
                         -32602)
        self.assertEqual(self._code({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                                     "params": {"name": "get_style", "arguments": ["linear"]}}), -32602)
        self.assertEqual(self._code({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                                     "params": {"name": 5}}), -32602)

    def test_non_string_method_and_non_object_request(self):
        self.assertEqual(self._code({"jsonrpc": "2.0", "id": 1, "method": 5}), -32600)
        self.assertEqual(self._code({"jsonrpc": "2.0", "id": 1}), -32600)
        # No id and no valid method: an invalid request, not a notification.
        self.assertEqual(mcp.handle({"jsonrpc": "2.0", "method": 5}),
                         {"jsonrpc": "2.0", "id": None,
                          "error": {"code": -32600, "message": "method must be a string"}})
        self.assertEqual(self._code(5), -32600)
        self.assertEqual(self._code(None), -32600)

    def test_handler_bug_is_internal_error(self):
        original = mcp._tool_specs
        mcp._tool_specs = lambda: 1 / 0
        try:
            out = mcp.handle({"jsonrpc": "2.0", "id": 7, "method": "tools/list"})
        finally:
            mcp._tool_specs = original
        self.assertEqual(out, {"jsonrpc": "2.0", "id": 7,
                               "error": {"code": -32603, "message": "internal error"}})


class StdioTest(unittest.TestCase):
    def test_session_survives_bad_lines(self):
        lines = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": None},
            {"jsonrpc": "2.0", "id": 2, "method": 5},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": ["x"]},
            "not json",
            5,
            [],
            [{"jsonrpc": "2.0", "id": 4, "method": "ping"},
             {"jsonrpc": "2.0", "method": "notifications/initialized"}],
            {"jsonrpc": "2.0", "id": 5, "method": "ping"},
        ]
        stdin = "\n".join(l if isinstance(l, str) else json.dumps(l) for l in lines) + "\n"
        proc = subprocess.run([sys.executable, str(SERVER / "mcp.py")], input=stdin,
                              capture_output=True, text=True, timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        replies = [json.loads(l) for l in proc.stdout.splitlines()]
        self.assertEqual(len(replies), 8, proc.stdout)
        self.assertEqual(replies[0]["id"], 1)
        self.assertIn("result", replies[0])
        self.assertEqual([r["error"]["code"] for r in replies[1:6]],
                         [-32600, -32602, -32700, -32600, -32600])
        self.assertEqual(replies[6], [{"jsonrpc": "2.0", "id": 4, "result": {}}])
        self.assertEqual(replies[7], {"jsonrpc": "2.0", "id": 5, "result": {}})


if __name__ == "__main__":
    unittest.main()
