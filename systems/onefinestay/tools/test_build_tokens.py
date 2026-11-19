#!/usr/bin/env python3
"""The Onefinestay token file still matches the readings the builder encodes."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_coral_search_and_rust_booking_stay_apart(self):
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#ff8065")
        self.assertEqual(TOKENS["light"]["brand"]["900"]["$value"], "#c84908")

    def test_painted_text_is_neutral_900(self):
        self.assertEqual(TOKENS["light"]["text"]["primary"]["$value"], "#26232a")
        self.assertEqual(TOKENS["light"]["surface"]["footer"]["$value"], "#3b393f")

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

    def test_radius_and_motion_match_the_page(self):
        self.assertEqual(TOKENS["core"]["radius"]["xs"]["$value"], "2px")
        self.assertEqual(TOKENS["core"]["motion"]["duration"]["default"]["$value"], "200ms")
        self.assertEqual(TOKENS["core"]["typography"]["display"]["$value"]["fontSize"], "64px")


if __name__ == "__main__":
    unittest.main()
