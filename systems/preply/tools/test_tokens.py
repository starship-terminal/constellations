"""Preply token checks. Run from the package tools directory."""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402
import token_checks  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


class TokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        # build() returns the document without writing tokens.json or anything under raw/.
        self.assertEqual(T, build_tokens.build())

    def test_no_dead_aliases(self):
        self.assertEqual(token_checks.alias_errors(T["core"], T["light"]), [])

    def test_every_token_has_a_source(self):
        for theme in ("core", "light"):
            for name, tok in token_checks.tokens_of(T[theme]):
                src = tok.get("$extensions", {}).get("source", "")
                self.assertTrue(src, f"{theme}.{name} has no source")

    def test_one_theme(self):
        self.assertNotIn("dark", T)
        self.assertEqual(T["$metadata"]["tokenSetOrder"], ["core", "light"])

    def test_measured_pink_and_ink(self):
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(light["color.bg.pink"], "#ff7aac")
        self.assertEqual(light["color.text.primary"], "#121117")
        self.assertEqual(light["color.action.focus"], "#006af5")


if __name__ == "__main__":
    unittest.main()
