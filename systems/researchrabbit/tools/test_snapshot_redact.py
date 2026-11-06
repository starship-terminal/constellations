"""capture/snapshot.js's __snap, run on a small page in headless Chromium: every REDACT match goes from text nodes,
comments, attributes and entity-split text, and signed query strings go from any attribute or inline
style. Skipped without node and the capture's Playwright ($PLAYWRIGHT or ~/.design-systems/pw)."""
import json
import os
import pathlib
import shutil
import subprocess
import unittest

HERE = pathlib.Path(__file__).resolve().parent
NODE = shutil.which("node")
PLAYWRIGHT = os.environ.get("PLAYWRIGHT") or str(pathlib.Path.home() / ".design-systems/pw/node_modules/playwright/index.mjs")
PAGE = ('<p>J&#97;ne&nbsp;Doe and Jane Doe</p><!-- Jane Doe --><img alt="Jane Doe" src="data:,">'
        '<a title="by Jane  Doe" href="#x">x</a><p>JANE DOE</p>'
        '<div data-src="https://cdn.example/a.png?X-Amz-Signature=abc123" style="background:url(https://cdn.example/b.png?sig=zzz9)"></div>'
        '<i id="c" style="color:#fff;background:url(https://cdn.example/c.png?sig=yyy8)"></i>')
REDACT = {"replace": [["jane\\s+doe", "i", "A User"]]}   # no g flag: every match must still go


@unittest.skipIf(NODE is None or not pathlib.Path(PLAYWRIGHT).is_file(), "node or the capture Playwright is not installed")
class SnapRedactTest(unittest.TestCase):
    def test_every_match_and_signed_query_is_gone(self):
        script = f"""
const pw = await import({json.dumps(pathlib.Path(PLAYWRIGHT).as_uri())});
const b = await pw.chromium.launch();
const p = await b.newPage();
await p.route('**/*', (r) => r.abort());
await p.setContent({json.dumps(PAGE)});
await p.addScriptTag({{ content: {json.dumps((HERE / "capture/snapshot.js").read_text())} }});
const out = await p.evaluate((r) => window.__snap('t', r), {json.dumps(REDACT)});
await b.close();
console.log(JSON.stringify(out));
"""
        res = subprocess.run([NODE, "--input-type=module", "-e", script], capture_output=True, text=True, timeout=120)
        self.assertEqual(res.returncode, 0, res.stderr[-2000:])
        body = json.loads(res.stdout).split("SNAPMETA", 1)[1]
        self.assertNotRegex(body, "(?i)jane")
        self.assertGreaterEqual(body.count("A User"), 6, body)
        self.assertNotIn("X-Amz-Signature", body)
        self.assertNotIn("sig=zzz9", body)
        self.assertNotIn("sig=yyy8", body)
        self.assertIn("color:#fff;background:url(https://cdn.example/c.png)", body)   # CSS before a signed URL stays


if __name__ == "__main__":
    unittest.main()
