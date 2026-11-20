"""The committed tokens.json passes the builder's own check.

Run from the package tools folder, which is how tools/package_tests.py invokes it.
"""
import importlib.util
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
TOKENS = HERE.parent / "tokens.json"


def load_builder():
    spec = importlib.util.spec_from_file_location("the_org_build_tokens", HERE / "build_tokens.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TokensTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        module = load_builder()
        tokens = json.loads(TOKENS.read_text())
        module.check(tokens)

    def test_committed_file_matches_builder(self):
        # Built in memory; the committed file is never rewritten by the test.
        self.assertEqual(json.loads(TOKENS.read_text()), load_builder().build())

    def test_only_declared_values_are_measured(self):
        tokens = json.loads(TOKENS.read_text())
        self.assertEqual(tokens["core"]["color"]["named"]["ink"]["$extensions"]["source"]["evidence"], "Reconstruction")
        self.assertEqual(tokens["core"]["color"]["named"]["brand"]["$extensions"]["source"]["evidence"], "Measured")

    def test_declared_values_match_in_a_common_form(self):
        canon = load_builder().canon
        self.assertEqual(canon([0.19, 1, 0.22, 1]), canon("cubic-bezier(.19, 1, .22, 1)"))
        self.assertEqual(canon("Inter, sans-serif"), canon('"Inter", sans-serif'))
        self.assertNotEqual(canon([0.19, 1, 0.22, 1]), canon("cubic-bezier(.2, 1, .22, 1)"))
        tokens = json.loads(TOKENS.read_text())
        for path in (("fontFamily", "primary"), ("fontFamily", "secondary"),
                     ("easing", "transition-01"), ("easing", "transition-timing")):
            with self.subTest(token=".".join(path)):
                self.assertEqual(tokens["core"][path[0]][path[1]]["$extensions"]["source"]["evidence"], "Measured")

    def test_alias_resolves_in_its_own_set_then_core(self):
        module = load_builder()
        tokens = json.loads(TOKENS.read_text())
        tokens["light"]["only-light"] = {"$type": "color", "$value": "#000000",
                                         "$extensions": {"source": {"evidence": "Measured"}}}
        tokens["light"]["color"]["text"]["$value"] = "{only-light}"
        module.check(tokens)  # resolves in light, where the old core-only check failed it
        tokens["light"]["color"]["text"]["$value"] = "{nowhere}"
        with self.assertRaises(SystemExit):
            module.check(tokens)

    def test_light_only(self):
        tokens = json.loads(TOKENS.read_text())
        self.assertIn("light", tokens)
        self.assertNotIn("dark", tokens)
        self.assertEqual(tokens["light"]["color"]["accent"]["$value"], "{color.named.signup}")


if __name__ == "__main__":
    unittest.main()
