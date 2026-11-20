#!/usr/bin/env python3
"""The Stripe token file resolves, and every token records a source."""
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
    def test_themes(self):
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light"])

    def test_roles_resolve(self):
        self.assertEqual(lookup("light.page"), "#ffffff")
        self.assertEqual(lookup("light.text"), "#061b31")
        self.assertEqual(lookup("light.accent"), "#533afd")
        self.assertEqual(lookup("light.muted"), "#50617a")
        self.assertEqual(lookup("light.border"), "#e5edf5")
        self.assertEqual(lookup("light.pricingAccent"), "#635bff")
        self.assertEqual(lookup("light.dashboardAccent"), "#675dff")

    def test_every_token_has_a_source(self):
        missing = [path for path, node in FLAT.items() if not node.get("$extensions", {}).get("source")]
        self.assertEqual(missing, [])

    def test_button_radius(self):
        self.assertEqual(lookup("light.component.button.radius"), "4px")
        self.assertEqual(lookup("core.radius.sm"), "4px")
