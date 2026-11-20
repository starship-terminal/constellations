"""The signed-in snapshot copies inside packages (systems/<slug>/tools/capture/) keep the kit's
private-data guards: one signed-URL parameter list, an unsnap.py that checks the copy and its
metadata and needs $SNAP_REDACT, and a snapshot.js that carries the kit's credential-field rule.
Each package is self-contained, so each carries its own copy; this keeps them in step."""
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

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "tools" / "kit" / "capture"
# Every copy of the kit's snapshot inside a package: label (the folder's path under systems/,
# which starts with the slug) -> the folder holding snapshot.js. Found on disk, not listed and
# not counted, whatever the layout (tools/capture/, capture/, a vendored tools/kit/): a package
# that copies the kit is checked from its first commit, and one that drops an unused copy
# simply leaves the set. No filter on the siblings: a copy that lost unsnap.py or
# signed-params.json must fail, not drop out.
PACKAGES = {p.parent.relative_to(ROOT / "systems").as_posix(): p.parent
            for p in sorted((ROOT / "systems").glob("*/**/snapshot.js"))}
SIBLINGS = ("unsnap.py", "signed-params.json")
# Packages whose capture really ran signed in through their copy (the README says so, and
# raw/ or screenshots/ hold the signed-in pages). Their copies must stay; any other copy may
# be removed with the package's unused kit files.
SIGNED_IN = ("claude", "coursera", "manus", "chatgpt", "notebooklm", "duolingo", "linear",
             "brilliant", "researchrabbit", "sentry")
SIGNED = [
    "https://bucket.s3.amazonaws.com/a.png?X-Amz-Algorithm=AWS4&X-Amz-Signature=abc",
    "https://storage.googleapis.com/b/o.png?X-Goog-Signature=abc",
    "https://d1.cloudfront.net/v.mp4?Expires=1&Policy=p&Signature=s&Key-Pair-Id=k",
    "https://acct.blob.core.windows.net/c/f.png?sv=2020&sig=abc",
    "https://cdn.example.test/f.png?a=1&amp;token=abc",
    "https://app.example.test/cb#access_token=abc&state=1",
    "https://app.example.test/x?auth=abc",
]
PLAIN = ["https://example.test/page?unit=7", "https://example.test/a?tokenizer=1&sigma=2"]
# A stand-in clone for the whole-copy pass: a signed URL in a data- attribute and an inline
# style, plain attributes that must stay, and an inlined stylesheet the page pass must clean.
WHOLE_COPY_NODES = [["img", {"data-src": "https://x/p.png?crop=(0,0)&token=abc", "alt": "a;b",
                             # cutSigned stops at ;name: so it would keep this token; only
                             # cutSignedUrl, the attribute cleaner, removes it.
                             "data-srcset": "https://x/p?options=a;b:c&token=abc"}],
                    ["div", {"style": "color:#fff;background:url(https://x/i.png?sig=1)",
                             "data-unit": "https://example.test/page?unit=7"}]]
WHOLE_COPY_STYLE = ".x{background:url(https://x/bg.png?X-Amz-Signature=abc)}"
WHOLE_COPY_WANT = {
    "attrs": [{"data-src": "https://x/p.png", "alt": "a;b", "data-srcset": "https://x/p"},
              {"style": "color:#fff;background:url(https://x/i.png)",
               "data-unit": "https://example.test/page?unit=7"}],
    "html": '<!doctype html>\n<img data-src="https://x/p.png" alt="a;b" data-srcset="https://x/p">'
            '<div style="color:#fff;background:url(https://x/i.png)" data-unit="https://example.test/page?unit=7">'
            '<style>.x{background:url(https://x/bg.png)}</style>',
}


def folder(label):
    return PACKAGES[label]


def slug_of(label):
    return label.split("/")[0]


