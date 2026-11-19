"""Tango tokens keep the measured marketing page and the app accent."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_light_page_and_accent(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["light"]["surface"]["page"]["$value"], "#fafafa")
        self.assertEqual(data["light"]["accent"]["$value"], "#6f26d0")
        self.assertEqual(data["light"]["text"]["primary"]["$value"], "#383838")
        self.assertEqual(data["light"]["highlight"]["$value"], "#f9650f")
        self.assertNotIn("dark", data)
        self.assertEqual(data["core"]["radius"]["appControl"]["$value"], "10px")
        self.assertEqual(data["core"]["font"]["family"]["display"]["$value"], "Gelica, Arial, sans-serif")


if __name__ == "__main__":
    unittest.main()
