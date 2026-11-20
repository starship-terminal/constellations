"""The committed outputs must rebuild from the package's inputs.

The builders run on a temporary copy of the package, so nothing committed is rewritten.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ['build_components_md.py']
OUTPUTS = ['components.md']


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.copy = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, cls.copy, ignore=shutil.ignore_patterns("__pycache__"))
        for b in BUILDERS:
            subprocess.run([sys.executable, str(cls.copy / "tools" / b)], check=True, capture_output=True, cwd=cls.copy)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for out in OUTPUTS:
            with self.subTest(out=out):
                self.assertEqual((self.copy / out).read_text(), (PKG / out).read_text())

    def test_failed_focus_is_not_published_as_a_reading(self):
        import json
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        failed = [k for k, c in raw.items() if (c.get("states", {}).get("focus-visible") or {}).get("via") == "focus failed"]
        text = (self.copy / "components.md").read_text()
        for k in failed:
            with self.subTest(component=k):
                self.assertNotIn(f"{k}-focus-visible.png", text)


if __name__ == "__main__":
    unittest.main()
