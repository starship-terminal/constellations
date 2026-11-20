"""Tests for app/scripts/build-float-parity-fixture.py. Run with `make test`."""
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "app/scripts/build-float-parity-fixture.py"


class AsciiLocaleTest(unittest.TestCase):
    def test_check_passes_under_an_ascii_locale_with_utf8_mode_off(self):
        # The fixture holds non-ASCII text ("café"); its read and write must say UTF-8.
        env = {**os.environ, "LC_ALL": "C", "LANG": "C", "PYTHONUTF8": "0", "PYTHONCOERCECLOCALE": "0"}
        run = subprocess.run([sys.executable, str(SCRIPT), "--check"], capture_output=True, text=True,
                             env=env, encoding="utf-8")
        self.assertEqual(run.returncode, 0, run.stdout[-2000:] + run.stderr[-2000:])


if __name__ == "__main__":
    unittest.main()