def capture_root(label):
    """The capture/ folder a copy sits in (its measure scripts live there too)."""
    d = folder(label)
    return next((a for a in (d, *d.parents) if a.name == "capture"), d)


def distinct(name):
    """One slug per distinct copy of `name` across PACKAGES. Most copies are byte-identical,
    so the tests that run a copy (node, a subprocess) run each distinct one once; the
    cheap text checks still read every package."""
    seen = {}
    for slug in PACKAGES:
        seen.setdefault((folder(slug) / name).read_bytes(), slug)
    return list(seen.values())


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class PackageSnapshots(unittest.TestCase):
    kit = json.loads((KIT / "signed-in" / "signed-params.json").read_text())

    def test_every_package_copy_is_found(self):
        # Discovery matches the disk: every snapshot.js under systems/ is in PACKAGES.
        on_disk = {p.parent for p in (ROOT / "systems").rglob("snapshot.js")}
        self.assertEqual(on_disk, set(PACKAGES.values()))
        slugs = {slug_of(label) for label in PACKAGES}
        self.assertEqual([s for s in SIGNED_IN if s not in slugs], [],
                         "a signed-in capture lost its snapshot copy")
        missing = [f"{label}/{name}" for label in PACKAGES for name in SIBLINGS
                   if not (folder(label) / name).is_file()]
        self.assertEqual(missing, [], "a snapshot.js copy without the kit files beside it")

    def test_each_copy_carries_the_kit_list(self):
        want = {"prefixes": self.kit["prefixes"], "params": self.kit["params"]}
        for slug in PACKAGES:
            d = folder(slug)
            spec = json.loads((d / "signed-params.json").read_text())
            self.assertEqual({"prefixes": spec["prefixes"], "params": spec["params"]}, want, slug)
            m = re.search(r"^\s*const SIGNED_PARAMS = (\{.*\});$", (d / "snapshot.js").read_text(), re.M)
            self.assertIsNotNone(m, f"{slug} snapshot.js has no SIGNED_PARAMS line")
            self.assertEqual(json.loads(m.group(1)), want, slug)

    def input_rule(self, src, label):
        """The credential-field rule of a snapshot.js: SECRET_FIELD and the two input lines."""
        m = re.search(r"^  const SECRET_FIELD = .*?\n.*?\n(?=  const srcIn)", src, re.M | re.S)
        self.assertIsNotNone(m, f"{label} has no SECRET_FIELD")
        lines = [l for l in src.splitlines() if "el.type === 'password'" in l or "SECRET_FIELD(el)" in l]
        self.assertEqual(len(lines), 2, label)
        return m.group(0), lines

    def test_snapshot_js_input_rule_matches_the_kit(self):
        # The kit blanks password (fixed stand-in), hidden, one-time-code, card-number and
        # token-named inputs. A package copy that only blanked password and hidden let a
        # named token or card field through, so each copy must carry the kit's rule verbatim.
        want = self.input_rule((KIT / "signed-in" / "snapshot.js").read_text(), "kit")
        for slug in PACKAGES:
            src = (folder(slug) / "snapshot.js").read_text()
            self.assertEqual(self.input_rule(src, slug), want, slug)
            self.assertNotIn("el.type === 'password' || el.type === 'hidden'", src, slug)

    @unittest.skipUnless(shutil.which("node"), "needs node")
    def test_snapshot_js_input_rule_blanks_credentials_when_run(self):
        cases = [  # (source field, expected value attribute on the copy; None = removed, unset = left to the later lines)
            ({"tagName": "INPUT", "type": "password", "value": "hunter2"}, "xxxxxxxx"),
            ({"tagName": "INPUT", "type": "password", "value": ""}, None),
            ({"tagName": "INPUT", "type": "hidden", "value": "csrf-abc"}, None),
            ({"tagName": "INPUT", "type": "text", "autocomplete": "one-time-code", "value": "123456"}, None),
            ({"tagName": "INPUT", "type": "text", "autocomplete": "cc-number", "value": "4242"}, None),
            ({"tagName": "INPUT", "type": "text", "name": "auth_token", "value": "tok-abc"}, None),
            ({"tagName": "INPUT", "type": "text", "id": "apiKey", "value": "key-abc"}, None),
            ({"tagName": "INPUT", "type": "text", "name": "q", "value": "plain"}, "unset"),   # falls through to the ordinary copy
        ]
        harness = """
const cases = %s;
const rule = %s;
const out = cases.map(([el]) => {
  const st = { attr: 'unset' };
  const c = { setAttribute: (k, v) => { st.attr = v; }, removeAttribute: () => { st.attr = null; } };
  new Function('el', 'c', rule)(el, c);
  return st.attr;
});
console.log(JSON.stringify(out));
"""
        for slug in distinct("snapshot.js"):
            defs, lines = self.input_rule((folder(slug) / "snapshot.js").read_text(), slug)
            rule = defs + "".join(l.strip() + "\n" for l in lines)
            res = subprocess.run(["node", "-e", harness % (json.dumps(cases), json.dumps(rule))],
                                 capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, (slug, res.stderr))
            self.assertEqual(json.loads(res.stdout), [w for _, w in cases], slug)

    @staticmethod
    def cut_signed_js(src, label):
        """The SIGNED regex and the cutSigned line of a snapshot.js, runnable on their own."""
        sig = re.search(r"^\s*const SIGNED_PARAMS = .*?\n\s*const SIGNED = new RegExp\(.*?'i'\);$", src, re.M | re.S)
        cut = re.findall(r"^\s*const cutSigned = .*$", src, re.M)
        assert sig and len(cut) == 1, f"{label} has no SIGNED regex or no single cutSigned line"
        url = re.findall(r"^\s*const cutSignedUrl = .*$", src, re.M)
        assert len(url) == 1, f"{label} has no single cutSignedUrl line"
        return sig.group(0), cut[0].strip() + "\n" + url[0].strip()

    @staticmethod
    def whole_copy_pass(src, label):
        """A copy's attribute pass over the clone and its pass over the serialised page."""
        attrs = [l.strip() for l in src.splitlines()
                 if "clone.querySelectorAll('*').forEach" in l and "cutSignedUrl" in l]
        page = [l.strip() for l in src.splitlines() if re.search(r"\bhtml = cutSigned\(", l)]
        assert len(attrs) == 1 and len(page) == 1, f"{label} has no single attribute pass and page pass"
        return attrs[0], page[0]

    def run_whole_copy_pass(self, slug):
        src = (folder(slug) / "snapshot.js").read_text()
        sig, cut = self.cut_signed_js(src, slug)
        attrs, page = self.whole_copy_pass(src, slug)
        js = sig + "\n" + cut + """
const nodes = %s.map(([tag, attrs]) => ({
  tag, attributes: Object.entries(attrs).map(([name, value]) => ({ name, value })),
  setAttribute(k, v) { this.attributes.find((a) => a.name === k).value = v; } }));
const clone = { querySelectorAll: () => nodes,
  get outerHTML() { return nodes.map((n) => '<' + n.tag + n.attributes.map((a) => ' ' + a.name + '="' + a.value + '"').join('') + '>').join('') + '<style>%s</style>'; } };
""" % (json.dumps(WHOLE_COPY_NODES), WHOLE_COPY_STYLE) + attrs + "\n" + page.replace("let html", "var html") + """
console.log(JSON.stringify({ attrs: nodes.map((n) => Object.fromEntries(n.attributes.map((a) => [a.name, a.value]))), html }));
"""
        res = subprocess.run(["node", "-e", js], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, (slug, res.stderr))
        return json.loads(res.stdout)

    def test_snapshot_js_cut_signed_matches_the_kit(self):
        # #401 stopped a package copy's query at ( and ;, which kept &token= after ?crop=(0,0), an
        # &amp; or a ;-separated query; Sentry's older copy ran from a colour's # into a later
        # url(...?sig=) and cut the CSS between. Every copy that cuts signed queries carries the kit's line.
        kit_sig, kit_cut = self.cut_signed_js((KIT / "signed-in" / "snapshot.js").read_text(), "kit")
        copies = sorted(p for p in (ROOT / "systems").glob("*/**/snapshot.js") if "cutSigned" in p.read_text())
        self.assertGreaterEqual(len(copies), len(PACKAGES))
        # abs() only cleans src/href/srcset/poster, so a signed URL in data-src, an inline style or an
        # inlined stylesheet reached the copy and unsnap.py refused it (coursera, manus, chatgpt,
        # notebooklm, duolingo and brilliant had no other pass). Every copy runs the kit's whole-copy
        # pass: every attribute, then the serialised page.
        # Run each distinct copy's two passes on a stand-in clone instead of matching their text.
        for slug in PACKAGES:
            self.whole_copy_pass((folder(slug) / "snapshot.js").read_text(), slug)
        if shutil.which("node"):
            for slug in distinct("snapshot.js"):
                self.assertEqual(self.run_whole_copy_pass(slug), WHOLE_COPY_WANT, slug)
        cases = {
            'color:#fff;background:url(https://x/p.png?sig=1)': 'color:#fff;background:url(https://x/p.png)',
            'a{color:#fff}b{background:url(https://x/p.png?sig=1)}': 'a{color:#fff}b{background:url(https://x/p.png)}',
            '<img data-src="https://x/p?crop=(0,0)&token=abc" alt="">': '<img data-src="https://x/p" alt="">',
            '<a href="https://x/p?a=1&amp;token=abc">': '<a href="https://x/p">',
            '<img data-src="https://x/p?options=a;b&token=abc">': '<img data-src="https://x/p">',
            'background:url(https://x/p.png?sig=1);color:red': 'background:url(https://x/p.png);color:red',
            'https://example.test/page?unit=7': 'https://example.test/page?unit=7',
        }
        # cutSignedUrl (every attribute but style) keeps a ;name: inside the query, so the token after it goes too
        url_cases = {
            '<img data-src="https://x/p?options=a;b:c&token=abc">': '<img data-src="https://x/p">',
            'https://x/p?a=1;b:2&X-Amz-Signature=abc': 'https://x/p',
            '<img data-src="https://x/p?crop=(0,0);b:c&token=abc">': '<img data-src="https://x/p">',
            'https://example.test/page?unit=7;b:2': 'https://example.test/page?unit=7;b:2',
        }
        ran = set()
        for path in copies:
            label = str(path.relative_to(ROOT))
            sig, cut = self.cut_signed_js(path.read_text(), label)
            self.assertEqual(cut, kit_cut, label)
            flat = lambda s: [l.strip() for l in s.splitlines()]
            self.assertEqual(flat(sig), flat(kit_sig), label)   # the regex cutSigned tests each match with
            if shutil.which("node") and (sig, cut) not in ran:   # identical code behaves identically
                ran.add((sig, cut))
                js = sig + "\n" + cut + f"\nconsole.log(JSON.stringify({json.dumps(list(cases))}.map(cutSigned)))"
                res = subprocess.run(["node", "-e", js], capture_output=True, text=True)
                self.assertEqual(res.returncode, 0, (label, res.stderr))
                self.assertEqual(json.loads(res.stdout), list(cases.values()), label)
                js = sig + "\n" + cut + f"\nconsole.log(JSON.stringify({json.dumps(list(url_cases))}.map(cutSignedUrl)))"
                res = subprocess.run(["node", "-e", js], capture_output=True, text=True)
                self.assertEqual(res.returncode, 0, (label, res.stderr))
                self.assertEqual(json.loads(res.stdout), list(url_cases.values()), label)

    def test_unsnap_flags_every_signed_url(self):
        for slug in PACKAGES:
            mod = load(folder(slug) / "unsnap.py", "unsnap_" + re.sub(r"\W", "_", slug))
            for u in SIGNED:
                self.assertTrue(mod.SIGNED.search(u), (slug, u))
            for u in PLAIN:
                self.assertFalse(mod.SIGNED.search(u), (slug, u))
            self.assertEqual(mod.leaks_in("<p>Jane&nbsp;Doe</p>", {"replace": [["jane\\s+doe", "gi", "x"]]}), ["redaction pattern 1"], slug)

    def run_unsnap(self, slug, body, meta, redact, env_redact=True):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        r = Path(d) / "r.json"
        r.write_text(json.dumps(redact))
        snap = Path(d) / "snap.txt"
        snap.write_text("SNAPSTART" + json.dumps(meta) + "SNAPMETA" + body + "SNAPEND")
        env = {k: v for k, v in os.environ.items() if k != "SNAP_REDACT"}
        if env_redact:
            env["SNAP_REDACT"] = str(r)
        res = subprocess.run([sys.executable, str(folder(slug) / "unsnap.py"), str(snap), str(Path(d) / "out")],
                             capture_output=True, text=True, env=env)
        return res, Path(d) / "out"

    def test_unsnap_checks_page_and_meta_and_needs_the_redaction_file(self):
        redact = {"replace": [["Jane Doe", "g", "A User"]]}
        meta = {"label": "home", "url": "https://x.example/"}
        for slug in distinct("unsnap.py"):
            res, out = self.run_unsnap(slug, "<p>hi</p>", meta, redact)
            self.assertEqual(res.returncode, 0, (slug, res.stderr))
            self.assertNotIn("title", json.loads((out / "home.json").read_text()), slug)
            res, out = self.run_unsnap(slug, "<p>hi</p>", meta, redact, env_redact=False)
            self.assertNotEqual(res.returncode, 0, slug)
            self.assertIn("SNAP_REDACT", res.stderr, slug)
            res, out = self.run_unsnap(slug, '<img src="https://x/a.png?X-Goog-Signature=1">', meta, redact)
            self.assertIn("LEAK", res.stderr, slug)
            self.assertFalse((out / "home.html").exists(), slug)
            # A name split by a tag, which the page-only regex never saw.
            res, out = self.run_unsnap(slug, "<p>Jane <b>Doe</b></p>", meta, redact)
            self.assertIn("LEAK", res.stderr, slug)
            self.assertFalse((out / "home.html").exists(), slug)
            # A name in the metadata, which the older copies never checked. Duolingo and NotebookLM
            # apply the replacements themselves, so for them the URL comes out rewritten.
            res, out = self.run_unsnap(slug, "<p>hi</p>", dict(meta, url="https://x.example/Jane Doe"), redact)
            if slug_of(slug) in ("duolingo", "notebooklm"):
                self.assertEqual(res.returncode, 0, (slug, res.stderr))
                self.assertEqual(json.loads((out / "home.json").read_text())["url"], "https://x.example/A User")
            else:
                self.assertIn("LEAK", res.stderr, slug)
                self.assertFalse((out / "home.html").exists(), slug)

    def test_unsnap_meets_accented_names_in_the_metadata(self):
        redact = {"replace": [["Jos\u00e9 Doe", "g", "A User"]]}
        for slug in distinct("unsnap.py"):
            if slug_of(slug) in ("duolingo", "notebooklm"):
                continue   # they rewrite the URL themselves; covered above
            res, out = self.run_unsnap(slug, "<p>hi</p>", {"label": "home", "url": "https://x.example/Jos\u00e9 Doe"}, redact)
            self.assertIn("LEAK", res.stderr, slug)
            self.assertFalse((out / "home.html").exists(), slug)

    def test_measure_scripts_read_a_copy_without_a_title(self):
        # unsnap.py drops the title, so a reader that dereferences it would throw on every new copy.
        for slug in PACKAGES:
            for f in capture_root(slug).rglob("*.mjs"):
                for m in re.finditer(r"\bm\.title\.", f.read_text()):
                    line = f.read_text()[:m.start()].rsplit("\n", 1)[-1]
                    self.assertTrue(line.endswith("m.title ? { title: "), f"{f.relative_to(ROOT)} reads m.title without a guard")

    def test_notebooklm_snapshot_carries_the_safe_url_copy(self):
        kit = (KIT / "safe-url.mjs").read_text()
        body = kit[kit.index("const RESOURCE"):].replace("export function safeUrl", "function safeUrl").rstrip()
        self.assertIn(body, (ROOT / "systems/notebooklm/tools/capture/signed-in/snapshot.js").read_text())
        self.assertEqual((ROOT / "systems/notebooklm/tools/capture/safe-url.mjs").read_text(), kit)


