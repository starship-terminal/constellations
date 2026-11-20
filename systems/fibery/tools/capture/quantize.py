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
    modes = {(sc.get('capture') or {}).get('mode') for sc in (sidecar_for(f) for _, f in ps)}
    # A scrollViewport tile set is capped the same 8 x 14000px as clip tiles;
    # the tile height itself is the viewport, not the chunk.
    intended = min(doc_h, 8 * 14000) if modes == {'scrollViewport'} and doc_h else (min(doc_h, 8 * clips[0]['height']) if doc_h else None)
    if intended is not None and abs(covered - intended) > 2:
        die(f'{name}: the tiles cover {covered}px of the intended {intended}px capture height '
            f'(document {doc_h}px) — a tile is missing')
    return intended


def tile_scale(parts):
    """PNG pixels per CSS pixel for these tiles, from the first sidecar that says.

    capture.scale is 'css' (the PNG is CSS-sized) or 'device' (the PNG is the
    clip times devicePixelRatio, e.g. the 2x mobile captures). Clips and
    document heights are always recorded in CSS px; the PNG is not.
    """
    for p in parts:
        if not p:
            continue
        if (p.get('capture') or {}).get('scale') == 'css':
            return 1
        dpr = ((p.get('actual') or {}).get('devicePixelRatio')
               or (p.get('requested') or {}).get('deviceScaleFactor'))
        if dpr:
            return dpr
    return 1


def stitched_sidecar(name, sheet, tile_paths, intended=None):
    """Rebuild name.png.capture.json from the part tiles' sidecars."""
    parts = [sidecar_for(f) for f in tile_paths]
    meta = dict(parts[0]) if parts and parts[0] else {'schemaVersion': 1}
    meta['screenshot'] = f'{name}.png'
    clips = [(p.get('capture') or {}).get('clip') for p in parts if p]
    clips = [c for c in clips if c]
    total_h = sum(c['height'] for c in clips)
    css_w = clips[0]['width'] if clips else sheet.width
    scale = tile_scale(parts)
    meta['capture'] = {'mode': 'stitchedParts',
                       'scale': (parts[0].get('capture') or {}).get('scale', 'device') if parts and parts[0] else 'device',
                       # The clip is recorded in CSS px like the part clips;
                       # png below carries the real device-pixel size.
                       'clip': {'x': 0, 'y': 0, 'width': css_w, 'height': total_h} if clips else None}
    meta['png'] = {'width': sheet.width, 'height': sheet.height}
    meta['stitchedFrom'] = [f.name for f in tile_paths]
    if clips:
        meta['partClip'] = clips
    if intended is not None:
        meta['intendedHeight'] = intended
        expected = {'width': round(css_w * scale), 'height': round(intended * scale)}
    elif clips:
        expected = {'width': round(css_w * scale), 'height': round(total_h * scale)}
    else:
        expected = {'width': sheet.width, 'height': sheet.height}
    matches = abs(sheet.width - expected['width']) <= 1 and abs(sheet.height - expected['height']) <= 2
    meta['dimensionCheck'] = {'status': 'pass' if matches else 'fail', 'expected': expected, 'basis': 'stitchedParts'}
    if not matches:
        meta['dimensionCheck']['error'] = (f"Stitched PNG {sheet.width}x{sheet.height}, "
                                           f"expected {expected['width']}x{expected['height']} "
                                           f"from the part clips at {scale}x")
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
    stitched[name] = stitched_sidecar(name, sheet, [f for _, f in ps], intended)
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
