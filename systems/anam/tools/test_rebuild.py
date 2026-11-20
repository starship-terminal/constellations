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
BUILDERS = ['build_components_md.py', 'build_style_guide.py']
OUTPUTS = ['components.md', 'style-guide.html']


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

    def test_no_colour_is_labelled_twice(self):
        text = (self.copy / "components.md").read_text()
        self.assertIsNone(re.search(r"(`[^`]+`) \1", text))


if __name__ == "__main__":
    unittest.main()
