"""The Polar builder reproduces tokens.json from raw/foundations.json, in memory.

Nothing here writes tokens.json: build() returns the document and the test compares it.
"""
import copy
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"
DATA = json.loads(TOKENS.read_text())


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
    elif isinstance(node, dict):
        for key, child in node.items():
            if not key.startswith("$"):
                yield from leaves(child, f"{path}.{key}" if path else key)


class TokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(DATA, build_tokens.build())

    def test_dark_page_and_accent(self):
        self.assertEqual(DATA["dark"]["surface"]["page"]["$value"], "#181818")
        self.assertEqual(DATA["dark"]["accent"]["$value"], "#155dfc")
        self.assertEqual(DATA["light"]["surface"]["page"]["$value"], "#ffffff")
        self.assertEqual(DATA["core"]["color"]["polar"]["950"]["$value"], "#090909")

    def test_status_comes_from_each_themes_reading(self):
        raw = build_tokens.RAW
        self.assertEqual(DATA["light"]["status"]["success"]["$value"], raw["semanticLightDocs"]["success"])
        self.assertEqual(DATA["dark"]["status"]["success"]["$value"], raw["semanticDark"]["success"])

    def test_a_missing_status_reading_fails_the_build(self):
        # No silent fallback to a ramp step: drop success from each theme's reading in turn.
        saved = build_tokens.RAW
        try:
            for theme in ("semanticDark", "semanticLightDocs"):
                raw = copy.deepcopy(saved)
                del raw[theme]["success"]
                build_tokens.RAW = raw
                with self.assertRaises(KeyError, msg=theme):
                    build_tokens.build()
        finally:
            build_tokens.RAW = saved

    def test_durations_are_durations(self):
        for set_name in ("core", "light", "dark"):
            for path, token in leaves(DATA[set_name]):
                if token["$type"] == "dimension" and not str(token["$value"]).startswith("{"):
                    self.assertRegex(token["$value"], r"^-?\d+(\.\d+)?(px|rem)$", path)
        self.assertEqual(DATA["core"]["motion"]["duration"]["fast"]["$type"], "duration")


if __name__ == "__main__":
    unittest.main()
