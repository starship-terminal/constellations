#!/usr/bin/env python3
"""Check tokens.json against the measured readings. No network."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tokens = json.loads((HERE / "tokens.json").read_text())
        cls.raw = json.loads((HERE / "raw" / "measured.json").read_text())

    def test_light_only(self):
        self.assertEqual(set(self.tokens) - {"$themes"}, {"core", "light"})
        self.assertNotIn("dark", self.tokens)

    def test_accent_matches_blue_50(self):
        accent = self.tokens["light"]["background"]["action"]["$value"]
        blue = self.tokens["core"]["color"]["blue"]["50"]["$value"]
        self.assertEqual(accent, "#1a91f0")
        self.assertEqual(blue, accent)

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}")

        walk(self.tokens, "")
        self.assertEqual(missing, [])

    def test_spacing_scale_is_the_declared_one(self):
        got = {k: v["$value"] for k, v in self.tokens["core"]["spacing"].items()}
        self.assertEqual(got["m"], "24px")
        self.assertEqual(got["s"], "16px")
        self.assertEqual(len(got), len(self.raw["spacing"]))

    def test_page_ground_is_neutral_10(self):
        self.assertEqual(self.tokens["light"]["background"]["page"]["$value"], "#eff2f9")
        self.assertEqual(self.tokens["core"]["color"]["neutral"]["10"]["$value"], "#eff2f9")


if __name__ == "__main__":
    unittest.main()
