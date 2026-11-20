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
PW = os.environ.get("PLAYWRIGHT") or str(Path.home() / ".design-systems/pw/node_modules/playwright/index.mjs")


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
    "https://maps.example.test/embed?q=x&key=AIzaFAKEKEY",
    "https://api.example.test/v1?api_key=abc", "https://api.example.test/v1?apikey=abc",
    "https://app.example.test/cb?oauth_token=abc", "https://app.example.test/x?auth_token=abc",
    "https://app.example.test/x?csrf_token=abc", "https://app.example.test/x#jwt=abc",
    "https://app.example.test/x?session=abc", "https://app.example.test/x?client_secret=abc",
    "https://cdn.example.test/v.mp4?hdnts=exp=1~acl=x", "https://cdn.example.test/v.mp4?__token__=abc",
    "https://api.example.test/v1?api-key=abc", "https://api.example.test/v1?access_key=abc",
    "https://app.example.test/x?session_id=abc", "https://app.example.test/x?sessionid=abc",
    "https://cdn.example.test/v.mp4?hmac=abc", "https://app.example.test/x?xsrf_token=abc",
    "https://app.example.test/x?session_token=abc", "https://api.example.test/v1?api_token=abc",
    "https://acct.example.test/c/f.png?sas_token=abc",
    "https://app.example.test/cb?refresh_token=abc", "https://app.example.test/x?auth=abc",
]
PLAIN = [
    "https://example.test/page?unit=7",
    "https://example.test/a?tokenizer=1&sigma=2&codec=h264",
    "https://example.test/a?keyword=x&monkey=1&sessions=3&jwtx=1",
    "https://example.test/docs#tokens",
    "color:#fff",
]


class SharedList(unittest.TestCase):
    def test_every_listed_name_has_a_signed_example(self):
        # so dropping a name from the list cannot pass silently
        spec = json.loads((SIGNED_IN / "signed-params.json").read_text())
        for name in spec["params"]:
            self.assertTrue(any(re.search(r"(?:[?&#]|%3F|%26|%23)(?:amp;)?" + re.escape(name) + r"(?:=|%3D)", u) for u in SIGNED), name)

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

    def test_unsnap_refuses_a_missing_snapshot_and_a_label_that_is_a_path(self):
        with tempfile.TemporaryDirectory() as d:
            redact = Path(d) / "r.json"
            redact.write_text(json.dumps({"replace": [["Jane Doe", "gi", "A User"]]}))
            out = Path(d) / "out"
            for body, why in [("not a snapshot", "no SNAPSTART"),
                              ("SNAPSTART" + json.dumps({"label": "Jane Doe/../x", "url": "https://x/"}) + "SNAPMETA<p>ok</p>SNAPEND", "not a plain name"),
                              ("SNAPSTART" + json.dumps({"label": "../escaped", "url": "https://x/"}) + "SNAPMETA<p>ok</p>SNAPEND", "not a plain name"),
                              ("SNAPSTART" + json.dumps({"label": "a/b", "url": "https://x/"}) + "SNAPMETA<p>ok</p>SNAPEND", "not a plain name"),
                              ("SNAPSTART" + json.dumps({"label": "..", "url": "https://x/"}) + "SNAPMETA<p>ok</p>SNAPEND", "not a plain name")]:
                snap = Path(d) / "snap.txt"
                snap.write_text(body)
                res = subprocess.run([sys.executable, str(SIGNED_IN / "unsnap.py"), str(snap), str(out)],
                                     capture_output=True, text=True, env={**os.environ, "SNAP_REDACT": str(redact)})
                self.assertNotEqual(res.returncode, 0, body)
                self.assertIn(why, res.stderr, body)
                self.assertNotIn("Traceback", res.stderr)
                self.assertNotIn("Jane", res.stderr)   # a refused label is never echoed
            self.assertFalse((Path(d) / "escaped.html").exists())

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


# A computed-style property whose value can be a url(). A script that copies property values in a
# loop (o[p] = cs[p], o[p] = v) must not read any of them raw.
URL_PROPS = re.compile(r"background-?image|(?<![.\w-])cursor(?![-\w])|mask-?image|list-?style-?image|border-?image", re.I)
RAW_PICK = re.compile(r"\b(?:o|out)\[(\w+)\] ?= ?(?:\w+(?:\[\1\]|\.getPropertyValue\(\1\))|v(?:\.length|\.slice))"
                      r"|\b(?:o|out)\[p\] ?= ?v\b(?![.(\w])")
# A single value read raw: p.backgroundImage.slice(…), content: p.content, a resolved custom property.
RAW_READ = re.compile(r"\b(?:p|q|pc|c|cs|a|b)\.(?:backgroundImage|content)\.(?:slice|replace)\(|\bcontent: (?:p|q|pc|a|b)\.content\b"
                      r"|\bout\.vars\[\w+\] = (?!noUrl\()")
# The same two shapes under any target name (style[p] = cs[p], vars[k]=bs.getPropertyValue(k),
# v[n] = (body.getPropertyValue(n) || ...)), for the kit only: RAW_PICK and RAW_READ above name the
# targets the package copies use, and many package copies (kit-ports.md in the audit) still read raw.
WIDE_PICK = re.compile(r"\b[\w.]+\[(\w+)\] ?= ?\w+\[\1\](?![\w.(]|\s*[-+*/%])")
WIDE_PROP = re.compile(r"\b[\w.]+\[[\w.]+\] ?= ?\(?(?:[\w.]+\.)?getPropertyValue\((?![\'\"])")
NO_URL_DEF = re.compile(r"\bnoUrl = \(v\)")
NO_URL_USE = re.compile(r"\bnoUrl\(")


