#!/usr/bin/env python3
"""Quantise full-colour shots in a scratch dir into screenshots/.

usage: python3 tools/quantize.py RAW_DIR
"""
import pathlib
import sys
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = pathlib.Path(sys.argv[1])
OUT = HERE / "screenshots"
OUT.mkdir(exist_ok=True)
for src in sorted(RAW.glob("*.png")):
    if ".part" in src.name:
        continue
    im = Image.open(src).convert("RGB")
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(OUT / src.name, optimize=True)
    print(src.name, im.size)
