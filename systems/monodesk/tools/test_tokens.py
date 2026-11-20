#!/usr/bin/env python3
"""Checks that MonoDesk tokens.json still matches the 2026-11-19 readings."""
import json
import pathlib
import re
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
        # Every alias in every set, string or composite, resolves against core and its own set.
        import token_checks
        self.assertEqual(token_checks.alias_errors(T["core"], T["light"], T["dark"]), [])

    def test_committed_tokens_match_build(self):
        import build_tokens  # main() builds in memory; only write() touches tokens.json
        self.assertEqual(T, json.loads(json.dumps(build_tokens.main())))

    def test_app_heading_says_it_was_typed_in(self):
        for path in ("font.size.appHeading", "typography.appHeading"):
            self.assertTrue(flat(T["core"])[path]["$extensions"]["source"].startswith("Reconstruction"), path)

    def test_unread_values_are_not_labelled_as_readings(self):
        # raw/css-vars.json holds no custom property, so a token sourced only to one says Reconstruction.
        for path, token in flat(T).items():
            src = token["$extensions"]["source"]
            backed = re.search(r"computed (?!--|custom property)", src)
            if src.startswith(("declared --", "computed --", "computed custom property --")) and not backed:
                self.fail(f"{path}: {src[:60]}")


if __name__ == "__main__":
    unittest.main()
