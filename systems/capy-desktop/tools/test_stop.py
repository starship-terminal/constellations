"""Runs capture/electron/stop.test.mjs under `node --test`, so `make test` covers the capture's
agent-run stop. Skipped when node is not installed."""
import pathlib
import shutil
import subprocess
import unittest

HERE = pathlib.Path(__file__).resolve().parent / "capture" / "electron"


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class StopTest(unittest.TestCase):
    def test_node_suite(self):
        run = subprocess.run(["node", "--test", "stop.test.mjs"], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)


if __name__ == "__main__":
    unittest.main()
