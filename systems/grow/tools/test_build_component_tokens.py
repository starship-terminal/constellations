"""build_component_tokens.py reads every value from raw/components-computed.json.

Each test copies the package's raw/ and tools/ into a temporary folder and runs
the builder there, so the committed files are never rewritten.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent


def build(edit=None):
    with tempfile.TemporaryDirectory() as d:
        root = Path(d) / "grow"
        shutil.copytree(PKG / "raw", root / "raw")
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        if edit:
            p = root / "raw" / "components-computed.json"
            j = json.loads(p.read_text())
            edit(j["components"])
            p.write_text(json.dumps(j))
        res = subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], capture_output=True, text=True)
        out = (root / "raw" / "component-tokens.json").read_text() if res.returncode == 0 else None
        return res, out


class ReadsFromRaw(unittest.TestCase):
    def test_rebuild_matches_the_committed_spec(self):
        res, out = build()
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(out, (PKG / "raw" / "component-tokens.json").read_text())

    def test_banner_values_are_the_readings(self):
        spec = json.loads((PKG / "raw" / "component-tokens.json").read_text())
        self.assertEqual(spec["light"]["banner"]["bg"]["value"], "rgba(0, 0, 0, 0)")
        self.assertEqual(spec["light"]["banner"]["link"]["value"], "#ffffff")
        self.assertEqual(spec["core"]["space"]["page"]["x"]["value"], "72px")

    def test_a_missing_reading_fails_instead_of_falling_back(self):
        def drop(c):
            del c["cert-cta"]["states"]["default"]["style"]["paddingLeft"]
        res, _ = build(drop)
        self.assertNotEqual(res.returncode, 0)
        self.assertIn("paddingLeft of cert-cta default", res.stderr)

    def test_a_changed_reading_changes_the_token(self):
        def recolour(c):
            c["footer"]["states"]["default"]["style"]["backgroundColor"] = "rgb(1, 2, 3)"
        res, out = build(recolour)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(json.loads(out)["light"]["color"]["surface"]["footer"]["value"], "#010203")


if __name__ == "__main__":
    unittest.main()
