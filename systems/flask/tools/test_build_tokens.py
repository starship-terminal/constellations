"""Tests for build_tokens + token_checks. Run: python3 -m unittest discover -s tools (from this package).

flask.do ships one theme — dark — so the committed tokens.json carries `core` and `dark` only;
these checks run the same alias and normalisation passes the builder runs, on the real file."""
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
        self.assertEqual(self.t["$metadata"]["tokenSetOrder"], ["core", "dark"])
        self.assertEqual([th["id"] for th in self.t["$themes"]], ["dark"])
        self.assertNotIn("light", self.t)

    def test_no_alias_errors(self):
        core, dark = self.t["core"], self.t["dark"]
        errs = token_checks.alias_errors(core, {}, dark)
        self.assertEqual(errs, [])

    def test_every_leaf_has_source(self):
        missing = [
            f"{s}.{n}"
            for s in ("core", "dark")
            for n, tok in token_checks.tokens_of(self.t[s])
            if not tok.get("$extensions", {}).get("source")
        ]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
