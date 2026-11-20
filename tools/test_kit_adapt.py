"""Tests for the kit's adapt guard: every product-specific file in tools/kit is one product's example
(Claude, ChatGPT, Gauth, Grok Bot) and stops when run as copied, until its ADAPTED_FOR line names the
new product. Run with `make test`; the JavaScript files are skipped without node."""
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
KIT = HERE / "kit"
NODE = shutil.which("node")

# Every file that holds one product's values, selectors or prose. A file added to the kit that is
# product-specific belongs here; GENERIC lists the ones that are product-free on purpose.
PRODUCT_FILES = [
    "build/build_tokens.py", "build/build_components_md.py", "build/build_components_md.public.py",
    "capture/public/lib.mjs", "capture/public/measure.mjs", "capture/public/public.mjs", "capture/public/build-measurements.mjs",
    "capture/icons.mjs", "capture/layout.mjs", "capture/vars.mjs",
    "capture/signed-in/measure.mjs", "capture/signed-in/lib.mjs", "capture/signed-in/render.mjs", "capture/signed-in/build-measurements.mjs",
    "native/measure.py", "native/build_tokens.py", "native/build_style_guide.py", "native/build_components_md.py",
]
TEMPLATE = "build/style-guide.template.html"
GENERIC = {
    "build/build_style_guide.py", "build/motion.py",
    "capture/css-colour.mjs", "capture/motion.mjs", "capture/motion-probe.mjs", "capture/quantize.py", "capture/safe-url.mjs",
    "capture/screenshot.mjs", "capture/readings.mjs", "capture/electron/shot.mjs", "capture/public/pin.mjs",
    "capture/no-query.mjs", "capture/crop.mjs",
    "capture/signed-in/snapshot.js", "capture/signed-in/unsnap.py", "capture/signed-in/render-all.sh",
    "capture/native/sample.py", "capture/native/shot.sh", "capture/native/winid.swift",
    "native/crops.py", "native/quantize.py",
}
GUARD_PY = re.compile(r"^ *ADAPTED_FOR = None$", re.M)
GUARD_JS = re.compile(r"^const ADAPTED_FOR = null;$", re.M)


def run(path, env=None):
    cmd = [NODE if path.suffix == ".mjs" else sys.executable, str(path)]
    base = {k: v for k, v in os.environ.items() if k not in ("KIT_EXAMPLE", "PLAYWRIGHT")}
    with tempfile.TemporaryDirectory() as d:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=60, cwd=d, env={**base, **(env or {})})


class AdaptGuard(unittest.TestCase):
    def test_every_kit_script_is_either_guarded_or_listed_as_generic(self):
        scripts = {str(p.relative_to(KIT)) for p in KIT.rglob("*") if p.suffix in (".py", ".mjs", ".js", ".sh", ".swift")
                   and not p.name.startswith("test_")}
        self.assertEqual(scripts - set(PRODUCT_FILES) - GENERIC, set(), "a new kit script: guard it or list it as generic")
        self.assertEqual(set(PRODUCT_FILES) - scripts, set())
        for rel in PRODUCT_FILES:
            src = (KIT / rel).read_text()
            self.assertEqual(len((GUARD_JS if rel.endswith(".mjs") else GUARD_PY).findall(src)), 1, rel)
            self.assertIn("PRODUCT (adapt)", src, rel)
        for rel in GENERIC - {"build/build_style_guide.py"}:   # the style guide builder reads the template's line
            if (KIT / rel).exists():
                self.assertNotIn("ADAPTED_FOR", (KIT / rel).read_text(), rel)

    def test_python_examples_stop_until_adapted(self):
        for rel in (r for r in PRODUCT_FILES if r.endswith(".py")):
            # in a package, native/measure.py finds sample.py under tools/capture/native; in the kit it sits apart
            res = run(KIT / rel, {"PYTHONPATH": str(KIT / "capture/native")})
            self.assertNotEqual(res.returncode, 0, rel)
            self.assertIn("not adapted", res.stderr, rel)
            self.assertIn("ADAPTED_FOR", res.stderr, rel)

    @unittest.skipIf(NODE is None, "node is not on PATH")
    def test_javascript_examples_stop_until_adapted(self):
        for rel in (r for r in PRODUCT_FILES if r.endswith(".mjs")):
            res = run(KIT / rel)
            self.assertEqual(res.returncode, 2, (rel, res.stderr[-500:]))
            self.assertIn("not adapted", res.stderr, rel)

    def test_an_adapted_copy_runs(self):
        # The kit's public components builder on an empty invented package, with ADAPTED_FOR set.
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            for sub in ("tools", "raw", "screenshots", "components/crops", "icons"):
                (pkg / sub).mkdir(parents=True)
            src = (KIT / "build/build_components_md.public.py").read_text()
            (pkg / "tools/build_components_md.py").write_text(GUARD_PY.sub('ADAPTED_FOR = "Example"', src))
            (pkg / "raw/components-computed.json").write_text(json.dumps({"_meta": {"read": "2026-01-02"}, "components": {}}))
            (pkg / "raw/layout.json").write_text("{}")
            (pkg / "tokens.json").write_text(json.dumps({"core": {"palette": {}}}))
            (pkg / "icons/INDEX.tsv").write_text("file\tname\n")
            res = run(pkg / "tools/build_components_md.py")
            self.assertEqual(res.returncode, 0, res.stderr[-1000:])
            self.assertTrue((pkg / "components.md").is_file())


