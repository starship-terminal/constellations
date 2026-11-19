#!/usr/bin/env python3
"""Rarible package: every token has a source, and the live colours match the probe."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
RAW = json.loads((ROOT / "raw" / "css-vars.json").read_text())


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

    def test_dark_matches_the_live_page(self):
        self.assertEqual(TOKENS["dark"]["page"]["$value"], "#0a0a0a")
        self.assertEqual(TOKENS["dark"]["surface"]["$value"], "#09090b")
        self.assertEqual(TOKENS["dark"]["text"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["dark"]["accent"]["$value"], "#faff00")
        self.assertEqual(TOKENS["dark"]["border"]["$value"], "#27272a")
        self.assertEqual(TOKENS["dark"]["on-accent"]["$value"], "#18181b")
        self.assertEqual(RAW["colors"]["dark"]["--brand"]["painted"], "#faff00")
        self.assertEqual(RAW["components"]["login"]["backgroundColor"], "rgb(250, 255, 0)")

    def test_light_matches_the_root_declaration(self):
        self.assertEqual(TOKENS["light"]["page"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["light"]["text"]["$value"], "#0a0a0a")
        self.assertEqual(TOKENS["light"]["muted"]["$value"], "#71717a")
        self.assertEqual(TOKENS["light"]["border"]["$value"], "#e4e4e7")
        self.assertEqual(RAW["colors"]["light"]["--background"]["painted"], "#ffffff")

    def test_type_and_radius_are_measured(self):
        self.assertEqual(TOKENS["core"]["typography"]["display"]["$value"]["fontSize"], "40px")
        self.assertEqual(TOKENS["core"]["typography"]["body"]["$value"]["fontSize"], "14px")
        self.assertEqual(TOKENS["core"]["radius"]["full"]["$value"], "9999px")
        self.assertIn("Geist Mono", TOKENS["core"]["font"]["sans"]["$value"])


if __name__ == "__main__":
    unittest.main()
