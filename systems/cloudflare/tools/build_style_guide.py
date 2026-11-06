#!/usr/bin/env python3
"""Render measured tokens and native CSS specimens; screenshots remain the live evidence."""
import html,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
t=json.loads((R/'tokens.json').read_text())
def esc(v): return html.escape(str(v),quote=True)
def walk(x,p=''):
 if isinstance(x,dict) and '$value' in x: yield p,x
 elif isinstance(x,dict):
  for k,v in x.items():
   if not k.startswith('$'):yield from walk(v,p+'.'+k if p else k)
def lookup(path):
 value=t
 for key in path.split('.'): value=value[key]
 return value['$value']
rows=[]
for path,x in walk(t):
 val=x['$value'];css=str(val) if isinstance(val,str) else ''
 sw=f'<span class="swatch" style="background:{esc(css)}"></span>' if x['$type']=='color' else ''
 rows.append(f'<tr data-set="{path.split(".")[0]}"><td>{sw}{esc(path)}</td><td>{esc(val)}</td><td>{esc(x["$extensions"]["source"])}</td></tr>')
summaries=[]
theme_values={}
for theme in ['dark','light','marketing']:
 if theme not in t:continue
 theme_values[theme]={role:lookup(f'{theme}.{path}') for role,path in [('page','background.page'),('surface','background.surface'),('text','text.primary'),('muted','text.secondary'),('accent','accent.default'),('border','border.default')]}
 cards=[]
 for role,path in [('Page','background.page'),('Surface','background.surface'),('Text','text.primary'),('Secondary text','text.secondary'),('Accent','accent.default'),('Border','border.default')]:
  val=lookup(f'{theme}.{path}')
  cards.append(f'<div class="palette-card"><div class="palette-fill" style="background:{esc(val)}"></div><strong>{role}</strong><code>{esc(val)}</code><small>{theme}.{path}</small></div>')
 summaries.append(f'<section data-set="{theme}"><h3>{theme.title()}</h3><div class="palette">'+''.join(cards)+'</div></section>')
specimens=[]
for path,x in walk(t['core'],'core'):
 val=x['$value'];kind=x['$type'];sample=''
 if kind=='typography':
  css={k:val[k] for k in ['fontFamily','fontSize','fontWeight','lineHeight','letterSpacing'] if k in val}
  style=';'.join(''.join('-'+c.lower() if c.isupper() else c for c in k)+':'+str(v) for k,v in css.items())
  sample=f'<div class="type-sample" style="{esc(style)}">Protect your website and API</div>'
 elif kind=='fontFamily':
  sample=f'<div class="font-sample" style="font-family:{esc(val)}">Cloudflare · Aa Bb Cc · 0123456789</div>'
 elif kind=='dimension' and path.startswith('core.radius.'):
  sample=f'<div class="radius-sample" style="border-radius:{esc(val)}"></div>'
 elif kind=='dimension' and path.startswith(('core.spacing.','core.sizing.')):
  prop='height' if 'height' in path.lower() else 'width'
  sample=f'<div class="dimension-sample" style="{prop}:{esc(val)}"></div>'
 if sample:
  specimens.append(f'<article class="specimen"><code>{esc(path)}</code>{sample}<small>{esc(val)}</small></article>')
