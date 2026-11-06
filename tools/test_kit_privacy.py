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

    def test_unsnap_finds_an_accented_name_in_the_metadata(self):
        with tempfile.TemporaryDirectory() as d:
            redact = Path(d) / "r.json"
            redact.write_text(json.dumps({"replace": [["José Núñez", "gi", "A User"]]}))
            snap = Path(d) / "snap.txt"
            snap.write_text("SNAPSTART" + json.dumps({"label": "home", "url": "https://x/", "who": "José Núñez"})
                            + "SNAPMETA<p>ok</p>SNAPEND")
            res = subprocess.run([sys.executable, str(SIGNED_IN / "unsnap.py"), str(snap), str(Path(d) / "out")],
                                 capture_output=True, text=True, env={**os.environ, "SNAP_REDACT": str(redact)})
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("LEAK", res.stderr)

    def test_unsnap_reads_entities_nbsp_and_split_elements(self):
        redact = {"replace": [["unrelated", "gi", "x"], ["jane\\s+doe", "gi", "A User"], ["Jane Doe", "g", "A User"]]}
        for page in ["<p>Jane&nbsp;Doe</p>", "<p>J&#97;ne Doe</p>", "<p>Ja<b>ne</b> Doe</p>",
                     "<p>Jane</p><p>Doe</p>", '<img alt="Jane&#x20;Doe">', "<p>JANE\u00a0DOE</p>",
                     '<p>Jane <span title="x>y">Doe</span></p>', "<p>Ja<!-- c -->ne Doe</p>"]:
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

    def test_recorded_page_urls_keep_only_origin_and_route_words(self):
        cases = {
            "https://claude.ai/chat/1f2e3d4c-aaaa-bbbb?q=secret#m": "https://claude.ai/chat/<id>",
            "https://app.example.test/project/My-Secret-Plan": "https://app.example.test/project/<id>",
            "https://app.example.test/team/eng/issue/ENG-123/fix-the-login-for-acme": "https://app.example.test/team/<id>/issue/<id>/<id>",
            "https://app.example.test/new-chat": "https://app.example.test/new-chat",
            "https://app.example.test/": "https://app.example.test/",
            "https://x.test/cb?code=abc#access_token=def": "https://x.test/cb",
            "file:///Users/someone/raw/home.html": "file:///<local file>",
            "not a url": "<url>",
            "https://app.example.test/project/my-plan": "https://app.example.test/project/<id>",
            "https://app.example.test/u/someone/settings": "https://app.example.test/u/<id>/settings",
            "https://claude.ai/chat/<id>": "https://claude.ai/chat/<id>",            # a second pass changes nothing
        }
        mod = (HERE / "kit/capture/safe-url.mjs").as_uri()
        got = self.node(f"import({json.dumps(mod)}).then(({{ safeUrl }}) => "
                        f"console.log(JSON.stringify({json.dumps(list(cases))}.map(safeUrl))))")
        self.assertEqual(got, list(cases.values()))
        for rel in ("signed-in/measure.mjs", "layout.mjs", "electron/shot.mjs", "public/measure.mjs"):
            src = (HERE / "kit/capture" / rel).read_text()
            self.assertIn("safe-url.mjs", src, rel)                  # each writer of a raw/ URL uses it
            self.assertIn("safeUrl(", src, rel)
        # a partial rerun cleans what it keeps from the last run too
        self.assertIn("url: v.url && safeUrl(v.url)", (HERE / "kit/capture/signed-in/measure.mjs").read_text())
        self.assertIn("out._meta.storyUrl = safeUrl(out._meta.storyUrl)", (HERE / "kit/capture/public/measure.mjs").read_text())


PLAYWRIGHT = os.environ.get("PLAYWRIGHT") or str(Path.home() / ".design-systems/pw/node_modules/playwright/index.mjs")


