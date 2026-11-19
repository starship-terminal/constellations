"""The committed tokens.json passes the kit check. Run from this package's tools/."""
import importlib.util
import json
import pathlib
import unittest

TOOLS = pathlib.Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "typeform_build_tokens", TOOLS / "native" / "build_tokens.py")
build_tokens = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_tokens)

TOKENS = TOOLS.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_light_and_dark_share_keys(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("light", doc)
        self.assertIn("dark", doc)
        self.assertIn("core", doc)


if __name__ == "__main__":
    unittest.main()
