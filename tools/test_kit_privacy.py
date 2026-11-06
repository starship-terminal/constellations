"""Tests for the capture kit's private-data guards (tools/kit/capture/). Run with `make test`.
The JavaScript halves run under node when it is on PATH and are skipped otherwise."""
import importlib.util
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
sys.path.insert(0, str(HERE))
import catalog  # noqa: E402

SIGNED_IN = HERE / "kit" / "capture" / "signed-in"
NODE = shutil.which("node")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


unsnap = load(SIGNED_IN / "unsnap.py", "kit_unsnap")

SIGNED = [
    "https://bucket.s3.amazonaws.com/a.png?X-Amz-Algorithm=AWS4&X-Amz-Signature=abc",
    "https://bucket.s3.amazonaws.com/a.png?x-amz-security-token=abc",
    "https://storage.googleapis.com/b/o.png?X-Goog-Signature=abc",
    "https://storage.googleapis.com/b/o.png?GoogleAccessId=x&X-Goog-Credential=abc",
    "https://d1.cloudfront.net/v.mp4?Expires=1&Policy=p&Signature=s&Key-Pair-Id=k",
    "https://acct.blob.core.windows.net/c/f.png?sv=2020&sig=abc",
    "https://cdn.example.test/f.png?a=1&amp;token=abc",
    "https://app.example.test/cb#access_token=abc&state=1",
    "https://app.example.test/cb?code=abc",
    "https://app.example.test/cb?id_token=abc",
    "https://proxy.example.test/?u=https%3A%2F%2Fx%2Fy.png%3Ftoken%3Dabc",
]
PLAIN = [
    "https://example.test/page?unit=7",
    "https://example.test/a?tokenizer=1&sigma=2&codec=h264",
    "https://example.test/docs#tokens",
    "color:#fff",
]


class SharedList(unittest.TestCase):
    def test_every_reader_flags_the_same_urls(self):
        for u in SIGNED:
            self.assertTrue(catalog.SIGNED_URL.search(u), u)
            self.assertTrue(unsnap.SIGNED.search(u), u)
        for u in PLAIN:
            self.assertFalse(catalog.SIGNED_URL.search(u), u)
            self.assertFalse(unsnap.SIGNED.search(u), u)

    def test_snapshot_js_carries_the_same_list(self):
        spec = json.loads((SIGNED_IN / "signed-params.json").read_text())
        m = re.search(r"^const SIGNED_PARAMS = (\{.*\});$", (SIGNED_IN / "snapshot.js").read_text(), re.M)
        self.assertIsNotNone(m, "snapshot.js lost its SIGNED_PARAMS line")
        self.assertEqual(json.loads(m.group(1)), {"prefixes": spec["prefixes"], "params": spec["params"]})

    def test_unsnap_refuses_a_copy_that_still_holds_one(self):
        with tempfile.TemporaryDirectory() as d:
            redact = Path(d) / "r.json"
            redact.write_text(json.dumps({"replace": [["Jane Doe", "gi", "A User"]]}))
            out = Path(d) / "out"
            for body, ok in [('<img src="https://x/a.png">', True),
                             ('<img data-src="https://x/a.png?X-Goog-Signature=1">', False),
                             ('<p>Jane Doe</p>', False)]:
                snap = Path(d) / "snap.txt"
                snap.write_text("SNAPSTART" + json.dumps({"label": "home", "url": "https://x/"}) + "SNAPMETA" + body + "SNAPEND")
                res = subprocess.run([sys.executable, str(SIGNED_IN / "unsnap.py"), str(snap), str(out)],
                                     capture_output=True, text=True, env={**os.environ, "SNAP_REDACT": str(redact)})
                self.assertEqual(res.returncode == 0, ok, res.stderr)
                self.assertEqual((out / "home.html").exists(), ok)
                if ok:
                    (out / "home.html").unlink()
                else:
                    self.assertIn("LEAK", res.stderr)
                    self.assertNotIn("Jane", res.stderr)

    def test_unsnap_reads_entities_nbsp_and_split_elements(self):
        redact = {"replace": [["unrelated", "gi", "x"], ["jane\\s+doe", "gi", "A User"], ["Jane Doe", "g", "A User"]]}
        for page in ["<p>Jane&nbsp;Doe</p>", "<p>J&#97;ne Doe</p>", "<p>Ja<b>ne</b> Doe</p>",
                     "<p>Jane</p><p>Doe</p>", '<img alt="Jane&#x20;Doe">', "<p>JANE\u00a0DOE</p>"]:
            self.assertIn("redaction pattern 2", unsnap.leaks_in(page, redact), page)
        self.assertEqual(unsnap.leaks_in("<p>Jane&nbsp;Doe</p>", redact), ["redaction pattern 2", "redaction pattern 3"])
        self.assertEqual(unsnap.leaks_in("<p>A User</p>", redact), [])
        self.assertEqual(unsnap.leaks_in('<a href="https://x/a?a=1&amp;sig=2">', redact), ["sig"])


