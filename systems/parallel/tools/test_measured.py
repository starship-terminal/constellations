"""Checks the Parallel readings that tokens.json is built from.

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

    def test_pages_are_useparallel(self):
        home = self.measured["pages"]["home-desktop"]
        login = self.measured["pages"]["login-desktop"]
        signup = self.measured["pages"]["signup-desktop"]
        self.assertEqual(home["url"], "https://www.useparallel.com/")
        self.assertEqual(login["url"], "https://www.useparallel.com/login")
        self.assertEqual(signup["url"], "https://www.useparallel.com/signup")
        self.assertFalse(home["challenge"])
        self.assertFalse(login["challenge"])
        self.assertFalse(signup["challenge"])
        self.assertIn("useparallel.com", self.measured["domain"])
        self.assertIn("parallel.ai was not opened", self.measured["note"])

    def test_page_fill_matches_the_token(self):
        self.assertEqual(self.measured["pages"]["home-desktop"]["bodyBg"], "rgb(251, 250, 249)")
        self.assertEqual(self.tokens["core"]["color"]["page"]["$value"], "#fbfaf9")

    def test_login_action_matches_the_token(self):
        sign_in = next(b for b in self.measured["pages"]["login-desktop"]["buttons"] if b["text"] == "Sign in")
        self.assertEqual(sign_in["backgroundColor"], "rgb(31, 31, 31)")
        self.assertEqual(sign_in["borderRadius"], "12px")
        self.assertEqual(self.tokens["core"]["color"]["action"]["$value"], "#1f1f1f")
        self.assertEqual(self.tokens["core"]["radius"]["control"]["$value"], "12px")

    def test_signup_was_not_an_email_form(self):
        signup = self.measured["pages"]["signup-desktop"]
        self.assertIn("Sign up with LinkedIn", signup["textHead"])
        self.assertEqual(signup["inputs"], [])
        self.assertTrue(any("AgentMail was not used" in line for line in self.measured["notEntered"]))

    def test_yellow_token_is_the_declared_property(self):
        self.assertEqual(self.tokens["core"]["color"]["yellow"]["$value"], "#eafa35")
        declared = self.measured["home-measure"]["productVars"]["--color-yellow"]
        self.assertEqual(declared, "#eafa35")


if __name__ == "__main__":
    unittest.main()
