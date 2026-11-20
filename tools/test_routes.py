"""Tests for server/routes.py's request handling: the guards, body parsing and
every POST/GET answer. A stub handler stands in for http.server and a fake
chat module stands in for chat.py, so no socket opens and no provider is called.
Run with `make test`."""
import contextlib
import os
import importlib.util
import io
import json
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

SERVER = Path(__file__).resolve().parent.parent / "server"

# routes.py's host guard reads DESIGN_SYSTEMS_ALLOWED_HOSTS from os.environ, which a
# shell or an earlier load of the repo's .env could fill. Pin it empty for the module,
# so GuardTest and the rest see only loopback and the hosts a test sets itself.
_ENV = mock.patch.dict(os.environ, {"DESIGN_SYSTEMS_ALLOWED_HOSTS": ""})


def setUpModule():
    _ENV.start()


def tearDownModule():
    _ENV.stop()


def _routes():
    spec = importlib.util.spec_from_file_location("routes_under_test", SERVER / "routes.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class ProviderError(Exception):
    pass


class Handler:
    """Just enough of BaseHTTPRequestHandler for routes.py."""

    def __init__(self, path, body=b"", headers=None, length=None):
        self.path = path
        self.headers = {"host": "127.0.0.1:8800", **(headers or {})}
        if length is None:
            length = len(body)
        if length != "":
            self.headers["content-length"] = str(length)
        self.rfile = io.BytesIO(body)
        self.wfile = io.BytesIO()
        self.server = types.SimpleNamespace(server_address=("127.0.0.1", 8800))
        self.status = None
        self.sent = {}

    def send_response(self, code):
        self.status = code

    def send_header(self, name, value):
        self.sent[name] = value

    def end_headers(self):
        pass

    def json(self):
        return json.loads(self.wfile.getvalue())


def _post(routes, path, obj=None, raw=None, **kw):
    body = raw if raw is not None else json.dumps(obj).encode()
    h = Handler(path, body, **kw)
    with contextlib.redirect_stderr(io.StringIO()):
        handled = routes.handle_post(h)
    return handled, h


class FakeChat:
    """Records what routes.py hands to chat.py and answers like it."""
    ProviderError = ProviderError

    def __init__(self, env_cfg=None, models=None, reply=None, raise_=None):
        self.env_cfg, self.models, self.reply, self.raise_ = env_cfg, models, reply, raise_
        self.calls = []

    def provider_config(self, provider):
        self.calls.append(("provider_config", provider))
        if provider and provider.get("api_key") and provider.get("model"):
            return dict(provider)
        return self.env_cfg

    def list_models(self, cfg):
        self.calls.append(("list_models", cfg))
        if self.raise_:
            raise self.raise_
        return self.models

    def run(self, messages, cfg):
        self.calls.append(("run", messages, cfg))
        if self.raise_:
            raise self.raise_
        return self.reply


class McpPostTest(unittest.TestCase):
    PING = {"jsonrpc": "2.0", "id": 1, "method": "ping"}

    def setUp(self):
        self.routes = _routes()

    def test_oversized_body_is_413_with_a_json_rpc_error(self):
        n = self.routes.MCP_BODY_LIMIT + 1
        _, h = _post(self.routes, "/api/mcp", raw=b" " * n)
        self.assertEqual(h.status, 413)
        self.assertEqual(h.json()["error"]["code"], -32600)
        self.assertIn(str(self.routes.MCP_BODY_LIMIT), h.json()["error"]["message"])

    def test_body_at_the_limit_is_read(self):
        raw = json.dumps(self.PING).encode().ljust(self.routes.MCP_BODY_LIMIT)
        _, h = _post(self.routes, "/api/mcp", raw=raw)
        self.assertEqual(h.status, 200)

    def test_missing_body_is_still_400(self):
        _, h = _post(self.routes, "/api/mcp", raw=b"", length="")
        self.assertEqual(h.status, 400)
        self.assertEqual(h.json()["error"]["message"], "a JSON-RPC body is required")

    def test_empty_batch_is_invalid_request(self):
        _, h = _post(self.routes, "/api/mcp", [])
        self.assertEqual(h.status, 200)
        self.assertEqual(h.json()["error"]["code"], -32600)

    def test_non_object_members_each_get_an_error(self):
        _, h = _post(self.routes, "/api/mcp", [1, 2])
        self.assertEqual(h.status, 200)
        self.assertEqual([r["error"]["code"] for r in h.json()], [-32600, -32600])

    def test_notification_only_batch_is_202(self):
        note = {"jsonrpc": "2.0", "method": "notifications/initialized"}
        for body in ([note], note):
            _, h = _post(self.routes, "/api/mcp", body)
            self.assertEqual(h.status, 202)

    def test_object_gets_a_bare_reply_and_batch_an_array(self):
        _, h = _post(self.routes, "/api/mcp", self.PING)
        self.assertEqual(h.json(), {"jsonrpc": "2.0", "id": 1, "result": {}})
        _, h = _post(self.routes, "/api/mcp", [self.PING])
        self.assertEqual(h.json(), [{"jsonrpc": "2.0", "id": 1, "result": {}}])


class BodyTest(unittest.TestCase):
    def setUp(self):
        self.routes = _routes()

    def body(self, raw, **kw):
        return self.routes._body(Handler("/api/chat", raw, **kw), cap=100)

    def test_a_json_object_is_read(self):
        self.assertEqual(self.body(b'{"a": 1}'), {"a": 1})

    def test_bad_lengths_read_nothing(self):
        self.assertIsNone(self.body(b'{"a": 1}', length=""))          # no header
        self.assertIsNone(self.body(b'{"a": 1}', length="ten"))
        self.assertIsNone(self.body(b'{"a": 1}', length=0))
        self.assertIsNone(self.body(b'{"a": 1}', length=-5))
        self.assertIsNone(self.body(b"{}" + b" " * 200))              # over the cap

    def test_non_objects_and_bad_bytes_read_nothing(self):
        for raw in (b"not json", b"[1, 2]", b'"text"', b"\xff\xfe{}"):
            self.assertIsNone(self.body(raw), raw)


class FrontDoorCasesTest(unittest.TestCase):
    """server/front-door-cases.json: the Host cases web/proxy.ts runs too
    (web/lib/request-guard.test.ts), so the two front doors agree."""

    def test_shared_host_cases(self):
        routes = _routes()
        cases = json.loads((SERVER / "front-door-cases.json").read_text())
        with mock.patch.dict(os.environ, {"DESIGN_SYSTEMS_ALLOWED_HOSTS": cases["allowedHosts"]}):
            for c in cases["hosts"]:
                h = types.SimpleNamespace(headers={"host": c["host"]})
                self.assertEqual(routes._host_ok(h), c["allowed"], c["host"])

    def test_forwarded_host_does_not_widen_the_allowlist(self):
        # Only Host is checked: X-Forwarded-Host is the client's own claim.
        routes = _routes()
        with mock.patch.dict(os.environ, {"DESIGN_SYSTEMS_ALLOWED_HOSTS": ""}):
            h = types.SimpleNamespace(headers={"host": "evil.test", "x-forwarded-host": "127.0.0.1"})
            self.assertFalse(routes._host_ok(h))


class BaseUrlTest(unittest.TestCase):
    """_base_url's result lands inside BASE="..." in the install.sh piped to
    sh, so anything beyond host characters falls back to the bind address."""

    def base(self, **headers):
        h = Handler("/api/install.sh", headers={"host": "designs.test", **headers})
        h.server.server_address = ("127.0.0.9", 8190)  # the fallback, distinct from any Host
        return _routes()._base_url(h)

    def test_plain_hosts_are_used(self):
        self.assertEqual(self.base(host="box.tail1.ts.net:8108"), "http://box.tail1.ts.net:8108")
        self.assertEqual(self.base(**{"x-forwarded-host": "a.test, b.test", "x-forwarded-proto": "https"}),
                         "https://a.test")
        self.assertEqual(self.base(host="[::1]:8800"), "http://[::1]:8800")

    def test_shell_characters_fall_back_to_the_bind_address(self):
        for headers in ({"host": "x.test`id`"}, {"host": "x.test$(id)"}, {"host": 'x.test";id;"'},
                        {"host": "x.test'"}, {"host": "x.test\\"}, {"host": "x.test id"},
                        {"x-forwarded-host": "x.test;id"},
                        {"x-forwarded-proto": "ftp"}, {"x-forwarded-proto": "https$(id)"}):
            self.assertEqual(self.base(**headers), "http://127.0.0.9:8190", headers)


class GuardTest(unittest.TestCase):
    def setUp(self):
        self.routes = _routes()
        self.routes._load = lambda name: FakeChat()

    def test_non_api_paths_are_left_alone(self):
        self.assertFalse(self.routes.handle_get(Handler("/gallery/")))
        self.assertFalse(self.routes.handle_post(Handler("/gallery/")))

    def test_cross_origin_post_is_refused(self):
        for header in ("origin", "referer"):
            handled, h = _post(self.routes, "/api/chat", {"messages": []},
                               headers={header: "https://evil.test/page"})
            self.assertTrue(handled)
            self.assertEqual((h.status, h.json()["error"]), (403, "cross-origin request"), header)

    def test_same_origin_passes(self):
        handled, h = _post(self.routes, "/api/nope", {}, headers={"origin": "http://127.0.0.1:8800"})
        self.assertEqual(h.status, 404)

    def test_the_allowlist_is_pinned_empty_for_these_tests(self):
        self.assertEqual(os.environ.get("DESIGN_SYSTEMS_ALLOWED_HOSTS"), "")

    def test_unknown_host_is_refused_on_get(self):
        h = Handler("/api/status", headers={"host": "rebound.example"})
        self.assertTrue(self.routes.handle_get(h))
        self.assertEqual(h.status, 403)


class GetTest(unittest.TestCase):
    def setUp(self):
        self.routes = _routes()
        self.routes._load = lambda name: FakeChat(env_cfg={"api": "anthropic"})

    def get(self, path):
        h = Handler(path)
        self.assertTrue(self.routes.handle_get(h))
        return h

    def test_status_reports_the_env_provider_without_the_key(self):
        h = self.get("/api/status?x=1")
        self.assertEqual((h.status, h.json()), (200, {"ok": True, "envProvider": True}))
        self.assertEqual(h.sent["cache-control"], "no-store")

    def test_unknown_route_is_404(self):
        self.assertEqual(self.get("/api/nope").status, 404)

    def test_missing_cli_files_are_404(self):
        with tempfile.TemporaryDirectory() as d:
            self.routes._ROOT = Path(d)
            self.assertEqual(self.get("/api/ds").status, 404)
            self.assertEqual(self.get("/api/install.sh").status, 404)


class ProviderTestRouteTest(unittest.TestCase):
    good = {"base_url": "https://models.example/v1/", "api_key": "test-key"}

    def setUp(self):
        self.routes = _routes()
        self.chat = FakeChat(models={"ok": True, "models": [{"id": "m", "label": "m"}]})
        self.routes._load = lambda name: self.chat

    def test_required_fields(self):
        for body in ({}, {"api_key": "k"}, {"base_url": "https://x.example"}):
            handled, h = _post(self.routes, "/api/provider/test", body)
            self.assertEqual(h.status, 400, body)
        handled, h = _post(self.routes, "/api/provider/test", raw=b"nope")
        self.assertEqual(h.status, 400)
        self.assertEqual(self.chat.calls, [])

    def test_defaults_and_trailing_slash(self):
        handled, h = _post(self.routes, "/api/provider/test", self.good)
        self.assertEqual((h.status, h.json()["ok"]), (200, True))
        cfg = self.chat.calls[0][1]
        self.assertEqual((cfg["api"], cfg["base_url"]), ("openai", "https://models.example/v1"))

    def test_non_string_fields_are_refused_not_crashed_on(self):
        # base_url as a number used to raise AttributeError on .rstrip and drop the connection.
        for extra in ({"base_url": 123}, {"api_key": ["k"]}, {"models_url": 5},
                      {"key_header": {"x": 1}}, {"api": 1}):
            handled, h = _post(self.routes, "/api/provider/test", {**self.good, **extra})
            self.assertTrue(handled)
            self.assertEqual(h.status, 400, extra)
        self.assertEqual(self.chat.calls, [])

    def test_provider_error_is_a_200_with_the_message(self):
        self.chat.raise_ = ProviderError("HTTP 401 from models.example")
        handled, h = _post(self.routes, "/api/provider/test", self.good)
        self.assertEqual((h.status, h.json()), (200, {"ok": False, "error": "HTTP 401 from models.example"}))

    def test_unexpected_error_is_a_generic_500(self):
        self.chat.raise_ = RuntimeError("/srv/private/path")
        handled, h = _post(self.routes, "/api/provider/test", self.good)
        self.assertEqual(h.status, 500)
        self.assertNotIn(b"private", h.wfile.getvalue())


class ChatRouteTest(unittest.TestCase):
    provider = {"api": "openai", "base_url": "https://models.example/v1", "api_key": "k", "model": "m"}

    def setUp(self):
        self.routes = _routes()
        self.chat = FakeChat(reply={"reply": "hi", "results": [], "media": []})
        self.routes._load = lambda name: self.chat

    def test_body_required(self):
        handled, h = _post(self.routes, "/api/chat", raw=b"")
        self.assertEqual(h.status, 400)

    def test_no_provider_anywhere_is_503(self):
        handled, h = _post(self.routes, "/api/chat", {"messages": []})
        self.assertEqual((h.status, h.json()["error"]), (503, "no_provider"))

    def test_env_fallback_and_message_filter(self):
        self.chat.env_cfg = {"api": "anthropic", "model": "env"}
        handled, h = _post(self.routes, "/api/chat", {"messages": [{"role": "user", "content": "x"}, "junk", 3]})
        self.assertEqual((h.status, h.json()["reply"]), (200, "hi"))
        self.assertEqual(self.chat.calls[-1][1], [{"role": "user", "content": "x"}])
        self.assertEqual(self.chat.calls[-1][2]["model"], "env")

    def test_browser_provider_is_used(self):
        handled, h = _post(self.routes, "/api/chat", {"messages": [], "provider": self.provider})
        self.assertEqual(h.status, 200)
        self.assertEqual(self.chat.calls[-1][2]["model"], "m")

    def test_ill_typed_provider_or_messages_are_refused(self):
        # Each of these raised outside the handler's try and dropped the connection.
        for body in ({"messages": [], "provider": "anthropic"},
                     {"messages": [], "provider": ["k"]},
                     {"messages": [], "provider": {**self.provider, "base_url": 1}},
                     {"messages": 5},
                     {"messages": {"role": "user"}},
                     {"messages": 0}, {"messages": False}, {"messages": ""}, {"messages": {}}):
            handled, h = _post(self.routes, "/api/chat", body)
            self.assertTrue(handled)
            self.assertEqual(h.status, 400, body)
        self.assertNotIn("run", [c[0] for c in self.chat.calls])

    def test_missing_or_null_messages_mean_none(self):
        self.chat.env_cfg = {"api": "anthropic"}
        for body in ({}, {"messages": None}, {"provider": None}):
            handled, h = _post(self.routes, "/api/chat", body or {"x": 1})
            self.assertEqual(h.status, 200, body)
            self.assertEqual(self.chat.calls[-1][1], [])

    def test_provider_error_is_a_200_with_empty_results(self):
        self.chat.env_cfg = {"api": "anthropic"}
        self.chat.raise_ = ProviderError("HTTP 429")
        handled, h = _post(self.routes, "/api/chat", {"messages": []})
        self.assertEqual((h.status, h.json()),
                         (200, {"reply": "", "error": "HTTP 429", "results": [], "media": []}))

    def test_unknown_post_route_is_404(self):
        handled, h = _post(self.routes, "/api/chat/extra", {"messages": []})
        self.assertEqual(h.status, 404)


if __name__ == "__main__":
    unittest.main()
