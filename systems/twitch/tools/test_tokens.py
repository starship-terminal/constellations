"""Shape checks for the Twitch token file. Not a grader."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parents[1] / "tokens.json"


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_sets(self):
        self.assertEqual(set(self.data), {"core", "dark", "$themes"})
        themes = {t["id"]: t["selectedTokenSets"] for t in self.data["$themes"]}
        self.assertEqual(themes["dark"]["core"], "source")
        self.assertEqual(themes["dark"]["dark"], "enabled")
        self.assertNotIn("light", themes)

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
        walk(self.data["dark"], "dark")
        self.assertEqual(missing, [])

    def test_measured_brand(self):
        accent = self.data["dark"]["color"]["accent"]["default"]["$value"]
        self.assertEqual(accent, "#9147ff")
        page = self.data["dark"]["color"]["background"]["page"]["$value"]
        self.assertEqual(page, "#0e0e10")


if __name__ == "__main__":
    unittest.main()