class CopyRecipe(unittest.TestCase):
    def test_every_file_the_readme_copies_exists_and_no_route_copies_the_whole_kit(self):
        text = (KIT / "README.md").read_text()
        cps = [ln.split()[1:-1] for block in re.findall(r"```bash\n(.*?)```", text, re.S) for ln in block.splitlines()
               if ln.startswith("cp ")]
        self.assertTrue(cps)
        for args in cps:
            for a in (x for x in args if not x.startswith("-")):
                m = re.fullmatch(r"(.*)\{(.+)\}(.*)", a)
                for path in ([m.group(1) + part + m.group(3) for part in m.group(2).split(",")] if m else [a]):
                    if "*" in path:
                        self.assertTrue(list(HERE.parent.glob(path)), path)
                    else:
                        self.assertTrue((HERE.parent / path).exists(), path)
                self.assertNotIn(a.rstrip("/"), ("tools/kit/capture", "tools/kit/build/*"), "copy one route, not the whole kit")


    def test_each_route_copies_every_kit_file_its_scripts_import(self):
        # A route's scripts import shared helpers (../safe-url.mjs, ../crop.mjs, ../no-query.mjs, ...); a helper
        # the recipe leaves out stops the copied script with ERR_MODULE_NOT_FOUND before capture starts.
        block = re.search(r"```bash\n(.*?)```", (KIT / "README.md").read_text(), re.S).group(1)
        shared_part, routes_part = block.split("# then one of:", 1)

        def copied(lines):
            out = set()
            for ln in lines.splitlines():
                if not ln.startswith("cp "):
                    continue
                args = [a for a in ln.split()[1:-1] if not a.startswith("-")]
                for a in args:
                    m = re.fullmatch(r"(.*)\{(.+)\}(.*)", a)
                    for path in ([m.group(1) + part + m.group(3) for part in m.group(2).split(",")] if m else [a]):
                        full = HERE.parent / path
                        out |= {q.resolve() for q in full.rglob("*") if q.is_file()} if full.is_dir() else {full.resolve()}
            return out

        shared = copied(shared_part)
        routes = re.split(r"^# (.+)$", routes_part, flags=re.M)[1:]
        self.assertTrue(routes)
        for name, lines in zip(routes[::2], routes[1::2]):
            files = shared | copied(lines)
            for f in sorted(x for x in files if x.suffix == ".mjs" and not x.name.startswith("test_")):
                for rel in re.findall(r"^import\b[^'\"]*from\s+['\"](\.{1,2}/[^'\"]+)['\"]", f.read_text(), re.M):
                    dep = (f.parent / rel).resolve()
                    with self.subTest(route=name, script=f.name, imports=rel):
                        self.assertIn(dep, files)


class TemplateGuard(unittest.TestCase):
    def guide(self, template):
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d)
            (pkg / "tools").mkdir()
            shutil.copy(KIT / "build/build_style_guide.py", pkg / "tools/build_style_guide.py")
            (pkg / "tools/style-guide.template.html").write_text(template)
            (pkg / "tokens.json").write_text(json.dumps({"core": {"radius": {"sm": {"$type": "dimension", "$value": "4px", "$extensions": {"source": "test"}}}}, "light": {}}))
            res = run(pkg / "tools/build_style_guide.py")
            out = (pkg / "style-guide.html").read_text() if (pkg / "style-guide.html").exists() else None
            return res, out

    def test_the_kit_template_stops_the_guide_until_adapted(self):
        tpl = (KIT / TEMPLATE).read_text()
        self.assertEqual(len(re.findall(r"^<!-- ADAPTED_FOR: none \|", tpl, re.M)), 1)
        res, out = self.guide(tpl)
        self.assertNotEqual(res.returncode, 0)
        self.assertIn("not adapted", res.stderr)
        self.assertIsNone(out)

    def test_an_adapted_template_renders_without_its_adapted_line(self):
        res, out = self.guide("<!doctype html>\n<!-- ADAPTED_FOR: Example | notes -->\n<style>/*CORE*/</style>\n")
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertNotIn("ADAPTED_FOR", out)
        self.assertIn("--radius-sm", out)
        # a package template from before the guard (no ADAPTED_FOR line) renders as it did
        res, out = self.guide("<!doctype html>\n<style>/*CORE*/</style>\n")
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertTrue(out.startswith("<!doctype html>\n<style>"))


if __name__ == "__main__":
    unittest.main()
