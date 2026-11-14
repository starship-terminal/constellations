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


def stitched_sidecar(name, sheet, tiles):
    """Rebuild name.png.capture.json from the part tiles' sidecars.

    tiles is the sorted [(index, Path)] list for the sheet. A passing
    dimensionCheck requires the full expected tile range and coverage, not
    just the tiles that happened to arrive: the indices must run 0..N-1 with
    no gap, the recorded part clips must tile [0, height) contiguously, and
    their union must reach the capture's own target height — the document
    height each part sidecar recorded, capped at the shooter's 8 chunks. A
    tile lost mid-run or a dead final tile fails the check instead of
    publishing a shortened sheet as a complete -full capture.

    Tile clips are CSS pixels, so the stitched clip stays in CSS pixels and the expected PNG size is
    each clip times its pixel scale (a 2x capture is twice its clip). A tile with no sidecar or no clip
    leaves the image without one: unmeasured shots are never marked as checked.
    """
    parts = [sidecar_for(f) for _, f in tiles]
    if not parts or any(not p for p in parts):
        return None
    clips = [(p.get('capture') or {}).get('clip') for p in parts]
    if any(not c for c in clips):
        return None
    scales = [pixel_scale(p) for p in parts]
    meta = dict(parts[0])
    meta['screenshot'] = f'{name}.png'
    total_h = sum(c['height'] for c in clips)
    meta['capture'] = {'mode': 'stitchedParts', 'scale': (parts[0].get('capture') or {}).get('scale', 'device'),
                       'clip': {'x': 0, 'y': 0, 'width': clips[0]['width'], 'height': total_h}}
    meta['png'] = {'width': sheet.width, 'height': sheet.height}
    meta['stitchedFrom'] = [f.name for _, f in tiles]
    meta['partClip'] = clips

    failures = []
    indices = sorted(i for i, _ in tiles)
    if indices != list(range(len(tiles))):
        missing = sorted(set(range(indices[-1] + 1)) - set(indices))
        failures.append(f"tile range {indices[0]}..{indices[-1]} is missing part{missing}")
    y = 0
    for c in sorted(clips, key=lambda c: c['y']):
        if abs(c['y'] - y) > 1:
            failures.append(f"part clips are not contiguous (gap before clip y={c['y']})")
            break
        y += c['height']
    doc_hs = [(p.get('actual') or {}).get('documentSize', {}).get('height') for p in parts if p]
    doc_hs = [h for h in doc_hs if h]
    if doc_hs:
        # The shooter bounds every full-page pass at 8 chunks, so the
        # intended coverage is min(document height, 8 * chunk); the chunk
        # is the largest clip height recorded (full tiles only).
        chunk = max(c['height'] for c in clips)
        expected_cover = min(max(doc_hs), 8 * chunk)
        if total_h < expected_cover - 1:
            failures.append(f"clips cover {total_h}px of the {expected_cover}px the capture targeted"
                            f" (document {max(doc_hs)}px, 8-chunk cap {8 * chunk}px)")
    expected = {'width': round(clips[0]['width'] * scales[0]),
                'height': sum(round(c['height'] * s) for c, s in zip(clips, scales))}
    if abs(sheet.width - expected['width']) > 1 or abs(sheet.height - expected['height']) > 1:
        failures.append(f"Stitched PNG {sheet.width}x{sheet.height}, "
                        f"expected {expected['width']}x{expected['height']} from the part clips")
    meta['dimensionCheck'] = {'status': 'pass' if not failures else 'fail', 'expected': expected, 'basis': 'stitchedParts'}
    if failures:
        meta['dimensionCheck']['error'] = '; '.join(failures)
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
    ims = [Image.open(f).convert('RGB') for _, f in ps]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    stitched[name] = stitched_sidecar(name, sheet, ps)
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
