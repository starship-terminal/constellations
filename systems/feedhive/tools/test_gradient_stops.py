"""gradient_stops() splits a gradient on top-level commas only and keeps
explicit stop positions (finding 14-29).

Run from the package root: python3 -m unittest discover -s tools
"""
import ast
import pathlib
import re
import unittest

SRC = (pathlib.Path(__file__).resolve().parent / "build_component_tokens.py").read_text()
NODE = next(n for n in ast.parse(SRC).body if isinstance(n, ast.FunctionDef) and n.name == "gradient_stops")
NS = {"re": re}
exec(compile(ast.Module([NODE], []), "gradient_stops", "exec"), NS)
gradient_stops = NS["gradient_stops"]


class GradientStopsTest(unittest.TestCase):
    def test_functional_colours_keep_their_commas(self):
        self.assertEqual(gradient_stops("rgb(68, 69, 255), rgb(117, 131, 253)"),
                         [("rgb(68, 69, 255)", 0.0), ("rgb(117, 131, 253)", 1.0)])

    def test_explicit_positions_are_kept(self):
        self.assertEqual(gradient_stops("#adadad 20%, #cacaca 80%"), [("#adadad", 0.2), ("#cacaca", 0.8)])

    def test_missing_positions_spread_between_known_ones(self):
        self.assertEqual([p for _, p in gradient_stops("#000, #111, #222 50%, #333")], [0.0, 0.25, 0.5, 1.0])

    def test_unreadable_stop_raises(self):
        with self.assertRaises(ValueError):
            gradient_stops("#000 10px")


if __name__ == "__main__":
    unittest.main()
