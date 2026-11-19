"""The Miro token file matches the pricing-page readings."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((ROOT / "tokens.json").read_text())
        self.raw = json.loads((ROOT / "raw" / "pricing-root-vars.json").read_text())

    def test_light_roles_match_measured_colours(self):
        light = self.tokens["light"]
        self.assertEqual(light["page"]["$value"], "#fafafc")
        self.assertEqual(light["surface"]["$value"], "#ffffff")
        self.assertEqual(light["text"]["$value"], "#1c1c1e")
        self.assertEqual(light["textMuted"]["$value"], "#555a6a")
        self.assertEqual(light["accent"]["$value"], "#3859ff")
        self.assertEqual(light["border"]["$value"], "#c7cad5")

    def test_accent_comes_from_the_pricing_button_token(self):
        self.assertEqual(self.raw["variables"]["--button-primary-bg-btn-primary-idle"], "#3859ff")
        self.assertIn("--button-primary-bg-btn-primary-idle", self.tokens["light"]["accent"]["$extensions"]["source"])

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if not key.startswith("$"):
                        walk(value, path + "." + key)

        walk(self.tokens, "")
        self.assertEqual(missing, [])

    def test_no_dark_set(self):
        self.assertNotIn("dark", self.tokens)


if __name__ == "__main__":
    unittest.main()