PLAYWRIGHT = os.environ.get("PLAYWRIGHT") or str(Path.home() / ".design-systems/pw/node_modules/playwright/index.mjs")


@unittest.skipIf(not shutil.which("node") or not Path(PLAYWRIGHT).is_file(), "node or the capture Playwright is not installed")
class PackageSnapshotsInABrowser(unittest.TestCase):
    """Runs each package copy's __snap on a small local page in headless Chromium (network
    aborted) and checks the finished copy, so a cleanup pass that moved before the stylesheets were
    inserted, or one a copy dropped, fails here and not only on a capture."""

    PAGE = ('<style>.x{background:url("https://cdn.example.test/bg.png?X-Amz-Signature=abc")}</style>'
            '<div class="x" style="background-image:url(https://cdn.example.test/i.png?sig=1);color:#fff">hi</div>'
            '<img data-src="https://cdn.example.test/a.png?crop=(0,0)&token=abc" src="https://cdn.example.test/plain.png?w=2">'
            '<a href="https://example.test/p?unit=7">x</a>')

    def test_every_copy_cuts_signed_urls_from_the_finished_copy(self):
        script = """
import fs from 'node:fs';
const pw = await import(%s);
const b = await pw.chromium.launch();
const res = {};
for (const [slug, file] of %s) {
  const p = await b.newPage();
  await p.route('**/*', (r) => (r.request().url().startsWith('https://app.example.test/') ? r.fulfill({ contentType: 'text/html', body: %s }) : r.abort()));
  await p.goto('https://app.example.test/home?unit=7&token=abc');
  await p.addScriptTag({ content: fs.readFileSync(file, 'utf8') });
  res[slug] = await p.evaluate(() => window.__snap('t', { replace: [['nothing-matches-this', 'g', 'x']], scrub: [], keep: [], badges: [] }));
  await p.close();
}
await b.close();
console.log(JSON.stringify(res));
""" % (json.dumps(Path(PLAYWRIGHT).as_uri()),
       json.dumps([[s, str(folder(s) / "snapshot.js")] for s in distinct("snapshot.js")]), json.dumps(self.PAGE))
        res = subprocess.run(["node", "--input-type=module", "-e", script], capture_output=True, text=True, timeout=300)
        self.assertEqual(res.returncode, 0, res.stderr[-2000:])
        for slug, out in json.loads(res.stdout).items():
            meta, body = out.removeprefix("SNAPSTART").split("SNAPMETA", 1)
            for leak in ("X-Amz-Signature", "sig=1", "token=abc"):
                self.assertNotIn(leak, body, (slug, leak))       # stylesheet, inline style, data-src
                self.assertNotIn(leak, meta, (slug, leak))       # the page URL in the metadata
            self.assertIn("unit=7", body, slug)                  # a plain query stays
            self.assertIn("plain.png", body, slug)


if __name__ == "__main__":
    unittest.main()
