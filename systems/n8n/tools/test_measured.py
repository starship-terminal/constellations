"""Checks the n8n readings that tokens.json is built from.

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
        self.assertEqual(pages["home"]["url"], "https://n8n.io/")
        self.assertEqual(pages["pricing"]["url"], "https://n8n.io/pricing/")
        self.assertEqual(pages["login"]["url"], "https://app.n8n.cloud/login")
        self.assertEqual(pages["register"]["url"], "https://app.n8n.cloud/register")
        self.assertFalse(pages["home"]["challenge"])
        self.assertFalse(pages["login"]["challenge"])
        self.assertFalse(pages["register"]["challenge"])

    def test_marketing_button_matches_the_token(self):
        button = self.measured["pages"]["home"]["primaryCta"]
        self.assertEqual(button["backgroundColor"], "rgb(255, 188, 202)")
        self.assertEqual(button["height"], "42px")
        self.assertEqual(button["borderRadius"], "9999px")
        token = self.tokens["core"]["color"]["marketing"]["button-primary"]["$value"]
        self.assertEqual(token, "#ffbcca")

    def test_console_page_matches_the_token(self):
        body = self.measured["pages"]["login"]["body"]
        self.assertEqual(body["backgroundColor"], "oklch(0.2046 0 89.88)")
        token = self.tokens["core"]["color"]["console"]["page"]
        self.assertEqual(token["$value"], "#171717")
        self.assertIn(body["backgroundColor"], token["$extensions"]["source"])

    def test_register_error_was_not_a_submitted_account(self):
        error = self.measured["pages"]["register"]["error"]
        self.assertEqual(error["text"], "Value needs to be an email address")
        self.assertIn("not submitted", error["trigger"])
        self.assertIn("real email was not submitted", self.measured["pages"]["register"]["notEntered"])

    def test_screenshot_gap_is_recorded(self):
        self.assertIn("not producing screenshot frames", self.measured["screenshotFrames"])


if __name__ == "__main__":
    unittest.main()
