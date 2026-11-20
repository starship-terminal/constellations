"""Pinterest token file holds the values measured on the public homepage."""
import json
import unittest
from pathlib import Path

TOKENS = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())


def get(path):
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return node["$value"]


class Tokens(unittest.TestCase):
    def test_primary_red(self):
        self.assertEqual(get("light.background.action"), "{palette.brand.pinterest}")
        self.assertEqual(get("core.palette.brand.pinterest"), "#e60023")

    def test_page_is_white(self):
        self.assertEqual(get("light.background.page"), "{palette.grayscale.0}")
        self.assertEqual(get("core.palette.grayscale.0"), "#ffffff")

    def test_button_radius(self):
        self.assertEqual(get("light.component.button.radius"), "16px")

    def test_catalog_paths(self):
        self.assertEqual(get("light.text.subtle"), "{palette.grayscale.300}")
        self.assertEqual(get("light.border.stroke"), "{palette.grayscale.150}")
        self.assertIn("Pin Sans", get("core.font.family.pin-sans"))

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if "source" not in node.get("$extensions", {}):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, path + "." + key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        walk(TOKENS["dark"], "dark")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
