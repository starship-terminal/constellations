#!/usr/bin/env python3
"""Deterministic DTCG tokens from browser computed CSS, without completing missing scales."""
import json, pathlib, re, collections, math
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(name): return json.loads((ROOT/'raw'/f'{name}.json').read_text())
def token(v,t,source): return {'$type':t,'$value':v,'$extensions':{'source':'Measured: '+source}}
def var(data,name,file,t='color'): return token(data['variables'][name],t,f'raw/{file}.json variables.{name}')
def elem(data,tag=None,label=None):
 return next(c for c in data['components'] if (tag is None or c['tag']==tag) and (label is None or c['label']==label))
def reviewed_input(data, name, rect):
 # This capture did not retain DOM ids or accessible input names. Bind to the
 # visually reviewed field's exact capture rectangle; fail closed on drift.
 matches=[c for c in data['components'] if c['tag']=='INPUT' and c.get('role') is None and c['rect']==rect]
 if len(matches)!=1: raise ValueError(f'Reviewed {name} field: expected exactly one match, got {len(matches)}; review capture before updating selector')
 return matches[0]
def style(data,c,prop,file,t):
 identity=f'{c["tag"]} {c["label"]!r}'
 if c['tag']=='INPUT': identity+=f' at reviewed rect {c["rect"]}'
 return token(c['styles'][prop],t,f'raw/{file}.json {identity} computed {prop}')
appfile='custom-rule-empty-dark-desktop'; app=read(appfile)
h=elem(app,'H1')
inp=reviewed_input(app,'rule-name',{'height':36,'width':848,'x':426,'y':275})
condition_value=reviewed_input(app,'condition-value',{'height':34.5,'width':375.546875,'x':792,'y':522.375})
link=elem(app,label='Edit expression')
core={'font':{'sans':style(app,h,'font-family',appfile,'fontFamily'),'mono':var(app,'--font-mono',appfile,'fontFamily')},'radius':{},'typography':{},'spacing':{},'sizing':{},'layout':{},'motion':{}}
core['borderWidth']={'ruleName':style(app,inp,'border-width',appfile,'dimension'),'conditionValue':style(app,condition_value,'border-width',appfile,'dimension')}
for k in ['sm','md','lg']: core['radius'][k]=var(app,'--radius-'+k,appfile,'dimension')
for role,c in [('heading',h),('body',inp),('button',link)]:
 s=c['styles'];core['typography'][role]=token({'fontFamily':s['font-family'],'fontSize':s['font-size'],'fontWeight':int(s['font-weight']),'lineHeight':s['line-height'],'letterSpacing':s['letter-spacing']},'typography',f'raw/{appfile}.json {c["tag"]} {c["label"]!r} at rect {c["rect"]} computed typography')
core['sizing']['controlHeight']=style(app,inp,'height',appfile,'dimension')
core['spacing']['controlGap']=style(app,inp,'gap',appfile,'dimension')
for name,key in [('smallContent','--container-sm'),('largeContent','--container-6xl'),('breakpoint2xl','--breakpoint-2xl')]: core['layout'][name]=var(app,key,appfile,'dimension')
core['motion']['easeIn']=token([.4,0,1,1],'cubicBezier',f'raw/{appfile}.json --ease-in cubic-bezier(.4, 0, 1, 1)')
result={'core':core}
for theme in ['dark','light']:
 file=appfile if theme=='dark' else 'security-rules-light-desktop'
 if not (ROOT/'raw'/f'{file}.json').exists(): continue
 d=read(file);v=d['variables']; heading=elem(d,'H1')
 # Read actual page and muted roles from extra root readings when available.
 mapping={'background':{'page':'--cf-white','surface':'--color-kumo-base','raised':'--color-kumo-elevated'},'text':{'primary':'--text-color-surface','disabled':'--text-color-disabled'},'accent':{'default':'--color-kumo-brand'},'border':{'default':'--color-border'},'status':{'success':'--color-kumo-success','warning':'--color-kumo-warning','danger':'--text-color-kumo-danger'},'focus':{'color':'--color-kumo-focus'}}
 result[theme]={g:{n:var(d,k,file) for n,k in group.items() if k in v} for g,group in mapping.items()}
 extra_file='security-analytics-dark-desktop' if theme=='dark' else file
 extra=read(extra_file).get('extra',{})
 body=next((r for r in extra.get('roots',[]) if r['selector']=='body'),None)
 if body: result[theme]['background']['page']=token(body['background'],'color',f'raw/{extra_file}.json extra.roots body computed background')
 muted=next(c for c in d['components'] if c['tag']=='P' and c['label'].startswith(('Protect your website','Secure your domain')))
 result[theme]['text']['secondary']=style(d,muted,'color',file,'color')
 result[theme]['component']={'heading':{'text':style(d,heading,'color',file,'color')}}
 if theme=='dark':
  result[theme]['component']['input']={n:style(d,inp,p,file,t) for n,p,t in [('background','background-color','color'),('text','color','color'),('height','height','dimension'),('radius','border-radius','dimension'),('borderWidth','border-width','dimension')]}
  result[theme]['component']['link']={n:style(d,link,p,file,t) for n,p,t in [('text','color','color'),('background','background-color','color'),('height','height','dimension'),('radius','border-radius','dimension'),('borderWidth','border-width','dimension')]}
 # Preserve directly readable color declarations; do not tokenize unresolved light-dark().
 result[theme]['declared']={k[2:]:var(d,k,file) for k,val in sorted(v.items()) if (k.startswith('--color-') or k.startswith('--cf-') or k.startswith('--text-color-')) and (val.startswith('#') or val.startswith('oklch('))}
