"""Store Playwright captures as 256-colour PNGs in screenshots/.

usage: python3 tools/capture/quantize.py RAW_DIR

Playwright screenshots are already sRGB, so there is no profile conversion, only quantization. A page
taller than one GPU texture is captured by public.mjs as name.part0.png, name.part1.png, ...; those are
stitched top to bottom into name.png first (the stitched full-colour copy stays in RAW_DIR). The
full-colour originals are kept in RAW_DIR only; screenshots/ gets the 256-colour versions that are
committed. Flat UI colours are exact, gradients and photographs band a little, so read exact colours
from raw/css-vars.json and raw/components-computed.json. Adapted from the Coursera kit.

Every image's .capture.json sidecar travels with it: a plain capture's sidecar is copied next to the
quantized PNG, and a stitched image's sidecar is rebuilt from its part tiles' sidecars — the parts'
clips recorded under partClip, the union under capture.clip, and a fresh dimensionCheck against the
stitched PNG's real pixel size (a part's own check can never vouch for the sheet). A stitch whose
tiles are missing, failed their own checks, or do not span the intended capture height is refused:
nothing is written for that name, and the run exits non-zero.
"""
from PIL import Image
import json, pathlib, re, shutil, sys

REF = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1])
OUT = REF / 'screenshots'
OUT.mkdir(exist_ok=True)


def sidecar_for(png):
    """The .capture.json that belongs to a PNG, wherever it lives."""
    f = png.parent / (png.name + '.capture.json')
    return json.loads(f.read_text()) if f.exists() else None


def die(msg):
    raise SystemExit('quantize: ' + msg)


def check_tiles(name, ps):
    """Refuse an incomplete tile set before stitching publishes a shortened sheet.

    public.mjs writes name.part0.png, name.part1.png, ... top to bottom. A later
    tile that fails after retry must not leave the earlier tiles to invent a
    shorter expected height. Require a contiguous part0..partN run, a passing
    dimension check and a clip on every tile, and (when the tile records it)
    a span that reaches the intended capture height.
    """
    idx = [i for i, _ in ps]
    if idx != list(range(len(ps))):
        die(f'{name}: part tiles {idx} are not a contiguous run from part0 — a tile failed or never wrote')
    clips, y = [], 0
    intended = None
    recorded_count = None
    for i, f in ps:
        sc = sidecar_for(f)
        if sc is None:
            die(f'{f.name}: no .capture.json sidecar — the tile never finished writing')
        chk = sc.get('dimensionCheck') or {}
        if chk.get('status') != 'pass':
            die(f'{f.name}: the tile\'s own dimension check is {chk.get("status")!r}'
                + (f" ({chk['error']})" if chk.get('error') else ''))
        clip = (sc.get('capture') or {}).get('clip')
        if not clip or not clip.get('width') or not clip.get('height'):
            die(f'{f.name}: sidecar records no capture.clip — not a tile capture')
        cap = sc.get('capture') or {}
        if cap.get('capturedHeight') and intended is None:
            intended = cap['capturedHeight']
        if cap.get('partCount') and recorded_count is None:
            recorded_count = cap['partCount']
        if recorded_count is not None and cap.get('partCount') not in (None, recorded_count):
            die(f'{name}: tiles disagree on partCount')
        y += clip['height']
        clips.append(clip)
    if recorded_count is not None and recorded_count != len(ps):
        die(f'{name}: {len(ps)} tiles on disk, capture recorded partCount {recorded_count}')
    if intended is not None and abs(y - intended) > 1:
        die(f'{name}: the tiles cover {y}px of the intended {intended}px capture height — a tile is missing')
    return intended


def pixel_scale(meta):
    """Device pixels per CSS pixel the tile was captured at: the recorded ratio, else the tile's own
    PNG width over its clip width, else 1 (a sidecar that records neither is read as a 1x capture)."""
    cap = meta.get('capture') or {}
    if cap.get('scale') == 'css':
        return 1
    dpr = (meta.get('actual') or {}).get('devicePixelRatio') or (meta.get('requested') or {}).get('deviceScaleFactor')
    if dpr:
        return dpr
    clip, png = cap.get('clip'), meta.get('png')
    return png['width'] / clip['width'] if clip and png and clip.get('width') and png.get('width') else 1


def stitched_sidecar(name, sheet, tile_paths, intended=None):
    """Rebuild name.png.capture.json from the part tiles' sidecars.

    Tile clips are CSS pixels, so the stitched clip stays in CSS pixels and the
    expected PNG size is each clip times its pixel scale (a 2x capture is twice
    its clip). check_tiles has already refused a missing, failed or short set.
    A sheet whose pixels do not match those clips records a failing
    dimensionCheck and is still written, so a reviewer can see the mismatch.
    Missing tiles, failed tile checks and a short span never get here."""
    parts = [sidecar_for(f) for f in tile_paths]
    clips = [(p.get('capture') or {}).get('clip') for p in parts]
    scales = [pixel_scale(p) for p in parts]
    span = sum(c['height'] for c in clips)
    meta = dict(parts[0])
    meta['screenshot'] = f'{name}.png'
    meta['capture'] = {'mode': 'stitchedParts', 'scale': (parts[0].get('capture') or {}).get('scale', 'device'),
                       'clip': {'x': clips[0]['x'], 'y': clips[0]['y'], 'width': clips[0]['width'],
                                'height': span}}
    if intended is not None:
        meta['capture']['intendedHeight'] = intended
        meta['intendedHeight'] = intended
    meta['png'] = {'width': sheet.width, 'height': sheet.height}
    meta['stitchedFrom'] = [f.name for f in tile_paths]
    meta['partClip'] = clips
    expected = {'width': round(clips[0]['width'] * scales[0]),
                'height': sum(round(c['height'] * s) for c, s in zip(clips, scales))}
    matches = abs(sheet.width - expected['width']) <= 1 and abs(sheet.height - expected['height']) <= 1
    meta['dimensionCheck'] = {'status': 'pass' if matches else 'fail', 'expected': expected, 'basis': 'stitchedParts'}
    if not matches:
        meta['dimensionCheck']['error'] = (f"Stitched PNG {sheet.width}x{sheet.height}, "
                                           f"expected {expected['width']}x{expected['height']} from the part clips")
    return meta


parts = {}
for f in RAW.glob('*.part*.png'):
    m = re.match(r'(.+)\.part(\d+)\.png$', f.name)
    if not m:   # a name such as x.partial.png is not a tile
        continue
    parts.setdefault(m.group(1), []).append((int(m.group(2)), f))
stitched = {}
for name, ps in parts.items():
    ps = sorted(ps)
    intended = check_tiles(name, ps)
    ims = [Image.open(f).convert('RGB') for _, f in ps]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    # Build the sidecar before writing the sheet. A refused stitch must not
    # leave a shortened full-colour PNG for the publisher to quantize.
    side = stitched_sidecar(name, sheet, [f for _, f in ps], intended)
    sheet.save(RAW / f'{name}.png')
    stitched[name] = side
    print('stitched', name, sheet.size)

n = 0
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    out_side = OUT / f'{f.name}.capture.json'
    out_side.unlink(missing_ok=True)   # never leave a previous run's measurements beside a new image
    if stitched.get(f.stem):
        out_side.write_text(json.dumps(stitched[f.stem], indent=1) + '\n')
    elif f.stem not in stitched and f.with_name(f.name + '.capture.json').exists():
        shutil.copyfile(f.with_name(f.name + '.capture.json'), out_side)
    n += 1
print(n, 'screenshots ->', OUT)
