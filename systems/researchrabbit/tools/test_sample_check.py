"""sample_check: a sampled colour must match its screenshot pixel within the tolerance."""
import pathlib
import tempfile
import unittest

from PIL import Image

from sample_check import check_samples

norm = str.lower
TOKENS = {"palette.grey.1": "#dde0e4"}
resolve = lambda v: TOKENS.get(v[1:-1], v) if v.startswith("{") else v


class SampleCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = pathlib.Path(self.tmp.name)
        Image.new("RGB", (4, 4), (0xdf, 0xe1, 0xe4)).save(self.root / "shot.png")

    def run_one(self, value, tolerance=3):
        return check_samples([("t", value, "shot.png", (1, 1))], self.root, resolve, norm, tolerance)

    def test_exact_match(self):
        self.assertEqual(self.run_one("#dfe1e4", tolerance=0), 1)

    def test_tolerance_boundary(self):
        self.assertEqual(self.run_one("#e2e1e4"), 1)          # 3 off: passes
        with self.assertRaises(ValueError):
            self.run_one("#e3e1e4")                           # 4 off: fails

    def test_mismatch(self):
        with self.assertRaisesRegex(ValueError, "is #dfe1e4, not #000000"):
            self.run_one("#000000")

    def test_alias_resolves_before_comparing(self):
        self.assertEqual(self.run_one("{palette.grey.1}"), 1)  # #dde0e4, 2 off

    def test_lfs_pointer_is_skipped(self):
        (self.root / "shot.png").write_text("version https://git-lfs.github.com/spec/v1\n")
        self.assertEqual(self.run_one("#000000"), 0)


if __name__ == "__main__":
    unittest.main()
