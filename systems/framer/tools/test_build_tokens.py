"""Tests for build_tokens + token_checks. Run: python3 -m unittest discover -s tools (from this package).

framer.com ships one theme — dark. The committed tokens.json carries `core`, `dark` and `auth`
(the separate light /login shell's readings); these checks run the same alias and normalisation
passes the builder runs, on the real file."""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import token_checks  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


@unittest.skipUnless(TOKENS.exists(), "no tokens.json yet (kit copy)")
class CommittedTokensTest(unittest.TestCase):
    def setUp(self):
        self.t = json.loads(TOKENS.read_text())

    def test_sets(self):
        self.assertEqual(self.t["$metadata"]["tokenSetOrder"], ["core", "dark", "auth"])
        self.assertEqual([th["id"] for th in self.t["$themes"]], ["dark", "auth"])
        self.assertNotIn("light", self.t)

    def test_login_readings_stay_out_of_dark(self):
        """Every /login reading is in `auth`, none in the dark marketing set."""
        for n, tok in token_checks.tokens_of(self.t["dark"]):
            self.assertNotIn("login-", tok["$extensions"]["source"], f"dark.{n}")
        auth = {n: tok for n, tok in token_checks.tokens_of(self.t["auth"])}
        self.assertEqual(auth["color.surface.loginPanel"]["$value"], "#ffffff")
        for n, tok in auth.items():
            self.assertIn("login-", tok["$extensions"]["source"], f"auth.{n}")

    def test_no_alias_errors(self):
        core, dark = self.t["core"], self.t["dark"]
        errs = token_checks.alias_errors(core, {}, dark) + token_checks.alias_errors(core, {}, self.t["auth"])
        self.assertEqual(errs, [])

    def test_every_leaf_has_source(self):
        missing = [
            f"{s}.{n}"
            for s in ("core", "dark", "auth")
            for n, tok in token_checks.tokens_of(self.t[s])
            if not tok.get("$extensions", {}).get("source")
        ]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
