"""components.md must rebuild from the committed raw readings.

The builder runs on a temporary copy of the package, so the committed files are never rewritten.
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


class BuildComponentsMdTest(unittest.TestCase):
    def test_components_md_matches_raw(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__"))
            # Remove the committed output from the copy first, so a builder that
            # writes nothing cannot pass by leaving the committed file in place.
            (copy / "components.md").unlink()
            subprocess.run([sys.executable, str(copy / "tools" / "build_components_md.py")],
                           check=True, capture_output=True)
            self.assertTrue((copy / "components.md").exists(), "components.md was not rebuilt")
            built = (copy / "components.md").read_text()
        self.assertEqual(built, (PKG / "components.md").read_text())

    def test_header_count_matches_raw(self):
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        states = sum(len(c.get("states", {})) for c in raw.values())
        m = re.search(r"\((\d+) components, (\d+) states\)", (PKG / "components.md").read_text())
        self.assertEqual((int(m.group(1)), int(m.group(2))), (len(raw), states))


if __name__ == "__main__":
    unittest.main()
