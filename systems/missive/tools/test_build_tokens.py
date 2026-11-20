"""The Missive token file stays a valid DTCG document the builder can rebuild."""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (builds in memory; writes only when run as a script)


class Tokens(unittest.TestCase):
    def test_sets_and_brand(self):
        doc = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(set(doc), {"core", "light", "dark", "$themes", "$metadata"})
        self.assertEqual(doc["core"]["color"]["brand"]["$value"], "#2266ed")
        self.assertEqual(doc["light"]["accent"]["$value"], "{color.brand}")
        self.assertEqual(doc["dark"]["page"]["$value"], "#1d1e1f")
        self.assertIn("motion", doc["core"])

    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_dark_set_reads_raw(self):
        raw = json.loads((ROOT / "raw" / "css-vars.json").read_text())["resolved"]["dark"]
        self.assertEqual(build_tokens.hex_of(raw["--background-color"]["value"]), build_tokens.dark["page"]["$value"])
        self.assertEqual(build_tokens.hex_of(raw["--input-background-color"]["value"]), build_tokens.dark["mailSurface"]["$value"])
        self.assertEqual(build_tokens.dark["border"]["$value"], "rgba(225, 226, 228, 0.14)")

    def test_dark_reading_must_parse(self):
        saved = dict(build_tokens.DARK)
        try:
            build_tokens.DARK["--text-color-a"] = {"value": "var(--unset)"}
            with self.assertRaises(SystemExit):
                build_tokens.dark_hex("--text-color-a")
            del build_tokens.DARK["--text-color-a"]
            with self.assertRaises(SystemExit):
                build_tokens.dark_hex("--text-color-a")
        finally:
            build_tokens.DARK.clear()
            build_tokens.DARK.update(saved)

    def test_dimensions_are_lengths(self):
        doc = json.loads((ROOT / "tokens.json").read_text())

        def walk(node):
            for k, v in node.items():
                if k.startswith("$"):
                    continue
                if isinstance(v, dict) and "$value" in v:
                    yield k, v
                elif isinstance(v, dict):
                    yield from walk(v)

        for name, tok in walk(doc["core"]):
            if tok.get("$type") == "dimension":
                self.assertRegex(tok["$value"], r"^-?\d+(\.\d+)?(px|rem)$", name)


if __name__ == "__main__":
    unittest.main()
