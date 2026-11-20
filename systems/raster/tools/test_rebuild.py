"""tokens.json and style-guide.html must rebuild from the builders, byte for byte (compared as bytes).

The builders run on a temporary copy of the package with both outputs removed first, so a builder
that writes nothing, or one that drifted from the committed file (it once wrote a `light` set
where tokens.json has `docs`), fails here. Nothing committed is rewritten.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ["build_tokens.py", "build_style_guide.py"]
OUTPUTS = ["tokens.json", "style-guide.html"]


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
