"""Wix public capture records a dated site tree and leaves login unstarted."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicCaptureTest(unittest.TestCase):
    def test_site_tree_is_dated(self):
        text = (ROOT / "site-tree.md").read_text()
        self.assertIn("2026-11-22", text)
        self.assertIn("November 2026", text)
        self.assertIn("https://users.wix.com/signin", text)
        self.assertIn("catalog.json", text)
        self.assertIn("login-extracted", text)
        self.assertIn("webapps-manifest.json", text)

    def test_login_review_not_started(self):
        data = json.loads((ROOT / "login-review.json").read_text())
        self.assertEqual(data["loginExtracted"], "not-started")
        self.assertFalse(data["typed"])
        self.assertFalse(data["submitted"])
        self.assertFalse(data["identityProviderClicked"])
        self.assertFalse(data["editorStarted"])

    def test_home_shot_exists(self):
        shot = ROOT / "screenshots" / "home-light-1440.png"
        self.assertTrue(shot.exists())
        sidecar = json.loads(shot.with_name(shot.name + ".capture.json").read_text())
        self.assertEqual(sidecar["metrics"]["innerWidth"], 1440)
        self.assertIsNone(sidecar["discarded"])


if __name__ == "__main__":
    unittest.main()
