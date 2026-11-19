"""The Spline tokens resolve, and the measured colours are the ones that were read."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


def load():
    return json.loads(TOKENS.read_text())


def lookup(data, path):
    node = data
    for part in path.split("."):
        node = node[part]
    value = node["$value"]
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return lookup(data, value[1:-1])
    return value


class Tokens(unittest.TestCase):
    def test_measured_colours(self):
        data = load()
        self.assertEqual(lookup(data, "dark.background.page"), "#000000")
        self.assertEqual(lookup(data, "dark.background.surface"), "#101010")
        self.assertEqual(lookup(data, "dark.text.primary"), "#eeeeee")
        self.assertEqual(lookup(data, "dark.text.secondary"), "#8a8a8a")
        self.assertEqual(lookup(data, "dark.background.action"), "#eeeeee")
        self.assertEqual(lookup(data, "dark.border.stroke"), "#2e2e2e")

    def test_button_aliases_resolve(self):
        data = load()
        self.assertEqual(lookup(data, "dark.component.button.bg"), "#eeeeee")
        self.assertEqual(lookup(data, "dark.component.button.radius"), "999px")
        self.assertEqual(lookup(data, "dark.component.button.height"), "44px")

    def test_type_uses_the_computed_hero(self):
        data = load()
        display = lookup(data, "core.typography.display")
        self.assertEqual(display["fontSize"], "72px")
        self.assertEqual(display["fontWeight"], 450)
        self.assertEqual(display["letterSpacing"], "-4.32px")

    def test_one_dark_theme(self):
        data = load()
        self.assertEqual([t["id"] for t in data["$themes"]], ["dark"])
        self.assertNotIn("light", data)


if __name__ == "__main__":
    unittest.main()
