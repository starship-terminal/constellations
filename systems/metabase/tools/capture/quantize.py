"""Convert accepted browser PNG/JPEG captures to 256-colour PNGs.

usage: python3 systems/metabase/tools/capture/quantize.py RAW_DIR

Keep originals outside git. The in-app browser emits JPEG; conversion cannot
restore lost detail. Measure values from the committed CSS readings, never
from quantized images. Inspect each result and record native dimensions.
PNG part files from the capture kit can also be stitched before conversion.
"""
from PIL import Image
import pathlib, re, sys

REF = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1])
OUT = REF / 'screenshots'
OUT.mkdir(exist_ok=True)

parts = {}
for f in RAW.glob('*.part*.png'):
    m = re.match(r'(.+)\.part(\d+)\.png$', f.name)
    parts.setdefault(m.group(1), []).append((int(m.group(2)), f))
for name, ps in parts.items():
    ims = [Image.open(f).convert('RGB') for _, f in sorted(ps)]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims)))
    y = 0
    for i in ims:
        sheet.paste(i, (0, y)); y += i.height
    sheet.save(RAW / f'{name}.png')
    print('stitched', name, sheet.size)

n = 0
for f in sorted(p for p in RAW.iterdir() if p.suffix.lower() in {'.png', '.jpg', '.jpeg'}):
    if '.part' in f.name:
        continue
    im = Image.open(f).convert('RGB')
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / (f.stem + '.png'), optimize=True)
    n += 1
print(n, 'screenshots ->', OUT)
