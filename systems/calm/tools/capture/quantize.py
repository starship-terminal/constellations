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
    # A stitched sheet is only 'pass' if the tiles provably cover the page:
    # contiguous indices, contiguous ranges, and the last tile reaching the
    # reported content height. Inner-scroller captures record where each tile
    # sat inside the scroller (capture.scroller, written by public.mjs):
    # clip.y is viewport-relative for those, so the tile's document position
    # is scroller.top + clip.y, and coverage is against the scroller's own
    # height, not the outer document's (which stays at the viewport height).
    # A capture that stopped early, or a lost tile, is a documented gap —
    # never a shortened 'complete' page.
    problems = []
    scrollers = [(p.get('capture') or {}).get('scroller') for p in parts]
    positions = [(sc['top'] + c['y']) if sc else c['y'] for c, sc in zip(clips, scrollers)]
    y = positions[0]
    if y != 0:
        problems.append(f"first tile starts at position {y}, not 0")
    for i, (c, pos) in enumerate(zip(clips, positions)):
        if abs(pos - y) > 2:
            problems.append(f"tile {i} at {pos}, expected {y}")
        y = pos + c['height']
    doc_h = next((sc['height'] for sc in scrollers if sc and sc.get('height')), None)
    basis_h = 'scroller'
    if doc_h is None:
        basis_h = 'document'
        doc_h = next(((((p.get('actual') or {}).get('documentSize') or {}).get('height'))
                      for p in parts if (p.get('actual') or {}).get('documentSize')), None)
    if doc_h and abs(y - doc_h) > 8:
        problems.append(f"tiles cover {y}px of the reported {doc_h}px {basis_h} content")
    meta = dict(parts[0])
    meta['screenshot'] = f'{name}.png'
    meta['capture'] = {'mode': 'stitchedParts', 'scale': (parts[0].get('capture') or {}).get('scale', 'device'),
                       'clip': {'x': clips[0]['x'], 'y': clips[0]['y'], 'width': clips[0]['width'],
                                'height': sum(c['height'] for c in clips)}}
    meta['png'] = {'width': sheet.width, 'height': sheet.height}
    meta['stitchedFrom'] = [f.name for f in tile_paths]
    meta['partClip'] = [dict(c, documentY=pos) for c, pos in zip(clips, positions)]
    expected = {'width': round(clips[0]['width'] * scales[0]),
                'height': sum(round(c['height'] * s) for c, s in zip(clips, scales))}
    matches = abs(sheet.width - expected['width']) <= 1 and abs(sheet.height - expected['height']) <= 1
    meta['dimensionCheck'] = {'status': 'pass' if matches and not problems else 'fail', 'expected': expected, 'basis': 'stitchedParts'}
    if problems:
        meta['dimensionCheck']['error'] = '; '.join(problems)
    if not matches:
        meta['dimensionCheck']['error'] = '; '.join(filter(None, [meta['dimensionCheck'].get('error'),
            f"Stitched PNG {sheet.width}x{sheet.height}, "
            f"expected {expected['width']}x{expected['height']} from the part clips"]))
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
    # Tiles must be a contiguous run from part0; a missing tile mid-capture is
    # a hole, not a shorter page.
    missing = [i for i in range(ps[-1][0] + 1) if i not in {i for i, _ in ps}]
    if missing:
        print(f'skipped {name}: missing tiles {missing} — a stitched sheet would hide the gap')
        # A previous run's stitched PNG must not survive a failed recapture:
        # the export loop below would quietly ship the old image with its old
        # sidecar. Remove both so the gap shows up as a gap.
        stale = RAW / f'{name}.png'
        if stale.exists():
            stale.unlink()
            stale_sc = stale.with_name(stale.name + '.capture.json')
            stale_sc.unlink(missing_ok=True)
        # and the previously published pair in screenshots/: an old complete
        # export beside a failed recapture reads as current evidence
        for pub in (OUT / f'{name}.png', OUT / f'{name}.png.capture.json'):
            pub.unlink(missing_ok=True)
        stitched[name] = False   # failed recapture: nothing valid to export
        continue
    ims = [Image.open(f).convert('RGB') for _, f in ps]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    stitched[name] = stitched_sidecar(name, sheet, [f for _, f in ps])
    print('stitched', name, sheet.size)

n = 0
for f in sorted(RAW.glob('*.png')):
    if '.part' in f.name:
        continue
    if stitched.get(f.stem) is False:
        continue  # failed recapture: no stitched sheet, nothing to export

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
