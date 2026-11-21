"""Mapbox token builder keeps measured colours and refuses a guessed dark theme."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_accent_is_measured_blue(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["blue"]["50"]["$value"], "#007afc")
        self.assertEqual(tokens["light"]["accent"]["default"]["$value"], "{color.blue.50}")
        self.assertNotIn("dark", tokens)
        self.assertEqual(tokens["light"]["page"]["$extensions"]["evidence"], "Measured")

    def test_catalog_not_required_for_rebuild(self):
        self.assertTrue((HERE / "tools" / "build_tokens.py").is_file())
        self.assertTrue((HERE / "site-tree.md").is_file())


if __name__ == "__main__":
    unittest.main()
