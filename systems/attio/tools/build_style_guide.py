#!/usr/bin/env python3
"""Render every measured token, with light/dark controls; no brand artwork."""
import html,json
from pathlib import Path
p=Path(__file__).resolve().parent.parent
t=json.loads((p/'tokens.json').read_text())
def flat(node,path=''):
 for k,v in node.items():
  if k.startswith('$'):continue
  name=path+'.'+k if path else k
  if '$value' in v:yield name,v
  else:yield from flat(v,name)
parts=[]
for theme,node in t.items():
 rows=[]
 for name,v in flat(node):
  value=html.escape(str(v['$value']),quote=True)
  swatch=f'<span class="swatch" style="background:{value}"></span>' if v['$type']=='color' else ''
  rows.append(f'<tr><th>{html.escape(name)}</th><td>{swatch}{value}</td><td>{html.escape(v["$extensions"]["source"])}</td></tr>')
 parts.append(f'<section data-theme="{theme}"><h2>{theme.title()}</h2><table>'+''.join(rows)+'</table></section>')
css='''body{font:14px/1.5 Inter,system-ui,sans-serif;margin:32px;background:#fff;color:#101112}body.dark{background:#101112;color:#f1f2f3}button{font:inherit;padding:8px 12px}table{border-collapse:collapse;width:100%}th,td{text-align:left;padding:8px;border-bottom:1px solid #898a8d;vertical-align:top}th{width:30%}td:last-child{font-size:12px}.swatch{display:inline-block;width:24px;height:24px;border:1px solid #898a8d;vertical-align:middle;margin-right:8px}body:not(.dark) [data-theme=dark],body.dark [data-theme=light]{display:none}'''
(p/'style-guide.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Attio measured tokens</title><style>'+css+'</style><h1>Attio measured tokens</h1><p>Frozen web measurements, 31 October 2026. Opaque CSS variable names carry no inferred role. Inter is not bundled.</p><button onclick="document.body.classList.toggle(\'dark\')">Toggle light / dark</button>'+''.join(parts)+'</html>')
