"""tokens.json, style-guide.html and components.md must rebuild from the committed raw readings,
and the type and radius tokens that cite a measured component must carry that reading.

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
BUILT = ("tokens.json", "style-guide.html", "components.md")
BUILDERS = ("build_tokens.py", "build_style_guide.py", "build_components_md.py")
TOKENS = json.loads((PKG / "tokens.json").read_text())
COMP = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]


def style(comp):
    return COMP[comp]["states"]["default"]["style"]


class RebuildTest(unittest.TestCase):
    def test_builders_reproduce_committed_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__"))
            for builder in BUILDERS:
                subprocess.run([sys.executable, str(copy / "tools" / builder)], check=True, capture_output=True)
            for name in BUILT:
                self.assertEqual((copy / name).read_text(), (PKG / name).read_text(), name)

    def test_measured_type_carries_its_reading(self):
        checked = 0
        for name, tok in TOKENS["core"]["typography"].items():
            m = re.match(r"Measured computed style on ([\w-]+)\.default", tok["$extensions"]["source"])
            if not m:
                continue
            s = style(m.group(1))
            for key in ("fontSize", "lineHeight", "fontWeight"):
                self.assertEqual(tok["$value"][key], s[key], f"{name}.{key}")
            checked += 1
        self.assertEqual(checked, 3)
        self.assertEqual(TOKENS["core"]["typography"]["book-title"]["$value"]["lineHeight"], "41.6px")

    def test_measured_radius_carries_its_reading(self):
        for name, tok in TOKENS["core"]["radius"].items():
            m = re.match(r"Measured computed borderTopLeftRadius on ([\w-]+)\.default", tok["$extensions"]["source"])
            self.assertTrue(m, name)
            self.assertEqual(tok["$value"], style(m.group(1))["borderTopLeftRadius"], name)

    def test_hand_body_type_is_labelled(self):
        src = TOKENS["core"]["typography"]["body"]["$extensions"]["source"]
        self.assertTrue(src.startswith("Reconstruction: entered by hand at capture time"), src)

    def test_dark_rows_are_labelled_from_the_dark_set(self):
        md = (PKG / "components.md").read_text()
        rows = [l for l in md.splitlines() if l.startswith("- [") and "-dark-" in l.split("]")[0]]
        self.assertTrue(rows)
        for row in rows:
            self.assertNotIn("`light.", row, row)


    def test_capture_date_moves_only_on_a_reading(self):
        src = (PKG / "tools" / "capture" / "public" / "measure.mjs").read_text()
        self.assertIn("read: PRIOR_READ || RUN,\n  lastAttempt: RUN,", src)
        self.assertNotIn("run: RUN, theme", src)
        self.assertIn("via, run: RUN };\n      c.run = RUN;\n      out._meta.read = RUN;", src)


if __name__ == "__main__":
    unittest.main()
