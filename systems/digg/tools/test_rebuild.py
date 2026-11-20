"""Rebuild checks for the Digg builders. Run from this folder, or via tools/package_tests.py.

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

    def test_declared_font_stacks_are_verbatim(self):
        V = json.loads((PKG / "raw" / "css-vars.json").read_text())
        decl = {n: v for rule in V["theme"] for n, v in rule.get("properties", {}).items()}
        fam = self.built["core"]["font"]["family"]
        self.assertEqual(fam["mono"]["$value"], decl["--font-vt323"])
        self.assertEqual(fam["typeset"]["$value"], decl["--font-ibm-plex"])

    def test_field_shadow_is_the_painted_layer(self):
        box = self.C["lg-email"]["states"]["default"]["style"]["boxShadow"]
        self.assertTrue(box.endswith("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px"), box)
        self.assertEqual(self.built["core"]["shadow"]["field"]["$value"],
                         [{"offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px", "color": "rgba(0, 0, 0, 0.05)"}])

    def test_rank_one_claims_no_screenshot(self):
        for theme in ("light", "dark"):
            src = self.built[theme]["text"]["rank-one"]["$extensions"]["source"]
            self.assertNotIn("screenshot", src, theme)

    def test_components_md_labels_each_colour_once(self):
        import re
        md = (self.root / "components.md").read_text()
        self.assertEqual(re.findall(r"`([a-z0-9.-]+)` `\1`", md), [])

    def test_a_colour_name_means_that_colour_in_every_theme(self):
        # One name map serves light and dark components, so a theme name printed after a colour
        # must hold that colour in every theme that defines it (dark d-signup text is #ffffff,
        # which light background.card holds but dark background.card does not).
        import re
        T = json.loads((PKG / "tokens.json").read_text())
        held = {}
        for s in ("core", "light", "dark"):
            for n, t in flat(T.get(s, {})):
                if isinstance(t["$value"], str) and t["$value"].startswith("#"):
                    held.setdefault(n, {})[s] = t["$value"].lower()
        md = (self.root / "components.md").read_text()
        for hexv, name in re.findall(r"(#[0-9a-f]{6}) `([^`]+)`", md):
            for s, v in held.get(name, {}).items():
                self.assertEqual(v, hexv, f"{hexv} named {name}, which is {v} in {s}")


if __name__ == "__main__":
    unittest.main()
