"""The signed-in snapshot copies inside packages (systems/<slug>/tools/capture/) keep the kit's
private-data guards: one signed-URL parameter list, an unsnap.py that checks the copy and its
metadata and needs $SNAP_REDACT, and a snapshot.js that copies no password or hidden value.
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
PACKAGES = {
    "claude": "signed-in", "coursera": "signed-in", "manus": "signed-in", "chatgpt": "signed-in",
    "notebooklm": "signed-in", "duolingo": "signed-in", "linear": "signed-in", "brilliant": "signed-in",
    "researchrabbit": "",
}
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


def folder(slug):
    return ROOT / "systems" / slug / "tools" / "capture" / PACKAGES[slug]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class PackageSnapshots(unittest.TestCase):
    kit = json.loads((KIT / "signed-in" / "signed-params.json").read_text())

    def test_each_copy_carries_the_kit_list(self):
        want = {"prefixes": self.kit["prefixes"], "params": self.kit["params"]}
        for slug in PACKAGES:
            d = folder(slug)
            spec = json.loads((d / "signed-params.json").read_text())
            self.assertEqual({"prefixes": spec["prefixes"], "params": spec["params"]}, want, slug)
            m = re.search(r"^\s*const SIGNED_PARAMS = (\{.*\});$", (d / "snapshot.js").read_text(), re.M)
            self.assertIsNotNone(m, f"{slug} snapshot.js has no SIGNED_PARAMS line")
            self.assertEqual(json.loads(m.group(1)), want, slug)

    def test_snapshot_js_blanks_password_and_hidden_values(self):
        for slug in PACKAGES:
            src = (folder(slug) / "snapshot.js").read_text()
            self.assertIn("if (el.type === 'password' || el.type === 'hidden') { c.removeAttribute('value'); return; }", src, slug)

    def test_unsnap_flags_every_signed_url(self):
        for slug in PACKAGES:
            mod = load(folder(slug) / "unsnap.py", f"unsnap_{slug}")
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
        for slug in PACKAGES:
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
            if slug in ("duolingo", "notebooklm"):
                self.assertEqual(res.returncode, 0, (slug, res.stderr))
                self.assertEqual(json.loads((out / "home.json").read_text())["url"], "https://x.example/A User")
            else:
                self.assertIn("LEAK", res.stderr, slug)
                self.assertFalse((out / "home.html").exists(), slug)

    def test_unsnap_meets_accented_names_in_the_metadata(self):
        redact = {"replace": [["Jos\u00e9 Doe", "g", "A User"]]}
        for slug in PACKAGES:
            if slug in ("duolingo", "notebooklm"):
                continue   # they rewrite the URL themselves; covered above
            res, out = self.run_unsnap(slug, "<p>hi</p>", {"label": "home", "url": "https://x.example/Jos\u00e9 Doe"}, redact)
            self.assertIn("LEAK", res.stderr, slug)
            self.assertFalse((out / "home.html").exists(), slug)

    def test_measure_scripts_read_a_copy_without_a_title(self):
        # unsnap.py drops the title, so a reader that dereferences it would throw on every new copy.
        for slug in PACKAGES:
            for f in (ROOT / "systems" / slug / "tools" / "capture").rglob("*.mjs"):
                for m in re.finditer(r"\bm\.title\.", f.read_text()):
                    line = f.read_text()[:m.start()].rsplit("\n", 1)[-1]
                    self.assertTrue(line.endswith("m.title ? { title: "), f"{f.relative_to(ROOT)} reads m.title without a guard")

    def test_notebooklm_snapshot_carries_the_safe_url_copy(self):
        kit = (KIT / "safe-url.mjs").read_text()
        body = kit[kit.index("const RESOURCE"):].replace("export function safeUrl", "function safeUrl").rstrip()
        self.assertIn(body, (ROOT / "systems/notebooklm/tools/capture/signed-in/snapshot.js").read_text())
        self.assertEqual((ROOT / "systems/notebooklm/tools/capture/safe-url.mjs").read_text(), kit)


if __name__ == "__main__":
    unittest.main()
