"""measure.mjs merges into the committed components file; a state kept from an earlier run
must keep its own date. Runs capture/merge-dates.mjs through node; skipped without node."""
import json
import pathlib
import shutil
import subprocess
import unittest

HELPER = pathlib.Path(__file__).resolve().parent / "capture" / "merge-dates.mjs"
MEASURE = pathlib.Path(__file__).resolve().parent / "capture" / "public" / "measure.mjs"
NODE = shutil.which("node")


@unittest.skipUnless(NODE, "needs node")
class MergeDatesTest(unittest.TestCase):
    def test_kept_states_keep_their_date(self):
        script = f"""
import {{ datePrior }} from {json.dumps(HELPER.as_uri())};
const c = {{ 'nav-shop': {{ default: {{ style: {{}} }}, hover: {{ style: {{}}, read: '2026-10-01' }} }} }};
datePrior(c, '2026-11-18');
console.log(JSON.stringify(c));
"""
        run = subprocess.run([NODE, "--input-type=module", "-e", script], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        states = json.loads(run.stdout)["nav-shop"]
        self.assertEqual(states["default"]["read"], "2026-11-18")
        self.assertEqual(states["hover"]["read"], "2026-10-01")

    def test_measure_dates_each_new_state(self):
        src = MEASURE.read_text()
        self.assertIn("datePrior(", src)
        self.assertIn("read: RUN }", src)
        self.assertIn("recaptureRun: RUN", src)


if __name__ == "__main__":
    unittest.main()
