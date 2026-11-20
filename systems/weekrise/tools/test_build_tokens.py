#!/usr/bin/env python3
"""The Weekrise token check still sees the measured primary colour."""
import pathlib
import json
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent


class BuildTokensTest(unittest.TestCase):
    def test_vapor_primary_is_present(self):
        # The token at the role, against the raw reading at its key (not a substring anywhere).
        tokens = json.loads((HERE.parent / "tokens.json").read_text())
        raw = json.loads((HERE.parent / "raw" / "css-vars.json").read_text())
        self.assertEqual(raw["properties"]["--vapor-primary"], "#2481ff")
        self.assertEqual(tokens["core"]["color"]["named"]["primary"]["$value"], raw["properties"]["--vapor-primary"])

    def test_checker_passes(self):
        proc = subprocess.run([sys.executable, str(HERE / "build_tokens.py")], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)


if __name__ == "__main__":
    unittest.main()
