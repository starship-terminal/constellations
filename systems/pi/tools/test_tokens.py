"""Checks the committed tokens.json. Run from the package tools folder."""
import json
import pathlib
import re
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def walk(node, prefix=()):
    if isinstance(node, dict) and "$value" in node:
        yield prefix, node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value, prefix + (key,))


class TokensTest(unittest.TestCase):
    def test_committed_file(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("light", doc)
        self.assertIn("dark", doc)
        light = sorted(".".join(p) for p, _ in walk(doc["light"]))
        dark = sorted(".".join(p) for p, _ in walk(doc["dark"]))
        self.assertEqual(light, dark)
        paths = {".".join(p) for name in ("core", "light", "dark") for p, _ in walk(doc[name])}
        for name in ("core", "light", "dark"):
            for path, token in walk(doc[name]):
                where = name + "." + ".".join(path)
                source = token.get("$extensions", {}).get("source")
                self.assertTrue(source, where)
                value = token["$value"]
                if isinstance(value, str) and re.fullmatch(r"\{[^}]+\}", value):
                    ref = value[1:-1]
                    self.assertTrue(
                        f"{name}.{ref}" in paths or f"core.{ref}" in paths or ref in paths,
                        f"{where} alias {value}",
                    )
                    continue
                if token.get("$type") == "color" and isinstance(value, str) and value.startswith("#"):
                    self.assertRegex(value, r"#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?")
                if token.get("$type") == "dimension":
                    self.assertRegex(value, r"-?\d+(\.\d+)?(px|rem)")


if __name__ == "__main__":
    unittest.main()
