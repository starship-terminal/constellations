"""The capture helpers that protect committed evidence: merged readings keep their own dates,
and icons/ is replaced only after the whole new set was written. Runs the .mjs helpers
through node; skipped when node is not installed. Never touches the package's own files."""
import json
import pathlib
import shutil
import subprocess
import tempfile
import unittest

CAPTURE = pathlib.Path(__file__).resolve().parent / "capture"
NODE = shutil.which("node")


def node(script):
    run = subprocess.run([NODE, "--input-type=module", "-e", script], capture_output=True, text=True)
    return run.returncode, run.stdout, run.stderr


@unittest.skipUnless(NODE, "needs node")
class CaptureHelpersTest(unittest.TestCase):
    def test_kept_readings_keep_their_date(self):
        url = (CAPTURE / "merge-dates.mjs").as_uri()
        rc, out, err = node(f"""
import {{ datePrior }} from {json.dumps(url)};
const c = {{ a: {{ states: {{ default: {{ style: {{}} }}, hover: {{ style: {{}}, read: '2026-10-01' }} }} }} }};
datePrior(c, '2026-11-18');
console.log(JSON.stringify(c));
""")
        self.assertEqual(rc, 0, err)
        states = json.loads(out)["a"]["states"]
        self.assertEqual(states["default"]["read"], "2026-11-18")
        self.assertEqual(states["hover"]["read"], "2026-10-01")

    def test_failed_write_leaves_the_old_set(self):
        url = (CAPTURE / "replace-set.mjs").as_uri()
        with tempfile.TemporaryDirectory() as tmp:
            icons = pathlib.Path(tmp) / "icons"
            icons.mkdir()
            (icons / "old.svg").write_text("<svg/>")
            (icons / "INDEX.tsv").write_text("old.svg\n")
            # A name with a missing subfolder makes the scratch write fail part-way.
            rc, _, _ = node(f"""
import {{ replaceSet }} from {json.dumps(url)};
replaceSet({json.dumps(str(icons))}, new Map([['new.svg', '<svg/>'], ['no/such/dir.svg', 'x']]), 'new.svg\\n');
""")
            self.assertNotEqual(rc, 0)
            self.assertEqual(sorted(p.name for p in icons.iterdir()), ["INDEX.tsv", "old.svg"])
            self.assertEqual((icons / "INDEX.tsv").read_text(), "old.svg\n")
            self.assertEqual([p.name for p in pathlib.Path(tmp).iterdir()], ["icons"])

    def test_complete_write_replaces_the_set(self):
        url = (CAPTURE / "replace-set.mjs").as_uri()
        with tempfile.TemporaryDirectory() as tmp:
            icons = pathlib.Path(tmp) / "icons"
            icons.mkdir()
            (icons / "old.svg").write_text("<svg/>")
            rc, _, err = node(f"""
import {{ replaceSet }} from {json.dumps(url)};
replaceSet({json.dumps(str(icons))}, new Map([['new.svg', '<svg id="n"/>']]), 'new.svg\\n');
""")
            self.assertEqual(rc, 0, err)
            self.assertEqual(sorted(p.name for p in icons.iterdir()), ["INDEX.tsv", "new.svg"])
            self.assertEqual((icons / "INDEX.tsv").read_text(), "new.svg\n")


if __name__ == "__main__":
    unittest.main()
