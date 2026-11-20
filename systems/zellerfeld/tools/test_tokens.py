#!/usr/bin/env python3
"""The committed tokens match the readings this capture wrote down."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def value(path):
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return node["$value"]


class Tokens(unittest.TestCase):
    def test_primary_is_the_measured_coral(self):
        self.assertEqual(value("dark.accent"), "#ff5e3e")
        self.assertEqual(value("dark.accent-foreground"), "#000000")

    def test_page_is_the_painted_black(self):
        self.assertEqual(value("dark.page"), "#000000")
        self.assertEqual(value("dark.surface"), "#171717")

    def test_button_radius_is_4px(self):
        self.assertEqual(value("core.radius.sm"), "4px")
        self.assertEqual(value("dark.component.button-primary.radius"), "4px")

    def test_type_styles_use_measured_sizes(self):
        self.assertEqual(value("core.typography.page-title")["fontSize"], "72px")
        self.assertEqual(value("core.typography.button")["fontSize"], "14px")
        self.assertEqual(value("core.typography.button")["letterSpacing"], "-0.14px")

    def test_every_token_names_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, path + [key])

        walk(TOKENS, [])
        self.assertEqual(missing, [])

    def test_style_guide_exists(self):
        text = (HERE / "style-guide.html").read_text()
        self.assertIn("#ff5e3e", text)
        self.assertIn("Zellerfeld", text)


if __name__ == "__main__":
    unittest.main()
