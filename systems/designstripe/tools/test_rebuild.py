"""Rebuild checks for the Designstripe builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots/, components/ and icons/ are
linked read-only), so nothing committed is rewritten.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ("build_component_tokens.py", "build_tokens.py", "build_style_guide.py", "build_components_md.py")
OUTPUTS = ("tokens.json", "raw/component-tokens.json", "style-guide.html", "components.md")


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for d in ("screenshots", "components", "icons"):
            if (PKG / d).exists():
                (root / d).symlink_to(PKG / d)
        for b in BUILDERS:
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        for f in OUTPUTS:
            self.assertEqual((PKG / f).read_text(), (self.root / f).read_text(), f)

    def test_page_field_reads_the_declaration(self):
        src = self.built["light"]["background"]["page"]["$extensions"]["source"]
        self.assertTrue(src.startswith("declared --background"), src)

    def test_kept_and_wrong_readings_are_flagged(self):
        self.assertTrue(self.C["hero-h1"]["states"]["default"].get("rerunError"))
        self.assertIn("kept reading", self.built["light"]["text"]["black"]["$extensions"]["source"])
        self.assertIn("kept reading", self.built["core"]["motion"]["control"]["$extensions"]["source"])
        body = self.built["core"]["font"]["size"]["measured"]["body"]["$extensions"]["source"]
        self.assertIn("read from the wrong element; recapture needed", body)

    def test_flags_follow_the_readings(self):
        """On a temp copy: a recaptured post-para (a real paragraph) clears its flag, and a kept
        reading whose date measure.mjs recorded is reported with that date."""
        root = pathlib.Path(self.tmp.name) / "recaptured"
        shutil.copytree(self.root / "tools", root / "tools")
        shutil.copytree(self.root / "raw", root / "raw")
        path = root / "raw" / "components-computed.json"
        J = json.loads(path.read_text())
        J["components"]["post-para"]["states"]["default"]["text"] = "A body paragraph " * 8
        J["components"]["hero-h1"]["states"]["default"].update({"read": "2026-11-10", "rerunOn": "2026-11-14"})
        path.write_text(json.dumps(J))
        subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, check=True, capture_output=True)
        spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        self.assertNotIn("wrong element", spec["core"]["font"]["size"]["measured"]["body"]["source"])
        black = spec["light"]["text"]["black"]["source"]
        self.assertIn("the 2026-11-14 re-read failed (rerunError) and the earlier reading was kept, read 2026-11-10", black)

    def test_builder_has_no_pasted_twice_loop_body(self):
        src = (PKG / "tools" / "build_component_tokens.py").read_text()
        self.assertEqual(src.count('raw = st(comp, state)["fontSize"]'), 1)
        self.assertEqual(src.count("v = rc(cname, state, prop)"), 1)


if __name__ == "__main__":
    unittest.main()
