"""Tango tokens keep the measured marketing page and the app accent."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        # Built in memory; the committed file is never rewritten by the test.
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.build())

    def test_declared_values_absent_from_raw_are_labelled_by_hand(self):
        doc = build_tokens.build()
        for path in (("core", "color", "purple", "700"), ("core", "color", "border"), ("light", "status", "error"),
                     ("core", "motion", "navDropdown")):
            node = doc
            for key in path:
                node = node[key]
            self.assertTrue(node["$extensions"]["source"].startswith("Reconstruction: entered by hand"), path)
        self.assertEqual(doc["core"]["motion"]["navDropdown"]["$type"], "duration")
        self.assertNotIn("buttonToken", doc["core"]["radius"])

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
