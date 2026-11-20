"""Checks for the committed MyMind tokens. Run from this package's tools/."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def tree():
    return json.loads(TOKENS.read_text())


def light_value(data, path):
    sets = {}
    for group in ("core", "light"):
        found = []
        build_tokens.walk(data[group], "", found)
        sets[group] = dict(found)
    return build_tokens.resolve(sets["light"][path]["$value"], sets, ("light", "core"))


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        self.assertGreater(build_tokens.check(tree()), 40)

    def test_accent_is_the_measured_orange(self):
        data = tree()
        self.assertEqual(data["core"]["color"]["orange"]["$value"], "#ff5924")
        self.assertEqual(data["light"]["color"]["page"]["$value"], "{color.canvas}")

    def test_light_roles_resolve_set_first_to_the_measured_colours(self):
        data = tree()
        self.assertEqual(light_value(data, "color.link"), "#1573dd")
        self.assertEqual(light_value(data, "component.link-nav.text"), "#1573dd")
        # chip-text once resolved to light.color.chip, the chip background.
        self.assertEqual(light_value(data, "color.chip-text"), "#748297")
        self.assertEqual(light_value(data, "color.chip"), "#f5f7f9")

    def test_a_chain_into_core_stays_in_core(self):
        # core.color.canvas -> {color.muted} must resolve to core's muted, not light's.
        data = tree()
        data["core"]["color"]["canvas"]["$value"] = "{color.muted}"
        self.assertEqual(light_value(data, "color.page"), data["core"]["color"]["muted"]["$value"])

    def test_self_alias_fails(self):
        data = tree()
        data["light"]["color"]["link"]["$value"] = "{color.link}"
        with self.assertRaisesRegex(ValueError, "cycle"):
            build_tokens.check(data)

    def test_dangling_alias_fails(self):
        data = tree()
        data["light"]["color"]["page"]["$value"] = "{color.nothing}"
        with self.assertRaisesRegex(ValueError, "points at nothing"):
            build_tokens.check(data)

    def test_core_cannot_see_light(self):
        data = tree()
        data["core"]["color"]["canvas"]["$value"] = "{color.page}"
        with self.assertRaisesRegex(ValueError, "points at nothing in core"):
            build_tokens.check(data)

    def test_measured_colour_needs_a_reading(self):
        data = tree()
        data["core"]["color"]["orange"]["$value"] = "#ff5925"
        with self.assertRaisesRegex(ValueError, "in no reading"):
            build_tokens.check(data)

    def test_missing_source_fails(self):
        data = tree()
        del data["core"]["color"]["orange"]["$extensions"]
        with self.assertRaisesRegex(ValueError, "missing evidence"):
            build_tokens.check(data)


if __name__ == "__main__":
    unittest.main()
