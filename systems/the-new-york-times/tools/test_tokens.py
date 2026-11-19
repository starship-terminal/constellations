#!/usr/bin/env python3
"""The New York Times package: painted colours match the readings."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
COMPUTED = json.loads((ROOT / "raw" / "computed.json").read_text())


def walk(node, path=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        here = f"{path}.{key}" if path else key
        if isinstance(value, dict) and "$value" in value:
            yield here, value
        elif isinstance(value, dict):
            yield from walk(value, here)


class TokensTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = [path for path, token in walk(TOKENS) if not token.get("$extensions", {}).get("source")]
        self.assertEqual(missing, [])

    def test_painted_masthead_and_action(self):
        self.assertEqual(TOKENS["core"]["color"]["masthead"]["$value"], "#567b95")
        self.assertEqual(TOKENS["core"]["color"]["ink"]["$value"], "#121212")
        self.assertEqual(TOKENS["core"]["color"]["accent"]["$value"], "#346eb7")
        self.assertEqual(COMPUTED["home"]["subscribe"]["backgroundColor"], "rgb(86, 123, 149)")
        self.assertEqual(COMPUTED["login"]["continue"]["backgroundColor"], "rgb(18, 18, 18)")
        self.assertEqual(COMPUTED["login"]["field"]["wrapBorder"], "1px solid rgb(0, 0, 0)")

    def test_only_light_theme_was_painted(self):
        self.assertEqual(list(TOKENS["$themes"]), [{"id": "light", "name": "Light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}}])
        self.assertNotIn("dark", TOKENS)


if __name__ == "__main__":
    unittest.main()
