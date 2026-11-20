"""The committed tokens.json matches the measured signed-out chrome."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads(TOKENS.read_text())

    def test_action_is_measured_razzmatazz(self):
        self.assertEqual(self.doc["core"]["color"]["razzmatazz"]["$value"], "#fe2c55")
        self.assertEqual(self.doc["dark"]["background"]["action"]["$value"], "{color.razzmatazz}")

    def test_page_is_black(self):
        self.assertEqual(self.doc["core"]["color"]["page"]["$value"], "#000000")
        self.assertEqual(self.doc["dark"]["background"]["page"]["$value"], "{color.page}")

    def test_selected_nav_is_primary(self):
        self.assertEqual(self.doc["core"]["color"]["primary"]["$value"], "#ff3b5c")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source", {})
                if "evidence" not in source:
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if not key.startswith("$"):
                        walk(value, f"{path}.{key}" if path else key)

        walk(self.doc["core"], "core")
        walk(self.doc["dark"], "dark")
        self.assertEqual(missing, [])

    def test_ease_keyword_is_derived(self):
        ease = self.doc["core"]["motion"]["easing"]["ease"]
        self.assertEqual(ease["$extensions"]["source"]["evidence"], "Derived")
        self.assertEqual(ease["$value"], [0.25, 0.1, 0.25, 1])


if __name__ == "__main__":
    unittest.main()
