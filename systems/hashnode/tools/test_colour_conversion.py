"""The components builder converts oklab()/oklch() fully: a chromatic value keeps its hue.

build_components_md.py writes components.md when it runs, so the test lifts just the converter
out of its source and runs it. The committed focus ring is oklab(0.561988 -0.023436 -0.238834 / 0.5), a 50%
blue; mapping L straight to grey wrote it as rgba(143, 143, 143, 0.5).

Run from the package root: python3 -m unittest discover -s tools
"""
import ast
import pathlib
import re
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


def converter():
    tree = ast.parse((HERE / "build_components_md.py").read_text())
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "_lab_okl")
    scope = {"re": re}
    exec(compile(ast.Module(body=[fn], type_ignores=[]), "build_components_md.py", "exec"), scope)
    return scope["_lab_okl"]


class OklabTest(unittest.TestCase):
    def test_focus_ring_is_blue(self):
        self.assertEqual(converter()("oklab(0.561988 -0.023436 -0.238834 / 0.5)"), "rgba(41, 98, 255, 0.5)")

    def test_grey_lightness_is_not_linear(self):
        # OKLab L 0.221 with no chroma is about #1b1b1b; L x 255 would give #383838.
        self.assertEqual(converter()("oklab(0.221 0 0)"), "#1b1b1b")

    def test_committed_components_carry_no_grey_focus_ring(self):
        self.assertNotIn("rgba(143, 143, 143, 0.5)", (PKG / "components.md").read_text())


def tokens_converter():
    tree = ast.parse((HERE / "build_tokens.py").read_text())
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "norm_color")
    scope = {"re": re}
    exec(compile(ast.Module(body=[fn], type_ignores=[]), "build_tokens.py", "exec"), scope)
    return scope["norm_color"]


class SharedCasesTest(unittest.TestCase):
    """The same inputs through both converters: oklch() through its hue, the
    percentage and `none` spellings, and alpha as a percentage."""

    def cases(self):
        import math
        L, C, h = 0.561988, 0.24, 264.4
        a, b = round(C * math.cos(math.radians(h)), 6), round(C * math.sin(math.radians(h)), 6)
        return [
            (f"oklch({L} {C} {h})", f"oklab({L} {a} {b})"),
            (f"oklch({L} {C} {h}deg / 0.5)", f"oklab({L} {a} {b} / 0.5)"),
            ("oklab(56.1988% -0.023436 -0.238834 / 50%)", "oklab(0.561988 -0.023436 -0.238834 / 0.5)"),
            ("oklch(0.221 none none)", "oklab(0.221 0 0)"),
            ("oklab(0.221 none none)", "oklab(0.221 0 0)"),
        ]

    def test_both_converters_agree_on_every_spelling(self):
        for f in (converter(), tokens_converter()):
            for x, y in self.cases():
                self.assertEqual(f(x), f(y), x)
            self.assertEqual(f("oklab(0.561988 -0.023436 -0.238834 / 0.5)"), "rgba(41, 98, 255, 0.5)")
            self.assertEqual(f("oklch(0.221 none none)"), "#1b1b1b")

    def test_chromatic_oklch_keeps_its_hue(self):
        for f in (converter(), tokens_converter()):
            v = f("oklch(0.561988 0.24 264.4)")
            r, g, b = (int(v[i:i + 2], 16) for i in (1, 3, 5))
            self.assertGreater(b, r + 100, v)  # a blue, not a grey


if __name__ == "__main__":
    unittest.main()
