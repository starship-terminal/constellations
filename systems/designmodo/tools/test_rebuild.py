"""Rebuild checks for the Designmodo builders. Run from this folder, or via tools/package_tests.py.

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

    def test_paper_is_labelled_typed_not_measured(self):
        src = self.built["light"]["background"]["paper"]["$extensions"]["source"]
        self.assertTrue(src.startswith("entered by hand at capture time, not measured"), src)

    def test_backgrounds_read_from_raw(self):
        bg = self.built["light"]["background"]
        self.assertEqual(self.C["site-footer"]["states"]["default"]["style"]["backgroundColor"], "rgb(255, 255, 255)")
        self.assertEqual(bg["page"]["$value"], "#ffffff")
        self.assertIn("computed backgroundColor of site-footer", bg["page"]["$extensions"]["source"])
        face = self.C["create-blank"]["states"]["default"]["paint"][0]
        self.assertTrue(face["node"].startswith("div.sc-hBxvHn"))
        self.assertEqual((face["bg"], bg["card-face"]["$value"]), ("rgb(244, 246, 247)", "#f4f6f7"))
        self.assertIn("painted background of the div.sc-hBxvHn", bg["card-face"]["$extensions"]["source"])

    def test_kept_tpl_card_reading_is_flagged(self):
        self.assertTrue(self.C["tpl-card"].get("recaptureMissed"))
        for k in ("tpl-card-width", "tpl-card-height"):
            self.assertIn("recaptureMissed", self.built["core"]["component"][k]["$extensions"]["source"], k)


if __name__ == "__main__":
    unittest.main()
