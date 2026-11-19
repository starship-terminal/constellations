"""Memotron token checks. The dark semantic colours are the rounded sRGB of
the --colors-* triplets declared on .cs_tidigit_dark_blue."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_dark_matches_computed_page(self):
        dark = TOKENS["dark"]
        self.assertEqual(dark["background"]["page"]["$value"], "#1f222e")
        self.assertEqual(dark["background"]["surface"]["$value"], "#151823")
        self.assertEqual(dark["text"]["primary"]["$value"], "#f2f2f2")
        self.assertEqual(dark["text"]["secondary"]["$value"], "#c9c9c9")
        self.assertEqual(dark["accent"]["primary"]["$value"], "#2c70dd")
        self.assertEqual(dark["border"]["strong"]["$value"], "#34384c")

    def test_light_text_is_near_black(self):
        self.assertEqual(TOKENS["light"]["text"]["primary"]["$value"], "#333333")
        self.assertEqual(TOKENS["light"]["background"]["surface"]["$value"], "#ffffff")

    def test_hero_is_the_authored_44(self):
        self.assertEqual(TOKENS["core"]["typography"]["hero-font-size"]["$value"], "44px")
        self.assertEqual(TOKENS["core"]["typography"]["hero-font-weight"]["$value"], 500)

    def test_every_token_has_a_source(self):
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


if __name__ == "__main__":
    unittest.main()
