"""Rebuild checks for the Delphi builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots/, components/ and icons/ are
linked read-only), so nothing committed is rewritten.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ("build_component_tokens.py", "build_tokens.py", "build_style_guide.py", "build_components_md.py")
OUTPUTS = ("tokens.json", "raw/component-tokens.json", "style-guide.html", "components.md")


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
        cls.root = root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for d in ("screenshots", "components", "icons"):
            if (PKG / d).exists():
                (root / d).symlink_to(PKG / d)
        for b in BUILDERS:
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        for f in OUTPUTS:
            self.assertEqual((PKG / f).read_text(), (self.root / f).read_text(), f)

    def test_page_field_reads_the_declaration(self):
        src = self.built["light"]["background"]["page"]["$extensions"]["source"]
        self.assertTrue(src.startswith("declared --background"), src)

    def test_components_md_labels_each_colour_once(self):
        import re
        md = (self.root / "components.md").read_text()
        self.assertEqual(re.findall(r"`([a-z0-9.-]+)` `\1`", md), [])

    def test_lab_colour_is_converted(self):
        """No committed reading is lab(), so give one component's text a lab() colour the browser
        resolves to #e37b4c (digg's declared --rank-one, raw/css-vars.json) and rebuild components.md."""
        root = pathlib.Path(self.tmp.name) / "lab"
        shutil.copytree(self.root / "tools", root / "tools")
        shutil.copytree(self.root / "raw", root / "raw")
        shutil.copy(self.root / "tokens.json", root / "tokens.json")
        for d in ("screenshots", "components", "icons"):
            if (PKG / d).exists():
                (root / d).symlink_to(PKG / d)
        path = root / "raw" / "components-computed.json"
        J = json.loads(path.read_text())
        J["components"]["mkt-header"]["states"]["default"]["textStyle"]["color"] = "lab(63.1181 38.4657 43.9524)"
        path.write_text(json.dumps(J))
        subprocess.run([sys.executable, str(root / "tools" / "build_components_md.py")], cwd=root, check=True, capture_output=True)
        md = (root / "components.md").read_text()
        self.assertIn("#e37b4c", md)
        self.assertNotIn("lab(63.1181", md)


if __name__ == "__main__":
    unittest.main()
