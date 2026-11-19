"""Polar token file keeps the measured marketing accent and page."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_dark_page_and_accent(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["dark"]["surface"]["page"]["$value"], "#181818")
        self.assertEqual(data["dark"]["accent"]["$value"], "#155dfc")
        self.assertEqual(data["light"]["surface"]["page"]["$value"], "#ffffff")
        self.assertEqual(data["core"]["color"]["polar"]["950"]["$value"], "#090909")


if __name__ == "__main__":
    unittest.main()
