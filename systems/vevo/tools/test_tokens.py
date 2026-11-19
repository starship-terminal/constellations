"""Vevo token file resolves. Run from this folder by tools/package_tests.py."""
import json
import pathlib
import re
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"
ALIAS = re.compile(r"\{([^}]+)\}")


def flatten(node, prefix=""):
    out = {}
    if not isinstance(node, dict):
        return out
    if "$value" in node:
        out[prefix] = node["$value"]
        return out
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        out.update(flatten(value, path))
    return out


class TokenTest(unittest.TestCase):
    def test_aliases_resolve_and_sources_exist(self):
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
        self.assertTrue(data["light"]["background"]["page"]["$extensions"]["source"])
