"""Tokens in this package resolve and match the readings they cite."""
import json
import pathlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
READINGS = json.loads((ROOT / "raw" / "readings.json").read_text())


class Tokens(unittest.TestCase):
    def test_marketing_accent_is_the_computed_cta(self):
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#0061fe")
        bg = READINGS["pages"]["https://reclaim.ai/"]["getStarted"]["backgroundColor"]
        self.assertEqual(bg, "rgb(0, 97, 254)")

    def test_login_page_is_the_dark_field(self):
        self.assertEqual(TOKENS["dark"]["page"]["$value"], "#171d26")
        self.assertEqual(
            READINGS["pages"]["https://app.reclaim.ai/login"]["body"]["backgroundColor"],
            "rgb(23, 29, 38)",
        )

    def test_radius_control_matches_the_nav_button(self):
        self.assertEqual(TOKENS["core"]["radius"]["control"]["$value"], "10px")
        self.assertEqual(
            READINGS["pages"]["https://reclaim.ai/"]["getStarted"]["borderRadius"],
            "10px",
        )

    def test_signup_was_not_entered(self):
        self.assertEqual(READINGS["pages"]["https://app.reclaim.ai/login"]["entered"], "nothing")
        self.assertIn("No email field", READINGS["pages"]["https://app.reclaim.ai/login"]["text"])

class Sources(unittest.TestCase):
    """EVIDENCE.md makes a source mandatory on every token."""

    def test_every_token_has_a_source(self):
        doc = json.loads((pathlib.Path(__file__).resolve().parent.parent / "tokens.json").read_text())
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not (node.get("$extensions") or {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        walk(v, f"{path}.{k}" if path else k)

        for name, tree in doc.items():
            if not name.startswith("$"):
                walk(tree, name)
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
