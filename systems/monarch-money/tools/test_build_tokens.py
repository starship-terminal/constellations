"""tokens.json is what the builder writes from raw/, with every dimension a px or rem length."""
import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


def leaves(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from leaves(v, prefix + k + ".")


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_dimensions_are_lengths(self):
        doc = json.loads(build_tokens.TEXT)
        for s in ("core", "light"):
            for name, tok in leaves(doc.get(s, {})):
                if tok["$type"] == "dimension":
                    self.assertRegex(tok["$value"], r"^-?\d*\.?\d+(px|rem)$", f"{s}.{name}")

    def test_em_tracking_is_converted_at_the_role_size(self):
        tracking = json.loads(build_tokens.TEXT)["core"]["font"]["tracking"]["eyebrow"]
        self.assertEqual(tracking["$value"], "0.7px")  # .05em at 14px

    def test_missing_reading_fails(self):
        with self.assertRaises(SystemExit):
            build_tokens.need("--type-nothing-size")


if __name__ == "__main__":
    unittest.main()
