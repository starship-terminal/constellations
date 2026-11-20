"""The oklab()/oklch() conversion in both builders is the full OKLab to sRGB
one: a chromatic value keeps its hue and a grey its true lightness.

Run from the package root: python3 -m unittest discover -s tools
"""
import ast
import pathlib
import re
import unittest

HERE = pathlib.Path(__file__).resolve().parent


def load(fn, name):
    """Lift one function out of a builder (the builders write on run)."""
    tree = ast.parse((HERE / fn).read_text())
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    ns = {"re": re}
    exec(compile(ast.Module([node], []), fn, "exec"), ns)
    return ns[name]


class OklabTest(unittest.TestCase):
    def test_components_md_converter(self):
        f = load("build_components_md.py", "_lab_okl")
        self.assertEqual(f("oklab(0.561988 -0.023436 -0.238834 / 0.5)"), "rgba(41, 98, 255, 0.5)")
        self.assertEqual(f("oklab(0.221 0 0)"), "#1b1b1b")
        self.assertEqual(f("oklch(0.5 none none)"), "#636363")

    def test_tokens_converter(self):
        f = load("build_tokens.py", "norm_color")
        self.assertEqual(f("oklab(0.561988 -0.023436 -0.238834 / 0.5)"), "rgba(41, 98, 255, 0.5)")
        self.assertEqual(f("oklch(0.5 0 0)"), "#636363")


class FontStackTest(unittest.TestCase):
    def test_brand_stack_is_measured_and_fallback_is_labelled(self):
        import json
        pkg = HERE.parent
        T = json.loads((pkg / "tokens.json").read_text())
        C = json.loads((pkg / "raw" / "components-computed.json").read_text())["components"]
        fam = T["core"]["font"]["family"]
        st = C["site-header"]["states"]["default"]
        raw = (st.get("textStyle") or {}).get("fontFamily") or st["style"]["fontFamily"]
        self.assertEqual(fam["brand"]["$value"], raw)
        self.assertTrue(fam["fallback"]["$extensions"]["source"].startswith("Reconstruction"))


class PressOnTest(unittest.TestCase):
    def test_request_node_reads_node_id(self):
        src = (HERE / "capture" / "public" / "measure.mjs").read_text()
        self.assertNotIn("const { node } = await cdp.send('DOM.requestNode'", src)


if __name__ == "__main__":
    unittest.main()
