"""capture/rename_parts.py renames a part in its shot and in that shot's per-part state shots, screenshots
included, and changes nothing on a second run. Works on a temporary package."""
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "capture"))
import rename_parts  # noqa: E402


class RenameTest(unittest.TestCase):
    def test_state_shots_are_renamed_with_their_part(self):
        with tempfile.TemporaryDirectory() as d:
            pkg = pathlib.Path(d)
            (pkg / "raw").mkdir()
            caps = {
                "panel": {"state": "default", "file": "dark/panel.png", "parts": {"old-part": {}, "other": {}}},
                "panel-old-part-hover": {"state": "hover", "file": "dark/panel-old-part-hover.png", "parts": {"old-part": {}}},
                "elsewhere": {"state": "default", "file": "dark/elsewhere.png", "parts": {"old-part": {}}},
            }
            for theme in ("dark", "light"):
                (pkg / "raw" / f"components.{theme}.json").write_text(json.dumps(caps))
                (pkg / "screenshots" / theme).mkdir(parents=True)
                (pkg / "screenshots" / theme / "panel-old-part-hover.png").write_bytes(b"png")
            saved = rename_parts.PKG, rename_parts.RENAMES
            rename_parts.PKG, rename_parts.RENAMES = pkg, {("panel", "old-part"): "new-part"}
            try:
                rename_parts.main()
                first = (pkg / "raw" / "components.dark.json").read_text()
                rename_parts.main()
            finally:
                rename_parts.PKG, rename_parts.RENAMES = saved
            out = json.loads(first)
            self.assertEqual(sorted(out), ["elsewhere", "panel", "panel-new-part-hover"])
            self.assertEqual(sorted(out["panel"]["parts"]), ["new-part", "other"])
            self.assertEqual(list(out["panel-new-part-hover"]["parts"]), ["new-part"])
            self.assertEqual(out["panel-new-part-hover"]["file"], "dark/panel-new-part-hover.png")
            self.assertEqual(list(out["elsewhere"]["parts"]), ["old-part"])
            self.assertTrue((pkg / "screenshots" / "dark" / "panel-new-part-hover.png").exists())
            self.assertEqual((pkg / "raw" / "components.dark.json").read_text(), first)


if __name__ == "__main__":
    unittest.main()
