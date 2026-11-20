#!/usr/bin/env python3
"""The Pocket builder reproduces tokens.json from raw/css-vars.json, in memory, with DTCG types.

Nothing here writes tokens.json: build() returns the document and the test compares it.
"""
import json
import re
import unittest
from pathlib import Path

import build_tokens

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
    elif isinstance(node, dict):
        for key, child in node.items():
            if not key.startswith("$"):
                yield from leaves(child, f"{path}.{key}" if path else key)


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(TOKENS, build_tokens.build())

    def test_types_hold_one_kind_of_value(self):
        for set_name in ("core", "light", "dark"):
            for path, token in leaves(TOKENS[set_name]):
                value, kind = token["$value"], token["$type"]
                self.assertTrue(token["$extensions"].get("source"), path)
                if kind == "dimension":
                    self.assertRegex(value, r"^-?(\d+|\d*\.\d+)(px|rem)$", path)
                elif kind == "duration":
                    self.assertRegex(value, r"^\d+(\.\d+)?ms$", path)
                elif kind == "cubicBezier":
                    self.assertEqual(len(value), 4, path)
                    self.assertTrue(all(isinstance(n, (int, float)) for n in value), path)

    def test_durations_and_easing_are_the_declared_values(self):
        g = json.loads((ROOT / "raw" / "css-vars.json").read_text())["global"]
        motion = TOKENS["core"]["motion"]
        self.assertEqual(g["--uiControlsDurationEnterMS"], ".1s")
        self.assertEqual(motion["duration"]["ui-enter"]["$value"], "100ms")
        self.assertEqual(g["--easingStandard"], "cubic-bezier(.4,0,.2,1)")
        self.assertEqual(motion["easing"]["standard"]["$value"], [0.4, 0, 0.2, 1])
        names = {e["name"] for e in TOKENS["core"]["$extensions"]["notTokenised"]}
        self.assertEqual(names, {"--fontSizeRoot", "--fontSizeRootMedium", "--fontSizeRootSmall"})


if __name__ == "__main__":
    unittest.main()
