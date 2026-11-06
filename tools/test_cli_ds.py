"""Tests for cli/ds, the terminal client for /api/mcp. Most run it against a stub
JSON-RPC server on 127.0.0.1 that answers canned tool results; one runs it
against server/api.py itself. Run with `make test`."""
import contextlib
import http.server
import importlib.machinery
import importlib.util
import io
import json
import os
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent


def _load(name, path):
    loader = importlib.machinery.SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


ds = _load("ds_cli", ROOT / "cli" / "ds")


def _text(obj):
    """A tools/call result carrying `obj` as its text item, the way mcp.py sends it."""
    return {"content": [{"type": "text", "text": json.dumps(obj)}]}


class Stub(http.server.BaseHTTPRequestHandler):
    """Answers POST /api/mcp from `answer(request) -> (status, bytes)`."""
    answer = None
    seen = []

    def do_POST(self):
        req = json.loads(self.rfile.read(int(self.headers["content-length"])))
        type(self).seen.append(req)
        status, body = type(self).answer(req)
        self.send_response(status)
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


def _serve(handler):
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{httpd.server_address[1]}"


def run_ds(*argv):
    """(exit code or message, stdout, stderr) of `ds <argv>`."""
    out, err = io.StringIO(), io.StringIO()
    with mock.patch.object(sys, "argv", ["ds", *argv]), \
            contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = ds.main()
        except SystemExit as e:
            code = e.code
    return code, out.getvalue(), err.getvalue()


class StubTest(unittest.TestCase):
    """Each test sets `self.tools`: tool name -> a result, or a function of the arguments."""

    @classmethod
    def setUpClass(cls):
        cls.handler = type("H", (Stub,), {"seen": []})
        cls.httpd, cls.base = _serve(cls.handler)

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def setUp(self):
        self.handler.seen.clear()
        self.tools = {}
        self.handler.answer = self.answer

    def answer(self, req):
        if req["method"] == "initialize":
            result = {"serverInfo": {"name": "design-systems", "version": "9"}, "instructions": "Read-only."}
        elif req["method"] == "tools/list":
            result = {"tools": [{"name": "search_styles", "description": "Rank styles. More text."}]}
        else:
            tool = self.tools[req["params"]["name"]]
            result = tool(req["params"]["arguments"]) if callable(tool) else tool
        return 200, json.dumps({"jsonrpc": "2.0", "id": req["id"], "result": result}).encode()

    def ds(self, *argv):
        return run_ds("--url", self.base + "/", *argv)

    def args(self, i=-1):
        return self.handler.seen[i]["params"]["arguments"]


class BaseUrlTest(unittest.TestCase):
    def test_flag_then_env_then_config_file(self):
        with tempfile.TemporaryDirectory() as d:
            cfg = Path(d) / "url"
            cfg.write_text("https://from-file.example/\n")
            with mock.patch.object(ds, "CFG", cfg), mock.patch.dict(os.environ, {"DESIGNS_URL": "https://env.example"}):
                self.assertEqual(ds._base("https://flag.example/"), "https://flag.example")
                self.assertEqual(ds._base(None), "https://env.example")
            with mock.patch.object(ds, "CFG", cfg), mock.patch.dict(os.environ, {}, clear=True):
                self.assertEqual(ds._base(None), "https://from-file.example")

    def test_nothing_configured_says_how_to_install(self):
        with mock.patch.object(ds, "CFG", Path("/nonexistent/ds/url")), mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(SystemExit) as caught:
                ds._base(None)
        self.assertIn("install.sh", str(caught.exception))


