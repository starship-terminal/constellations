#!/usr/bin/env python3
"""The package's tokens stay tied to the computed readings in raw/computed.json."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
RAW = json.loads((PKG / "raw" / "computed.json").read_text())


def flat(node, prefix=""):
    out = {}
    if isinstance(node, dict) and "$value" in node:
        out[prefix] = node
        return out
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            path = f"{prefix}.{key}" if prefix else key
            out.update(flat(value, path))
    return out


class TokensMatchReadings(unittest.TestCase):
    def test_home_page_and_ink(self):
        self.assertEqual(TOKENS["light"]["background"]["page"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["light"]["background"]["ink"]["$value"], "#000000")
        self.assertEqual(RAW["pages"]["home"]["body"]["backgroundColor"], "rgb(255, 255, 255)")

    def test_display_size_matches_h2(self):
        size = TOKENS["core"]["typography"]["display"]["$value"]["fontSize"]
        self.assertEqual(size, "64px")
        self.assertIn("64px", RAW["pages"]["home"]["display"]["fontSize"])

    def test_login_field_fill(self):
        self.assertEqual(TOKENS["light"]["background"]["field-login"]["$value"], "#edf2f7")
        self.assertEqual(RAW["pages"]["login"]["field"]["backgroundColor"], "rgb(237, 242, 247)")

    def test_every_token_names_a_source(self):
        missing = [path for path, token in flat(TOKENS).items() if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_no_dark_theme_was_invented(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([theme["id"] for theme in TOKENS["$themes"]], ["light"])


if __name__ == "__main__":
    unittest.main()
