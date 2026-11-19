"""tools/gated.py parses its arguments strictly: an unknown flag exits 2 and writes nothing."""
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
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

    def test_help_exits_0(self):
        r = run("--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("--check", r.stdout)


spec = importlib.util.spec_from_file_location("gated", GATED)
gated = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gated)


class GatedCheckTest(unittest.TestCase):
    """--check demands the exact render of the catalog, on a pull request and on main
    alike: a roll-up that lags captures already on main is stale."""

    def entry(self, slug, gap=None, access="signed out"):
        return {"slug": slug, "name": slug.title(), "access": access,
                "capture": {"gaps": [gap] if gap else []}}

    def setUp(self):
        self.alpha = self.entry("alpha", "sign-in was not entered")
        self.beta = self.entry("beta", access="public marketing")
        self.added = self.entry("added", "login was not submitted")
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        (self.root / "catalog.json").write_text(json.dumps({"systems": [self.alpha, self.beta, self.added]}))
        self.addCleanup(self.tmp.cleanup)

    def check(self, committed, env=None):
        out = self.root / "docs" / "GATED.md"
        if committed is None:
            out.unlink(missing_ok=True)
        else:
            out.write_text(committed)
        pr = {"GITHUB_BASE_REF": "main", "GITHUB_HEAD_SHA": "refs/pr-head"}
        with mock.patch.object(gated, "ROOT", self.root), mock.patch.object(gated, "OUT", out), \
                mock.patch.dict(os.environ, env if env is not None else pr), \
                mock.patch("sys.stdout", new_callable=io.StringIO) as printed:
            code = gated.main(["--check"])
        self.assertEqual(out.read_text() if out.exists() else None, committed)  # --check writes nothing
        return code, printed.getvalue()

    def test_the_exact_render_passes(self):
        self.assertEqual(self.check(gated.render([self.alpha, self.beta, self.added])), (0, "gated ok\n"))

    def test_a_roll_up_that_lags_main_fails_even_on_a_pull_request(self):
        code, printed = self.check(gated.render([self.alpha, self.beta]))
        self.assertEqual(code, 1)
        self.assertIn("stale", printed)

    def test_a_roll_up_still_naming_a_removed_package_fails(self):
        removed = self.entry("removed", "checkout was not entered")
        self.assertEqual(self.check(gated.render([self.alpha, self.beta, self.added, removed]))[0], 1)

    def test_a_hand_edit_and_a_missing_file_fail(self):
        text = gated.render([self.alpha, self.beta, self.added])
        self.assertEqual(self.check(text.replace("Alpha", "Hand"))[0], 1)
        self.assertEqual(self.check(None)[0], 1)


if __name__ == "__main__":
    unittest.main()
