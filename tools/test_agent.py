"""Tests for server/ (library tools and the chat adapters). Run with `make test`."""
import importlib.util
import json
import os
import unittest
from pathlib import Path

SERVER = Path(__file__).resolve().parent.parent / "server"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, SERVER / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


library = _load("agent_library", "library.py")
chat = _load("agent_chat", "chat.py")


class SearchTest(unittest.TestCase):
    def test_systems_hits(self):
        out = library.call("search_styles", {"query": "dark dense dashboard", "store": "systems", "limit": 5})
        self.assertTrue(out["hits"])
        self.assertTrue(all(h["store"] == "systems" for h in out["hits"]))
        self.assertTrue(all(h["slug"] for h in out["hits"]))

    def test_limit_and_store(self):
        out = library.call("search_styles", {"query": "minimal", "store": "systems", "limit": 2})
        self.assertLessEqual(len(out["hits"]), 2)

    def test_unknown_slug_and_tool(self):
        with self.assertRaises(library.ToolError):
            library.get_style("no-such-package")
        with self.assertRaises(library.ToolError):
            library.call("drop_tables", {})

    def test_missing_required_args_raise(self):
        # A bare call must fail as a ToolError, never as an uncaught TypeError
        # that could end an MCP session.
        with self.assertRaises(library.ToolError):
            library.call("get_style", {})
        with self.assertRaises(library.ToolError):
            library.call("read_doc", {})

    def test_get_style_store_disambiguates(self):
        sys_row = library.get_style("linear", "systems")
        self.assertEqual(sys_row.get("slug"), "linear")
        ref = library.get_style("linear", "refero")
        self.assertEqual(ref.get("slug"), "linear")
        self.assertNotEqual(ref, sys_row)

    def test_collect_ignores_error_results(self):
        # A failed tool call must not abort the turn: nothing is collected from
        # an error payload, while a good one still lands.
        results, media = {}, {}
        chat._collect("get_style", {"slug": "nope"}, {"error": "no such style"}, results, media)
        self.assertFalse(results)
        self.assertFalse(media)
        chat._collect("get_style", {"slug": "x"}, {"slug": "x", "name": "X"}, results, media)
        self.assertEqual(results["systems:x"]["slug"], "x")


class PackageFileTest(unittest.TestCase):
    SLUG = "linear" if (Path(__file__).resolve().parents[1] / "systems" / "linear").is_dir() else None

    def setUp(self):
        if not self.SLUG:
            self.skipTest("systems/linear is not present")

    def test_read_doc_defaults_to_readme(self):
        out = library.read_doc(self.SLUG)
        self.assertTrue(out["path"].endswith("README.md"))
        self.assertIn("#", out["text"])

    def test_bounded_path_cannot_escape(self):
        for bad in ("../../catalog.json", "/etc/passwd", ".."):
            with self.assertRaises(library.ToolError):
                library.read_doc(self.SLUG, bad)

    def test_get_tokens_lists_groups_then_values(self):
        groups = library.get_tokens(self.SLUG)
        self.assertIn("base", groups["groups"])
        first = next(iter(groups["groups"]))
        values = library.get_tokens(self.SLUG, first)
        self.assertTrue(values["tokens"])
        with self.assertRaises(library.ToolError):
            library.get_tokens(self.SLUG, "nope")

    def test_media(self):
        listing = library.list_media(self.SLUG, "screenshots")
        if not listing["items"]:
            self.skipTest("no screenshots in this package")
        item = listing["items"][0]
        self.assertTrue(item["url"].startswith("/media/systems/"))
        shot = library.view_media(self.SLUG, f"screenshots/{item['name']}.png")
        self.assertIn("_image", shot)
        self.assertEqual(shot["_image"]["media_type"], "image/png")

    def test_handoff_prompt(self):
        out = library.handoff_prompt(self.SLUG)
        self.assertIn("tokens", out["prompt"])
        self.assertIn(self.SLUG, out["prompt"])


