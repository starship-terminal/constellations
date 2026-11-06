"""Run this package's browser-free Node capture tests (screenshot contract, saved readings) in make test."""
import pathlib
import shutil
import subprocess
import unittest

HERE = pathlib.Path(__file__).resolve().parent


class ScreenshotMetadataTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the capture scripts")
    def test_capture_metadata_contract(self):
        result = subprocess.run(["node", "--test", "capture/test_screenshot.mjs"], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for the capture scripts")
    def test_saved_readings_survive_partial_runs(self):
        result = subprocess.run(["node", "--test", "capture/test_readings.mjs"], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
