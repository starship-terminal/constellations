"""The Stocksy tokens resolve, and the measured brand green is the accent."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parents[1] / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_accent_is_the_measured_green(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["dark"]["color"]["action"]["fill"]["$value"], "#0ae47c")
        self.assertEqual(data["dark"]["color"]["bg"]["page"]["$value"], "#000000")
        self.assertEqual(data["core"]["font"]["family"]["brand"]["$value"][0], "Poppins")

    def test_component_aliases_point_at_a_real_token(self):
        data = json.loads(TOKENS.read_text())

        def walk(node, path, found):
            if isinstance(node, dict):
                if "$value" in node and isinstance(node["$value"], str) and node["$value"].startswith("{"):
                    found.append((path, node["$value"].strip("{}")))
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, path + [key], found)

        refs = []
        walk(data, [], refs)
        flat = set()

        def flatten(node, path):
            if isinstance(node, dict) and "$value" in node:
                flat.add(".".join(path))
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        flatten(child, path + [key])

        flatten(data, [])
        missing = [ref for _, ref in refs if ref not in flat]
        self.assertEqual(missing, [])


# ---- every token records where its value came from (docs/EVIDENCE.md)
import json as _json
import pathlib as _pathlib

_TOKENS_FILE = _pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def _unsourced(node, path=()):
    """Dotted paths of leaves whose $extensions.source is missing or empty."""
    out = []
    for key, child in node.items():
        if key.startswith("$") or not isinstance(child, dict):
            continue
        if "$value" in child:
            source = (child.get("$extensions") or {}).get("source")
            if not source:
                out.append(".".join(path + (key,)))
        else:
            out.extend(_unsourced(child, path + (key,)))
    return out


class EverySourcedTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = _unsourced(_json.loads(_TOKENS_FILE.read_text()))
        self.assertEqual(missing, [], "tokens with no $extensions.source")

    def test_unsourced_leaf_is_reported(self):
        tree = {"core": {"a": {"$value": "#000", "$extensions": {"source": {}}},
                         "b": {"$value": "#fff", "$extensions": {"source": {"evidence": "Measured"}}}}}
        self.assertEqual(_unsourced(tree), ["core.a"])


if __name__ == "__main__":
    unittest.main()
