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
whose tiles lack sidecars gets none. public.mjs writes <name>.plan.json before the tiles; a stitch
is published only when the saved tiles are that plan's count, in order from part 0, and the sheet
is the planned height. A partial set stays in RAW and is not published.
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


def load_plan(name):
    """The tile plan public.mjs wrote before shooting, or None when this run has no plan."""
    f = RAW / f'{name}.plan.json'
    if not f.exists():
        return None
    plan = json.loads(f.read_text())
    if not isinstance(plan, dict) or not isinstance(plan.get('parts'), int):
        raise SystemExit(f'{name}.plan.json has no integer parts count')
    return plan


def planned_sheet(plan, width, scales):
    """The PNG size the plan promised: planned CSS height times the tiles' pixel scale."""
    height = plan.get('intendedHeight')
    if not isinstance(height, (int, float)) or height <= 0:
        return None
    scale = scales[0] if scales else 1
    if any(abs(s - scale) > 0.01 for s in scales):
        return None
    return {'width': round(width * scale), 'height': round(height * scale)}


def stitched_sidecar(name, sheet, tile_paths, plan=None):
    """Rebuild name.png.capture.json from the part tiles' sidecars, or None when any tile cannot vouch.

    Tile clips are CSS pixels, so the stitched clip stays in CSS pixels and the expected PNG size is
    each clip times its pixel scale (a 2x capture is twice its clip). A tile with no sidecar or no clip
    leaves the image without one: unmeasured shots are never marked as checked. When a plan exists,
    the expected height is the planned page height, not the sum of whichever tiles happened to land."""
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
    basis = 'stitchedParts'
    planned = planned_sheet(plan, clips[0]['width'], scales) if plan else None
    if planned:
        expected = planned
        basis = 'plan'
        meta['plan'] = {'parts': plan['parts'], 'intendedHeight': plan.get('intendedHeight'),
                        'pageHeight': plan.get('pageHeight'), 'chunk': plan.get('chunk')}
    matches = abs(sheet.width - expected['width']) <= 1 and abs(sheet.height - expected['height']) <= 1
    meta['dimensionCheck'] = {'status': 'pass' if matches else 'fail', 'expected': expected, 'basis': basis}
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
    plan = load_plan(name)
    indices = [i for i, _ in ps]
    # A capture that died mid-loop leaves parts 0..k of n. Stitching those and
    # checking the sheet against the same tiles would publish a truncated page
    # as pass. The plan is the count, the order and the height.
    if plan is not None:
        expected_n = plan['parts']
        if expected_n < 1 or indices != list(range(expected_n)):
            print('refusing', name, '— tile set', indices, 'is not the planned',
                  expected_n, 'parts in order from 0')
            continue
        if not isinstance(plan.get('intendedHeight'), (int, float)) or plan['intendedHeight'] <= 0:
            print('refusing', name, '— plan has no intendedHeight')
            continue
    elif indices != list(range(len(ps))):
        print('refusing', name, '— non-contiguous part set', indices)
        continue
    ims = [Image.open(f).convert('RGB') for _, f in ps]
    if any(i.width != ims[0].width for i in ims):
        print('refusing', name, '— tiles differ in width')
        continue
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    if plan is not None:
        scales = [pixel_scale(sidecar_for(f) or {}) for _, f in ps]
        planned = planned_sheet(plan, (sidecar_for(ps[0][1]) or {}).get('capture', {}).get('clip', {}).get('width') or ims[0].width, scales)
        # css-scale tiles are 1 CSS px per PNG px, so the sheet height is the planned height.
        if planned and abs(sheet.height - planned['height']) > 1:
            print('refusing', name, '— stitched height', sheet.height, 'is not the planned', planned['height'])
            continue
    sheet.save(RAW / f'{name}.png')
    stitched[name] = stitched_sidecar(name, sheet, [f for _, f in ps], plan)
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
