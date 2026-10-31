"""Build only values measured in live Supabase pages. No inferred states."""
import json
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
def read(name):
    return json.loads((HERE / 'raw' / (name + '.json')).read_text())
def token(value, kind, source):
    ext = {'source': 'Measured: ' + source}
    if kind == 'color' and value.startswith('oklch('):
        original = value
        match = re.fullmatch(r'oklch\(([\d.]+) ([\d.]+) ([\d.]+)(?: / ([\d.]+))?\)', value)
        if not match:
            raise ValueError(value)
        L, C, H = map(float, match.groups()[:3])
        a, b = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
        l=(L+.3963377774*a+.2158037573*b)**3
        m=(L-.1055613458*a-.0638541728*b)**3
        s=(L-.0894841775*a-1.2914855480*b)**3
        linear=[4.0767416621*l-3.3077115913*m+.2309699292*s,
                -1.2684380046*l+2.6097574011*m-.3413193965*s,
                -.0041960863*l-.7034186147*m+1.7076147010*s]
        rgb=[round(255*min(1,max(0,12.92*x if x<=.0031308 else 1.055*x**(1/2.4)-.055))) for x in linear]
        alpha=float(match.group(4) or 1)
        value=('#%02x%02x%02x' % tuple(rgb)) if alpha==1 else f'rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, {alpha})'
        ext={'source':'Derived: OKLCH to 8-bit sRGB conversion of Measured: '+source,
             'measuredCss':original,'conversion':'OKLCH to OKLab to linear sRGB; transfer curve; clip to gamut; round channels to 8 bits; alpha retained'}
    return {'$type': kind, '$value': value, '$extensions': ext}
def build():
    out = {'core': {}, 'dark': {}, 'light': {}}
    for theme, name in [('dark', 'app-projects-grid'), ('light', 'app-light-projects-grid')]:
        data = read(name)
        def find(label, tag=None):
            return next((i,c) for i,c in enumerate(data['components']) if c['label']==label and (not tag or c['tag']==tag))
        def t(value, kind, where):
            return token(value,kind,f'raw/{name}.json {where}; live {theme} desktop')
        body=data['body']
        ci,card=next((i,c) for i,c in enumerate(data['components']) if c['label'].startswith('kindlejoy-reading-app ') and c['tag']=='A')
        ai,accent=find('New project')
        si,secondary=find('Sorted by name')
        ii,inp=next((i,c) for i,c in enumerate(data['components']) if c['tag']=='INPUT')
        out[theme]={'background':{'page':t(body['background-color'],'color','body.background-color'), 'surface':t(card['styles']['background-color'],'color',f'components[{ci}].styles.background-color')},
            'text':{'primary':t(body['color'],'color','body.color'),'secondary':token(read('secondary-text')[theme]['color'],'color',f'raw/secondary-text.json {theme}.color; Current billing cycle paragraph')},
            'border':{'default':t(body['border-color'],'color','body.border-color')},
            'accent':{'default':t(accent['styles']['background-color'],'color',f'components[{ai}].styles.background-color')},'component':{}}
        for key,index,element in [('primaryButton',ai,accent),('secondaryButton',si,secondary),('searchField',ii,inp),('card',ci,card)]:
            out[theme]['component'][key]={dest:t(element['styles'][prop],typ,f'components[{index}].styles.{prop}') for prop,dest,typ in [('background-color','bg','color'),('color','text','color'),('border-radius','radius','dimension'),('height','height','dimension')]}
        if theme=='dark':
            core=out['core']
            core['fontFamily']={'body':t(body['font-family'],'fontFamily','body.font-family')}
            core['typography']={}
            for role,index,element in [('label',ai,accent),('heading',*find('Projects','H1'))]:
                st=element['styles'];core['typography'][role]=t({'fontFamily':st['font-family'],'fontSize':st['font-size'],'fontWeight':int(st['font-weight']),'lineHeight':st['line-height'],'letterSpacing':'0px'},'typography',f'components[{index}].styles')
                # Do not invent an unmeasured letter-spacing value.
                del core['typography'][role]['$value']['letterSpacing']
            core['typography']['body']=t({'fontFamily':body['font-family'],'fontSize':body['font-size'],'fontWeight':int(body['font-weight']),'lineHeight':body['line-height']},'typography','body')
            core['radius']={'control':t(accent['styles']['border-radius'],'dimension',f'components[{ai}].styles.border-radius')}
            core['size']={'controlHeight':t(accent['styles']['height'],'dimension',f'components[{ai}].styles.height')}
            core['motion']={'controlDuration':t(accent['styles']['transition-duration'],'duration',f'components[{ai}].styles.transition-duration')}
    for theme in ['dark','light']:
        for name, file, index in [('switchChecked',f'{theme}-switches',0), ('inviteTextareaFocused',f'{theme}-invite',4), ('invitePanel',f'{theme}-invite',0)]:
            data=read('expanded/'+file+'.measurements')
            element=data['components'][index]
            out[theme]['component'][name]={key:token(element['styles'][prop],typ,f'raw/expanded/{file}.measurements.json components[{index}].styles.{prop}; live {theme}') for key,prop,typ in [('bg','background-color','color'),('text','color','color'),('radius','border-radius','dimension'),('height','height','dimension')]}
    header=read('expanded/dark-table.measurements')['components'][0]['styles']
    out['core']['typography']['tableHeader']=token({'fontFamily':header['font-family'],'fontSize':header['font-size'],'fontWeight':int(header['font-weight']),'lineHeight':header['line-height']},'typography','raw/expanded/dark-table.measurements.json components[0].styles; dark team table header')
    for theme in ['dark','light']:
        warning=read('continuation/'+theme+'-warning.measurements')
        out[theme]['status']={'warning':{key:token(warning['styles'][prop],typ,f'raw/continuation/{theme}-warning.measurements.json styles.{prop}; spend-cap warning') for key,prop,typ in [('bg','background-color','color'),('text','color','color'),('border','border-color','color'),('radius','border-radius','dimension'),('padding','padding','dimension')]}}
        out[theme]['status']['warning']['bodyText']=token(warning['children'][2]['styles']['color'],'color',f'raw/continuation/{theme}-warning.measurements.json children[2].styles.color; warning body text')
    out['$themes']=[{'id':theme,'name':theme.title(),'selectedTokenSets':{'core':'enabled',theme:'enabled'}} for theme in ['dark','light']]
    out['$extensions']={'notTokenised': ['Full CSS variable inventory was not captured; exported variables are a partial browser reading.', 'Spacing scale, focus ring, hover and pressed colors, status ramps and breakpoint thresholds not measured.', 'Raw shadows and easing values remain in per-state readings; not generalized into semantic scales.']}
    (HERE/'tokens.json').write_text(json.dumps(out,indent=2)+'\n')
    derived=[]
    def collect(node, prefix=''):
        for key,value in node.items():
            if key.startswith('$'): continue
            if '$value' in value:
                if value['$extensions']['source'].startswith('Derived:'): derived.append(prefix+key)
            else: collect(value,prefix+key+'.')
    collect(out)
    (HERE/'raw/derived-values.json').write_text(json.dumps({'reason':'OKLCH-to-sRGB serialization for catalogue contrast support; originals remain in token measuredCss','paths':derived},indent=2)+'\n')
if __name__=='__main__': build()
