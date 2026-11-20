#!/usr/bin/env python3
"""The package's own check: every token names a source, four headline colours are pinned to the
values read live, and raw/component-tokens.json and tokens.json hold the same number of leaves.
It does not re-read raw/: the pinned colours are literals."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
SPEC = json.loads((HERE / "raw" / "component-tokens.json").read_text())


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            yield from leaves(v, f"{path}.{k}" if path else k)


class Tokens(unittest.TestCase):
    def test_every_token_has_a_measured_source(self):
        for path, token in leaves(TOKENS):
            src = token.get("$extensions", {}).get("source", "")
            self.assertTrue(src.startswith("computed") or src.startswith("declared") or src.startswith("derived"), path)
            self.assertNotIn("invent", src.lower(), path)

    def test_page_grounds_match_the_live_read(self):
        self.assertEqual(TOKENS["dark"]["color"]["bg"]["page"]["$value"], "#000000")
        self.assertEqual(TOKENS["light"]["color"]["bg"]["page"]["$value"], "#f9f8f6")
        self.assertEqual(TOKENS["light"]["color"]["action"]["fill"]["$value"], "#fb7232")
        self.assertEqual(TOKENS["light"]["color"]["action"]["app"]["$value"], "#ff6821")

    def test_spec_and_tokens_have_the_same_leaf_count(self):
        def count(node):
            if isinstance(node, dict) and "type" in node and "value" in node:
                return 1
            if isinstance(node, dict):
                return sum(count(v) for k, v in node.items() if not k.startswith("_"))
            return 0
        spec_n = count(SPEC["core"]) + count(SPEC["dark"]) + count(SPEC["light"]) + count(SPEC["component"])
        token_n = sum(1 for _ in leaves(TOKENS["core"])) + sum(1 for _ in leaves(TOKENS["dark"])) + sum(1 for _ in leaves(TOKENS["light"]))
        self.assertEqual(spec_n, token_n)


if __name__ == "__main__":
    unittest.main()
