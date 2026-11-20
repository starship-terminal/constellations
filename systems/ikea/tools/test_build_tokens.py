"""tokens.json must rebuild from the raw readings: measured type steps carry their readings,
typed ones say so, aliases name no set, and no token holds another.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def nested(node, path=""):
    out = []
    if isinstance(node, dict):
        if "$value" in node and any(not k.startswith("$") for k in node):
            out.append(path)
        for k, v in node.items():
            if not k.startswith("$"):
                out += nested(v, f"{path}.{k}" if path else k)
    return out


class BuildTokensTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = build_tokens.build()

    def test_committed_tokens_match_builder(self):
        self.assertEqual(json.loads(TOKENS.read_text()), self.doc)

    def test_measured_type_steps(self):
        typ = self.doc["core"]["typography"]
        # login-heading (heading-l) paints 24/30 700; product-title (heading-s) 16/20 700.
        self.assertEqual(typ["heading-l"]["$value"]["lineHeight"], "30px")
        self.assertEqual(typ["heading-s"]["$value"]["lineHeight"], "20px")
        for key, tok in typ.items():
            src = tok["$extensions"]["source"]
            self.assertTrue("computed on" in src or "Reconstruction" in src, key)

    def test_aliases_name_no_set(self):
        self.assertEqual(re.findall(r"\{(?:core|light)\.[^}]*\}", json.dumps(self.doc)), [])

    def test_no_token_holds_tokens(self):
        self.assertEqual(nested(self.doc), [])


if __name__ == "__main__":
    unittest.main()
