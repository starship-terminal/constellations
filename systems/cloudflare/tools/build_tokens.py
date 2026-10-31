#!/usr/bin/env python3
"""Deterministic DTCG tokens from browser computed CSS, without completing missing scales."""
import json, pathlib, re, collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
def read(name): return json.loads((ROOT/'raw'/f'{name}.json').read_text())
def token(v,t,source): return {'$type':t,'$value':v,'$extensions':{'source':'Measured: '+source}}
def var(data,name,file,t='color'): return token(data['variables'][name],t,f'raw/{file}.json variables.{name}')
def elem(data,tag=None,label=None):
 return next(c for c in data['components'] if (tag is None or c['tag']==tag) and (label is None or c['label']==label))
def style(data,c,prop,file,t): return token(c['styles'][prop],t,f'raw/{file}.json {c["tag"]} {c["label"]!r} computed {prop}')
appfile='custom-rule-empty-dark-desktop'; app=read(appfile)
h=elem(app,'H1'); inp=elem(app,'INPUT'); link=elem(app,label='Edit expression')
core={'font':{'sans':style(app,h,'font-family',appfile,'fontFamily'),'mono':var(app,'--font-mono',appfile,'fontFamily')},'radius':{},'typography':{},'spacing':{},'sizing':{},'layout':{},'motion':{}}
for k in ['sm','md','lg']: core['radius'][k]=var(app,'--radius-'+k,appfile,'dimension')
for role,c in [('heading',h),('body',inp),('button',link)]:
 s=c['styles'];core['typography'][role]=token({'fontFamily':s['font-family'],'fontSize':s['font-size'],'fontWeight':int(s['font-weight']),'lineHeight':s['line-height'],'letterSpacing':s['letter-spacing']},'typography',f'raw/{appfile}.json {c["tag"]} {c["label"]!r} computed typography')
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
  result[theme]['component']['input']={n:style(d,inp,p,file,t) for n,p,t in [('background','background-color','color'),('text','color','color'),('height','height','dimension'),('radius','border-radius','dimension')]}
  result[theme]['component']['link']={'text':style(d,link,'color',file,'color')}
 # Preserve directly readable color declarations; do not tokenize unresolved light-dark().
 result[theme]['declared']={k[2:]:var(d,k,file) for k,val in sorted(v.items()) if (k.startswith('--color-') or k.startswith('--cf-') or k.startswith('--text-color-')) and (val.startswith('#') or val.startswith('oklch('))}
file='public-home-desktop';d=read(file)
result['marketing']={'background':{'page':var(d,'--color-background-200',file),'surface':var(d,'--color-background-content',file)},'text':{'primary':var(d,'--color-foreground',file),'secondary':var(d,'--color-text-secondary',file)},'accent':{'default':var(d,'--text-color-kumo-brand',file)},'border':{'default':var(d,'--color-border',file)}}
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
print('Built measured tokens')
