"""The package tokens file passes build_tokens.check."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_dark_page_is_black(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["dark"]["background"]["page"]["$value"], "#000000")
        self.assertNotIn("light", doc)


def _tok(value="#000000", ty="color"):
    return {"$value": value, "$type": ty,
            "$extensions": {"source": {"evidence": "Measured", "capture": "test"}}}


def _doc(**sets):
    return {name: tree for name, tree in sets.items()}


class CheckNegativeTest(unittest.TestCase):
    """build_tokens.check refuses broken trees, built in memory."""

    def test_minimal_tree_passes(self):
        build_tokens.check(_doc(core={"c": _tok()}, dark={"page": _tok("{c}")}))

    def test_missing_alias_inside_typography_fails(self):
        type_tok = _tok({"fontFamily": "{font.nope}", "fontSize": "16px"}, "typography")
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(_doc(core={"c": _tok()}, dark={"body": type_tok}))

    def test_dead_top_level_alias_fails(self):
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(_doc(core={"c": _tok()}, dark={"page": _tok("{nope}")}))

    def test_missing_source_fails(self):
        bare = {"$value": "#000000", "$type": "color"}
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(_doc(core={"c": bare}))

    def test_light_and_dark_keys_differ_fails(self):
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(_doc(core={"c": _tok()}, light={"page": _tok()}, dark={"other": _tok()}))


if __name__ == "__main__":
    unittest.main()
