"""Tests for the kit's style guide builder (tools/kit/build/build_style_guide.py) and its template:
the guide works offline and no token value can end its <style> early. Run with `make test`."""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILD = HERE / "kit" / "build"


def tok(v, ty="color"):
    return {"$type": ty, "$value": v, "$extensions": {"source": "test"}}


class StyleGuide(unittest.TestCase):
    def render(self, tokens, template="<!doctype html>\n<style>\n:root {\n/*CORE*/\n}\n</style>\n"):
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            (pkg / "tools").mkdir()
            shutil.copy(BUILD / "build_style_guide.py", pkg / "tools/build_style_guide.py")
            (pkg / "tools/style-guide.template.html").write_text(template)
            (pkg / "tokens.json").write_text(json.dumps(tokens))
            res = subprocess.run([sys.executable, str(pkg / "tools/build_style_guide.py")], capture_output=True, text=True,
                                 timeout=60, env={**os.environ, "KIT_EXAMPLE": "1"})
            self.assertEqual(res.returncode, 0, res.stderr[-1000:])
            return (pkg / "style-guide.html").read_text()

    def test_a_value_holding_a_closing_style_tag_cannot_end_the_stylesheet(self):
        html = self.render({"core": {"bg": {"img": tok('url("data:image/svg+xml,<svg></svg></STYLE><script>alert(1)</script>")', "string")}}})
        self.assertEqual(len(re.findall(r"</style", html, re.I)), 1, html)
        self.assertIn("<\\/STYLE><script>", html)
        self.assertIn("<svg></svg>", html)   # an svg data URI is written as it is

    def test_the_kit_template_fetches_nothing(self):
        tpl = (BUILD / "style-guide.template.html").read_text()
        self.assertEqual(re.findall(r"""(?:href|src)=["']https?://""", tpl), [])
        self.assertNotIn("@import", tpl)


if __name__ == "__main__":
    unittest.main()
