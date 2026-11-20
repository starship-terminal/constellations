"""Checks for the Lummi token builder. Run from this folder, or via tools/package_tests.py.

The builder types its core values in by hand from the 2026-11-18 readings, so these
tests hold each one to raw/: a value labelled Measured must appear in the raw
readings, and the committed tokens.json must be what the builder writes.
"""
import json
import pathlib
import re
import unittest

import build_tokens

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = PKG / "tokens.json"
RAW = "".join((PKG / "raw" / name).read_text() for name in ("components-computed.json", "css-vars.json"))


def raw_forms(value):
    """The ways a literal can be written in the raw readings."""
    forms = {value}
    m = re.fullmatch(r"#([0-9a-f]{6})", value)
    if m:
        forms.add("rgb(%d, %d, %d)" % tuple(int(m.group(1)[i:i + 2], 16) for i in (0, 2, 4)))
    m = re.fullmatch(r"([\d.]+)ms", value)
    if m:
        forms.add("%gs" % (float(m.group(1)) / 1000))
    m = re.fullmatch(r"(\d+)px", value)
    if m:
        forms.add(m.group(1))
    return forms


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        built = build_tokens.build()
        build_tokens.check(built)
        self.assertEqual(json.loads(TOKENS.read_text()), built)

    def test_measured_literals_are_in_raw(self):
        flat = build_tokens.check(build_tokens.build())
        missing = []
        for path, tok in flat.items():
            value = tok["$value"]
            if not path.startswith("core.") or not isinstance(value, (str, int)) or "{" in str(value):
                continue
            if not tok["$extensions"]["source"].startswith("Measured"):
                continue
            text = str(value).replace('"', '\\"')
            if not any(f in RAW for f in raw_forms(text)):
                missing.append(f"{path}={value}")
        self.assertEqual(missing, [], "Measured values with no raw reading")

    def test_durations_are_typed_duration(self):
        doc = build_tokens.build()
        doc["core"]["motion"]["fast"]["$type"] = "dimension"
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(doc)

    def test_missing_alias_fails(self):
        doc = build_tokens.build()
        doc["light"]["link"]["$value"] = "{color.does-not-exist}"
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(doc)


if __name__ == "__main__":
    unittest.main()
