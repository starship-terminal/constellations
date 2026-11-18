"""Rows tokens stay tied to the 2026-11-19 computed-style readings."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


class RowsTokens(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_measured_page_and_accent(self):
        light = self.data["light"]["color"]
        self.assertEqual(light["page"]["$value"], "#fbf9f0")
        self.assertEqual(light["ink"]["$value"], "#3a032d")
        self.assertEqual(light["accent"]["$value"], "#ffc800")

    def test_display_size(self):
        display = self.data["core"]["typography"]["display"]["$value"]
        self.assertEqual(display["fontSize"], "64px")
        self.assertEqual(display["fontWeight"], 600)
        self.assertEqual(display["fontFamily"], "{fontFamily.display}")
        self.assertIn("GT Flexa", self.data["core"]["fontFamily"]["display"]["$value"])

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if "source" not in node.get("$extensions", {}):
                    missing.append(path)
                return
            if isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, f"{path}.{key}" if path else key)

        walk(self.data, "")
        self.assertEqual(missing, [])

    def test_light_theme_only(self):
        self.assertEqual([theme["id"] for theme in self.data["$themes"]], ["light"])
        self.assertNotIn("dark", self.data)


if __name__ == "__main__":
    unittest.main()
