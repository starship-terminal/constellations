#!/usr/bin/env python3
"""The Rivian token build is deterministic and keeps a source on every token."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class BuildTokens(unittest.TestCase):
    def test_build_is_stable_and_sourced(self):
        # main() builds in memory; only write() touches tokens.json, so a mismatch leaves it alone.
        import build_tokens
        before = (PKG / "tokens.json").read_text()
        self.assertEqual(before, json.dumps(build_tokens.main(), indent=2) + "\n")
        tokens = json.loads(before)
        self.assertIn("light", tokens)
        self.assertNotIn("dark", tokens)

        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                self.assertIn("source", node.get("$extensions", {}))
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child)

        walk(tokens["core"])
        walk(tokens["light"])
        self.assertEqual(tokens["light"]["page"]["$value"], "#ffffff")
        self.assertEqual(tokens["light"]["accent"]["$value"], "#ffaa00")
        self.assertEqual(tokens["light"]["text"]["$value"], "#000000")
        self.assertEqual(tokens["core"]["control"]["header-height"]["$value"], "56px")
        self.assertEqual(tokens["core"]["radius"]["mega"]["$value"], "40px")


if __name__ == "__main__":
    unittest.main()
