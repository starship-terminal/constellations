#!/usr/bin/env python3
"""Import reviewed browser readings and images; raw browser exports stay outside Git.
Usage: python3 tools/import_capture.py /absolute/path/to/cloudflare
Only accepted captures named in accepted.json are imported.
"""
import json, pathlib, re, sys
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parents[1]
source=pathlib.Path(sys.argv[1])
accepted=json.loads((ROOT/'tools/accepted.json').read_text())
manifest=[]
for name,route in sorted(accepted.items()):
    original='account-home-light-desktop' if name=='account-home-dark-desktop' else name
    data=json.loads((source/route/(original+'.json')).read_text())
    image=source/route/(original+('.image' if route=='app' else '.png'))
    im=Image.open(image); size=im.size; fmt=im.format
    # Native pixels, no resizing. Palette copies are layout evidence only.
    im.convert('RGB').quantize(colors=256).save(ROOT/'screenshots'/(name+'.png'))
    data['url']=re.sub(r'/[0-9a-f]{32}(?=/|$)','/:account',data.get('url',''))
    extra=source/route/(original+'.extra.json')
    if extra.exists(): data['extra']=json.loads(extra.read_text())
    data['png']={'width':size[0],'height':size[1]}
    data['originalScreenshotFormat']=fmt
    data['evidence']='Measured: live signed-in dashboard' if route=='app' else 'Measured: public marketing page, not dashboard evidence'
    data['components']=[c for c in data['components'] if c['rect']['width']>2 and c['rect']['height']>2]
    for c in data['components']:
        c['label']=c.pop('text',c.get('label',''))
    (ROOT/'raw'/(name+'.json')).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    manifest.append({'name':name,'route':route,'viewport':data['viewport'],'png':data['png'],'time':data['time'],'review':'Accepted after visual inspection of intended visible state; ordinary viewport boundaries do not assert whole-page coverage.'})
(ROOT/'raw/capture-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Imported {len(manifest)} reviewed captures')
