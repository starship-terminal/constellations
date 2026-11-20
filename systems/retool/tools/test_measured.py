"""Checks the Retool readings that tokens.json is built from.

Run from this folder: python3 -m unittest test_measured.py
"""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
MEASURED = ROOT / "raw" / "measured.json"
TOKENS = ROOT / "tokens.json"


class MeasuredTest(unittest.TestCase):
    def setUp(self):
        self.measured = json.loads(MEASURED.read_text())
        self.tokens = json.loads(TOKENS.read_text())

    def test_pages_were_the_signed_out_surfaces(self):
        pages = self.measured["pages"]
        self.assertEqual(pages["home"]["url"], "https://retool.com/")
        self.assertEqual(pages["pricing"]["url"], "https://retool.com/pricing")
        self.assertEqual(pages["login"]["url"], "https://login.retool.com/auth/login")
        self.assertEqual(pages["signup"]["url"], "https://login.retool.com/auth/signup")
        self.assertEqual(pages["docs"]["url"], "https://docs.retool.com/")
        self.assertFalse(pages["home"]["challenge"])
        self.assertFalse(pages["login"]["challenge"])
        self.assertFalse(pages["signup"]["challenge"])
        self.assertFalse(pages["docs"]["challenge"])

    def test_marketing_button_matches_the_token(self):
        button = self.measured["pages"]["home"]["primaryCta"]
        self.assertEqual(button["backgroundColor"], "rgb(233, 235, 223)")
        self.assertEqual(button["color"], "rgb(21, 21, 21)")
        self.assertEqual(button["height"], "40px")
        token = self.tokens["dark"]["button"]["$value"]
        self.assertEqual(token, "#e9ebdf")
        self.assertIn("rgb(233, 235, 223)", self.tokens["dark"]["button"]["$extensions"]["source"])

    def test_login_field_matches_the_token(self):
        email = self.measured["pages"]["login"]["email"]
        self.assertEqual(email["backgroundColor"], "rgb(247, 248, 244)")
        self.assertIn("solid 2px", email["focus"]["outline"])
        token = self.tokens["core"]["color"]["login"]["field"]
        self.assertEqual(token["$value"], "#f7f8f4")
        self.assertIn("left empty", token["$extensions"]["source"])

    def test_signup_was_not_submitted(self):
        signup = self.measured["pages"]["signup"]
        self.assertFalse(signup["askedForCardPhoneOrId"])
        self.assertFalse(signup["askedForCompanySso"])
        self.assertIn("not email-only", signup["notEntered"])
        self.assertIn("not submitted", signup["notEntered"])

    def test_screenshot_gap_is_recorded(self):
        self.assertIn("not producing screenshot frames", self.measured["screenshotFrames"])

    def test_light_marketing_is_labelled_as_a_class_probe(self):
        probe = self.measured["lightClassProbe"]
        self.assertIn("not a published light marketing theme", probe["note"])
        self.assertEqual(self.tokens["light"]["page"]["$value"], "#e9ebdf")
        self.assertIn("class was set to light", self.tokens["light"]["page"]["$extensions"]["source"])



class BuildTest(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        import sys
        sys.path.insert(0, str(ROOT / "tools"))
        import build_tokens  # build() returns the tree; only write() touches tokens.json
        self.assertEqual(json.loads(TOKENS.read_text()), json.loads(json.dumps(build_tokens.build())))

    def test_unread_values_say_reconstruction(self):
        import sys
        sys.path.insert(0, str(ROOT / "tools"))
        import build_tokens
        for path, tok in build_tokens.leaves(json.loads(TOKENS.read_text())):
            value = tok["$value"]
            if not isinstance(value, (str, int, float)) or (isinstance(value, str) and value.startswith("{")):
                continue  # aliases and composites carry the evidence of what they name
            labelled = tok["$extensions"]["source"].startswith("Reconstruction")
            self.assertEqual(labelled, not build_tokens.in_raw(value), path)


class MatcherTest(unittest.TestCase):
    """The colour matcher on its own, against fixed inputs (not the package's labels)."""

    def setUp(self):
        import sys
        sys.path.insert(0, str(ROOT / "tools"))
        import build_tokens
        self.b = build_tokens
        self.saved = list(build_tokens.RAW_COLOURS)

    def tearDown(self):
        self.b.RAW_COLOURS[:] = self.saved

    def test_opacity_must_match(self):
        self.b.RAW_COLOURS[:] = [(0, 0, 0, 0.0), (0, 0, 0, 0.04), (35, 79, 166, 0.5)]
        self.assertFalse(self.b.colour_in_raw("#000000"))
        self.assertTrue(self.b.colour_in_raw("#0000000a"))
        self.assertTrue(self.b.colour_in_raw("#234fa680"))
        self.assertFalse(self.b.colour_in_raw("#234fa6"))

    def test_parses_comma_space_and_slash_forms(self):
        found = self.b._colours("rgb(1, 2, 3) rgba(4,5,6,0.2) rgb(7 8 9/0.5) #0a0b0c #0d0e0f80")
        self.assertEqual(found, [(1, 2, 3, 1.0), (4, 5, 6, 0.2), (7, 8, 9, 0.5), (10, 11, 12, 1.0), (13, 14, 15, 128 / 255)])

if __name__ == "__main__":
    unittest.main()
