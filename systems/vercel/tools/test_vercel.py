"""Checks for the 2026-11-21 signed-in walk. Public tokens stay as they were."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


class SignedInWalk(unittest.TestCase):
    def test_review_names_two_screens(self):
        review = json.loads((HERE / "login-review.json").read_text())
        self.assertTrue(review["signed_in"])
        self.assertGreaterEqual(len(review["screens"]), 2)
        for screen in review["screens"]:
            self.assertTrue((HERE / screen["file"]).is_file(), screen["file"])

    def test_create_menu_was_not_submitted(self):
        review = json.loads((HERE / "login-review.json").read_text())
        self.assertTrue(review["offered"]["create"]["reached"])
        self.assertFalse(review["offered"]["create"]["submitted"])
        self.assertIn("Project", review["offered"]["create"]["items"])
        self.assertTrue(review["not_submitted"])

    def test_public_tokens_stay(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(tokens["dark"]["surface"]["page"]["$value"], "#000000")
        self.assertEqual(tokens["dark"]["text"]["primary"]["$value"], "#ededed")
        self.assertNotIn("light", tokens)

    def test_no_secret_literal_in_notes(self):
        text = (HERE / "login-review.json").read_text() + (HERE / "README.md").read_text()
        self.assertNotIn("sk_", text)
        self.assertNotRegex(text, r"team_[A-Za-z0-9]{8,}")
        self.assertNotRegex(text, r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")


if __name__ == "__main__":
    unittest.main()
