"""Tests for build_tokens + token_checks. Run: python3 -m unittest discover -s tools (from this package).

gofundme.com ships one theme — the consumer light — so the committed tokens.json carries `core` and `light` only;
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
        self.assertEqual(self.t["$metadata"]["tokenSetOrder"], ["core", "light"])
        self.assertEqual([th["id"] for th in self.t["$themes"]], ["light"])
        self.assertNotIn("dark", self.t)

    def test_no_alias_errors(self):
        core, light = self.t["core"], self.t["light"]
        errs = token_checks.alias_errors(core, light, {})
        self.assertEqual(errs, [])

    def test_every_leaf_has_source(self):
        missing = [
            f"{s}.{n}"
            for s in ("core", "light")
            for n, tok in token_checks.tokens_of(self.t[s])
            if not tok.get("$extensions", {}).get("source")
        ]
        self.assertEqual(missing, [])



@unittest.skipUnless(TOKENS.exists(), "no tokens.json yet (kit copy)")
class MeasuredRoleAliasTest(unittest.TestCase):
    """A measured role aliases only a declared var of its own kind (an ink never a surface)."""

    def test_roles_alias_their_kind(self):
        m = json.loads(TOKENS.read_text())["light"]["measured"]["color"]
        kinds = {"text": ("text",), "border": ("border",), "surface": ("surface",)}
        for group, fams in kinds.items():
            for key, tok in m.get(group, {}).items():
                v = tok["$value"] if isinstance(tok, dict) and "$value" in tok else None
                if isinstance(v, str) and v.startswith("{"):
                    self.assertTrue(v[1:].split(".")[1] in fams, f"{group}.{key} -> {v}")
        for key in ("ink", "footerInk"):
            self.assertEqual(m["text"][key]["$value"], "{color.text.default}")

if __name__ == "__main__":
    unittest.main()
