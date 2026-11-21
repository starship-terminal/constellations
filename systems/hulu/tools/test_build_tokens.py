#!/usr/bin/env python3
"""The token check fails when a value has no capture source."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "build_tokens.py"


class BuildTokensTest(unittest.TestCase):
    def test_package_tokens_pass(self):
        result = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("tokens ok", result.stdout)

    def test_missing_source_fails(self):
        data = json.loads((ROOT / "tokens.json").read_text())
        data["light"]["color"]["page"].pop("$extensions")
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "pkg"
            (package / "raw").mkdir(parents=True)
            (package / "tools").mkdir()
            (package / "tokens.json").write_text(json.dumps(data))
            (package / "raw" / "measured-hex.json").write_text(
                (ROOT / "raw" / "measured-hex.json").read_text()
            )
            script = (package / "tools" / "build_tokens.py")
            script.write_text(SCRIPT.read_text())
            result = subprocess.run(
                [sys.executable, str(script)], capture_output=True, text=True
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing source", result.stderr)


if __name__ == "__main__":
    unittest.main()