def js_block(path, start, end):
    """The source lines from the first one starting with `start` through the first after it starting with `end`."""
    lines = Path(path).read_text().splitlines()
    i = next(n for n, l in enumerate(lines) if l.lstrip().startswith(start))
    j = next(n for n in range(i, len(lines)) if lines[n].lstrip().startswith(end))
    return "\n".join(lines[i:j + 1])


@unittest.skipIf(NODE is None, "node is not on PATH")
class JavaScriptHalves(unittest.TestCase):
    def node(self, src):
        res = subprocess.run([NODE, "-e", src], capture_output=True, text=True, timeout=30)
        self.assertEqual(res.returncode, 0, res.stderr)
        return json.loads(res.stdout)

    def test_snapshot_cuts_every_signed_query_and_keeps_plain_ones(self):
        src = js_block(SIGNED_IN / "snapshot.js", "const SIGNED_PARAMS", "const cutSigned")
        got = self.node(src + f"\nconsole.log(JSON.stringify({json.dumps(SIGNED + PLAIN)}.map((u) => [SIGNED.test(u), cutSigned(u)])))")
        for u, (flag, cut) in zip(SIGNED + PLAIN, got):
            self.assertEqual(flag, bool(catalog.SIGNED_URL.search(u)), u)   # the same regex as the python side
        for u, (_, cut) in zip(SIGNED[:-1], got):                          # the %-encoded one stays for unsnap to refuse
            self.assertFalse(catalog.SIGNED_URL.search(cut), cut)
            self.assertTrue(cut.startswith(u.split("?")[0].split("#")[0]), cut)
        for u, (_, cut) in zip(PLAIN, got[len(SIGNED):]):
            self.assertEqual(cut, u)
        cases = {
            'background:url("https://x/p.png?X-Amz-Signature=1") center; color:#fff':
                'background:url("https://x/p.png") center; color:#fff',
            'background:url(https://x/p.png?sig=1);color:red': 'background:url(https://x/p.png);color:red',
            '<img data-src="https://x/p?size=1,2&Signature=abc">': '<img data-src="https://x/p">',
            '<img data-src="https://x/p?crop=(0,0)&token=abc" alt="">': '<img data-src="https://x/p" alt="">',
            '<img srcset="https://x/a.png?sig=1 1x, https://x/b.png 2x">': '<img srcset="https://x/a.png 1x, https://x/b.png 2x">',
        }
        got = self.node(src + f"\nconsole.log(JSON.stringify({json.dumps(list(cases))}.map(cutSigned)))")
        self.assertEqual(got, list(cases.values()))

    def test_measured_styles_record_no_url(self):
        for path in (SIGNED_IN / "measure.mjs", HERE / "kit/capture/public/lib.mjs"):
            src = js_block(path, "const noUrl", "const noUrl")
            got = self.node(src + "\nconsole.log(JSON.stringify(["
                            "noUrl('url(\"https://x/p.png?X-Amz-Signature=1\"), linear-gradient(red, blue)'),"
                            "noUrl('url(\"data:image/svg+xml,abc\")'), noUrl('url(#clip)'), noUrl('auto'), noUrl(3),"
                            "noUrl('url(\"https://x/photo(1).png?token=abc\") no-repeat'),"
                            "noUrl(\"url('https://x/a\\\\'b(2).png?sig=1')\"), noUrl('url(https://x/p.png?sig=1), none')]))")
            self.assertEqual(got, ['url(…), linear-gradient(red, blue)', 'url("data:image/svg+xml,abc")', 'url(#clip)', 'auto', 3,
                                   'url(…) no-repeat', 'url(…)', 'url(…), none'], path)


if __name__ == "__main__":
    unittest.main()
