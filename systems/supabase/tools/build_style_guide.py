"""Render every measured token and link every retained screenshot."""
import json,html
from pathlib import Path
HERE=Path(__file__).resolve().parent.parent
def leaves(node,prefix=''):
    for k,v in node.items():
        if k.startswith('$'):continue
        if '$value' in v:yield prefix+k,v
        else:yield from leaves(v,prefix+k+'.')
def build():
    tokens=json.loads((HERE/'tokens.json').read_text()); rows=[]
    for name,t in leaves(tokens):
        value=t['$value']; shown=json.dumps(value) if isinstance(value,dict) else str(value)
        swatch=f'<i style="background:{html.escape(shown,quote=True)}"></i>' if t['$type']=='color' else ''
        rows.append(f'<tr><td>{html.escape(name)}</td><td>{swatch}{html.escape(shown)}</td><td>{html.escape(t["$extensions"]["source"])}</td></tr>')
    palette={theme:{k:tokens[theme][group][key]['$value'] for k,group,key in [('page','background','page'),('surface','background','surface'),('text','text','primary'),('border','border','default'),('accent','accent','default')]} for theme in ['dark','light']}
    for theme in palette: palette[theme]['onaccent']=tokens[theme]['component']['primaryButton']['text']['$value']
    gallery=''.join(f'<figure><a href="screenshots/{p.name}"><img loading="lazy" src="screenshots/{p.name}" alt="{p.stem}"></a><figcaption>{p.stem}</figcaption></figure>' for p in sorted((HERE/'screenshots').glob('*.png')))
    doc='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Supabase measured style guide</title><style>body{margin:32px;background:var(--page);color:var(--text);font-family:Inter,system-ui,sans-serif}button{padding:8px 16px;border:1px solid var(--border);border-radius:8px;background:var(--accent);color:var(--onaccent)}table{width:100%;border-collapse:collapse;font-size:13px}td{padding:12px;border:1px solid var(--border);overflow-wrap:anywhere}i{display:inline-block;width:32px;height:24px;vertical-align:middle;margin-right:8px;border:1px solid var(--border)}.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}figure{margin:0;padding:12px;background:var(--surface)}img{width:100%;max-height:420px;object-fit:contain}figcaption{font-size:12px}a{color:inherit}</style><h1>Supabase</h1><p>Measured public landing and signed-in dashboard, 31 October 2026. Paused projects limited database coverage.</p><button id="theme">Switch theme</button><p>This guide is a token specimen, not a dashboard reconstruction. Screenshots show the live UI.</p><h2>Measured tokens</h2><table>ROWS</table><h2>Accepted screenshots</h2><div class="gallery">GALLERY</div><script>const palettes=PALETTES;let theme='dark';function apply(){for(const [k,v] of Object.entries(palettes[theme]))document.documentElement.style.setProperty('--'+k,v);document.getElementById('theme').textContent='Switch to '+(theme==='dark'?'light':'dark')}document.getElementById('theme').onclick=()=>{theme=theme==='dark'?'light':'dark';apply()};apply();</script></html>'''
    (HERE/'style-guide.html').write_text(doc.replace('ROWS',''.join(rows)).replace('GALLERY',gallery).replace('PALETTES',json.dumps(palette)))
if __name__=='__main__':build()
