"""Visitors tokens match the public-page readings."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Measured(unittest.TestCase):
    def test_accent_is_the_trial_button(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        accent = tokens["core"]["color"]["accent"]
        self.assertEqual(accent["$value"], "#918df6")
        self.assertIn("Start 14 day free trial", accent["$extensions"]["source"])
        self.assertNotIn("dark", tokens)

    def test_css_vars_match_the_ink(self):
        raw = json.loads((ROOT / "raw" / "css-vars.json").read_text())
        self.assertEqual(raw["vars"]["--fg-4"], "#181925")
        self.assertEqual(raw["vars"]["--purple-4"], "#918df6")
        self.assertEqual(raw["vars"]["--background"], "#fff")

    def test_login_was_not_submitted(self):
        pages = json.loads((ROOT / "raw" / "pages.json").read_text())
        login = next(p for p in pages if p["url"].endswith("/login"))
        self.assertEqual(login["status"], 200)
        self.assertFalse(login["challenge"])
        kinds = [i["type"] for i in login["inputs"]]
        self.assertIn("email", kinds)
        self.assertIn("hidden", kinds)

    def test_home_screenshot_exists(self):
        shot = ROOT / "screenshots" / "home-light-default.png"
        self.assertTrue(shot.is_file())
        # A checkout with LFS smudge skipped (CI) holds the pointer, not the image.
        with shot.open("rb") as f:
            if f.read(64).startswith(b"version https://git-lfs.github.com/spec/v1"):
                self.skipTest("screenshot is an unpulled Git LFS pointer")
        self.assertGreater(shot.stat().st_size, 1000)


if __name__ == "__main__":
    unittest.main()
