"""Build Sentry app tokens from live computed styles. Public CSS stays separate."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):return json.loads((ROOT/'raw/app'/f'{name}.json').read_text())
def token(value,kind,source):return {'$type':kind,'$value':value,'$extensions':{'source':'Measured: '+source}}
def component(name,predicate):
 d=load(name)
 i,c=next((i,c) for i,c in enumerate(d['components']) if predicate(c))
 return c['styles'],f'raw/app/{name}.json components[{i}] ({c["tag"]} {c["label"][:45]})'
def build():
 out={'$description':'Live Sentry web app measurements, 2026-10-31. Partial coverage; public marketing values excluded.','core':{},'light':{},'dark':{}}
 base=load('foundations-dark')['elements'][1]['styles']
 out['core']['font']={'sans':token(base['fontFamily'],'fontFamily','raw/app/foundations-dark.json body fontFamily')}
 for theme in ['light','dark']:
  t=out[theme]
  if theme=='dark':bg,fg=base['backgroundColor'],base['color']
  else:
   body=load('foundations-light')['body'];bg,fg=body['background'],body['color']
  t['background']={'page':token(bg,'color',f'raw/app/foundations-{theme}.json body background'),'surface':token(bg,'color',f'raw/app/foundations-{theme}.json body background; same observed main surface')}
  muted,ms=component(f'traces-{theme}-list',lambda c:c['role']=='tab' and c['label']=='Trace Samples')
  active,acs=component(f'traces-{theme}-list',lambda c:c['role']=='tab' and c['label']=='Span Samples')
  field,fs=component(f'command-{theme}-dialog',lambda c:c['tag']=='INPUT' and c['label']=='Search commands')
  t['text']={'primary':token(fg,'color',f'raw/app/foundations-{theme}.json body color'),'secondary':token(muted['color'],'color',ms+' color')}
  t['accent']={'primary':token(active['color'],'color',acs+' color; selected tab text, not filled button')}
  t['border']={'default':token(field['border-color'],'color',fs+' border-color')}
  t['component']={'search':{key:token(field[prop],kind,fs+' '+prop) for key,prop,kind in [('background','background-color','color'),('text','color','color'),('radius','border-radius','dimension'),('height','height','dimension'),('focus-shadow','box-shadow','shadow')]}}
  t['syntax']={k.removeprefix('--prism-'):token(v,'color',f'raw/app/command-{theme}-dialog.json root {k}') for k,v in load(f'command-{theme}-dialog')['customProperties'].items() if k.startswith('--prism-')}
 roles={'body':token({key:base[prop] for key,prop in [('fontFamily','fontFamily'),('fontSize','fontSize'),('fontWeight','fontWeight'),('lineHeight','lineHeight')]},'typography','raw/app/foundations-dark.json elements[1] body computed typography')}
 for role,name,predicate in [('button','issues-dark-empty',lambda c:c['tag']=='BUTTON' and c['label']=='Ask Seer'),('caption','trace-dark-waterfall',lambda c:c['tag']=='INPUT' and c['styles']['font-size']=='12px')]:
  s,src=component(name,predicate)
  roles[role]=token({'fontFamily':s['font-family'],'fontSize':s['font-size'],'fontWeight':int(s['font-weight']),'lineHeight':s['line-height'],'letterSpacing':s['letter-spacing']},'typography',src+' computed typography')
 out['core']['typography']=roles
 # Preserve observed sizes only. No interpolated or inferred scale steps.
 for group,prop in [('radius','border-radius'),('sizing','height')]:
  values={}
  for name in ['issues-dark-empty','trace-dark-waterfall','command-dark-dialog']:
   for i,c in enumerate(load(name)['components']):
    v=c['styles'][prop]
    if c['tag'] in ['INPUT','BUTTON'] and re.fullmatch(r'\d+(\.\d+)?px',v) and float(v[:-2])>0:
     if group=='sizing' and not 20<float(v[:-2])<50:continue
     values.setdefault(v,f'raw/app/{name}.json components[{i}] {prop}')
  out['core'][group]={f'observed-{i}':token(v,'dimension',src) for i,(v,src) in enumerate(sorted(values.items(),key=lambda x:float(x[0][:-2])))}
 out['$extensions']={'notTokenised':{'motion':'Search inputs expose 0.12s transitions and cubic-bezier(0.72,0,0.16,1); retained in raw readings. Reduced motion not captured.','missing':'No complete primitive ramps, status palette, spacing scale, pressed/hover variants or mobile app measurements. Feedback form shadow DOM is screenshot-only.'}}
 (ROOT/'tokens.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':build()
