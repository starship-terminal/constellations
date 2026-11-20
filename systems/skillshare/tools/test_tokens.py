"""Skillshare token checks. Run from systems/skillshare/tools."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_green_is_measured(self):
        leaf = TOKENS["core"]["color"]["green"]
        self.assertEqual(leaf["$value"], "#55da9b")
        self.assertIn("computed", leaf["$extensions"]["source"])

    def test_no_dark_set(self):
        self.assertNotIn("dark", TOKENS)

    def test_every_leaf_has_a_source(self):
        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                self.assertIn("source", node.get("$extensions", {}), path)
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        walk(v, path + "." + k)
        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")

    def test_screenshots_exist(self):
        shots = ROOT / "screenshots"
        self.assertTrue((shots / "home-light-default.png").is_file())
        self.assertTrue((shots / "login-light-default.png").is_file())
        self.assertTrue((shots / "mobile-home-light-default.png").is_file())


if __name__ == "__main__":
    unittest.main()
