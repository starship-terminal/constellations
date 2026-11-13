"""Store Playwright captures as 256-colour PNGs in screenshots/.

usage: python3 tools/capture/quantize.py RAW_DIR

Playwright screenshots are already sRGB, so there is no profile conversion, only quantization. A page
taller than one GPU texture is captured by public.mjs as name.part0.png, name.part1.png, ...; those are
stitched top to bottom into name.png first (the stitched full-colour copy stays in RAW_DIR). The
full-colour originals are kept in RAW_DIR only; screenshots/ gets the 256-colour versions that are
committed. Flat UI colours are exact, gradients and photographs band a little, so read exact colours
from raw/css-vars.json and raw/components-computed.json. Adapted from the Coursera kit.
"""
from PIL import Image
import pathlib, re, shutil, sys

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
    ims = [Image.open(f).convert('RGB') for _, f in sorted(ps)]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    print('stitched', name, sheet.size)

n = 0
sides = 0
for f in sorted(RAW.glob('*.png')):
    # '*.partN.png' tiles are stitched above, '*.new.png' are staging files
    # public.mjs renames only on success — a leftover means a rejected shot
    # and must never be published.
    if '.part' in f.name or f.name.endswith('.new.png'):
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    # The capture record travels with its image: a recapture refreshes the
    # sidecar in RAW and this copies the fresh record, not a stale one.
    side = RAW / (f.name + '.capture.json')
    if side.exists():
        shutil.copy2(side, OUT / side.name)
        sides += 1
    n += 1
# Tile records (name.partN.png.capture.json) document the chunks a tall page
# was stitched from; they are committed next to the stitched image.
for f in sorted(RAW.glob('*.part*.png.capture.json')):
    if '.new.' in f.name:
        continue
    m = re.match(r'(.+)\.part(\d+)\.png\.capture\.json$', f.name)
    if not m or not (OUT / f'{m.group(1)}.png').exists():
        continue
    shutil.copy2(f, OUT / f.name)
    sides += 1
print(n, 'screenshots +', sides, 'sidecars ->', OUT)