class ProviderTest(unittest.TestCase):
    def test_parse_openai_and_anthropic_shape(self):
        self.assertEqual(chat._parse_models({"data": [{"id": "m1"}, {"id": "m2", "display_name": "M2"}]}),
                         [{"id": "m1", "label": "m1"}, {"id": "m2", "label": "M2"}])

    def test_parse_gemini_shape(self):
        self.assertEqual(chat._parse_models({"models": [{"name": "models/gemini-2.5-pro",
                                                         "displayName": "Gemini 2.5 Pro"}]}),
                         [{"id": "gemini-2.5-pro", "label": "Gemini 2.5 Pro"}])

    def test_config_prefers_body_then_env(self):
        cfg = chat.provider_config({"api": "openai", "base_url": "https://x.test/v1/",
                                    "api_key": "k", "model": "m"})
        self.assertEqual(cfg["base_url"], "https://x.test/v1")
        env = chat.provider_config(None)
        self.assertEqual(env is not None, bool(os.environ.get("ANTHROPIC_API_KEY")))

    def test_list_models_only_passes_missing_route(self):
        cfg = {"api": "openai", "api_key": "k", "base_url": "https://x.test/v1"}
        orig = chat._request
        try:
            for err, ok in (("HTTP 404", True), ("HTTP 405", True),
                            ("HTTP 401", False), ("HTTP 500", False), ("unreachable", False)):
                chat._request = lambda *a, _e=err, **k: (_ for _ in ()).throw(chat.ProviderError(_e))
                self.assertEqual(chat.list_models(cfg)["ok"], ok, err)
            chat._request = lambda *a, **k: {"data": [{"id": "m1"}]}
            self.assertEqual(chat.list_models(cfg)["models"][0]["id"], "m1")
        finally:
            chat._request = orig

    def test_headers(self):
        cfg = {"api": "anthropic", "api_key": "k"}
        self.assertEqual(chat._headers(cfg)["x-api-key"], "k")
        self.assertIn("anthropic-version", chat._headers(cfg))
        cfg = {"api": "openai", "api_key": "k"}
        self.assertEqual(chat._headers(cfg)["authorization"], "Bearer k")
        cfg = {"api": "openai", "api_key": "k", "key_header": "x-goog-api-key"}
        self.assertEqual(chat._headers(cfg)["x-goog-api-key"], "k")


class WireShapeTest(unittest.TestCase):
    TURNS = [
        {"role": "user", "text": "dense dark table?"},
        {"role": "assistant", "text": None, "calls": [{"id": "c1", "name": "search_styles", "args": {"query": "dense"}}]},
        {"role": "tool", "id": "c1", "result": {"hits": []}},
        {"role": "tool", "id": "c2", "result": {"_image": {"media_type": "image/png", "data": "AA==",
                                                          "url": "/systems/x/y.png", "name": "x/y"}}},
    ]

    def test_anthropic_merges_tool_results_into_one_user_message(self):
        msgs = chat._anthropic_messages(self.TURNS)
        self.assertEqual([m["role"] for m in msgs], ["user", "assistant", "user"])
        results = msgs[2]["content"]
        self.assertEqual(len(results), 2)
        self.assertTrue(all(b["type"] == "tool_result" for b in results))
        self.assertEqual(results[1]["content"][1]["type"], "image")

    def test_openai_roles(self):
        msgs = chat._openai_messages(self.TURNS)
        roles = [m["role"] for m in msgs]
        # OpenAI tool messages take text only; an image result closes the tool
        # run and follows as its own user message.
        self.assertEqual(roles, ["system", "user", "assistant", "tool", "tool", "user"])
        tool = msgs[4]
        self.assertEqual(tool["tool_call_id"], "c2")
        self.assertIn("x/y", tool["content"])
        image = [p for p in msgs[5]["content"] if p["type"] == "image_url"]
        self.assertTrue(image)


class McpTest(unittest.TestCase):
    mcp = _load("agent_mcp", "mcp.py")

    def _roundtrip(self, *reqs):
        return [r for r in (self.mcp.handle(req) for req in reqs) if r is not None]

    def test_initialize_and_list(self):
        init, listing = self._roundtrip(
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        self.assertEqual(init["result"]["serverInfo"]["name"], "design-systems")
        self.assertEqual([t["name"] for t in listing["result"]["tools"]],
                         [s["name"] for s in library.SPECS])

    def test_call_and_unknown(self):
        ok, bad = self._roundtrip(
            {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
             "params": {"name": "search_styles", "arguments": {"query": "dark", "limit": 1}}},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
             "params": {"name": "nope", "arguments": {}}})
        self.assertEqual(ok["result"]["content"][0]["type"], "text")
        self.assertIn("error", bad)

    def test_notification_gets_no_reply(self):
        self.assertEqual(self._roundtrip({"jsonrpc": "2.0", "method": "notifications/initialized"}), [])


