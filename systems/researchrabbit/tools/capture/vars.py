#!/usr/bin/env python3
"""Read the custom properties and every styled-component's rules out of the archived snapshots.

usage: python3 tools/capture/vars.py

Reads $RR_SNAPSHOTS/*.html.gz (default ~/.design-systems/snaps/researchrabbit) and merges
into raw/css-vars.json: the :root custom properties in declaration order, the font families
the pages load, the @media conditions and @keyframes the stylesheets hold, the rules on bare
elements (`globals`: body, button:focus), and, for each
styled-component, its display name (the `File__Name` part of the `File__Name-sc-hash` class
the DOM carries) mapped to the CSS rules of its generated class.

The file is merged, never replaced: the 2026-10-04 snapshots are gone, so their readings stay
and each later capture adds its pages, rules and conditions (`reads` lists the dates). A
:root value that differs from the one already recorded is kept under `rootChanged`. Running it
twice on the same snapshots changes nothing.
"""
import collections, gzip, json, os, pathlib, re

REF = pathlib.Path(__file__).resolve().parent.parent.parent
ARCH = pathlib.Path(os.environ.get('RR_SNAPSHOTS', '~/.design-systems/snaps/researchrabbit')).expanduser()
READ = os.environ.get('RR_READ', '2026-10-17')
OUT = REF / 'raw' / 'css-vars.json'

prev = json.loads(OUT.read_text()) if OUT.exists() else {}
root_vars = dict(prev.get('root', {}))
root_changed = dict(prev.get('rootChanged', {}))
fonts = set(prev.get('fonts', []))
components = collections.defaultdict(set, {k: set(v) for k, v in prev.get('components', {}).items()})
media = dict(prev.get('media', {}))
keyframes = dict(prev.get('keyframes', {}))
globals_ = set(prev.get('globals', []))
pages_prev = list(prev.get('pages', []))

pages = sorted(ARCH.glob('*.html.gz'))
seen_media = collections.defaultdict(set)
for f in pages:
    html = gzip.open(f, 'rt').read()
    css = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', html, re.S))
    for block in re.findall(r'(?m)^:root \{([^}]*)\}', css):
        for name, value in re.findall(r'(--[\w-]+):\s*([^;]+);', block):
            value = value.strip()
            if name not in root_vars:
                root_vars[name] = value
            elif root_vars[name] != value:
                root_changed[name] = value
    fonts.update(m.strip(' "\'') for m in re.findall(r'family=([^:&"]+)', html))
    for cond in re.findall(r'@media ([^{]+)\{', css):
        seen_media[cond.strip()].add(f.name)
    for name, body in re.findall(r'@keyframes ([\w-]+) \{(.*?\})\s*\}', css, re.S):
        keyframes.setdefault(name, re.sub(r'\s+', ' ', body).strip())
    # Rules on bare elements (body, button:focus, html), which no styled-component owns.
    for sel, body in re.findall(r'(?m)^([a-z*:][^{}.@\n]*)\{([^{}]*)\}', css):
        sel = sel.strip()
        if sel.startswith(':root') or 'intercom' in sel or '--tw-' in body:
            continue
        globals_.add(f'{sel} {{ {body.strip()} }}')
    rules = collections.defaultdict(list)
    for sel, body in re.findall(r'(?m)^([^{}@\n][^{}\n]*)\{([^{}]*)\}', css):
        for cls in re.findall(r'\.([A-Za-z][\w-]*)', sel):
            rules[cls].append(f'{sel.strip()} {{ {body.strip()} }}')
    for cls_attr in re.findall(r'class="([^"]*__[^"]*)"', html):
        names = cls_attr.split()
        for i, n in enumerate(names):
            m = re.match(r'([A-Z]\w*__\w+)-sc-[\w]+-\d+$', n)
            if m and i + 1 < len(names):
                gen = names[i + 1]
                if '__' not in gen:
                    for r in rules.get(gen, []):
                        components[m.group(1)].add(r.replace('.' + gen, '&'))
for cond, files in seen_media.items():
    media[cond] = max(media.get(cond, 0), len(files))

new_pages = [p.name.removesuffix('.html.gz') for p in pages]
reads = list(prev.get('reads', ['2026-10-04']))
if new_pages and READ not in reads:
    reads.append(READ)
out = {
    'source': 'app.researchrabbit.ai, signed in, read from the DOM and CSSOM of redacted snapshots',
    'reads': reads,
    'pages': pages_prev + [p for p in new_pages if p not in pages_prev],
    'root': root_vars,
    'rootChanged': dict(sorted(root_changed.items())),
    'fonts': sorted(fonts),
    'media': dict(sorted(media.items())),
    'keyframes': dict(sorted(keyframes.items())),
    'globals': sorted(g for g in globals_ if not g.startswith(('mjx', 'sentinel'))),  # MathJax's own rules
    'components': {k: sorted(v) for k, v in sorted(components.items())},
}
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps(out, indent=1) + '\n')
print(len(root_vars), 'vars,', len(root_changed), 'changed,', len(components), 'components,', len(media), 'media, fonts', sorted(fonts))
