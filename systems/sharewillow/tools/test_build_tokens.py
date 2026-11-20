#!/usr/bin/env python3
"""The builder writes tokens that match the raw readings."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class BuildTokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        # Built in memory; importing the builder writes nothing.
        import sys
        sys.path.insert(0, str(HERE / "tools"))
        import build_tokens
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.render())

    def test_band_is_part_of_the_light_page_not_a_theme(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertNotIn("dark", tokens)
        self.assertEqual([t["id"] for t in tokens["$themes"]], ["light"])
        self.assertEqual(tokens["light"]["band"]["bg"]["page"]["$value"], "#0d0a07")

    def test_light_page_is_the_measured_ivory(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        theme = json.loads((HERE / "raw" / "theme.css.json").read_text())
        self.assertEqual(tokens["light"]["bg"]["page"]["$value"], theme["properties"]["--color-bg"])
        self.assertEqual(tokens["light"]["text"]["primary"]["$value"], "#180600")
        self.assertEqual(tokens["light"]["accent"]["default"]["$value"], "#faf082")

    def test_login_link_is_the_resolved_brand_accent(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        login = json.loads((HERE / "raw" / "login-tokens.json").read_text())
        self.assertEqual(tokens["light"]["app"]["link"]["$value"], login["tokens"]["--brand-accent"]["rgb"])

    def test_every_token_has_a_source(self):
        tokens = json.loads((HERE / "tokens.json").read_text())

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source", "")
                self.assertTrue(source.startswith("raw/"), path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, path + "." + key)

        walk(tokens["core"], "core")
        walk(tokens["light"], "light")

    def test_gaps_are_recorded_not_filled(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        gaps = " ".join(tokens["$extensions"]["notTokenised"])
        self.assertIn("screenshot", gaps)
        self.assertIn("checkbox", gaps)
        self.assertIn("Phone", gaps)


if __name__ == "__main__":
    unittest.main()
