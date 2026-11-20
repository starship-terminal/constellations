"""tokens.json and style-guide.html must rebuild from the committed raw readings, and every token
that cites a measured reading must carry that reading.

The builders run on a temporary copy of the package, so the committed files are never rewritten.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILT = ("tokens.json", "style-guide.html")
# "measured <prop> on <component>.<state> (<page>, <date>)", as build_tokens.measured() writes it.
CITE = re.compile(r"^measured (textStyle\.)?(\w+) on ([\w-]+)\.([\w-]+) \(")
HAND = "Reconstruction: entered by hand at capture time"


def leaves(node, path=()):
    if isinstance(node, dict):
        if "$value" in node:
            yield path, node
            return
        for k, v in node.items():
            if not k.startswith("$"):
                yield from leaves(v, path + (k,))


def norm(c):
    m = re.fullmatch(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", c.strip())
    if not m:
        return c
    r, g, b, a = m.groups()
    if a is None or float(a) >= 1:
        return "#%02x%02x%02x" % (int(r), int(g), int(b))
    return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))


class RebuildTest(unittest.TestCase):
    def test_builders_reproduce_committed_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__"))
            for builder in ("build_tokens.py", "build_style_guide.py"):
                subprocess.run([sys.executable, str(copy / "tools" / builder)], check=True, capture_output=True)
            for name in BUILT:
                self.assertEqual((copy / name).read_text(), (PKG / name).read_text(), name)

    def test_cited_colours_and_sizes_match_the_reading(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        comps = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        checked = 0
        for path, tok in leaves(tokens):
            if tok["$type"] not in ("color", "dimension"):
                continue
            m = CITE.match(str(tok.get("$extensions", {}).get("source", "")))
            if not m:
                continue
            text, prop, comp, state = m.groups()
            s = comps[comp]["states"][state]
            raw = (s.get("textStyle") or {})[prop] if text else s["style"][prop]
            self.assertEqual(str(tok["$value"]), norm(raw), ".".join(path))
            checked += 1
        self.assertGreater(checked, 30)

    def test_hand_values_are_labelled(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        hand = [("core", "color", "ground", "light-card"), ("core", "color", "accent", "violet"),
                ("core", "color", "accent", "link"), ("core", "color", "price", "struck"),
                ("light", "background", "surface"), ("light", "background", "raised"),
                ("core", "spacing", "2"), ("core", "spacing", "3"), ("core", "spacing", "4")]
        for path in hand:
            node = tokens
            for k in path:
                node = node[k]
            self.assertTrue(node["$extensions"]["source"].startswith(HAND), ".".join(path))
        # Nothing else claims a hand value, and nothing hand-entered still says measured.
        labelled = [p for p, t in leaves(tokens) if str(t.get("$extensions", {}).get("source", "")).startswith(HAND)]
        self.assertEqual(sorted(labelled), sorted(hand))


if __name__ == "__main__":
    unittest.main()