class HttpApiTest(unittest.TestCase):
    """The /api/ HTTP surface api.py runs: /api/mcp over streamable HTTP plus
    the /api/ds and /api/install.sh serves that bootstrap the CLI."""
    api = _load("agent_api", "api.py")

    @classmethod
    def setUpClass(cls):
        import http.server
        import threading
        cls.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), cls.api.Handler)
        cls.base = f"http://127.0.0.1:{cls.httpd.server_address[1]}"
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def _req(self, path, method="GET", obj=None):
        import urllib.request
        import urllib.error
        data = json.dumps(obj).encode() if obj is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method,
                                     headers={"content-type": "application/json"})
        try:
            with urllib.request.urlopen(req) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            body = e.read()
            e.close()
            return e.code, body

    def _mcp(self, obj):
        return self._req("/api/mcp", "POST", obj)

    def test_initialize_and_call_over_http(self):
        status, body = self._mcp({"jsonrpc": "2.0", "id": 1, "method": "initialize",
                                  "params": {"protocolVersion": "2025-03-26"}})
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["result"]["serverInfo"]["name"], "design-systems")
        status, body = self._mcp({"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                                  "params": {"name": "search_styles",
                                             "arguments": {"query": "dark", "limit": 1}}})
        self.assertEqual(status, 200)
        hits = json.loads(json.loads(body)["result"]["content"][0]["text"])["hits"]
        self.assertEqual(len(hits), 1)

    def test_notification_batch_and_get(self):
        status, body = self._mcp({"jsonrpc": "2.0", "method": "notifications/initialized"})
        self.assertEqual((status, body), (202, b""))
        status, body = self._mcp([{"jsonrpc": "2.0", "id": 1, "method": "ping"},
                                  {"jsonrpc": "2.0", "id": 2, "method": "ping"}])
        self.assertEqual(status, 200)
        self.assertEqual(len(json.loads(body)), 2)
        self.assertEqual(self._req("/api/mcp")[0], 405)
        self.assertEqual(self._req("/api/mcp", "DELETE")[0], 200)

    def test_ds_and_install_script(self):
        status, body = self._req("/api/ds")
        self.assertEqual(status, 200)
        self.assertTrue(body.startswith(b"#!/usr/bin/env python3"))
        status, body = self._req("/api/install.sh")
        self.assertEqual(status, 200)
        text = body.decode()
        self.assertIn(f'BASE="{self.base}"', text)
        self.assertNotIn("@DS_BASE@", text)

    def test_mcp_rejects_bad_bodies(self):
        import urllib.request
        import urllib.error
        req = urllib.request.Request(self.base + "/api/mcp", data=b"not json",
                                     headers={"content-type": "application/json"})
        try:
            with urllib.request.urlopen(req) as r:
                status = r.status
        except urllib.error.HTTPError as e:
            status = e.code
            e.close()
        self.assertEqual(status, 400)


class HostAllowlistTest(unittest.TestCase):
    """routes.py refuses a Host it does not know, so a DNS-rebound name cannot
    pass the Origin==Host check."""
    api = _load("agent_api_hosts", "api.py")

    @classmethod
    def setUpClass(cls):
        import http.server
        import threading
        cls.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), cls.api.Handler)
        cls.base = f"http://127.0.0.1:{cls.httpd.server_address[1]}"
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def _status(self, host, origin=None):
        import urllib.error
        import urllib.request
        headers = {"Host": host}
        if origin:
            headers["Origin"] = origin
        req = urllib.request.Request(self.base + "/api/mcp", data=b'{"jsonrpc":"2.0","id":1,"method":"ping"}',
                                     headers={"content-type": "application/json", **headers})
        try:
            with urllib.request.urlopen(req) as r:
                return r.status
        except urllib.error.HTTPError as e:
            e.close()
            return e.code

    def test_rebound_name_is_refused(self):
        # Origin matches Host, as it does under DNS rebinding.
        self.assertEqual(self._status("evil.test:8190", "http://evil.test:8190"), 403)
        for host in ("evil.test", "evil.ts.net.evil.test", "127.0.0.1:1,evil.test", "a@localhost", "x:port"):
            self.assertEqual(self._status(host), 403, host)

    def test_known_hosts_pass(self):
        for host in ("127.0.0.1:8190", "localhost:8800", "[::1]:8190", "100.64.0.7:8108",
                     "box.tail123.ts.net:8108", "app.localhost"):
            self.assertEqual(self._status(host), 200, host)

    def test_env_allowlist(self):
        old = os.environ.get("DESIGN_SYSTEMS_ALLOWED_HOSTS")
        os.environ["DESIGN_SYSTEMS_ALLOWED_HOSTS"] = "designs.example.test, other.test:8108"
        try:
            self.assertEqual(self._status("designs.example.test:443"), 200)
            self.assertEqual(self._status("other.test:8108"), 200)
            self.assertEqual(self._status("other.test:9999"), 403)
        finally:
            if old is None:
                os.environ.pop("DESIGN_SYSTEMS_ALLOWED_HOSTS", None)
            else:
                os.environ["DESIGN_SYSTEMS_ALLOWED_HOSTS"] = old


