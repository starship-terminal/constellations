"""Package checks that do not need a catalog.json entry."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class QuizletPackage(unittest.TestCase):
    def test_review_names_two_screens_and_the_files_exist(self):
        review = json.loads((HERE / "login-review.json").read_text())
        self.assertTrue(review["signed_in"])
        self.assertGreaterEqual(len(review["screens"]), 2)
        for screen in review["screens"]:
            self.assertTrue((HERE / screen["file"]).is_file(), screen["file"])
        for stop in ("nav", "settings", "create"):
            item = review["offered"][stop]
            self.assertTrue(item["items"])
            self.assertIsInstance(item["reached"], list)
        self.assertTrue(review["gaps"])
        self.assertTrue(review["not_submitted"])

    def test_tokens_round_trip(self):
        import subprocess
        import sys
        before = (HERE / "tokens.json").read_text()
        subprocess.check_call([sys.executable, str(HERE / "tools" / "build_tokens.py")])
        self.assertEqual(before, (HERE / "tokens.json").read_text())

    def test_no_email_in_notes(self):
        banned = ("@", "gmail.com")
        for path in HERE.rglob("*"):
            if path.suffix not in {".md", ".json", ".html", ".py"}:
                continue
            if "node_modules" in path.parts:
                continue
            text = path.read_text(errors="ignore")
            if path.name == "test_quizlet.py":
                continue
            self.assertNotIn("gmail.com", text, str(path))


if __name__ == "__main__":
    unittest.main()
