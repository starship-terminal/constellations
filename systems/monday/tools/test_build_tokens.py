#!/usr/bin/env python3
"""The Monday token file still matches the readings the builder encodes."""
import json
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_product_blue_and_marketing_purple_stay_apart(self):
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#0073ea")
        self.assertEqual(TOKENS["light"]["marketing"]["accent"]["$value"], "#6161ff")

    def test_dark_page_is_the_declared_navy(self):
        self.assertEqual(TOKENS["dark"]["background"]["page"]["$value"], "#181b34")

    def test_every_token_names_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if "source" not in node.get("$extensions", {}):
                    missing.append(".".join(path))
                return
            if isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        walk(v, path + [k])

        walk(TOKENS, [])
        self.assertEqual(missing, [])

    def test_radius_and_motion_match_the_login_sheet(self):
        self.assertEqual(TOKENS["core"]["radius"]["small"]["$value"], "4px")
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$value"], "160px")
        self.assertEqual(TOKENS["core"]["motion"]["duration"]["productive-short"]["$value"], "70ms")


class Builder(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        sys.path.insert(0, str(HERE / "tools"))
        import build_tokens  # writes only when run as a script
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.text)

    def test_missing_status_colour_fails(self):
        sys.path.insert(0, str(HERE / "tools"))
        import build_tokens
        saved = list(build_tokens.STATUS)
        try:
            build_tokens.STATUS.append(("nothing", "--color-nothing"))
            with self.assertRaises(SystemExit):
                build_tokens.status_group()
        finally:
            build_tokens.STATUS[:] = saved


if __name__ == "__main__":
    unittest.main()
