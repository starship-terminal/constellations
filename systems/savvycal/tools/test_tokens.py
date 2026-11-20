"""tokens.json keeps the measured page and accent colours, and every token carries a source label."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


class Tokens(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_light_only(self):
        self.assertIn("light", self.data)
        self.assertNotIn("dark", self.data)
        self.assertEqual(self.data["$themes"][0]["id"], "light")

    def test_page_and_accent_values(self):
        light = self.data["light"]["color"]
        self.assertEqual(light["page"]["$value"], "#fcf7ed")
        self.assertEqual(light["accent"]["$value"], "#f54320")
        self.assertEqual(light["neon"]["$value"], "#b9ff78")
        self.assertEqual(light["ink"]["$value"], "#0c0c09")
        self.assertEqual(light["surface"]["$value"], "#ffffff")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if not isinstance(node, dict):
                return
            if "$value" in node:
                source = (node.get("$extensions") or {}).get("source", "")
                if "Measured" not in source and "Derived" not in source and "Sampled" not in source and "Declared" not in source:
                    missing.append(".".join(path))
                return
            for key, child in node.items():
                if not key.startswith("$"):
                    walk(child, path + [key])

        walk(self.data["core"], ["core"])
        walk(self.data["light"], ["light"])
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
