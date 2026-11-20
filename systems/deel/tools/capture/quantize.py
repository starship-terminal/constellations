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


def passed(f):
    """A shooter's own sidecar must report dimensionCheck pass; a png with no
    sidecar was not written by screenshotWithMetadata (e.g. a stitched sheet)."""
    side = pathlib.Path(str(f) + '.capture.json')
    if not side.exists():
        return True
    meta = json.loads(side.read_text())
    return meta.get('dimensionCheck', {}).get('status') == 'pass'


parts = {}
for f in RAW.glob('*.part*.png'):
    m = re.match(r'(.+)\.part(\d+)\.png$', f.name)
    if not m:   # a name such as x.partial.png is not a tile
        continue
    parts.setdefault(m.group(1), []).append((int(m.group(2)), f))
for name, ps in parts.items():
    ps = sorted(ps)
    manifest = RAW / f'{name}.parts.json'
    have = {i for i, _ in ps}
    if manifest.exists():
        want = json.loads(manifest.read_text())
        tiles = want.get('tiles')
        if tiles is not None:
            if {f.name for _, f in ps} != set(tiles):
                print('skip', name, '- incomplete tile set (a part timed out or failed); rerun the page')
                continue
        elif not want.get('complete') or have != set(range(want.get('parts', -1))):
            print('skip', name, '- incomplete tile set (a part timed out or failed); rerun the page')
            continue
    elif have != set(range(max(have) + 1)):
        print('skip', name, '- no parts manifest and tiles are not contiguous; rerun the page')
        continue
    if not all(passed(f) for _, f in ps):
        print('skip', name, '- a tile sidecar reports a failed capture; rerun the page')
        continue
    ims = [Image.open(f).convert('RGB') for _, f in ps]
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
    if not passed(f):
        print('skip', f.name, '- sidecar reports a failed capture')
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    n += 1
print(n, 'screenshots ->', OUT)
