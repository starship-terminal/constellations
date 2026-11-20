"""Nothing tokens stay tied to the capture readings."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / name).read_text())


class TokenTests(unittest.TestCase):
    def test_measured_colours_match_readings(self):
        tokens = load("tokens.json")
        readings = load("raw/readings.json")
        self.assertEqual(tokens["light"]["background"]["page"]["$value"], "#f4f4f4")
        self.assertEqual(tokens["light"]["action"]["accent"]["$value"], "#ffc700")
        self.assertEqual(tokens["light"]["surface"]["footer"]["$value"], "#040404")
        self.assertEqual(tokens["dark"]["background"]["page"]["$value"], "#181818")
        declared = readings["declaredRoot"]
        self.assertEqual(declared["greyscale-100"], "244 244 244")
        self.assertEqual(declared["accent-yellow"], "255 199 0")
        self.assertEqual(declared["greyscale-black"], "4 4 4")
        self.assertEqual(declared["greyscale-dm-light"], "24 24 24")

    def test_radius_and_type_are_the_computed_ones(self):
        tokens = load("tokens.json")
        self.assertEqual(tokens["core"]["radius"]["default"]["$value"], "4px")
        self.assertEqual(tokens["core"]["radius"]["md"]["$value"], "6px")
        self.assertEqual(tokens["core"]["typography"]["display-xl"]["$value"]["fontSize"], "48px")
        self.assertEqual(tokens["core"]["font"]["family"]["ui"]["$value"], "NType82-Regular, sans-serif")

    def test_screenshot_gap_is_recorded(self):
        readings = load("raw/readings.json")
        self.assertIn("not producing screenshot frames", readings["viewport"]["note"])


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

    def dead_aliases(self, flat):
        """(path, reference) for every alias that names no token or that loops back on itself."""
        def target(path, ref):
            return next((c for c in (ref, f"{path.split('.')[0]}.{ref}", f"core.{ref}") if c in flat), None)

        def reaches_a_value(path, ref, seen):
            at = target(path, ref)
            if at is None or at in seen:
                return False
            for text in self.strings(flat[at]["$value"]):
                for inner in re.findall(r"\{([^{}]+)\}", text):
                    if not reaches_a_value(at, inner, seen | {at}):
                        return False
            return True

        return [(path, ref) for path, token in flat.items() for text in self.strings(token["$value"])
                for ref in re.findall(r"\{([^{}]+)\}", text) if not reaches_a_value(path, ref, {path})]

    def test_every_alias_resolves(self):
        self.assertEqual(self.dead_aliases(self.leaves()), [])

    def test_a_circular_alias_fails(self):
        flat = self.leaves()
        path = next(p for p, t in flat.items() if t.get("$type") == "color")
        flat[path] = {**flat[path], "$value": "{" + path.split(".", 1)[1] + "}"}
        self.assertTrue(self.dead_aliases(flat))


if __name__ == "__main__":
    unittest.main()
