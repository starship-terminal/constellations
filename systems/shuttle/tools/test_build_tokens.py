"""Shuttle token file keeps the measured dark page and tint."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        # Built in memory; the committed file is never rewritten by the test.
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.build())

    def test_translucent_readings_keep_their_alpha(self):
        dark = build_tokens.build()["dark"]
        self.assertEqual(dark["border"]["hairline"]["$value"], "#ffffff33")  # rgba(255, 255, 255, 0.2)
        self.assertEqual(dark["text"]["muted"]["$value"], "#ebebf599")  # rgba(235, 235, 245, 0.6)

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
