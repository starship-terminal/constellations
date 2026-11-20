#!/usr/bin/env python3
"""The Mercury token file matches a fresh build, resolves, and every token records a source."""
import json
import pathlib
import re
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def flatten(tokens):
    flat = {}

    def walk(node, path):
        if not isinstance(node, dict):
            return
        if "$value" in node:
            flat[".".join(path)] = node
            return
        for key, child in node.items():
            if not key.startswith("$"):
                walk(child, path + [key])

    walk(tokens, [])
    return flat


FLAT = flatten(TOKENS)


def lookup(path, depth=0):
    node = FLAT.get(path)
    if node is None or depth > 12:
        return None
    value = node["$value"]
    if not isinstance(value, str):
        return value
    match = re.fullmatch(r"\{([^}]+)\}", value.strip())
    if not match:
        return value
    ref = match.group(1)
    set_name = path.split(".")[0]
    for candidate in (f"{set_name}.{ref}", f"core.{ref}", ref):
        if candidate in FLAT:
            return lookup(candidate, depth + 1)
    return None


class TokensTest(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        # Builds in memory (the builder writes only when run as a script).
        import build_tokens
        self.assertEqual(TOKENS, json.loads(json.dumps(build_tokens.tokens)))

    def test_dtcg_value_shapes(self):
        for path, node in FLAT.items():
            if node["$type"] == "cubicBezier":
                self.assertIsInstance(node["$value"], list, path)
                self.assertEqual(len(node["$value"]), 4, path)
            if node["$type"] == "color" and isinstance(node["$value"], str) and node["$value"].startswith("#"):
                self.assertIn(len(node["$value"]), (7, 9), path)

    def test_themes(self):
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light", "dark"])

    def test_roles_resolve(self):
        self.assertEqual(lookup("light.page"), "#fbfcfd")
        self.assertEqual(lookup("dark.page"), "#171721")
        self.assertEqual(lookup("light.accent"), "#5266eb")
        self.assertEqual(lookup("light.text"), "#272735")
        self.assertEqual(lookup("dark.text"), "#ededf3")

    def test_every_alias_resolves(self):
        for path, node in FLAT.items():
            value = node["$value"]
            if isinstance(value, str) and "{" in value:
                self.assertIsNotNone(lookup(path), path)

    def test_every_token_has_a_source(self):
        for path, node in FLAT.items():
            self.assertIn("source", node.get("$extensions", {}), path)


if __name__ == "__main__":
    unittest.main()
