"""tokens.json and style-guide.html must rebuild from the committed raw readings, and every token
that cites a measured component reading must carry that reading.

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
# "<label>: <component>.<state> <prop>, <note>", as build_tokens.cm()/dm() write it.
CITE = re.compile(r"^Measured computed style, public[^:]*: ([\w-]+)\.([\w-]+) (\w+), ")
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
            # Remove the committed outputs first, so a builder that writes nothing cannot pass.
            for name in BUILT:
                (copy / name).unlink()
            for builder in ("build_tokens.py", "build_style_guide.py"):
                subprocess.run([sys.executable, str(copy / "tools" / builder)], check=True, capture_output=True)
            for name in BUILT:
                self.assertEqual((copy / name).read_text(), (PKG / name).read_text(), name)

    def test_cited_values_match_the_reading(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        comps = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        checked = 0
        for path, tok in leaves(tokens):
            m = CITE.match(str(tok.get("$extensions", {}).get("source", "")))
            if not m or tok["$type"] not in ("color", "dimension", "fontWeight"):
                continue
            comp, state, prop = m.groups()
            raw = comps[comp]["states"][state]["style"][prop]
            want = norm(raw) if tok["$type"] == "color" else (int(raw) if tok["$type"] == "fontWeight" else raw)
            self.assertEqual(tok["$value"], want, ".".join(path))
            checked += 1
        self.assertGreater(checked, 40)

    def test_corrected_values(self):
        core = json.loads((PKG / "tokens.json").read_text())["core"]
        self.assertEqual(core["font"]["size"]["menu"]["$value"], "12.8px")
        self.assertEqual(core["typography"]["heading"]["$value"]["lineHeight"], "41.4px")
        self.assertEqual(core["typography"]["body-lg"]["$value"]["lineHeight"], "29.25px")
        self.assertEqual(core["elevation"]["card"]["$value"][0]["color"], "rgba(30, 41, 59, 0.15)")
        self.assertEqual(len(core["elevation"]["control"]["$value"]), 2)

    def test_hand_values_are_labelled(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        hand = {("core", "color", "slate", "200"), ("core", "color", "zinc", "500"), ("light", "helpBand"),
                ("core", "elevation", "popover"), ("core", "elevation", "dialog"),
                ("core", "space", "1"), ("core", "space", "3"), ("core", "space", "5"), ("core", "space", "16"),
                ("core", "layout", "page"), ("core", "layout", "phone"), ("core", "layout", "navHeight")}
        labelled = {p for p, t in leaves(tokens) if str(t.get("$extensions", {}).get("source", "")).startswith(HAND)}
        self.assertEqual(labelled, hand)


if __name__ == "__main__":
    unittest.main()
