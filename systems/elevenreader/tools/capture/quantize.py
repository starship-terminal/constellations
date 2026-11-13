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
import json, pathlib, re, sys

REF = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1])
OUT = REF / 'screenshots'
OUT.mkdir(exist_ok=True)


def dim_failed(f):
    """Whether the capture sidecar rejects f: screenshotWithMetadata saves the
    PNG and can then reject it for a dimension mismatch, and the rejected PNG
    stays in RAW. A True return means <name>.png.capture.json exists and does
    NOT report status pass; None means no sidecar (the file was not written by
    screenshotWithMetadata, so there is no check to honour)."""
    side = f.with_name(f.name + '.capture.json')
    if not side.exists():
        return None
    try:
        return json.loads(side.read_text()).get('dimensionCheck', {}).get('status') != 'pass'
    except Exception as e:
        print('  unreadable sidecar', side.name, '-', e)
        return True


stitched = set()
parts = {}
for f in RAW.glob('*.part*.png'):
    m = re.match(r'(.+)\.part(\d+)\.png$', f.name)
    if not m:   # a name such as x.partial.png is not a tile
        continue
    parts.setdefault(m.group(1), []).append((int(m.group(2)), f))
for name, ps in parts.items():
    tiles = [f for _, f in sorted(ps)]
    # A rejected tile must not reach the stitched sheet: the sheet is only as
    # good as its worst tile.
    bad = [f.name for f in tiles if dim_failed(f)]
    if bad:
        print('  skip', name, '- tile(s) the sidecar rejected:', ', '.join(bad))
        continue
    ims = [Image.open(f).convert('RGB') for _, f in sorted(ps)]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    stitched.add(f'{name}.png')
    print('stitched', name, sheet.size)

n = 0
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    if f.name not in stitched and dim_failed(f):
        print('  skip', f.name, '- capture sidecar rejects it (no passing dimension check)')
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    n += 1
print(n, 'screenshots ->', OUT)
