#!/usr/bin/env python3
"""Deterministically map live demo CSS readings to DTCG tokens. Never infer missing themes."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
T = {'core': {}, 'light': {}, '$themes': [{'id':'light','name':'light','selectedTokenSets':{'core':'enabled','light':'enabled'}}]}
def read(name):
    return json.loads((HERE/'raw'/f'{name}-light-desktop.json').read_text())['reading']['elements']
def pick(name, **fields):
    found=[(i,e) for i,e in enumerate(read(name)) if all(e[k]==v for k,v in fields.items())]
    if not found: raise ValueError((name,fields))
    i,e=found[0]
    return e, f'Measured: raw/{name}-light-desktop.json reading.elements[{i}], light, 1440 CSS px; official Edumation demo custom theme'
def put(path,ty,value,source):
    n=T
    parts=path.split('.')
    for k in parts[:-1]: n=n.setdefault(k,{})
    n[parts[-1]]={'$type':ty,'$value':value,'$extensions':{'source':source}}
def prop(path,ty,name,field,**query):
    e,src=pick(name,**query);put(path,ty,e['styles'][field],src+'; computed '+field)
prop('light.background.page','color','query-builder','backgroundColor',testid='query-builder-root')
prop('light.background.surface','color','dashboard','backgroundColor',testid='dashcard')
prop('light.background.overlay','color','numeric-filter','backgroundColor',testid='clause-popover')
prop('light.text.primary','color','dashboard','color',tag='H1')
prop('light.text.secondary','color','dashboard','color',testid='revision-history-button')
prop('light.text.disabled','color','numeric-filter','color',tag='BUTTON',label='Add filter')
prop('light.text.onAccent','color','query-builder','color',tag='BUTTON',label='Visualize')
prop('light.text.link','color','query-builder','color',tag='A',label='Courses')
prop('light.accent.default','color','query-builder','backgroundColor',tag='BUTTON',label='Visualize')
prop('light.border.default','color','dashboard','borderColor',testid='dashcard')
prop('core.fontFamily.sans','fontFamily','query-builder','fontFamily',tag='BUTTON',label='Visualize')
for role,name,q in [('button','query-builder',{'tag':'BUTTON','label':'Visualize'}),('metric','dashboard',{'tag':'H1'}),('heading','dashboard',{'testid':'dashboard-name-heading'}),('caption','dashboard',{'testid':'revision-history-button'})]:
    e,src=pick(name,**q);s=e['styles'];put('core.typography.'+role,'typography',{k:s[k] for k in ['fontFamily','fontSize','fontWeight','lineHeight','letterSpacing']},src+'; computed type properties')
for role,name,q in [('control','query-builder',{'tag':'BUTTON','label':'Visualize'}),('input','numeric-filter',{'tag':'INPUT'}),('card','dashboard',{'testid':'dashcard'}),('popover','numeric-filter',{'testid':'clause-popover'})]:
    prop('core.radius.'+role,'dimension',name,'borderRadius',**q)
prop('core.borderWidth.control','dimension','query-builder','borderWidth',tag='BUTTON',label='Visualize')
prop('core.sizing.control','dimension','query-builder','height',tag='BUTTON',label='Visualize')
prop('core.sizing.compactControl','dimension','query-builder','height',tag='BUTTON',label='New')
prop('core.layout.chartSidebar','dimension','chart-display','width',testid='sidebar-left')
prop('core.shadow.popover','shadow','numeric-filter','boxShadow',testid='clause-popover')
# Export individual measured component states, not an invented global scale.
for role,name,q in [('primary','query-builder',{'tag':'BUTTON','label':'Visualize'}),('quiet','query-builder',{'tag':'BUTTON','label':'Save'}),('disabled','numeric-filter',{'tag':'BUTTON','label':'Add filter'}),('input','numeric-filter',{'tag':'INPUT'}),('popover','numeric-filter',{'testid':'clause-popover'}),('card','dashboard',{'testid':'dashcard'}),('filter','dashboard',{'testid':'parameter-value-widget-target'})]:
    for key,ty,css in [('bg','color','backgroundColor'),('text','color','color'),('border','color','borderColor'),('radius','dimension','borderRadius'),('height','dimension','height')]:prop(f'light.component.{role}.{key}',ty,name,css,**q)
for group in ['core','light']:
    def check(n):
        for v in n.values():
            if '$value' in v:
                assert v['$value'] and v['$extensions']['source'].startswith('Measured:')
            else: check(v)
    check(T[group])
(HERE/'tokens.json').write_text(json.dumps(T,indent=2)+'\n')
print('tokens built from explicit observed elements')
