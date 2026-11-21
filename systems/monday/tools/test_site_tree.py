"""Checks for the 2026-11-22 monday.com public site tree. unittest so `make test` collects them."""

import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class SiteTreeTest(unittest.TestCase):
    def test_site_tree_dated_november_2026(self):
        text = (ROOT / "site-tree.md").read_text()
        self.assertIn("2026-11-22", text)
        self.assertIn("November 2026", text)
        self.assertIn("catalog.json was left alone", text)
        self.assertIn("webapps-manifest.json was left alone", text)

    def test_login_extracted_not_started(self):
        review = json.loads((ROOT / "login-review.json").read_text())
        self.assertEqual(review["login_extracted"], "not-started")
        self.assertFalse(review["signed_in"])
        self.assertFalse(review["wall"]["inputs"][0]["filled"])

    def test_required_shots(self):
        shots = ROOT / "screenshots"
        for name in (
            "home-light-1440.png",
            "pricing-light-1440.png",
            "login-empty-light-1440.png",
            "signup-empty-light-1440.png",
        ):
            self.assertTrue((shots / name).is_file(), name)

    def test_no_rate_limit_wall_in_screenshots(self):
        for path in (ROOT / "screenshots").glob("*.capture.json"):
            data = json.loads(path.read_text())
            title = data.get("title") or ""
            self.assertNotIn("Suspicious activity", title)
            url = data.get("finalUrl") or data.get("url") or ""
            self.assertNotIn("oauth", url.lower())


if __name__ == "__main__":
    unittest.main()
