"""The Kitchen.co builders reproduce the committed files.

Each builder runs in a scratch copy of the package, so nothing committed is rewritten, and its
output is compared with the committed file. Run from this folder, or via
tools/package_tests.py kitchen.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
BUILDERS = ["build_tokens.py", "build_components_md.py", "build_style_guide.py"]
OUTPUTS = ["tokens.json", "components.md", "style-guide.html"]


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from leaves(v, f"{path}.{k}" if path else k)


def rgb(hex_value):
    h = hex_value.lstrip("#")
    return "rgb(%d, %d, %d)" % tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


class Rebuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.dst = Path(cls.tmp.name) / PKG.name
        # Images only need to exist (components.md links them), so they are copied empty.
        shutil.copytree(PKG, cls.dst, ignore=shutil.ignore_patterns("*.png"))
        for png in PKG.rglob("*.png"):
            (cls.dst / png.relative_to(PKG)).parent.mkdir(parents=True, exist_ok=True)
            (cls.dst / png.relative_to(PKG)).touch()
        for b in BUILDERS:
            res = subprocess.run([sys.executable, str(cls.dst / "tools" / b)], cwd=cls.dst,
                                 capture_output=True, text=True, timeout=120)
            if res.returncode:
                raise AssertionError(f"{b} failed:\n{res.stderr}")
        cls.tokens = json.loads((PKG / "tokens.json").read_text())

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for rel in OUTPUTS:
            with self.subTest(rel):
                self.assertEqual((self.dst / rel).read_text(), (PKG / rel).read_text(),
                                 f"{rel}: the builders no longer reproduce the committed file")

    def test_measured_colours_are_in_raw(self):
        """A colour labelled Measured must be a reading in raw/ (15-1: #ffdc4d, #e5e5e5 were not)."""
        raw = "".join(p.read_text().lower() for p in (PKG / "raw").glob("*.json"))
        for set_name in ("light",):
            for path, leaf in leaves(self.tokens[set_name]):
                v = leaf["$value"]
                if leaf["$type"] != "color" or not str(v).startswith("#"):
                    continue
                if leaf["$extensions"]["source"].startswith("Measured"):
                    self.assertTrue(v in raw or rgb(v) in raw, f"{set_name}.{path} {v} is labelled Measured but no raw file holds it")

    def test_themes_have_ids(self):
        self.assertTrue(all("id" in t for t in self.tokens["$themes"]))


if __name__ == "__main__":
    unittest.main()
