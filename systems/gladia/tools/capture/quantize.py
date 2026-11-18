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
stitched PNG's real pixel size (a part's own check can never vouch for the sheet).

A capture only publishes when its sidecar's dimensionCheck passed. screenshotWithMetadata invalidates
the same-path sidecar before shooting, so a failed recapture leaves a failing (or half-written, or
missing) sidecar beside the raw PNG — the raw file stays, and the previously published screenshot and
sidecar in screenshots/ keep standing as the last good evidence instead of being overwritten.
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
    """Refuse an incomplete tile set before stitching publishes a shortened -full.png.

    public.mjs writes name.part0.png, name.part1.png, ... top to bottom, one
    .capture.json sidecar per tile with its own dimension check and the clip it
    shot. A tile whose screenshot threw still leaves its sidecar (status fail)
    or nothing at all, and public.mjs swallows the error, so the surviving set
    alone cannot prove completeness. Require: a contiguous part0..partN run,
    every tile's own check passed, the clips butt-join from y=0, and the
    covered height reaches the intended capture height (the document height the
    tile sidecars recorded, capped at the 8-chunk tile ceiling).
    """
    idx = [i for i, _ in ps]
    if idx != list(range(len(ps))):
        die(f'{name}: part tiles {idx} are not a contiguous run from part0 — a tile failed or never wrote')
    clips, y = [], 0
    doc_h = None
    for i, f in ps:
        sc = sidecar_for(f)
        if sc is None:
            # No sidecars at all: publish the stitch and write no sidecar.
            # A partial set, one tile measured and another not, still dies.
            if all(sidecar_for(tile) is None for _, tile in ps):
                return None
            die(f'{f.name}: no .capture.json sidecar — the tile never finished writing')
        chk = sc.get('dimensionCheck') or {}
        if chk.get('status') != 'pass':
            die(f'{f.name}: the tile\'s own dimension check is {chk.get("status")!r}'
                + (f" ({chk['error']})" if chk.get('error') else ''))
        clip = (sc.get('capture') or {}).get('clip')
        if not clip:
            die(f'{f.name}: sidecar records no capture.clip — not a tile capture')
        if clip.get('x') or abs(clip.get('y', -1) - y) > 1:
            die(f'{f.name}: clip starts at y={clip.get("y")}, expected {y} — the tiles do not butt-join')
        y += clip['height']
        clips.append(clip)
        if doc_h is None:
            doc_h = ((sc.get('actual') or {}).get('documentSize') or {}).get('height')
    if len({c['width'] for c in clips}) > 1:
        die(f'{name}: tile clip widths differ — {sorted(c["width"] for c in clips)}')
    covered = y
    intended = min(doc_h, 8 * clips[0]['height']) if doc_h else None
    if intended is not None and abs(covered - intended) > 2:
        die(f'{name}: the tiles cover {covered}px of the intended {intended}px capture height '
            f'(document {doc_h}px, at most 8 x {clips[0]["height"]}px tiles) — a tile is missing')
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

    Tile clips are CSS pixels, so the stitched clip stays in CSS pixels and the expected PNG size is
    each clip times its pixel scale (a 2x capture is twice its clip). The intended document height
    check_tiles measured is in CSS px too and scales the same way."""
    parts = [sidecar_for(f) for f in tile_paths]
    meta = dict(parts[0]) if parts and parts[0] else {'schemaVersion': 1}
    meta['screenshot'] = f'{name}.png'
    clips = [(p.get('capture') or {}).get('clip') for p in parts if p]
    clips = [c for c in clips if c]
    scales = [pixel_scale(p) for p in parts if p]
    meta['capture'] = {'mode': 'stitchedParts',
                       'scale': (parts[0].get('capture') or {}).get('scale', 'device') if parts and parts[0] else 'device',
                       'clip': {'x': clips[0]['x'], 'y': clips[0]['y'], 'width': clips[0]['width'],
                                'height': sum(c['height'] for c in clips)} if clips else None}
    meta['png'] = {'width': sheet.width, 'height': sheet.height}
    meta['stitchedFrom'] = [f.name for f in tile_paths]
    if clips:
        meta['partClip'] = clips
    if intended is not None:
        meta['intendedHeight'] = intended
        expected = {'width': round(clips[0]['width'] * scales[0]), 'height': round(intended * scales[0])}
    elif clips:
        expected = {'width': round(clips[0]['width'] * scales[0]),
                    'height': sum(round(c['height'] * s) for c, s in zip(clips, scales))}
    else:
        expected = {'width': sheet.width, 'height': sheet.height}
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
    sheet.save(RAW / f'{name}.png')
    # No sidecars at all: publish the PNG and write no sidecar. A rebuilt
    # sidecar with no clips would compare the sheet to itself and pass.
    if all(sidecar_for(f) is None for _, f in ps):
        stitched[name] = None
    else:
        stitched[name] = stitched_sidecar(name, sheet, [f for _, f in ps], intended)
    print('stitched', name, sheet.size)

n = 0
skipped = []
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    # Publish only a capture whose own check passed. screenshotWithMetadata
    # invalidates the same-path sidecar before shooting, so a failed recapture
    # leaves a failing sidecar beside the raw PNG — the tile loop refuses
    # those, and a plain capture must not publish one either: the previously
    # published screenshot and sidecar stay as the last good evidence.
    if f.stem in stitched:
        meta = stitched[f.stem]
    else:
        meta = sidecar_for(f)
    status = ((meta or {}).get('dimensionCheck') or {}).get('status')
    # A stitched image publishes even when its rebuilt check fails: the
    # failing sidecar is the evidence. An unmeasured stitch publishes with
    # no sidecar. A plain capture with no sidecar publishes and drops any
    # sidecar a previous run left behind.
    publish_fail = f.stem in stitched and status == 'fail'
    unmeasured = f.stem in stitched and meta is None
    plain_unmeasured = f.stem not in stitched and meta is None
    if status != 'pass' and not publish_fail and not unmeasured and not plain_unmeasured:
        skipped.append(f'{f.name} (sidecar {status or "missing"})')
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / f.name, optimize=True)
    out_side = OUT / f'{f.name}.capture.json'
    out_side.unlink(missing_ok=True)   # never leave a previous run's measurements beside a new image
    if publish_fail or (f.stem in stitched and meta):
        out_side.write_text(json.dumps(meta, indent=1) + '\n')
    elif not unmeasured and not plain_unmeasured and f.with_name(f.name + '.capture.json').exists():
        shutil.copyfile(f.with_name(f.name + '.capture.json'), out_side)
    n += 1
print(n, 'screenshots ->', OUT)
for s in skipped:
    print('  skipped (kept the earlier published shot):', s)
