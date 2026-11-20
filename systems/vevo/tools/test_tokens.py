"""Vevo token file resolves. Run from this folder by tools/package_tests.py."""
import json
import pathlib
import re
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"
ALIAS = re.compile(r"\{([^}]+)\}")


def tokens_in(node, prefix=""):
    out = {}
    if not isinstance(node, dict):
        return out
    if "$value" in node:
        out[prefix] = node
        return out
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        out.update(tokens_in(value, path))
    return out


def flatten(node):
    return {path: tok["$value"] for path, tok in tokens_in(node).items()}


class TokenTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        data = json.loads(TOKENS.read_text())
        missing = [
            path
            for path, tok in tokens_in(data).items()
            if not str((tok.get("$extensions") or {}).get("source", "")).strip()
        ]
        self.assertEqual(missing, [])

    def test_aliases_resolve(self):
        data = json.loads(TOKENS.read_text())
        flat = flatten(data)
        self.assertIn("light.background.page", flat)
        self.assertIn("core.typography.display", flat)
        missing = []
        for path, value in flat.items():
            if not isinstance(value, str):
                continue
            match = ALIAS.fullmatch(value.strip())
            if not match:
                continue
            ref = match.group(1)
            set_name = path.split(".")[0]
            if not any(c in flat for c in (f"{set_name}.{ref}", f"core.{ref}", ref)):
                missing.append(f"{path} -> {ref}")
        self.assertEqual(missing, [])
