"""Resend token file keeps the measured marketing page and accent."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_dark_page_and_accent(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["dark"]["surface"]["page"]["$value"], "#000000")
        self.assertEqual(data["dark"]["accent"]["$value"], "#ffffff")
        self.assertEqual(data["dark"]["text"]["primary"]["$value"], "#f0f0f0")
        self.assertEqual(data["dark"]["text"]["secondary"]["$value"], "#a1a4a5")
        self.assertNotIn("light", data)
        self.assertEqual(data["core"]["color"]["gray"]["12"]["$value"], "#f0f0f0")
        self.assertEqual(data["core"]["radius"]["2xl"]["$value"], "16px")


if __name__ == "__main__":
    unittest.main()
