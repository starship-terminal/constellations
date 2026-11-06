"""capture/set_mode.py changes only theme.mode, refuses anything else without touching the file, and keeps a
backup. Works on a temporary settings file, never the owner's."""
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "capture"))
import set_mode  # noqa: E402

SETTINGS = """// Zed settings
{
  "theme": { "mode": "dark", "light": "One Light", "dark": "One Dark" },
  "ui_font_size": 16,
}
"""


class SetModeTest(unittest.TestCase):
    def test_edit_changes_only_the_mode(self):
        out = set_mode.edit(SETTINGS, "light")
        self.assertEqual(out, SETTINGS.replace('"mode": "dark"', '"mode": "light"'))

    def test_refusals_are_explicit(self):
        for text, mode in ((SETTINGS, "sepia"), ("{}", "light"), ('{"theme": {"light": "x"}}', "light"), ("{", "light")):
            with self.assertRaises(SystemExit):
                set_mode.edit(text, mode)

    def test_write_keeps_a_backup_and_leaves_no_temp(self):
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d) / "settings.json"
            p.write_text(SETTINGS)
            set_mode.write(p, set_mode.edit(SETTINGS, "light"))
            self.assertIn('"mode": "light"', p.read_text())
            self.assertEqual((pathlib.Path(d) / "settings.json.bak").read_text(), SETTINGS)
            self.assertEqual(sorted(x.name for x in pathlib.Path(d).iterdir()), ["settings.json", "settings.json.bak"])


if __name__ == "__main__":
    unittest.main()
