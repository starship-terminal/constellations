"""Xbox tokens resolve and use measured colour forms."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_file_parses_and_names_both_themes(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("core", doc)
        self.assertIn("light", doc)
        self.assertIn("dark", doc)
        self.assertEqual(doc["light"]["action"]["primary"]["$value"], "{core.color.lime}")
        self.assertEqual(doc["core"]["color"]["lime"]["$value"], "#9bf00b")
        self.assertEqual(doc["core"]["color"]["storeGreen"]["$value"], "#008746")


if __name__ == "__main__":
    unittest.main()
