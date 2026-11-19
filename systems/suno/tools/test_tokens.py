"""Suno token checks. Run from the package tools directory by package_tests.py."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
RAW = json.loads((ROOT / "raw" / "root-vars.json").read_text())
VARS = RAW["rootVars"]


def value(node):
    return node["$value"]


class TokenTests(unittest.TestCase):
    def test_dark_page_matches_declared_and_computed_body(self):
        page = value(TOKENS["dark"]["color"]["bg"]["page"])
        self.assertEqual(page, VARS["--color-background-primary"])
        self.assertEqual(page, "#101012")
        self.assertEqual(RAW["body"]["backgroundColor"], "rgb(16, 16, 18)")

    def test_text_and_accent_match_custom_properties(self):
        self.assertEqual(value(TOKENS["dark"]["color"]["text"]["primary"]), VARS["--color-foreground-primary"])
        self.assertEqual(value(TOKENS["dark"]["color"]["accent"]["brand"]), VARS["--color-accent-brand"])
        self.assertEqual(value(TOKENS["dark"]["color"]["border"]["primary"]), VARS["--color-border-primary"])

    def test_light_declarations_match_on_light_names(self):
        light = TOKENS["light"]["color"]
        self.assertEqual(value(light["bg"]["page"]), VARS["--color-background-primary-light"])
        self.assertEqual(value(light["text"]["primary"]), VARS["--color-foreground-primary-on-light"])
        self.assertEqual(value(light["border"]["primary"]), VARS["--color-border-primary-on-light"])

    def test_every_token_names_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = (node.get("$extensions") or {}).get("source")
                if not source:
                    missing.append(".".join(path))
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, path + [key])

        walk(TOKENS, [])
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
