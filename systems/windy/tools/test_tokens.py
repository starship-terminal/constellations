#!/usr/bin/env python3
"""The Windy token file matches the readings it claims to come from."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
VARS = json.loads((HERE / "raw" / "css-vars.json").read_text())


def value(set_name, *path):
    node = TOKENS[set_name]
    for part in path:
        node = node[part]
    return node["$value"]


class Tokens(unittest.TestCase):
    def test_primitives_match_root(self):
        root = VARS["root"]
        pairs = {
            "red": "--color-red",
            "orange": "--color-orange",
            "white": "--color-white",
            "black": "--color-black",
            "gray": "--color-gray",
            "error": "--color-error",
            "ok": "--color-ok",
        }
        for name, var in pairs.items():
            self.assertEqual(value("core", "color", name), root[var])

    def test_light_aliases_match_root_bindings(self):
        self.assertEqual(value("light", "text", "primary"), "{color.gray}")
        self.assertEqual(value("light", "background", "page"), "{color.white}")
        self.assertEqual(value("light", "border", "stroke"), "{color.gray-light-2}")

    def test_dark_aliases_match_dark_content(self):
        self.assertEqual(value("dark", "text", "primary"), "{color.gray-light}")
        self.assertEqual(value("dark", "text", "secondary"), "{color.yellow}")
        self.assertEqual(value("dark", "background", "page"), "{color.black}")
        self.assertEqual(value("dark", "border", "selected"), "{color.orange-light}")

    def test_search_height_is_the_measured_field(self):
        self.assertEqual(value("light", "component", "search", "height"), "33px")

    def test_every_token_has_a_source(self):
        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                self.assertTrue(node.get("$extensions", {}).get("source"), node)
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        walk(v)
        walk(TOKENS)


if __name__ == "__main__":
    unittest.main()
