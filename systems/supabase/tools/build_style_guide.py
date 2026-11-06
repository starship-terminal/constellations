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
    specimens=[]
    css_names={'fontFamily':'font-family','fontSize':'font-size','fontWeight':'font-weight','lineHeight':'line-height'}
    for name,t in tokens['core']['typography'].items():
        style=';'.join(f'{css_names[k]}:{v}' for k,v in t['$value'].items() if k in css_names)
        specimens.append(f'<article><small>{html.escape(name)}</small><p style="{html.escape(style,quote=True)}">The quick brown fox: 0123456789</p></article>')
    for theme in ['dark','light']:
        samples=[]
        for name,c in tokens[theme]['component'].items():
            style=f"background:{c['bg']['$value']};color:{c['text']['$value']};border-radius:{c['radius']['$value']};height:{c['height']['$value']}"
            samples.append(f'<article><small>{html.escape(name)}</small><div class="component-sample" style="{html.escape(style,quote=True)}">Aa</div></article>')
        warning=tokens[theme]['status']['warning']
        w={k:v['$value'] for k,v in warning.items()}
        samples.append(f'<article style="width:100%"><small>Measured warning</small><div style="background:{w["bg"]};color:{w["text"]};border:1px solid {w["border"]};border-radius:{w["radius"]};padding:{w["padding"]}">Warning title<p style="color:{w["bodyText"]};margin-bottom:0">Measured colours, radius and padding. Sample text and border width are illustrative.</p></div></article>')
        specimens.append(f'<section class="samples" data-sample-theme="{theme}"><h3>{theme.title()} components</h3><p>Measured background, text, radius and height. Width, border and sample content are illustrative. Font stacks use locally available faces; proprietary fonts are not bundled.</p>'+''.join(samples)+'</section>')
    gallery=''.join(f'<figure><a href="screenshots/{p.name}"><img loading="lazy" src="screenshots/{p.name}" alt="{p.stem}"></a><figcaption>{p.stem}</figcaption></figure>' for p in sorted((HERE/'screenshots').glob('*.png')))
    doc='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Supabase measured style guide</title><style>body{margin:32px;background:var(--page);color:var(--text);font-family:Inter,system-ui,sans-serif}button{padding:8px 16px;border:1px solid var(--border);border-radius:8px;background:var(--accent);color:var(--onaccent)}table{width:100%;border-collapse:collapse;font-size:13px}td{padding:12px;border:1px solid var(--border);overflow-wrap:anywhere}i{display:inline-block;width:32px;height:24px;vertical-align:middle;margin-right:8px;border:1px solid var(--border)}.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}figure{margin:0;padding:12px;background:var(--surface)}img{width:100%;max-height:420px;object-fit:contain}figcaption{font-size:12px}a{color:inherit}.samples[hidden]{display:none}.samples{display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start}.samples h3,.samples p{width:100%}.component-sample{width:160px;overflow:auto;box-sizing:border-box;border:1px solid var(--border);display:grid;place-items:center}small{display:block;margin:12px 0}</style><h1>Supabase</h1><p>Measured public landing and signed-in dashboard, 31 October 2026. Paused projects limited database coverage.</p><button id="theme">Switch theme</button><p>This guide is a token specimen, not a dashboard reconstruction. Screenshots show the live UI.</p><h2>Measured specimens</h2>SPECIMENS<h2>Measured tokens</h2><table>ROWS</table><h2>Accepted screenshots</h2><div class="gallery">GALLERY</div><script>const palettes=PALETTES;let theme='dark';function apply(){for(const [k,v] of Object.entries(palettes[theme]))document.documentElement.style.setProperty('--'+k,v);document.querySelectorAll('[data-sample-theme]').forEach(el=>el.hidden=el.dataset.sampleTheme!==theme);document.getElementById('theme').textContent='Switch to '+(theme==='dark'?'light':'dark')}document.getElementById('theme').onclick=()=>{theme=theme==='dark'?'light':'dark';apply()};apply();</script></html>'''
    (HERE/'style-guide.html').write_text(doc.replace('SPECIMENS',''.join(specimens)).replace('ROWS',''.join(rows)).replace('GALLERY',gallery).replace('PALETTES',json.dumps(palette)))
if __name__=='__main__':build()
