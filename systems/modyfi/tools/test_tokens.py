"""Package contract: the builders reproduce the committed files, and every token says where it came from."""
import json
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "tools"))

import build_from_readings  # noqa: E402  (writes only when run as a script)
import build_tokens  # noqa: E402

TOKENS = json.loads((HERE / "tokens.json").read_text())


def leaves(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from leaves(v, prefix + k + ".")


class Contract(unittest.TestCase):
    def test_measured_colours(self):
        core = TOKENS["core"]["color"]
        self.assertEqual(core["accent"]["$value"].lower(), "#ff0357")
        self.assertEqual(core["paragraph"]["$value"].lower(), "#c9c9c9")
        self.assertIn(core["background"]["$value"].lower(), ("#000000", "#000"))
        self.assertIn(core["heading"]["$value"].lower(), ("#ffffff", "#fff"))
        self.assertIn("dark", TOKENS["$themes"][0]["selectedTokenSets"])
        self.assertEqual(TOKENS["dark"]["color"]["accent"]["$value"], "{core.color.accent}")

    def test_every_token_has_a_source(self):
        for setname in ("core", "dark"):
            for name, tok in leaves(TOKENS[setname]):
                ext = tok.get("$extensions") or {}
                self.assertTrue(ext.get("source"), f"{setname}.{name} has no source")

    def test_tokens_match_builder(self):
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.TEXT)

    def test_readings_match_builder(self):
        self.assertEqual((HERE / "raw" / "components-computed.json").read_text(), build_from_readings.COMPONENTS_TEXT)
        self.assertEqual((HERE / "raw" / "css-vars.json").read_text(), build_from_readings.VARS_TEXT)

    def test_crop_repair_only_for_the_old_capture(self):
        row = {"sel": "a.x", "backgroundColor": "rgb(1, 1, 1)", "color": "rgb(2, 2, 2)"}
        crops = {"signup-button-default": {"backgroundColor": "rgb(9, 9, 9)", "text": "Sign up"}}
        old = build_from_readings.default_row("signup-button", row, {"innerWidth": 1440}, crops)
        self.assertEqual(old["backgroundColor"], "rgb(9, 9, 9)")
        self.assertIn("crops-measured.json", old["source"])
        self.assertNotIn("text", old)
        fresh = build_from_readings.default_row("signup-button", row, {"innerWidth": 1440, "readAtRest": True}, crops)
        self.assertEqual(fresh["backgroundColor"], "rgb(1, 1, 1)")
        self.assertNotIn("crops-measured.json", fresh["source"])

    def test_signup_default_is_at_rest(self):
        # The homepage pass read the signup control under the pointer; the crop pass read it at rest.
        states = json.loads(build_from_readings.COMPONENTS_TEXT)["components"]["signup-button"]["states"]
        self.assertEqual(states["default"]["backgroundColor"], "rgba(0, 0, 0, 0)")
        self.assertEqual(states["hover"]["backgroundColor"], "rgb(255, 3, 87)")

    def test_focus_label_follows_the_reading(self):
        # A saved focus reading (after a recapture) is Measured; without one the hand row is not.
        saved = {"focus-visible": {"outline": "rgb(0, 0, 0) solid 2px", "component": "cta-button", "sel": "a.rl-button"}}
        self.assertEqual(build_from_readings.cta_focus(saved)["evidence"], "Measured")
        self.assertEqual(build_from_readings.cta_focus({})["evidence"], "Reconstruction")


if __name__ == "__main__":
    unittest.main()
