"""tokens.json is what the builder writes, and motion values DTCG cannot carry are listed."""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_untokenised_easings_are_listed(self):
        listed = json.loads(build_tokens.TEXT)["core"]["$extensions"]["notTokenised"]
        values = {x["value"] for x in listed}
        self.assertIn("steps(12, end)", values)


class CaptureDates(unittest.TestCase):
    MEASURE = pathlib.Path(__file__).resolve().parent / "capture" / "public" / "measure.mjs"

    def test_measure_merge_dates(self):
        """capture/public/test_dates.mjs: only a successful read moves the dates (needs node)."""
        import shutil
        import subprocess
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        test = self.MEASURE.with_name("test_dates.mjs")
        out = subprocess.run([node, "--test", str(test)], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout[-2000:] + out.stderr[-2000:])

    def test_measure_dates_only_through_mark_read(self):
        src = self.MEASURE.read_text()
        self.assertNotIn("out._meta.read = run", src)
        comp = src[src.index("function comp("):src.index("async function measure(")]
        self.assertNotRegex(comp, r"\{ page: current, run\b")
        self.assertIn("markRead(out, c, state,", src)


if __name__ == "__main__":
    unittest.main()
