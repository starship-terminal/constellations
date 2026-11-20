"""The style guide's script must fill its tables from the token tree the builder inlines.

build_style_guide.py inlines a slim tree ({v, t, s} per token). A script that reads DTCG $value
and $type instead matches nothing and leaves Palette, Spacing, Type and Family empty, which no
HTML comparison catches. This test runs the page's own script in Node against a minimal DOM stub
and counts the rows it writes. Skipped when Node is not installed.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import re
import shutil
import subprocess
import unittest

PAGE = pathlib.Path(__file__).resolve().parent.parent / "style-guide.html"

HARNESS = """
const out = {};
const el = (id) => (out[id] ??= { id, innerHTML: '' });
globalThis.document = {
  getElementById: el,
  documentElement: { style: { setProperty() {} } },
};
globalThis.getComputedStyle = () => ({ getPropertyValue: () => '' });
%s
const rows = (id) => ((out[id] || {}).innerHTML.match(/<div/g) || []).length;
console.log(JSON.stringify({ roles: rows('roles-out'), spacing: rows('spacing-out'), type: rows('type-out'), fam: rows('fam-out') }));
"""


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class StyleGuideScriptTest(unittest.TestCase):
    def test_tables_are_filled(self):
        html = PAGE.read_text()
        script = re.findall(r"<script>([\s\S]*?)</script>", html)[-1]
        run = subprocess.run(["node", "-e", HARNESS % script], capture_output=True, text=True)
        errors = [l for l in run.stderr.splitlines() if "Error" in l]
        self.assertEqual(run.returncode, 0, "the page script threw: " + (errors[0] if errors else run.stderr[-300:]))
        counts = json.loads(run.stdout.strip().splitlines()[-1])
        for table, n in counts.items():
            self.assertGreater(n, 0, f"{table} table is empty: {counts}")


if __name__ == "__main__":
    unittest.main()
