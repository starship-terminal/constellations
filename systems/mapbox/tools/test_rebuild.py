"""tokens.json, style-guide.html and components.md must rebuild from the builders, byte for byte.

The builders run on a temporary copy of the package with the outputs removed first, so a builder
that writes nothing, or a committed file that went stale (components.md once listed four measured
components as "Not present"), fails here. Nothing committed is rewritten.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
# In the order the README's Rebuild section runs them.
BUILDERS = ["build_tokens.py", "build_style_guide.py", "build_components_md.py"]
OUTPUTS = ["tokens.json", "style-guide.html", "components.md"]


class RebuildTest(unittest.TestCase):
    def test_outputs_match_committed(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__"))
            for out in OUTPUTS:
                (copy / out).unlink()
            for b in BUILDERS:
                subprocess.run([sys.executable, str(copy / "tools" / b)], check=True, capture_output=True, cwd=copy)
            for out in OUTPUTS:
                with self.subTest(out=out):
                    self.assertTrue((copy / out).exists(), f"{out} was not rebuilt")
                    self.assertEqual((copy / out).read_bytes(), (PKG / out).read_bytes())


if __name__ == "__main__":
    unittest.main()
