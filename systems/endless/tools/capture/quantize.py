"""Store Playwright captures as 256-colour PNGs in screenshots/.

usage: python3 tools/capture/quantize.py RAW_DIR

Playwright screenshots are already sRGB, so there is no profile conversion, only quantization. A page
taller than one GPU texture is captured by public.mjs as name.part0.png, name.part1.png, ...; those are
stitched top to bottom into name.png first (the stitched full-colour copy stays in RAW_DIR). The
full-colour originals are kept in RAW_DIR only; screenshots/ gets the 256-colour versions that are
committed, plus each shot's sanitized `.capture.json` record (viewport, scale, dimension check and —
for a page that hit the 8-chunk cap — the truncation flag public.mjs drops as name.truncated.json).
Flat UI colours are exact, gradients and photographs band a little, so read exact colours from
raw/css-vars.json and raw/components-computed.json. Adapted from the Coursera kit.
"""
from PIL import Image
import json, pathlib, re, sys

REF = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1])
OUT = REF / 'screenshots'
OUT.mkdir(exist_ok=True)

parts = {}
for f in RAW.glob('*.part*.png'):
    m = re.match(r'(.+)\.part(\d+)\.png$', f.name)
    if not m:   # a name such as x.partial.png is not a tile
        continue
    parts.setdefault(m.group(1), []).append((int(m.group(2)), f))
for name, ps in parts.items():
    ps = sorted(ps)
    ims = [Image.open(f).convert('RGB') for _, f in ps]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    print('stitched', name, sheet.size)
    # The stitched image gets its own capture record, built from the tiles', so
    # the measured viewport, pixel ratio and PNG dimensions survive the merge.
    recs = []
    for _, f in ps:
        side = f.parent / (f.name + '.capture.json')
        if side.exists():
            recs.append(json.loads(side.read_text()))
    if recs:
        rec = dict(recs[0])
        rec['screenshot'] = f'{name}.png'
        rec['capture'] = dict(rec.get('capture') or {}, mode='stitched', clip=None,
                              tiles=[f.name for _, f in ps])
        rec['png'] = {'width': sheet.width, 'height': sheet.height}
        exp = (recs[0].get('dimensionCheck') or {}).get('expected') or {}
        exp_h = sum(((r.get('dimensionCheck') or {}).get('expected') or {}).get('height', 0) for r in recs)
        ok = exp.get('width') == sheet.width and abs(exp_h - sheet.height) <= len(ims)
        rec['dimensionCheck'] = {'status': 'pass' if ok else 'fail',
                                 'expected': {'width': exp.get('width'), 'height': exp_h},
                                 'basis': 'stitched tiles'}
        (RAW / f'{name}.png.capture.json').write_text(json.dumps(rec, indent=2) + '\n')

n = 0
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    n += 1
    # Publish the sanitized capture record beside the image: it is the only
    # place the actual browser width, scale, dimension check and truncation
    # flag survive.
    side = f.parent / (f.name + '.capture.json')
    if side.exists():
        rec = json.loads(side.read_text())
        trunc = f.parent / (f.stem + '.truncated.json')
        if trunc.exists():
            rec['truncated'] = json.loads(trunc.read_text())
            side.write_text(json.dumps(rec, indent=2) + '\n')
        (OUT / side.name).write_text(json.dumps(rec, indent=2) + '\n')
print(n, 'screenshots ->', OUT)
