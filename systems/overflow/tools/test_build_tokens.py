"""The Overflow token builder reproduces the committed tokens.json and keeps measured colours.

build_tokens.build() runs in memory; nothing here writes tokens.json. Run from the package tools
directory, which is how tools/package_tests.py calls it.
"""
import json
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
TOKENS = PKG / "tokens.json"
sys.path.insert(0, str(HERE))
import build_tokens  # noqa: E402


class BuildTokens(unittest.TestCase):
    def test_committed_file_is_what_the_builder_makes(self):
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.build())

    def test_the_browser_focus_ring_is_not_a_measured_brand_colour(self):
        data = json.loads(TOKENS.read_text())
        for token in (data["core"]["color"]["focus-ring"], data["light"]["focus"]["outline"]):
            self.assertEqual(token["$extensions"]["evidence"], "Observed")
            self.assertIn("default focus ring", token["$extensions"]["source"])

    def test_the_style_guide_says_the_ring_is_the_browsers(self):
        guide = (PKG / "style-guide.html").read_text()
        self.assertIn("Chromium's default focus ring", guide)
        self.assertIn("focus (Chromium's default ring, not Overflow's)", guide)

    def test_durations_are_typed_duration(self):
        for key, token in json.loads(TOKENS.read_text())["core"]["motion"].items():
            if str(token["$value"]).endswith("ms"):
                self.assertEqual(token["$type"], "duration", key)

    def test_measured_roles(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["light"]["background"]["action"]["$value"], "{color.ink}")
        self.assertEqual(data["core"]["color"]["ink"]["$value"], "#000000")
        self.assertEqual(data["light"]["background"]["app-action"]["$value"], "#0071db")
        self.assertEqual(data["light"]["background"]["auth-panel"]["$value"], "{color.auth-panel}")
        self.assertEqual(data["core"]["color"]["auth-panel"]["$value"], "#d6f3ff")
        self.assertNotIn("dark", data)
        self.assertIn("$extensions", data["light"]["text"]["primary"])


if __name__ == "__main__":
    unittest.main()
