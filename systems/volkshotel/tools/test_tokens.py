"""The Volkshotel token file names measured colours and resolves its aliases."""

import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parents[1] / "tokens.json"
SRC = "www.volkshotel.nl"


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_measured_colours(self):
        light = self.data["light"]
        self.assertEqual(light["background"]["page"]["$value"], "#ffffff")
        self.assertEqual(light["background"]["band"]["$value"], "#f1f1f1")
        self.assertEqual(light["background"]["inverse"]["$value"], "#000000")
        self.assertEqual(light["text"]["primary"]["$value"], "#000000")
        self.assertEqual(light["text"]["muted"]["$value"], "#717171")
        self.assertEqual(light["text"]["inverse"]["$value"], "#ffffff")
        self.assertEqual(light["border"]["card"]["$value"], "#d5d5d5")
        self.assertEqual(light["component"]["button"]["bg"]["$value"], "#ffffff")
        self.assertEqual(light["component"]["button-hover"]["bg"]["$value"], "#000000")

    def test_every_token_names_the_page(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source", "")
                if SRC not in source and "Derived" not in source:
                    missing.append(".".join(path))
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

    def test_square_corners(self):
        self.assertEqual(self.data["core"]["radius"]["none"]["$value"], "0px")


if __name__ == "__main__":
    unittest.main()
