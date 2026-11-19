"""The committed tokens.json matches a fresh build, and every token has a source."""
import json
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
TOKENS = PKG / "tokens.json"


def walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value)


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_rebuild(self):
        before = TOKENS.read_text()
        subprocess.run([sys.executable, str(HERE / "build_tokens.py")], check=True, cwd=PKG)
        self.assertEqual(TOKENS.read_text(), before)

    def test_every_token_has_a_source(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("light", doc)
        self.assertNotIn("dark", doc)
        for token in walk(doc):
            source = token.get("$extensions", {}).get("source")
            self.assertTrue(source, token)


if __name__ == "__main__":
    unittest.main()
