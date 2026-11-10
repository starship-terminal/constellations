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
    # Stitch only a verified, complete set from the latest run. RAW is reused
    # between captures: a base file newer than every tile means the page now
    # fits one shot and the tiles are stale; a tile much older than the newest
    # is a leftover tail from a taller capture. Both are dropped, never stitched.
    ps.sort()
    base = RAW / f'{name}.png'
    newest = max(f.stat().st_mtime for _, f in ps)
    if base.exists() and base.stat().st_mtime > newest:
        print('dropping stale tiles for', name, '(a fresh single capture is newer)')
        for _, f in ps:
            f.unlink()
        continue
    fresh = [(i, f) for i, f in ps if newest - f.stat().st_mtime < 3600]
    if [i for i, _ in fresh] != list(range(len(fresh))):
        print('skipping', name, ': tile set is not a contiguous run from part0')
        continue
    if len(fresh) != len(ps):
        stale = [f for i, f in ps if (i, f) not in [(j, g) for j, g in fresh]]
        print('dropping', len(ps) - len(fresh), 'stale trailing tile(s) for', name)
        for f in stale:
            f.unlink()
        ps = fresh
    ims = [Image.open(f).convert('RGB') for _, f in ps]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(base)
    for _, f in ps:
        f.unlink()  # consumed: a later shorter capture cannot re-stitch them
    print('stitched', name, sheet.size)

n = 0
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    n += 1
print(n, 'screenshots ->', OUT)
