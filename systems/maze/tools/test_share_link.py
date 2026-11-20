"""The sample report's share link stays out of the package.

A share link that grants access is masked like a signed URL (owner's rule, 2026-11-21): the
committed text says app.maze.co/report/[share-link], and the capture scripts read the real link
from MAZE_REPORT_URL. This fails if any text file in the package names a report path again.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT = {".md", ".json", ".html", ".mjs", ".js", ".py", ".tsv", ".txt", ".svg", ".css"}
REPORT_PATH = re.compile(r"app\.maze\.co/report/(?!\[share-link\])[A-Za-z0-9]")


def leaks(root):
    out = []
    for path in sorted(root.rglob("*")):
        if path == Path(__file__).resolve():   # this file's own fixture names a made-up report
            continue
        if path.is_file() and path.suffix in TEXT and "node_modules" not in path.parts:
            if REPORT_PATH.search(path.read_text(encoding="utf-8", errors="replace")):
                out.append(str(path.relative_to(root)))
    return out


class ShareLink(unittest.TestCase):
    def test_no_file_names_the_report_link(self):
        self.assertEqual(leaks(ROOT), [])

    def test_catalog_entry_does_not_name_the_report_link(self):
        # catalog.json holds maze's capture block (routes, gaps), which the gallery builder copies
        # as is, so the placeholder must be the only report path there too.
        catalog = json.loads((ROOT.parent.parent / "catalog.json").read_text(encoding="utf-8"))
        entry = next(s for s in catalog["systems"] if s.get("slug") == "maze")
        text = json.dumps(entry, ensure_ascii=False)
        self.assertIsNone(REPORT_PATH.search(text))
        self.assertIn("app.maze.co/report/[share-link]", text)

    def test_a_named_report_link_is_found(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "a.json").write_text('{"url": "https://app.maze.co/report/Some-Test/abc123/intro"}')
            Path(tmp, "b.md").write_text("the report at `app.maze.co/report/[share-link]`")
            self.assertEqual(leaks(Path(tmp)), ["a.json"])

    def test_capture_writes_mask_the_link(self):
        # The real link is only used to navigate: both files that record page URLs pass their
        # text through lib.mjs's maskReport, which puts the placeholder back before writing.
        capture = ROOT / "tools" / "capture"
        lib = (capture / "public" / "lib.mjs").read_text()
        self.assertIn("split(REPORT).join(REPORT_PLACEHOLDER)", lib)
        self.assertIn("app.maze.co/report/[share-link]", lib)
        for script in (capture / "vars.mjs", capture / "public" / "measure.mjs"):
            writes = [l for l in script.read_text().splitlines() if "writeFileSync(" in l]
            self.assertTrue(writes, script.name)
            for line in writes:
                with self.subTest(script=script.name):
                    self.assertIn("maskReport(", line)

    def test_capture_scripts_read_the_link_from_the_environment(self):
        lib = (ROOT / "tools" / "capture" / "public" / "lib.mjs").read_text()
        self.assertIn("process.env.MAZE_REPORT_URL", lib)


if __name__ == "__main__":
    unittest.main()
