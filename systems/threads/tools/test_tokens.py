"""Shape checks for the Threads token file. Not a grader."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parents[1] / "tokens.json"


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_sets(self):
        self.assertEqual(set(self.data), {"core", "light", "dark", "$themes"})
        themes = {t["id"]: t["selectedTokenSets"] for t in self.data["$themes"]}
        self.assertEqual(themes["light"]["core"], "source")
        self.assertEqual(themes["light"]["light"], "enabled")
        self.assertEqual(themes["dark"]["dark"], "enabled")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if not isinstance(node, dict):
                return
            if "$value" in node:
                source = (node.get("$extensions") or {}).get("source")
                if not isinstance(source, str) or not source:
                    missing.append(path)
                return
            for key, child in node.items():
                if key.startswith("$"):
                    continue
                walk(child, f"{path}.{key}" if path else key)

        walk(self.data["core"], "core")
        walk(self.data["light"], "light")
        walk(self.data["dark"], "dark")
        self.assertEqual(missing, [])

    def test_painted_login_button_is_not_the_blue_primary(self):
        dark = self.data["dark"]["color"]["control"]["button-background"]["$value"]
        light = self.data["light"]["color"]["control"]["button-background"]["$value"]
        self.assertEqual(dark.lower(), "#ffffff")
        self.assertEqual(light.lower(), "#000000")

    def test_measured_radii_are_present(self):
        radius = self.data["core"]["radius"]
        self.assertEqual(radius["login-field"]["$value"], "18px")
        self.assertEqual(radius["login-card"]["$value"], "24px")
        self.assertIn("Measured", radius["login-field"]["$extensions"]["source"])
        self.assertIn("Derived", self.data["core"]["spacing"]["1"]["$extensions"]["source"])


if __name__ == "__main__":
    unittest.main()
