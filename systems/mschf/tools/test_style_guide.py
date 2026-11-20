"""tokens.json and style-guide.html are what the builders write, and the guide defines every
custom property its template uses."""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class Guide(unittest.TestCase):
    def test_tokens_match_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_guide_matches_builder(self):
        with tempfile.TemporaryDirectory() as tmp:
            pkg = pathlib.Path(tmp) / "pkg"
            shutil.copytree(ROOT, pkg, ignore=shutil.ignore_patterns("screenshots", "components", "boards", "raw"))
            subprocess.run([sys.executable, str(pkg / "tools" / "build_style_guide.py")], check=True, capture_output=True)
            self.assertEqual((pkg / "style-guide.html").read_text(), (ROOT / "style-guide.html").read_text())

    def test_every_var_the_page_uses_is_defined(self):
        # The dark set (the only painted theme) never reached the page: the template had no
        # /*LIGHT*/ slot, where a dark-only package's set is written, and used --color-ink-hover.
        html = (ROOT / "style-guide.html").read_text()
        used = set(re.findall(r"var\((--[A-Za-z0-9-]+)\)", html))
        defined = set(re.findall(r"^\s*(--[A-Za-z0-9-]+):", html, re.M))
        self.assertEqual(sorted(used - defined), [])

    def test_muted_text_is_not_the_border_rule(self):
        import json
        dark = json.loads(build_tokens.TEXT)["dark"]
        self.assertEqual(dark["text"]["muted"]["$value"], "{color.ink}")
        self.assertEqual(dark["border"]["subtle"]["$value"], "{color.rule}")


if __name__ == "__main__":
    unittest.main()
