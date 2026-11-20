"""The archived-page sanitiser must drop every event handler and script URL,
including the spellings a text pattern misses. Runs in Node; skipped
without it.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import shutil
import subprocess
import unittest

MOD = pathlib.Path(__file__).resolve().parent / "capture" / "public" / "sanitize.mjs"
CASES = [
    '<a href="javascript: alert(1)">',
    "<a href='JaVaScRiPt&#58;alert(1)'>",
    '<a href="java&#x09;script:alert(1)">',
    "<svg/onload=alert(1)>",
    '<img src=x onerror="alert(1)">',
    '<iframe srcdoc="<script>alert(1)</script>">',
    '<form action=" vbscript:x">',
]


@unittest.skipUnless(shutil.which("node"), "node not installed")
class SanitizeTest(unittest.TestCase):
    def run_node(self, tags):
        js = (f"import({json.dumps(MOD.as_uri())}).then((m) => "
              f"console.log(JSON.stringify({json.dumps(tags)}.map(m.cleanTag))))")
        out = subprocess.run(["node", "--input-type=module", "-e", js], capture_output=True, text=True, check=True)
        return json.loads(out.stdout)

    def test_no_handler_or_script_url_survives(self):
        for before, after in zip(CASES, self.run_node(CASES)):
            low = after.lower()
            self.assertNotIn("onload", low, before)
            self.assertNotIn("onerror", low, before)
            self.assertNotIn("script:", low.replace("&#58;", ":").replace("&#x09;", ""), before)
            self.assertNotIn("alert", low, before)

    def test_ordinary_tags_keep_their_attributes(self):
        tags = ['<a href="/css/site.css" class="x">', '<img src="/image/a.png" alt="A b">', "<br/>"]
        self.assertEqual(self.run_node(tags), ['<a href="/css/site.css" class="x">', '<img src="/image/a.png" alt="A b">', "<br />"])


    def test_unquoted_slash_values_keep_their_slash(self):
        tags = ["<img src=/image/>", "<a href=/>", "<img src=x />", '<img src="x"/>', "<br/>"]
        self.assertEqual(self.run_node(tags), ["<img src=/image/>", "<a href=/>", "<img src=x />", '<img src="x" />', "<br />"])

    def test_invalid_numeric_reference_does_not_throw(self):
        self.assertEqual(self.run_node(['<a href="&#x110000;">', '<a href="&#xD800;javascript:x">']),
                         ['<a href="&#x110000;">', '<a href="&#xD800;javascript:x">'])

if __name__ == "__main__":
    unittest.main()
