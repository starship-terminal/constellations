#!/usr/bin/env python3
"""Render every token from the measured light-only demo package."""
import json,html
from pathlib import Path
P=Path(__file__).resolve().parent.parent
T=json.loads((P/'tokens.json').read_text())
def flat(n,p=''):
 for k,v in n.items():
  if k.startswith('$'):continue
  if '$value' in v:yield p+k,v
  else:yield from flat(v,p+k+'.')
def val(p):
 n=T
 for k in p.split('.'):n=n[k]
 return n['$value']
rows=[]
for k,t in flat(T):
 v=t['$value'];sw=f'<span class="swatch" style="background:{html.escape(v)}"></span>' if t['$type']=='color' else ''
 rows.append(f'<tr><td>{html.escape(k)}</td><td>{sw}{html.escape(str(v))}</td><td>{html.escape(t["$extensions"]["source"])}</td></tr>')
s=f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Metabase: Edumation demo measured style guide</title><style>body{{font-family:{val('core.fontFamily.sans')};color:{val('light.text.primary')};background:{val('light.background.page')};margin:32px;line-height:1.5}}h1{{font-size:28px}}.notice{{padding:16px;border:1px solid {val('light.border.default')};border-radius:{val('core.radius.card')}}}button{{background:{val('light.accent.default')};color:{val('light.text.onAccent')};border:0;border-radius:{val('core.radius.control')};height:{val('core.sizing.control')};padding:0 15px;font-weight:600}}table{{border-collapse:collapse;width:100%;font-size:13px}}td,th{{text-align:left;padding:12px;border-bottom:1px solid {val('light.border.default')};overflow-wrap:anywhere}}.swatch{{display:inline-block;width:24px;height:24px;border:1px solid #ccc;vertical-align:middle;margin-right:10px}}img{{max-width:100%;height:auto}}a{{color:{val('light.accent.default')}}}</style><h1>Metabase / Edumation demo</h1><p class="notice">Measured live from the official interactive demo. Custom purple branding, light only. No dark theme was captured. Inter is not bundled; the system sans-serif fallback may render here.</p><p><button>Visualize</button> <a href="components.md">Component evidence</a></p><h2>Visual query builder</h2><img src="screenshots/query-builder-light-desktop.png" alt="Captured unsaved visual query builder"><h2>All measured tokens</h2><table><thead><tr><th>Token</th><th>Value</th><th>Evidence</th></tr></thead><tbody>{''.join(rows)}</tbody></table></html>'''
(P/'style-guide.html').write_text(s)
