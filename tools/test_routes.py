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
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        handled = routes.handle_post(h)
    h.stderr = err.getvalue()
    return handled, h


def _store():
    spec = importlib.util.spec_from_file_location("provider_store_under_test", SERVER / "provider_store.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _loader(chat, store=None):
    """routes._load for a test: the real provider store (pointed at a
    throwaway folder by TempConfig), the fake chat for everything else."""
    store = store or _store()
    return lambda name: store if name == "provider_store" else chat


class TempConfig(unittest.TestCase):
    """Points DESIGN_SYSTEMS_CONFIG_DIR at a fresh folder for each test, so a
    saved provider never lands in the real ~/.config."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.config = Path(self._tmp.name) / "config"
        patch = mock.patch.dict(os.environ, {"DESIGN_SYSTEMS_CONFIG_DIR": str(self.config)})
        patch.start()
        self.addCleanup(patch.stop)
        self.addCleanup(self._tmp.cleanup)


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


class GetTest(TempConfig):
    def setUp(self):
        super().setUp()
        self.routes = _routes()
        self.routes._load = _loader(FakeChat(env_cfg={"api": "anthropic", "api_key": "env-test-key"}))

    def get(self, path):
        h = Handler(path)
        self.assertTrue(self.routes.handle_get(h))
        return h

    def test_status_reports_the_env_provider_without_the_key(self):
        h = self.get("/api/status?x=1")
        self.assertEqual((h.status, h.json()),
                         (200, {"ok": True, "envProvider": True, "configured": True, "source": "env"}))
        self.assertNotIn(b"env-test-key", h.wfile.getvalue())
        self.assertEqual(h.sent["cache-control"], "no-store")

    def test_unknown_route_is_404(self):
        self.assertEqual(self.get("/api/nope").status, 404)

    def test_missing_cli_files_are_404(self):
        with tempfile.TemporaryDirectory() as d:
            self.routes._ROOT = Path(d)
            self.assertEqual(self.get("/api/ds").status, 404)
            self.assertEqual(self.get("/api/install.sh").status, 404)


class ProviderTestRouteTest(TempConfig):
    good = {"base_url": "https://models.example/v1/", "api_key": "test-key"}

    def setUp(self):
        super().setUp()
        self.routes = _routes()
        self.chat = FakeChat(models={"ok": True, "models": [{"id": "m", "label": "m"}]})
        self.routes._load = _loader(self.chat)

    def test_required_fields(self):
        # No body, or no key with none held. A blank base URL is the API's default.
        for body in ({}, {"base_url": "https://x.example"}):
            handled, h = _post(self.routes, "/api/provider/test", body)
            self.assertEqual(h.status, 400, body)
        handled, h = _post(self.routes, "/api/provider/test", raw=b"nope")
        self.assertEqual(h.status, 400)
        self.assertNotIn("list_models", [c[0] for c in self.chat.calls])

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


class ChatRouteTest(TempConfig):
    provider = {"api": "openai", "base_url": "https://models.example/v1", "api_key": "k", "model": "m"}

    def setUp(self):
        super().setUp()
        self.routes = _routes()
        self.chat = FakeChat(reply={"reply": "hi", "results": [], "media": []})
        self.routes._load = _loader(self.chat)

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

    def test_a_key_in_the_body_is_refused(self):
        # A page from before keys moved server-side; the key is never used.
        handled, h = _post(self.routes, "/api/chat", {"messages": [], "provider": self.provider})
        self.assertEqual((h.status, h.json()["error"]), (400, "key_in_body"))
        self.assertNotIn("run", [c[0] for c in self.chat.calls])

    def test_saved_provider_is_used(self):
        _store().save_provider(self.provider, "replace")
        self.chat.env_cfg = {"api": "anthropic", "model": "env", "api_key": "env-k"}
        handled, h = _post(self.routes, "/api/chat", {"messages": [], "provider": {"model": "ignored"}})
        self.assertEqual(h.status, 200)
        self.assertEqual((self.chat.calls[-1][2]["model"], self.chat.calls[-1][2]["api_key"]), ("m", "k"))

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


KEY = "sk-test-0123456789abcdef"
KEY2 = "sk-test-rotated-fedcba9876"
ENV_KEY = "sk-env-test-5555555555"
GOOD = {"api": "openai", "base_url": "https://models.example/v1", "model": "m1", "name": "example"}


class KeyChat(FakeChat):
    """A chat module whose model list passes, or fails echoing the key back
    as some providers do."""

    def __init__(self, fail=False, **kw):
        super().__init__(**kw)
        self.fail = fail
        self.no_list = False

    def list_models(self, cfg):
        self.calls.append(("list_models", cfg))
        if self.raise_:
            raise self.raise_
        if self.no_list:
            return {"ok": True, "models": [], "note": "no model list at this endpoint; type the model name"}
        if self.fail:
            return {"ok": False, "error": f"https://models.example/v1/models answered HTTP 401 for {cfg['api_key']}"}
        return {"ok": True, "models": [{"id": "m1", "label": "Model one"}]}


def _send(routes, method, path, obj=None):
    body = b"" if obj is None else json.dumps(obj).encode()
    h = Handler(path, body)
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        handled = getattr(routes, f"handle_{method}")(h)
    h.stderr = err.getvalue()
    return handled, h


class ProviderKeyTest(TempConfig):
    """The server-held key: tested before it is saved, saved 0600 outside the
    checkout, never returned, resolved saved-then-env, kept out of every
    answer and log line."""

    def setUp(self):
        super().setUp()
        self.routes = _routes()
        self.store = _store()
        self.chat = KeyChat()
        self.routes._load = _loader(self.chat, self.store)
        self.seen = []

    def call(self, method, path, obj=None):
        handled, h = _send(self.routes, method, path, obj)
        self.assertTrue(handled)
        self.seen += [h.wfile.getvalue().decode(), h.stderr]
        return h

    def assert_no_key(self, *keys):
        text = "\n".join(self.seen)
        for k in keys or (KEY, KEY2, ENV_KEY):
            self.assertNotIn(k, text)

    def saved(self):
        return self.store.load() or {}

    def models_calls(self):
        return [c[1] for c in self.chat.calls if c[0] == "list_models"]

    def test_save_tests_first_then_writes_0600_outside_the_checkout(self):
        h = self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.assertEqual((h.status, h.json()["ok"], h.json()["source"]), (200, True, "saved"))
        self.assertEqual([c["api_key"] for c in self.models_calls()], [KEY])
        f = self.config / "provider.db"
        self.assertEqual(self.config.stat().st_mode & 0o777, 0o700)
        self.assertEqual(self.saved()["api_key"], KEY)
        # SQLite's side files get the database file's mode.
        for p in self.config.iterdir():
            self.assertEqual(p.stat().st_mode & 0o777, 0o600, p.name)
        self.assertFalse(str(f).startswith(str(SERVER.parent)))
        self.assert_no_key()

    def test_state_says_where_the_key_comes_from_never_the_key(self):
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        got = self.call("get", "/api/provider").json()
        self.assertEqual((got["source"], got["configured"], got["provider"]), ("saved", True, GOOD))
        status = self.call("get", "/api/status").json()
        self.assertEqual((status["source"], status["configured"]), ("saved", True))
        self.assertNotIn("api_key", json.dumps(got))
        self.assert_no_key()

    def test_a_failing_key_is_not_saved_and_its_echo_is_redacted(self):
        self.chat.fail = True
        h = self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.assertEqual((h.status, h.json()["ok"], h.json()["saved"]), (200, False, False))
        self.assertIn("[redacted]", h.json()["error"])
        self.assertIsNone(self.store.load())
        self.assert_no_key()

    def test_rotation_keeps_the_old_key_until_the_new_one_passes(self):
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.chat.fail = True
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY2})
        self.assertEqual(self.saved()["api_key"], KEY)
        self.chat.fail = False
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY2})
        self.assertEqual(self.saved()["api_key"], KEY2)
        self.assert_no_key()

    def test_the_model_changes_without_the_key_but_the_endpoint_does_not(self):
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.chat.calls.clear()
        h = self.call("post", "/api/provider", {**GOOD, "model": "m2"})
        self.assertEqual(h.status, 200)
        self.assertEqual(self.models_calls(), [])
        self.assertEqual((self.saved()["model"], self.saved()["api_key"]), ("m2", KEY))
        for change in ({"base_url": "https://elsewhere.example/v1"}, {"api": "anthropic"},
                       {"key_header": "x-other"}, {"models_url": "https://models.example/list"}):
            h = self.call("post", "/api/provider", {**GOOD, **change})
            self.assertEqual(h.status, 400, change)
        self.assertEqual(self.saved()["base_url"], GOOD["base_url"])

    def test_bad_saves_are_refused_without_quoting_the_key(self):
        for body in ({**GOOD, "model": "", "api_key": KEY}, {**GOOD}, {**GOOD, "base_url": 1},
                     {**GOOD, "api": "other"}, {**GOOD, "api_key": KEY + "\nx-injected: 1"}):
            h = self.call("post", "/api/provider", body)
            self.assertEqual(h.status, 400, body)
        self.assertEqual(self.models_calls(), [])
        self.assert_no_key()

    def test_the_held_key_is_tested_only_against_its_own_endpoint(self):
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.chat.calls.clear()
        h = self.call("post", "/api/provider/test", {**GOOD, "base_url": GOOD["base_url"] + "/"})
        self.assertEqual((h.status, h.json()["ok"]), (200, True))
        self.assertEqual([c["api_key"] for c in self.models_calls()], [KEY])
        self.chat.calls.clear()
        h = self.call("post", "/api/provider/test", {**GOOD, "base_url": "https://attacker.example/v1"})
        self.assertEqual(h.status, 400)
        self.assertEqual(self.models_calls(), [])
        self.assert_no_key()

    def test_precedence_saved_then_env_then_none(self):
        self.chat.reply = {"reply": "hi", "results": [], "media": []}
        h = self.call("post", "/api/chat", {"messages": []})
        self.assertEqual(h.status, 503)
        self.chat.env_cfg = {"api": "anthropic", "base_url": "https://api.anthropic.com",
                             "api_key": ENV_KEY, "model": "env"}
        self.assertEqual(self.call("get", "/api/provider").json()["source"], "env")
        self.call("post", "/api/chat", {"messages": []})
        self.assertEqual(self.chat.calls[-1][2]["api_key"], ENV_KEY)
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.call("post", "/api/chat", {"messages": []})
        self.assertEqual(self.chat.calls[-1][2]["api_key"], KEY)
        h = self.call("delete", "/api/provider")
        self.assertEqual((h.json()["removed"], h.json()["source"]), (True, "env"))
        self.call("post", "/api/chat", {"messages": []})
        self.assertEqual(self.chat.calls[-1][2]["api_key"], ENV_KEY)
        self.assertEqual(self.call("delete", "/api/provider").json()["removed"], False)
        self.assert_no_key()

    def test_a_broken_saved_file_is_reported_not_replaced_by_env(self):
        self.chat.env_cfg = {"api": "anthropic", "api_key": ENV_KEY, "model": "env"}
        self.config.mkdir(parents=True)
        (self.config / "provider.db").write_text(("not a database, key %s " % KEY) * 200)
        state = self.call("get", "/api/provider").json()
        self.assertEqual((state["source"], state["configured"]), ("saved", False))
        h = self.call("post", "/api/chat", {"messages": []})
        self.assertRegex(h.json()["error"], "cannot be (read|used)")
        self.assertNotIn("run", [c[0] for c in self.chat.calls])
        self.assert_no_key()

    def test_logs_and_errors_never_carry_the_key(self):
        # An exception whose text quotes the key, as an invalid header value does.
        self.chat.raise_ = ValueError(f"Invalid header value b'Bearer {KEY}'")
        h = self.call("post", "/api/provider/test", {**GOOD, "api_key": KEY})
        self.assertEqual(h.status, 500)
        self.assertIn("[redacted]", h.stderr)
        self.chat.raise_ = ProviderError(f"https://models.example/v1?k={KEY} unreachable")
        h = self.call("post", "/api/provider/test", {**GOOD, "api_key": KEY})
        self.assertEqual((h.status, h.json()["ok"]), (200, False))
        self.chat.raise_ = None
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.chat.raise_ = RuntimeError(f"boom {KEY}")
        h = self.call("post", "/api/chat", {"messages": []})
        self.assertEqual(h.status, 500)
        self.chat.raise_ = ProviderError(f"HTTP 401 for {KEY}")
        h = self.call("post", "/api/chat", {"messages": []})
        self.assertIn("[redacted]", h.json()["error"])
        self.assert_no_key()

    def test_a_migration_never_replaces_a_saved_provider(self):
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.chat.calls.clear()
        self.chat.fail = True
        h = self.call("post", "/api/provider", {**GOOD, "api_key": KEY2, "migrate": True})
        self.assertEqual((h.json()["ok"], h.json()["existing"]), (False, True))
        self.assertEqual(self.models_calls(), [])
        self.chat.fail = False
        self.assertEqual(self.saved()["api_key"], KEY)
        self.call("delete", "/api/provider")
        h = self.call("post", "/api/provider", {**GOOD, "api_key": KEY2, "migrate": True})
        self.assertTrue(h.json()["ok"])
        self.assertEqual(self.call("post", "/api/provider", {**GOOD, "migrate": "yes"}).status, 400)
        self.assert_no_key()

    def test_an_unchecked_key_never_replaces_a_working_one(self):
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.chat.no_list = True
        h = self.call("post", "/api/provider", {**GOOD, "api_key": KEY2})
        self.assertFalse(h.json()["ok"])
        self.assertIn("could not be checked", h.json()["error"])
        self.assertEqual(self.saved()["api_key"], KEY)
        self.call("delete", "/api/provider")
        h = self.call("post", "/api/provider", {**GOOD, "api_key": KEY2})
        self.assertEqual((h.json()["ok"], h.json()["verified"]), (True, False))
        self.assert_no_key()

    def test_a_blank_key_header_is_its_apis_default(self):
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        h = self.call("post", "/api/provider", {**GOOD, "key_header": "Authorization", "model": "m3"})
        self.assertEqual(h.status, 200)
        self.assertTrue(self.store.same_endpoint({"api": "anthropic"}, {"api": "anthropic", "key_header": "x-api-key"}))
        self.assertFalse(self.store.same_endpoint({"api": "openai"}, {"api": "openai", "key_header": "x-api-key"}))

    def test_a_model_only_save_never_writes_back_a_changed_or_removed_key(self):
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        seen = self.store.load()
        self.store.save_provider({**seen, "api_key": KEY2}, "replace")
        self.assertFalse(self.store.update_model(seen, "m9", ""))
        self.assertEqual((self.saved()["api_key"], self.saved()["model"]), (KEY2, GOOD["model"]))
        now = self.store.load()
        self.store.remove()
        self.assertFalse(self.store.update_model(now, "m9", ""))
        self.assertIsNone(self.store.load())

    def test_each_save_mode_decides_and_writes_in_one_statement(self):
        a = {**GOOD, "api_key": KEY}
        self.assertTrue(self.store.save_provider(a, "create"))
        self.assertFalse(self.store.save_provider({**a, "api_key": KEY2}, "create"))
        self.assertFalse(self.store.save_provider({**a, "api_key": KEY2}, "same-key"))
        self.assertTrue(self.store.save_provider({**a, "model": "m5"}, "same-key"))
        self.assertTrue(self.store.save_provider({**a, "api_key": KEY2}, "replace"))
        self.assertEqual(self.saved()["api_key"], KEY2)

    def test_the_web_store_reads_what_python_wrote(self):
        # Both servers share the file: the schema and columns must match.
        import shutil
        import subprocess
        if not shutil.which("node"):
            self.skipTest("Node.js is required")
        self.store.save_provider({**GOOD, "api_key": KEY}, "replace")
        script = ("import('" + str(SERVER.parent / "web" / "lib" / "provider-store.ts") + "')"
                  ".then(async m => { const p = await m.loadSaved(); console.log(JSON.stringify(m.publicView(p))); })")
        out = subprocess.run(["node", "--disable-warning=ExperimentalWarning", "-e", script],
                             capture_output=True, text=True,
                             env={**os.environ, "DESIGN_SYSTEMS_CONFIG_DIR": str(self.config)})
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(json.loads(out.stdout.strip().splitlines()[-1]), GOOD)

    def raw_bytes(self):
        return b"".join(p.read_bytes() for p in self.config.iterdir() if p.is_file())

    def test_no_copy_of_a_removed_or_replaced_key_stays_in_the_files(self):
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY2})
        self.assertNotIn(KEY.encode(), self.raw_bytes())
        self.call("delete", "/api/provider")
        self.assertNotIn(KEY2.encode(), self.raw_bytes())

    def test_remove_and_a_checked_replacement_recover_a_damaged_file(self):
        self.config.mkdir(parents=True)
        db = self.config / "provider.db"
        db.write_text(("damaged %s " % KEY) * 300)
        (self.config / "provider.db-journal").write_text("old key %s" % KEY)
        h = self.call("delete", "/api/provider")
        self.assertEqual((h.status, h.json()["removed"], h.json()["source"]), (200, True, "none"))
        self.assertEqual(list(self.config.iterdir()), [])
        db.write_text(("damaged %s " % KEY) * 300)
        h = self.call("post", "/api/provider", {**GOOD, "api_key": KEY2})
        self.assertTrue(h.json()["ok"])
        self.assertEqual(self.saved()["api_key"], KEY2)
        db.write_text(("damaged %s " % KEY) * 300)
        h = self.call("post", "/api/provider", {**GOOD, "api_key": KEY2, "migrate": True})
        self.assertFalse(h.json()["ok"])

    def test_a_busy_database_is_never_deleted(self):
        import sqlite3
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        other = sqlite3.connect(self.config / "provider.db", isolation_level=None)
        other.execute("BEGIN EXCLUSIVE")
        try:
            h = self.call("post", "/api/provider", {**GOOD, "api_key": KEY2})
            self.assertEqual(h.status, 500)
            h = self.call("delete", "/api/provider")
            self.assertEqual(h.status, 500)
        finally:
            other.execute("ROLLBACK")
            other.close()
        self.assertEqual(self.saved()["api_key"], KEY)

    def test_an_unreadable_folder_is_reported_not_replaced_by_env(self):
        self.chat.env_cfg = {"api": "anthropic", "api_key": ENV_KEY, "model": "env"}
        self.call("post", "/api/provider", {**GOOD, "api_key": KEY})
        os.chmod(self.config, 0o000)
        try:
            cfg, source, error = self.store.resolve(self.chat.env_cfg)
        finally:
            os.chmod(self.config, 0o700)
        self.assertEqual((cfg, source), (None, "saved"))
        self.assertTrue(error)

    def test_delete_is_only_the_provider_route(self):
        handled, h = _send(self.routes, "delete", "/api/mcp")
        self.assertFalse(handled)
        h = Handler("/api/provider", headers={"origin": "https://evil.example"})
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertTrue(self.routes.handle_delete(h))
        self.assertEqual(h.status, 403)


if __name__ == "__main__":
    unittest.main()
