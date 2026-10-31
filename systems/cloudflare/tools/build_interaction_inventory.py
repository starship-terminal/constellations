#!/usr/bin/env python3
"""Export the live external interaction inventory without changing recorded statuses."""
import argparse
import collections
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = pathlib.Path.home() / '.design-systems/cloudflare/interaction-inventory.json'
IDENTIFIER = re.compile(r'(?<![0-9a-fA-F])[0-9a-fA-F]{32}(?![0-9a-fA-F])')


def sanitize(value):
    if isinstance(value, str):
        return IDENTIFIER.sub(':id', value)
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, dict):
        return {sanitize(key): sanitize(item) for key, item in value.items()}
    return value


def cell(value):
    if value is None:
        return ''
    return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('\n', '<br>')


def build(source):
    data = sanitize(json.loads(source.read_text()))
    entries = data['entries']
    counts = collections.Counter(entry.get('status', 'unspecified') for entry in entries)
    imported = 0
    raw = 0
    for entry in entries:
        shot = entry.get('screenshot')
        if not shot:
            continue
        match = re.fullmatch(r'app/([^/]+)\.image', shot)
        name = match.group(1) if match else None
        if name == 'account-home-light-desktop':
            name = 'account-home-dark-desktop'
        target = ROOT / 'screenshots' / f'{name}.png' if name else None
        if target and target.is_file():
            entry['screenshot'] = target.relative_to(ROOT).as_posix()
            entry['screenshotEvidence'] = 'Imported package screenshot'
            imported += 1
        else:
            entry['screenshotEvidence'] = 'Raw evidence outside repository; not yet imported'
            raw += 1
    data['exportSummary'] = {
        'entryCount': len(entries),
        'statusCounts': dict(sorted(counts.items())),
        'importedScreenshotReferences': imported,
        'rawScreenshotReferencesNotImported': raw,
        'countingNote': 'Counts are discovered-control occurrences, not unique controls. Shared navigation repeats across parent states. Pending reconciliation remains unresolved: no pending occurrence is inferred complete from another occurrence.',
        'sanitization': 'All standalone 32-hex identifiers replaced with :id. Recorded statuses and source completeness preserved.',
    }
    (ROOT / 'interaction-inventory.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    lines = ['# Cloudflare interaction inventory', '', str(data.get('scope', '')), '',
             f"Source completeness: **{str(data.get('complete', 'unspecified')).lower()}**. This is a snapshot of ongoing exploration, not a claim of full dashboard coverage.", '',
             data['exportSummary']['countingNote'], '',
             '| Recorded status | Discovered-control occurrences |', '| --- | ---: |']
    lines += [f'| {cell(status)} | {count} |' for status, count in sorted(counts.items())]
    lines += ['', f'{imported} screenshot references resolve to imported package images; {raw} refer to raw evidence not yet imported.', '',
              'Pending controls remain unexercised in their recorded parent state. Blocked and not executed rows retain their recorded reasons below. Missing statuses remain unspecified.', '',
              'Regenerate from the repository root with `python3 systems/cloudflare/tools/build_interaction_inventory.py`. The external source is read once and never modified. JSON preserves every source field, with identifiers sanitized and screenshot import annotations added.', '']
    groups = collections.defaultdict(list)
    for entry in entries:
        groups[entry.get('parent', 'unspecified')].append(entry)
    for parent, rows in groups.items():
        lines += [f'## {cell(parent)}', '', '| ID | Control | Action | Status | Result / reason | Evidence |', '| --- | --- | --- | --- | --- | --- |']
        for entry in rows:
            shot = entry.get('screenshot', '')
            evidence = f'[{cell(shot)}]({shot})' if entry.get('screenshotEvidence') == 'Imported package screenshot' else (f'Raw, not imported: {cell(shot)}' if shot else '')
            reason = '; '.join(str(entry[k]) for k in ('result', 'reason') if entry.get(k))
            lines.append('| ' + ' | '.join([cell(entry.get('id')), cell(entry.get('control')), cell(entry.get('action')), cell(entry.get('status', 'unspecified')), cell(reason), evidence]) + ' |')
        lines.append('')
    (ROOT / 'interaction-inventory.md').write_text('\n'.join(lines).rstrip() + '\n')
    print(json.dumps(data['exportSummary'], indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=pathlib.Path, default=DEFAULT_SOURCE, help='External inventory JSON (default: live Cloudflare capture inventory)')
    build(parser.parse_args().source)
