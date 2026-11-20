"""css4_srgb gives the sRGB values browsers do for lab(), lch(), oklab(), oklch() and
color-mix(..., transparent), and refuses any other mix.

Loads only build_tokens.py's imports, helper constants and functions (not its top-level build),
so the test needs no raw files and writes nothing."""
import ast
import pathlib
import unittest

SRC = (pathlib.Path(__file__).resolve().parent / "build_tokens.py").read_text()
_mod = ast.parse(SRC)
_keep = [n for n in _mod.body if isinstance(n, (ast.FunctionDef, ast.Import, ast.ImportFrom))
         or (isinstance(n, ast.Assign) and all(isinstance(t, ast.Name) and t.id.startswith("_") for t in n.targets))]
NS = {}
exec(compile(ast.Module(body=_keep, type_ignores=[]), "build_tokens.py", "exec"), NS)
css4_srgb = NS["css4_srgb"]


class Css4(unittest.TestCase):
    def test_coloured_values(self):
        self.assertEqual(css4_srgb("lab(54.2905 80.8049 69.891)"), "#ff0000")    # D50 Lab, sRGB red
        self.assertEqual(css4_srgb("lch(54.2905 106.839 40.8526)"), "#ff0000")
        self.assertEqual(css4_srgb("oklch(0.627955 0.257683 29.2339)"), "#ff0000")
        self.assertEqual(css4_srgb("oklch(62.7955% 0.257683 29.2339)"), "#ff0000")
        self.assertEqual(css4_srgb("oklab(0.627955 0.224863 0.125846)"), "#ff0000")

    def test_opacity(self):
        self.assertEqual(css4_srgb("oklch(0 0 0 / 0.5)"), "rgba(0, 0, 0, 0.5)")
        self.assertEqual(css4_srgb("color-mix(in srgb, rgb(255, 0, 0) 40%, transparent)"), "rgba(255, 0, 0, 0.4)")
        self.assertEqual(css4_srgb("color-mix(in oklab, oklch(1 0 0) 50%, transparent)"), "rgba(255, 255, 255, 0.5)")

    def test_other_mixes_raise_and_plain_colours_pass_through(self):
        with self.assertRaises(ValueError):
            css4_srgb("color-mix(in srgb, red 50%, blue)")
        self.assertIsNone(css4_srgb("#ffffff"))
        with self.assertRaises(ValueError):
            css4_srgb("oklch(0.5 0.1)")  # two components: not a colour

    def test_percent_alpha_and_lab_lch_neutrals(self):
        self.assertEqual(css4_srgb("lab(50 0 0 / 25%)"), "rgba(119, 119, 119, 0.25)")
        self.assertEqual(css4_srgb("lch(100 0 0)"), "#ffffff")


if __name__ == "__main__":
    unittest.main()
