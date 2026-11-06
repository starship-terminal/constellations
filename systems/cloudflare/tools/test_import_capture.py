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


if __name__ == '__main__':
    unittest.main()
