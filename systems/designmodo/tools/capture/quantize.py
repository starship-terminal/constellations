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
stitched PNG's real pixel size. A tile whose own check failed (or has no sidecar) fails the sheet, and
the expected size is the tiles' recorded one, never the sheet's own width.
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


def stitched_sidecar(name, sheet, tile_paths):
    """Rebuild name.png.capture.json from the part tiles' sidecars."""
    parts = [sidecar_for(f) for f in tile_paths]
    meta = dict(parts[0]) if parts and parts[0] else {'schemaVersion': 1}
    meta['screenshot'] = f'{name}.png'
    clips = [(p.get('capture') or {}).get('clip') for p in parts if p]
    clips = [c for c in clips if c]
    total_h = sum(c['height'] for c in clips)
    meta['capture'] = {'mode': 'stitchedParts',
                       'scale': (parts[0].get('capture') or {}).get('scale', 'device') if parts and parts[0] else 'device',
                       # Part clips are CSS px, so the stitched clip keeps the CSS width; png below is device px.
                       'clip': {'x': 0, 'y': 0, 'width': clips[0]['width'] if clips else sheet.width,
                                'height': total_h} if clips else None}
    meta['png'] = {'width': sheet.width, 'height': sheet.height}
    meta['stitchedFrom'] = [f.name for f in tile_paths]
    if clips:
        meta['partClip'] = clips
    # The expectation comes from the tiles' own recorded checks, never from the sheet being judged:
    # a tile with a missing sidecar or a failed check cannot be vouched for, and every tile must
    # have been expected at the same width as the stitched sheet.
    problems = []
    tile_checks = [(p or {}).get('dimensionCheck') or {} for p in parts]
    for f, chk in zip(tile_paths, tile_checks):
        if chk.get('status') != 'pass':
            problems.append(f"tile {f.name} dimensionCheck is {chk.get('status', 'missing')}")
    exp = [c.get('expected') or {} for c in tile_checks]
    widths = {e.get('width') for e in exp}
    exp_w = next(iter(widths)) if len(widths) == 1 and None not in widths else None
    exp_h = sum(e['height'] for e in exp) if all('height' in e for e in exp) else None
    if exp_w is None:
        problems.append('tiles disagree on, or do not record, an expected width')
    expected = {'width': exp_w, 'height': exp_h}
    if not problems:
        if abs(sheet.width - exp_w) > 1 or abs(sheet.height - exp_h) > 1:
            problems.append(f"Stitched PNG {sheet.width}x{sheet.height}, expected {exp_w}x{exp_h} from the tiles' recorded checks")
    meta['dimensionCheck'] = {'status': 'fail' if problems else 'pass', 'expected': expected, 'basis': 'stitchedParts'}
    if problems:
        meta['dimensionCheck']['error'] = '; '.join(problems)
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
    idx = [i for i, _ in ps]
    if idx != list(range(len(idx))):
        # A failed tile was logged at capture time; stitching whichever parts
        # remain would publish a shortened image as the full page. Refuse and
        # leave the parts in RAW_DIR for the re-run.
        print('SKIP', name, ': missing tile(s) in', idx, '- re-run the capture')
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
