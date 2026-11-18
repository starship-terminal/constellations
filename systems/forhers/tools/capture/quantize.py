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
stitched PNG's real pixel size (a part's own check can never vouch for the sheet). A stitched image
whose tiles lack sidecars gets none.
"""
from PIL import Image
import json, pathlib, re, shutil, sys

REF = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1])
OUT = REF / 'screenshots'
OUT.mkdir(exist_ok=True)


def die(msg):
    raise SystemExit('quantize: ' + msg)


def sidecar_for(png):
    """The .capture.json that belongs to a PNG, wherever it lives."""
    f = png.parent / (png.name + '.capture.json')
    return json.loads(f.read_text()) if f.exists() else None


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


def tile_failures(tile_paths):
    """Refuse a tile set that is not contiguous from part 0, or whose recorded page height is short.

    A missing sidecar is not a failure here: the stitch still publishes the image
    and writes no sidecar. A recorded dimensionCheck of fail, or a page height
    the tiles do not cover, is a failure and nothing is published.
    """
    indexes = []
    for f in tile_paths:
        m = re.match(r'.+\.part(\d+)\.png$', f.name)
        indexes.append(int(m.group(1)) if m else -1)
    if indexes != list(range(len(indexes))):
        return ['tile indexes are not a contiguous set from part 0']
    metas = [sidecar_for(f) for f in tile_paths]
    reasons = []
    for f, meta in zip(tile_paths, metas):
        if meta is None:
            reasons.append(f'{f.name}: missing sidecar')
        elif (meta.get('dimensionCheck') or {}).get('status') == 'fail':
            reasons.append(f"{f.name}: dimensionCheck is 'fail'")
    if reasons:
        return reasons
    clips = [(m.get('capture') or {}).get('clip') if m else None for m in metas]
    if not clips or any(not c or not c.get('height') for c in clips) or clips[0].get('y') != 0:
        return []
    for prev, nxt in zip(clips, clips[1:]):
        if abs((prev['y'] + prev['height']) - nxt['y']) > 1:
            return ['tile clips do not meet']
    intended = None
    for m in metas:
        doc = ((m or {}).get('actual') or {}).get('documentSize') or {}
        if doc.get('height'):
            intended = doc['height']
            break
    if intended is None:
        return []
    covered = clips[-1]['y'] + clips[-1]['height']
    if abs(covered - intended) > 1:
        return [f'tiles cover {covered}px of a {intended}px page']
    return []


def stitched_sidecar(name, sheet, tile_paths):
    """Rebuild name.png.capture.json from the part tiles' sidecars, or None when any tile cannot vouch.

    Tile clips are CSS pixels, so the stitched clip stays in CSS pixels and the expected PNG size is
    each clip times its pixel scale (a 2x capture is twice its clip). A tile with no sidecar, no clip,
    or a failed dimensionCheck leaves the image without a passing sidecar: a failed part is never
    published as a fresh pass."""
    failed = tile_failures(tile_paths)
    if failed and all('missing sidecar' in reason for reason in failed):
        return None
    if failed:
        return {'screenshot': f'{name}.png', 'stitchedFrom': [f.name for f in tile_paths],
                'dimensionCheck': {'status': 'fail', 'basis': 'stitchedParts',
                                   'error': 'refused failed tiles: ' + '; '.join(failed)}}
    parts = [sidecar_for(f) for f in tile_paths]
    if not parts or any(not p for p in parts):
        return None
    clips = [(p.get('capture') or {}).get('clip') for p in parts]
    scales = [pixel_scale(p) for p in parts]
    if any(not c for c in clips):
        return None
    meta = dict(parts[0])
    meta['screenshot'] = f'{name}.png'
    meta['capture'] = {'mode': 'stitchedParts', 'scale': (parts[0].get('capture') or {}).get('scale', 'device'),
                       'clip': {'x': clips[0]['x'], 'y': clips[0]['y'], 'width': clips[0]['width'],
                                'height': sum(c['height'] for c in clips)}}
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
    tile_paths = [f for _, f in ps]
    failed = tile_failures(tile_paths)
    # A missing sidecar still publishes the stitch and writes no sidecar.
    # A failed dimensionCheck, a gap, or a short page publishes nothing.
    missing_only = bool(failed) and all('missing sidecar' in reason for reason in failed)
    if failed and not missing_only:
        print('  ! skipped', name, '; '.join(failed), flush=True)
        sys.stdout.flush()
        stale = RAW / f'{name}.png'
        if stale.exists():
            stale.unlink()
            stale.with_name(stale.name + '.capture.json').unlink(missing_ok=True)
        for pub in (OUT / f'{name}.png', OUT / f'{name}.png.capture.json'):
            pub.unlink(missing_ok=True)
        stitched[name] = False
        continue
    ims = [Image.open(f).convert('RGB') for f in tile_paths]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    side = stitched_sidecar(name, sheet, tile_paths)
    if side is None:
        stitched[name] = None
        print('stitched', name, sheet.size, 'without a sidecar')
        continue
    if (side.get('dimensionCheck') or {}).get('status') == 'fail' and 'refused failed tiles' in (side.get('dimensionCheck') or {}).get('error', ''):
        print('  ! skipped', name, side.get('dimensionCheck', {}).get('error', 'failed tiles'))
        (RAW / f'{name}.png').unlink(missing_ok=True)
        for pub in (OUT / f'{name}.png', OUT / f'{name}.png.capture.json'):
            pub.unlink(missing_ok=True)
        stitched[name] = False
        continue
    stitched[name] = side
    print('stitched', name, sheet.size)

n = 0
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    if stitched.get(f.stem) is False:
        continue  # failed or missing tiles: nothing valid to publish
    chk = (sidecar_for(f) or {}).get('dimensionCheck') or {}
    if f.stem not in stitched:
        # A failed rerun can leave an older PNG behind, and its sidecar says so: never publish it.
        if chk.get('status') == 'fail':
            die(f'{f.name}: dimension check failed'
                + (f" ({chk['error']})" if chk.get('error') else '') + ' — not publishing a failed capture')
    elif chk.get('status') == 'fail' and (stitched.get(f.stem) or {}).get('dimensionCheck', {}).get('status') != 'fail':
        # A rebuilt sidecar already records the sheet's own failure. Publish
        # that. An older sidecar that failed, with no rebuilt one, does not.
        die(f'{f.name}: a stitched part failed its dimension check — not publishing')
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
