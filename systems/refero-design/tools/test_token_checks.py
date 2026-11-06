"""token_checks: each set's aliases resolve in core or that set; light/dark gaps are listed."""
import unittest

from token_checks import alias_errors, parity_gap


def t(v):
    return {"$value": v, "$type": "color"}


CORE = {"gray": {"0": t("#fff"), "900": t("#000")}}


class AliasErrors(unittest.TestCase):
    def test_core_and_same_set_aliases_pass(self):
        light = {"text": {"primary": t("{gray.900}"), "link": t("{text.primary}")}}
        dark = {"text": {"primary": t("{gray.0}"), "link": t("{text.primary}")}}
        self.assertEqual(alias_errors(CORE, light, dark), [])

    def test_light_alias_held_only_by_dark_fails(self):
        light = {"text": {"primary": t("{background.popover}")}}
        dark = {"text": {"primary": t("{gray.0}")}, "background": {"popover": t("{gray.900}")}}
        self.assertEqual(alias_errors(CORE, light, dark), ["light.text.primary: alias {background.popover} points at nothing in core or light"])

    def test_core_cannot_alias_a_theme(self):
        core = {"gray": {"0": t("{text.primary}")}}
        light = {"text": {"primary": t("#000")}}
        self.assertEqual(len(alias_errors(core, light, {})), 1)

    def test_aliases_inside_composite_values(self):
        light = {"shadow": {"card": {"$value": [{"color": "{gray.missing}"}], "$type": "shadow"}}}
        self.assertEqual(len(alias_errors(CORE, light, {})), 1)


class ParityGap(unittest.TestCase):
    def test_lists_each_side(self):
        light = {"a": t("#000"), "b": t("#000")}
        dark = {"a": t("#fff"), "c": t("#fff")}
        self.assertEqual(parity_gap(light, dark), (["b"], ["c"]))


if __name__ == "__main__":
    unittest.main()
