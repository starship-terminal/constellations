"""The public Revolut readings survive the token build."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_light_accent_is_the_home_page_value(self):
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#234fa6")

    def test_dark_accent_is_the_pricing_page_value(self):
        self.assertEqual(TOKENS["dark"]["accent"]["$value"], "#6fa0ff")

    def test_page_and_text_roles(self):
        self.assertEqual(TOKENS["light"]["background"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["light"]["foreground"]["$value"], "#1f1f1f")
        self.assertEqual(TOKENS["dark"]["background"]["$value"], "#000000")
        self.assertEqual(TOKENS["dark"]["foreground"]["$value"], "#ffffff")

    def test_radius_round_is_the_pill(self):
        self.assertEqual(TOKENS["core"]["radius"]["round"]["$value"], "9999px")

    def test_every_token_names_its_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                src = node.get("$extensions", {}).get("source")
                if not src:
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, path + "." + key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        walk(TOKENS["dark"], "dark")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
