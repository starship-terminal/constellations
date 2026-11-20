"""Committed tokens: dark provenance cites the dark declaration, and no token is also a group."""
import json
import pathlib
import unittest

TOKENS = json.loads((pathlib.Path(__file__).resolve().parent.parent / "tokens.json").read_text())


def walk(node, path=""):
    if isinstance(node, dict):
        yield path, node
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, f"{path}.{k}" if path else k)


class Outputs(unittest.TestCase):
    def test_no_token_holds_tokens(self):
        bad = [p for p, n in walk(TOKENS) if "$value" in n and any(not k.startswith("$") for k in n)]
        self.assertEqual(bad, [])

    def test_dark_alias_cites_its_own_declaration(self):
        t = TOKENS["dark"]["button"]["critical"]["background"]["active"]
        src = t["$extensions"]["source"]
        self.assertEqual(t["$value"], "{palette.gds.red.10}")
        self.assertIn("declared as var(--red-10)", src)
        self.assertIn('data-gds-theme="dark"', src.split(";")[0])


if __name__ == "__main__":
    unittest.main()
