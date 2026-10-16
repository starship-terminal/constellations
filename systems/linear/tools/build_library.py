from pathlib import Path
import json,html,re,xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont
from math import ceil
P=Path(__file__).resolve().parent.parent
E=html.escape
# Evidence classes remain separate so sampled app pixels are not mistaken for CSS.
colors={
 'app':{'canvas':'#09090B','surface':'#121214','raised':'#1A1A1C','popover':'#212123','selected':'#323234','text':'#FFFFFF','muted':'#969699','accent':'#5E6AD2','border':'#2B2B2E'},
 'web':{'canvas':'#08090A','surface':'#0F1011','raised':'#161718','border':'#24282C','text':'#F7F8F8','secondary':'#D0D6E0','muted':'#8A8F98','subtle':'#62666D','primary':'#E5E5E6','accent':'#5E6AD2'},
 'brand':{'mercury-white':'#F4F5F8','nordic-gray':'#222326'},
 'semantic':{'todo':'#A0A0A5','in-progress':'#F2C94C','done':'#5E6AD2','urgent':'#EB5757','success':'#27A644','link':'#4EA7FC'}
}
# Tokens are built by tools/build_tokens.py from the 2026-10-17 measurements; the colours above
# only draw these SVG reconstructions.
def rect(x,y,w,h,fill='#1A1A1C',r=8,stroke='none'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'
def text(x,y,s,size=13,fill='#F7F8F8',weight=400,font='Inter, Arial, sans-serif'):
 return f'<text x="{x}" y="{y}" font-family="{E(font)}" font-size="{size}" font-weight="{weight}" fill="{fill}">{E(str(s))}</text>'
def centered_text(x,y,s,size=13,fill='#F7F8F8',weight=400,font='Inter, Arial, sans-serif'):
 return text(x,y,s,size,fill,weight,font).replace('<text ', '<text text-anchor="middle" ',1)
def control_width(label,size=13,padding=12):
 # Size to the reference fallback font; anchoring remains centered if fonts change.
 try: face=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',size*10)
 except OSError: face=ImageFont.load_default(size=size*10)
 return ceil(face.getlength(label)/10)+2*padding
def line(x,y,x2,y2,color='#2B2B2E'):
 return f'<path d="M{x} {y}H{x2}" stroke="{color}"/>' if y==y2 else f'<path d="M{x} {y}L{x2} {y2}" stroke="{color}"/>'
def circle(x,y,r,c,stroke='none'):
 return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{stroke}"/>'
def svg(w,h,body,title='Linear reference'):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{E(title)}</title>{body}</svg>'
def group(name,body):return f'<g id="{E(name)}">{body}</g>'
def button(label,w=116,bg='#5E6AD2',fg='#FFFFFF',stroke='none',r=9999):
 return rect(0,0,w,28,bg,min(r,14),stroke)+centered_text(w/2,18,label,13,fg,500)
comps={}
def comp(name,w,h,body):
 comps[name]={'width':w,'height':h,'body':body}
 (P/'components'/f'{name}.svg').write_text(svg(w,h,group(name,body),name))
primary_w=control_width('Create issue')
comp('button-primary-default',primary_w,28,button('Create issue',primary_w))
comp('button-primary-hover',primary_w,28,button('Create issue',primary_w,'#707DE1'))
comp('button-primary-focus',primary_w+8,36,rect(1,1,primary_w+6,34,'none',18,'#A0A9FF')+'<g transform="translate(4 4)">'+button('Create issue',primary_w)+'</g>')
comp('button-primary-disabled',primary_w,28,button('Create issue',primary_w,'#363846','#848595'))
for name,label,bg,fg,stroke in [('secondary','Add filter','#1A1A1C','#D0D6E0','#2B2B2E'),('ghost','Display','none','#969699','none'),('danger','Delete','#372022','#F17378','#5D3035')]:
 w=control_width(label)
 comp('button-'+name,w,28,button(label,w,bg,fg,stroke))
web_w=control_width('Get started')
comp('button-web-primary',web_w,32,rect(0,0,web_w,32,'#E5E5E6',16)+centered_text(web_w/2,21,'Get started',13,'#08090A',510))
comp('button-icon',28,28,rect(0,0,28,28,'#1A1A1C',14,'#2B2B2E')+'<path d="M8 14h12M14 8v12" stroke="#D0D6E0" stroke-width="1.5"/>')
tabs='';tab_x=0
for label,selected in [('Overview',True),('Activity',False),('Issues',False)]:
 w=control_width(label)
 tabs+=f'<g transform="translate({tab_x} 0)">'+button(label,w,'#323234' if selected else '#1A1A1C','#FFFFFF' if selected else '#969699','#2B2B2E')+'</g>'
 tab_x+=w+6
comp('tabs-pill',tab_x-6,28,tabs)
comp('field-default',320,36,rect(0.5,.5,319,35,'#121214',8,'#323234')+text(12,23,'Search issues…',13,'#969699'))
comp('field-focus',320,36,rect(1,1,318,34,'#121214',8,'#707DE1')+text(12,23,'Improve onboarding',13))
comp('field-error',320,58,rect(1,1,318,34,'#121214',8,'#EB5757')+text(12,23,'',13)+text(0,53,'Enter a title to continue',12,'#F17378'))
comp('checkbox-checked',18,18,rect(1,1,16,16,'#5E6AD2',4)+'<path d="m5 9 3 3 5-6" fill="none" stroke="white" stroke-width="1.6"/>')
comp('checkbox-empty',18,18,rect(1,1,16,16,'#121214',4,'#55555B'))
comp('switch-on',30,18,rect(0,0,30,18,'#5E6AD2',9)+circle(21,9,6,'#fff'))
comp('switch-off',30,18,rect(0,0,30,18,'#323234',9)+circle(9,9,6,'#969699'))
badge_w=control_width('Performance',11,10)+12
comp('badge-label',badge_w,24,rect(0,0,badge_w,24,'#1A1A1C',12,'#323234')+circle(13,12,3,'#5E6AD2')+centered_text((22+badge_w-10)/2,16,'Performance',11,'#D0D6E0'))
comp('avatar',24,24,circle(12,12,12,'#33567A')+text(5,16,'AL',10,'#fff',500))
comp('shortcut',32,23,rect(.5,.5,31,22,'#212123',5,'#3A3A3E')+centered_text(16,15,'⌘K',10,'#969699',400,'Menlo, monospace'))
comp('tooltip',153,29,rect(0,0,153,29,'#212123',7,'#3A3A3E')+text(10,19,'Search workspace   /',11))
comp('toast-success',320,48,rect(.5,.5,319,47,'#212123',10,'#3A3A3E')+circle(24,24,8,'#27A644')+text(20,28,'✓',11)+text(43,29,'Issue updated',13)+text(293,29,'×',16,'#969699'))
comp('nav-item-selected',220,28,rect(0,0,220,28,'#232325',8)+circle(17,14,6,'none','#969699')+text(33,19,'My issues',13,'#fff',500))
comp('issue-row',720,40,rect(0,0,720,40,'#121214',0)+line(0,39,720,39)+text(16,25,'▥',14,'#969699')+text(42,25,'ENG-128',12,'#969699')+circle(124,20,6,'none','#F2C94C')+text(142,25,'Improve the onboarding flow',13)+rect(480,9,control_width('Design',11,10),22,'#1A1A1C',11,'#323234')+centered_text(480+control_width('Design',11,10)/2,24,'Design',11,'#D0D6E0')+circle(663,20,10,'#33567A')+text(656,24,'AL',9)+text(687,25,'Sep 23',10,'#969699'))
card=rect(.5,.5,287,115,'#1A1A1C',9,'#2B2B2E')+text(14,23,'ENG-128',11,'#969699')+text(14,50,'Improve the onboarding flow',13)+text(14,68,'for new team members',13)+circle(20,94,5,'none','#F2C94C')+text(35,98,'Design',11,'#969699')+circle(263,94,9,'#33567A')
comp('board-card',288,116,card)
pop=rect(.5,.5,279,269,'#212123',10,'#3A3A3E')+text(14,26,'Change status…',13,'#969699')+line(0,42,280,42)
for i,(label,col) in enumerate([('Backlog','#777780'),('Todo','#A0A0A5'),('In Progress','#F2C94C'),('In Review','#67A2EC'),('Done','#5E6AD2'),('Canceled','#969699'),('Duplicate','#969699')]):
 y=48+i*30
 if i==3:pop+=rect(5,y,270,28,'#323234',6)
 pop+=circle(20,y+14,5,'none',col)+text(35,y+19,label,13)+text(253,y+19,str(i+1),11,'#969699')
comp('status-menu',280,270,pop)
modal=rect(.5,.5,639,285,'#1A1A1C',16,'#323234')+text(24,30,'ENG  ›  New issue',12,'#969699')+text(611,30,'×',18,'#969699')+text(24,72,'Issue title',24,'#77777B',500)+text(24,109,'Add description…',14,'#77777B')
chip_x=24
for label in ['Todo','No priority','Assignee','Project']:
 w=control_width(label)
 modal+=f'<g transform="translate({chip_x} 155)">'+button(label,w,'#212123','#D0D6E0','#323234')+'</g>'
 chip_x+=w+8
modal+=line(0,222,640,222)+rect(24,247,14,14,'none',4,'#55555B')+text(47,259,'Create more',12,'#969699')+f'<g transform="translate({616-primary_w} 240)">'+button('Create issue',primary_w)+'</g>'
comp('issue-composer',640,286,modal)
prop=rect(.5,.5,339,259,'#1A1A1C',12,'#2B2B2E')+text(16,30,'Properties',13,'#969699',500)
for i,(a,b) in enumerate([('Status','In Progress'),('Priority','Medium'),('Lead','Alex Lee'),('Dates','Sep 23'),('Teams','Product'),('Labels','Add label')]):prop+=text(16,65+i*32,a,13,'#969699')+text(130,65+i*32,b,13)
comp('property-panel',340,260,prop)
empty=rect(0,0,420,208,'#121214',12)+circle(210,53,18,'#212123')+text(199,60,'◇',24,'#969699')+text(143,106,'No projects yet',18,'#F7F8F8',500)+text(71,135,'Organize related issues around a shared goal.',13,'#969699')+f'<g transform="translate({(420-control_width("New project"))/2} 157)">'+button('New project',control_width('New project'))+'</g>'
comp('empty-state',420,208,empty)
cal=rect(.5,.5,279,305,'#212123',12,'#3A3A3E')+text(16,27,'Target date',13,'#D0D6E0')+rect(12,41,256,32,'#121214',6,'#3A3A3E')+text(22,62,'09/23/2026',13)+text(16,103,'September 2026',13,'#fff',500)+text(230,103,'‹  ›',16,'#969699')
for i,day in enumerate(['S','M','T','W','T','F','S']):cal+=text(21+i*36,132,day,11,'#969699')
for d in range(1,31):
 i=d+1;x=12+(i%7)*36;y=142+(i//7)*28
 if d==23:cal+=rect(x,y,28,26,'#5E6AD2',5)
 cal+=text(x+8,y+18,d,11)
comp('date-picker',280,306,cal)
# Boards use native SVG geometry and named groups, with no bitmap UI baked in.
def board(name,title,subtitle,w,h,body):
 header=text(40,53,'LINEAR / STYLE REFERENCE',12,'#8A8F98',500)+text(40,103,title,32,'#F7F8F8',510)+text(40,135,subtitle,13,'#8A8F98')
 (P/'boards'/f'{name}.svg').write_text(svg(w,h,rect(0,0,w,h,'#08090A',0)+header+body,title))
body=''
for j,(g,vals) in enumerate(colors.items()):
 y=195+j*194;body+=text(40,y,g.upper(),13,'#D0D6E0',500)
 for i,(n,h) in enumerate(vals.items()):
  x=40+i*100;body+=rect(x,y+18,86,76,h,8,'#323234')+text(x,y+115,n,10,'#D0D6E0')+text(x,y+134,h,10,'#8A8F98',400,'Menlo, monospace')
body+=text(40,1005,'APP: screenshot samples + reconstruction • WEB: computed CSS • BRAND: official • SEMANTIC: suggested roles',12,'#8A8F98')
board('01-colors','Color systems','Keep authenticated app, public website, and brand tokens in separate groups.',1200,1040,body)
body=text(40,209,'Inter Variable',48,'#F7F8F8',510)+text(42,243,'UI / navigation / product examples / marketing',14,'#8A8F98')
body+=text(40,327,'Berkeley Mono',40,'#D0D6E0',400,'Berkeley Mono, Menlo, monospace')+text(42,365,'CODE / NUMBERS / TECHNICAL ANNOTATIONS',12,'#8A8F98',400,'Menlo, monospace')
body+=text(40,460,'Tiempos Headline',58,'#F7F8F8',400,'Tiempos Headline, Georgia, serif')+text(42,500,'Editorial exception: Linear Method. Install licensed face for fidelity.',14,'#8A8F98')
for i,(name,size,weight) in enumerate([('Hero / 64 · 510 · 64',64,510),('Section / 48 · 510 · 48',48,510),('Issue / 20 · 590 · 26.6',20,590),('Body / 14 · 400 · 21',14,400),('Navigation / 13 · 510',13,510),('Metadata / 12 · 400',12,400)]):body+=text(650,216+i*78,name,min(size,38),'#F7F8F8',weight)
body+=text(40,585,'Public Inter features: cv01 + ss03. Variable weights: 400, 510, 590.',14,'#D0D6E0')
body+=text(40,620,'Authenticated code preferences: 12px, Regular, Default. Exact code family unverified.',13,'#8A8F98')
for i,r in enumerate([4,6,8,12,16,9999]):
 x=40+i*175;body+=rect(x,700,136,84,'#1A1A1C',min(r,42),'#3A3A3E')+text(x,814,'Radius '+str(r),13,'#D0D6E0')
board('02-type-and-geometry','Typography & geometry','Three measured font families. App geometry is reconstructed at logical pixel scale.',1200,870,body)
body='';names=list(comps)
for i,n in enumerate(names[:23]):
 c=comps[n];col=i%3;row=i//3;x=40+col*385;y=195+row*116
 body+=text(x,y,n,12,'#8A8F98')+f'<g transform="translate({x} {y+18})">'+group(n,c['body'])+'</g>'
board('03-controls','Controls & states','SVG reconstructions. Hover, focus, error, disabled and toast variants are proposed, not observed.',1200,1170,body)
body=''
for n,x,y in [('status-menu',40,185),('date-picker',365,185),('property-panel',700,185),('issue-composer',40,540),('empty-state',710,560),('board-card',40,895),('issue-row',385,920)]:
 c=comps[n];body+=text(x,y-10,n,12,'#8A8F98')+f'<g transform="translate({x} {y})">'+group(n,c['body'])+'</g>'
board('04-components','Menus, panels & composition','Neutral fictional content replaces workspace data. Editable reconstruction geometry.',1200,1050,body)
# Reference icon overview; no third-party icons are represented as original work.
iconbody='';reficons=[]
for f in sorted((P/'icons/reference').glob('*.svg')):
 try:
  root=ET.fromstring(f.read_text()); vb=root.attrib.get('viewBox','0 0 16 16');w=float(vb.split()[2]);h=float(vb.split()[3]);inner='<g fill="'+root.attrib.get('fill','currentColor')+'" stroke="'+root.attrib.get('stroke','none')+'">'+''.join(ET.tostring(c,encoding='unicode') for c in root)+'</g>'
  reficons.append((f.stem,inner,w,h))
 except Exception as ex:print('ICON PARSE',f,ex)
for i,(n,inner,w,h) in enumerate(reficons):
 x=40+(i%6)*188;y=190+(i//6)*115
 iconbody+=rect(x,y,160,88,'#121214',9,'#24282C')+f'<g transform="translate({x+18} {y+16}) scale({20/w})" fill="#D0D6E0" color="#D0D6E0">{inner}</g>'+text(x+10,y+70,n[:24],9,'#8A8F98')
board('05-icons','Icon reference atlas','Extracted from visible public demos. Proprietary reference assets; preserve source attribution.',1200,1040,iconbody)
(P/'components/manifest.json').write_text(json.dumps([{ 'name':n,'file':n+'.svg','width':c['width'],'height':c['height'],'status':'reconstruction','source':'See component matrix in README.md'} for n,c in comps.items()],indent=2))
print('Built',len(comps),'components,',len(reficons),'reference icons and 5 boards')
