"""Package token check. Run from the package tools/ directory."""
import json
import pathlib
import re
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def walk(node, path=()):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        yield path, node
        return
    for key, child in node.items():
        if key.startswith("$"):
            continue
        yield from walk(child, path + (key,))


def aliases(value):
    if isinstance(value, str):
        return re.findall(r"\{([^}]+)\}", value)
    if isinstance(value, dict):
        out = []
        for v in value.values():
            out.extend(aliases(v))
        return out
    return []


class TokenFileTest(unittest.TestCase):
    def test_committed_tokens(self):
        doc = json.loads(TOKENS.read_text())
        paths = {".".join((name,) + p) for name in ("core", "light") for p, _ in walk(doc[name])}
        self.assertIn("light", doc)
        self.assertNotIn("dark", doc)
        for name in ("core", "light"):
            for p, token in walk(doc[name]):
                where = name + "." + ".".join(p)
                src = token.get("$extensions", {}).get("source", {})
                self.assertTrue(src.get("evidence") and src.get("capture"), where)
                for alias in aliases(token["$value"]):
                    self.assertIn(alias, paths, f"{where} alias {{{alias}}}")
                value = token["$value"]
                if isinstance(value, str) and value.startswith("{"):
                    continue
                if token["$type"] == "color" and isinstance(value, str):
                    self.assertRegex(value, r"#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?")
                if token["$type"] == "dimension":
                    self.assertRegex(value, r"-?\d+(\.\d+)?px")


if __name__ == "__main__":
    unittest.main()
