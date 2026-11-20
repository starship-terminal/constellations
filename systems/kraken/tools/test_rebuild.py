"""The Kraken builders reproduce the committed files.

Each builder runs in a scratch copy of the package, so nothing committed is rewritten, and its
output is compared with the committed file. Run from this folder, or via
tools/package_tests.py kraken.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
BUILDERS = ["build_tokens.py", "build_style_guide.py"]
OUTPUTS = ["tokens.json", "style-guide.html"]


class Rebuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.dst = Path(cls.tmp.name) / PKG.name
        shutil.copytree(PKG, cls.dst, ignore=shutil.ignore_patterns("*.png", "screenshots", "components"))
        for b in BUILDERS:
            res = subprocess.run([sys.executable, str(cls.dst / "tools" / b)], cwd=cls.dst,
                                 capture_output=True, text=True, timeout=120)
            if res.returncode:
                raise AssertionError(f"{b} failed:\n{res.stderr}")
        cls.tokens = json.loads((PKG / "tokens.json").read_text())

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for rel in OUTPUTS:
            with self.subTest(rel):
                self.assertEqual((self.dst / rel).read_text(), (PKG / rel).read_text(),
                                 f"{rel}: the builders no longer reproduce the committed file")

    def test_motion_comes_from_this_package(self):
        """The rebuild must not import tools/kit/build/motion.py, so a kit change cannot change it."""
        src = (PKG / "tools" / "build_tokens.py").read_text()
        self.assertNotIn('"kit"', src)

    def test_spacing_scale_is_a_reconstruction(self):
        for step in ("1", "2", "3", "4", "5", "6", "8", "10", "12", "16"):
            src = self.tokens["core"]["spacing"][step]["$extensions"]["source"]
            self.assertTrue(src.startswith("Reconstruction"), f"core.spacing.{step}: {src}")

    def test_components_links_resolve(self):
        md = (PKG / "components.md").read_text()
        for target in re.findall(r"\]\(([^)#]+)\)", md):
            if not target.startswith("http"):
                self.assertTrue((PKG / target).exists(), f"components.md links a missing file: {target}")


if __name__ == "__main__":
    unittest.main()
