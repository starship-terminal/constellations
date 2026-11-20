"""The Miro token file matches the pricing-page readings."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((ROOT / "tokens.json").read_text())
        self.raw = json.loads((ROOT / "raw" / "pricing-root-vars.json").read_text())

    def test_light_roles_match_measured_colours(self):
        light = self.tokens["light"]
        self.assertEqual(light["page"]["$value"], "#fafafc")
        self.assertEqual(light["surface"]["$value"], "#ffffff")
        self.assertEqual(light["text"]["$value"], "#1c1c1e")
        self.assertEqual(light["textMuted"]["$value"], "#555a6a")
        self.assertEqual(light["accent"]["$value"], "#3859ff")
        self.assertEqual(light["border"]["$value"], "#c7cad5")

    def test_accent_comes_from_the_pricing_button_token(self):
        self.assertEqual(self.raw["variables"]["--button-primary-bg-btn-primary-idle"], "#3859ff")
        self.assertIn("--button-primary-bg-btn-primary-idle", self.tokens["light"]["accent"]["$extensions"]["source"])

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if not key.startswith("$"):
                        walk(value, path + "." + key)

        walk(self.tokens, "")
        self.assertEqual(missing, [])

    def test_no_dark_set(self):
        self.assertNotIn("dark", self.tokens)



class Build(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        import build_tokens  # builds on import; writes only when run as a script
        self.assertEqual(json.loads((ROOT / "tokens.json").read_text()), json.loads(json.dumps(build_tokens.doc)))

    def test_excluded_custom_properties_are_not_labelled_measured(self):
        # raw/pricing-root-vars.json excludes --tw-* and --wcds-*, so no reading backs a token sourced to one.
        def leaves(node):
            for k, v in node.items():
                if isinstance(v, dict) and "$value" in v:
                    yield v
                elif isinstance(v, dict) and not k.startswith("$"):
                    yield from leaves(v)
        for tok in leaves(json.loads((ROOT / "tokens.json").read_text())):
            src = tok["$extensions"]["source"]
            if "--tw-" in src or "--wcds-" in src:
                self.assertTrue(src.startswith("Reconstruction"), src[:80])

    def test_guide_matches_render(self):
        import build_style_guide
        self.assertEqual((ROOT / "style-guide.html").read_text(), build_style_guide.html)

if __name__ == "__main__":
    unittest.main()