class ChatErrorTest(unittest.TestCase):
    """An unexpected failure in /api/chat answers a generic 500; the exception
    text (paths, upstream content) stays in the server log."""

    def test_500_hides_exception_text(self):
        import contextlib
        import io
        import types
        routes = _load("agent_routes_500", "routes.py")

        class ProviderError(Exception):
            pass

        def boom(messages, cfg):
            raise RuntimeError("/srv/secret/path leaked")
        fake = types.SimpleNamespace(ProviderError=ProviderError, run=boom,
                                     provider_config=lambda p: {"api": "openai"})
        routes._load = lambda name: fake
        body = json.dumps({"messages": []}).encode()

        class H:
            path = "/api/chat"
            headers = {"content-length": str(len(body)), "host": "127.0.0.1:1"}
            rfile = io.BytesIO(body)
            wfile = io.BytesIO()
            status = None

            def send_response(self, code):
                self.status = code

            def send_header(self, *a):
                pass

            def end_headers(self):
                pass
        h = H()
        log = io.StringIO()
        with contextlib.redirect_stderr(log):
            self.assertTrue(routes.handle_post(h))
        self.assertEqual(h.status, 500)
        self.assertNotIn(b"secret", h.wfile.getvalue())
        self.assertIn("/srv/secret/path leaked", log.getvalue())


class ProviderUrlTest(unittest.TestCase):
    """The provider endpoints fetch a caller-chosen URL, so they must not read
    local files, follow redirects, or echo another server's response body."""

    @classmethod
    def setUpClass(cls):
        import http.server
        import threading
        hits = cls.hits = []

        class Upstream(http.server.BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_GET(self):
                hits.append(self.path)
                if self.path.startswith("/redirect"):
                    self.send_response(302)
                    self.send_header("location", "/target/models")
                    self.send_header("content-length", "0")
                    self.end_headers()
                    return
                body = b"internal-secret-body"
                self.send_response(401 if self.path.startswith("/denied") else 200)
                self.send_header("content-length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        cls.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
        cls.base = f"http://127.0.0.1:{cls.httpd.server_address[1]}"
        threading.Thread(target=cls.httpd.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()

    def _models(self, base_url, **extra):
        return chat.list_models({"api": "openai", "api_key": "k", "base_url": base_url, **extra})

    def test_scheme_and_host_rules(self):
        for url in ("file:///etc/passwd", "ftp://x.test/models", "http://x.test/models",
                    "http://10.0.0.5/models", "gopher://127.0.0.1/", "https:///models"):
            with self.assertRaises(chat.ProviderError, msg=url):
                chat.check_url(url)
        for url in ("https://api.x.test/v1/models", "http://127.0.0.1:11434/v1/models",
                    "http://localhost/models", "http://[::1]:8000/models"):
            chat.check_url(url)

    def test_file_url_is_never_read(self):
        out = self._models("file:///etc")
        self.assertFalse(out["ok"])
        self.assertNotIn("root", out["error"])

    def test_redirect_not_followed(self):
        before = len(self.hits)
        out = self._models(self.base + "/redirect")
        self.assertFalse(out["ok"])
        self.assertIn("redirect", out["error"])
        self.assertEqual(self.hits[before:], ["/redirect/models"])

    def test_upstream_body_not_echoed(self):
        out = self._models(self.base + "/denied")
        self.assertFalse(out["ok"])
        self.assertIn("HTTP 401", out["error"])
        self.assertNotIn("internal-secret-body", out["error"])

    def test_default_port_is_same_origin(self):
        self.assertTrue(chat._same_origin("https://p.test:443/v1", "https://p.test/models"))
        self.assertFalse(chat._same_origin("https://p.test:8443/v1", "https://p.test/models"))

    def test_non_http_greeting_not_echoed(self):
        import socket
        import threading
        srv = socket.socket()
        srv.bind(("127.0.0.1", 0))
        srv.listen(1)

        def greet():
            conn, _ = srv.accept()
            conn.sendall(b"220 internal-smtp-banner ESMTP\r\n")
            conn.close()
        threading.Thread(target=greet, daemon=True).start()
        try:
            out = self._models(f"http://127.0.0.1:{srv.getsockname()[1]}")
        finally:
            srv.close()
        self.assertFalse(out["ok"])
        self.assertNotIn("internal-smtp-banner", out["error"])

    def test_models_url_must_share_origin(self):
        out = self._models("https://api.x.test/v1", models_url=self.base + "/models")
        self.assertFalse(out["ok"])
        self.assertIn("origin", out["error"])
        self.assertEqual(self.hits.count("/models"), 0)


if __name__ == "__main__":
    unittest.main()