@unittest.skipIf(NODE is None or not Path(PLAYWRIGHT).is_file(), "node or the capture Playwright is not installed")
class SnapshotInABrowser(unittest.TestCase):
    """Runs snapshot.js's __snap on a small page in headless Chromium (the capture's own Playwright,
    $PLAYWRIGHT or ~/.design-systems/pw), and checks the copy it returns."""

    def snap(self, page, setup="", redact=None):
        redact = redact or {"replace": [["nothing-matches-this", "g", "x"]]}
        script = f"""
const pw = await import({json.dumps(Path(PLAYWRIGHT).as_uri())});
const b = await pw.chromium.launch();
const p = await b.newPage();
await p.setContent({json.dumps(page)});
await p.evaluate(() => {{ {setup} }});
await p.addScriptTag({{ content: {json.dumps((SIGNED_IN / "snapshot.js").read_text())} }});
const out = await p.evaluate((r) => window.__snap('t', r), {json.dumps(redact)});
await b.close();
console.log(JSON.stringify(out));
"""
        res = subprocess.run([NODE, "--input-type=module", "-e", script], capture_output=True, text=True, timeout=120)
        self.assertEqual(res.returncode, 0, res.stderr[-2000:])
        return json.loads(res.stdout).split("SNAPMETA", 1)[1]

    def test_credential_fields_never_reach_the_copy(self):
        # Each field trips exactly one rule: neutral ids, so the autocomplete rule is tested on its own.
        page = ('<input type="password" id="f1"><input type="hidden" name="f2" value="HIDDENTOKEN1">'
                '<input id="f3" autocomplete="one-time-code"><input id="f4" autocomplete="cc-number">'
                '<input type="text" id="f5" autocomplete="current-password"><input name="api_key" id="f6">'
                '<input id="q" value="">')
        setup = ("document.getElementById('f1').value = 'PASSWORDVALUE1';"
                 "document.getElementById('f3').value = '123987';"
                 "document.getElementById('f4').value = '4111222233334444';"
                 "document.getElementById('f5').value = 'SHOWNPASSWORD1';"
                 "document.getElementById('f6').value = 'APIKEYVALUE1';"
                 "document.getElementById('q').value = 'plain search';")
        body = self.snap(page, setup)
        for secret in ("PASSWORDVALUE1", "HIDDENTOKEN1", "123987", "4111222233334444", "SHOWNPASSWORD1", "APIKEYVALUE1"):
            self.assertNotIn(secret, body)
        self.assertIn('value="xxxxxxxx"', body)          # the password field still renders filled
        self.assertIn('value="plain search"', body)       # ordinary fields keep what was typed

    def test_redaction_reaches_text_nodes_comments_and_attributes(self):
        page = ('<p>J&#97;ne&nbsp;Doe and Jane Doe</p><!-- Jane Doe --><img alt="Jane Doe" src="data:,">'
                '<a title="by Jane  Doe" href="#x">x</a><p>JANE\u00a0DOE</p>')
        redact = {"replace": [["jane\\s+doe", "i", "A User"]]}   # no g: every match must still go
        script = f"""
const pw = await import({json.dumps(Path(PLAYWRIGHT).as_uri())});
const b = await pw.chromium.launch();
const p = await b.newPage();
await p.setContent({json.dumps(page)});
await p.addScriptTag({{ content: {json.dumps((SIGNED_IN / "snapshot.js").read_text())} }});
const out = await p.evaluate((r) => window.__snap('t', r), {json.dumps(redact)});
await b.close();
console.log(JSON.stringify(out));
"""
        res = subprocess.run([NODE, "--input-type=module", "-e", script], capture_output=True, text=True, timeout=120)
        self.assertEqual(res.returncode, 0, res.stderr[-2000:])
        out = json.loads(res.stdout)
        body = out.split("SNAPMETA", 1)[1]
        self.assertEqual(unsnap.leaks_in(body, redact), [], body)
        self.assertGreaterEqual(body.count("A User"), 6, body)



@unittest.skipIf(NODE is None or not Path(PLAYWRIGHT).is_file(), "node or the capture Playwright is not installed")
class RawShotsStayOutOfTheRepo(unittest.TestCase):
    def test_public_capture_needs_a_scratch_dir_outside_a_package(self):
        env = {k: v for k, v in os.environ.items() if k != "RAW"}
        res = subprocess.run([NODE, str(HERE / "kit/capture/public/public.mjs")], capture_output=True, text=True,
                             timeout=60, env={**env, "PLAYWRIGHT": PLAYWRIGHT})
        self.assertEqual(res.returncode, 2, res.stderr)
        self.assertIn("set RAW=", res.stderr)
        src = (HERE / "kit/capture/public/public.mjs").read_text()
        self.assertIn("'.design-systems', path.basename(PKG), 'raw-shots'", src)
        self.assertNotIn("raw/full/", src)


if __name__ == "__main__":
    unittest.main()
