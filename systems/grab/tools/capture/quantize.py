"""Mask, then store the iPhone Mirroring captures as 256-colour PNGs in screenshots/light/.

usage: python3 tools/capture/quantize.py RAW_DIR

RAW_DIR holds light/ (Grab has no dark UI), with <name>.png (sRGB, written by capture/native/shot.sh)
and <name>.raw.png (the Display P3 original, skipped here). Every box in tools/masks.json is painted
over first (an address, a postcode, the map round the owner's home, card digits), so no private span
reaches the repo. The window's rounded corners are transparent, so the copies keep their alpha (fast
octree quantisation, no dither). Flat UI colours survive exactly; read values from raw/readings.json,
never from these. The full-colour captures stay outside the repo. Needs Pillow.
"""
from PIL import Image, ImageDraw
from collections import Counter
import json, pathlib, sys

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
MASKS = json.loads((PKG / "tools" / "masks.json").read_text())["masks"]


def ring_colour(im, x, y, w, h):
    """The most common colour on the box's one-pixel border (as sample.py mask does)."""
    W, H = im.size
    x0, y0, x1, y1 = max(x, 0), max(y, 0), min(x + w, W), min(y + h, H)
    if x1 <= x0 or y1 <= y0:
        raise ValueError(f"mask box {[x, y, w, h]} lies outside the {W}x{H} capture")
    px = im.load()
    ring = [px[i, j] for j in (max(y0 - 1, 0), min(y1, H - 1)) for i in range(x0, x1)]
    ring += [px[i, j] for i in (max(x0 - 1, 0), min(x1, W - 1)) for j in range(y0, y1)]
    return Counter(ring).most_common(1)[0][0]


def mask(im, entries):
    for e in entries:
        if isinstance(e, list):
            e = {"box": e}
        x, y, w, h = e["box"]
        colour = ring_colour(im, x, y, w, h) if "fill" not in e else e["fill"]
        paint = Image.new("L", im.size, 0)
        d = ImageDraw.Draw(paint)
        d.rectangle([x, y, x + w - 1, y + h - 1], fill=255)
        for kx, ky, kw, kh, shape in e.get("keep", []):
            (d.ellipse if shape == "ellipse" else d.rectangle)([kx, ky, kx + kw - 1, ky + kh - 1], fill=0)
        if e.get("screen"):   # leave the black outside the screen's rounded corners alone
            black = im.convert("RGB").point(lambda v: 255 if v == 0 else 0).convert("L").point(lambda v: 255 if v == 255 else 0)
            paint.paste(0, (0, 0), black)
        im.paste(colour, (0, 0), paint)
    return im


def main(raw, pkg=PKG):
    """Check every masks.json key names a capture before anything is written, then mask and store."""
    shots = [f for f in sorted((raw / "light").glob("*.png")) if not f.name.endswith(".raw.png")]
    unknown = sorted(set(MASKS) - {f.stem for f in shots})
    if unknown:
        # A mistyped key would leave its real capture unmasked: refuse before writing a single PNG.
        raise SystemExit(f"masks.json names captures that do not exist, nothing written: {', '.join(unknown)}")
    out = pkg / "screenshots" / "light"
    out.mkdir(parents=True, exist_ok=True)
    for f in shots:
        im = mask(Image.open(f).convert("RGBA"), MASKS.get(f.stem, []))
        im.quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(out / f.name, optimize=True)
    print(len(shots), "screenshots ->", pkg / "screenshots")


if __name__ == "__main__":
    main(pathlib.Path(sys.argv[1]).expanduser())