def no_url_scope_errors(src):
    """Line numbers where noUrl( is used with no definition in scope. A definition holds from its line
    until a later line indented less than it (the end of the block it sits in), so each browser
    callback needs its own: they run in the page, apart from the module and from each other."""
    bad, live = [], []
    for n, line in enumerate(src.splitlines(), 1):
        if not line.strip():
            continue
        ind = len(line) - len(line.lstrip())
        live = [d for d in live if d <= ind]
        d = NO_URL_DEF.search(line)
        for u in NO_URL_USE.finditer(line):
            if not live and not (d and d.start() < u.start()):
                bad.append(n)
                break
        if d:
            live.append(ind)
    return bad


def capture_scripts_recording_raw_urls(root):
    """(path, reason) for each capture script under root (every systems/*/tools/capture and the kit's own
    tools/kit/capture, which new packages copy from) that records a computed value raw."""
    bad = []
    root = Path(root)
    for path in sorted([*root.glob("systems/*/tools/capture/**/*"), *root.glob("tools/kit/capture/**/*")]):
        if path.suffix not in (".mjs", ".js") or path.name.startswith("test_"):
            continue
        src = path.read_text()
        if "getComputedStyle" not in src:
            continue
        rel = str(path.relative_to(root))
        if URL_PROPS.search(src):
            bad += [(rel, "raw pick " + m.group(0)) for m in RAW_PICK.finditer(src)]
        bad += [(rel, "raw read " + m.group(0)) for m in RAW_READ.finditer(src)]
        bad += [(rel, f"noUrl used with no definition in scope at line {n}") for n in no_url_scope_errors(src)]
    return bad


def kit_scripts_recording_raw_values(root):
    """(path, reason) for each of the kit's own capture scripts that copies a computed value or a
    custom property into a map raw, whatever the map is called. Kit only: see WIDE_PICK."""
    bad = []
    root = Path(root)
    for path in sorted(root.glob("tools/kit/capture/**/*")):
        if path.suffix not in (".mjs", ".js") or path.name.startswith("test_"):
            continue
        src = path.read_text()
        rel = str(path.relative_to(root))
        if "getComputedStyle" in src and URL_PROPS.search(src):
            bad += [(rel, "raw pick " + m.group(0)) for m in WIDE_PICK.finditer(src)]
        bad += [(rel, "raw custom property " + m.group(0)) for m in WIDE_PROP.finditer(src)]
    for rel in ("tools/kit/capture/vars.mjs", "tools/kit/capture/electron/shot.mjs"):
        bad += [(rel, f"custom property read without noUrl at line {n}") for n in vars_reads_without_no_url((root / rel).read_text())]
        bad += [(rel, f"noUrl used with no definition in scope at line {n}") for n in no_url_scope_errors((root / rel).read_text())]
    return bad


# vars.mjs reads every custom property a stylesheet declares and the value each resolves to. A custom
# property can hold a url() with a signed or per-account query, so each read of one (any
# getPropertyValue(name) with a computed name) goes through noUrl. So does an @font-face rule's src
# (and the descriptors copied in a loop), which names the font files and can carry the same query.
# A literal name other than 'src' (font-family, font-weight...) holds no URL and is left alone.
PROP_READ = re.compile(r"getPropertyValue\((?!['\"](?!src['\"]))")
SRC_ID = re.compile(r"srcId\((?:[\w.]+\.)*getPropertyValue\('src'\)\)")
PROP_READ_SAFE = re.compile(r"noUrl\((?:[\w.]+(?:\([\w.]*\))?\.)*getPropertyValue\((?!['\"](?!src['\"]))")


def vars_reads_without_no_url(src):
    """Line numbers in a vars.mjs source where a custom property's or font-face src's value is read without noUrl."""
    # srcId(...) only hashes a src (queries cut) to tell two faces apart; the hash is never recorded as a value.
    lines = [SRC_ID.sub("", line) for line in src.splitlines()]
    return [n for n, line in enumerate(lines, 1) if len(PROP_READ.findall(line)) != len(PROP_READ_SAFE.findall(line))]


def vars_scripts_recording_raw_values(root):
    """(path, reason) for each vars.mjs under root (every package's and the kit's) that records a value raw."""
    root = Path(root)
    bad = []
    for path in sorted([*root.glob("systems/*/tools/capture/**/vars.mjs"), *root.glob("tools/kit/capture/**/vars.mjs")]):
        src = path.read_text()
        rel = str(path.relative_to(root))
        bad += [(rel, f"custom property read without noUrl at line {n}") for n in vars_reads_without_no_url(src)]
        bad += [(rel, f"noUrl used with no definition in scope at line {n}") for n in no_url_scope_errors(src)]
    return bad


def js_block(path, start, end):
    """The source lines from the first one starting with `start` through the first after it starting with `end`."""
    lines = Path(path).read_text().splitlines()
    i = next(n for n, l in enumerate(lines) if l.lstrip().startswith(start))
    j = next(n for n in range(i, len(lines)) if lines[n].lstrip().startswith(end))
    return "\n".join(lines[i:j + 1])


