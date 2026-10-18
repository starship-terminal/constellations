#!/usr/bin/env python3
"""Draw the site's PNG icons from the gallery's brand mark (the four squares in
docs/assets/favicon.svg): the Apple touch icon, the web app manifest's 192 and 512
icons, and a maskable 512 with the mark inside the safe zone.

    python3 tools/make_icons.py      write docs/assets/icons/*.png

Needs Pillow. The PNGs are committed (Git LFS); rerun only when the mark changes.
"""
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets" / "icons"
INK, PAPER = (27, 27, 26), (247, 247, 245)  # the gallery's --text and --bg
# The mark on an 18-unit grid: x, y, size and corner radius of each square.
SQUARES = ((1, 1, 7, 2), (10, 1, 7, 3.5), (1, 10, 7, 3.5), (10, 10, 7, 2))


def icon(size: int, mark: float, background=INK, ink=PAPER) -> Image.Image:
    """A square icon with the mark `mark` of `size` wide, centred."""
    scale = 4  # draw large, then shrink, for smooth corners
    big = size * scale
    img = Image.new("RGB", (big, big), background)
    draw = ImageDraw.Draw(img)
    unit = mark * big / 18
    offset = (big - unit * 18) / 2
    for x, y, w, r in SQUARES:
        box = [offset + x * unit, offset + y * unit, offset + (x + w) * unit, offset + (y + w) * unit]
        draw.rounded_rectangle(box, radius=r * unit, fill=ink)
    return img.resize((size, size), Image.LANCZOS)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    icon(180, 0.62).save(OUT / "apple-touch-icon.png", optimize=True)
    icon(192, 0.62).save(OUT / "icon-192.png", optimize=True)
    icon(512, 0.62).save(OUT / "icon-512.png", optimize=True)
    icon(512, 0.5).save(OUT / "icon-maskable-512.png", optimize=True)  # inside the 80% safe zone
    print(f"wrote 4 icons to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
