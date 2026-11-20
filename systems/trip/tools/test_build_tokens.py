"""The Trip token builder keeps measured colours and does not invent a dark theme."""
import json
import unittest
from pathlib import Path

import build_tokens

HERE = Path(__file__).resolve().parent.parent


class BuildTokens(unittest.TestCase):
    def test_brand_aliases_to_blue6(self):
        data = build_tokens.build()
        self.assertEqual(data["light"]["color"]["bg-brand"]["$value"], "{core.color.blue6}")
        self.assertEqual(data["core"]["color"]["blue6"]["$value"].lower(), "#2c61fe")
        self.assertEqual(data["light"]["color"]["text-primary"]["$value"], "{core.color.neutral10}")

    def test_no_dark_set(self):
        data = build_tokens.build()
        self.assertEqual(set(data) - {"$themes"}, {"core", "light"})
        self.assertEqual(data["$themes"][0]["id"], "light")

    def test_body_m_matches_the_shorthand(self):
        data = build_tokens.build()
        body = data["core"]["typography"]["body-m"]["$value"]
        self.assertEqual(body["fontSize"], "14px")
        self.assertEqual(body["fontWeight"], 400)
        self.assertEqual(body["lineHeight"], 1.5)
        self.assertIn("Trip Geom", body["fontFamily"])

    def test_written_file_matches_builder(self):
        # The whole committed file, built in memory.
        self.assertEqual(json.loads((HERE / "tokens.json").read_text()), build_tokens.build())

    def test_colours_are_hex(self):
        import re

        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                yield node
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        yield from walk(v)
        for token in walk(build_tokens.build()):
            if token["$type"] == "color" and not token["$value"].startswith("{"):
                self.assertRegex(token["$value"], r"^#[0-9a-f]{6}([0-9a-f]{2})?$")
        self.assertEqual(build_tokens.to_hex("hsla(0,0%,100%,0.96)"), "#fffffff5")

    def test_search_card_shadow_is_the_computed_colour(self):
        shadow = build_tokens.build()["light"]["shadow"]["search-card"]
        self.assertTrue(shadow["$value"].startswith("0px 0px 4px 0px rgba(7, 20, 60, 0.16)"))


if __name__ == "__main__":
    unittest.main()
