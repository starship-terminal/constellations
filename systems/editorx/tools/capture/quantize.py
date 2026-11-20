"""Store Playwright captures as 256-colour PNGs in screenshots/.

usage: python3 tools/capture/quantize.py RAW_DIR

Playwright screenshots are already sRGB, so there is no profile conversion, only quantization. A page
taller than one GPU texture is captured by public.mjs as name.part0.png, name.part1.png, ...; those are
stitched top to bottom into name.png first (the stitched full-colour copy stays in RAW_DIR). The
full-colour originals are kept in RAW_DIR only; screenshots/ gets the 256-colour versions that are
committed. Flat UI colours are exact, gradients and photographs band a little, so read exact colours
from raw/css-vars.json and raw/components-computed.json. Adapted from the Coursera kit.

Every name.png.capture.json sidecar screenshotWithMetadata wrote — viewport, scale, dimension
check, clip/tile details — is copied next to its PNG so the committed screenshots keep their capture
record. A stitched image gets a combined sidecar: mode "stitched", the stitched PNG's own dimensions,
and one tile entry per part sidecar.
"""
from PIL import Image
import json
import pathlib, re, sys

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
    # The stitched image's sidecar combines its tiles' records: each tile
    # keeps its own clip, dimensions and check, and the whole reports the
    # stitched PNG's size and the AND of the tile checks.
    sidecars = []
    for _, f in ps:
        sc = f.with_name(f.name + '.capture.json')
        if sc.exists():
            sidecars.append(json.loads(sc.read_text()))
    if sidecars:
        combined = dict(sidecars[0])
        combined['screenshot'] = f'{name}.png'
        combined['capture'] = {
            'mode': 'stitched',
            'scale': sidecars[0].get('capture', {}).get('scale'),
            'tiles': [{
                'screenshot': s.get('screenshot'),
                'clip': s.get('capture', {}).get('clip'),
                'png': s.get('png'),
                'dimensionCheck': s.get('dimensionCheck'),
                'capturedAt': s.get('capturedAt'),
            } for s in sidecars],
        }
        combined['png'] = {'width': sheet.width, 'height': sheet.height}
        combined['dimensionCheck'] = {
            'status': 'pass' if all(s.get('dimensionCheck', {}).get('status') == 'pass' for s in sidecars) else 'fail',
            'basis': 'stitchedTiles',
        }
        (RAW / f'{name}.png.capture.json').write_text(json.dumps(combined, indent=2) + '\n')
        print('stitched sidecar', name, 'from', len(sidecars), 'tiles')

n = 0
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    sc = f.with_name(f.name + '.capture.json')
    if sc.exists():     # the capture record travels with its PNG
        (OUT / sc.name).write_text(sc.read_text())
    n += 1
print(n, 'screenshots ->', OUT)
