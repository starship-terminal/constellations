"""The style guide keeps token values inside their element: a value holding </script>,
</style> or a marker name cannot close the element or pull in another section."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parent.parent
HOSTILE = ' </script></style>ROWS@@ROWS@@'


def poison(node):
    if isinstance(node, dict):
        if isinstance(node.get('$value'), str):
            node['$value'] += HOSTILE
        for value in node.values():
            poison(value)


class StyleGuideTests(unittest.TestCase):
    def test_hostile_values_stay_inside_their_element(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)
            (package / 'tools').mkdir()
            (package / 'screenshots').mkdir()
            shutil.copy(PACKAGE / 'tools/build_style_guide.py', package / 'tools')
            tokens = json.loads((PACKAGE / 'tokens.json').read_text())
            poison(tokens)
            (package / 'tokens.json').write_text(json.dumps(tokens))
            subprocess.run([sys.executable, str(package / 'tools/build_style_guide.py')], check=True,
                           capture_output=True, cwd=package)
            page = (package / 'style-guide.html').read_text()
            clean = (PACKAGE / 'style-guide.html').read_text()
            for tag in ('</script>', '</style>'):
                self.assertEqual(page.count(tag), clean.count(tag), tag)
            # A value spelling a marker is shown as written, never replaced by another section:
            # a second copy of the token table would add rows.
            self.assertEqual(page.count('<tr'), clean.count('<tr'))
            self.assertIn('ROWS@@ROWS@@', page)


if __name__ == '__main__':
    unittest.main()
