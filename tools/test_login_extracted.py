"""A signed-in capture is not done until the walk covers more than the first page."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("login_extracted", HERE / "login_extracted.py")
login = importlib.util.module_from_spec(spec)
spec.loader.exec_module(login)


def offered(nav=None, settings=None, create=None):
    def area(items):
        items = list(items)
        return {"items": items, "reached": list(items)}

    return {
        "nav": area(nav or ["Events", "Calendars"]),
        "settings": area(settings or ["Preferences"]),
        "create": area(create or ["New event"]),
    }


def review(**over):
    row = {
        "offered": offered(),
        "screens": [
            {"name": "Events", "file": "screenshots/home.png"},
            {"name": "Calendars", "file": "screenshots/calendars.png"},
        ],
        "gaps": ["guest list: the trial has no event"],
        "not_submitted": ["create event"],
    }
    row.update(over)
    return row


def app(**over):
    row = {
        "name": "Luma",
        "domain": "lu.ma",
        "status": "captured",
        "package": "systems/luma",
        "notes": "",
        "login-extracted": "not-started",
    }
    row.update(over)
    return row


class LoginExtractedTest(unittest.TestCase):
    def test_a_missing_field_fails(self):
        row = app()
        del row["login-extracted"]
        self.assertTrue(login.check_app(row))

    def test_not_started_needs_no_review(self):
        self.assertEqual(login.check_app(app()), [])

    def test_partial_without_a_reason_fails(self):
        problems = login.check_app(app(**{"login-extracted": "partial"}))
        self.assertTrue(any("notes" in p for p in problems))

    def test_partial_with_a_reason_passes(self):
        row = app(**{"login-extracted": "partial", "notes": "company-size step did not advance"})
        self.assertEqual(login.check_app(row), [])

    def test_done_without_a_review_fails(self):
        problems = login.check_app(app(**{"login-extracted": "done"}))
        self.assertTrue(problems)

    def test_done_rejects_a_screen_with_no_file(self):
        body = review(screens=[{"name": "Events", "file": ""}, {"name": "Calendars", "file": "screenshots/calendars.png"}])
        problems = login.check_app(app(**{"login-extracted": "done", "login-review": body}))
        self.assertTrue(any("no screenshot" in p for p in problems))

    def test_done_rejects_a_file_that_is_not_in_the_package(self):
        problems = login.check_app(app(**{"login-extracted": "done", "login-review": review()}))
        self.assertTrue(any("not in the package" in p for p in problems))

    def test_a_review_before_a_pass_fails(self):
        problems = login.check_app(app(**{"login-review": {"screens": []}}))
        self.assertTrue(any("only set once" in p for p in problems))

    def test_done_rejects_a_one_page_review(self):
        body = review(screens=[{"name": "Events", "file": "screenshots/home.png"}])
        problems = login.check_app(app(**{"login-extracted": "done", "login-review": body}))
        self.assertTrue(any("first page" in p for p in problems))

    def test_done_rejects_a_nav_item_left_unopened(self):
        body = review()
        body["offered"]["nav"]["reached"] = ["Events"]
        problems = login.check_app(app(**{"login-extracted": "done", "login-review": body}))
        self.assertTrue(any("Calendars" in p and "unopened" in p for p in problems))

    def test_done_rejects_a_screenshot_the_review_never_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "systems" / "luma"
            for name in ("home.png", "calendars.png", "signed-in-settings.png", "discover-light-default.png"):
                shot = package / "screenshots" / name
                shot.parent.mkdir(parents=True, exist_ok=True)
                shot.write_bytes(b"png")
            row = app(package="systems/luma", **{"login-extracted": "done", "login-review": review()})
            old = login.ROOT
            login.ROOT = Path(tmp)
            try:
                problems = login.check_app(row)
            finally:
                login.ROOT = old
            self.assertTrue(any("signed-in-settings.png" in p and "missing from login-review" in p for p in problems))
            self.assertFalse(any("discover-light" in p for p in problems))

    def test_done_accepts_a_walk_whose_files_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "systems" / "luma"
            for name in ("home.png", "calendars.png"):
                shot = package / "screenshots" / name
                shot.parent.mkdir(parents=True, exist_ok=True)
                shot.write_bytes(b"png")
            row = app(package="systems/luma", **{"login-extracted": "done", "login-review": review()})
            old = login.ROOT
            login.ROOT = Path(tmp)
            try:
                self.assertEqual(login.check_app(row), [])
            finally:
                login.ROOT = old

    def test_check_command_accepts_the_manifest(self):
        r = subprocess.run(
            [sys.executable, str(HERE / "login_extracted.py"), "--check"],
            cwd=HERE.parent, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("login-extracted ok", r.stdout)

    def test_unknown_flag_exits_2(self):
        r = subprocess.run(
            [sys.executable, str(HERE / "login_extracted.py"), "--bogus"],
            cwd=HERE.parent, capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        self.assertIn("usage:", r.stderr)


if __name__ == "__main__":
    unittest.main()
