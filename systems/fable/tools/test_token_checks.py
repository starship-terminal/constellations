"""token_checks: each set's aliases resolve in core or that set; light/dark gaps are listed.

The fixture tests hold for any product's mapping; test_committed_tokens_pass runs the same
check on the package's own tokens.json."""
import json
import pathlib
import unittest

from token_checks import alias_errors, parity_gap

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


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

    @unittest.skipUnless(TOKENS.exists(), "no tokens.json yet")
    def test_committed_tokens_pass(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(alias_errors(doc["core"], doc["light"], doc["dark"]), [])


class ParityGap(unittest.TestCase):
    def test_lists_each_side(self):
        light = {"a": t("#000"), "b": t("#000")}
        dark = {"a": t("#fff"), "c": t("#fff")}
        self.assertEqual(parity_gap(light, dark), (["b"], ["c"]))

    @unittest.skipUnless(TOKENS.exists(), "no tokens.json yet")
    def test_committed_gap_is_disclosed(self):
        # Fable's light set carries the measured marketing/catalog roles
        # (text.emotionInk, action.*, background.band, ...) the scoped .dark
        # declarations never redeclare; the dark set adds discover/footer ink.
        # The gap is expected and disclosed, not an error — this pins it.
        doc = json.loads(TOKENS.read_text())
        lt, dk = parity_gap(doc["light"], doc["dark"])
        # The complete disclosed gap — dropping another dark role or adding
        # one more unmatched light role must fail here.
        self.assertEqual(lt, [
            "action.ctaFill", "action.ctaInk", "action.emotionCtaFill", "action.emotionCtaInk",
            "background.appBanner", "background.band", "background.page", "background.surface",
            "background.surfaceHover", "border.emotionFocusRing", "border.focusRing",
            "border.hairline", "text.emotionInk", "text.footerMuted", "text.ink",
            "text.muted", "text.onDark"])
        self.assertEqual(dk, ["text.discoverInk", "text.footerInk"])


if __name__ == "__main__":
    unittest.main()
