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


if __name__ == "__main__":
    unittest.main()
