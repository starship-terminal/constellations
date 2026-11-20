"""The committed Tesla tokens pass build_tokens.check, and keep the measured primary, page and text colours."""
import json
import pathlib
import unittest

import importlib.util

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("build_tokens", HERE / "build" / "build_tokens.py")
build_tokens = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_tokens)

TOKENS = HERE.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        doc = json.loads(TOKENS.read_text())
        build_tokens.check(doc)

    def test_primary_is_measured_blue(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["light"]["color"]["color-primary"]["$value"], "#3e6ae1")
        self.assertEqual(doc["light"]["color"]["color-primary"]["$extensions"]["marketing"], "#171a20")

    def test_page_and_text(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["light"]["color"]["theme-background"]["$value"], "#ffffff")
        self.assertEqual(doc["dark"]["color"]["theme-background"]["$value"], "#000000")
        self.assertEqual(doc["light"]["color"]["theme-foreground"]["$value"], "#393c41")


if __name__ == "__main__":
    unittest.main()
