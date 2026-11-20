"""Tests for build_tokens' value checking on the glorify package.

Run from the package root: python3 -m unittest discover -s tools
The committed-tokens test walks systems/glorify/tokens.json so the check stays
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
    def test_committed_file_matches_an_in_memory_build(self):
        # build_tokens writes only under __main__, so importing it built the tokens without touching the file.
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.tokens)

    def test_weight_names_match_their_values(self):
        names = {100: "thin", 200: "extralight", 300: "light", 400: "regular", 500: "medium",
                 600: "semibold", 700: "bold", 800: "extrabold", 900: "black"}
        for name, tok in leaves(build_tokens.tokens["core"]["font"]["weight"]):
            self.assertEqual(names.get(tok["$value"]), name, name)

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


if __name__ == "__main__":
    unittest.main()
