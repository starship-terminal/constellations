"""Tokens in this package resolve and match the readings they cite."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
READINGS = json.loads((ROOT / "raw" / "readings.json").read_text())


class Tokens(unittest.TestCase):
    def test_marketing_accent_is_the_computed_cta(self):
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#0061fe")
        bg = READINGS["pages"]["https://reclaim.ai/"]["getStarted"]["backgroundColor"]
        self.assertEqual(bg, "rgb(0, 97, 254)")

    def test_login_page_is_the_dark_field(self):
        self.assertEqual(TOKENS["dark"]["page"]["$value"], "#171d26")
        self.assertEqual(
            READINGS["pages"]["https://app.reclaim.ai/login"]["body"]["backgroundColor"],
            "rgb(23, 29, 38)",
        )

    def test_radius_control_matches_the_nav_button(self):
        self.assertEqual(TOKENS["core"]["radius"]["control"]["$value"], "10px")
        self.assertEqual(
            READINGS["pages"]["https://reclaim.ai/"]["getStarted"]["borderRadius"],
            "10px",
        )

    def test_signup_was_not_entered(self):
        self.assertEqual(READINGS["pages"]["https://app.reclaim.ai/login"]["entered"], "nothing")
        self.assertIn("No email field", READINGS["pages"]["https://app.reclaim.ai/login"]["text"])


if __name__ == "__main__":
    unittest.main()
