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

    def test_check_reports_against_its_own_root_and_writes_nothing(self):
        alpha = {"slug": "alpha", "name": "Alpha", "access": "signed out",
                 "capture": {"gaps": ["sign-in was not entered"]}}
        beta = {"slug": "beta", "name": "Beta", "access": "public marketing", "capture": {"gaps": []}}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "catalog.json").write_text(json.dumps({"systems": [alpha, beta]}))
            out = root / "docs" / "GATED.md"
            for committed, code, said in ((gated.render([alpha, beta]), 0, "gated ok"),
                                          (gated.render([alpha]), 1, "stale")):
                out.write_text(committed)
                with mock.patch.object(gated, "ROOT", root), mock.patch.object(gated, "OUT", out), \
                        mock.patch.dict(os.environ, {}, clear=True), \
                        mock.patch("sys.stdout", new_callable=io.StringIO) as printed:
                    self.assertEqual(gated.main(["--check"]), code)
                self.assertIn(said, printed.getvalue())
                self.assertEqual(out.read_text(), committed)

    def test_help_exits_0(self):
        r = run("--help")
        self.assertEqual(r.returncode, 0)
        self.assertIn("--check", r.stdout)


spec = importlib.util.spec_from_file_location("gated", GATED)
gated = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gated)


def git_router(base, branch, fail=False):
    """A stand-in for subprocess.run that answers `git show <ref>:catalog.json` by
    ref, as the Check workflow's fetched origin/main and refs/pr-head do."""
    def run(args, **kwargs):
        if fail:
            raise subprocess.CalledProcessError(128, args)
        ref, _, path = args[-1].partition(":")
        assert args[:2] == ["git", "show"] and path == "catalog.json", args
        rows = {"origin/main": base, "refs/pr-head": branch}[ref]
        return mock.Mock(stdout=json.dumps({"systems": rows}), returncode=0)
    return run


class GatedLagTest(unittest.TestCase):
    """On a pull request the roll-up may leave out packages the merge adds, and is
    otherwise re-rendered from the merge's catalog, never trusted from the branch."""

    def entry(self, slug, gap=None, access="signed out"):
        return {"slug": slug, "name": slug.title(), "access": access,
                "capture": {"gaps": [gap] if gap else []}}

    def setUp(self):
        self.alpha = self.entry("alpha", "sign-in was not entered")
        self.beta = self.entry("beta", access="public marketing")
        self.newer = self.entry("newer", "login was not submitted")   # landed on main after the branch started
        self.added = self.entry("added", "checkout was not entered")  # what this pull request adds
        self.base = [self.alpha, self.beta, self.newer]
        self.branch = [self.alpha, self.beta, self.added]
        self.head = [self.alpha, self.beta, self.newer, self.added]

    def matches(self, current, head=None, base=None, branch=None, env=None, fail=False):
        env = {"GITHUB_BASE_REF": "main", "GITHUB_HEAD_SHA": "refs/pr-head"} if env is None else env
        run = git_router(base or self.base, branch or self.branch, fail)
        with mock.patch.dict(os.environ, env, clear=True), mock.patch.object(gated.catalog.subprocess, "run", run):
            return gated.gated_matches_base(head or self.head, current)

    def test_a_roll_up_that_lags_main_or_this_pull_request_is_accepted(self):
        for subset in ([self.alpha, self.beta], [self.alpha, self.beta, self.added],
                       [self.alpha, self.beta, self.newer]):
            self.assertTrue(self.matches(gated.render(subset)), [s["slug"] for s in subset])

    def test_a_hand_edited_roll_up_is_rejected_even_when_the_branch_carries_it(self):
        self.assertFalse(self.matches(gated.render(self.branch).replace("Alpha", "Hand")))
        self.assertFalse(self.matches(gated.render(self.branch).replace("_2 of 3", "_3 of 3")))

    def test_leaving_out_a_package_the_branch_and_main_share_is_rejected(self):
        self.assertFalse(self.matches(gated.render([self.alpha, self.added])))

    def test_a_removed_package_still_listed_is_rejected(self):
        head = [self.alpha, self.newer, self.added]
        branch = [self.alpha, self.added]
        self.assertFalse(self.matches(gated.render(self.base), head=head, branch=branch))
        # Leaving it out is the right render of what the merge keeps.
        self.assertTrue(self.matches(gated.render([self.alpha, self.added]), head=head, branch=branch))

    def test_an_edited_existing_row_is_rejected(self):
        edited = json.loads(json.dumps(self.head))
        edited[0]["capture"]["gaps"] = ["payment was not entered"]
        self.assertFalse(self.matches(gated.render([self.alpha, self.beta]), head=edited))

    def test_no_pull_request_or_an_unreadable_ref_keeps_the_exact_rule(self):
        prior = gated.render([self.alpha, self.beta])
        self.assertFalse(self.matches(prior, env={}))
        self.assertFalse(self.matches(prior, env={"GITHUB_BASE_REF": "main"}))
        self.assertFalse(self.matches(prior, fail=True))
        self.assertFalse(self.matches(prior, base=[{"slug": None}]))


if __name__ == "__main__":
    unittest.main()
