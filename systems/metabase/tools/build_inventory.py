#!/usr/bin/env python3
"""Render and validate the partial page/control inventory without inferring coverage."""
import json
from collections import Counter
from pathlib import Path
P = Path(__file__).resolve().parent.parent
source = json.loads((P / 'raw/interaction-inventory.json').read_text())
rows = source['entries']
allowed = {'pending', 'explored and captured', 'explored and duplicate', 'blocked', 'not executed'}
ids = set()
for row in rows:
    if row['id'] in ids:
        raise ValueError(f"duplicate inventory id {row['id']!r}")
    ids.add(row['id'])
    if row['status'] not in allowed:
        raise ValueError(f"{row['id']}: status {row['status']!r} is not one of {sorted(allowed)}")
    if row.get('screenshot') and not (P / row['screenshot']).is_file():
        raise ValueError(f"{row['id']}: screenshot {row['screenshot']} does not exist")
counts = Counter(r['status'] for r in rows)
def cell(value):
    return str(value or '').replace('|', '\\|').replace('\n', ' ')
lines = ['# Page and interaction inventory', '', '**Partial exploration.** Pending rows remain; this is a resumable checkpoint, not exhaustive coverage.', '',
         'The first rows record actual interactions. Discovered-control rows preserve visible controls conservatively until their individual behavior is reconciled. A screenshot reference on a pending row proves visibility only, not activation. Repeated controls are not assumed equivalent.', '',
         '| Status | Rows |', '|---|---:|']
lines += [f'| {s} | {counts[s]} |' for s in sorted(allowed)]
lines += ['', 'Light was restored after the authorized Dark capture. No creation, deletion, invitation, cache clear, or account update was submitted.', '',
          '## Remaining branches', '']
lines += [f'- {cell(r["control"])}: {cell(r["reason"])}.' for r in rows if r['id'].startswith('p')]
lines += ['', '## Recorded controls', '', '| ID | Parent / path | Control | Action / result | Theme / CSS width | Status / reason | Evidence |', '|---|---|---|---|---|---|---|']
for r in rows:
    evidence = f'[image]({r["screenshot"]})' if r.get('screenshot') else ''
    lines.append('| '+ ' | '.join([cell(r['id']),cell(r['parent']),cell(r['control']),cell(r['action'])+'; '+cell(r['result']),f'{r["theme"]} / {r["width"]}',cell(r['status'])+'; '+cell(r['reason']),evidence])+' |')
(P / 'interactions.md').write_text('\n'.join(lines)+'\n')
print(dict(counts))
