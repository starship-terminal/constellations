#!/usr/bin/env python3
"""The measured Synthesia colours survive a rebuild, built in memory; every token has a source."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        import sys
        sys.path.insert(0, str(HERE / "tools"))
        import build_tokens  # importing writes nothing
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.render())

    def test_every_token_has_a_source_and_dimensions_are_lengths(self):
        import re
        tokens = json.loads((HERE / "tokens.json").read_text())

        def walk(node, path):
            for key, value in node.items():
                if key.startswith("$") or not isinstance(value, dict):
                    continue
                if "$value" in value:
                    yield f"{path}.{key}", value
                # A token can hold child tokens (core.color.base.dark.opacity-10, hover states),
                # so keep walking its non-$ keys too.
                yield from walk(value, f"{path}.{key}")
        for name in ("core", "light"):
            for path, token in walk(tokens[name], name):
                with self.subTest(token=path):
                    self.assertTrue(token.get("$extensions", {}).get("source"))
                    if token["$type"] == "dimension" and not token["$value"].startswith("{"):
                        self.assertRegex(token["$value"], r"^-?\d+(\.\d+)?(px|rem)$")

    def test_painted_values(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["indigo"]["500"]["$value"], "#3e57da")
        self.assertEqual(tokens["core"]["color"]["ink"]["$value"], "#090b22")
        self.assertEqual(tokens["light"]["color"]["bg"]["brand"]["$value"], "{color.indigo.500}")
        self.assertEqual(tokens["core"]["typography"]["hero"]["$value"]["fontSize"], "56px")
        self.assertIn("light", tokens)
        self.assertNotIn("dark", tokens)


if __name__ == "__main__":
    unittest.main()