@unittest.skipIf(NODE is None, "node is not on PATH")
class ConsoleScrub(unittest.TestCase):
    """Package captures commit their logs (raw/*.log), and a Playwright error quotes the locator it failed on
    and, on navigation, the page URL. Each capture script that prints such errors runs here in a scratch copy of
    the kit, with a stub Playwright whose launch throws an error carrying two queries, and must print the
    message without them."""
    SCRIPTS = ["icons.mjs", "layout.mjs", "motion-probe.mjs", "public/measure.mjs", "public/public.mjs", "signed-in/measure.mjs"]

    def test_every_script_prints_errors_without_their_queries(self):
        for rel in self.SCRIPTS:
            with self.subTest(script=rel), tempfile.TemporaryDirectory() as d:
                d = Path(d)
                capture = d / "pkg/tools/capture"
                shutil.copytree(HERE / "kit/capture", capture, ignore=shutil.ignore_patterns("test_*", "native"))
                stub = d / "playwright-stub.mjs"
                stub.write_text("const launch = async () => { throw new Error(\"page.goto: net::ERR_FAILED at "
                                "https://cdn.example.test/a.png?token=SECRET1 waiting for locator('img[src=\\\"/b.png?sig=SECRET2\\\"]')\"); };\n"
                                "export const chromium = { launch, connectOverCDP: launch };\nexport default { chromium };\n")
                snaps = d / "snaps"
                snaps.mkdir()
                (snaps / "home-dark.html").write_text("<html><head><style>:root{--a:1px}</style></head><body></body></html>")
                # every page copy the signed-in specs name, with the metadata snapshot.js writes beside it
                labels = set(re.findall(r"snap: '([^']+)'", (HERE / "kit/capture/signed-in/measure.mjs").read_text())) | {"home-dark"}
                for label in labels:
                    (snaps / f"{label}.html").write_text("<html><body></body></html>")
                    (snaps / f"{label}.json").write_text('{"url": "https://x.test/", "w": 1440, "h": 900}')
                env = {**os.environ, "PLAYWRIGHT": stub.as_uri(), "KIT_EXAMPLE": "1", "SNAPS": str(snaps), "RAW": str(d / "raw"),
                       "HOME": str(d / "home"), "USERPROFILE": str(d / "home")}
                res = subprocess.run([NODE, str(capture / rel)], capture_output=True, text=True, cwd=d, timeout=60, env=env)
                out = res.stdout + res.stderr
                self.assertNotEqual(res.returncode, 0, out[-1500:])
                self.assertIn("cdn.example.test/a.png", out, out[-1500:])   # the error was printed
                for secret in ("SECRET1", "SECRET2", "token=", "sig="):
                    self.assertNotIn(secret, out, out[-1500:])

    def test_scrub_console_cleans_strings_and_errors(self):
        mod = (HERE / "kit/capture/no-query.mjs").as_uri()
        script = (f"import({json.dumps(mod)}).then(({{ scrubConsole }}) => {{ scrubConsole();"
                  "console.log('failed', 'img[src=\"/a?sig=S1\"]', 3); console.error(new Error('at /b?token=S2'));"
                  "console.warn('ok /c'); })")
        res = subprocess.run([NODE, "-e", script], capture_output=True, text=True, timeout=30)
        self.assertEqual(res.returncode, 0, res.stderr)
        out = res.stdout + res.stderr
        self.assertIn('failed img[src="/a"] 3', res.stdout)
        self.assertIn("at /b", res.stderr)
        self.assertIn("ok /c", res.stderr)
        self.assertNotIn("S1", out)
        self.assertNotIn("S2", out)


