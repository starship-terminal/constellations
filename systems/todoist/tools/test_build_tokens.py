"""tokens.json matches a fresh build from raw/readings.json."""
import json
import unittest
from pathlib import Path

import build_tokens

HERE = Path(__file__).resolve().parent.parent


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_the_builder(self):
        committed = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(committed, build_tokens.document())
        self.assertEqual(committed["light"]["background"]["action"]["$value"], "#e34432")
        self.assertIn("oklch(61.47% .1986 30.12)", committed["light"]["background"]["action"]["$extensions"]["source"])
        self.assertEqual(committed["light"]["brand"]["app-action"]["$value"], "#d33322")
        self.assertTrue(committed["core"]["typography"]["display"]["$extensions"]["source"])

    def test_oklch_conversion_matches_a_painted_reading(self):
        # --greyopaque-900 is oklch(25.38% .0086 75.21); the home body computed rgb(37, 34, 30).
        self.assertEqual(build_tokens.oklch_hex("oklch(25.38% .0086 75.21)"), "#25221e")
        self.assertEqual(build_tokens.oklch_hex("oklch(25.38% .0086 75.21/.07)"), "#25221e12")
        with self.assertRaises(ValueError):
            build_tokens.oklch_hex("oklch(70% .4 150)")  # outside sRGB

    def test_readings_name_the_pages(self):
        raw = json.loads((HERE / "raw" / "readings.json").read_text())
        self.assertEqual(raw["pages"]["login"]["url"], "https://app.todoist.com/auth/login?locale=en")
        self.assertFalse(raw["pages"]["signup"]["entered"])


if __name__ == "__main__":
    unittest.main()
