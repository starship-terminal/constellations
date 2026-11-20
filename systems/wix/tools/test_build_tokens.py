"""The Wix token builder writes only values that are in the readings."""
import json
import unittest
from pathlib import Path

import build_tokens

ROOT = Path(__file__).resolve().parent.parent


class BuildTokens(unittest.TestCase):
    def test_rebuild_matches_file(self):
        built = build_tokens.build()
        saved = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(built, saved)

    def test_header_cta_is_the_painted_blue(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["action"]["header"]["$value"], "#166aea")
        self.assertIn("22, 106, 234", tokens["light"]["action"]["header"]["$extensions"]["source"])

    def test_no_dark_set(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertNotIn("dark", tokens)
        notes = tokens["core"]["$extensions"]["notTokenised"]
        self.assertTrue(any("Dark theme" in note for note in notes))

    def test_login_was_not_submitted(self):
        readings = json.loads((ROOT / "raw" / "readings.json").read_text())
        self.assertFalse(readings["pages"]["login"]["submitted"])


if __name__ == "__main__":
    unittest.main()
