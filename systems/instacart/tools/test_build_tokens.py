"""tokens.json must rebuild from the raw readings, and every value whose source names a
computed reading must be that reading.

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


def leaves(node, path=""):
    if isinstance(node, dict):
        if "$value" in node:
            yield path, node
            return
        for k, v in node.items():
            if not k.startswith("$"):
                yield from leaves(v, f"{path}.{k}" if path else k)


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.doc)

    def test_computed_dimensions_are_the_readings(self):
        n = 0
        for path, tok in leaves(build_tokens.doc):
            m = re.match(r"computed (\w+) of (\S+) \(raw/components-computed\.json\)", tok["$extensions"]["source"])
            if not m or tok["$type"] != "dimension":
                continue
            self.assertEqual(tok["$value"], build_tokens.reading(m.group(2), m.group(1)), path)
            n += 1
        self.assertGreaterEqual(n, 9)

    def test_typed_values_say_so(self):
        typ = build_tokens.doc["core"]["typography"]
        for key in ("heading", "display"):
            self.assertTrue(typ[key]["$extensions"]["source"].startswith("Reconstruction"), key)
        self.assertTrue(build_tokens.doc["core"]["font"]["weight"]["bold"]["$extensions"]["source"].startswith("Reconstruction"))


if __name__ == "__main__":
    unittest.main()
