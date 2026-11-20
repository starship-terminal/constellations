"""An achromatic oklch()/oklab() reading converts through OKLab (linear grey
L^3, then sRGB gamma), not L x 255 (finding 14-22).

Run from the package root: python3 -m unittest discover -s tools
"""
import ast
import pathlib
import re
import unittest

SRC = (pathlib.Path(__file__).resolve().parent / "build_component_tokens.py").read_text()
NODE = next(n for n in ast.parse(SRC).body if isinstance(n, ast.FunctionDef) and n.name == "norm_color")
NS = {"re": re}
exec(compile(ast.Module([NODE], []), "norm_color", "exec"), NS)


class OklchGreyTest(unittest.TestCase):
    def test_mid_grey(self):
        self.assertEqual(NS["norm_color"]("oklch(0.5 0 none)"), "#636363")

    def test_black_tint_keeps_alpha(self):
        self.assertEqual(NS["norm_color"]("oklch(0 0 none / 0.85)"), "rgba(0, 0, 0, 0.85)")


if __name__ == "__main__":
    unittest.main()
