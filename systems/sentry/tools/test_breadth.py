"""Protect credential removal and honest state acceptance in breadth imports."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PILLOW = importlib.util.find_spec('PIL') is not None
NUMPY = importlib.util.find_spec('numpy') is not None


class BreadthEvidenceTests(unittest.TestCase):
    @unittest.skipUnless(PILLOW and NUMPY, 'breadth importer needs Pillow and numpy')
    def test_truncated_and_complete_credentials_are_removed(self):
        from import_breadth import sanitize
        fake_key = '0123456789abcdef' * 2
        for suffix in ['', '@o123.ingest.us.sentry.io/456']:
            raw = {'label': 'dsn: https://' + fake_key + suffix, 'children': ['sntrys_TESTTOKEN123']}
            clean = sanitize(raw)
            self.assertNotIn(fake_key, json.dumps(clean))
            self.assertNotIn('TESTTOKEN123', json.dumps(clean))
        self.assertEqual(sanitize('https://docs.sentry.io/product/'), 'https://docs.sentry.io/product/')

    def test_rejected_attempts_do_not_get_imported_as_screenshots(self):
        for batch in ('breadth', 'breadth2'):
            manifest = json.loads((ROOT / f'raw/{batch}/import-manifest.json').read_text())
            inventory = json.loads((ROOT / f'raw/{batch}/inventory.json').read_text())
            actions = {a['parentState']: a for a in inventory['actions']}
            for item in manifest['captures']:
                if item['decision'] == 'reject':
                    self.assertEqual(actions[item['id']]['status'], 'pending')
                    self.assertIsNone(actions[item['id']]['screenshot'])
                    self.assertFalse((ROOT / f"screenshots/{batch}/{item['id']}.png").exists())
                    self.assertFalse((ROOT / f"screenshots/{batch}-mixed/{item['id']}.png").exists())
                elif item['decision'] == 'accept':
                    shot = ROOT / actions[item['id']]['screenshot']
                    self.assertTrue(shot.exists())
                    sidecar = json.loads(Path(str(shot) + '.capture.json').read_text())
                    reading = json.loads((ROOT / actions[item['id']]['reading']).read_text())
                    self.assertEqual(sidecar['actual'], reading['viewport'])
                    self.assertEqual(sidecar['visualReview']['status'], 'accepted')

    def test_embedded_demos_and_failed_menu_remain_distinct(self):
        inventory = json.loads((ROOT / 'raw/breadth/inventory.json').read_text())
        actions = {a['parentState']: a for a in inventory['actions']}
        self.assertEqual(actions['dashboard-widget-actions-dark']['status'], 'pending')
        for action in actions.values():
            if 'embedded' in action['provenance'] and action['screenshot']:
                self.assertIn('/breadth-mixed/', action['screenshot'])
        self.assertTrue(all(c['status'] in ('pending', 'blocked', 'not executed')
                            for c in inventory['controlOccurrences']))

    @unittest.skipUnless(PILLOW and NUMPY, 'breadth importer needs Pillow and numpy')
    def test_opening_form_is_distinct_from_final_submission(self):
        from import_breadth import control_status
        control = {'tag': 'BUTTON', 'label': 'Create Monitor'}
        self.assertEqual(control_status(control, '/organizations/10xswe/monitors/')[0], 'pending')
        self.assertEqual(control_status(control, '/organizations/10xswe/monitors/new/settings/')[0], 'not executed')
        control['disabled'] = True
        self.assertEqual(control_status(control, '/organizations/10xswe/monitors/new/settings/')[0], 'blocked')


if __name__ == '__main__':
    unittest.main()
