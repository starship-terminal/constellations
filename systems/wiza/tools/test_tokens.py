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

    def test_families_are_names_not_files(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertIn("Britti Sans", core["font.family.display"])
        self.assertNotIn("woff", core["font.family.display"])


if __name__ == "__main__":
    unittest.main()
