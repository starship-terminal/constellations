"""The Krisp builders reproduce the committed files.

Each builder runs in a scratch copy of the package, so nothing committed is rewritten, and its
output is compared with the committed file. Run from this folder, or via
tools/package_tests.py krisp.
"""
import json
import re
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


def forms(hex_value):
    h = hex_value.lower().lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return ["#" + h, f"rgb({r}, {g}, {b})", f"rgba({r}, {g}, {b},"]


class Rebuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.dst = Path(cls.tmp.name) / PKG.name
        shutil.copytree(PKG, cls.dst, ignore=shutil.ignore_patterns("*.png", "screenshots", "components"))
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

    def test_aliases_name_no_set(self):
        """{core.x} only resolves through catalog.py's set-prefix fallback; DTCG readers call it dangling."""
        for ref in re.findall(r"\{([^{}]+)\}", json.dumps(self.tokens)):
            self.assertNotIn(ref.split(".")[0], ("core", "light", "dark"), f"{{{ref}}} names a set")

    def test_colours_not_in_raw_are_reconstructions(self):
        """A colour that no raw file holds must carry the Reconstruction label (docs/EVIDENCE.md)."""
        raw = "".join(p.read_text().lower() for p in (PKG / "raw").glob("*.json"))
        for set_name in ("core", "light", "dark"):
            for path, leaf in leaves(self.tokens[set_name]):
                v = leaf["$value"]
                if leaf["$type"] != "color" or not re.fullmatch(r"#[0-9a-fA-F]{6}", str(v)):
                    continue
                if not any(f in raw for f in forms(v)):
                    self.assertTrue(leaf["$extensions"]["source"].startswith("Reconstruction"),
                                    f"{set_name}.{path} {v} is in no raw file but is not labelled Reconstruction")


if __name__ == "__main__":
    unittest.main()
