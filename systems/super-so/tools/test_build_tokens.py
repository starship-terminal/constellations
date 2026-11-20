#!/usr/bin/env python3
"""The Super.so token builder writes the measured colours and refuses a missing raw file."""
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class BuildTokensTest(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        # Built in memory; the committed file is never rewritten by the test.
        import build_tokens
        self.assertEqual((PKG / "tokens.json").read_text(), build_tokens.render())

    def test_refuses_a_missing_raw_file(self):
        # A copy of the builder beside an empty package folder: it must fail, not invent tokens.
        with tempfile.TemporaryDirectory() as d:
            tools = pathlib.Path(d) / "tools"
            tools.mkdir()
            (tools / "build_tokens.py").write_text((HERE / "build_tokens.py").read_text())
            done = subprocess.run([sys.executable, str(tools / "build_tokens.py")], cwd=tools,
                                  capture_output=True, text=True)
            self.assertNotEqual(done.returncode, 0)
            self.assertIn("foundations.json", done.stderr)
            self.assertFalse((pathlib.Path(d) / "tokens.json").exists())

    def test_dimensions_are_single_lengths(self):
        import re
        import build_tokens

        def walk(node):
            for k, v in node.items():
                if isinstance(v, dict) and "$value" in v:
                    yield k, v
                elif isinstance(v, dict) and not k.startswith("$"):
                    yield from walk(v)
        doc = build_tokens.build()
        for theme in ("core", "light", "dark"):
            for name, token in walk(doc[theme]):
                if token["$type"] == "dimension":
                    self.assertRegex(token["$value"], r"^-?\d+(\.\d+)?px$", name)

    def test_writes_measured_accent(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["accent"]["$value"], "#ffbe3c")
        self.assertEqual(tokens["dark"]["accent"]["$value"], "#ffb224")
        self.assertEqual(tokens["light"]["page"]["$value"], "#fdfdfc")
        self.assertEqual(tokens["dark"]["page"]["$value"], "#151514")
        self.assertIn("source", tokens["light"]["accent"]["$extensions"])
        self.assertIn("hero", tokens["core"]["typography"])

    def test_raw_file_is_the_only_input(self):
        raw = json.loads((PKG / "raw" / "foundations.json").read_text())
        self.assertEqual(raw["colors"]["accent"], "#ffbe3c")
        self.assertNotIn("invented", json.dumps(raw).lower())


if __name__ == "__main__":
    unittest.main()
