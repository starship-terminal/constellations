"""The Orchids token build copies measured readings and does not invent a ramp.

build_tokens.build() runs in memory; nothing here writes tokens.json."""

import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())


class BuildTokensTest(unittest.TestCase):
    def test_committed_file_is_what_the_builder_makes(self):
        self.assertEqual(TOKENS, build_tokens.build())

    def test_primary_is_the_measured_amber(self):
        self.assertEqual(TOKENS["core"]["color"]["primary"]["$value"], "#fcaa26")
        self.assertEqual(TOKENS["light"]["page"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["dark"]["page"]["$value"], "#0e0c0c")
        self.assertIn("source", TOKENS["core"]["color"]["primary"]["$extensions"])

    def test_paused_colours_stay_out_of_the_product_accent(self):
        # raw/css-vars.json reads the paused page link as rgb(0, 112, 243); the token is its hex.
        self.assertEqual(TOKENS["core"]["color"]["paused"]["link"]["$value"], "#0070f3")
        self.assertNotEqual(TOKENS["light"]["accent"]["$value"], "#0070f3")

    def test_colours_are_hex_and_durations_are_durations(self):
        def leaves(node, path=""):
            if isinstance(node, dict) and "$value" in node:
                yield path, node
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        yield from leaves(v, f"{path}.{k}")

        for path, t in leaves({k: TOKENS[k] for k in ("core", "light", "dark")}):
            if t["$type"] == "color":
                self.assertRegex(t["$value"], r"^(#[0-9a-f]{6}|\{[^}]+\})$", path)
            if t["$type"] == "dimension":
                self.assertNotRegex(t["$value"], r"m?s$", path)
            if ".motion.duration." in path:
                self.assertEqual(t["$type"], "duration", path)


if __name__ == "__main__":
    unittest.main()
