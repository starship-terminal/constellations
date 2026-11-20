"""The Perplexity token file stays tied to the measured readings."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
READINGS = json.loads((ROOT / "raw" / "named-vars.json").read_text())


class TokensTest(unittest.TestCase):
    def test_themes_match_readings(self):
        pairs = [
            ("light", "appLight", "--bg-base", ("color", "bg", "base")),
            ("light", "appLight", "--fg-primary", ("color", "fg", "primary")),
            ("light", "appLight", "--accent-bg-strong", ("color", "accent", "bg", "strong")),
            ("dark", "appDark", "--bg-base", ("color", "bg", "base")),
            ("dark", "appDark", "--fg-primary", ("color", "fg", "primary")),
            ("dark", "appDark", "--accent-bg-strong", ("color", "accent", "bg", "strong")),
        ]
        for theme, reading, css, path in pairs:
            node = TOKENS[theme]
            for part in path:
                node = node[part]
            raw = READINGS[reading]["vals"][css]
            self.assertRegex(raw, r"^#[0-9a-f]{6}([0-9a-f]{2})?$", f"{reading} {css}")
            self.assertEqual(node["$value"], raw, f"{theme}.{'.'.join(path)} against {reading} {css}")
            self.assertIn(css, node["$extensions"]["source"])

    def test_radius_and_type_come_from_the_light_root(self):
        self.assertEqual(TOKENS["core"]["radius"]["8"]["$value"], "8px")
        self.assertEqual(TOKENS["core"]["radius"]["full"]["$value"], "9999px")
        hero = TOKENS["core"]["typography"]["hero"]["$value"]
        self.assertEqual(hero["fontSize"], "46px")
        self.assertEqual(hero["fontFamily"], "{font.family.display}")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
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
