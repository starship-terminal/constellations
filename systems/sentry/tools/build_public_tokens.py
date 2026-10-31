"""Build landing-page tokens only; never treat marketing CSS as app evidence."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build():
    data = json.loads((ROOT / 'raw/public/landing-desktop.json').read_text())
    output = {'$description': 'Sentry public landing page only. Signed-in app capture pending.', 'core': {}, 'dark': {}}
    for name, value in data['customProperties'].items():
        # Retain declared values verbatim. Complex CSS remains in the reading.
        if value.startswith('#'):
            kind = 'color'
        elif value.endswith(('px', 'rem')) and ' ' not in value:
            kind = 'dimension'
        else:
            continue
        group = 'dark' if name in ('--bg-primary', '--bg-secondary', '--border-color') else 'core'
        output[group][name.removeprefix('--')] = {
            '$type': kind, '$value': value,
            '$extensions': {'source': f'Measured: raw/public/landing-desktop.json customProperties.{name}; live /welcome/ html.dark, 1440px. Public marketing only.'},
        }
    for width in ('desktop', 'mobile'):
        reading = json.loads((ROOT / f'raw/public/landing-{width}.json').read_text())
        heading = next(c for c in reading['components'] if c['tag'] == 'H1')
        for prop, kind in [('font-family', 'fontFamily'), ('font-size', 'dimension'), ('line-height', 'dimension'), ('font-weight', 'fontWeight')]:
            value = heading['styles'][prop]
            output['core'][f'hero-{width}-{prop}'] = {'$type': kind, '$value': int(value) if kind == 'fontWeight' else value, '$extensions': {'source': f'Measured: raw/public/landing-{width}.json, h1 computed {prop}; public landing only.'}}
    (ROOT / 'raw/public/tokens.json').write_text(json.dumps(output, indent=2) + '\n')


if __name__ == '__main__':
    build()
