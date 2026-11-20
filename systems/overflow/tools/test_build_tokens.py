#!/usr/bin/env python3
"""The Overflow token build refuses a broken alias and round-trips the committed file."""
import json, pathlib, subprocess, sys, tempfile, unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from token_checks import alias_errors


class AliasTests(unittest.TestCase):
    def test_a_missing_alias_is_reported(self):
        core = {"color": {"ink": {"$value": "#000000", "$type": "color", "$extensions": {"source": "t"}}}}
        light = {"text": {"$value": "{color.missing}", "$type": "color", "$extensions": {"source": "t"}}}
        errs = alias_errors(core, light, {})
        self.assertTrue(any("color.missing" in e for e in errs))

    def test_committed_tokens_have_no_alias_gaps(self):
        tokens = json.loads((HERE.parent / "tokens.json").read_text())
        self.assertEqual(alias_errors(tokens["core"], tokens["light"], tokens.get("dark", {})), [])

    def test_builder_is_deterministic(self):
        subprocess.check_call([sys.executable, str(HERE / "build_component_tokens.py")], cwd=HERE.parent)
        subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")], cwd=HERE.parent)
        first = (HERE.parent / "tokens.json").read_text()
        subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")], cwd=HERE.parent)
        self.assertEqual(first, (HERE.parent / "tokens.json").read_text())


if __name__ == "__main__":
    unittest.main()
