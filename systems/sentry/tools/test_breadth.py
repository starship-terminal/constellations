"""Protect credential removal and honest state acceptance in breadth imports."""
import importlib.util
import json
from pathlib import Path
import re
import tempfile
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

    @unittest.skipUnless(PILLOW and NUMPY, 'breadth importer needs Pillow and numpy')
    def test_recorded_urls_keep_origin_and_route_words_only(self):
        from import_breadth import safe_url
        cases = {
            'https://acme.sentry.io/explore/traces/trace/f0e83586fdd18d22ecab2fc313d84e05/':
                'https://acme.sentry.io/explore/traces/trace/<id>/',
            'https://acme.sentry.io/explore/releases/f6caa28ad41aee2ba62f9af8975565460c74fe90/commits/':
                'https://acme.sentry.io/explore/releases/<id>/commits/',
            'https://acme.sentry.io/settings/projects/my-app/source-maps/62fb505e-a481-5695-9b8f-4705d8502a6f/':
                'https://acme.sentry.io/settings/projects/<id>/source-maps/<id>/',
            '/organizations/acme/dashboard/4504883/?project=4511308759695360&sort=-project':
                '/organizations/acme/dashboard/<id>/',
            'https://acme.sentry.io/issues/?query=is%3Aunresolved#frag': 'https://acme.sentry.io/issues/',
            '#main': '#main',
            '#access_token=abc': '#<id>',
            'mailto:someone@example.test': 'mailto:<id>',
            None: None,
        }
        for raw, want in cases.items():
            self.assertEqual(safe_url(raw), want, raw)

    @unittest.skipUnless(PILLOW and NUMPY, 'breadth importer needs Pillow and numpy')
    def test_signed_params_and_masked_tokens_are_removed(self):
        from import_breadth import sanitize
        for url in ['https://cdn.example.test/a.png?X-Amz-Signature=abc',
                    'https://cdn.example.test/a.png?X-Goog-Credential=abc',
                    'https://cdn.example.test/v.mp4?Expires=1&Key-Pair-Id=k',
                    'https://app.example.test/cb#id_token=abc']:
            self.assertEqual(sanitize(url), '[redacted signed URL]', url)
        self.assertEqual(sanitize('https://example.test/a?tokenizer=1'), 'https://example.test/a?tokenizer=1')
        self.assertEqual(sanitize('Token sntrys_****abcd shown'), 'Token [redacted token] shown')

    def test_committed_inventories_carry_no_ids_or_queries(self):
        id_like = re.compile(r'[0-9a-f]{12,}|\d{6,}|[?]')
        for batch in ('breadth', 'breadth2'):
            inventory = json.loads((ROOT / f'raw/{batch}/inventory.json').read_text())
            for row in inventory['actions'] + inventory['controlOccurrences']:
                for key in ('url', 'href'):
                    self.assertFalse(id_like.search(row.get(key) or ''), (batch, row['id'], row.get(key)))
            for reading in (ROOT / f'raw/{batch}/readings').glob('*.json'):
                url = json.loads(reading.read_text()).get('url') or ''
                self.assertFalse(id_like.search(url), (reading.name, url))

    @unittest.skipUnless(PILLOW and NUMPY, 'breadth importer needs Pillow and numpy')
    def test_validation_finds_every_bad_capture_before_writing(self):
        from import_breadth import validate
        from PIL import Image
        with tempfile.TemporaryDirectory() as d:
            src = Path(d)
            viewport = {'innerWidth': 4, 'innerHeight': 3}
            for name, size in (('good', (4, 3)), ('wrong-size', (8, 3))):
                (src / f'{name}.json').write_text(json.dumps({'viewport': viewport}))
                Image.new('RGB', size).save(src / f'{name}.jpg')
            (src / 'no-image.json').write_text(json.dumps({'viewport': viewport}))
            (src / 'dup.json').write_text(json.dumps({'viewport': viewport}))
            pages = [{'id': n} for n in ('dup', 'good', 'wrong-size', 'no-image', 'no-reading', 'skipped')]
            decisions = {
                'dup': {'decision': 'duplicate', 'duplicateOf': 'gone'},
                'good': {'decision': 'accept'}, 'wrong-size': {'decision': 'accept'},
                'no-image': {'decision': 'accept'}, 'no-reading': {'decision': 'reject'},
            }
            errors = validate(src, pages, decisions)
            self.assertEqual(len(errors), 4, errors)
            for name in ('dup', 'wrong-size', 'no-image', 'no-reading'):
                self.assertTrue(any(e.startswith(name + ':') for e in errors), (name, errors))
            decisions['dup']['duplicateOf'] = 'good'   # an original later in the list is fine
            self.assertEqual(len(validate(src, pages, decisions)), 3)


if __name__ == '__main__':
    unittest.main()