class CommandsTest(StubTest):
    def test_status_and_tools(self):
        code, out, _ = self.ds("status")
        self.assertEqual(code, 0)
        self.assertIn("design-systems 9", out)
        self.assertIn("Read-only.", out)
        self.assertEqual(self.handler.seen[0]["method"], "initialize")
        code, out, _ = self.ds("--json", "status")
        self.assertEqual(json.loads(out)["serverInfo"]["version"], "9")
        code, out, _ = self.ds("tools")
        self.assertEqual(out.split(), ["search_styles", "Rank", "styles"])
        code, out, _ = self.ds("--json", "tools")
        self.assertEqual(json.loads(out)["tools"][0]["name"], "search_styles")

    def test_find_forwards_filters_and_prints_hits(self):
        self.tools["search_styles"] = lambda a: {"hits": [{"slug": "acme", "name": "Acme", "goodFor": "dense tables"},
                                                          {"slug": "beta", "tagline": "calm"}]}
        code, out, _ = self.ds("find", "dark", "dense", "--platform", "ios", "--limit", "2", "--store", "systems")
        self.assertEqual(code, 0)
        self.assertEqual(self.args(), {"query": "dark dense", "store": "systems", "platform": "ios",
                                       "style": None, "limit": 2})
        self.assertIn("dense tables", out)
        self.assertIn("calm", out)
        self.tools["search_styles"] = {"content": [{"type": "text", "text": '{"hits": []}'}]}
        self.assertIn("no hits", self.ds("find", "zzz")[1])
        code, out, _ = self.ds("--json", "find", "zzz")
        self.assertEqual(json.loads(out), {"hits": []})

    def test_style_prints_known_fields_and_files(self):
        self.tools["get_style"] = _text({"name": "Acme", "platform": "web", "tags": ["dark", "dense"],
                                         "unknown": "hidden", "files": {"tokens": "systems/acme/tokens.json"}})
        code, out, _ = self.ds("style", "acme", "--store", "systems")
        self.assertEqual(self.args(), {"slug": "acme", "store": "systems"})
        self.assertIn("dark, dense", out)
        self.assertIn("systems/acme/tokens.json", out)
        self.assertNotIn("hidden", out)
        self.assertEqual(json.loads(self.ds("--json", "style", "acme")[1])["unknown"], "hidden")

    def test_export_lists_groups_without_a_group(self):
        self.tools["get_tokens"] = _text({"slug": "acme", "groups": {"light": 3, "core": 5}, "note": "pick one"})
        code, out, _ = self.ds("export", "acme")
        self.assertIn("acme: token groups — light (3), core (5)", out)
        self.assertIn("pick one", out)

    def test_export_follows_pages_to_print_a_whole_group(self):
        pages = {None: {"tokens": {"a": "1"}, "truncated": True, "nextOffset": 1},
                 1: {"tokens": {"b": "2"}, "truncated": True, "nextOffset": 2},
                 2: {"tokens": {"c": "3"}, "truncated": False}}
        self.tools["get_tokens"] = lambda a: _text(pages[a.get("offset")])
        code, out, _ = self.ds("export", "acme", "-g", "dark")
        self.assertEqual(out.splitlines(), ["a: 1", "b: 2", "c: 3"])
        self.assertEqual([s["params"]["arguments"].get("offset") for s in self.handler.seen], [None, 1, 2])
        code, out, _ = self.ds("--json", "export", "acme", "-g", "dark")
        joined = json.loads(out)
        self.assertEqual((joined["tokens"], joined["offset"]), ({"a": "1", "b": "2", "c": "3"}, 0))
        self.assertNotIn("nextOffset", joined)

    def test_export_one_page_points_at_the_next(self):
        self.tools["get_tokens"] = lambda a: _text({"tokens": {"a": "1"}, "truncated": True, "nextOffset": 7})
        code, out, err = self.ds("export", "acme", "-g", "dark", "--offset", "0", "--limit", "1")
        self.assertEqual(self.args(), {"slug": "acme", "group": "dark", "offset": 0, "limit": 1})
        self.assertEqual(out, "a: 1\n")
        self.assertIn("--offset 7", err)

    def test_export_from_an_old_server_that_truncated_stops_cleanly(self):
        self.tools["get_tokens"] = _text({"partial": "{\"a\":", "bytes": 99999})
        code, out, _ = self.ds("export", "acme", "-g", "dark")
        self.assertIn("does not page get_tokens", code)

    def test_doc_single_page_hints_the_next_offset(self):
        self.tools["read_doc"] = _text({"text": "# Acme\n", "truncated": True, "nextOffset": 40, "length": 90})
        code, out, err = self.ds("doc", "acme", "tokens.json")
        self.assertEqual(self.args(), {"slug": "acme", "path": "tokens.json"})
        self.assertEqual(out, "# Acme\n\n")
        self.assertIn("doc acme tokens.json --offset 40", err)
        self.assertIn("--url", err)                                   # the hint repeats --url
        self.tools["read_doc"] = _text({"text": "x", "truncated": True})
        self.assertIn("… [truncated]", self.ds("readme", "acme", "--offset", "3")[2])
        self.assertEqual(self.args()["offset"], 3)

    def test_doc_all_joins_every_page(self):
        pages = {None: {"path": "README.md", "text": "one ", "truncated": True, "nextOffset": 4},
                 4: {"text": "two", "truncated": False}}
        self.tools["read_doc"] = lambda a: _text(pages[a.get("offset")])
        self.assertEqual(self.ds("doc", "acme", "--all")[1], "one two\n")
        joined = json.loads(self.ds("--json", "doc", "acme", "--all")[1])
        self.assertEqual((joined["text"], joined["pages"], joined["truncated"]), ("one two", 2, False))
        self.assertNotIn("nextOffset", joined)
        self.assertEqual(json.loads(self.ds("--json", "doc", "acme")[1])["nextOffset"], 4)

    def test_media_prints_absolute_urls(self):
        self.tools["list_media"] = _text({"items": [{"kind": "screenshots", "name": "home.png",
                                                     "url": "/media/systems/acme/home.png"}], "capped": True})
        code, out, err = self.ds("media", "acme", "screenshots")
        self.assertEqual(self.args(), {"slug": "acme", "kind": "screenshots"})
        self.assertIn(f"{self.base}/media/systems/acme/home.png", out)
        self.assertIn("capped", err)

    def test_handoff_sends_the_description_or_none(self):
        self.tools["handoff_prompt"] = _text({"prompt": "Apply acme."})
        self.assertEqual(self.ds("handoff", "acme", "a", "todo", "app")[1], "Apply acme.\n")
        self.assertEqual(self.args()["app_description"], "a todo app")
        self.ds("handoff", "acme")
        self.assertIsNone(self.args()["app_description"])

    def test_a_plain_text_result_is_printed_as_is(self):
        self.tools["handoff_prompt"] = {"content": [{"type": "text", "text": "not json"}]}
        self.assertEqual(self.ds("--json", "handoff", "acme")[1], '"not json"\n')


