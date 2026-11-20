"""norm_color converts CSS Color 4 notations the way browsers do.

Loads only the builder's imports and functions (not its top-level build), so
the test needs no raw files and writes nothing.
"""
import ast
import pathlib
import unittest

SRC = pathlib.Path(__file__).with_name("build_component_tokens.py").read_text()
_mod = ast.parse(SRC)
NS = {}
exec(compile(ast.Module(body=[n for n in _mod.body if isinstance(n, (ast.FunctionDef, ast.Import, ast.ImportFrom))],
                        type_ignores=[]), "build_component_tokens.py", "exec"), NS)
norm_color = NS["norm_color"]


class NormColor(unittest.TestCase):
    def test_lab_is_d50(self):
        # CSS Color 4 sRGB red is lab(54.29 80.80 69.89) with a D50 white
        self.assertEqual(norm_color("lab(54.2905 80.8049 69.8910)"), "#ff0000")
        self.assertEqual(norm_color("lab(50 0 0)"), "#777777")

    def test_oklch_percent_lightness(self):
        self.assertEqual(norm_color("oklch(62.8% 0.2577 29.23)"), "#ff0000")
        self.assertEqual(norm_color("oklch(0.628 0.2577 29.23)"), "#ff0000")


if __name__ == "__main__":
    unittest.main()
