"""The oklab()/oklch() conversion in build_components_md.py is the full OKLab
to sRGB one: a chromatic value keeps its hue and a grey its true lightness.

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

if __name__ == "__main__":
    unittest.main()
