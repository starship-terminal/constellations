#!/usr/bin/env python3
"""Derive the Glass icon set from its master render, docs/assets/logo/hero-ai.png.

The site ships two app icons, chosen under Settings > Preferences:

  Flat   the default: the vector prism mark. docs/assets/favicon.svg and every
         PNG and .ico in docs/assets/icons/ are the designer's own renders of
         it, committed as delivered; this script never writes them.
  Glass  an AI-rendered glass prism, raster only. This script writes its set
         into docs/assets/icons/glass/ with the Flat set's names, sizes and
         shapes, so the two swap file for file.

    python3 tools/make_icons.py      write docs/assets/icons/glass/*

Needs Pillow. The output is committed (Git LFS); rerun only when hero-ai.png or
the crop changes. A rerun over an unchanged master rewrites identical bytes.
"""
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "docs" / "assets" / "logo" / "hero-ai.png"
OUT = ROOT / "docs" / "assets" / "icons" / "glass"
TILE = (8, 9, 10)  # #08090a, the Flat mark's tile and the dark theme's page
# The square of the 1024 render that makes one tile: the prism (x 251-755,
# y 279-747) at the Flat triangle's 62.5% of the tile width, beam and bands
# running off the edges as they do in the Flat mark.
CROP = (99, 109, 907, 917)
CORNER = 14 / 64  # the Flat tile's corner radius (rx 14 on its 64 viewBox)
SAFE = 0.8        # maskable safe zone: the tile scaled to 80%, as Flat's is


def tile(size: int) -> Image.Image:
    """The cropped render at `size`, its black lifted to the #08090a tile.

    Screen-blending the tile colour maps the render's pure black to #08090a and
    leaves the bright glass and bands all but untouched, so Glass sits on the
    same ground as Flat and the maskable padding shows no seam.
    """
    art = Image.open(MASTER).convert("RGB").resize((size, size), Image.LANCZOS, box=CROP)
    return ImageChops.screen(art, Image.new("RGB", art.size, TILE))


def rounded(img: Image.Image) -> Image.Image:
    """`img` with the Flat tile's rounded corners, transparent outside them."""
    scale = 4  # draw the mask large, then shrink, for smooth corners
    big = img.width * scale
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, big - 1, big - 1], radius=CORNER * big, fill=255)
    out = img.convert("RGBA")
    out.putalpha(mask.resize(img.size, Image.LANCZOS))
    return out


def maskable(size: int) -> Image.Image:
    """The square tile at the safe zone's size, centred on a #08090a field."""
    inner = round(size * SAFE)
    out = Image.new("RGB", (size, size), TILE)
    out.paste(tile(inner), ((size - inner) // 2,) * 2)
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    favicons = {s: rounded(tile(s)) for s in (16, 32, 48)}
    for s, img in favicons.items():
        img.save(OUT / f"favicon-{s}.png", optimize=True)
    favicons[48].save(OUT / "favicon.ico", sizes=[(s, s) for s in favicons],
                      append_images=[favicons[16], favicons[32]])
    tile(180).save(OUT / "apple-touch-icon.png", optimize=True)  # iOS rounds it itself
    rounded(tile(192)).save(OUT / "icon-192.png", optimize=True)
    rounded(tile(512)).save(OUT / "icon-512.png", optimize=True)
    maskable(512).save(OUT / "icon-maskable-512.png", optimize=True)
    print(f"wrote 8 icons to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
