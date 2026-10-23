"""Store the iPhone Mirroring captures as 256-colour PNGs in screenshots/<theme>/.

usage: python3 tools/capture/quantize.py RAW_DIR

RAW_DIR holds dark/ only (Spotify for iOS has no light theme), with <name>.png (sRGB, written by
capture/native/shot.sh) and <name>.raw.png (the Display P3 original, skipped here). SKIP leaves out
two captures that repeat another: 01-home-loading is 02-home once loaded (only the mini player's
icons differ), and 13-library-longpress-sheet shows the same share sheet as 14-share-sheet. The
window's rounded corners are transparent, so the copies keep their alpha (fast octree quantisation,
no dither). Flat UI colours survive exactly; glass and gradients band a little, so read values from
raw/readings.json, never from these.
The full-colour captures stay outside the repo. Needs Pillow.
"""
from PIL import Image
import pathlib, sys

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1]).expanduser()

SKIP = {"01-home-loading.png", "13-library-longpress-sheet.png"}

n = 0
for theme in ("dark",):
    out = PKG / "screenshots" / theme
    out.mkdir(parents=True, exist_ok=True)
    for f in sorted((RAW / theme).glob("*.png")):
        if f.name.endswith(".raw.png") or f.name in SKIP:
            continue
        im = Image.open(f).convert("RGBA")
        im.quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(out / f.name, optimize=True)
        n += 1
print(n, "screenshots ->", PKG / "screenshots")
