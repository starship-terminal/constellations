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

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


def sanitize(value):
    if isinstance(value, dict):
        return {key: sanitize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, str):
        # Labels can truncate the DSN before its hostname. Match the key prefix.
        value = re.sub(r'https?://[a-f0-9]{16,}[^\s\"\'<>]*', '[redacted DSN]', value, flags=re.I)
        value = re.sub(r'https?://[^\s\"\'<>]*\.ingest\.[^\s\"\'<>]*', '[redacted DSN]', value, flags=re.I)
        value = re.sub(r'\bsntrys_[A-Za-z0-9]+\b', '[redacted token]', value)
        # Signed links are not navigational evidence worth retaining.
        if re.search(r'[?&](?:signature|x-amz-signature|token|access_token)=', value, re.I):
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
        theme = decision.get('theme', 'light' if '-light' in name else 'dark')
        action = {
            'id': f'action:{name}', 'parentState': name, 'url': page['url'],
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
            action.update(status='explored and duplicate', duplicateOf=f"action:{decision['duplicateOf']}",
                          observedResult=decision['reason'], screenshot=shots[decision['duplicateOf']])
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
                'url': page['url'], 'controlLabel': control.get('label', ''),
                'location': control.get('rect'), 'tag': control.get('tag'),
                'role': control.get('role'), 'href': control.get('href'),
                'action': 'not individually reconciled',
                'observedResult': None, 'theme': theme, 'viewport': reading['viewport'],
                'screenshot': shots.get(name),
                'status': status, 'reason': reason,
            })
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
