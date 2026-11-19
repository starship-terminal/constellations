"""The Runey tokens resolve, and the measured colours stay the measured colours."""

import json
import unittest
from pathlib import Path

TOKENS = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())


def resolve(value, seen=None):
    if not isinstance(value, str) or not value.startswith("{") or not value.endswith("}"):
        return value
    seen = seen or set()
    path = value[1:-1]
    if path in seen:
        raise AssertionError(f"alias loop at {path}")
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return resolve(node["$value"], seen | {path})


class Tokens(unittest.TestCase):
    def test_measured_colours(self):
        self.assertEqual(TOKENS["core"]["color"]["page"]["$value"], "#fafafa")
        self.assertEqual(TOKENS["core"]["color"]["foreground"]["$value"], "#1a1a1a")
        self.assertEqual(TOKENS["core"]["color"]["primary"]["$value"], "#292929")
        self.assertEqual(TOKENS["core"]["color"]["primary-light"]["$value"], "#575757")
        self.assertEqual(TOKENS["core"]["color"]["muted"]["$value"], "#757575")
        self.assertEqual(TOKENS["core"]["color"]["border"]["$value"], "#ebebeb")

    def test_aliases_resolve(self):
        self.assertEqual(resolve(TOKENS["light"]["surface"]["page"]["$value"]), "#fafafa")
        self.assertEqual(resolve(TOKENS["light"]["text"]["primary"]["$value"]), "#1a1a1a")
        self.assertEqual(resolve(TOKENS["light"]["accent"]["$value"]), "#292929")
        self.assertEqual(resolve(TOKENS["dark"]["surface"]["page"]["$value"]), "#0d0d0d")
        self.assertEqual(resolve(TOKENS["dark"]["accent"]["$value"]), "#d9d9d9")

    def test_themes(self):
        names = [theme["name"] for theme in TOKENS["$themes"]]
        self.assertEqual(names, ["light", "dark"])

    def test_radius_and_type(self):
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$value"], "9999px")
        self.assertEqual(TOKENS["core"]["typography"]["hero"]["$value"]["fontSize"], "64px")
        self.assertEqual(TOKENS["core"]["motion"]["duration"]["fast"]["$value"], "150ms")


if __name__ == "__main__":
    unittest.main()
