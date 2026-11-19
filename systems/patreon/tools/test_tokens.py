"""Patreon token checks. Run from the package tools/ directory."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
TOKENS = json.loads((HERE.parent / "tokens.json").read_text())
RAW = json.loads((HERE.parent / "raw" / "computed.json").read_text())


class TokenTest(unittest.TestCase):
    def test_primary_matches_reading(self):
        self.assertEqual(TOKENS["core"]["color"]["primary"]["$value"], RAW["resolved"]["--color-primary"])

    def test_button_height_matches_desktop(self):
        self.assertEqual(
            TOKENS["core"]["size"]["button"]["$value"],
            RAW["computed"]["desktop1440"]["getStarted"]["height"],
        )

    def test_login_page_is_measured(self):
        self.assertEqual(TOKENS["light"]["color"]["login"]["page"]["$value"], "#020202")
        self.assertEqual(RAW["computed"]["login"]["htmlBackground"], "rgb(2, 2, 2)")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if "source" not in node.get("$extensions", {}):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}" if path else key)

        walk(TOKENS, "")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
