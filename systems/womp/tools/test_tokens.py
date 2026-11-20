"""The committed tokens resolve, and the measured marketing colours are the ones recorded."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads(TOKENS.read_text())

    def test_sets(self):
        self.assertEqual(set(self.tokens), {"core", "light", "dark", "$themes"})

    def test_light_page_and_accent(self):
        light = self.tokens["light"]
        self.assertEqual(light["background"]["page"]["$value"], "#FFFFFF")
        self.assertEqual(light["text"]["primary"]["$value"], "#202020")
        self.assertEqual(light["accent"]["solid"]["$value"], "#202020")
        self.assertEqual(light["border"]["stroke"]["$value"], "#D9D9D9")

    def test_dark_footer(self):
        dark = self.tokens["dark"]
        self.assertEqual(dark["background"]["page"]["$value"], "#111111")
        self.assertEqual(dark["text"]["primary"]["$value"], "#EEEEEE")

    def test_display_step(self):
        display = self.tokens["core"]["typography"]["display"]["$value"]
        self.assertEqual(display["fontSize"], "64px")
        self.assertEqual(display["fontWeight"], "{fontWeight.semibold}")
        self.assertEqual(display["letterSpacing"], "-1.6px")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = (node.get("$extensions") or {}).get("source")
                if not source:
                    missing.append(".".join(path))
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if key == "$themes":
                        continue
                    walk(child, path + [key])

        walk(self.tokens, [])
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
