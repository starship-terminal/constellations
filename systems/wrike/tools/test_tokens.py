"""Checks that the Wrike tokens match the readings in raw/."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
RAW = json.loads((HERE / "raw" / "components-computed.json").read_text())


def value(path):
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return node["$value"]


class Tokens(unittest.TestCase):
    def test_accent_matches_home_button(self):
        home = next(p for p in RAW["pages"] if p["name"] == "home")
        button = home["buttons"][0]
        self.assertEqual(button["bg"], "rgb(0, 224, 92)")
        self.assertEqual(value("light.color.action.fill"), "#00e05c")
        self.assertEqual(button["color"], "rgb(22, 33, 54)")
        self.assertEqual(value("light.color.text.on-accent"), "#162136")

    def test_display_matches_desktop_h1(self):
        home = next(p for p in RAW["pages"] if p["name"] == "home")
        self.assertEqual(home["h1"]["size"], "64px")
        self.assertEqual(value("core.typography.display")["fontSize"], "64px")
        self.assertEqual(value("core.typography.display")["fontWeight"], 600)

    def test_spacing_matches_1440_vars(self):
        home = next(p for p in RAW["pages"] if p["name"] == "home")
        self.assertEqual(home["vars"]["--website-spacing-1x"], "16px")
        self.assertEqual(value("core.spacing.1x"), "16px")
        self.assertEqual(home["viewport"]["w"], 1440)

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = (node.get("$extensions") or {}).get("source")
                if not source:
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, path + "." + key if path else key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
