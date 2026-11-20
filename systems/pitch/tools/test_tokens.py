"""Pitch tokens stay inside the colours that raw/ holds, unless a token says it was entered by hand."""
import json
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())

RAW = ROOT / "raw"


def raw_colours():
    """Every colour in raw/*.json, as lower-case hex: #rgb, #rrggbb, rgb() and rgba()."""
    found = set()

    def walk(node):
        if isinstance(node, dict):
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)
        elif isinstance(node, str):
            low = node.lower()
            for m in re.finditer(r"#([0-9a-f]{3}|[0-9a-f]{6}|[0-9a-f]{8})\b", low):
                h = m.group(1)
                found.add("#" + ("".join(c * 2 for c in h) if len(h) == 3 else h))
            for m in re.finditer(r"rgba?\(\s*(\d+)[ ,]+(\d+)[ ,]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", low):
                r, g, b, a = m.groups()
                h = "#" + "".join(f"{int(x):02x}" for x in (r, g, b))
                if a is not None and float(a) < 1:
                    h += f"{math.floor(float(a) * 255 + 0.5):02x}"
                found.add(h)

    for path in sorted(RAW.glob("*.json")):
        walk(json.loads(path.read_text()))
    return found


MEASURED = raw_colours()


def colours(node):
    """Every literal colour value whose source does not say it was entered by hand."""
    if isinstance(node, dict):
        if node.get("$type") == "color" and isinstance(node.get("$value"), str):
            value = node["$value"]
            source = str(node.get("$extensions", {}).get("source", ""))
            if not value.startswith("{") and not source.startswith("Reconstruction"):
                yield value.lower()
        for child in node.values():
            yield from colours(child)


class Tokens(unittest.TestCase):
    def test_every_literal_colour_was_measured(self):
        found = set(colours(TOKENS))
        self.assertTrue(found, "no colour tokens")
        self.assertEqual(found - MEASURED, set())

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}" if path else key)

        walk(TOKENS, "")
        self.assertEqual(missing, [])

    def test_light_theme_only(self):
        self.assertIn("light", TOKENS)
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light"])

    def test_cover_screenshot_exists(self):
        self.assertTrue((ROOT / "screenshots" / "home-light-default.png").is_file())
        self.assertTrue((ROOT / "screenshots" / "login-light-default.png").is_file())


if __name__ == "__main__":
    unittest.main()
