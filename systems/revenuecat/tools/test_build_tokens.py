"""Checks for the RevenueCat token build. Run from this package's tools/ folder."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        tokens = build_tokens.build()
        build_tokens.relabel_unread(tokens)
        self.assertEqual(json.loads(TOKENS.read_text()), json.loads(json.dumps(tokens)))

    def test_app_ramps_say_they_were_typed_in(self):
        # The --rc-* ramps were read as hex in the capture session but raw/readings.json does not store them.
        step = json.loads(TOKENS.read_text())["core"]["color"]["app"]["pink"]["10"]["$extensions"]["source"]
        self.assertEqual(step["evidence"], "Reconstruction")

    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_marketing_page_is_white(self):
        tokens = json.loads(TOKENS.read_text())
        self.assertEqual(tokens["light"]["background"]["page"]["$value"], "{color.marketing.color-white}")
        self.assertEqual(tokens["core"]["color"]["marketing"]["color-white"]["$value"], "#ffffff")

    def test_app_dark_surface_is_the_login_field(self):
        tokens = json.loads(TOKENS.read_text())
        self.assertEqual(tokens["dark"]["background"]["surface"]["$value"], "{color.app.neutral.100}")
        self.assertEqual(tokens["core"]["color"]["app"]["neutral"]["100"]["$value"], "#14161b")

    def test_every_token_names_a_source(self):
        tokens = json.loads(TOKENS.read_text())
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if "source" not in node.get("$extensions", {}):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if not key.startswith("$"):
                        walk(value, f"{path}.{key}" if path else key)

        for name in ("core", "light", "dark"):
            walk(tokens[name], name)
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
