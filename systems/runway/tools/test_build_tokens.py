"""tokens.json is hand-written from this capture (there is no builder): every token says it was
Measured, and the measured roles keep their values."""
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

    def test_page_and_accent_are_measured(self):
        light = self.data["light"]
        self.assertEqual(light["background"]["page"]["$value"], "#ffffff")
        self.assertEqual(light["background"]["inverse"]["$value"], "#0c0c0c")
        self.assertEqual(light["background"]["accent"]["$value"], "#2b22fa")
        self.assertEqual(light["text"]["primary"]["$value"], "#0c0c0c")
        self.assertEqual(light["text"]["secondary"]["$value"], "#404040")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if not isinstance(node, dict):
                return
            if "$value" in node:
                source = (node.get("$extensions") or {}).get("source", "")
                if "Measured" not in source:
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
