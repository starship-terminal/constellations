"""tokens.json matches an in-memory build, and its pins hold the values taken on 2026-11-19 (literal
pins, not a comparison with raw/: raw/readings.md is prose)."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


class RiseTokens(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        import build_tokens  # build() returns the tree; only write() touches tokens.json
        self.assertEqual(TOKENS, json.loads(json.dumps(build_tokens.build())))

    def test_unpainted_hairline_is_gone(self):
        # The unset border colour on border-width 0 elements is not a painted edge.
        self.assertNotIn("hairline", TOKENS["light"]["border"])

    def test_primary_is_the_declared_triplet(self):
        self.assertEqual(TOKENS["light"]["color"]["primary"]["$value"], "#7161ec")

    def test_one_theme(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([theme["id"] for theme in TOKENS["$themes"]], ["light"])

    def test_button_height(self):
        self.assertEqual(TOKENS["core"]["size"]["button-sm"]["$value"], "34px")

    def test_every_token_has_a_source(self):
        def walk(node):
            for key, value in node.items():
                if key.startswith("$"):
                    continue
                if isinstance(value, dict) and "$value" in value:
                    self.assertIn("source", value.get("$extensions", {}), key)
                elif isinstance(value, dict):
                    walk(value)
        walk(TOKENS["core"])
        walk(TOKENS["light"])


if __name__ == "__main__":
    unittest.main()
