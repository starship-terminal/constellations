#!/usr/bin/env python3
"""Import reviewed browser readings and images; raw browser exports stay outside Git.
Usage: python3 tools/import_capture.py /absolute/path/to/cloudflare
Only accepted captures named in accepted.json are imported.
"""
import importlib.util, json, pathlib, re, sys
import numpy as np
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
# The library's masking primitives, with this package's rules (tools/redact-rules/cloudflare.json):
# every rectangle a rule names for a screenshot is painted before the palette copy is saved.
spec=importlib.util.spec_from_file_location('library_redact_images',REPO/'tools/redact_images.py')
redact=importlib.util.module_from_spec(spec); spec.loader.exec_module(redact)
rules_path=redact.package_rules(ROOT)
rules=json.loads(rules_path.read_text()) if rules_path else {}
def masked(im,rel):
    """The RGB image with every rule rectangle for rel painted; unchanged when none applies."""
    rgb=im.convert('RGB')
    rects,_=redact.rules_for(rules,rel,rgb.size)
    if not rects: return rgb,0
    pixels=np.array(rgb)
    for rect in rects: redact.paint(pixels,rect)
    return Image.fromarray(pixels),len(rects)
def sanitize(value):
    if isinstance(value,str): return re.sub(r'(?<![0-9a-fA-F])[0-9a-fA-F]{32}(?![0-9a-fA-F])',':id',value)
    if isinstance(value,list): return [sanitize(item) for item in value]
    if isinstance(value,dict): return {sanitize(key):sanitize(item) for key,item in value.items()}
    return value
def main(source):
    accepted=json.loads((ROOT/'tools/accepted.json').read_text())
    manifest=[]
    for name,route in sorted(accepted.items()):
        # The source export for the dark account home was saved under a light name; its reading
        # records html.dark-mode and the committed image is dark, so only the file name is wrong.
        original='account-home-light-desktop' if name=='account-home-dark-desktop' else name
        data=json.loads((source/route/(original+'.json')).read_text())
        image=source/route/(original+('.image' if route=='app' else '.png'))
        im=Image.open(image); size=im.size; fmt=im.format
        # Native pixels, no resizing. Palette copies are layout evidence only.
        rgb,_=masked(im,f'screenshots/{name}.png')
        rgb.quantize(colors=256).save(ROOT/'screenshots'/(name+'.png'))
        data['url']=re.sub(r'/[0-9a-f]{32}(?=/|$)','/:account',data.get('url',''))
        extra=source/route/(original+'.extra.json')
        if extra.exists(): data['extra']=json.loads(extra.read_text())
        data=sanitize(data)
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

if __name__=='__main__':
    main(pathlib.Path(sys.argv[1]))