class ErrorsTest(StubTest):
    def test_tool_error_exits_with_its_text(self):
        self.tools["get_style"] = {"isError": True, "content": [{"type": "text", "text": "unknown slug: nope"}]}
        self.assertEqual(self.ds("style", "nope")[0], "ds: unknown slug: nope")

    def test_rpc_error_exits_with_code_and_message(self):
        self.handler.answer = lambda req: (200, json.dumps(
            {"jsonrpc": "2.0", "id": 1, "error": {"code": -32601, "message": "no such method"}}).encode())
        self.assertEqual(self.ds("status")[0], "ds: mcp error -32601: no such method")
        self.handler.answer = lambda req: (200, b'{"error": "flat string"}')
        self.assertEqual(self.ds("status")[0], "ds: mcp error None: flat string")

    def test_a_non_json_rpc_page_exits_cleanly(self):
        # A wrong URL (the static docs site, a login page) used to end in a JSONDecodeError traceback.
        for body in (b"<!doctype html><title>Sign in</title>", b"[1, 2]"):
            self.handler.answer = lambda req, body=body: (200, body)
            code = self.ds("find", "dark")[0]
            self.assertIsInstance(code, str)
            self.assertIn("did not answer with JSON-RPC", code)

    def test_http_error_and_unreachable_server(self):
        self.handler.answer = lambda req: (502, b"bad gateway")
        self.assertIn("HTTP Error 502", self.ds("status")[0])
        httpd, base = _serve(Stub)
        httpd.shutdown()
        httpd.server_close()                                          # nothing listens there now
        code = run_ds("--url", base, "status")[0]
        self.assertTrue(code.startswith(f"ds: {base}/api/mcp: "), code)

    def test_an_empty_reply_is_an_empty_result(self):
        self.handler.answer = lambda req: (200, b"")
        self.assertEqual(self.ds("find", "dark")[1], "no hits\n")


class RealServerTest(unittest.TestCase):
    """ds against server/api.py: the tool names and payload shapes it reads exist."""

    def test_status_find_and_style(self):
        api = _load("ds_cli_api", ROOT / "server" / "api.py")
        httpd, base = _serve(api.Handler)
        try:
            code, out, _ = run_ds("--url", base, "status")
            self.assertEqual(code, 0)
            self.assertTrue(out.startswith("design-systems "), out)
            code, out, _ = run_ds("--url", base, "--json", "find", "dark", "--store", "systems", "--limit", "1")
            hits = json.loads(out)["hits"]
            self.assertEqual(len(hits), 1)
            code, out, _ = run_ds("--url", base, "style", hits[0]["slug"])
            self.assertEqual(code, 0)
            self.assertIn("name", out)
        finally:
            httpd.shutdown()
            httpd.server_close()


if __name__ == "__main__":
    unittest.main()
