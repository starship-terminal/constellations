"""Shuttle token file keeps the measured dark page and tint."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_dark_page_and_accent(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["dark"]["surface"]["page"]["$value"], "#000000")
        self.assertEqual(data["dark"]["accent"]["$value"], "#0077ff")
        self.assertEqual(data["dark"]["text"]["primary"]["$value"], "#ffffff")
        self.assertEqual(data["dark"]["surface"]["raised"]["$value"], "#2c2c2e")
        self.assertNotIn("light", data)
        self.assertEqual(data["core"]["radius"]["md"]["$value"], "8px")
        self.assertEqual(data["core"]["radius"]["2xl"]["$value"], "24px")
        self.assertEqual(data["core"]["typography"]["display"]["$value"]["fontSize"], "62px")


if __name__ == "__main__":
    unittest.main()
