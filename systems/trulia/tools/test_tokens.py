"""Provenance checks for the Trulia homepage tokens."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
RAW = json.loads((ROOT / "raw" / "homepage-computed.json").read_text())


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value, f"{path}.{key}" if path else key)


class TokenTests(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = [path for path, token in walk(TOKENS) if not token.get("$extensions", {}).get("source")]
        self.assertEqual(missing, [])

    def test_painted_accent_is_primary_dark(self):
        accent = TOKENS["light"]["color"]["accent"]["$value"]
        self.assertEqual(accent, "{color.tarzana.700}")
        self.assertEqual(TOKENS["core"]["color"]["tarzana"]["700"]["$value"], "#007882")
        self.assertEqual(RAW["computedCustomProperties"]["--colors-primary-dark"], "rgb(0, 120, 130)")

    def test_body_ink_matches_the_reading(self):
        self.assertEqual(TOKENS["core"]["color"]["grey"]["900"]["$value"], "#3b4144")
        self.assertEqual(RAW["elements"]["body"]["color"], "rgb(59, 65, 68)")

    def test_control_radius_is_8(self):
        self.assertEqual(TOKENS["core"]["radius"]["m"]["$value"], "8px")
        self.assertEqual(RAW["elements"]["primaryCta"]["borderRadius"], "8px")

    def test_no_dark_theme_was_invented(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([theme["id"] for theme in TOKENS["$themes"]], ["light"])


if __name__ == "__main__":
    unittest.main()
