#!/usr/bin/env python3
"""Cut element crops from screenshots/ into components/crops/ as listed in tools/crops.json.

    python3 tools/crops.py

Crops come from the committed 256-colour screenshots, so they show layout, not exact values. A crop
from the light capture gets "-light" before the extension. Needs Pillow. Deterministic.
"""
import json
import pathlib
from PIL import Image

PKG = pathlib.Path(__file__).resolve().parent.parent
SPEC = json.loads((PKG / "tools" / "crops.json").read_text())
OUT = PKG / "components" / "crops"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    made = set()
    for c in SPEC["crops"]:
        x, y, w, h = c["box"]
        for theme in c["themes"]:
            src = PKG / "screenshots" / theme / f"{c['capture']}.png"
            if not src.exists():
                raise SystemExit(f"{c['name']}: no {src.relative_to(PKG)}")
            name = c["name"] + ("-light" if theme == "light" else "") + ".png"
            Image.open(src).crop((x, y, x + w, y + h)).save(OUT / name, optimize=True)
            made.add(name)
    for stale in OUT.glob("*.png"):
        if stale.name not in made:
            stale.unlink()
    print(len(made), "crops ->", OUT.relative_to(PKG))


if __name__ == "__main__":
    main()
