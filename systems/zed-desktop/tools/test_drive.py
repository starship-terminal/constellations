"""capture/drive.py finds the Settings window in a `wins Zed` listing before any Settings click, refuses a
main-window click while Settings is in front, and refuses a file-tree click when an extra scratch file moves
todo.txt's row. Reads sample listings and a temporary folder only; nothing is driven."""
import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "capture"))
argv, sys.argv = sys.argv, ["drive.py", "dark"]
try:
    import drive  # noqa: E402
finally:
    sys.argv = argv

LISTING = """906 layer 3 0.0 0.0 10.0 10.0 | Settings
905 layer 0 306.0 132.0 1100.0 800.0 | Settings
812 layer 0 0.0 33.0 1728.0 1084.0 | scratch — main.py
frontmost: Zed
"""


class SettingsOriginTest(unittest.TestCase):
    def test_reads_the_frontmost_settings_window_past_other_layers(self):
        self.assertEqual(drive.settings_origin(LISTING), (306, 132))

    def test_a_layer_3_window_alone_is_not_settings(self):
        self.assertIsNone(drive.settings_origin("906 layer 3 306.0 132.0 10.0 10.0 | Settings\n"))

    def test_settings_behind_the_editor_is_refused(self):
        covered = "812 layer 0 0.0 33.0 1728.0 1084.0 | scratch — main.py\n905 layer 0 306.0 132.0 1100.0 800.0 | Settings\n"
        self.assertIsNone(drive.settings_origin(covered))

    def test_no_settings_window(self):
        self.assertIsNone(drive.settings_origin("812 layer 0 0.0 33.0 1728.0 1084.0 | settings.json\nfrontmost: Zed\n"))
        self.assertIsNone(drive.settings_origin(""))


class MouseTest(unittest.TestCase):
    def run_with(self, listing):
        calls = []

        def run(cmd, **kw):
            calls.append(cmd)
            return subprocess.CompletedProcess(cmd, 0, stdout=listing if cmd[0].endswith("wins") else "", stderr="")
        with mock.patch.object(drive, "ensure_front"), mock.patch.object(drive.subprocess, "run", run), \
                mock.patch.object(drive.time, "sleep"):
            drive.mouse("click", 100, 100)
        return calls

    def test_refuses_while_settings_is_in_front(self):
        with self.assertRaises(SystemExit):
            self.run_with(LISTING)

    def test_clicks_when_the_main_window_is_in_front(self):
        main_front = "812 layer 0 0.0 33.0 1728.0 1084.0 | scratch — main.py\n905 layer 0 306.0 132.0 1100.0 800.0 | Settings\n"
        calls = self.run_with(main_front)
        self.assertTrue(calls[-1][0].endswith("mouse"))


class TodoRowTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.scr = pathlib.Path(self.tmp.name)
        (self.scr / "todo.txt").write_text("")
        patch = mock.patch.object(drive, "SCR", self.scr)
        patch.start()
        self.addCleanup(patch.stop)

    def tearDown(self):
        self.tmp.cleanup()

    def test_rows(self):
        self.assertEqual(drive.TODO_Y(), 100)
        (self.scr / "hello.txt").write_text("")
        self.assertEqual(drive.TODO_Y(), 126)

    def test_another_hello_file_stops(self):
        (self.scr / "hello.txt").write_text("")
        (self.scr / "hello-light.txt").write_text("")
        with self.assertRaises(SystemExit):
            drive.TODO_Y()


if __name__ == "__main__":
    unittest.main()
