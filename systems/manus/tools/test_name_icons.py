"""capture/name_icons.py renames every icon or none: a clash leaves icons/ and INDEX.tsv as they were."""
import contextlib
import importlib.util
import io
import pathlib
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("name_icons", HERE / "capture" / "name_icons.py")
name_icons = importlib.util.module_from_spec(spec)
spec.loader.exec_module(name_icons)

HEAD = "file\tname\thash\ta\tb\tc\td\tcount\trole\tnote"


def row(h):
    return f"icon-{h}.svg\ticon-{h}\t{h}\t1\t1\t1\t1\t1\tx\tunnamed fallback"


class NameIcons(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = pathlib.Path(self.tmp.name)
        self.icons = self.dir / "icons"
        self.icons.mkdir()
        self.names = self.dir / "icon-names.tsv"

    def setup(self, hashes, names, extra=()):
        (self.icons / "INDEX.tsv").write_text("\n".join([HEAD] + [row(h) for h in hashes]) + "\n")
        for h in hashes:
            (self.icons / f"icon-{h}.svg").write_text(h)
        for f in extra:
            (self.icons / f).write_text("x")
        self.names.write_text("hash\tname\n" + "".join(f"{h}\t{n}\n" for h, n in names.items()))

    def state(self):
        return sorted(p.name for p in self.icons.iterdir()), (self.icons / "INDEX.tsv").read_text()

    def run_main(self):
        with contextlib.redirect_stdout(io.StringIO()):
            name_icons.main(self.icons, self.names)

    def assert_refused(self):
        before = self.state()
        with self.assertRaises(SystemExit):
            self.run_main()
        self.assertEqual(self.state(), before)

    def test_existing_target_after_a_valid_move(self):
        self.setup(["aaaa", "bbbb"], {"aaaa": "arrow", "bbbb": "close"}, extra=["close.svg"])
        self.assert_refused()

    def test_two_hashes_one_name(self):
        self.setup(["aaaa", "bbbb"], {"aaaa": "arrow", "bbbb": "arrow"})
        self.assert_refused()

    def test_missing_source_after_a_valid_move(self):
        self.setup(["aaaa", "bbbb"], {"aaaa": "arrow", "bbbb": "close"})
        (self.icons / "icon-bbbb.svg").unlink()
        self.assert_refused()

    def test_success_then_rerun_changes_nothing(self):
        self.setup(["aaaa", "bbbb"], {"aaaa": "arrow", "bbbb": "close"})
        self.run_main()
        files, index = self.state()
        self.assertEqual(files, ["INDEX.tsv", "arrow.svg", "close.svg"])
        self.assertIn("arrow.svg\tarrow\taaaa", index)
        self.assertIn("named by role on 2026-10-17", index)
        self.run_main()
        self.assertEqual(self.state(), (files, index))


if __name__ == "__main__":
    unittest.main()
