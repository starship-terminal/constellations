from pathlib import Path
import json,html,re,base64
from PIL import ImageFont
from fontTools.ttLib import TTFont
root=Path(__file__).resolve().parent.parent
font=TTFont(root/'assets/inter.woff2');font.flavor=None;font.save(root/'assets/inter-preview.ttf')
tokens=json.loads((root/'assets/tokens.json').read_text())
def esc(s):return html.escape(str(s),quote=True)
def px(v):return float(v[:-3])*16 if v.endswith('rem') else float(v[:-2])
def rect(x,y,w,h,fill='#fff',r=8,stroke='none'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'
def text(x,y,s,size=13,weight=450,fill='#303030',anchor='start'):return f'<text x="{x}" y="{y}" font-family="Inter, Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>'
def width(s,size=13):return ImageFont.truetype(str(root/'assets/inter-preview.ttf'),size).getlength(s)
def svg(body,w,h):
 font_data=base64.b64encode((root/'assets/inter.woff2').read_bytes()).decode()
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><style>@font-face{{font-family:Inter;src:url(data:font/woff2;base64,{font_data}) format("woff2");font-weight:100 900}}</style></defs>{body}</svg>'
def control(label,fill,ink,size=13,height=28,r=8,pad=12,stroke='none',icon=None):
 w=round(width(label,size)+2*pad+(24 if icon else 0),2)
 content=rect(0,0,w,height,fill,r,stroke)
 if icon:
  raw=(root/'icons'/icon).read_text();raw=re.sub(r'<svg\b[^>]*>','',raw);raw=raw.rsplit('</svg>',1)[0]
  content+=f'<g transform="translate({pad}, {(height-20)/2})" fill="{ink}">{raw}</g>'
 content+=text(pad+(24 if icon else 0)+width(label,size)/2,height/2+size*.35,label,size,550,ink,'middle')
 return content,w,height
items=[]
def add(name,b,w,h):
 (root/'components'/f'{name}.svg').write_text(svg(b,w,h));items.append((name,b,w,h))
for label,fill,ink,stroke in [('Primary',tokens['color-bg-fill-brand'],tokens['color-text-brand-on-bg-fill'],'none'),('Secondary',tokens['color-bg-fill'],tokens['color-text'],tokens['color-border']),('Critical',tokens['color-bg-fill-critical'],tokens['color-text-critical-on-bg-fill'],'none'),('Disabled',tokens['color-bg-fill-disabled'],tokens['color-text-disabled'],'none'),('Tertiary','none',tokens['color-text'],'none')]:
 b,w,h=control('Save product' if label!='Critical' else 'Delete product',fill,ink,stroke=stroke);add('button-'+label.lower(),b,w,h)
for size,h in [('micro',24),('medium',28),('large',32)]:
 b,w,h=control('Add product',tokens['color-bg-fill-brand'],'white',height=h,size=14 if size=='large' else 13,icon='PlusIcon.svg');add('button-icon-'+size,b,w,h)
for name,tone in [('Paid','success'),('Draft',None),('Pending','caution'),('Overdue','critical'),('Information','info'),('Warning','warning')]:
 fill=tokens['color-bg-fill-'+tone+'-secondary'] if tone else tokens['color-bg-fill-transparent-secondary'];ink=tokens['color-text-'+tone] if tone else tokens['color-text-secondary'];b,w,h=control(name,fill,ink,height=20,pad=8);add('badge-'+name.lower(),b,w,h)
for label in ['Wholesale','VIP customer','Summer collection']:
 w=round(width(label)+36,2);b=rect(0,0,w,24,tokens['color-bg-fill-tertiary'])+text(8,16,label)+f'<path d="M{w-17} 8l8 8m0-8l-8 8" stroke="#616161" stroke-width="1.5"/>';add('tag-'+label.lower().replace(' ','-'),b,w,24)
for variant in ['default','focus','error','disabled']:
 fill=tokens['color-input-bg-surface'];stroke=tokens['color-border-critical'] if variant=='error' else tokens['color-input-border'];b=text(0,13,'Product title')
 if variant=='focus':b+=rect(1,23,318,38,'none',10,'#005bd3')
 b+=rect(4,26,312,32,fill,8,stroke)+text(16,47,'Everyday tote',fill=tokens['color-text-disabled'] if variant=='disabled' else '#303030');b+=text(4,78,'Enter a product title' if variant=='error' else 'Visible to your customers',12,450,tokens['color-text-critical'] if variant=='error' else '#616161');add('textfield-'+variant,b,320,90)
for state in ['unchecked','checked','indeterminate']:
 b=rect(1,1,18,18,'#303030' if state!='unchecked' else '#fff',4,'#8a8a8a')
 if state=='checked':b+='<path d="M5 10l3 3 7-7" fill="none" stroke="white" stroke-width="2"/>'
 if state=='indeterminate':b+='<path d="M5 10h10" stroke="white" stroke-width="2"/>'
 b+=text(28,15,'Track quantity');add('checkbox-'+state,b,135,22)
for state in ['off','on']:
 b='<circle cx="10" cy="10" r="9" fill="'+('#303030' if state=='on' else '#fff')+'" stroke="#8a8a8a"/>'
 if state=='on':b+='<circle cx="10" cy="10" r="4" fill="white"/>'
 add('radio-'+state,b+text(28,15,'Physical product'),145,22)
add('card',rect(1,1,358,158,'white',12,'#dedede')+text(17,30,'Product organization',14,650)+text(17,60,'Group related content in a clear surface.')+rect(17,82,326,1,'#e3e3e3',0)+text(17,116,'Collection',13)+text(17,140,'Summer essentials',13,450,'#616161'),360,160)
for tone in ['info','success','warning','critical']:
 add('banner-'+tone,rect(0,0,440,90,tokens['color-bg-surface-'+tone],8)+text(16,28,tone.capitalize()+' message',14,650,tokens['color-text-'+tone])+text(16,56,'Explain the outcome and give a clear next action.',13,450,tokens['color-text-'+tone]),440,90)
add('progress',rect(0,0,320,8,'#e3e3e3',4)+rect(0,0,208,8,tokens['color-bg-fill-brand'],4),320,8)
add('tabs',rect(0,0,105,28,'#e3e3e3',8)+text(12,19,'All products',13,550)+text(121,19,'Active')+text(185,19,'Draft'),260,32)
# Boards are editable reference redraws; exact gradients and bevel effects remain in live CSS.
for start in range(0,len(items),12):
 subset=items[start:start+12];y=112;content=''
 for row in range(0,len(subset),2):
  pair=subset[row:row+2];cell=max(130,max(h for n,b,w,h in pair)+65)
  for col,(n,b,w,h) in enumerate(pair):
   x=40+col*540
   content+=rect(x,y,520,cell,'white',12,'#dedede')+text(x+16,y+25,n,11,550,'#616161')+f'<g transform="translate({x+16},{y+45})">{b}</g>'
  y+=cell+16
 body=rect(0,0,1120,y+24,'#f1f1f1',0)+text(40,52,'Polaris / Component reference',28,650)+text(40,80,'Editable redraws · Desktop light theme · See live CSS for exact bevels and states',13,450,'#616161')+content
 (root/'boards'/f'components-{start//12+1:02}.svg').write_text(svg(body,1120,y+24))
# semantic palette board
colors=[(k,v)for k,v in tokens.items()if k.startswith('color-') and k!='color-scheme']
for start in range(0,len(colors),48):
 chunk=colors[start:start+48];b=rect(0,0,1440,1100,'#f1f1f1',0)+text(32,45,'Polaris / Semantic colors',26,650)
 for i,(k,v) in enumerate(chunk):
  x=32+i%3*468;y=80+i//3*61;b+=rect(x,y,36,36,v,8,'#ddd')+text(x+48,y+14,k,10,550)+text(x+48,y+31,v,10,450,'#616161')
 (root/'boards'/f'colors-{start//48+1:02}.svg').write_text(svg(b,1440,1100))
(root/'evidence/vector-manifest.json').write_text(json.dumps({'components':[n for n,*_ in items],'count':len(items),'status':'Token-based editable redraws. Complex bevels, gradients, responsive behavior and interaction are documented by actual React gallery, not reproduced completely in SVG.'},indent=2))
print(len(items),'component SVGs')
b=rect(0,0,1120,1120,'#fff',0)+text(40,52,'Polaris / Typography',28,650);y=110
for k,v in tokens.items():
 if k.startswith('font-size-'):
  s=px(v);b+=text(40,y,k+' · '+str(s)+'px',11,450,'#616161')+text(270,y,'Products that work · Aa 012345',s,450);y+=s+34
(root/'boards/typography.svg').write_text(svg(b,1120,1120))
b=rect(0,0,1120,1200,'#f1f1f1',0)+text(40,52,'Polaris / Geometry',28,650);y=100
for k,v in tokens.items():
 if k.startswith('border-radius-'):
  b+=rect(40,y,60,48,'#303030',min(px(v),24))+text(125,y+28,k+' · '+str(px(v))+'px');y+=70
(root/'boards/geometry.svg').write_text(svg(b,1120,1200))
