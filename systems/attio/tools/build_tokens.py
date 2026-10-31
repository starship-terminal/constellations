#!/usr/bin/env python3
"""Deterministic measured Attio tokens. Never infer dark colours from :root.

Source indices address frozen scoped readings, not live DOM positions. Scope
variables are retained under cssVariable with their opaque names, without
invented semantics. Semantic roles below come from actual rendered elements.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
out = {'core': {}, 'light': {}, 'dark': {}}

def put(tree, path, value, kind, source):
    parts = path.split('.')
    for key in parts[:-1]:
        tree = tree.setdefault(key, {})
    tree[parts[-1]] = {'$value': value, '$type': kind,
                         '$extensions': {'source': 'Measured: ' + source}}

for theme in ['light', 'dark']:
    name = f'companies-{theme}-scoped.json'
    raw = json.loads((HERE / 'raw' / name).read_text())
    rows = raw['elements']
    for role, index, prop in [
        ('page', 0, 'backgroundColor'), ('surface', 10, 'backgroundColor'),
        ('text.primary', 116, 'color'), ('text.secondary', 282, 'color'),
        ('text.onAccent', 253, 'color'), ('text.link', 390, 'color'),
        ('accent.default', 249, 'backgroundColor')]:
        put(out[theme], 'role.'+role, rows[index]['styles'][prop], 'color',
            f'raw/{name} elements[{index}].styles.{prop}; {raw["viewport"]["width"]} CSS px')
    # Actual table separator custom property, matched to cell border readings.
    key='--x1ir7zyd'
    put(out[theme], 'role.border.default', raw['mainVars'][key], 'color', f'raw/{name} main computed {key}; table cell border')
    for key, value in sorted(raw['mainVars'].items()):
        if value.startswith('#'):
            put(out[theme], 'cssVariable.'+key.lstrip('-'), value, 'color', f'raw/{name} main computed {key}; role unassigned')
    for component, index in [('primaryButton',249),('iconButton',302),('toolbarButton',232),('sidebar',10),('tableLabel',433)]:
        for prop, kind in [('backgroundColor','color'),('color','color'),('borderRadius','dimension'),('height','dimension'),('fontFamily','fontFamily'),('fontSize','dimension'),('fontWeight','fontWeight'),('lineHeight','dimension'),('boxShadow','shadow'),('padding','string'),('gap','string'),('transitionDuration','string'),('transitionTimingFunction','string')]:
            value=rows[index]['styles'][prop]
            put(out[theme], f'component.{component}.{prop}',value,kind,f'raw/{name} elements[{index}].styles.{prop}; default state')
    if theme == 'light':
        put(out['core'],'fontFamily.body',rows[433]['styles']['fontFamily'],'fontFamily',f'raw/{name} elements[433].styles.fontFamily')
        for prop in ['fontSize','lineHeight','letterSpacing']:
            put(out['core'],'type.table.'+prop,rows[433]['styles'][prop],'dimension',f'raw/{name} elements[433].styles.{prop}')
        for key,value in sorted(raw['mainVars'].items()):
            if value.endswith('px') and value[:-2].isdigit():
                put(out['core'],'dimension.'+key.lstrip('-'),value,'dimension',f'raw/{name} main computed {key}; role unassigned')
(HERE / 'tokens.json').write_text(json.dumps(out,indent=2)+'\n')
print('Built measured tokens from frozen scoped readings.')
