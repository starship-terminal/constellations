#!/usr/bin/env python3
"""Medium package: every colour token has a source, and the measured pairs match."""
import json, pathlib, unittest

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

    def test_light_page_and_accent_match_the_probe(self):
        self.assertEqual(TOKENS["light"]["background"]["neutral"]["primary"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["dark"]["background"]["neutral"]["primary"]["$value"], "#171717")
        self.assertEqual(TOKENS["light"]["foreground"]["accent"]["primary"]["$value"], "#1a8917")
        self.assertEqual(TOKENS["dark"]["foreground"]["accent"]["primary"]["$value"], "#6ab668")

    def test_raw_pairs_are_complete(self):
        self.assertGreaterEqual(len(RAW["colors"]), 70)
        for name, pair in RAW["colors"].items():
            self.assertIn("light", pair)
            self.assertIn("dark", pair)


if __name__ == "__main__":
    unittest.main()
