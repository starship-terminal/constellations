"""The Nextdoor token file matches the declared readings."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
DECLARED = json.loads((ROOT / "raw" / "tokens-declared.json").read_text())


class Tokens(unittest.TestCase):
    def test_brand_and_text(self):
        self.assertEqual(TOKENS["light"]["color"]["accent"]["$value"], "#1B8751")
        self.assertEqual(TOKENS["light"]["color"]["text"]["$value"], "#232F46")
        self.assertEqual(TOKENS["light"]["color"]["page"]["$value"], "#FFFFFF")
        self.assertEqual(TOKENS["dark"]["color"]["page"]["$value"], "#262626")

    def test_type_and_control(self):
        body = TOKENS["core"]["typography"]["body"]["$value"]
        self.assertEqual(body["fontSize"], "16px")
        self.assertEqual(body["fontWeight"], 420)
        self.assertEqual(TOKENS["light"]["component"]["buttonBrand"]["height"]["$value"], "48px")
        self.assertEqual(TOKENS["light"]["component"]["field"]["height"]["$value"], "56px")

    def test_declared_light_matches(self):
        self.assertEqual(
            TOKENS["light"]["color"]["muted"]["$value"],
            DECLARED["light"]["--nd-color-fgSecondary"],
        )


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
