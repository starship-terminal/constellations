"""Tests for how tools/refero/fetch.py and classify.py write the refero stores:
atomic files, a renamed style's folder, the LFS pointer guard and the catalog
refresh after labelling. No network: page fetches and the API are patched.
Run with `make test`."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS / "refero"))
import classify  # noqa: E402
import fetch  # noqa: E402

RESULT = {"meta": {"url": "https://acme.example", "extractedAt": "2026-01-01"},
          "designSystem": {"theme": "light", "northStar": "Move fast"}}
NO_MEDIA = {"video_url": None, "video_poster_url": None,
            "video_detail_url": None, "video_detail_poster_url": None}
UUID = "00000000-0000-0000-0000-000000000001"


class ReferoTmp(unittest.TestCase):
    """A temporary refero/ that both modules read and write."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.refero = Path(tmp.name) / "refero"
        db = self.refero / "refero.db"
        for mod, attrs in ((fetch, {"REFERO": self.refero, "WORK": self.refero / ".work", "DB": db}),
                           (classify, {"REFERO": self.refero, "DB": db})):
            for name, value in attrs.items():
                patcher = mock.patch.object(mod, name, value)
                patcher.start()
                self.addCleanup(patcher.stop)

    def run_fetch(self, name):
        page = (UUID, f"{fetch.BASE}/style/{UUID}", RESULT, "# DESIGN\n", name, NO_MEDIA)
        with mock.patch.object(fetch, "fetch_sitemap_uuids", return_value=[UUID]), \
             mock.patch.object(fetch, "fetch_one", return_value=page), \
             mock.patch("sys.stdout"):
            fetch.cmd_fetch(SimpleNamespace(force=True, limit=0, workers=1))

    def tmp_files(self):
        return sorted(p.name for p in self.refero.rglob("*.tmp"))


class FetchWritesTest(ReferoTmp):
    def test_a_fetch_writes_the_folder_atomically(self):
        self.run_fetch("Acme")
        self.assertEqual((self.refero / "acme" / "DESIGN.md").read_text(), "# DESIGN\n")
        self.assertEqual(json.loads((self.refero / "acme" / "meta.json").read_text())["slug"], "acme")
        self.assertEqual(self.tmp_files(), [])

    def test_a_renamed_style_moves_its_folder_instead_of_orphaning_it(self):
        self.run_fetch("Acme")
        (self.refero / "acme" / "tokens.json").write_text("{}")  # an export artifact
        self.run_fetch("Acme Labs")
        self.assertFalse((self.refero / "acme").exists())
        self.assertTrue((self.refero / "acme-labs" / "tokens.json").is_file())
        meta = json.loads((self.refero / "acme-labs" / "meta.json").read_text())
        self.assertEqual(meta["slug"], "acme-labs")

    def test_the_catalog_is_written_atomically(self):
        self.run_fetch("Acme")
        with mock.patch("sys.stdout"):
            fetch.cmd_catalog()
        catalog = json.loads((self.refero / "catalog.json").read_text())
        self.assertEqual([s["slug"] for s in catalog["styles"]], ["acme"])
        self.assertEqual(self.tmp_files(), [])


class ClassifyWritesTest(ReferoTmp):
    LABELS = {"product_type": "devtools", "design_style": "minimal", "tags": ["saas"]}

    def test_an_lfs_pointer_db_exits_with_a_clear_message(self):
        self.refero.mkdir(parents=True)
        (self.refero / "refero.db").write_text("version https://git-lfs.github.com/spec/v1\n")
        with self.assertRaises(SystemExit) as raised:
            classify.init_db()
        self.assertIn("Git LFS pointer", str(raised.exception))

    def test_write_meta_inserts_labels_after_theme_atomically(self):
        self.run_fetch("Acme")
        classify.write_meta("acme", self.LABELS)
        meta = json.loads((self.refero / "acme" / "meta.json").read_text())
        keys = list(meta)
        self.assertEqual(keys[keys.index("theme") + 1], "product_type")
        self.assertEqual(meta["tags"], ["saas"])
        self.assertEqual(self.tmp_files(), [])

    def test_a_labelling_run_refreshes_catalog_json(self):
        self.run_fetch("Acme")
        with mock.patch("sys.stdout"):
            fetch.cmd_catalog()
        with mock.patch.object(classify, "call_api", return_value=({"acme": self.LABELS}, [], None)), \
             mock.patch.dict(classify.os.environ, {"ANTHROPIC_API_KEY": "test-key"}), \
             mock.patch.object(sys, "argv", ["classify.py"]), \
             mock.patch("sys.stdout"), mock.patch("sys.stderr"):
            classify.main()
        row = json.loads((self.refero / "catalog.json").read_text())["styles"][0]
        self.assertEqual((row["product_type"], row["design_style"], row["tags"]),
                         ("devtools", "minimal", ["saas"]))


if __name__ == "__main__":
    unittest.main()
