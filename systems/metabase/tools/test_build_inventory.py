"""The inventory builder rejects bad rows with a message, also under python3 -O."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parent.parent


class InventoryTests(unittest.TestCase):
    def run_with(self, rows):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)
            (package / 'raw').mkdir()
            (package / 'tools').mkdir()
            shutil.copy(PACKAGE / 'tools/build_inventory.py', package / 'tools')
            (package / 'raw/interaction-inventory.json').write_text(json.dumps({'entries': rows}))
            return subprocess.run([sys.executable, '-O', str(package / 'tools/build_inventory.py')],
                                  capture_output=True, text=True)

    def row(self, **changes):
        row = json.loads((PACKAGE / 'raw/interaction-inventory.json').read_text())['entries'][0]
        row.pop('screenshot', None)
        row.update(changes)
        return row

    def test_duplicate_id_is_rejected(self):
        run = self.run_with([self.row(), self.row()])
        self.assertNotEqual(run.returncode, 0)
        self.assertIn('duplicate inventory id', run.stderr)

    def test_unknown_status_and_missing_screenshot_are_rejected(self):
        run = self.run_with([self.row(status='done')])
        self.assertIn("status 'done'", run.stderr)
        run = self.run_with([self.row(screenshot='screenshots/missing.png')])
        self.assertIn('does not exist', run.stderr)

    def test_valid_rows_build(self):
        self.assertEqual(self.run_with([self.row()]).returncode, 0)


if __name__ == '__main__':
    unittest.main()
