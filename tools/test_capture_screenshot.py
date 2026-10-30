"""Run the kit's browser-free Node screenshot contract tests in make test."""
import pathlib
import shutil
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


class ScreenshotMetadataTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the web capture kit")
    def test_capture_metadata_contract(self):
        result = subprocess.run(
            ["node", "--test", "tools/kit/capture/test_screenshot.mjs"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
