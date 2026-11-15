"""tools/gated.py parses its arguments strictly: an unknown flag exits 2 and writes nothing."""
import subprocess
import sys
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()
