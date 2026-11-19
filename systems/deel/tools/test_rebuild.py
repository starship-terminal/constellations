"""Rebuild checks for the Deel builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/, so nothing committed is rewritten.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for b in ("build_component_tokens.py", "build_tokens.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)

    def test_font_families_are_the_computed_stacks(self):
        fam = self.built["core"]["font"]["family"]
        for key, comp in (("sans", "footer-link"), ("brand", "nav-link"), ("display", "hero-h1")):
            self.assertEqual(fam[key]["$value"], self.C[comp]["states"]["default"]["style"]["fontFamily"])

    def test_no_css_color4_value_left_unconverted(self):
        for path, leaf in flat(self.built):
            if leaf.get("$type") == "color":
                self.assertFalse(str(leaf["$value"]).startswith("oklab("), path)


if __name__ == "__main__":
    unittest.main()
