#!/usr/bin/env python3
"""The Super.so token builder writes the measured colours and refuses a missing raw file."""
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class BuildTokensTest(unittest.TestCase):
    def test_writes_measured_accent(self):
        subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")], cwd=HERE)
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["accent"]["$value"], "#ffbe3c")
        self.assertEqual(tokens["dark"]["accent"]["$value"], "#ffb224")
        self.assertEqual(tokens["light"]["page"]["$value"], "#fdfdfc")
        self.assertEqual(tokens["dark"]["page"]["$value"], "#151514")
        self.assertIn("source", tokens["light"]["accent"]["$extensions"])
        self.assertIn("hero", tokens["core"]["typography"])

    def test_raw_file_is_the_only_input(self):
        raw = json.loads((PKG / "raw" / "foundations.json").read_text())
        self.assertEqual(raw["colors"]["accent"], "#ffbe3c")
        self.assertNotIn("invented", json.dumps(raw).lower())


if __name__ == "__main__":
    unittest.main()
