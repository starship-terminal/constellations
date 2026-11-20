"""The committed token and components files must rebuild from the raw readings.

The builders run on a temporary copy of the package, so the committed files are never rewritten.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ["build_component_tokens.py", "build_tokens.py", "build_components_md.public.py"]
OUTPUTS = ["raw/component-tokens.json", "tokens.json", "components.md"]


def leaves(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from leaves(v, prefix + k + ".")


class BuildersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        copy = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__"))
        # Remove the committed outputs from the copy first, so a builder that
        # writes nothing cannot pass by leaving the committed file in place.
        for out in OUTPUTS:
            (copy / out).unlink()
        for b in BUILDERS:
            subprocess.run([sys.executable, str(copy / "tools" / b)], check=True, capture_output=True, cwd=copy)
        cls.copy = copy

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for out in OUTPUTS:
            with self.subTest(out=out):
                self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
                self.assertEqual((self.copy / out).read_text(), (PKG / out).read_text())

    def test_dark_elevation_border_is_the_dark_declaration(self):
        dark = json.loads((self.copy / "tokens.json").read_text())["dark"]
        tok = dark["elevation"]["named"]["primary-border"]
        self.assertEqual(tok["$value"], "#313131")
        self.assertIn(".c12bynq4", tok["$extensions"]["source"])

    def test_alias_only_where_the_css_names_the_variable(self):
        # dark bg.discount is declared as a literal on .c12bynq4: equal hex to a ramp step is no alias
        tokens = json.loads((self.copy / "tokens.json").read_text())
        for theme in ("light", "dark"):
            for name, tok in leaves(tokens[theme]):
                v = tok["$value"]
                if tok["$type"] == "color" and isinstance(v, str) and v.startswith("{palette."):
                    with self.subTest(theme=theme, name=name):
                        self.assertIn("->", tok["$extensions"]["source"])

    def test_heart_tokens_are_the_recorded_icon_paint(self):
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        icon = raw["card-heart"]["states"]["default"]["icon"]
        meas = json.loads((self.copy / "raw" / "component-tokens.json").read_text())["core"]["measured"]
        self.assertEqual(meas["heart-idle"]["value"], "rgba(0, 0, 0, 0.5)")
        self.assertEqual(icon["fill"], "rgba(0, 0, 0, 0.5)")
        self.assertEqual(meas["heart-stroke"]["value"], "#ffffff")


if __name__ == "__main__":
    unittest.main()
