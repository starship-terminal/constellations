"""Tests for the repository's .gitignore. Run with `make test`."""
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def ignored(path: str) -> bool:
    """True when the repository's .gitignore ignores path, tracked or not."""
    run = subprocess.run(["git", "check-ignore", "-q", "--no-index", path], cwd=ROOT)
    if run.returncode not in (0, 1):
        raise RuntimeError(f"git check-ignore failed on {path}")
    return run.returncode == 0


class GitignoreTest(unittest.TestCase):
    def test_full_colour_page_captures_stay_out_of_the_repo(self):
        self.assertTrue(ignored("systems/acme/raw/full/home-default.png"))
        self.assertTrue(ignored("systems/acme/raw/full/home-full.part0.png.capture.json"))

    def test_the_rest_of_raw_is_still_committed(self):
        self.assertFalse(ignored("systems/acme/raw/components-computed.json"))
        self.assertFalse(ignored("systems/acme/raw/fullpage.json"))


if __name__ == "__main__":
    unittest.main()
