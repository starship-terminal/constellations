"""capture/drive.py finds the Settings window in a `wins Zed` listing before any Settings click. Reads a
sample listing only; nothing is driven."""
import pathlib
import sys
import unittest

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


if __name__ == "__main__":
    unittest.main()
