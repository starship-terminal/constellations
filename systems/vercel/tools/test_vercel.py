"""Checks for the 2026-11-21 public refresh. Login stays not-started."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


class PublicRefresh(unittest.TestCase):
    def test_public_shots_exist(self):
        shots = list((HERE / "screenshots").glob("*.png"))
        names = {p.name for p in shots}
        self.assertIn("home-light-desktop.png", names)
        self.assertIn("home-dark-desktop.png", names)
        self.assertIn("login-light-desktop.png", names)
        self.assertIn("signup-light-desktop.png", names)
        self.assertIn("home-light-phone.png", names)
        self.assertIn("pricing-light-phone.png", names)
        for shot in shots:
            self.assertFalse(shot.read_bytes().startswith(b"version https://git-lfs"), shot.name)

    def test_login_was_not_entered(self):
        notes = (HERE / "README.md").read_text() + (HERE / "site-tree.md").read_text()
        self.assertIn("not-started", notes)
        self.assertNotIn("signed_in", notes)
        self.assertNotRegex(notes, r"https://vercel.com/[A-Za-z0-9_-]{3,}/dashboard")

    def test_light_and_dark_pages(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["surface"]["page"]["$value"], "#fafafa")
        self.assertEqual(tokens["dark"]["surface"]["page"]["$value"], "#000000")
        self.assertEqual(tokens["light"]["text"]["primary"]["$value"], "#171717")
        self.assertEqual(tokens["dark"]["text"]["primary"]["$value"], "#ededed")

    def test_no_account_literal(self):
        text = ""
        for rel in (
            "README.md",
            "site-tree.md",
            "components.md",
            "patterns.md",
            "tokens.json",
            "raw/public-2026-11-21.json",
            "raw/dark-2026-11-21.json",
            "raw/capture.json",
        ):
            text += (HERE / rel).read_text()
        self.assertNotIn("sk_", text)
        self.assertNotRegex(text, r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")


if __name__ == "__main__":
    unittest.main()
