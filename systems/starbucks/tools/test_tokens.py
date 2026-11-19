"""Checks the committed Starbucks tokens. Run from the package tools/ directory."""
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
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, prefix + (key,))


class StarbucksTokens(unittest.TestCase):
    def test_every_token_has_a_source_and_a_resolvable_alias(self):
        doc = json.loads(TOKENS.read_text())
        paths = {".".join(p) for p, _ in walk(doc)}
        self.assertIn("light.background.page", paths)
        self.assertIn("light.action.accent-bg", paths)
        for path, token in walk(doc):
            where = ".".join(path)
            source = token.get("$extensions", {}).get("source")
            self.assertIsInstance(source, str, where)
            self.assertGreater(len(source), 12, where)
            value = token["$value"]
            if isinstance(value, str):
                for alias in re.findall(r"\{([^{}]+)\}", value):
                    self.assertIn(alias, paths, where)
            if token.get("$type") == "dimension" and isinstance(value, str) and not value.startswith("{"):
                self.assertRegex(value, r"^-?\d+(\.\d+)?px$")


if __name__ == "__main__":
    unittest.main()
