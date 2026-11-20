"""Rebuild checks for the Descript builders. Run from this folder, or via tools/package_tests.py.

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

    def test_font_families_are_the_computed_stacks(self):
        fam = self.built["core"]["font"]["family"]
        for key, comp in (("sans", "nav-link"), ("auth", "au-email-btn"), ("label", "hero-eyebrow"), ("display", "hero-display")):
            self.assertEqual(fam[key]["$value"], self.C[comp]["states"]["default"]["style"]["fontFamily"], key)

    def test_no_oklab_colour_token(self):
        for path, leaf in flat(self.built):
            if leaf.get("$type") == "color":
                self.assertFalse(str(leaf["$value"]).startswith("oklab("), path)

    def test_oklab_colour_converts_to_srgb(self):
        """No committed colour token is oklab, so feed build_tokens.py two oklab leaves: the auth
        button's 90% hover shade (raw/components-computed.json au-email-btn hover) and an opaque white."""
        root = pathlib.Path(self.tmp.name) / "oklab"
        shutil.copytree(self.root / "tools", root / "tools")
        shutil.copytree(self.root / "raw", root / "raw")
        spec_path = root / "raw" / "component-tokens.json"
        spec = json.loads(spec_path.read_text())
        hover = self.C["au-email-btn"]["states"]["hover"]["style"]["backgroundColor"]
        self.assertTrue(hover.startswith("oklab("), hover)
        spec["core"]["test-oklab"] = {
            "hover": {"value": hover, "type": "color", "source": "test", "description": "test"},
            "white": {"value": "oklab(0.999994 0.0000455678 0.0000200868)", "type": "color", "source": "test", "description": "test"},
        }
        spec_path.write_text(json.dumps(spec))
        subprocess.run([sys.executable, str(root / "tools" / "build_tokens.py")], cwd=root, check=True, capture_output=True)
        got = json.loads((root / "tokens.json").read_text())["core"]["test-oklab"]
        self.assertEqual(got["hover"]["$value"], "rgba(63, 42, 50, 0.9)")
        self.assertEqual(got["hover"]["$extensions"]["authored"], hover)
        self.assertEqual(got["white"]["$value"], "#ffffff")
        self.assertEqual(got["white"]["$extensions"]["authored"], "oklab(0.999994 0.0000455678 0.0000200868)")


if __name__ == "__main__":
    unittest.main()
