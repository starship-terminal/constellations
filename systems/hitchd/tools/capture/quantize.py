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


def stitched_sidecar(name, sheet, tile_paths, manifest=None):
    """Rebuild name.png.capture.json from the part tiles' sidecars, or None when any tile cannot vouch.

    Tile clips are CSS pixels, so the stitched clip stays in CSS pixels and the expected PNG size is
    each clip times its pixel scale (a 2x capture is twice its clip). A tile with no sidecar or no clip
    leaves the image without one: unmeasured shots are never marked as checked. Tile continuity and the
    shooter's .full.json manifest are verified too: a tile that timed out mid-run leaves a shortened part
    set, and a shortened sheet is a partial capture — its sidecar fails its dimensionCheck, it never
    silently passes as the whole page."""
    parts = [sidecar_for(f) for f in tile_paths]
    if not parts or any(not p for p in parts):
        return None
    clips = [(p.get('capture') or {}).get('clip') for p in parts]
    scales = [pixel_scale(p) for p in parts]
    if any(not c for c in clips):
        return None
    meta = dict(parts[0])
    problems = []
    # tiles must be contiguous vertical slices of the same column: index order
    # already checked by the caller; the clip geometry must agree
    y = clips[0]['y']
    for i, c in enumerate(clips):
        if c['x'] != clips[0]['x'] or c['width'] != clips[0]['width']:
            problems.append(f"part{i} clips a different column than part0")
        if c['y'] != y:
            problems.append(f"part{i} clips y={c['y']}, expected {y} — a tile is missing or duplicated")
        y += c['height']
    if manifest:
        owed = manifest.get('expectedTiles')
        have = manifest.get('tilesWritten')
        if owed is not None and len(parts) != owed:
            problems.append(f"page owed {owed} tiles, only {len(parts)} stitched — the sheet is partial")
        if have is not None and len(parts) != have:
            problems.append(f"shooter wrote {have} tiles, {len(parts)} stitched — the set is inconsistent")
    if problems:
        meta['partial'] = problems
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
    meta['dimensionCheck'] = {'status': 'pass' if matches and not problems else 'fail', 'expected': expected, 'basis': 'stitchedParts'}
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
    # tile indices must run 0..n-1: a timeout that leaves a hole in the
    # sequence means the sheet skips part of the page — record it, still
    # stitch what survived (the sidecar's check will fail it as partial)
    idx = [i for i, _ in ps]
    mf = RAW / f'{name}.full.json'
    manifest = json.loads(mf.read_text()) if mf.exists() else None
    if idx != list(range(len(ps))):
        manifest = dict(manifest or {})
        manifest.setdefault('indexGap', idx)
    ims = [Image.open(f).convert('RGB') for _, f in ps]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    stitched[name] = stitched_sidecar(name, sheet, [f for _, f in ps], manifest)
    if manifest and manifest.get('indexGap'):
        stitched[name] = dict(stitched[name] or {})
        stitched[name].setdefault('partial', []).append(f"tile indices {idx} are not contiguous")
        stitched[name].setdefault('dimensionCheck', {})['status'] = 'fail'
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
