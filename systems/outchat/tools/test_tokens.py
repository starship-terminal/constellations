#!/usr/bin/env python3
"""Outchat: every token has a source, and the measured marketing colours match."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def walk(node, path=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        here = f"{path}.{key}" if path else key
        if isinstance(value, dict) and "$value" in value:
            yield here, value
        elif isinstance(value, dict):
            yield from walk(value, here)


class TokensTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = [path for path, token in walk(TOKENS) if not token.get("$extensions", {}).get("source")]
        self.assertEqual(missing, [])

    def test_marketing_action_and_page(self):
        self.assertEqual(TOKENS["light"]["background"]["page"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["light"]["background"]["action"]["$value"], "#000000")
        self.assertEqual(TOKENS["light"]["text"]["primary"]["$value"], "#000000")
        self.assertEqual(TOKENS["light"]["text"]["on-action"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$value"], "9999px")
        self.assertEqual(TOKENS["core"]["font"]["size"]["hero"]["$value"], "60px")

    def test_app_tokens_are_canvas_resolved(self):
        self.assertEqual(TOKENS["light"]["app"]["primary"]["$value"], "#171717")
        self.assertEqual(TOKENS["light"]["app"]["background"]["$value"], "#ffffff")
        self.assertNotIn("dark", TOKENS)


if __name__ == "__main__":
    unittest.main()
