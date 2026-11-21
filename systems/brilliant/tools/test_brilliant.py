"""Package checks that do not need a catalog.json edit."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class BrilliantPublic(unittest.TestCase):
    def test_public_review_stops_at_empty_walls(self):
        review = json.loads((HERE / "login-review.json").read_text())
        self.assertEqual(review["login_extracted"], "not-started")
        self.assertFalse(review["signed_in"])
        self.assertGreaterEqual(len(review["screens"]), 2)
        for screen in review["screens"]:
            path = HERE / screen["file"]
            self.assertTrue(path.is_file(), screen["file"])
            head = path.read_bytes()[:8]
            # Git LFS may replace the worktree copy with a pointer after add.
            # Either a real PNG or an LFS pointer is acceptable here.
            self.assertTrue(
                head.startswith(b"\x89PNG") or path.read_text(errors="ignore").startswith("version https://git-lfs"),
                screen["file"],
            )
        self.assertTrue(review["gaps"])
        self.assertTrue(review["not_submitted"])
        self.assertIn("catalog.json", " ".join(review["gaps"]))

    def test_tokens_round_trip(self):
        import subprocess
        import sys

        before = (HERE / "tokens.json").read_text()
        subprocess.check_call([sys.executable, str(HERE / "tools" / "build_tokens.py")])
        self.assertEqual(before, (HERE / "tokens.json").read_text())

    def test_no_email_in_public_notes(self):
        notes = [
            HERE / "README.md",
            HERE / "DESIGN.md",
            HERE / "components.md",
            HERE / "patterns.md",
            HERE / "site-tree.md",
            HERE / "login-review.json",
            HERE / "tokens.json",
            HERE / "raw" / "css-vars.json",
            HERE / "raw" / "public-2026-11-21.json",
        ]
        for path in notes:
            text = path.read_text(errors="ignore")
            self.assertNotIn("gmail.com", text, str(path))
            self.assertNotIn("oauth", text.lower(), str(path))


if __name__ == "__main__":
    unittest.main()
