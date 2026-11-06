"""Render all measured app tokens and link their live screenshot evidence."""
import json,html
from pathlib import Path
R=Path(__file__).resolve().parents[1];t=json.loads((R/'tokens.json').read_text())
def flat(x,p=''):
 for k,v in x.items():
  if k.startswith('$'):continue
  if '$value' in v:yield p+k,v
  else:yield from flat(v,p+k+'.')
rows=[]
for name,v in flat(t):
 value=v['$value'];display=json.dumps(value) if isinstance(value,dict) else str(value)
 swatch=f'<span class="swatch" style="background:{html.escape(display)}"></span>' if v['$type']=='color' else ''
 rows.append(f'<tr data-set="{name.split(".")[0]}"><td>{swatch}{html.escape(name)}</td><td><code>{html.escape(display)}</code></td><td>{html.escape(v["$extensions"]["source"])}</td></tr>')
css=''
for theme in ['light','dark']:
 s=t[theme];css+=f'html[data-theme="{theme}"]{{--page:{s["background"]["page"]["$value"]};--text:{s["text"]["primary"]["$value"]};--muted:{s["text"]["secondary"]["$value"]};--border:{s["border"]["default"]["$value"]};--accent:{s["accent"]["primary"]["$value"]};}}'
# The theme rules go raw into <style>: </ is escaped so a value cannot close it.
css=css.replace('</','<\\/')
body='''<!doctype html><html data-theme="dark"><meta charset="utf-8"><title>Sentry measured style guide</title><style>'''+css+'''body{background:var(--page);color:var(--text);font:14px/1.5 Rubik,Arial,sans-serif;margin:32px}button,a{color:var(--accent)}button{background:var(--page);border:1px solid var(--border);border-radius:6px;padding:8px 12px}h1{font-size:24px}p{color:var(--muted)}table{border-collapse:collapse;width:100%;table-layout:fixed}td,th{text-align:left;border-bottom:1px solid var(--border);padding:12px;overflow-wrap:anywhere}td:last-child{font-size:12px;color:var(--muted)}.swatch{display:inline-block;width:20px;height:20px;vertical-align:middle;margin-right:8px;border:1px solid var(--border)}img{max-width:100%;border:1px solid var(--border)}html[data-theme=light] tr[data-set=dark],html[data-theme=dark] tr[data-set=light]{display:none}</style><h1>Sentry: measured app styles</h1><p>Live signed-in evidence, 31 October 2026. Partial capture. Public marketing styles stay separate. This guide's layout is a reference viewer, not an app reconstruction.</p><button id="theme">Switch theme</button><p><a href="README.md">Coverage and limitations</a> · <a href="components.md">Components</a> · <a href="raw/public/README.md">Public landing evidence</a></p><img id="evidence" src="screenshots/app/trace-dark-waterfall.png" alt="Live trace waterfall"><h2>Every measured app token</h2><table><thead><tr><th>Token</th><th>Value</th><th>Source</th></tr></thead><tbody>'''+''.join(rows)+'''</tbody></table><script>document.getElementById('theme').onclick=()=>{const t=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=t;document.getElementById('evidence').src='screenshots/app/trace-'+t+'-waterfall.png'}</script></html>'''
(R/'style-guide.html').write_text(body)
