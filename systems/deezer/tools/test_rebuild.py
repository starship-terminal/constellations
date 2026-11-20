"""Rebuild checks for the Deezer builders. Run from this folder, or via tools/package_tests.py.

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

    def test_page_field_is_labelled_sampled(self):
        src = self.built["light"]["background"]["page"]["$extensions"]["source"]
        self.assertTrue(src.startswith("sampled, not measured"), src)

    def test_kept_readings_are_flagged(self):
        self.assertTrue(self.C["menu-popover"].get("recaptureMissed"))
        core = self.built["core"]
        for leaf in (core["radius"]["popover"], core["shadow"]["popover"], core["component"]["popover-width"], core["component"]["artist-image"]):
            self.assertIn("recaptureMissed", leaf["$extensions"]["source"])

    def test_transparent_outline_is_no_focus_ring(self):
        md = (self.root / "components.md").read_text()
        focus = next(l for l in md.splitlines() if l.startswith("**Focus.**"))
        ringed = focus.split(" draw an outline ring: ")[1].split(". ")[0]
        self.assertNotIn("rgba(0, 0, 0, 0)", ringed)
        self.assertNotIn("transparent", ringed)
        self.assertNotIn("`login-show-password`", ringed)


if __name__ == "__main__":
    unittest.main()
