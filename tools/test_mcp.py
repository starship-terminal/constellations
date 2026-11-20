"""Tests for server/mcp.py's JSON-RPC handling: malformed messages get a
JSON-RPC error and never end the stdio session. Run with `make test`."""
import contextlib
import importlib.util
import io
import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

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


class DispatchTest(unittest.TestCase):
    def _call(self, name, args=None):
        out = mcp.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                          "params": {"name": name, "arguments": args or {}}})
        return out["result"]

    def test_unknown_method_and_tool(self):
        out = mcp.handle({"jsonrpc": "2.0", "id": 1, "method": "resources/list"})
        self.assertEqual(out["error"], {"code": -32601, "message": "no method 'resources/list'"})
        out = mcp.handle({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "rm_rf"}})
        self.assertEqual(out["error"], {"code": -32602, "message": "unknown tool 'rm_rf'"})

    def test_initialize_echoes_a_string_protocol_version_only(self):
        init = lambda v: mcp.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize",
                                     "params": {"protocolVersion": v}})["result"]
        self.assertEqual(init("2025-06-18")["protocolVersion"], "2025-06-18")
        self.assertEqual(init(5)["protocolVersion"], "2025-03-26")
        self.assertEqual(init(None)["serverInfo"], mcp.SERVER_INFO)

    def test_tool_os_error_never_reaches_the_client(self):
        # An OSError names an absolute path; the caller learns only the tool and the type.
        spec = mcp.library._BY_NAME["get_style"]
        boom = FileNotFoundError(2, "No such file or directory", "/srv/private/checkout/catalog.json")
        log = io.StringIO()
        with mock.patch.dict(spec, {"fn": mock.Mock(side_effect=boom)}), \
                contextlib.redirect_stderr(log):
            out = self._call("get_style", {"slug": "linear"})
        self.assertTrue(out["isError"])
        self.assertEqual(out["content"], [{"type": "text", "text": "get_style failed (FileNotFoundError)"}])
        self.assertIn("/srv/private/checkout", log.getvalue())

    def test_bad_argument_message_is_kept(self):
        spec = mcp.library._BY_NAME["get_style"]
        with mock.patch.dict(spec, {"fn": mock.Mock(side_effect=ValueError("invalid literal for int(): 'x'"))}):
            out = self._call("get_style", {"slug": "linear"})
        self.assertEqual(out["content"][0]["text"], "get_style failed: invalid literal for int(): 'x'")

    def test_non_tool_error_is_generic(self):
        log = io.StringIO()
        with mock.patch.object(mcp.library, "call", side_effect=RuntimeError("/srv/private/x")), \
                contextlib.redirect_stderr(log):
            out = self._call("get_style", {"slug": "linear"})
        self.assertEqual(out, {"content": [{"type": "text", "text": "get_style failed"}], "isError": True})
        self.assertIn("/srv/private/x", log.getvalue())

    def test_view_media_becomes_an_image_block(self):
        img = {"url": "/media/systems/x/a.png", "name": "a.png", "data": "QUJD", "media_type": "image/png"}
        with mock.patch.object(mcp.library, "call", return_value={"_image": img}):
            out = self._call("view_media", {"path": "systems/x/a.png"})
        self.assertEqual(out["content"][1], {"type": "image", "data": "QUJD", "mimeType": "image/png"})
        self.assertEqual(json.loads(out["content"][0]["text"]), {"url": img["url"], "name": "a.png"})

    def test_real_tool_refuses_a_path_like_slug_without_leaking_the_checkout(self):
        root = str(SERVER.parent)
        for args in ({"slug": "../../etc/passwd"}, {"slug": "/etc/passwd"}, {"slug": "x" * 50_000}):
            out = self._call("get_style", args)
            self.assertTrue(out["isError"], args)
            self.assertNotIn(root, out["content"][0]["text"])
            self.assertLessEqual(len(out["content"][0]["text"]), 400)


class BatchTest(unittest.TestCase):
    PING = {"jsonrpc": "2.0", "id": 1, "method": "ping"}
    NOTE = {"jsonrpc": "2.0", "method": "notifications/initialized"}

    def test_empty_batch_is_one_invalid_request(self):
        out = mcp.handle_batch([])
        self.assertEqual(out["id"], None)
        self.assertEqual(out["error"]["code"], -32600)

    def test_each_non_object_member_gets_its_own_error(self):
        out = mcp.handle_batch([1, "x", self.PING])
        self.assertEqual([r.get("error", {}).get("code") for r in out], [-32600, -32600, None])
        self.assertEqual(out[2]["id"], 1)

    def test_only_notifications_get_nothing(self):
        self.assertIsNone(mcp.handle_batch([self.NOTE, self.NOTE]))
        self.assertIsNone(mcp.handle_batch(self.NOTE))

    def test_single_message_and_scalar(self):
        self.assertEqual(mcp.handle_batch(self.PING), {"jsonrpc": "2.0", "id": 1, "result": {}})
        self.assertEqual(mcp.handle_batch(5)["error"]["code"], -32600)


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
