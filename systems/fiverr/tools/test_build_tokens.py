"""Tests for build_tokens' value checking on the fiverr package.

Run from the package root: python3 -m unittest discover -s tools
The committed-tokens test walks systems/fiverr/tokens.json so the check stays
honest about the file the package actually ships.
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def leaves(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from leaves(v, prefix + k + ".")


def aliases(v):
    if isinstance(v, str):
        return build_tokens.re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


class CheckTest(unittest.TestCase):
    def test_colours_normalise(self):
        self.assertEqual(build_tokens.norm_color("rgb(29, 191, 115)"), "#1dbf73")
        self.assertEqual(build_tokens.norm_color("rgba(255, 255, 255, 0.1)"),
                         "rgba(255, 255, 255, 0.1)")
        self.assertEqual(build_tokens.norm_color("hsl(0, 0%, 96%)"), "#f5f5f5")

    def test_dimension_accepts_px_and_rem_only(self):
        build_tokens.check("t.x", "dimension", "42px")
        build_tokens.check("t.x", "dimension", "1.5rem")
        for bad in ("42", "42em", "42%", "auto"):
            with self.assertRaises(ValueError, msg=bad):
                build_tokens.check("t.x", "dimension", bad)

    def test_color_rejects_non_colours(self):
        for bad in ("soon", "url(x.png)", "42px"):
            with self.assertRaises(ValueError, msg=bad):
                build_tokens.check("t.x", "color", bad)

    def test_alias_strings_skip_check(self):
        # An alias is resolved by the alias pass, not the value check.
        build_tokens.check("t.x", "color", "{color.neutral.paper}")
        build_tokens.check("t.x", "dimension", "{space.m}")

    def test_duration_and_number(self):
        build_tokens.check("t.d", "duration", "150ms")
        with self.assertRaises(ValueError):
            build_tokens.check("t.d", "duration", "150s")
        with self.assertRaises(ValueError):
            build_tokens.check("t.n", "number", "3")
        with self.assertRaises(ValueError):
            build_tokens.check("t.w", "fontWeight", 400.0)


class CommittedTokensTest(unittest.TestCase):
    @unittest.skipUnless(TOKENS.exists(), "no tokens.json yet")
    def test_every_leaf_passes_check(self):
        doc = json.loads(TOKENS.read_text())
        for set_name, tree in doc.items():
            if set_name.startswith("$"):
                continue
            for name, tok in leaves(tree):
                with self.subTest(set=set_name, token=name):
                    self.assertIn("$type", tok, f"{set_name}.{name} has no $type")
                    self.assertIn("source", tok.get("$extensions", {}),
                                  f"{set_name}.{name} has no source evidence")
                    build_tokens.check(f"{set_name}.{name}", tok["$type"], tok["$value"])

    @unittest.skipUnless(TOKENS.exists(), "no tokens.json yet")
    def test_aliases_resolve(self):
        doc = json.loads(TOKENS.read_text())
        names = {n for tree in doc.values() if isinstance(tree, dict)
                 for n, _ in leaves(tree)}
        for set_name, tree in doc.items():
            if set_name.startswith("$"):
                continue
            for name, tok in leaves(tree):
                for a in aliases(tok["$value"]):
                    self.assertIn(a, names, f"{set_name}.{name}: alias {{{a}}} points at nothing")


RAW = pathlib.Path(__file__).resolve().parent.parent / "raw" / "components-computed.json"
COMPUTED = build_tokens.re.compile(r"computed (\w+) of (\S+) (\S+) \(raw/components-computed\.json\)$")


def same(raw, value):
    """A raw computed reading and the committed value it became."""
    if raw is None:
        return False
    if raw == value:
        return True
    try:
        if build_tokens.norm_color(raw) == value:
            return True
    except ValueError:
        pass
    m = build_tokens.re.fullmatch(r"([\d.]+)s", str(raw))
    if m and value == f"{float(m.group(1)) * 1000:g}ms":
        return True
    try:
        return float(raw) == float(value)
    except (TypeError, ValueError):
        return False


class MeasuredLeavesTest(unittest.TestCase):
    """Every leaf whose source names a computed reading carries that reading."""

    @unittest.skipUnless(TOKENS.exists() and RAW.exists(), "no tokens.json or raw readings")
    def test_computed_leaves_match_raw(self):
        doc = json.loads(TOKENS.read_text())
        comps = json.loads(RAW.read_text())
        comps = comps.get("components", comps)
        checked = 0
        for set_name, tree in doc.items():
            if set_name.startswith("$"):
                continue
            for name, tok in leaves(tree):
                m = COMPUTED.match(tok.get("$extensions", {}).get("source", ""))
                if not m:
                    continue
                prop, comp, state = m.groups()
                with self.subTest(token=f"{set_name}.{name}"):
                    st = comps[comp]["states"][state]
                    self.assertNotEqual(st.get("via"), "focus failed")
                    raw = [(st.get("style") or {}).get(prop), (st.get("textStyle") or {}).get(prop)]
                    self.assertTrue(any(same(r, tok["$value"]) for r in raw),
                                    f"{tok['$value']!r} is not the raw {prop} {raw}")
                    checked += 1
        self.assertGreater(checked, 30)

    @unittest.skipUnless(TOKENS.exists(), "no tokens.json yet")
    def test_no_transparent_colour(self):
        # A transparent reading (alpha 0) paints nothing; committed as a fill it hands a
        # consumer an invisible surface.
        doc = json.loads(TOKENS.read_text())
        for set_name, tree in doc.items():
            if set_name.startswith("$"):
                continue
            for name, tok in leaves(tree):
                if tok.get("$type") == "color" and isinstance(tok["$value"], str):
                    self.assertNotRegex(tok["$value"], r"^(transparent|rgba\([^)]*,\s*0\))$",
                                        f"{set_name}.{name}")


if __name__ == "__main__":
    unittest.main()
