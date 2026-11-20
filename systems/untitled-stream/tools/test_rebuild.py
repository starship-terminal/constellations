"""The builders reproduce the committed files: a rebuild that changes nothing.

Each builder runs on a scratch copy of the package (never on the package itself), and its output is
compared byte for byte with the committed tokens.json, components.md and style-guide.html.
"""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
BUILDERS = {
    "build_tokens.py": "tokens.json",
    "build_components_md.py": "components.md",
    "build_style_guide.py": "style-guide.html",
}


class Rebuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.copy = Path(cls.tmp.name) / PKG.name
        shutil.copytree(PKG, cls.copy, ignore=shutil.ignore_patterns("__pycache__"))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_each_builder_reproduces_its_file(self):
        for builder, output in BUILDERS.items():
            with self.subTest(builder=builder):
                done = subprocess.run([sys.executable, str(self.copy / "tools" / builder)], cwd=self.copy,
                                      capture_output=True, text=True)
                self.assertEqual(done.returncode, 0, done.stderr)
                self.assertEqual((self.copy / output).read_bytes(), (PKG / output).read_bytes(),
                                 f"{builder} no longer reproduces {output}")


if __name__ == "__main__":
    unittest.main()
