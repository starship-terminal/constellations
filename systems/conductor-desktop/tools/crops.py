#!/usr/bin/env python3
"""Cut element crops from screenshots/ into components/crops/, using the boxes inspector/shots.py recorded.

    python3 tools/crops.py

Each measured part of each shot becomes `{part}-{state}.png` (dark) or `{part}-{state}-light.png`,
from the first shot that measured that part in that state. The box is the element's own box in
screenshot pixels, widened by PAD on every side so a focus ring or shadow shows; parts bigger than
half the window (the sidebar, a backdrop) are left to the screenshots. Crops come from the committed
256-colour screenshots: they show layout and state, not exact values. Needs Pillow. Deterministic.
"""
import json
import pathlib

from PIL import Image

try:  # a package may name the shot that holds a part's default reading (tools/prefer.py)
    from prefer import skip
except ImportError:
    def skip(shot, part, state):
        return False

PKG = pathlib.Path(__file__).resolve().parent.parent
OUT = PKG / "components" / "crops"
PAD = 12


def crops(theme):
    caps = json.loads((PKG / "raw" / f"components.{theme}.json").read_text())
    done = {}
    for shot, d in caps.items():
        src = PKG / "screenshots" / theme / f"{shot.split('~')[0]}.png"   # shot~focus shares its shot's screenshot
        if not src.exists():
            # A missing screenshot (a partial checkout, an unpulled LFS tree) must stop the build: skipping it
            # would leave its crops out of `made`, and the sweep below would delete them as stale.
            raise SystemExit(f"{shot}: no {src.relative_to(PKG)}")
        im = None
        for part, v in d["parts"].items():
            key = f"{part}-{d['state']}"
            if skip(shot, part, d["state"]):
                continue
            if key in done or not v.get("box"):
                continue
            x, y, w, h = v["box"]
            im = im or Image.open(src)
            if w * h > im.width * im.height / 2 or w < 4 or h < 4:
                continue
            if x < 0 or y < 0 or x + w > im.width or y + h > im.height:
                continue  # partly scrolled out of the window
            box = (max(0, x - PAD), max(0, y - PAD), min(im.width, x + w + PAD), min(im.height, y + h + PAD))
            name = key + ("-light" if theme == "light" else "") + ".png"
            im.crop(box).save(OUT / name, optimize=True)
            done[key] = name
    return done


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    made = set()
    for theme in ("dark", "light"):
        if (PKG / "raw" / f"components.{theme}.json").exists():
            made |= set(crops(theme).values())
    for stale in OUT.glob("*.png"):
        if stale.name not in made:
            stale.unlink()
    print(len(made), "crops ->", OUT.relative_to(PKG))


if __name__ == "__main__":
    main()
