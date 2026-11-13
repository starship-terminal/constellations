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


def meta_ok(side):
    """The .capture.json sidecar screenshot.mjs writes next to every PNG: only a
    'pass' dimensionCheck may replace a published screenshot. A missing sidecar
    means the image came from elsewhere (a stitched sheet has none — its tiles
    were each checked) and is allowed through."""
    if not side.exists():
        return True
    try:
        return json.loads(side.read_text()).get('dimensionCheck', {}).get('status') == 'pass'
    except (OSError, ValueError):
        return False


parts = {}
sidecars = {}
for f in RAW.glob('*.part*.png'):
    m = re.match(r'(.+)\.part(\d+)\.png$', f.name)
    if not m:   # a name such as x.partial.png is not a tile
        continue
    parts.setdefault(m.group(1), []).append((int(m.group(2)), f))
for f in RAW.glob('*.capture.json'):
    m = re.match(r'(.+)\.part(\d+)\.png\.capture\.json$', f.name)
    if m:
        sidecars.setdefault(m.group(1), {})[int(m.group(2))] = f
skip = set()
for name, ps in parts.items():
    have = {i for i, _ in ps}
    meta = sidecars.get(name, {})
    # A tile that failed mid-capture leaves either a missing PNG or a failed
    # .capture.json behind; stitching around it would publish a shortened page
    # over the last good one, so the whole sheet is skipped instead.
    want = set(range(max(have | set(meta)) + 1))
    bad_meta = [i for i, s in meta.items() if not meta_ok(s)]
    if have != want or bad_meta:
        print(f'! {name}: incomplete tile set or failed capture '
              f'(have parts {sorted(have)}, sidecars {sorted(meta)}, failed {bad_meta}); '
              f'not stitching — keeping any earlier {name}.png')
        skip.add(f'{name}.png')
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
    if '.part' in f.name or f.name in skip:
        continue
    if not meta_ok(pathlib.Path(str(f) + '.capture.json')):
        print('! skipping', f.name, '(failed .capture.json check); keeping any earlier copy')
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    n += 1
print(n, 'screenshots ->', OUT)
