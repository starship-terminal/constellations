"""Confirm every Vercel token carries a source string."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parents[1] / "tokens.json"


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value, f"{path}.{key}" if path else key)


class TokenSourceTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        data = json.loads(TOKENS.read_text())
        missing = [path for path, node in walk(data) if not (node.get("$extensions") or {}).get("source")]
        self.assertEqual(missing, [])

    def test_both_themes_have_a_page(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["dark"]["surface"]["page"]["$value"], "#000000")
        self.assertEqual(data["dark"]["text"]["primary"]["$value"], "#ededed")
        self.assertEqual(data["light"]["surface"]["page"]["$value"], "#fafafa")
        self.assertEqual(data["light"]["text"]["primary"]["$value"], "#171717")


if __name__ == "__main__":
    unittest.main()
