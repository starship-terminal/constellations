"""measure.mjs merges into the committed components file. A state kept from an earlier run keeps
its own date, and _meta.captured keeps the earlier date until a reading succeeds, so a rerun that
fails throughout never redates old readings. Runs capture/merge-dates.mjs through node; skipped
without node."""
import json
import pathlib
import shutil
import subprocess
import unittest

CAPTURE = pathlib.Path(__file__).resolve().parent / "capture"
NODE = shutil.which("node")


@unittest.skipUnless(NODE, "needs node")
class MergeDatesTest(unittest.TestCase):
    def test_kept_states_keep_their_date(self):
        script = f"""
import {{ datePrior }} from {json.dumps((CAPTURE / "merge-dates.mjs").as_uri())};
const c = {{ 'nav-cta': {{ states: {{ default: {{ style: {{}} }}, hover: {{ style: {{}}, read: '2026-10-01' }} }} }} }};
datePrior(c, '2026-11-18');
console.log(JSON.stringify(c));
"""
        run = subprocess.run([NODE, "--input-type=module", "-e", script], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        states = json.loads(run.stdout)["nav-cta"]["states"]
        self.assertEqual(states["default"]["read"], "2026-11-18")
        self.assertEqual(states["hover"]["read"], "2026-10-01")

    def test_captured_moves_only_on_a_reading(self):
        src = (CAPTURE / "public" / "measure.mjs").read_text()
        # The run starts from the earlier date and advances it only where a state was read.
        self.assertIn("captured: priorCaptured || RUN, lastAttempt: RUN", src)
        self.assertNotIn("captured: new Date()", src)
        read_at = src.index("read: RUN };\n    out._meta.captured = RUN;")
        self.assertGreater(read_at, src.index("async function measure("))
        self.assertIn("recaptureRun: RUN", src)


if __name__ == "__main__":
    unittest.main()
