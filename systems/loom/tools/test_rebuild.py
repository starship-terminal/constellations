"""tokens.json, components.md and style-guide.html must rebuild from the committed raw readings.

The builders run on a temporary copy of the package, so the committed files are never rewritten.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILT = ("tokens.json", "components.md", "style-guide.html")


class RebuildTest(unittest.TestCase):
    def test_builders_reproduce_committed_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__", "screenshots", "components"))
            for builder in ("build_tokens.py", "build_components_md.py", "build_style_guide.py"):
                subprocess.run([sys.executable, str(copy / "tools" / builder)], check=True, capture_output=True)
            for name in BUILT:
                self.assertEqual((copy / name).read_text(), (PKG / name).read_text(), name)

    def test_failed_focus_is_listed_as_not_captured(self):
        md = (PKG / "components.md").read_text()
        for key in ("nav-menu", "continue-button"):
            row = next(line for line in md.splitlines() if line.startswith(f"| {key} |"))
            self.assertIn("focus-visible (focus could not be captured)", row)


if __name__ == "__main__":
    unittest.main()
