"""The Open tokens resolve to the colours measured on o-p-e-n.com."""
import json
import re
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


class Tokens(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_cream_and_black(self):
        self.assertEqual(self.data["core"]["color"]["cream"]["$value"], "#eeece7")
        self.assertEqual(self.data["core"]["color"]["black"]["$value"], "#000000")
        self.assertEqual(self.data["core"]["color"]["copper"]["$value"], "#bf7d41")

    def test_themes(self):
        self.assertEqual(self.data["dark"]["text"]["$value"], "{color.cream}")
        self.assertEqual(self.data["light"]["page"]["$value"], "{color.cream}")
        self.assertEqual(self.data["dark"]["page"]["$value"], "{color.black}")

    def test_pill(self):
        self.assertEqual(self.data["core"]["radius"]["pill"]["$value"], "999px")
        self.assertEqual(self.data["core"]["size"]["control"]["$value"], "60px")


class EverySource(unittest.TestCase):
    """Every token names a source and every alias resolves (finding 22-9). tokens.json is written by hand
    here, so this is the check that notices a token added without $extensions.source."""

    DOC = json.loads((Path(__file__).resolve().parents[1] / "tokens.json").read_text())

    def leaves(self):
        flat = {}

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                flat[path] = node
            elif isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}" if path else key)

        for name, node in self.DOC.items():
            if not name.startswith("$"):
                walk(node, name)
        return flat

    def strings(self, value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, (dict, list)):
            for item in (value.values() if isinstance(value, dict) else value):
                yield from self.strings(item)

    def test_every_token_names_a_source(self):
        missing = [p for p, t in self.leaves().items() if not (t.get("$extensions") or {}).get("source")]
        self.assertEqual(missing, [])

    def test_every_alias_resolves(self):
        flat = self.leaves()
        dead = []
        for path, token in flat.items():
            for text in self.strings(token["$value"]):
                for ref in re.findall(r"\{([^{}]+)\}", text):
                    if not any(c in flat for c in (ref, f"{path.split('.')[0]}.{ref}", f"core.{ref}")):
                        dead.append((path, ref))
        self.assertEqual(dead, [])


if __name__ == "__main__":
    unittest.main()
