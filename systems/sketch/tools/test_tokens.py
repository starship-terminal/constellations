"""Sketch package checks. Run from the package tools folder by package_tests.py."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, f"{path}.{key}" if path else key)


class TokenTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = [path for path, node in walk(TOKENS) if not (node.get("$extensions") or {}).get("source")]
        self.assertEqual(missing, [])

    def test_measured_page_colour(self):
        self.assertEqual(TOKENS["light"]["background"]["page"]["$value"], "#f5f5f5")
        self.assertEqual(TOKENS["light"]["text"]["primary"]["$value"], "#212123")
        self.assertEqual(TOKENS["dark"]["background"]["page"]["$value"], "#2d2d2f")

    def test_button_radius_is_the_computed_value(self):
        self.assertEqual(TOKENS["core"]["radius"]["button"]["$value"], "24px")


if __name__ == "__main__":
    unittest.main()
