"""Store Playwright captures as 256-colour PNGs in screenshots/.

usage: python3 tools/capture/quantize.py RAW_DIR

Playwright screenshots are already sRGB, so there is no profile conversion, only quantization. A page
taller than one GPU texture is captured by public.mjs as name.part0.png, name.part1.png, ...; those are
stitched top to bottom into name.png first, and only when the capture's name.parts.json completion
record lists exactly the tiles on disk (the stitched full-colour copy stays in RAW_DIR). The
full-colour originals are kept in RAW_DIR only; screenshots/ gets the 256-colour versions that are
committed. Flat UI colours are exact, gradients and photographs band a little, so read exact colours
from raw/css-vars.json and raw/components-computed.json. Adapted from the Coursera kit.
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
    # A tile set is stitched only with its completion record: public.mjs writes
    # name.parts.json after the last tile lands, so a set without one (a run
    # killed mid-capture, or tiles dropped) is a partial page, not evidence —
    # skipping it is loud, stitching it would silently truncate the page.
    rec = RAW / f'{name}.parts.json'
    if not rec.exists():
        print(f'  ! {name}: no {rec.name} completion record; leaving {len(ps)} tile(s) unstitched')
        continue
    want = json.loads(rec.read_text()).get('tiles', [])
    ondisk = {f.name for _, f in ps}
    if sorted(want) != sorted(ondisk):
        print(f'  ! {name}: record lists {len(want)} tile(s) but {len(ondisk)} are on disk; leaving unstitched')
        continue
    ims = [Image.open(f).convert('RGB') for _, f in sorted(ps)]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    print('stitched', name, sheet.size)

n = 0
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    n += 1
print(n, 'screenshots ->', OUT)
