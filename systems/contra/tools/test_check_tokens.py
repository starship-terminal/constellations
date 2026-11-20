#!/usr/bin/env python3
"""The package checker refuses a token with no evidence label."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILD = HERE / "check_tokens.py"


class CheckTokensTest(unittest.TestCase):
    def test_package_tokens_pass(self):
        proc = subprocess.run([sys.executable, str(BUILD)], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("contra tokens ok", proc.stdout)

    def test_missing_source_fails(self):
        tokens = json.loads((HERE.parent / "tokens.json").read_text())
        tokens["light"]["text"]["primary"]["$extensions"]["source"] = "guessed"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "tokens.json").write_text(json.dumps(tokens))
            script = BUILD.read_text().replace(
                'HERE = Path(__file__).resolve().parent.parent',
                f'HERE = Path(r"{root}")',
            )
            path = root / "check.py"
            path.write_text(script)
            proc = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 1)
        self.assertIn("source does not say", proc.stderr)


if __name__ == "__main__":
    unittest.main()
