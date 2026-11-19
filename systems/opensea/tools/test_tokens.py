#!/usr/bin/env python3
"""OpenSea package: every token has a source, and the probe colours match."""
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

    def test_dark_page_and_accent_match_the_probe(self):
        self.assertEqual(TOKENS["dark"]["page"]["$value"], "#080808")
        self.assertEqual(TOKENS["dark"]["surface"]["$value"], "#0c0c0c")
        self.assertEqual(TOKENS["dark"]["text"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["dark"]["muted"]["$value"], "#acacac")
        self.assertEqual(TOKENS["dark"]["accent"]["$value"], "#0086ff")
        self.assertEqual(TOKENS["dark"]["border"]["$value"], "#202020")

    def test_light_pair_matches_the_probe(self):
        self.assertEqual(TOKENS["light"]["page"]["$value"], "#fafafa")
        self.assertEqual(TOKENS["light"]["text"]["$value"], "#171717")
        self.assertEqual(TOKENS["light"]["muted"]["$value"], "#666666")
        self.assertEqual(TOKENS["light"]["link"] if False else TOKENS["light"]["foreground"]["link"]["$value"], "#0086ff")

    def test_raw_pairs_cover_both_themes(self):
        self.assertGreaterEqual(len(RAW["colors"]), 30)
        for name, pair in RAW["colors"].items():
            if name == "frosted":
                continue
            self.assertIn("dark", pair, name)
            self.assertIn("light", pair, name)

    def test_focus_ring_is_the_measured_blue(self):
        self.assertEqual(TOKENS["core"]["color"]["focus"]["$value"], "#99c8ff")
        self.assertEqual(RAW["focus"]["input-focus-outline"], "none 1px #99c8ff")


if __name__ == "__main__":
    unittest.main()