file='public-home-desktop';d=read(file)
result['marketing']={'background':{'page':var(d,'--color-background-200',file),'surface':var(d,'--color-background-content',file)},'text':{'primary':var(d,'--color-foreground',file),'secondary':var(d,'--color-text-secondary',file)},'accent':{'default':var(d,'--text-color-kumo-brand',file)},'border':{'default':var(d,'--color-border',file)}}
# Derived 8-bit sRGB previews let legacy hex-only consumers use the measured roles.
# OKLCH -> OKLab -> linear sRGB matrices, followed by the sRGB transfer curve.
def srgb_preview(value):
 if value.startswith('#'):
  h=value[1:]
  if len(h)==3: h=''.join(c*2 for c in h)
  if len(h)!=6: raise ValueError(f'Unsupported preview color: {value}')
  return '#'+h.lower(), False, 'hex normalization to 8-bit sRGB'
 m=re.fullmatch(r'oklch\(([^ ]+) +([^ ]+) +([^ )]+)\)',value)
 if not m: raise ValueError(f'Unsupported preview color: {value}')
 lightness,chroma,hue=m.groups()
 L=float(lightness.rstrip('%'))/(100 if lightness.endswith('%') else 1)
 C=float(chroma); H=0 if hue=='none' else float(hue)
 a=C*math.cos(math.radians(H)); b=C*math.sin(math.radians(H))
 l=(L+.3963377774*a+.2158037573*b)**3
 m=(L-.1055613458*a-.0638541728*b)**3
 s=(L-.0894841775*a-1.2914855480*b)**3
 linear=[4.0767416621*l-3.3077115913*m+.2309699292*s,
         -1.2684380046*l+2.6097574011*m-.3413193965*s,
         -.0041960863*l-.7034186147*m+1.7076147010*s]
 clipped=any(c<0 or c>1 for c in linear)
 channels=[max(0,min(1,c)) for c in linear]
 encoded=[12.92*c if c<=.0031308 else 1.055*c**(1/2.4)-.055 for c in channels]
 return '#'+''.join(f'{math.floor(c*255+.5):02x}' for c in encoded),clipped,'OKLCH to OKLab to linear sRGB, sRGB transfer, nearest 8-bit rounding'
for theme in ['dark','light','marketing']:
 result[theme]['preview']={}
 for role,path in {'page':'background.page','surface':'background.surface','text':'text.primary','muted':'text.secondary','accent':'accent.default','border':'border.default'}.items():
  group,key=path.split('.')
  if key not in result[theme].get(group,{}):raise ValueError(f'{theme}.{path}: the reading has no value for this role, so no preview can be derived')
  original=result[theme][group][key]['$value']
  value,clipped,method=srgb_preview(original)
  source=f'Derived: {theme}.{path} ({original}); {method}; '+('out-of-gamut linear channels clipped to [0, 1].' if clipped else 'no gamut clipping.')
  result[theme]['preview'][role]={'$type':'color','$value':value,'$extensions':{'source':source}}
# Keep raw measurement use counts as evidence, separate from semantic-role assignment.
counts={}
for f in sorted((ROOT/'raw').glob('*.json')):
 d=json.loads(f.read_text())
 if not isinstance(d,dict) or 'components' not in d: continue
 counts[f.stem]={p:dict(collections.Counter(c['styles'][p] for c in d['components'] if p in c['styles'])) for p in ['color','background-color','font-size','border-radius']}
(ROOT/'raw/value-use-counts.json').write_text(json.dumps(counts,indent=2)+'\n')
result['$themes']=[{'id':t,'name':t,'selectedTokenSets':{'core':'enabled',t:'enabled'}} for t in ['dark','light','marketing'] if t in result]
result['$extensions']={'notTokenised':'Unresolved light-dark() declarations remain in raw readings. No unobserved hover/pressed states, full scales or missing status roles are inferred. Marketing is a separate public surface, not the dashboard light theme.'}
(ROOT/'tokens.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('Built measured tokens and derived sRGB previews')
