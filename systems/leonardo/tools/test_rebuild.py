"""The builders reproduce the committed files, and split_host_vars.py refuses its own output.

Every builder runs on a temporary copy of the package, so the committed files are never rewritten.
"""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ["build_component_tokens.py", "build_tokens.py", "build_components_md.py", "build_style_guide.py"]
OUTPUTS = ["raw/component-tokens.json", "tokens.json", "components.md", "style-guide.html"]


def copy_package(tmp):
    copy = pathlib.Path(tmp) / "leonardo"
    shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__"))
    return copy


class RebuildTest(unittest.TestCase):
    def test_builders_reproduce_committed_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = copy_package(tmp)
            for b in BUILDERS:
                subprocess.run([sys.executable, str(copy / "tools" / b)], check=True, capture_output=True, cwd=copy)
            for out in OUTPUTS:
                self.assertEqual((copy / out).read_text(), (PKG / out).read_text(), out)

    def test_light_set_holds_no_product_role(self):
        # The product was painted dark only; the light set is the docs color mode.
        import json
        light = json.loads((PKG / "tokens.json").read_text())["light"]["color"]
        self.assertEqual(sorted(light), ["docs"])

    def test_split_host_vars_refuses_its_own_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = copy_package(tmp)
            before = (copy / "raw" / "css-vars.json").read_bytes()
            res = subprocess.run([sys.executable, str(copy / "tools" / "split_host_vars.py")], capture_output=True, text=True)
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("already split", res.stderr)
            self.assertEqual((copy / "raw" / "css-vars.json").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