class PackageCaptureScripts(unittest.TestCase):
    """Python only, so it runs without node."""

    def test_every_package_capture_script_records_computed_values_through_no_url(self):
        # Every package's capture scripts and the kit's, found by glob so a new copy is covered too: no computed
        # value that can hold a url() (a picked property, a pseudo-element's content or background
        # image, a resolved custom property, a one-off box reading) is recorded raw, and each scope
        # that calls noUrl defines it first (a const read before its line throws, and the paint-loop
        # fix had put it after pick).
        self.assertEqual(capture_scripts_recording_raw_urls(HERE.parent), [])

    def test_the_raw_patterns_catch_each_shape(self):
        for raw in ("for (const p of props) o[p] = cs[p];", "out[p] = cs.getPropertyValue(p);",
                    "const v = cs.getPropertyValue(p); o[p] = v;", "o[p]=v.slice(0,300)"):
            self.assertTrue(RAW_PICK.search(raw), raw)
        for ok in ("o[p] = noUrl(cs[p]);", "o[p] = noUrl(v).slice(0, 300);", "if (v !== skip) o[k] = v;"):
            self.assertFalse(RAW_PICK.search(ok), ok)
        for raw in ("content: p.content, width", "p.backgroundImage.slice(0, 200)", "out.vars[n] = root.getPropertyValue(n).trim();"):
            self.assertTrue(RAW_READ.search(raw), raw)
        self.assertFalse(RAW_READ.search("out.vars[n] = noUrl(v);"))

    def test_kit_scripts_record_no_value_raw_under_any_name(self):
        # The Electron route wrote every custom property raw as v[n] = (body.getPropertyValue(n) || ...),
        # a target name the package-wide patterns above do not know.
        self.assertEqual(kit_scripts_recording_raw_values(HERE.parent), [])

    def test_the_wide_patterns_catch_each_shape(self):
        for raw in ("for (const p of PROPS) style[p] = cs[p];", "vars[k]=bs.getPropertyValue(k)",
                    "for (const n of names) v[n] = (body.getPropertyValue(n) || html.getPropertyValue(n)).trim();",
                    "out.vars[n] = root.getPropertyValue(n).trim();"):
            self.assertTrue(WIDE_PICK.search(raw) or WIDE_PROP.search(raw), raw)
        for ok in ("style[p] = noUrl(cs[p]);", "vars[k] = noUrl(bs.getPropertyValue(k));", "v[n] = read(n);",
                   "o[k] = c.getPropertyValue('font-family');", "seen[k] = seen[k] + 1;", "o[p] = cs[p].slice(0, 9);"):
            self.assertFalse(WIDE_PICK.search(ok) or WIDE_PROP.search(ok), ok)
        # the line every package's electron/shot.mjs still carries, which the vars lint flags too
        self.assertEqual(vars_reads_without_no_url(
            "  for (const n of [...names].sort()) v[n] = (body.getPropertyValue(n) || html.getPropertyValue(n)).trim();"), [1])

    def test_every_vars_script_records_custom_properties_through_no_url(self):
        # Declared values (props[k], decls, root/dark) and resolved ones (raw, resolved[w], theme) alike.
        self.assertEqual(vars_scripts_recording_raw_values(HERE.parent), [])
        # Each copy of noUrl is the kit's, which test_vars_no_url_reads_authored_tokens runs under node.
        tested = re.search(r"const noUrl = .*?: v\);", (HERE / "kit/capture/vars.mjs").read_text()).group(0)
        for path in [*HERE.parent.glob("systems/*/tools/capture/**/vars.mjs"), HERE / "kit/capture/vars.mjs"]:
            for d in re.findall(r"const noUrl = .*?: v\);", path.read_text()):
                self.assertEqual(d, tested, path)

    def test_the_vars_patterns_catch_each_shape(self):
        for raw in ("props[k] = r.style.getPropertyValue(k).trim();", "const raw = getComputedStyle(el).getPropertyValue(name).trim();",
                    "return Object.fromEntries(ns.map((n) => [n, cs.getPropertyValue(n).trim()]));",
                    "all[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim();"):
            self.assertEqual(vars_reads_without_no_url(raw), [1], raw)
        for ok in ("props[k] = noUrl(r.style.getPropertyValue(k).trim());", "const raw = noUrl(getComputedStyle(el).getPropertyValue(name).trim());",
                   "return Object.fromEntries(ns.map((n) => [n, noUrl(cs.getPropertyValue(n).trim())]));",
                   "ff.push({ family: r.style.getPropertyValue('font-family'), src: noUrl(r.style.getPropertyValue('src')) });",
                   "for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());"):
            self.assertEqual(vars_reads_without_no_url(ok), [], ok)
        # a font-face src is read through noUrl like any other value: raw, by literal name or in a loop, is flagged
        for raw in ("ff.push({ family: r.style.getPropertyValue('font-family'), src: r.style.getPropertyValue('src') });",
                    "if (r.type === CSSRule.FONT_FACE_RULE) {\n  const o = { file };\n  for (const k of r.style) o[k] = r.style.getPropertyValue(k).trim();\n}"):
            self.assertNotEqual(vars_reads_without_no_url(raw), [], raw)
        self.assertEqual(vars_reads_without_no_url("const o = { family: r.style.getPropertyValue('font-family') };"), [])
        self.assertEqual(vars_reads_without_no_url("ff.push({ src: noUrl(r.style.getPropertyValue('src')), sid: srcId(r.style.getPropertyValue('src')) });"), [])
        self.assertEqual(vars_reads_without_no_url("ff.push({ src: noUrl(r.style.getPropertyValue('src')), sid: r.style.getPropertyValue('src') });"), [1])

    def test_vars_scripts_record_no_raw_font_urls(self):
        # A font response URL, a font-face cssText and a link href can carry a signed query: font URL lists
        # keep the path only (bare()), cssText goes through noUrl, an href keeps origin and path.
        root = HERE.parent
        raw = re.compile(r"fonts\.(?:push|add)\((?!bare\(|o\))|fontfaces\.push\((?!noUrl\()|(?<!hrefPath\()\bm\.getAttribute\('href'\)")
        bad = []
        for path in sorted([*root.glob("systems/*/tools/capture/**/vars.mjs"), root / "tools/kit/capture/vars.mjs"]):
            for n, line in enumerate(path.read_text().splitlines(), 1):
                if raw.search(line):
                    bad.append(f"{path.relative_to(root)}:{n}")
        self.assertEqual(bad, [])
        for slug in ("brilliant", "coursera"):
            self.assertIn("bare(", (root / f"systems/{slug}/tools/capture/vars.mjs").read_text())

    def test_a_placeholder_is_recorded_as_a_placeholder_and_every_text_through_no_email(self):
        for path in (SIGNED_IN / "measure.mjs", HERE / "kit/capture/public/lib.mjs"):
            src = path.read_text()
            text = [l for l in src.splitlines() if re.match(r"\s*text: ", l)]
            self.assertTrue(text, path)
            for line in text:
                self.assertNotIn("placeholder", line, path)   # a field's placeholder is not its text
                self.assertIn("noEmail(", line, path)
            for line in (l for l in src.splitlines() if "out.placeholder = {" in l or "text: tn.textContent" in l):
                self.assertIn("noEmail(", line, path)
            self.assertRegex(src, r"out\.placeholder = \{ text: noEmail\(", path)

    def test_placeholder_fallback_goes_through_no_url(self):
        # The composer placeholder falls back to the ::before content, a computed value that can be a url().
        root = HERE.parent
        bad = []
        for path in sorted([*root.glob("systems/*/tools/capture/**/measure.mjs"), SIGNED_IN / "measure.mjs"]):
            for n, line in enumerate(path.read_text().splitlines(), 1):
                if re.search(r"data-placeholder'\) \|\| b\.content", line):
                    bad.append(f"{path.relative_to(root)}:{n}")
        self.assertEqual(bad, [])

    def test_each_callback_needs_its_own_no_url(self):
        two = ("const HELPERS = () => {\n  const noUrl = (v) => v;\n  const box = (el) => noUrl(el);\n};\n"
               "async function styleOf(locator) {\n  return locator.evaluate((el) => {\n{inner}  });\n}\n")
        self.assertEqual(no_url_scope_errors(two.replace("{inner}", "    const noUrl = (v) => v;\n    const pick = (cs) => noUrl(cs);\n")), [])
        self.assertEqual(no_url_scope_errors(two.replace("{inner}", "    const pick = (cs) => noUrl(cs);\n")), [7])
        self.assertEqual(no_url_scope_errors(two.replace("{inner}", "    const pick = (cs) => noUrl(cs);\n    const noUrl = (v) => v;\n")), [7])
        self.assertEqual(no_url_scope_errors("l.evaluate((el) => { const noUrl = (v) => v; return noUrl(el); });"), [])


