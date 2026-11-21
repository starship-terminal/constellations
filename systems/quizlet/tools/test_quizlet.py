"""Package checks that do not need a catalog.json edit."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class QuizletPackage(unittest.TestCase):
    def test_public_review_stops_at_empty_walls(self):
        review = json.loads((HERE / "login-review.json").read_text())
        self.assertEqual(review["login_extracted"], "not-started")
        self.assertFalse(review["signed_in"])
        self.assertGreaterEqual(len(review["screens"]), 2)
        for screen in review["screens"]:
            self.assertTrue((HERE / screen["file"]).is_file(), screen["file"])
        for stop in ("nav", "create", "walls"):
            item = review["offered"][stop]
            self.assertTrue(item["items"])
            self.assertIsInstance(item["reached"], list)
        self.assertTrue(review["gaps"])
        self.assertTrue(review["not_submitted"])
        self.assertIn("catalog.json", " ".join(review["gaps"]))

    def test_tokens_round_trip(self):
        import subprocess
        import sys
        before = (HERE / "tokens.json").read_text()
        subprocess.check_call([sys.executable, str(HERE / "tools" / "build_tokens.py")])
        self.assertEqual(before, (HERE / "tokens.json").read_text())

    def test_no_email_in_notes(self):
        notes = [
            HERE / "README.md",
            HERE / "DESIGN.md",
            HERE / "components.md",
            HERE / "patterns.md",
            HERE / "site-tree.md",
            HERE / "login-review.json",
            HERE / "tokens.json",
            HERE / "style-guide.html",
            HERE / "raw" / "css-vars.json",
            HERE / "raw" / "components-computed.json",
        ]
        for path in notes:
            text = path.read_text(errors="ignore")
            self.assertNotIn("gmail.com", text, str(path))
            self.assertNotIn("@", text, str(path))


if __name__ == "__main__":
    unittest.main()
