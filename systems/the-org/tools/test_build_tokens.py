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

    def test_light_only(self):
        tokens = json.loads(TOKENS.read_text())
        self.assertIn("light", tokens)
        self.assertNotIn("dark", tokens)
        self.assertEqual(tokens["light"]["color"]["accent"]["$value"], "{color.named.signup}")


if __name__ == "__main__":
    unittest.main()
