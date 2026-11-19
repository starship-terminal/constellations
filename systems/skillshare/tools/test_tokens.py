#!/usr/bin/env python3
"""Skillshare tokens stay inside the measured set."""
import json, pathlib, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())

MEASURED = {
    "#ffffff", "#000000", "#0b1215", "#394649", "#dcdce1", "#55da9b",
    "#50cf93", "#5620c1", "#fafafa", "#f4f4f4", "#070c0e", "#002333",
    "#232424",
}


class Tokens(unittest.TestCase):
    def test_light_only(self):
        self.assertEqual([t["id"] for t in T["$themes"]], ["light"])
        self.assertNotIn("dark", T)

    def test_accent_is_measured_mint(self):
        self.assertEqual(T["light"]["color"]["accent"]["$value"], "#55da9b")
        self.assertEqual(T["light"]["color"]["link"]["$value"], "#5620c1")

    def test_hex_colours_were_measured(self):
        for name, tok in T["light"]["color"].items():
            value = tok["$value"]
            if isinstance(value, str) and value.startswith("#"):
                self.assertIn(value, MEASURED, name)

    def test_control_radius(self):
        self.assertEqual(T["core"]["radius"]["control"]["$value"], "4px")


if __name__ == "__main__":
    unittest.main()
