"""The Nomad Goods token file resolves, and the measured page colour is the one that was read."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def flatten(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        return {path: node["$value"]}
    out = {}
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            out.update(flatten(child, f"{path}.{key}" if path else key))
    return out


FLAT = flatten(TOKENS)


def resolve(value, depth=0):
    if depth > 8 or not isinstance(value, str) or not (value.startswith("{") and value.endswith("}")):
        return value
    ref = value[1:-1]
    if ref not in FLAT:
        raise AssertionError(f"missing alias {ref}")
    return resolve(FLAT[ref], depth + 1)


class TokenFile(unittest.TestCase):
    def test_page_colour_is_the_measured_grey(self):
        self.assertEqual(resolve(FLAT["light.background.page"]), "#f3f3f3")

    def test_primary_text_is_black(self):
        self.assertEqual(resolve(FLAT["light.text.primary"]), "#000000")

    def test_display_size_is_the_desktop_computed_size(self):
        self.assertEqual(FLAT["core.typography.display"]["fontSize"], "77px")

    def test_every_alias_resolves(self):
        for path, value in FLAT.items():
            if isinstance(value, str) and value.startswith("{"):
                resolve(value)
            if isinstance(value, dict):
                for item in value.values():
                    if isinstance(item, str) and item.startswith("{"):
                        resolve(item)


if __name__ == "__main__":
    unittest.main()
