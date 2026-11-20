"""tokens.json and components.md are what the builders write, and marketing values come from the
marketing sheet, not from whichever of the 385 harvested sheets came last."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_marketing_sheet_wins_over_later_sheets(self):
        # The docs and app sheets redeclare these names later in the harvest.
        self.assertEqual(build_tokens.resolved("--color-black"), "#0e0e0e")
        self.assertEqual(build_tokens.resolved("--container-xl"), "1200px")
        self.assertEqual(json.loads(build_tokens.TEXT)["core"]["layout"]["content"]["$value"], "1200px")

    def test_rem_and_short_hex_are_normalised(self):
        self.assertEqual(build_tokens.resolved("--text-xs"), "12px")
        self.assertEqual(build_tokens.resolved("--color-white-2"), "#ffffff")

    def test_a_name_the_marketing_sheet_lacks_fails(self):
        with self.assertRaises(SystemExit):
            build_tokens.resolved("--font-weight-bold")


class Components(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        with tempfile.TemporaryDirectory() as tmp:
            pkg = pathlib.Path(tmp) / "pkg"
            shutil.copytree(ROOT, pkg, ignore=shutil.ignore_patterns("screenshots", "components", "icons", "boards"))
            subprocess.run([sys.executable, str(pkg / "tools" / "build_components_md.py")], check=True, capture_output=True)
            self.assertEqual((pkg / "components.md").read_text(), (ROOT / "components.md").read_text())

    def test_rows_escape_pipes_and_skip_failed_focus(self):
        src = (ROOT / "tools" / "build_components_md.py").read_text()
        # Load only the helpers (the module writes when run as a script).
        ns = {"__name__": "helpers", "__file__": str(ROOT / "tools" / "build_components_md.py")}
        exec(compile(src.split("\nlines = [")[0], "bcm", "exec"), ns)
        row = ns["row"]("hover", {"style": {"fontFamily": "Odd|Face, serif"}, "via": "mouse\nhover"}, None)
        self.assertEqual(row.count(" | "), 4)  # five cells, the pipe in the font name escaped
        self.assertIn("\\|", row)

    def test_gap_links_resolve_from_the_package_root(self):
        text = (ROOT / "components.md").read_text()
        self.assertNotIn("](../", text)
        self.assertIn("## Gaps", text)


class CaptureDates(unittest.TestCase):
    def test_measure_merge_dates(self):
        """capture/public/test_dates.mjs: a partial rerun dates only what it read (needs node)."""
        import shutil
        import subprocess
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        test = pathlib.Path(__file__).resolve().parent / "capture" / "public" / "test_dates.mjs"
        out = subprocess.run([node, "--test", str(test)], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout[-2000:] + out.stderr[-2000:])


if __name__ == "__main__":
    unittest.main()
