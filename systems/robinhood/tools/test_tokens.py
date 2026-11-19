"""Robinhood tokens resolve and the committed file matches a fresh read of itself."""
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
        self.assertEqual(doc["light"]["color"]["accent"]["$value"], "#CCFF00")
        self.assertEqual(doc["dark"]["color"]["accent"]["$value"], "#00C805")
        self.assertEqual(doc["dark"]["color"]["page"]["$value"], "#000000")
        for theme in ("light", "dark"):
            for role in ("page", "surface", "text", "muted", "accent", "border"):
                token = doc[theme]["color"][role]
                self.assertTrue(token["$extensions"]["source"])
                self.assertEqual(token["$extensions"]["evidence"], "Measured")


if __name__ == "__main__":
    unittest.main()
