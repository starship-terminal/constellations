#!/usr/bin/env python3
"""Squarespace tokens stay inside the measured set."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())

MEASURED = {
    "#ffffff", "#000000", "#0e0e0e", "#666666", "#5a5a5a", "#898989",
    "#adadad", "#b7b7b7", "#f2f2f2", "#dddddd", "#0072f0", "#242424",
    "#e7e7e7", "#c32d38", "#f9f9f9",
}


class Tokens(unittest.TestCase):
    def test_light_only(self):
        self.assertEqual([theme["id"] for theme in T["$themes"]], ["light"])
        self.assertNotIn("dark", T)

    def test_accent_is_measured_blue(self):
        self.assertEqual(T["light"]["color"]["accent"]["$value"], "#0072f0")
        self.assertEqual(T["light"]["color"]["ink"]["$value"], "#000000")

    def test_hex_colours_were_measured(self):
        for name, tok in T["light"]["color"].items():
            value = tok["$value"]
            if isinstance(value, str) and value.startswith("#"):
                self.assertIn(value, MEASURED, name)

    def test_control_radius(self):
        self.assertEqual(T["core"]["radius"]["control"]["$value"], "4px")
        self.assertEqual(T["core"]["radius"]["none"]["$value"], "0px")


if __name__ == "__main__":
    unittest.main()
