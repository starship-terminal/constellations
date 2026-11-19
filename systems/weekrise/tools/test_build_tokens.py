#!/usr/bin/env python3
"""The Weekrise token check still sees the measured primary colour."""
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent


class BuildTokensTest(unittest.TestCase):
    def test_vapor_primary_is_present(self):
        tokens = (HERE.parent / "tokens.json").read_text()
        self.assertIn("#2481ff", tokens)
        self.assertIn("--vapor-primary", (HERE.parent / "raw" / "css-vars.json").read_text())

    def test_checker_passes(self):
        proc = subprocess.run([sys.executable, str(HERE / "build_tokens.py")], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)


if __name__ == "__main__":
    unittest.main()