@unittest.skipIf(NODE is None, "node is not on PATH")
class JavaScriptHalves(unittest.TestCase):
    def node(self, src):
        res = subprocess.run([NODE, "-e", src], capture_output=True, text=True, timeout=30)
        self.assertEqual(res.returncode, 0, res.stderr)
        return json.loads(res.stdout)

    def test_snapshot_cuts_every_signed_query_and_keeps_plain_ones(self):
        src = js_block(SIGNED_IN / "snapshot.js", "const SIGNED_PARAMS", "const cutSignedUrl")
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
            # A match that starts at a colour's # must not run on to a later signed url() and take the CSS.
            'color:#fff;background:url(https://x/p.png?sig=1)': 'color:#fff;background:url(https://x/p.png)',
            'a{color:#fff}b{background:url(https://x/p.png?sig=1)}': 'a{color:#fff}b{background:url(https://x/p.png)}',
            '<a href="https://x/p?a=1&amp;token=abc">': '<a href="https://x/p">',
            '<img data-src="https://x/p?options=a;b&token=abc">': '<img data-src="https://x/p">',
            'color:#fff; background:url(https://x/p.png?sig=1)': 'color:#fff; background:url(https://x/p.png)',
        }
        got = self.node(src + f"\nconsole.log(JSON.stringify({json.dumps(list(cases))}.map(cutSigned)))")
        self.assertEqual(got, list(cases.values()))

    def test_cut_signed_url_reads_a_semicolon_inside_a_url_query(self):
        # cutSigned stops a query at ";name:" because that starts the next CSS declaration, which is right
        # for a style attribute and a stylesheet. In any other attribute the ; and : are part of the URL,
        # so the signed parameter after them was left in (unsnap.py then refused the copy). cutSignedUrl
        # has no declaration rule, and the attribute pass uses it for every attribute except style.
        src = js_block(SIGNED_IN / "snapshot.js", "const SIGNED_PARAMS", "const cutSignedUrl")
        url_cases = {
            '<img data-src="https://x/p?options=a;b:c&token=abc">': '<img data-src="https://x/p">',
            'https://x/p?a=1;b:2&X-Amz-Signature=abc': 'https://x/p',
            'https://x/p?crop=(0,0)&token=abc': 'https://x/p',
            'https://x/p?a=1&amp;token=abc': 'https://x/p',
            'https://x/p?unit=7;b:2': 'https://x/p?unit=7;b:2',
            'https://x/p?page=2#top': 'https://x/p?page=2#top',
            # a ) or , before a ; is still inside the query: only whitespace, a quote, < > or { } end it
            '<img data-src="https://x/p?crop=(0,0);b:c&token=abc">': '<img data-src="https://x/p">',
            'https://x/p?crop=(0,0),b:c&token=abc': 'https://x/p',
            'https://x/a.png?sig=1 1x, https://x/b.png 2x': 'https://x/a.png 1x, https://x/b.png 2x',
        }
        got = self.node(src + f"\nconsole.log(JSON.stringify({json.dumps(list(url_cases))}.map(cutSignedUrl)))")
        self.assertEqual(got, list(url_cases.values()))
        # the style-attribute rule is unchanged: it still stops at ;name: so a colour's # never runs into a later url()
        style = {
            'color:#fff;background:url(https://x/p.png?sig=1)': 'color:#fff;background:url(https://x/p.png)',
            'https://x/p?a=1;b:2&token=abc': 'https://x/p?a=1;b:2&token=abc',   # the case cutSignedUrl exists for
        }
        got = self.node(src + f"\nconsole.log(JSON.stringify({json.dumps(list(style))}.map(cutSigned)))")
        self.assertEqual(got, list(style.values()))
        # on CSS text it can cut more than cutSigned (it runs from a colour's # through the url() and on), never less
        for css in ('color:#fff;background:url(https://x/p.png?sig=1);margin:0', 'background:url(https://x/p.png?sig=1);color:red', 'background:url(https://x/p.png?sig=1), url(https://x/q.png?token=a)'):
            got = self.node(src + f"\nconsole.log(JSON.stringify([cutSignedUrl({json.dumps(css)})]))")
            self.assertFalse(catalog.SIGNED_URL.search(got[0]), got)

    def test_snapshot_attribute_pass_uses_the_url_only_cut_for_non_style_attributes(self):
        src = (SIGNED_IN / "snapshot.js").read_text()
        self.assertIn("(a.name === 'style' ? cutSigned : cutSignedUrl)(a.value)", src)

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

    def test_electron_vars_record_no_url_or_query(self):
        # shot.mjs writes every root custom property beside the screenshot; a signed-in app can set one
        # to an avatar or asset URL that carries a signature.
        shot = (HERE / "kit/capture/electron/shot.mjs").read_text()
        src = next(l.strip() for l in shot.splitlines() if l.strip().startswith("const noUrl = "))
        self.assertIn("vars.vars = scrubQueries(vars.vars);", shot)   # the recorded values go through no-query.mjs
        mod = (HERE / "kit/capture/no-query.mjs").as_uri()
        self.assertEqual(re.search(r"const noUrl = .*?: v\);", src).group(0),
                         re.search(r"const noUrl = .*?: v\);", (HERE / "kit/capture/vars.mjs").read_text()).group(0))
        cases = {
            'url("https://cdn.example.test/a.png?X-Amz-Signature=1")': 'url(…)',
            '"https://cdn.example.test/a.png?token=abc"': '"https://cdn.example.test/a.png"',
            'https://cdn.example.test/a.png#access_token=abc': 'https://cdn.example.test/a.png',
            '"https://cdn.example.test/a(1).png?token=abc"': '"https://cdn.example.test/a(1).png"',
            '"https://cdn.example.test/a.png?crop=(0,0)&token=abc"': '"https://cdn.example.test/a.png"',
            'https://cdn.example.test/a.png?crop=(0,0)&token=abc 2x': 'https://cdn.example.test/a.png',   # fails closed: over-cut
            'avatar?token=secret': 'avatar',
            '//cdn.example.test/avatar.png?token=secret': '//cdn.example.test/avatar.png',
            '"//cdn.example.test/a.png#access_token=abc"': '"//cdn.example.test/a.png"',
            'image-set("//cdn.example.test/a.png?sig=1" 1x, //cdn.example.test/b.png?sig=2 2x)': 'image-set("//cdn.example.test/a.png" 1x, //cdn.example.test/b.png',
            '/media/avatar.png?token=secret': '/media/avatar.png',
            '"avatar.png?sig=abc"': '"avatar.png"',
            '/avatar.png?crop=(0,0)&token=secret': '/avatar.png',
            'avatar(1).png?token=secret': 'avatar(1).png',
            'calc(100% - 2px)': 'calc(100% - 2px)',
            'url(data:image/svg+xml,abc) no-repeat': 'url(data:image/svg+xml,abc) no-repeat',
            '#5e6ad2': '#5e6ad2',
            '0 1px 2px rgba(0, 0, 0, 0.1)': '0 1px 2px rgba(0, 0, 0, 0.1)',
            '': '',
        }
        script = (f"import({json.dumps(mod)}).then(({{ noQuery }}) => {{ {src}\n"
                  f"console.log(JSON.stringify({json.dumps(list(cases))}.map((v) => noQuery(noUrl(v))))); }})")
        got = self.node(script)
        self.assertEqual(got, list(cases.values()))
        for v in got:
            self.assertFalse(catalog.SIGNED_URL.search(v), v)
        # body's own value wins whenever it has one, a blank override included; html's is the fallback
        page = {"H": {"--a": " red", "--b": " blue", "--c": "url(https://x.test/a.png?sig=1)"}, "B": {"--a": " ", "--b": ""}}
        stub = (f"const VALUES = {json.dumps(page)}; const document = {{ documentElement: 'H', body: 'B' }};\n"
                "const getComputedStyle = (e) => ({ getPropertyValue: (n) => VALUES[e][n] ?? '' });\n")
        src = js_block(HERE / "kit/capture/electron/shot.mjs", "const noUrl", "const read")
        got = self.node(stub + src + "\nconsole.log(JSON.stringify(['--a', '--b', '--c'].map(read)))")
        self.assertEqual(got, ["", "blue", "url(…)"])

    def test_the_no_query_node_tests_pass(self):
        # tools/kit/capture/test_no_query.mjs: the full case table, and keys that clean alike being merged
        # the TAP reporter is named: node picks the spec reporter by itself on CI, whose counts read "ℹ pass 5"
        res = subprocess.run([NODE, "--test", "--test-reporter=tap", str(HERE / "kit/capture/test_no_query.mjs")],
                             capture_output=True, text=True, timeout=60)
        self.assertEqual(res.returncode, 0, res.stdout[-3000:] + res.stderr[-1000:])
        self.assertRegex(res.stdout, r"(?m)^# pass [1-9]")
        self.assertRegex(res.stdout, r"(?m)^# fail 0$")

    def test_vars_mjs_writes_its_output_through_the_query_scrub(self):
        # vars.mjs records declared and resolved values and selectors; noUrl only sees url(), so a bare,
        # scheme-relative or relative URL with a query kept it until the whole output went through scrubQueries.
        src = (HERE / "kit/capture/vars.mjs").read_text()
        self.assertIn("const saved = scrubQueries(out);", src)
        self.assertIn("JSON.stringify(saved, null, 1)", src)
        self.assertIn("from './no-query.mjs'", src)

    @unittest.skipIf(not Path(PW).is_file(), "the capture Playwright is not installed")
    def test_vars_mjs_prints_no_query_either(self):
        # Train 19: the saved JSON was scrubbed, but the console summary printed the raw selector map, and
        # package captures commit their console output (raw/*.log). Run vars.mjs on a page copy holding a
        # selector with a query, and look for the id in both the file and stdout.
        with tempfile.TemporaryDirectory() as d:
            pkg, snaps = Path(d) / "pkg", Path(d) / "snaps"
            (pkg / "tools/capture").mkdir(parents=True)
            snaps.mkdir()
            for f in ("vars.mjs", "no-query.mjs"):
                shutil.copy(HERE / "kit/capture" / f, pkg / "tools/capture" / f)
            (snaps / "home.html").write_text('<html><head><style>img[src="/avatar?account_id=12345"]{--avatar-size:32px}'
                                             ' a[href=/u?session=abc]{--link:#00f} :root{--bg:#fff}</style></head><body></body></html>')
            res = subprocess.run([NODE, str(pkg / "tools/capture/vars.mjs")], capture_output=True, text=True, timeout=120,
                                 env={**os.environ, "SNAPS": str(snaps), "PLAYWRIGHT": PW, "KIT_EXAMPLE": "1"})
            self.assertEqual(res.returncode, 0, res.stderr[-2000:])
            saved = (pkg / "raw/css-vars.json").read_text()
        self.assertIn('img[src=\\"/avatar\\"]', saved)
        self.assertIn('img[src="/avatar"]', res.stdout)   # the printed map is the scrubbed one
        for out in (saved, res.stdout, res.stderr):
            self.assertNotIn("12345", out)
            self.assertNotIn("account_id", out)
            self.assertNotIn("session=", out)

    def test_electron_shot_prints_no_query_in_its_errors(self):
        src = (HERE / "kit/capture/electron/shot.mjs").read_text()
        for line in (l for l in src.splitlines() if "console.error(`" in l and "${" in l):
            self.assertIn("noQuery(", line, line)

    def test_measure_scripts_write_every_string_through_the_email_mask(self):
        # Greptile on PR 1298: styleOf masked text, but attrs['aria-label'] (and an error or a selector)
        # still reached components-computed.json with the address in it
        for path in (SIGNED_IN / "measure.mjs", HERE / "kit/capture/public/measure.mjs"):
            src = path.read_text()
            writes = [l for l in src.splitlines() if "writeFileSync(OUT" in l]
            self.assertTrue(writes, path)
            for line in writes:
                self.assertIn(", noEmails, 1)", line, path)
            block = js_block(path, "const EMAIL", "const noEmails")
            got = self.node(block + "\nconsole.log(JSON.stringify({ attrs: { 'aria-label': 'Switch to person.name@example.co' }, "
                            "error: 'toggle refused: A \"a@b.example\"', n: 3, list: ['x', 'y@z.test'] }, noEmails))")
            self.assertEqual(got, {"attrs": {"aria-label": "Switch to <email>"}, "error": 'toggle refused: A "<email>"', "n": 3, "list": ["x", "<email>"]}, path)
        self.assertIn("(out.attrs ||= {})[a] = noEmail(el.getAttribute(a))", (SIGNED_IN / "measure.mjs").read_text())

    def test_recorded_text_masks_email_addresses(self):
        # finding 11e-22: a sign-in field's placeholder showed the product's inbox, and styleOf recorded it
        for path in (SIGNED_IN / "measure.mjs", HERE / "kit/capture/public/lib.mjs"):
            src = js_block(path, "const noEmail = ", "const noEmail = ")
            got = self.node(src + "\nconsole.log(JSON.stringify(["
                            "noEmail('Email hello.team+news@example.co.uk to join'), noEmail('first.last@sub.example.com'),"
                            "noEmail('Sign in'), noEmail('@handle and a@b'), noEmail(null)]))")
            self.assertEqual(got, ["Email <email> to join", "<email>", "Sign in", "@handle and a@b", None], path)

    def test_font_face_ids_tell_apart_files_the_masked_src_cannot(self):
        # noUrl turns every font file URL into url(…), so two faces of one family, weight and style that
        # differ only in the file would share a key and one would be dropped. srcId hashes the src with
        # its queries cut, and goes in the key only.
        root = HERE.parent
        lines = {line.strip() for slug in ("airbnb", "airtable", "anam", "anthropic", "expedia", "gauth", "refero-design")
                 for line in (root / f"systems/{slug}/tools/capture/vars.mjs").read_text().splitlines() if line.lstrip().startswith("const srcId = ")}
        self.assertEqual(len(lines), 1, "every copy carries the same srcId")
        a, b, c = ('url("https://x.test/a.woff2?X-Amz-Signature=1") format("woff2")', 'url("https://x.test/b.woff2") format("woff2")',
                   'url("https://x.test/a.woff2?X-Amz-Signature=2") format("woff2")')
        got = self.node(next(iter(lines)) + f"\nconsole.log(JSON.stringify([{json.dumps(a)}, {json.dumps(b)}, {json.dumps(c)}].map(srcId)))")
        self.assertNotEqual(got[0], got[1])
        self.assertEqual(got[0], got[2])

    def test_vars_no_url_reads_authored_tokens(self):
        # A declared custom property keeps its authored tokens (unlike a computed value, which the
        # browser serialises as lowercase url("...")), so case, escapes and inner space all occur.
        src = js_block(HERE / "kit/capture/vars.mjs", "const noUrl", "const noUrl")
        cases = {
            'url("https://x/p.png?X-Amz-Signature=1"), linear-gradient(red, blue)': 'url(…), linear-gradient(red, blue)',
            'URL("https://x.test/a?sig=secret")': 'url(…)',
            'Url(https://x.test/a?sig=secret) no-repeat': 'url(…) no-repeat',
            'url(https://x.test/a\\)b?sig=secret)': 'url(…)',
            'url( https://x.test/a?sig=secret )': 'url(…)',
            'url( #clip)': 'url( #clip)',
            'url( "data:image/svg+xml,abc")': 'url( "data:image/svg+xml,abc")',
            'URL(#clip)': 'URL(#clip)',
            'url("data:image/svg+xml,abc")': 'url("data:image/svg+xml,abc")',
            '4px': '4px',
            # an @font-face src: the file URLs go, the format hints and local() names stay
            'url("https://x.test/f.woff2?X-Amz-Signature=1") format("woff2"), url(https://x.test/f.woff?token=a) format("woff")':
                'url(…) format("woff2"), url(…) format("woff")',
            'local("Inter"), url(data:font/woff2;base64,AAAA) format("woff2")': 'local("Inter"), url(data:font/woff2;base64,AAAA) format("woff2")',
        }
        got = self.node(src + f"\nconsole.log(JSON.stringify({json.dumps(list(cases))}.map(noUrl)))")
        self.assertEqual(got, list(cases.values()))

    def test_painted_layer_background_images_record_no_url(self):
        # The paint loop keeps a background image that does not start with url(https:, so a gradient
        # followed by a signed url() reached the readings unless it went through noUrl too.
        root = HERE.parent
        copies = [SIGNED_IN / "measure.mjs", HERE / "kit/capture/public/lib.mjs",
                  *(root / f"systems/{p}/tools/capture/signed-in/measure.mjs"
                    for p in ("chatgpt", "claude", "coursera", "linear", "manus", "notebooklm", "sentry")),
                  *(root / f"systems/{p}/tools/capture/{rel}" for p, rel in (
                      ("coursera", "lib.mjs"), ("gauth", "lib.mjs"), ("refero-design", "public/lib.mjs"),
                      ("tokentracker", "public/lib.mjs"), ("sentry", "public/lib.mjs"),
                      ("researchrabbit", "measure.mjs")))]
        for path in copies:
            src = path.read_text()
            painted = [ln for ln in src.splitlines()
                       if re.search(r"const bgi = c\.backgroundImage|bgImage: c\.backgroundImage === 'none'", ln)]
            self.assertTrue(painted, path)
            for ln in painted:
                self.assertIn("noUrl(c.backgroundImage)", ln, path)
            got = self.node(js_block(path, "const noUrl", "const noUrl")
                            + "\nconsole.log(JSON.stringify(noUrl('linear-gradient(red, blue), url(\"https://x/p.png?sig=1\")')))")
            self.assertEqual(got, "linear-gradient(red, blue), url(…)", path)

    def test_every_recorded_background_image_goes_through_no_url(self):
        # Beyond the paint loop, a measure script records a background image in the computed-style
        # pick, a ::before/::after and (Coursera's in-page box()) a box. NotebookLM had no noUrl at
        # all and Coursera's box() and pseudo() read it raw, so each read of one goes through noUrl.
        root = HERE.parent
        for path in (SIGNED_IN / "measure.mjs", root / "systems/notebooklm/tools/capture/signed-in/measure.mjs",
                     root / "systems/coursera/tools/capture/signed-in/measure.mjs"):
            src = path.read_text()
            reads = re.findall(r"[\w(]*\b(?:c|cs|p)\.backgroundImage\.(?:slice|replace)\(", src)
            self.assertFalse(reads, (path, reads))   # a recorded value is noUrl(x.backgroundImage)...
            self.assertNotRegex(src, r"o\[p\] = cs\[p\]", path)   # ...and so is every picked property
            self.assertEqual(len(re.findall(r"const noUrl = ", src)), 1, path)

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



