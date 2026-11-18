"""Crop the top of a full-page PNG to a viewport. Used when Lenis leaves a
viewport screenshot mid-scroll while window.scrollY stays 0."""
import sys
from PIL import Image

src, dst, w, h = sys.argv[1:]
im = Image.open(src)
im.crop((0, 0, int(w), int(h))).save(dst)
