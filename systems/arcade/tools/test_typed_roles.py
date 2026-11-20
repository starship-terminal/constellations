"""The committed outputs must rebuild from the package's inputs, and the typed roles must follow their readings.

The builders run on a temporary copy of the package, so nothing committed is rewritten.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ['build_component_tokens.py', 'build_tokens.py']
OUTPUTS = ['raw/component-tokens.json', 'tokens.json']


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.copy = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, cls.copy, ignore=shutil.ignore_patterns("__pycache__"))
        # Remove the committed outputs from the copy first, so a builder that
        # writes nothing cannot pass by leaving the committed file in place.
        for out in OUTPUTS:
            (cls.copy / out).unlink()
        for b in BUILDERS:
            subprocess.run([sys.executable, str(cls.copy / "tools" / b)], check=True, capture_output=True, cwd=cls.copy)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for out in OUTPUTS:
            with self.subTest(out=out):
                self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
                self.assertEqual((self.copy / out).read_text(), (PKG / out).read_text())


# Each role below is read from raw/components-computed.json. Changing those
# readings must change the built token, and a missing, stale or disagreeing
# reading must stop the build instead of falling back to a typed value.
CASES = [
    dict(name="surface", reads=lambda C: [("plan-card-pro", "default"), ("field-text", "default")], prop="backgroundColor", sentinel="rgb(18, 52, 87)", expect='"#123457"'),
    dict(name="muted", reads=lambda C: [("nav-link", "default")], prop="color", sentinel="rgb(18, 52, 87)", expect='"#123457"'),
    dict(name="surface-hover", reads=lambda C: [("nav-link", "hover"), ("nav-login", "hover")], prop="backgroundColor", sentinel="rgb(18, 52, 87)", expect='"#123457"'),
    dict(name="ink-hover", reads=lambda C: [("nav-signup", "hover"), ("plan-cta-pro", "hover")], prop="backgroundColor", sentinel="rgb(18, 52, 87)", expect='"#123457"'),
    dict(name="focus-ring", reads=lambda C: [("nav-link", "focus-visible"), ("nav-signup", "focus-visible"), ("cta-large", "focus-visible")], prop="outlineColor", sentinel="rgb(18, 52, 87)", expect='"#123457"'),
    dict(name="chip-text", reads=lambda C: [("suggestion-chip", "default")], prop="color", sentinel="rgb(18, 52, 87)", expect='"#123457"'),
    dict(name="footer-muted", reads=lambda C: [("footer-link", "default")], prop="color", sentinel="rgb(18, 52, 87)", expect='"#123457"'),
]

RAW_JSON = "raw/components-computed.json"
OUT_JSON = "raw/component-tokens.json"
SKIP = shutil.ignore_patterns("__pycache__", "screenshots", "crops", "boards", "icons", "*.png", "*.jpg", "*.webp")


def _build(mutate):
    with tempfile.TemporaryDirectory() as tmp:
        copy = pathlib.Path(tmp) / "pkg"
        shutil.copytree(PKG, copy, ignore=SKIP)
        raw = json.loads((copy / RAW_JSON).read_text())
        mutate(raw["components"])
        (copy / RAW_JSON).write_text(json.dumps(raw))
        r = subprocess.run([sys.executable, str(copy / "tools" / "build_component_tokens.py")],
                           capture_output=True, text=True, cwd=copy)
        out = (copy / OUT_JSON).read_text() if r.returncode == 0 else ""
        return r.returncode, out


def _set(reads, prop, value):
    def mutate(C):
        for comp, state in reads(C):
            C[comp]["states"][state]["style"][prop] = value
    return mutate


def _flag(reads, flag):
    def mutate(C):
        comp = reads(C)[0][0]
        C[comp][flag] = True
    return mutate


class ReadingsDriveRolesTest(unittest.TestCase):
    def test_roles_follow_their_readings(self):
        committed = (PKG / OUT_JSON).read_text()
        for c in CASES:
            with self.subTest(role=c["name"]):
                self.assertNotIn(c["expect"], committed)
                code, out = _build(_set(c["reads"], c["prop"], c["sentinel"]))
                self.assertEqual(code, 0)
                self.assertIn(c["expect"], out)

    def test_bad_readings_stop_the_build(self):
        for c in CASES:
            for flag in c.get("flags", ("missing", "recaptureMissed")):
                with self.subTest(role=c["name"], flag=flag):
                    code, _ = _build(_flag(c["reads"], flag))
                    self.assertNotEqual(code, 0)
            if len(c["reads"](json.loads((PKG / RAW_JSON).read_text())["components"])) > 1:
                with self.subTest(role=c["name"], case="disagree"):
                    def one(C, c=c):
                        comp, state = c["reads"](C)[0]
                        C[comp]["states"][state]["style"][c["prop"]] = c["sentinel"]
                    code, _ = _build(one)
                    self.assertNotEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
