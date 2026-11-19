"""Teachable tokens carry a measured source and resolve."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if not key.startswith("$"):
                yield from walk(child, f"{path}.{key}" if path else key)


class TokensTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = [path for path, token in walk(TOKENS) if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_accent_is_the_measured_chartreuse(self):
        self.assertEqual(TOKENS["core"]["color"]["brand"]["yellow"]["$value"], "#e6ff32")
        self.assertEqual(TOKENS["light"]["color"]["action"]["fill"]["$value"], "{color.brand.yellow}")

    def test_light_is_the_only_theme(self):
        self.assertIn("light", TOKENS)
        self.assertNotIn("dark", TOKENS)


if __name__ == "__main__":
    unittest.main()