@unittest.skipIf(NODE is None, "node is not on PATH")
class RawShotsStayOutOfTheRepo(unittest.TestCase):
    def test_public_capture_needs_a_scratch_dir_outside_a_package(self):
        # A copy of the capture tree in a scratch package, with a stand-in Playwright whose launch throws:
        # if the RAW guard ever regressed, this fails without opening a browser, reaching the network or
        # writing into the checkout. So it needs no Playwright and runs in CI too.
        env = {k: v for k, v in os.environ.items() if k != "RAW"}
        with tempfile.TemporaryDirectory() as d:
            capture = Path(d) / "pkg" / "tools" / "capture"
            shutil.copytree(HERE / "kit/capture", capture, ignore=shutil.ignore_patterns("test_*", "native"))
            stub = Path(d) / "playwright-stub.mjs"
            stub.write_text("const launch = () => { throw new Error('stub Playwright: no browser in this test'); };\n"
                            "export const chromium = { launch, connectOverCDP: launch };\nexport default { chromium };\n")
            res = subprocess.run([NODE, str(capture / "public/public.mjs")], capture_output=True, text=True, cwd=d,
                                 timeout=60, env={**env, "PLAYWRIGHT": stub.as_uri(), "KIT_EXAMPLE": "1",
                                                  "HOME": str(Path(d) / "home"), "USERPROFILE": str(Path(d) / "home")})
            self.assertEqual(res.returncode, 2, res.stderr)
            self.assertIn("set RAW=", res.stderr)
            self.assertNotIn("stub Playwright", res.stderr)
            self.assertEqual(sorted(p.name for p in (Path(d) / "pkg").iterdir()), ["tools"])   # nothing written
            # a regressed guard would default to ~/.design-systems/<slug>/raw-shots: HOME points in here
            self.assertFalse((Path(d) / "home").exists())
        src = (HERE / "kit/capture/public/public.mjs").read_text()
        self.assertIn("'.design-systems', path.basename(PKG), 'raw-shots'", src)
        self.assertNotIn("raw/full/", src)


if __name__ == "__main__":
    unittest.main()
