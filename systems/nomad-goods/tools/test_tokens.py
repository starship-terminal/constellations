"""The Nomad Goods token file resolves, is what build_tokens.build() makes from raw/ (built in memory,
nothing written), and every Measured value is one raw/readings.json holds."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_tokens  # noqa: E402
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def flatten(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        return {path: node["$value"]}
    out = {}
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            out.update(flatten(child, f"{path}.{key}" if path else key))
    return out


FLAT = flatten(TOKENS)


def resolve(value, depth=0):
    if depth > 8 or not isinstance(value, str) or not (value.startswith("{") and value.endswith("}")):
        return value
    ref = value[1:-1]
    if ref not in FLAT:
        raise AssertionError(f"missing alias {ref}")
    return resolve(FLAT[ref], depth + 1)


class TokenFile(unittest.TestCase):
    def test_page_colour_is_the_measured_grey(self):
        self.assertEqual(resolve(FLAT["light.background.page"]), "#f3f3f3")

    def test_primary_text_is_black(self):
        self.assertEqual(resolve(FLAT["light.text.primary"]), "#000000")

    def test_display_size_is_the_desktop_computed_size(self):
        self.assertEqual(FLAT["core.typography.display"]["fontSize"], "77px")

    def test_every_alias_resolves(self):
        for path, value in FLAT.items():
            if isinstance(value, str) and value.startswith("{"):
                resolve(value)
            if isinstance(value, dict):
                for item in value.values():
                    if isinstance(item, str) and item.startswith("{"):
                        resolve(item)


class Builder(unittest.TestCase):
    def test_committed_file_is_what_the_builder_makes(self):
        self.assertEqual(TOKENS, build_tokens.build())

    def test_every_token_has_a_source_and_evidence(self):
        self.assertGreater(build_tokens.check(copy.deepcopy(TOKENS)), 100)

    def test_a_token_without_evidence_fails(self):
        doc = copy.deepcopy(TOKENS)
        del doc["core"]["color"]["page"]["$extensions"]["evidence"]
        with self.assertRaisesRegex(SystemExit, "no source or evidence"):
            build_tokens.check(doc)

    def test_a_duration_typed_as_dimension_fails(self):
        doc = copy.deepcopy(TOKENS)
        doc["core"]["space"]["4"]["$value"] = "150ms"
        with self.assertRaisesRegex(SystemExit, "not one px length"):
            build_tokens.check(doc)

    def test_a_missing_reading_stops_the_build(self):
        with self.assertRaisesRegex(SystemExit, "no computed.nope"):
            build_tokens.R("nope.width")

    def test_measured_colours_and_lengths_are_in_raw(self):
        raw = (ROOT / "raw" / "readings.json").read_text()
        rgb = {"#%02x%02x%02x" % tuple(int(x) for x in m)
               for m in __import__("re").findall(r"rgba?\((\d+),\s*(\d+),\s*(\d+)", raw)}
        for path, t in leaves(TOKENS["core"]):
            if t["$extensions"]["evidence"] != "Measured" or not isinstance(t["$value"], str):
                continue
            if t["$type"] == "color":
                self.assertIn(t["$value"][:7], rgb, path)
            elif t["$type"] == "dimension":   # a px length, or a viewport width recorded as a number
                self.assertTrue(f'"{t["$value"]}' in raw or f'{t["$value"][:-2]},' in raw or f' {t["$value"]}' in raw, path)

    def test_no_success_colour_is_invented(self):
        self.assertNotIn("success", TOKENS["light"]["status"])


def leaves(node, path="core"):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
    elif isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from leaves(v, f"{path}.{k}")


if __name__ == "__main__":
    unittest.main()