# Only the dark default state has captured component tokens. Do not synthesize
# light, hover, focus or disabled variants from unrelated semantic colors.
i=t['dark']['component']['input']
input_css=';'.join(f'{prop}:{lookup("dark.component.input."+key)}' for prop,key in [('background','background'),('color','text'),('height','height'),('border-radius','radius'),('border-width','borderWidth')])
body_type=lookup('core.typography.body')
input_css+=';'+ ';'.join(f'{prop}:{body_type[key]}' for prop,key in [('font-family','fontFamily'),('font-size','fontSize'),('font-weight','fontWeight'),('line-height','lineHeight'),('letter-spacing','letterSpacing')])
link_css=';'.join(f'{prop}:{lookup("dark.component.link."+key)}' for prop,key in [('background','background'),('color','text'),('height','height'),('border-radius','radius'),('border-width','borderWidth')])
button_type=lookup('core.typography.button')
link_css+=';'+ ';'.join(f'{prop}:{button_type[key]}' for prop,key in [('font-family','fontFamily'),('font-size','fontSize'),('font-weight','fontWeight'),('line-height','lineHeight'),('letter-spacing','letterSpacing')])
components=f'''<section data-set="dark"><h2>Captured component values: dark default state</h2><div class="specimens"><article class="specimen"><h3>Rule-name input</h3><label for="rule-name-preview">Illustrative sample text</label><input id="rule-name-preview" value="Example rule" readonly tabindex="-1" style="{esc(input_css)};box-sizing:border-box;width:100%"><p>Default, unfocused. Fill, text, height, radius and border width use dark.component.input; type uses core.typography.body. Sample width and text are illustrative. The captured shadow ring is not tokenized here.</p></article><article class="specimen"><h3>Edit expression action</h3><button type="button" tabindex="-1" style="{esc(link_css)};pointer-events:none">Edit expression</button><p>Default, unfocused. Text color, fill, height, radius and border width use dark.component.link; type uses core.typography.button. This captured action is a button. Browser padding and specimen placement are illustrative.</p></article></div><p>No light, hover, focus or disabled component preview is inferred.</p></section>'''
photos=''.join(f'<figure><a href="screenshots/{f.name}"><img loading="lazy" src="screenshots/{f.name}" alt="{esc(f.stem)}"></a><figcaption>{esc(f.stem)}</figcaption></figure>' for f in sorted((R/'screenshots').glob('*.png')))
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cloudflare measured style guide</title><style>
body{margin:0;background:var(--page,#101010);color:var(--text,#fafafa);font:14px system-ui,sans-serif}main{max-width:1300px;margin:auto;padding:32px}h1{font-size:28px}h2{margin-top:40px}select{padding:10px;border:1px solid var(--border,#777);border-radius:8px;background:var(--surface);color:inherit}table{width:100%;border-collapse:collapse;table-layout:fixed}td,th{padding:12px;border-bottom:1px solid var(--border,#444);text-align:left;overflow-wrap:anywhere}td:first-child{width:30%}.swatch{display:inline-block;width:22px;height:22px;border:1px solid var(--border,#888);vertical-align:middle;margin-right:8px}.palette,.specimens{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:16px}.palette-card,.specimen{border:1px solid var(--border);border-radius:8px;padding:16px;background:var(--surface);overflow-wrap:anywhere}.palette-fill{height:70px;border:1px solid var(--border);margin-bottom:12px}.palette-card strong,.palette-card code,.palette-card small,.specimen code,.specimen small{display:block;margin-top:8px}.palette-card small,.specimen small{color:var(--muted)}.specimens{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}.type-sample,.font-sample{margin:24px 0;overflow:auto}.font-sample{font-size:20px}.radius-sample{width:80px;height:64px;border:2px solid var(--accent);margin:20px 0;background:var(--page)}.dimension-sample{width:100px;height:24px;margin:20px 0;background:var(--accent)}.shots{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}figure{margin:0}img{max-width:100%;height:260px;object-fit:contain;object-position:top}figcaption{padding:8px}a{color:inherit}[hidden]{display:none!important}
</style><main><h1>Cloudflare measured style guide</h1><p>Live dashboard evidence and separate public marketing captures. Browser-measured values retain their source CSS syntax. No brand assets or fonts are licensed for reuse by this guide.</p><label>Token set <select id="theme"><option value="dark">Dashboard dark</option><option value="light">Dashboard light</option><option value="marketing">Public marketing</option><option value="all">All tokens</option></select></label><h2>Semantic palette</h2>SUMMARIES<h2>Measured type and geometry</h2><p>These specimens apply the measured CSS directly. Font files are not bundled, so missing fonts use the recorded fallbacks. Specimen containers illustrate values and are not captured Cloudflare components.</p><div class="specimens">SPECIMENS</div>COMPONENTS<h2>Every token and its evidence</h2><table><thead><tr><th>Token</th><th>Value</th><th>Evidence</th></tr></thead><tbody>ROWS</tbody></table><h2>Verified live screenshots</h2><div class="shots">PHOTOS</div></main><script>const palettes=PALETTES;function update(){let t=document.querySelector('select').value;let p=palettes[t]||palettes.dark;Object.entries(p).forEach(([k,v])=>document.body.style.setProperty('--'+k,v));document.querySelectorAll('[data-set]').forEach(e=>e.hidden=t!=='all'&&e.dataset.set!==t&&e.dataset.set!=='core')}document.querySelector('select').onchange=update;update()</script></html>'''
for marker,value in [('COMPONENTS',components),('SUMMARIES',''.join(summaries)),('SPECIMENS',''.join(specimens)),('ROWS',''.join(rows)),('PHOTOS',photos),('PALETTES',json.dumps(theme_values))]:page=page.replace(marker,value)
(R/'style-guide.html').write_text(page)
