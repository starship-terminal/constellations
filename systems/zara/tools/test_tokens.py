"""The token file matches the raw readings."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_page_is_white(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["color"]["bg"]["page"]["$value"], "#ffffff")
        self.assertEqual(tokens["light"]["color"]["text"]["primary"]["$value"], "#000000")
        self.assertEqual(tokens["core"]["radius"]["none"]["$value"], "0px")
        self.assertIn("source", tokens["light"]["action"]["primary"]["$extensions"])

    def test_no_dark_set(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertNotIn("dark", tokens)


if __name__ == "__main__":
    unittest.main()
