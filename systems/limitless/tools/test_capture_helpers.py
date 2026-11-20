"""icons.mjs replaces icons/ only after the whole new set was written (capture/replace-set.mjs). Runs the .mjs helpers
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



class CaptureDatesTest(unittest.TestCase):
    """measure.mjs merges into the committed file: the run date moves only when a state is read,
    and a failed re-read keeps the earlier reading and its date."""

    def test_capture_date_moves_only_on_a_reading(self):
        src = (CAPTURE / "public" / "measure.mjs").read_text()
        self.assertIn("captured: prevDate || TODAY, lastAttempt: TODAY", src)
        ok = src.index("c.states[state] = { ...s, crop: file, via, read: TODAY };")
        self.assertLess(ok, src.index("out._meta.captured = TODAY;"))
        self.assertLess(ok, src.index("c.read = TODAY;"))
        self.assertEqual(src.count("recaptureError: msg, recaptureRun: TODAY"), 2)

    def test_backfill_dates_states_and_success_clears_missed(self):
        src = (CAPTURE / "public" / "measure.mjs").read_text()
        backfill = src.index("for (const st of Object.values(c.states || {})) if (st && typeof st === 'object' && !st.read) st.read = prevDate;")
        self.assertLess(backfill, src.index("const out = {"))
        ok = src.index("c.states[state] = { ...s, crop: file, via, read: TODAY };")
        self.assertLess(ok, src.index("delete c.recaptureMissed;"))


if __name__ == "__main__":
    unittest.main()
