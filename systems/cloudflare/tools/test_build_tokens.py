"""Regression checks run builders in isolated copies, never edit capture evidence."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
CAPTURE = 'custom-rule-empty-dark-desktop.json'


class BuilderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        shutil.copytree(ROOT / 'raw', self.root / 'raw')
        (self.root / 'tools').mkdir()
        for script in ('build_tokens.py', 'build_style_guide.py'):
            shutil.copy(ROOT / 'tools' / script, self.root / 'tools' / script)

    def build(self, script='build_tokens.py', success=True):
        run = subprocess.run([sys.executable, str(self.root / 'tools' / script)], capture_output=True, text=True)
        self.assertEqual(run.returncode == 0, success, run.stderr)
        return run

    def mutate(self, operation):
        path = self.root / 'raw' / CAPTURE
        data = json.loads(path.read_text())
        operation(data['components'])
        path.write_text(json.dumps(data))

    def test_reordering_preserves_all_tokens_and_measured_widths(self):
        self.build()
        expected = (self.root / 'tokens.json').read_bytes()
        self.mutate(lambda components: components.reverse())
        self.build()
        self.assertEqual((self.root / 'tokens.json').read_bytes(), expected)
        tokens = json.loads(expected)
        self.assertEqual(tokens['core']['borderWidth']['ruleName']['$value'], '0px')
        self.assertEqual(tokens['core']['borderWidth']['conditionValue']['$value'], '1px')
        self.assertEqual(tokens['dark']['component']['input']['height']['$value'], '36px')

    def test_missing_reviewed_field_fails_closed(self):
        self.mutate(lambda components: components.__setitem__(slice(None), [c for c in components if not (c['tag'] == 'INPUT' and c['rect']['y'] == 275)]))
        self.assertIn('expected exactly one match, got 0', self.build(success=False).stderr)

    def test_duplicate_reviewed_field_fails_closed(self):
        self.mutate(lambda components: components.append(next(c for c in components if c['tag'] == 'INPUT' and c['rect']['y'] == 275)))
        self.assertIn('expected exactly one match, got 2', self.build(success=False).stderr)

    def test_guide_has_dark_only_measured_component_previews(self):
        self.build()
        self.build('build_style_guide.py')
        guide = (self.root / 'style-guide.html').read_text()
        self.assertIn('Captured component values: dark default state', guide)
        self.assertIn('id="rule-name-preview"', guide)
        self.assertIn('background:oklch(0.205 0 none)', guide)
        self.assertIn('height:36px;border-radius:8px;border-width:0px', guide)
        self.assertIn('dark.component.link', guide)
        self.assertIn('No light, hover, focus or disabled component preview is inferred.', guide)
        self.build('build_style_guide.py')
        self.assertEqual(guide, (self.root / 'style-guide.html').read_text())

    def test_missing_preview_role_names_the_role(self):
        path = self.root / 'raw' / 'security-rules-light-desktop.json'
        data = json.loads(path.read_text())
        del data['variables']['--color-border']
        path.write_text(json.dumps(data))
        stderr = self.build(success=False).stderr
        self.assertIn('light.border.default', stderr)
        self.assertNotIn('KeyError', stderr)

    def test_missing_marketing_role_names_the_role(self):
        path = self.root / 'raw' / 'public-home-desktop.json'
        data = json.loads(path.read_text())
        del data['variables']['--color-border']
        path.write_text(json.dumps(data))
        stderr = self.build(success=False).stderr
        self.assertIn('marketing.border.default', stderr)
        self.assertNotIn('KeyError', stderr)


if __name__ == '__main__':
    unittest.main()
