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

    def test_action_and_form_roles_alias_their_kind(self):
        """Inks alias a button's text.* or text.*, fills a button's surface.* or surface.*, borders
        an input's border.* or border.*; a role with no var of its kind stays a literal."""
        m = json.loads(TOKENS.read_text())["light"]["measured"]["color"]
        ink_keys = {"ctaInk", "heroCtaInk", "donateInk", "shareInk", "wpButtonInk", "fieldInk", "pillInk", "placeholder"}
        fill_keys = {"ctaFill", "heroCtaFill", "donateFill", "continueFill", "wpButtonFill", "fieldBg", "countryFieldBg", "ctaHover"}
        border_keys = {"fieldBorder", "pillBorder"}
        for group in ("action", "form"):
            for key, tok in m.get(group, {}).items():
                if key.startswith("$"):
                    continue
                v = tok["$value"]
                if not (isinstance(v, str) and v.startswith("{")):
                    self.assertRegex(v, r"^(#[0-9a-f]{6}|rgba\()", f"{group}.{key}")  # the literal fallback
                    continue
                parts = v[1:-1].split(".")[1:]
                if key in ink_keys:
                    self.assertTrue(parts[0] == "text" or (parts[0] in ("button", "input") and "text" in parts), f"{key} -> {v}")
                elif key in fill_keys:
                    self.assertTrue(parts[0] == "surface" or (parts[0] in ("button", "input") and "surface" in parts), f"{key} -> {v}")
                elif key in border_keys:
                    self.assertTrue(parts[0] == "border" or (parts[0] == "input" and "border" in parts), f"{key} -> {v}")
                else:
                    self.fail(f"{group}.{key} is not classed as ink, fill or border")
        # no declared var paints the transparent fills, so they stay literals
        self.assertEqual(m["action"]["ctaFill"]["$value"], "rgba(255, 255, 255, 0)")
        self.assertEqual(m["form"]["fieldBg"]["$value"], "rgba(0, 0, 0, 0)")

if __name__ == "__main__":
    unittest.main()
