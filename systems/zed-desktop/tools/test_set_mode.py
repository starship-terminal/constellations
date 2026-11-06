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

    def test_write_keeps_the_file_mode(self):
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d) / "settings.json"
            p.write_text(SETTINGS)
            p.chmod(0o640)
            set_mode.write(p, set_mode.edit(SETTINGS, "light"))
            self.assertEqual(p.stat().st_mode & 0o777, 0o640)

    def test_a_symlinked_settings_file_stays_a_link(self):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / "dotfiles").mkdir(); (d / "zed").mkdir()
            real = d / "dotfiles" / "settings.json"
            real.write_text(SETTINGS)
            link = d / "zed" / "settings.json"
            link.symlink_to(real)
            set_mode.write(link, set_mode.edit(SETTINGS, "light"))
            self.assertTrue(link.is_symlink())
            self.assertIn('"mode": "light"', real.read_text())
            self.assertEqual((d / "zed" / "settings.json.bak").read_text(), SETTINGS)
            self.assertEqual(sorted(x.name for x in (d / "dotfiles").iterdir()), ["settings.json"])

    def test_a_failed_replace_leaves_the_file_and_no_temp(self):
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d) / "settings.json"
            p.write_text(SETTINGS)
            saved = set_mode.os.replace

            def boom(src, dst):
                raise OSError("disk full")
            set_mode.os.replace = boom
            try:
                with self.assertRaises(OSError):
                    set_mode.write(p, set_mode.edit(SETTINGS, "light"))
            finally:
                set_mode.os.replace = saved
            self.assertEqual(p.read_text(), SETTINGS)
            self.assertEqual((pathlib.Path(d) / "settings.json.bak").read_text(), SETTINGS)
            self.assertEqual(sorted(x.name for x in pathlib.Path(d).iterdir()), ["settings.json", "settings.json.bak"])


if __name__ == "__main__":
    unittest.main()
