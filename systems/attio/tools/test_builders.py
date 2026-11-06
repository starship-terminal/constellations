"""Regression checks for visible-label tokens and evidence-preserving rebuilds."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from PIL import Image
from build_images import build_images

PACKAGE = Path(__file__).resolve().parent.parent


class TokenTests(unittest.TestCase):
    def test_visible_labels_are_separate_from_container_geometry(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)
            (package / 'raw').mkdir()
            (package / 'tools').mkdir()
            shutil.copy(PACKAGE / 'tools/build_tokens.py', package / 'tools')
            for theme in ['light', 'dark']:
                shutil.copy(PACKAGE / f'raw/companies-{theme}-scoped.json', package / 'raw')
            subprocess.run([sys.executable, str(package / 'tools/build_tokens.py')], check=True,
                           capture_output=True)
            tokens = json.loads((package / 'tokens.json').read_text())
            for theme in ['light', 'dark']:
                components = tokens[theme]['component']
                for component in ['primaryButton', 'toolbarButton']:
                    label = components[component]['label']
                    self.assertEqual(label['fontSize']['$value'], '14px')
                    self.assertEqual(label['fontWeight']['$value'], '500')
                    self.assertEqual(label['lineHeight']['$value'], '20px')
                    self.assertEqual(components[component]['container']['height']['$value'], '28px')
                    self.assertNotIn('fontSize', components[component]['container'])
                self.assertEqual(components['primaryButton']['label']['color']['$value'],
                                 'rgb(255, 255, 255)')
                self.assertNotIn('label', components['sidebar'])
                self.assertNotIn('label', components['iconButton'])


    def test_shifted_reading_fails_instead_of_building_wrong_roles(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)
            (package / 'raw').mkdir()
            (package / 'tools').mkdir()
            shutil.copy(PACKAGE / 'tools/build_tokens.py', package / 'tools')
            for theme in ['light', 'dark']:
                shutil.copy(PACKAGE / f'raw/companies-{theme}-scoped.json', package / 'raw')
            path = package / 'raw/companies-dark-scoped.json'
            raw = json.loads(path.read_text())
            raw['elements'].insert(0, {'tag': 'DIV', 'label': 'Inserted', 'styles': {}})
            path.write_text(json.dumps(raw))
            run = subprocess.run([sys.executable, str(package / 'tools/build_tokens.py')],
                                 capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('companies-dark-scoped.json: elements[0]', run.stderr)
            self.assertFalse((package / 'tokens.json').exists())


class ImageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.package = root / 'package'
        self.source = root / 'originals'
        for directory in [self.source, self.package / 'raw', self.package / 'screenshots',
                          self.package / 'components']:
            directory.mkdir(parents=True)
        self.captures = []
        for name, colour in [('first.png', 'red'), ('last.png', 'blue')]:
            Image.new('RGB', (12, 10), colour).save(self.source / name, format='JPEG')
            data = (self.source / name).read_bytes()
            self.captures.append(dict(file=name, packagedFile='screenshots/'+name,
                status='accepted', sha256=hashlib.sha256(data).hexdigest(),
                imageSize=[12, 10], decodedFormat='JPEG'))
            (self.package / 'screenshots' / name).write_bytes(b'original packaged sentinel')
        (self.package / 'components/crop.png').write_bytes(b'original crop sentinel')
        (self.package / 'raw/crops.json').write_text(json.dumps([
            dict(source='screenshots/first.png', file='components/crop.png', box=[1, 2, 7, 8])]))
        self.write_manifest()

    def write_manifest(self):
        (self.package / 'raw/capture-manifest.json').write_text(json.dumps(dict(captures=self.captures)))

    def assert_rejected_without_writes(self, message):
        before = {p: p.read_bytes() for folder in ['screenshots', 'components']
                  for p in (self.package / folder).iterdir()}
        with self.assertRaisesRegex(ValueError, message):
            build_images(self.package, self.source)
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_changed_last_original_does_not_overwrite_first_output_or_crops(self):
        Image.new('RGB', (12, 10), 'green').save(self.source / 'last.png', format='JPEG')
        self.assert_rejected_without_writes('SHA-256 mismatch')

    def test_dimensions_checked_even_when_hash_matches(self):
        self.captures[-1]['imageSize'] = [13, 10]
        self.write_manifest()
        self.assert_rejected_without_writes('dimensions mismatch')

    def test_decoded_format_checked_even_when_hash_matches(self):
        self.captures[-1]['decodedFormat'] = 'PNG'
        self.write_manifest()
        self.assert_rejected_without_writes('format mismatch')

    def test_verified_originals_make_png_and_expected_crop(self):
        build_images(self.package, self.source)
        with Image.open(self.package / 'screenshots/first.png') as image:
            self.assertEqual(image.format, 'PNG')
            self.assertEqual(image.size, (12, 10))
        with Image.open(self.package / 'components/crop.png') as image:
            self.assertEqual(image.size, (6, 6))
        before = (self.package / 'components/crop.png').read_bytes()
        build_images(self.package)
        self.assertEqual(before, (self.package / 'components/crop.png').read_bytes())


if __name__ == '__main__':
    unittest.main()
