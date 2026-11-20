"""Wealthsimple tokens resolve and match the 2026-11-19 computed readings."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_file_loads_and_themes_match_shape(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("core", doc)
        self.assertIn("light", doc)
        self.assertIn("dark", doc)
        self.assertEqual(doc["light"]["color"]["page"]["$value"], "#FCFCFC")
        self.assertEqual(doc["light"]["color"]["text"]["$value"], "#1C1B1B")
        self.assertEqual(doc["dark"]["color"]["page"]["$value"], "#0D0D0D")
        self.assertEqual(doc["dark"]["color"]["accent"]["$value"], "#6DC382")
        self.assertEqual(doc["core"]["radius"]["pill"]["$value"], "1000px")
        self.assertEqual(doc["core"]["size"]["login-button-height"]["$value"], "54px")
        for theme in ("light", "dark"):
            for role in ("page", "surface", "text", "muted", "accent", "border"):
                token = doc[theme]["color"][role]
                self.assertTrue(token["$extensions"]["source"])
                self.assertEqual(token["$extensions"]["evidence"], "Measured")


if __name__ == "__main__":
    unittest.main()
