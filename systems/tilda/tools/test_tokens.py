"""Checks for the Tilda tokens file. Run from this package's tools/ folder."""
import json
import pathlib
import re
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"
HEX = re.compile(r"^#[0-9A-F]{6}$")
DIM = re.compile(r"^-?\d+(\.\d+)?px$")


def walk(node, prefix=()):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = prefix + (key,)
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


class TokenFileTest(unittest.TestCase):
    def test_file_loads_and_has_light_only(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("core", doc)
        self.assertIn("light", doc)
        self.assertNotIn("dark", doc)
        self.assertGreater(len(list(walk(doc["core"]))), 10)

    def test_every_token_has_a_source_and_a_legal_value(self):
        doc = json.loads(TOKENS.read_text())
        paths = {".".join(path) for name in ("core", "light") for path, _ in walk(doc[name])}
        for name in ("core", "light"):
            for path, token in walk(doc[name]):
                where = name + "." + ".".join(path)
                source = token.get("$extensions", {}).get("source", {})
                self.assertTrue(source.get("evidence") and source.get("capture"), where)
                value = token["$value"]
                if isinstance(value, str) and value.startswith("{"):
                    self.assertIn(value.strip("{}"), paths, where)
                    continue
                kind = token["$type"]
                if kind == "color":
                    self.assertRegex(value, HEX, where)
                elif kind == "dimension":
                    self.assertRegex(value, DIM, where)
                elif kind == "typography":
                    self.assertIn("fontSize", value, where)
                    self.assertRegex(value["fontSize"], DIM, where)


if __name__ == "__main__":
    unittest.main()
