#!/usr/bin/env python3
"""Import reviewed live-browser evidence; raw JPEGs remain outside the repository.

Run from any directory. The manifest makes acceptance explicit; the library's
masking primitives apply versioned coordinate rules before PNG quantization.
This imports evidence, not new token values or claims of exhaustive coverage.
"""
import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
SIGNED_PARAMS = ROOT / 'tools' / 'capture' / 'signed-in' / 'signed-params.json'


def signed_url_pattern(spec):
    """A URL parameter that carries a credential, from the prefixes and names in
    signed-params.json: after ?, &, &amp;, # or their %-encodings, case-insensitive."""
    names = [re.escape(p) + r'[A-Za-z0-9-]*' for p in spec['prefixes']] + [re.escape(p) for p in spec['params']]
    return re.compile(r'(?:[?&#]|%3F|%26|%23)(?:amp;)?(' + '|'.join(names) + r')(?:=|%3D)', re.I)


SIGNED = signed_url_pattern(json.loads(SIGNED_PARAMS.read_text()))

# The Python form of tools/capture/safe-url.mjs: a segment right after one of these names a
# resource however plain its spelling, so it is masked even when it looks like a route word.
RESOURCE = re.compile(
    r'^(?:c|g|p|u|chat|chats|project|projects|artifact|artifacts|cowork|share|shared|doc|docs|document|'
    r'documents|page|pages|file|files|folder|folders|thread|threads|conversation|conversations|task|tasks|'
    r'issue|issues|notebook|notebooks|workspace|workspaces|space|spaces|team|teams|org|orgs|organization|'
    r'user|users|profile|people|member|members|channel|channels|board|boards|session|sessions|course|'
    r'courses|lesson|lessons|story|stories|collection|collections|dashboard|dashboards|database|databases|'
    r'calendar|calendars|event|events|deck|decks|app|apps|repo|repos)$', re.I)
ROUTE_WORD = re.compile(r'^[a-z]+(?:[-_][a-z]+)?$')


def safe_url(url):
    """The form a page URL or link is recorded in: origin and path only (a query or fragment can
    carry a signed credential or a search), every path segment that is not a plain route word
    masked as <id> (trace ids, release SHAs, bundle UUIDs, project and dashboard ids). Relative
    paths keep their shape; an in-page #fragment becomes #<id> unless it is a route word."""
    if not isinstance(url, str) or not url:
        return url
    if url.startswith('#'):
        frag = url[1:]
        return url if ROUTE_WORD.match(frag) and len(frag) <= 20 else '#<id>'
    try:
        x = urlsplit(url)
    except ValueError:
        return '<url>'
    if x.scheme == 'file':
        return 'file:///<local file>'
    if x.scheme and x.scheme not in ('http', 'https'):
        return x.scheme + ':<id>'   # mailto:, tel:, javascript: name a person or carry code
    # hostname and port only: a user:password@ in the authority is never kept. A //host link
    # keeps its host, so an external link never reads as an internal path.
    try:
        host = (x.hostname or '') + (f':{x.port}' if x.port else '')
    except ValueError:
        return '<url>'
    base = f'{x.scheme}://{host}' if x.scheme else (f'//{host}' if x.netloc else '')
    parts = x.path.split('/')
    return base + '/'.join(s if not s or (ROUTE_WORD.match(s) and len(s) <= 20 and not RESOURCE.match(parts[i - 1] if i else ''))
                           else '<id>' for i, s in enumerate(parts))


def sanitize(value):
    if isinstance(value, dict):
        return {key: sanitize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, str):
        # Labels can truncate the DSN before its hostname. Match the key prefix.
        value = re.sub(r'https?://[a-f0-9]{16,}[^\s\"\'<>]*', '[redacted DSN]', value, flags=re.I)
        value = re.sub(r'https?://[^\s\"\'<>]*\.ingest\.[^\s\"\'<>]*', '[redacted DSN]', value, flags=re.I)
        # A token can already be partly masked in the UI (sntrys_****abcd), so * counts as part of it.
        value = re.sub(r'\bsntrys_[*A-Za-z0-9]+', '[redacted token]', value)
        # Signed links are not navigational evidence worth retaining.
        if SIGNED.search(value):
            return '[redacted signed URL]'
    return value


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(sanitize(data), indent=2, ensure_ascii=False) + '\n')


def control_status(control, url):
    if control.get('disabled'):
        return 'blocked', 'Disabled in observed state'
    label = control.get('label', '').strip().casefold()
    if control.get('tag', '').upper() == 'BUTTON':
        if label in {'save', 'save changes', 'save rule', 'save rules', 'save team', 'save avatar',
                     'save for everyone', 'reset all thresholds', 'enable all', 'disable all'}:
            return 'not executed', 'Would save or change persistent account, project or shared settings'
        if label in {'delete', 'remove', 'revoke', 'close account and delete organizations',
                     'remove organization', 'remove team'}:
            return 'not executed', 'Destructive or access-revoking action; capture does not authorize execution'
        if label in {'sign out', 'sign out of all devices'}:
            return 'not executed', 'Would end the owner\'s authenticated session'
        if label == 'skip task':
            return 'not executed', 'Would change the persisted onboarding checklist'
        if label == 'create monitor' and '/monitors/new/settings/' in url:
            return 'not executed', 'Final form submission would create a monitor'
    return 'pending', 'Discovered control; page capture alone does not prove activation'


