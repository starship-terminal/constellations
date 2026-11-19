#!/usr/bin/env python3
"""The Vivid Money token file resolves, and every token records a source."""
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
    def test_theme(self):
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light"])

    def test_roles_resolve(self):
        self.assertEqual(lookup("light.page"), "#ffffff")
        self.assertEqual(lookup("light.text"), "#333333")
        self.assertEqual(lookup("light.accent"), "#7d33f6")
        self.assertEqual(lookup("light.surface"), "#f5f5f4")
        self.assertEqual(lookup("light.border"), "#eceef2")
        self.assertEqual(lookup("light.muted"), "#79797f")

    def test_every_token_has_a_source(self):
        missing = [path for path, node in FLAT.items() if not node.get("$extensions", {}).get("source")]
        self.assertEqual(missing, [])

    def test_no_invented_dark_set(self):
        self.assertNotIn("dark", TOKENS)


if __name__ == "__main__":
    unittest.main()
