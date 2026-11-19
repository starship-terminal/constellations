"""Stellate token file keeps the measured marketing page and accent."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_light_page_and_accent(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["light"]["surface"]["page"]["$value"], "#f8fafc")
        self.assertEqual(data["light"]["accent"]["$value"], "#608bd8")
        self.assertEqual(data["light"]["text"]["primary"]["$value"], "#283448")
        self.assertEqual(data["light"]["text"]["secondary"]["$value"], "#3b4c6a")
        self.assertEqual(data["dark"]["surface"]["page"]["$value"], "#18181b")
        self.assertEqual(data["dark"]["accent"]["$value"], "#1aa3ff")
        self.assertEqual(data["core"]["radius"]["lg"]["$value"], "8px")
        self.assertIn("ttCommons", data["core"]["font"]["family"]["sans"]["$value"])


if __name__ == "__main__":
    unittest.main()