def validate(source, pages, decisions):
    """Every problem with the reviewed captures, found before anything is written, so a bad
    capture never leaves the package half rewritten."""
    errors = []
    accepted = {name for name, row in decisions.items() if row.get('decision') == 'accept'}
    for page in pages:
        name = page['id']
        decision = decisions.get(name)
        if decision is None:
            continue
        kind = decision.get('decision')
        if kind not in ('accept', 'duplicate', 'reject'):
            errors.append(f'{name}: unknown decision {kind!r}')
            continue
        reading_path = source / f'{name}.json'
        if not reading_path.exists():
            errors.append(f'{name}: missing {reading_path.name}')
            continue
        # Every file the import reads is parsed here, so a malformed one stops it before the
        # first deletion or write.
        parsed = {}
        for path in (reading_path, source / f'{name}.controls.json'):
            if path.exists():
                try:
                    parsed[path.name] = json.loads(path.read_text())
                except ValueError as err:
                    errors.append(f'{name}: {path.name} is not valid JSON ({err})')
        if reading_path.name not in parsed:
            continue
        if kind == 'duplicate' and decision.get('duplicateOf') not in accepted:
            errors.append(f"{name}: duplicateOf {decision.get('duplicateOf')!r} is not an accepted capture")
        if kind != 'accept':
            continue
        shot = source / f'{name}.jpg'
        if not shot.exists():
            errors.append(f'{name}: missing {shot.name}')
            continue
        viewport = parsed[reading_path.name].get('viewport') or {}
        with Image.open(shot) as im:
            size = im.size
        if (abs(size[0] - viewport.get('innerWidth', -9)) > 1
                or abs(size[1] - viewport.get('innerHeight', -9)) > 1):
            errors.append(f'{name}: viewport/image dimension mismatch')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch', choices=['breadth', 'breadth2'], default='breadth')
    parser.add_argument('--source', type=Path)
    args = parser.parse_args()
    batch = args.batch
    source = (args.source or Path.home() / '.design-systems/sentry' / batch).expanduser()
    manifest_path = ROOT / 'raw' / batch / 'import-manifest.json'
    manifest = json.loads(manifest_path.read_text())
    source_inventory = json.loads((source / 'inventory.json').read_text())
    decisions = {row['id']: row for row in manifest['captures']}
    if set(decisions) - {row['id'] for row in source_inventory['pages']}:
        raise ValueError('Manifest references missing source captures')
    spec = importlib.util.spec_from_file_location('library_redact_images', REPO / 'tools/redact_images.py')
    redact = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(redact)
    rules = json.loads((REPO / 'tools/redact-rules/sentry.json').read_text())
    errors = validate(source, source_inventory['pages'], decisions)
    if errors:
        raise ValueError('Not importing; fix these captures first:\n' + '\n'.join(errors))
    shots, readings, actions, controls = {}, {}, [], []
    for page in source_inventory['pages']:
        name = page['id']
        if name not in decisions:
            continue  # A live capture pass may append records not yet reviewed.
        decision = decisions[name]
        expected_group = (batch + '-mixed' if 'embedded' in decision['provenance'] else batch)
        for group in (batch, batch + '-mixed'):
            if decision['decision'] != 'accept' or group != expected_group:
                # Remove only this builder's explicitly reviewed output paths
                # when a later review rejects or reclassifies a capture.
                for suffix in ('.png', '.png.capture.json'):
                    (ROOT / 'screenshots' / group / (name + suffix)).unlink(missing_ok=True)
        if decision['decision'] != 'accept':
            (ROOT / 'raw' / batch / 'readings' / (name + '.json')).unlink(missing_ok=True)
        reading = json.loads((source / f'{name}.json').read_text())
        reading['url'] = safe_url(reading.get('url'))
        theme = decision.get('theme', 'light' if '-light' in name else 'dark')
        action = {
            'id': f'action:{name}', 'parentState': name, 'url': safe_url(page['url']),
            'controlLabel': page['action'], 'location': 'see screenshot and control occurrence rectangles',
            'action': page['action'], 'theme': theme, 'viewport': reading['viewport'],
            'capturedAt': reading['capturedAt'], 'provenance': decision['provenance'],
        }
        if decision['decision'] == 'accept':
            group = batch + '-mixed' if 'embedded' in decision['provenance'] else batch
            shot = f'screenshots/{group}/{name}.png'
            raw = f'raw/{batch}/readings/{name}.json'
            shots[name], readings[name] = shot, raw
            im = Image.open(source / f'{name}.jpg').convert('RGB')
            actual = reading['viewport']
            if abs(im.width - actual['innerWidth']) > 1 or abs(im.height - actual['innerHeight']) > 1:
                raise ValueError(f'{name}: viewport/image dimension mismatch')
            rects, _ = redact.rules_for(rules, shot, im.size)
            pixels = np.array(im)
            for rect in rects:
                redact.paint(pixels, rect)
            (ROOT / shot).parent.mkdir(parents=True, exist_ok=True)
            redact.save_256(Image.fromarray(pixels), ROOT / shot)
            write(ROOT / raw, reading)
            write(ROOT / (shot + '.capture.json'), {
                'schemaVersion': 1, 'capturedAt': reading['capturedAt'],
                'screenshot': Path(shot).name, 'source': decision['provenance'],
                'actual': actual, 'theme': reading['theme'],
                'capture': {'mode': 'viewport', 'originalFormat': 'JPEG',
                            'note': 'Browser CSS-scale JPEG; converted to 256-colour PNG after credential masking.'},
                'png': {'width': im.width, 'height': im.height},
                'dimensionCheck': {'status': 'pass', 'basis': 'Decoded image within one pixel of actual viewport'},
                'visualReview': {'status': 'accepted', 'note': decision['review']},
                'redaction': {'rules': 'tools/redact-rules/sentry.json', 'rectangleCount': len(rects)},
                'cropCoordinates': {'status': 'unverified'},
            })
            action.update(status='explored and captured', observedResult=decision['review'],
                          screenshot=shot, reading=raw)
            if name == 'dashboard-widget-actions-dark':
                action.update(status='pending', observedResult=decision['review'])
        elif decision['decision'] == 'duplicate':
            # The screenshot is filled in after the loop: the original may come later in the list.
            action.update(status='explored and duplicate', duplicateOf=f"action:{decision['duplicateOf']}",
                          observedResult=decision['reason'], screenshot=None)
        else:
            action.update(status='pending', observedResult=decision['reason'],
                          reason='Rejected attempt; needs a settled recapture', screenshot=None)
        actions.append(action)
        control_file = source / f'{name}.controls.json'
        if not control_file.exists():
            action['controlInventoryGap'] = 'First five states predate the control reader; reconcile from live UI'
            continue
        # Preserve occurrences by originating state. A repeated label is not
        # proof of equivalent behaviour and never closes a pending action.
        for index, control in enumerate(json.loads(control_file.read_text())):
            status, reason = control_status(control, page['url'])
            controls.append({
                'id': f'{name}:control:{index}', 'parentState': name,
                'url': safe_url(page['url']), 'controlLabel': control.get('label', ''),
                'location': control.get('rect'), 'tag': control.get('tag'),
                'role': control.get('role'), 'href': safe_url(control.get('href')),
                'action': 'not individually reconciled',
                'observedResult': None, 'theme': theme, 'viewport': reading['viewport'],
                'screenshot': shots.get(name),
                'status': status, 'reason': reason,
            })
    for action in actions:
        if action['status'] == 'explored and duplicate':
            action['screenshot'] = shots[action['duplicateOf'].removeprefix('action:')]
    inventory = {
        'schemaVersion': 1, 'scope': source_inventory.get('scope', 'Sentry safe page and interaction capture'),
        'completion': 'partial; safe interactions, lower-page content, other widths and themes remain pending',
        'sourceManifest': f'raw/{batch}/import-manifest.json',
        'counts': {'captureAttempts': len(actions), 'acceptedScreenshots': len(shots),
                   'actionsByStatus': dict(Counter(row['status'] for row in actions)),
                   'controlOccurrencesByStatus': dict(Counter(row['status'] for row in controls))},
        'notes': [
            'Control occurrences are not unique controls and overlap captured action descriptions; do not add the two counts.',
            'No mutation is authorized by a pending row. Inspect safe action boundaries before activation.',
            'Mixed captures isolate onboarding with embedded product demos; iframe contents were not measured.',
            'This pass does not extend tokens.json. Readings retain computed evidence for future token work.',
        ],
        'actions': actions, 'controlOccurrences': controls,
    }
    write(ROOT / f'raw/{batch}/inventory.json', inventory)
    lines = [f'# Sentry {batch} exploration', '',
             'Partial coverage. The [machine-readable inventory](inventory.json) retains every discovered control occurrence.', '',
             '| Captured action / state | Status | Screenshot | Review |',
             '|---|---|---|---|']
    for row in actions:
        screenshot = f"[View](../../{row['screenshot']})" if row.get('screenshot') else 'Not accepted'
        cells = [row['action'], row['status'], screenshot, row['observedResult']]
        lines.append('| ' + ' | '.join(str(sanitize(c)).replace('|', '\\|').replace('\n', ' ') for c in cells) + ' |')
    (ROOT / f'raw/{batch}/README.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps(inventory['counts'], indent=2))


if __name__ == '__main__':
    main()
