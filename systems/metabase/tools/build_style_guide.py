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
def css(props):
 return html.escape(';'.join(f"{k}:{v}" for k,v in props.items()),quote=True)
def sample(k,t):
 v=t['$value']; ty=t['$type']; styles={}
 text='Aa, Courses 123'
 if ty=='color': return f'<span class="swatch" style="background:{html.escape(v)}"></span>'
 if ty=='typography':
  names={'fontFamily':'font-family','fontSize':'font-size','fontWeight':'font-weight','lineHeight':'line-height','letterSpacing':'letter-spacing'}
  styles={names[p]:x for p,x in v.items()}
 elif ty=='fontFamily':styles={'font-family':v}
 elif ty=='shadow':styles={'box-shadow':v,'padding':'20px','margin':'16px'};text='Popover elevation'
 elif ty=='dimension':
  if 'radius' in k:styles={'border-radius':v,'border':'1px solid #666','padding':'12px'};text='Corner'
  elif 'borderWidth' in k:styles={'border':f'{v} solid #666','padding':'12px'};text='Border'
  elif 'layout' in k:styles={'width':v,'max-width':'100%','background':'#eee'};text='Measured width'
  else:styles={'height':v,'min-width':'48px','background':'#eee','overflow':'hidden'};text='Height'
 return f'<div class="sample" style="{css(styles)}">{text}</div>'
rows=[]
for k,t in flat(T):
 v=t['$value']
 rows.append(f'<tr><td>{html.escape(k)}</td><td>{sample(k,t)}<code>{html.escape(str(v))}</code></td><td>{html.escape(t["$extensions"]["source"])}</td></tr>')
components=[]
for role,group in T['light']['component'].items():
 props={name:group[key]['$value'] for key,name in [('bg','background'),('text','color'),('border','border-color'),('radius','border-radius'),('height','height')]}
 props.update({'border-style':'solid','border-width':val('core.borderWidth.control'),'box-sizing':'border-box','max-width':'100%'})
 if role in ('input','inputFocused'):
  specimen=f'<input aria-label="{role}" readonly value="Axis title" style="{css(props)}">'
 elif role in ('primary','quiet','disabled','filter'):
  disabled='disabled' if role=='disabled' else ''
  specimen=f'<button {disabled} style="{css(props)}">{role}</button>'
 else:
  if role=='popover':props['box-shadow']=val('core.shadow.popover')
  props.update({'width':'240px','overflow':'auto','padding':'16px'})
  specimen=f'<div style="{css(props)}">{role} container</div>'
 components.append(f'<section><h3>{role}</h3>{specimen}</section>')
s=f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Metabase: Edumation demo measured style guide</title><style>body{{font-family:{val('core.fontFamily.sans')};color:{val('light.text.primary')};background:{val('light.background.page')};margin:32px;line-height:1.5}}h1{{font-size:28px}}.notice{{padding:16px;border:1px solid {val('light.border.default')};border-radius:{val('core.radius.card')}}}button{{background:{val('light.accent.default')};color:{val('light.text.onAccent')};border:0;border-radius:{val('core.radius.control')};height:{val('core.sizing.control')};padding:0 15px;font-weight:600}}table{{border-collapse:collapse;width:100%;font-size:13px}}td,th{{text-align:left;padding:12px;border-bottom:1px solid {val('light.border.default')};overflow-wrap:anywhere}}.swatch{{display:inline-block;width:24px;height:24px;border:1px solid #ccc;vertical-align:middle;margin-right:10px}}.sample{{display:block;margin-bottom:8px}}.specimens{{display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start}}.specimens section{{max-width:100%}}code{{font-size:12px}}img{{max-width:100%;height:auto}}a{{color:{val('light.accent.default')}}}</style><h1>Metabase / Edumation demo</h1><p class="notice">Measured live from the official interactive demo. Custom purple branding, light only. No dark theme was captured. Inter is not bundled; the system sans-serif fallback may render here.</p><p><button>Visualize</button> <a href="components.md">Component evidence</a></p><h2>Measured component specimens</h2><p>Static examples apply the measured token groups. Labels and specimen spacing are guide scaffolding; focus styling is shown without claiming keyboard parity.</p><div class="specimens">{''.join(components)}</div><h2>Visual query builder</h2><img src="screenshots/query-builder-light-desktop.png" alt="Captured unsaved visual query builder"><h2>All measured tokens</h2><table><thead><tr><th>Token</th><th>Value</th><th>Evidence</th></tr></thead><tbody>{''.join(rows)}</tbody></table></html>'''
(P/'style-guide.html').write_text(s)
