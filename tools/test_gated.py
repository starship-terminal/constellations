"""tools/gated.py parses its arguments strictly: an unknown flag exits 2 and writes nothing."""
import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
GATED = HERE / "gated.py"
OUT = HERE.parent / "docs" / "GATED.md"


def run(*args):
    return subprocess.run([sys.executable, str(GATED), *args], capture_output=True, text=True)


class GatedFlagsTest(unittest.TestCase):
    def test_unknown_flags_exit_2_with_usage_and_write_nothing(self):
        before = OUT.read_bytes() if OUT.exists() else None
        mtime = OUT.stat().st_mtime_ns if OUT.exists() else None
        for flag in ("--bogus", "--chek", "check", "--check=1"):
            r = run(flag)
            self.assertEqual(r.returncode, 2, (flag, r.stderr))
            self.assertIn("usage:", r.stderr)
            self.assertEqual(r.stdout, "")
        after = OUT.read_bytes() if OUT.exists() else None
        self.assertEqual(before, after)
        if mtime is not None:
            self.assertEqual(mtime, OUT.stat().st_mtime_ns)

    def test_check_writes_nothing_and_reports_current_state(self):
        mtime = OUT.stat().st_mtime_ns
        r = run("--check")
        self.assertIn(r.returncode, (0, 1), r.stderr)
        self.assertEqual(mtime, OUT.stat().st_mtime_ns)
        self.assertTrue("gated ok" in r.stdout or "stale" in r.stdout, r.stdout)

    def test_help_exits_0(self):
        r = run("--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("--check", r.stdout)


spec = importlib.util.spec_from_file_location("gated", GATED)
gated = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gated)


class GatedLagTest(unittest.TestCase):
    """gated_matches_base accepts a roll-up that predates packages on main."""

    def entry(self, slug, gap=None, access="signed out"):
        return {"slug": slug, "name": slug.title(), "access": access,
                "capture": {"gaps": [gap] if gap else []}}

    def setUp(self):
        self.alpha = self.entry("alpha", "sign-in was not entered")
        self.beta = self.entry("beta", access="public marketing")
        self.newer = self.entry("newer", "login was not submitted")
        self.added = self.entry("added", access="public marketing")
        self.base = [self.alpha, self.beta, self.newer]
        self.head = [self.alpha, self.beta, self.newer, self.added]
        self.prior = gated.render([self.alpha, self.beta])

    def matches(self, systems, current, base_ref="main"):
        shown = json.dumps({"systems": self.base})

        def fake_run(args, **kwargs):
            return mock.Mock(stdout=shown, returncode=0)

        env = {"GITHUB_BASE_REF": base_ref} if base_ref else {}
        with mock.patch.dict(os.environ, env, clear=False), \
                mock.patch.object(gated.subprocess, "run", fake_run):
            if not base_ref:
                os.environ.pop("GITHUB_BASE_REF", None)
            return gated.gated_matches_base(systems, current)

    def test_an_older_roll_up_is_accepted(self):
        self.assertTrue(self.matches(self.head, self.prior))

    def test_a_changed_existing_row_is_rejected(self):
        changed = json.loads(json.dumps(self.head))
        changed[0]["capture"]["gaps"] = ["checkout was not entered"]
        self.assertFalse(self.matches(changed, self.prior))

    def test_a_hand_edited_roll_up_is_rejected(self):
        self.assertFalse(self.matches(self.head, self.prior.replace("Alpha", "Hand")))

    def test_without_a_pull_request_base_the_exemption_does_not_apply(self):
        self.assertFalse(self.matches(self.head, self.prior, base_ref=None))


if __name__ == "__main__":
    unittest.main()
