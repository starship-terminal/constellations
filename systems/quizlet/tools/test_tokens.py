"""Quizlet tokens trace to the readings dump."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
READINGS = json.loads((ROOT / "raw" / "readings.json").read_text())


class TokensTest(unittest.TestCase):
    def test_primary_matches_computed_login(self):
        self.assertEqual(TOKENS["core"]["color"]["twilight"]["500"]["$value"], "#4255ff")
        self.assertIn("66, 85, 255", READINGS["computed"]["loginButton"]["backgroundColor"])

    def test_page_matches_body(self):
        self.assertEqual(TOKENS["core"]["color"]["gray"]["200"]["$value"], "#f6f7fb")
        self.assertIn("246, 247, 251", READINGS["computed"]["body"]["backgroundColor"])

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = (node.get("$extensions") or {}).get("source")
                if not source:
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, path + "." + key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        walk(TOKENS["dark"], "dark")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
