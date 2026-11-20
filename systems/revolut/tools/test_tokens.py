"""The public Revolut readings survive the token build."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_light_accent_is_the_home_page_value(self):
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#234fa6")

    def test_dark_accent_is_the_pricing_page_value(self):
        self.assertEqual(TOKENS["dark"]["accent"]["$value"], "#6fa0ff")

    def test_page_and_text_roles(self):
        self.assertEqual(TOKENS["light"]["background"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["light"]["foreground"]["$value"], "#1f1f1f")
        self.assertEqual(TOKENS["dark"]["background"]["$value"], "#000000")
        self.assertEqual(TOKENS["dark"]["foreground"]["$value"], "#ffffff")

    def test_radius_round_is_the_pill(self):
        self.assertEqual(TOKENS["core"]["radius"]["round"]["$value"], "9999px")

    def test_every_token_names_its_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                src = node.get("$extensions", {}).get("source")
                if not src:
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, path + "." + key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        walk(TOKENS["dark"], "dark")
        self.assertEqual(missing, [])



class Build(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        import sys
        sys.path.insert(0, str(HERE / "tools" / "build"))
        import build_tokens  # build() returns the tree; only write() touches tokens.json
        self.assertEqual(TOKENS, json.loads(json.dumps(build_tokens.build(), ensure_ascii=False)))

    def test_foundation_without_a_raw_file_is_not_measured(self):
        # No raw/foundation.json was kept, so the scales say Reconstruction.
        self.assertEqual(TOKENS["core"]["space"]["sp400"]["$extensions"]["evidence"], "Reconstruction")

    def test_easings_are_dtcg_numbers(self):
        for name, tok in TOKENS["core"]["motion"]["easing"].items():
            self.assertEqual(len(tok["$value"]), 4, name)

if __name__ == "__main__":
    unittest.main()
