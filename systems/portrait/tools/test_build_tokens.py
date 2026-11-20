#!/usr/bin/env python3
"""The portrait builder reproduces tokens.json in memory, every alias resolves, and the page
colour is the measured gray-10. Nothing here writes tokens.json."""

import json
import unittest
from pathlib import Path

import build_tokens

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
    elif isinstance(node, dict):
        for key, child in node.items():
            if not key.startswith("$"):
                yield from leaves(child, f"{path}.{key}" if path else key)


def lookup(root, ref):
    node = root
    for part in ref.strip("{}").split("."):
        node = node.get(part) if isinstance(node, dict) else None
    return node if isinstance(node, dict) and "$value" in node else None


def refs(value):
    if isinstance(value, str) and value.startswith("{"):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from refs(v)


class Tokens(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(TOKENS, build_tokens.build())

    def test_page_colour_is_the_measured_gray(self):
        self.assertEqual(TOKENS["core"]["color"]["gray"]["10"]["$value"], "#f7f7f7")
        self.assertEqual(TOKENS["light"]["color"]["bg"]["page"]["$value"], "{color.gray.10}")

    def test_every_alias_resolves_set_first(self):
        # The catalog resolves an alias in the token's own set first, then in core, and follows the
        # chain to a final value: a dangling alias, a self alias or a loop (a -> b -> a) all fail.
        def final(set_name, ref, trail):
            if ref in trail:
                self.fail(f"alias loop: {' -> '.join(trail + [ref])}")
            hit = lookup(TOKENS[set_name], ref) or lookup(TOKENS["core"], ref)
            self.assertIsNotNone(hit, f"{' -> '.join(trail + [ref])} resolves to nothing")
            for nxt in refs(hit["$value"]):
                final(set_name, nxt, trail + [ref])

        for set_name in ("core", "light", "dark"):
            for path, token in leaves(TOKENS[set_name]):
                for ref in refs(token["$value"]):
                    final(set_name, ref, ["{" + path + "}"])

    def test_every_token_has_a_type_a_source_and_an_evidence_label(self):
        for set_name in ("core", "light", "dark"):
            for path, token in leaves(TOKENS[set_name]):
                self.assertIn("$type", token, f"{set_name}.{path}")
                ext = token.get("$extensions", {})
                self.assertTrue(ext.get("source"), f"{set_name}.{path}")
                self.assertIn(ext.get("evidence"), ("Measured", "Reconstruction"), f"{set_name}.{path}")

    def test_no_browser_default_focus_ring(self):
        # #e59700 is Chromium's default ring colour and outline-style was none: not a product value.
        for set_name in ("core", "light", "dark"):
            for path, token in leaves(TOKENS[set_name]):
                self.assertNotEqual(token["$value"], "#e59700", f"{set_name}.{path}")


if __name__ == "__main__":
    unittest.main()
