"""The Pattern Brands token file resolves, and the measured page colours are the ones that were read."""
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
    def test_page_colour_is_the_measured_white(self):
        self.assertEqual(resolve(FLAT["light.background.page"]), "#ffffff")

    def test_primary_text_is_the_measured_ink(self):
        self.assertEqual(resolve(FLAT["light.text.primary"]), "#1e1e1e")

    def test_action_is_the_measured_green(self):
        self.assertEqual(resolve(FLAT["light.background.action"]), "#084935")

    def test_page_title_is_the_legal_h1(self):
        self.assertEqual(FLAT["core.typography.page-title"]["fontSize"], "48px")

    def test_every_alias_resolves(self):
        for path, value in FLAT.items():
            if isinstance(value, str) and value.startswith("{"):
                resolve(value)
            if isinstance(value, dict):
                for item in value.values():
                    if isinstance(item, str) and item.startswith("{"):
                        resolve(item)

    def test_every_token_has_a_source(self):
        # docs/EVIDENCE.md: every value says where it came from.
        doc = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}" if path else key)

        walk(doc, "")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
