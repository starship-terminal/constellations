"""The Pryzm token file matches the measured record."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
MEASURED = json.loads((ROOT / "raw" / "measured.json").read_text())


class Measured(unittest.TestCase):
    def test_dark_primary_is_the_declared_hex(self):
        self.assertEqual(TOKENS["dark"]["accent"]["$value"], "#e5e5e5")
        self.assertEqual(MEASURED["declaredDarkHex"]["--primary"], "#e5e5e5")

    def test_page_is_black(self):
        self.assertEqual(TOKENS["dark"]["page"]["$value"], "#000000")
        self.assertEqual(MEASURED["themeOnScreen"], "dark")

    def test_hero_size_matches_the_1169_reading(self):
        hero = TOKENS["core"]["typography"]["hero"]["$value"]
        self.assertEqual(hero["fontSize"], "48px")
        self.assertEqual(hero["letterSpacing"], "-0.96px")
        self.assertEqual(MEASURED["elements"]["h1HomeAt1169"]["fontSize"], "48px")

    def test_control_radius_is_8px(self):
        self.assertEqual(TOKENS["core"]["radius"]["control"]["$value"], "8px")

    def test_reduced_motion_is_recorded_as_ignored(self):
        self.assertEqual(TOKENS["core"]["motion"]["$extensions"]["reducedMotion"], "ignores")
        self.assertIn("ignores", MEASURED["motion"]["reducedMotion"])

    def test_light_hex_is_evidence_not_a_theme_set(self):
        self.assertNotIn("light", TOKENS)
        self.assertEqual(MEASURED["declaredLightHex"]["--background"], "#fff")


if __name__ == "__main__":
    unittest.main()
