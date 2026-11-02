"""Tests for tools/agent (library tools and the chat adapters). Run with `make test`."""
import importlib.util
import json
import os
import unittest
from pathlib import Path


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parent / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


library = _load("agent_library", "agent/library.py")
chat = _load("agent_chat", "agent/chat.py")


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
        self.assertTrue(item["url"].startswith("/systems/"))
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
        self.assertEqual(roles, ["system", "user", "assistant", "tool", "tool"])
        tool = msgs[4]
        self.assertEqual(tool["tool_call_id"], "c2")
        self.assertEqual(tool["content"][1]["type"], "image_url")


class McpTest(unittest.TestCase):
    mcp = _load("agent_mcp", "agent/mcp.py")

    def _roundtrip(self, *reqs):
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            for r in reqs:
                self.mcp.handle(r)
        return [json.loads(l) for l in buf.getvalue().splitlines() if l.strip()]

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


if __name__ == "__main__":
    unittest.main()
