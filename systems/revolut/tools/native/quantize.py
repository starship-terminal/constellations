"""Store the iPhone Mirroring captures as 256-colour PNGs in screenshots/<theme>/.

usage: python3 tools/capture/quantize.py RAW_DIR

RAW_DIR holds dark/ and light/, each with <name>.png (sRGB, written by capture/native/shot.sh) and
<name>.raw.png (the Display P3 original, skipped here). The window's rounded corners are transparent,
so the copies keep their alpha (fast octree quantisation, no dither). Flat UI colours survive
exactly; glass and gradients band a little, so read values from raw/readings.json, never from these.
The full-colour captures stay outside the repo. Needs Pillow.
"""
from PIL import Image
import pathlib, sys

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1]).expanduser()

n = 0
for theme in ("dark", "light"):
    out = PKG / "screenshots" / theme
    out.mkdir(parents=True, exist_ok=True)
    for f in sorted((RAW / theme).glob("*.png")):
        if f.name.endswith(".raw.png"):
            continue
        im = Image.open(f).convert("RGBA")
        im.quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(out / f.name, optimize=True)
        n += 1
print(n, "screenshots ->", PKG / "screenshots")
