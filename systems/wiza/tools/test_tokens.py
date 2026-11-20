"""Tests for the Wiza token sets.

Run from the package tools directory, which is what tools/package_tests.py does.
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import token_checks  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


class TokensTest(unittest.TestCase):
    def test_no_dead_aliases(self):
        errors = token_checks.alias_errors(T["core"], T["light"])
        self.assertEqual(errors, [])

    def test_every_token_has_a_source(self):
        for theme in ("core", "light"):
            for name, tok in token_checks.tokens_of(T[theme]):
                src = tok.get("$extensions", {}).get("source", "")
                self.assertTrue(src, f"{theme}.{name} has no $extensions.source")

    def test_one_theme_only(self):
        self.assertNotIn("dark", T)
        self.assertEqual(T["$metadata"]["tokenSetOrder"], ["core", "light"])
        self.assertEqual([t["id"] for t in T["$themes"]], ["light"])

    def test_measured_brand_ink(self):
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(light["color.ink"], "#26114a")
        self.assertEqual(light["color.accent"], "#7e43ff")
        self.assertEqual(light["component.buttonPrimary.background"], "#26114a")
        self.assertEqual(light["component.authSubmit.background"], "#7e43ff")

    def test_committed_file_matches_builder(self):
        # Importing the builder writes nothing; render() is the file's text.
        import build_tokens
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.render())

    def test_colours_are_hex_and_dimensions_one_length(self):
        import re
        for theme in ("core", "light"):
            for name, tok in token_checks.tokens_of(T[theme]):
                value = tok["$value"]
                if isinstance(value, str) and value.startswith("{"):
                    continue
                if tok["$type"] == "color":
                    self.assertRegex(value, r"^#[0-9a-f]{6}([0-9a-f]{2})?$", name)
                if tok["$type"] == "dimension":
                    self.assertRegex(value, r"^-?(\d+(\.\d+)?|\.\d+)(px|rem)$", name)
        self.assertEqual(T["core"]["color"]["neutral"]["25"]["$value"], "#1d4f810a")

    def test_type_steps_claim_no_unread_tracking(self):
        for name, tok in token_checks.tokens_of(T["core"]["typography"]):
            self.assertNotIn("letterSpacing", tok["$value"], name)
            self.assertTrue(tok["$extensions"]["source"].startswith("Reconstruction: lineHeight"), name)
        display = T["core"]["typography"]["display"]["$value"]
        self.assertEqual((display["fontSize"], display["lineHeight"]), ("80px", "80px"))

    def test_families_are_names_not_files(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertIn("Britti Sans", core["font.family.display"])
        self.assertNotIn("woff", core["font.family.display"])


if __name__ == "__main__":
    unittest.main()
