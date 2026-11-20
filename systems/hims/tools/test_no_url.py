"""Every noUrl() in the capture scripts must drop a URL's query, including an
unquoted url() with an escaped closing parenthesis (signed URLs never reach
raw/). Runs each definition in Node; skipped without Node.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import re
import shutil
import subprocess
import unittest

CAPTURE = pathlib.Path(__file__).resolve().parent / "capture"
CASES = {
    "url(https://cdn.test/a\\)b.png?sig=SECRET) no-repeat": "url(…) no-repeat",
    'url("https://cdn.test/a.png?sig=SECRET")': "url(…)",
    "url(data:image/png;base64,AA)": "url(data:image/png;base64,AA)",
}


def definitions():
    for f in sorted(CAPTURE.rglob("*.mjs")):
        src = f.read_text()
        for m in re.finditer(r"const noUrl = \(v\) => \(typeof v === 'string'\s*\?\s*(v\.replace\(.*?'url\(…\)'\))\s*:\s*v\);", src, re.S):
            yield f"{f.relative_to(CAPTURE)}:{src[:m.start()].count(chr(10)) + 1}", m.group(1)


@unittest.skipUnless(shutil.which("node"), "node not installed")
class NoUrlTest(unittest.TestCase):
    def test_every_definition_drops_signed_queries(self):
        defs = list(definitions())
        self.assertGreaterEqual(len(defs), 5)
        for where, expr in defs:
            js = f"const f = (v) => {expr}; const c = {json.dumps(list(CASES))}; console.log(JSON.stringify(c.map(f)));"
            out = json.loads(subprocess.run(["node", "-e", js], capture_output=True, text=True, check=True).stdout)
            self.assertEqual(out, list(CASES.values()), where)


if __name__ == "__main__":
    unittest.main()
