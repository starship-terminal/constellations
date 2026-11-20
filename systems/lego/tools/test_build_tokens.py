"""tokens.json and style-guide.html must rebuild from the committed raw readings, and the
shadow parser must read every layer the stylesheets declare.

The builders run on a temporary copy of the package, so the committed files are never rewritten.
"""
import importlib.util
import io
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

PKG = pathlib.Path(__file__).resolve().parent.parent


def copy_package(tmp):
    copy = pathlib.Path(tmp) / "pkg"
    shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__", "screenshots", "components"))
    return copy


def load_builder(copy):
    spec = importlib.util.spec_from_file_location("lego_build_tokens", copy / "tools" / "build_tokens.py")
    mod = importlib.util.module_from_spec(spec)
    with redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


class RebuildTest(unittest.TestCase):
    def test_tokens_and_style_guide_match_raw(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = copy_package(tmp)
            for builder in ("build_tokens.py", "build_style_guide.py"):
                subprocess.run([sys.executable, str(copy / "tools" / builder)], check=True, capture_output=True)
            self.assertEqual((copy / "tokens.json").read_text(), (PKG / "tokens.json").read_text())
            self.assertEqual((copy / "style-guide.html").read_text(), (PKG / "style-guide.html").read_text())


class ShadowParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.mod = load_builder(copy_package(cls.tmp.name))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_rgba_colour_with_commas_is_one_layer(self):
        layers = self.mod.shadow_layers("t", "rgba(0, 0, 0, 0.2) 0px 2px 4px -1px, 0 1px 0 #fff")
        self.assertEqual(len(layers), 2)
        self.assertEqual(layers[0]["color"], "rgba(0, 0, 0, 0.2)")
        self.assertEqual(layers[0]["spread"], "-1px")
        self.assertEqual(layers[1], {"offsetX": "0px", "offsetY": "1px", "blur": "0px", "spread": "0px", "color": "#ffffff"})

    def test_inset_is_kept_wherever_it_stands(self):
        first = self.mod.shadow_layers("t", "inset 0px 1px 1px 0px #0000000d")[0]
        last = self.mod.shadow_layers("t", "rgb(70, 149, 240) 0px 0px 0px 1px inset")[0]
        self.assertTrue(first["inset"])
        self.assertTrue(last["inset"])
        self.assertNotIn("inset", self.mod.shadow_layers("t", "0px 1px 1px #000")[0])

    def test_unreadable_layer_raises(self):
        for bad in ("0px 16px 16px", "0px 1px var(--x)", "0px 1px 2px 3px 4px #000"):
            with self.assertRaises(SystemExit, msg=bad):
                self.mod.shadow_layers("t", bad)

    def test_token_cannot_also_hold_tokens(self):
        tree = {}
        self.mod.put(tree, ["a", "b"], {"$value": 1})
        with self.assertRaises(ValueError):
            self.mod.put(tree, ["a", "b", "c"], {"$value": 2})


if __name__ == "__main__":
    unittest.main()
