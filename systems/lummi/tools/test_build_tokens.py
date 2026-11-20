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


def raw_leaves():
    """Every string and number in the raw readings, whole: a value matches only when it equals one."""
    out = set()

    def walk(n):
        if isinstance(n, dict):
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)
        elif not isinstance(n, bool):
            out.add(n)

    for name in ("components-computed.json", "css-vars.json"):
        walk(json.loads((PKG / "raw" / name).read_text()))
    return out


RAW = raw_leaves()
RAW_STRINGS = [x for x in RAW if isinstance(x, str)]


def raw_forms(value):
    """The whole values a literal can be recorded as in the readings."""
    forms = {value}
    m = re.fullmatch(r"#([0-9a-f]{6})", value)
    if m:
        forms.add("rgb(%d, %d, %d)" % tuple(int(m.group(1)[i:i + 2], 16) for i in (0, 2, 4)))
    m = re.fullmatch(r"([\d.]+)ms", value)
    if m:
        forms.add("%gs" % (float(m.group(1)) / 1000))
    m = re.fullmatch(r"(\d+)px", value)
    if m:
        forms.add(int(m.group(1)))
    return forms


def shadow_css(layers):
    return ", ".join(f"{l['color']} {l['offsetX']} {l['offsetY']} {l['blur']} {l['spread']}" for l in layers)


def literals(path, value):
    """(path, literal) for every literal inside a token value; aliases are skipped."""
    if isinstance(value, dict):
        for k, v in value.items():
            yield from literals(f"{path}.{k}", v)
    elif isinstance(value, list):
        if all(isinstance(x, (int, float)) for x in value):          # a cubic-bezier
            yield path, "cubic-bezier(%s)" % ", ".join("%g" % x for x in value)
        else:
            for i, v in enumerate(value):
                yield from literals(f"{path}[{i}]", v)
    elif isinstance(value, str) and value.startswith("{"):
        return
    else:
        yield path, value


def in_raw(value):
    if isinstance(value, (int, float)):
        return value in RAW or str(value) in RAW
    return any(f in RAW for f in raw_forms(value))


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        built = build_tokens.build()
        build_tokens.check(built)
        self.assertEqual(json.loads(TOKENS.read_text()), built)

    def test_measured_literals_are_in_raw(self):
        flat = build_tokens.check(build_tokens.build())
        missing = []
        for path, tok in flat.items():
            if not path.startswith("core.") or not tok["$extensions"]["source"].startswith("Measured"):
                continue
            if tok["$type"] == "shadow":
                css = shadow_css(tok["$value"])
                if not any(x == css or x.endswith(", " + css) for x in RAW_STRINGS):
                    missing.append(f"{path}={css}")
                continue
            for where, value in literals(path, tok["$value"]):
                if not in_raw(value):
                    missing.append(f"{where}={value}")
        self.assertEqual(missing, [], "Measured values with no raw reading")

    def test_a_partial_match_is_not_a_reading(self):
        # 440 appears inside the recorded viewport width 1440, but 440px is no reading
        self.assertFalse(in_raw("440px"))
        self.assertTrue(in_raw("40px"))

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
