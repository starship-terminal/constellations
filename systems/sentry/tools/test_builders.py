"""Guard evidence separation, semantic selection and reproducible package outputs."""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative):
    return json.loads((ROOT / relative).read_text())


def tokens(node):
    if isinstance(node, dict):
        if '$value' in node:
            yield node
        else:
            for value in node.values():
                yield from tokens(value)


class EvidenceTests(unittest.TestCase):
    def test_theme_roles_follow_visible_selected_tab_and_body(self):
        result = read('tokens.json')
        for theme in ('dark', 'light'):
            reading = read(f'raw/app/traces-{theme}-list.json')
            selected = next(c for c in reading['components']
                            if c['role'] == 'tab' and c['label'] == 'Span Samples')
            self.assertEqual(result[theme]['accent']['primary']['$value'],
                             selected['styles']['color'])
            foundation = read(f'raw/app/foundations-{theme}.json')
            body_color = (foundation['elements'][1]['styles']['color']
                          if theme == 'dark' else foundation['body']['color'])
            self.assertEqual(result[theme]['text']['primary']['$value'], body_color)
        self.assertNotEqual(result['light']['background']['page']['$value'],
                            result['dark']['background']['page']['$value'])

    def test_all_sources_resolve_and_stores_stay_separate(self):
        for filename, store in [('tokens.json', 'app'), ('raw/public/tokens.json', 'public')]:
            for token in tokens(read(filename)):
                source = token['$extensions']['source']
                self.assertTrue(source.startswith('Measured: '))
                path = re.search(r'raw/(?:app|public)/[\w-]+\.json', source).group()
                self.assertTrue(path.startswith(f'raw/{store}/'), source)
                self.assertTrue((ROOT / path).is_file(), source)
                index = re.search(r'components\[(\d+)\]', source)
                if index:
                    self.assertLess(int(index[1]), len(read(path)['components']))
        self.assertNotIn('capture pending', read('raw/public/tokens.json')['$description'])

    def test_screenshot_sidecars_match_readings(self):
        groups = set()
        for path in (ROOT / 'screenshots/app').glob('*.png.capture.json'):
            sidecar = json.loads(path.read_text())
            name = path.name.removesuffix('.png.capture.json')
            raw = read(f'raw/app/{name}.json')
            # Read-only capture preserves the browser's actual viewport, not requested overrides.
            self.assertEqual(sidecar['actual'], raw['viewport'])
            self.assertLessEqual(abs(sidecar['png']['width'] - sidecar['actual']['innerWidth']), 1)
            groups.add(round(sidecar['actual']['devicePixelRatio'], 1))
        self.assertEqual(groups, {1.8, 2.0})

    def test_builders_reproduce_committed_outputs_in_isolation(self):
        outputs = ['tokens.json', 'raw/public/tokens.json', 'style-guide.html', 'components.md']
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'sentry'
            shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns('__pycache__'))
            for name in ['build_tokens', 'build_public_tokens', 'build_style_guide', 'build_components_md']:
                subprocess.run([sys.executable, str(target / 'tools' / f'{name}.py')], check=True)
            for name in outputs:
                self.assertEqual((ROOT / name).read_bytes(), (target / name).read_bytes(), name)


if __name__ == '__main__':
    unittest.main()
