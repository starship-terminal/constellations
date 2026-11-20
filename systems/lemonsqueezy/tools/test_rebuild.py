"""tokens.json, components.md and style-guide.html must rebuild from the committed raw readings,
and every token that cites a computed reading must carry that reading.

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
BUILT = ("tokens.json", "components.md", "style-guide.html")
CITE = re.compile(r"^computed (\w+) on ([\w-]+)/([\w-]+) ")


def leaves(node, path=()):
    if isinstance(node, dict):
        if "$value" in node:
            yield path, node
            return
        for k, v in node.items():
            if not k.startswith("$"):
                yield from leaves(v, path + (k,))


class RebuildTest(unittest.TestCase):
    def test_builders_reproduce_committed_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__", "screenshots", "components"))
            for builder in ("build_tokens.py", "build_components_md.py", "build_style_guide.py"):
                subprocess.run([sys.executable, str(copy / "tools" / builder)], check=True, capture_output=True)
            for name in BUILT:
                self.assertEqual((copy / name).read_text(), (PKG / name).read_text(), name)

    def test_cited_dimensions_match_the_reading(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        comps = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        checked = 0
        for path, tok in leaves(tokens):
            m = CITE.match(str(tok.get("$extensions", {}).get("source", "")))
            if not m or tok["$type"] != "dimension":
                continue
            prop, comp, state = m.groups()
            self.assertEqual(tok["$value"], comps[comp]["states"][state]["style"][prop], ".".join(path))
            checked += 1
        self.assertGreater(checked, 20)

    def test_hand_values_are_labelled(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        for name in ("display", "title", "body", "label", "code"):
            src = tokens["core"]["typography"][name]["$extensions"]["source"]
            self.assertTrue(src.startswith("Reconstruction: entered by hand"), name)


if __name__ == "__main__":
    unittest.main()
