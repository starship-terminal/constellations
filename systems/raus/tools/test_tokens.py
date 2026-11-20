"""The Raus token file names measured colours and resolves its aliases."""

import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parents[1] / "tokens.json"
SRC = "www.raus.life, computed style, 2026-11-19"


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_measured_colours(self):
        light = self.data["light"]
        self.assertEqual(light["surface"]["page"]["$value"], "#fdf9ed")
        self.assertEqual(light["text"]["primary"]["$value"], "#23212c")
        self.assertEqual(light["text"]["forest"]["$value"], "#006434")
        self.assertEqual(light["action"]["orange"]["$value"], "#dd5000")
        self.assertEqual(light["action"]["ink"]["$value"], "#23212c")
        self.assertEqual(light["surface"]["promo"]["$value"], "#a6dfff")
        self.assertEqual(light["surface"]["search"]["$value"], "#fcbd1c")
        self.assertEqual(light["action"]["magenta"]["$value"], "#b218a4")
        self.assertEqual(light["action"]["filters"]["$value"], "#bdda0e")

    def test_every_token_names_the_page(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source", "")
                if SRC not in source:
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, path + [key])

        walk(self.data["core"], ["core"])
        walk(self.data["light"], ["light"])
        self.assertEqual(missing, [])

    def test_themes_are_light_only(self):
        self.assertEqual([t["name"] for t in self.data["$themes"]], ["light"])
        self.assertNotIn("dark", self.data)


if __name__ == "__main__":
    unittest.main()
