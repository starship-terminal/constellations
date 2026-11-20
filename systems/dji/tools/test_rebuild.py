"""Rebuild checks for the DJI builders. Run from this folder, or via tools/package_tests.py.

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

    def test_page_and_hairline_read_the_declarations(self):
        spec = json.loads((self.root / "raw" / "component-tokens.json").read_text())["light"]
        self.assertTrue(spec["background"]["page"]["source"].startswith("declared --white"))
        self.assertTrue(spec["border"]["hairline"]["source"].startswith("declared --black-divider"))
        V = json.loads((PKG / "raw" / "css-vars.json").read_text())
        light_divider = [r["properties"]["--divider"] for r in V["app"] if r["selector"] == ":root .light-theme" and "--divider" in r["properties"]]
        self.assertEqual(light_divider, ["var(--black-divider)"])

    def test_wrong_element_reading_is_flagged(self):
        self.assertIn("no longer supported", self.C["co-lede"]["states"]["default"]["text"])
        src = self.built["core"]["font"]["size"]["measured"]["body"]["$extensions"]["source"]
        self.assertIn("read from the wrong element; recapture needed", src)

    def test_recaptured_lede_clears_the_flag(self):
        root = pathlib.Path(self.tmp.name) / "recaptured"
        shutil.copytree(self.root / "tools", root / "tools")
        shutil.copytree(self.root / "raw", root / "raw")
        path = root / "raw" / "components-computed.json"
        J = json.loads(path.read_text())
        J["components"]["co-lede"]["states"]["default"]["text"] = "DJI is a global leader in civilian drones and creative camera technology."
        path.write_text(json.dumps(J))
        subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, check=True, capture_output=True)
        spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        self.assertNotIn("wrong element", spec["core"]["font"]["size"]["measured"]["body"]["source"])

    def test_dark_components_are_labelled_from_the_dark_set(self):
        md = (self.root / "components.md").read_text()
        self.assertIn("rgba(255, 255, 255, 0.09) `action.ghost-hover`", md)


if __name__ == "__main__":
    unittest.main()
