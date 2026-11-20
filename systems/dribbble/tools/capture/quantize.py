"""Store Playwright captures as 256-colour PNGs in screenshots/.

usage: python3 tools/capture/quantize.py RAW_DIR

Playwright screenshots are already sRGB, so there is no profile conversion, only quantization. A page
taller than one GPU texture is captured by public.mjs as name.part0.png, name.part1.png, ...; those are
stitched top to bottom into name.png first (the stitched full-colour copy stays in RAW_DIR). The
full-colour originals are kept in RAW_DIR only; screenshots/ gets the 256-colour versions that are
committed. Flat UI colours are exact, gradients and photographs band a little, so read exact colours
from raw/css-vars.json and raw/components-computed.json. Adapted from the Coursera kit.

Failed or pending captures are never exported. screenshotWithMetadata
(tools/capture/screenshot.mjs) writes a <name>.png.capture.json sidecar per attempt and marks it
dimensionCheck.status: pass | fail ('pending' while the attempt is in flight). A failed attempt can
still leave a PNG behind — the old file is untouched when the browser probe dies, and a mismatched
PNG is written before its dimensions are rejected — so a PNG whose sidecar says fail or pending is
never stitched or copied into screenshots/. A PNG with no sidecar at all is not a
screenshotWithMetadata product (a hand-placed raw, or a stitch this script wrote), and converts as
before.
"""
from PIL import Image
import json, pathlib, re, sys

REF = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1])
OUT = REF / 'screenshots'
OUT.mkdir(exist_ok=True)


def verdict(f):
    """The sidecar's dimension-check status ('pass', 'fail', 'pending'), or None
    when no .capture.json exists at all. An unreadable sidecar counts as fail."""
    side = pathlib.Path(str(f) + '.capture.json')
    if not side.exists():
        return None
    try:
        return json.loads(side.read_text()).get('dimensionCheck', {}).get('status')
    except Exception:
        return 'fail'


# A tile or shot is publishable unless its own capture result says fail/pending.
publishable = lambda f: verdict(f) in ('pass', None)

parts = {}
for f in RAW.glob('*.part*.png'):
    m = re.match(r'(.+)\.part(\d+)\.png$', f.name)
    if not m:   # a name such as x.partial.png is not a tile
        continue
    parts.setdefault(m.group(1), []).append((int(m.group(2)), f))
for name, ps in sorted(parts.items()):
    ps = sorted(ps)
    bad = [f.name for _, f in ps if not publishable(f)]
    if bad:
        print('SKIP stitch', name, '- tiles failed or pending:', ', '.join(bad))
        continue
    ims = [Image.open(f).convert('RGB') for _, f in ps]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    # The stitch's own sidecar: it is the composite of publishable tiles,
    # recorded so a later run verifies it like any capture.
    (RAW / f'{name}.png.capture.json').write_text(json.dumps({
        'schemaVersion': 1,
        'screenshot': f'{name}.png',
        'stitchedFrom': [f.name for _, f in ps],
        'dimensionCheck': {'status': 'pass', 'basis': 'stitched from publishable tiles'},
    }, indent=2) + '\n')
    print('stitched', name, sheet.size)

n = 0
skipped = []
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    if not publishable(f):
        skipped.append(f.name + f' (capture {verdict(f)})')
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    n += 1
for s in skipped:
    print('SKIP', s)
print(n, 'screenshots ->', OUT)
