"""Regressions for token typing, capture setup and privacy acceptance."""
import contextlib
import copy
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image

import build_tokens
import ingest_evidence as ingest


HERE = Path(__file__).resolve().parent.parent


class TokenTypes(unittest.TestCase):
    def test_css_shorthands_remain_evidence_instead_of_dimensions(self):
        path = HERE / "raw/readings/example-dark-desktop.json"
        for prop, value in (("borderRadius", "12px 0px 0px"),
                            ("borderWidth", "0px 0px 1.11111px"),
                            ("padding", "16px 20px")):
            with self.subTest(prop=prop):
                item = build_tokens.measured(path, {"width": 1440, "height": 1000},
                                             {"index": 1, "tag": "TD", "styles": {prop: value}}, prop)
                self.assertNotIn("$value", item)
                self.assertEqual(item["$extensions"]["notTokenised"]["value"], value)
                self.assertIn("example-dark-desktop.json", item["$extensions"]["source"])

    def test_a_single_length_is_a_dimension(self):
        item = build_tokens.measured(HERE / "raw/readings/example-dark-desktop.json",
                                     {"width": 1440, "height": 1000},
                                     {"index": 1, "tag": "TD", "styles": {"padding": "16px"}}, "padding")
        self.assertEqual((item["$type"], item["$value"]), ("dimension", "16px"))


class PrivacyAcceptance(unittest.TestCase):
    def test_sanitization_removes_private_text_and_preserves_measurements(self):
        measured = {"index": 7, "className": "text-secondary", "rect": {"x": 12, "width": 48},
                    "styles": {"color": "rgb(27, 27, 31)", "padding": "16px 20px"}}
        raw = {"variables": {"--brand": "#6c47ff"}, "width": 1440, "height": 1000,
               "elements": [{**measured, "name": "person@example.test sk_test_fixtureSecret123",
                             "details": ["user_fixture1234567890123456", "local@example"]}]}
        before = copy.deepcopy(raw)
        clean = ingest.sanitize(raw)
        self.assertEqual(raw, before, "sanitization must not mutate the source")
        self.assertEqual(clean["variables"], raw["variables"])
        self.assertEqual({key: clean["elements"][0][key] for key in measured}, measured)
        text = json.dumps(clean)
        self.assertNotIn("person@example", text)
        self.assertNotIn("sk_test_fixture", text)
        self.assertNotIn("user_fixture", text)
        self.assertNotIn("local@example", text)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source, self.package, self.repo = (self.root / name for name in ("source", "package", "repo"))
        (self.source / "raw-shots").mkdir(parents=True)
        self.rules = self.repo / "tools/redact-rules/clerk.json"
        self.rules.parent.mkdir(parents=True)
        self.rules.write_text('{"families": []}')
        self.shot = self.source / "raw-shots/dialog.png"
        Image.new("RGB", (64, 64), "white").save(self.shot)
        self.target = self.package / "screenshots/dialog.png"

    def run_ingest(self, reads):
        with patch.object(ingest, "REPO", self.repo), patch.object(ingest, "image_reads", side_effect=reads), contextlib.redirect_stdout(io.StringIO()):
            ingest.ingest(self.source, self.package)

    def test_rejection_matches_the_image_hash_not_only_its_filename(self):
        rejected_hash = ingest.sha256(self.shot)
        self.rules.write_text(json.dumps({"families": [], "excludeSources": [
            {"file": "dialog.png", "sha256": rejected_hash, "reason": "clipped fixture"}]}))
        self.target.parent.mkdir(parents=True)
        self.target.write_bytes(b"stale accepted image")
        self.run_ingest([])
        manifest_path = self.package / "raw/readings/_ingest.json"
        manifest = json.loads(manifest_path.read_text())
        self.assertFalse(self.target.exists())
        self.assertEqual(manifest["images"], [])
        self.assertEqual(manifest["rejectedImages"][0]["sha256"], rejected_hash)
        Image.new("RGB", (64, 64), "black").save(self.shot)
        self.run_ingest([[[]], [[]]])
        manifest = json.loads(manifest_path.read_text())
        self.assertTrue(self.target.is_file())
        self.assertEqual(manifest["rejectedImages"], [])
        self.assertNotEqual(manifest["images"][0]["sourceSha256"], rejected_hash)

    def test_private_text_in_final_ocr_prevents_acceptance(self):
        private = ("contact@example.test", 2, 2, 40, 12, ("fixture-line",))
        with self.assertRaisesRegex(SystemExit, "Post-write OCR found private text"):
            self.run_ingest([[[]], [[private]]])
        self.assertFalse(self.target.exists())
        self.assertFalse((self.package / "raw/readings/_ingest.json").exists())


class CaptureSetup(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node.js is needed for the capture helper")
    def test_a_fresh_capture_directory_saves_both_outputs(self):
        helper = HERE / "tools/capture-repl.js"
        with tempfile.TemporaryDirectory() as directory:
            program = """const fs=require('node:fs/promises');
const captureDir=process.argv[1], nodeRepl={write(){}};
const login={playwright:{evaluate:async()=>({elements:[],variables:{},width:1440})},screenshot:async()=>Buffer.from('screenshot fixture')};
eval(await fs.readFile(process.argv[2],'utf8')+'\\n globalThis.runFixture=originalCapture;');
await globalThis.runFixture('fresh');
"""
            # The helper runs in a REPL with shared bindings; evaluate this test
            # in the same async lexical scope instead of invoking a browser.
            result = subprocess.run(["node", "-e", "(async()=>{" + program + "})().catch(e=>{console.error(e);process.exit(1)});", directory, str(helper)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(directory) / "readings/fresh.json").is_file())
            self.assertTrue((Path(directory) / "raw-shots/fresh.png").is_file())


if __name__ == "__main__":
    unittest.main()
