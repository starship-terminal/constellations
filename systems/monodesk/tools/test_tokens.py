#!/usr/bin/env python3
"""Checks that MonoDesk tokens.json still matches the 2026-11-19 readings."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    out = {}
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            out[path] = v
        elif isinstance(v, dict):
            out.update(flat(v, path))
    return out


class TokensTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = [p for p, t in flat(T).items() if "source" not in t.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_brand_colours(self):
        light = flat(T["light"])
        self.assertEqual(light["brand.blue"]["$value"], "#1c64f5")
        self.assertEqual(light["brand.highlighter"]["$value"], "#d1ff6e")
        self.assertEqual(light["brand.funGreen"]["$value"], "#026232")
        self.assertEqual(light["background.page"]["$value"], "#1c64f5")
        self.assertEqual(light["text.primary"]["$value"], "#161616")

    def test_primary_pill(self):
        core = flat(T["core"])
        self.assertEqual(core["component.button.primary.background"]["$value"], "#d1ff6e")
        self.assertEqual(core["component.button.primary.text"]["$value"], "#026232")
        self.assertEqual(core["component.button.primary.radius"]["$value"], "100px")

    def test_login_card(self):
        core = flat(T["core"])
        self.assertEqual(core["component.card.login.radius"]["$value"], "16px")
        self.assertEqual(core["component.button.login.background"]["$value"], "#161616")
        self.assertEqual(core["component.field.radius"]["$value"], "9px")

    def test_no_dead_aliases(self):
        names = set(flat(T["core"]))
        for path, token in flat(T["core"]).items():
            value = token["$value"]
            if not isinstance(value, dict):
                continue
            for key, item in value.items():
                if isinstance(item, str) and item.startswith("{") and item.endswith("}"):
                    ref = item[1:-1]
                    self.assertIn(ref, names, f"{path}.{key} -> {ref}")


if __name__ == "__main__":
    unittest.main()
