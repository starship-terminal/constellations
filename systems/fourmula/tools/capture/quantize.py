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
whose tiles lack sidecars gets none. Before stitching, check_tiles vets the set: tiles must be
numbered part0..partN-1 with no gap, each tile's sidecar must exist with a passing dimensionCheck,
the clips must run contiguously from y=0 at one width, and the union must cover the intended capture
(the measured document height, capped at the shooter's 8-chunk bound). A failed set is left in
RAW_DIR unstitched — a shortened image is never published under the full name.
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


def check_tiles(name, ps):
    """Vet a tile set before stitching. Returns (tile_paths, reason); reason is None when the set is
    safe to stitch. A tile set that fails any check is never stitched: a shortened image published
    under the full name is worse than none.

    Required: the tiles are numbered part0..partN-1 with no gap (a tile that failed to write leaves a
    hole, and the survivors must not stitch short), every tile has a sidecar that vouches for it
    (dimensionCheck pass), every tile's clip runs contiguously from y=0 at one width, and the union
    covers the whole intended capture — min(the page's measured documentHeight, the shooter's 8-chunk
    bound, chunk = 14000 device px / the run's pixel scale)."""
    tile_paths = [f for _, f in ps]
    idx = [i for i, _ in ps]
    if idx != list(range(len(ps))):
        missing = sorted(set(range(idx[-1] + 1)) - set(idx))
        return None, f'{name}: gaps in the tile run (missing part{missing[0]}); a partial page is never stitched'
    parts = [sidecar_for(f) for f in tile_paths]
    if any(not p for p in parts):
        return None, f'{name}: a part tile lacks its .capture.json sidecar; unmeasured tiles are never stitched'
    for p, f in zip(parts, tile_paths):
        chk = (p.get('dimensionCheck') or {}).get('status')
        if chk != 'pass':
            return None, f'{name}: {f.name} sidecar dimensionCheck is {chk!r}; a failed tile is never stitched'
    clips = [(p.get('capture') or {}).get('clip') for p in parts]
    if any(not c for c in clips):
        return None, f'{name}: a part tile sidecar records no clip; unmeasured tiles are never stitched'
    y = 0
    w = clips[0]['width']
    for i, c in enumerate(clips):
        if c['width'] != w:
            return None, f'{name}: part{i} clip width {c["width"]} != part0 {w}; mismatched tiles are never stitched'
        if c['x'] != 0 or c['y'] != y:
            return None, f'{name}: part{i} clip starts at {c["x"]},{c["y"]}, expected 0,{y}; non-contiguous tiles are never stitched'
        y += c['height']
    # The intended height: the document the shooter measured, capped at its 8-chunk bound
    # (chunk = floor(14000 / devicePixelRatio) CSS px — public.mjs Shooter.full).
    doc = ((parts[0].get('actual') or {}).get('documentSize') or {}).get('height')
    dpr = (parts[0].get('actual') or {}).get('devicePixelRatio') \
        or (parts[0].get('requested') or {}).get('deviceScaleFactor') or 1
    if doc:
        want = min(doc, 8 * (14000 // int(dpr)))
        if y < want:
            return None, (f'{name}: tiles cover {y} of {want} intended px '
                          f'(document {doc}); a shortened page is never stitched')
    return tile_paths, None


def stitched_sidecar(name, sheet, tile_paths):
    """Rebuild name.png.capture.json from the part tiles' sidecars, or None when any tile cannot vouch.

    Tile clips are CSS pixels, so the stitched clip stays in CSS pixels and the expected PNG size is
    each clip times its pixel scale (a 2x capture is twice its clip). A tile with no sidecar or no clip
    leaves the image without one: unmeasured shots are never marked as checked."""
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
    tile_paths, reason = check_tiles(name, ps)
    if tile_paths is None:
        # A partial tile set must not become a shortened "full" image: leave
        # the tiles in RAW_DIR as evidence and publish nothing for the name.
        print('  ! skipped', reason)
        continue
    ims = [Image.open(f).convert('RGB') for f in tile_paths]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    stitched[name] = stitched_sidecar(name, sheet, tile_paths)
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
