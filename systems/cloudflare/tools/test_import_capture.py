"""The importer masks every rule rectangle before it saves a palette screenshot."""
import importlib.util
import unittest

NEEDS = all(importlib.util.find_spec(m) for m in ('PIL', 'numpy'))


@unittest.skipUnless(NEEDS, 'the importer needs Pillow and numpy')
class MaskTests(unittest.TestCase):
    def setUp(self):
        import import_capture
        from PIL import Image
        self.mod, self.Image = import_capture, Image

    def test_reads_this_packages_rules(self):
        self.assertEqual(self.mod.rules_path.name, 'cloudflare.json')

    def test_rule_rectangles_are_painted_and_other_images_untouched(self):
        im = self.Image.new('RGB', (12, 10), 'red')
        im.paste((255, 255, 255), (2, 3, 10, 6))
        saved = self.mod.rules
        self.addCleanup(setattr, self.mod, 'rules', saved)
        self.mod.rules = {'families': [{'files': ['screenshots/a.png'], 'rects': [[1, 2, 11, 7, 'solid']]}]}
        out, count = self.mod.masked(im, 'screenshots/a.png')
        self.assertEqual(count, 1)
        self.assertFalse(any(px[1] > 200 for px in out.getdata()))
        out, count = self.mod.masked(im, 'screenshots/b.png')
        self.assertEqual(count, 0)
        self.assertEqual(list(out.getdata()), list(im.getdata()))

    def test_import_saves_masked_screenshots(self):
        import json, tempfile
        from pathlib import Path
        saved = self.mod.rules
        self.addCleanup(setattr, self.mod, 'rules', saved)
        self.mod.rules = {'families': [{'files': ['screenshots/x-dark-desktop.png'], 'rects': [[1, 2, 11, 7, 'solid']]}]}
        with tempfile.TemporaryDirectory() as d:
            root, source = Path(d) / 'package', Path(d) / 'source'
            for folder in (root / 'tools', root / 'screenshots', root / 'raw', source / 'app'):
                folder.mkdir(parents=True)
            (root / 'tools/accepted.json').write_text(json.dumps({'x-dark-desktop': 'app'}))
            im = self.Image.new('RGB', (12, 10), 'red')
            im.paste((255, 255, 255), (2, 3, 10, 6))
            im.save(source / 'app/x-dark-desktop.image', format='PNG')
            (source / 'app/x-dark-desktop.json').write_text(json.dumps({
                'url': 'https://dash.example.test/home', 'viewport': {'width': 12, 'height': 10},
                'time': '2026-01-01T00:00:00Z',
                'components': [{'rect': {'width': 5, 'height': 5}, 'text': 'Invented'}]}))
            self.mod.main(source, root)
            with self.Image.open(root / 'screenshots/x-dark-desktop.png') as out:
                self.assertFalse(any(px[1] > 200 for px in out.convert('RGB').getdata()))
            self.assertEqual(json.loads((root / 'raw/x-dark-desktop.json').read_text())['components'][0]['label'], 'Invented')


if __name__ == '__main__':
    unittest.main()
