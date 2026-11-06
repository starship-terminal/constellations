#!/usr/bin/env python3
"""Crop verified native screenshot pixels using raw/crops.json.

The mapping is {"output-name.png": {"screenshot":"screenshots/name.png",
"box":[left,top,right,bottom],"coordinateSpace":"native-screenshot-pixels"}}.
Boxes must be chosen against the actual screenshot. Live DOM rectangles are
not valid crop coordinates for this capture because the layouts reflowed.
Pillow is an existing repository capture dependency.
"""
import json
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent.parent


def build():
    manifest = json.loads((HERE / "raw" / "crops.json").read_text())
    target = HERE / "components" / "crops"
    target.mkdir(parents=True, exist_ok=True)
    for filename, spec in sorted(manifest.items()):
        if Path(filename).name != filename or not filename.endswith(".png"):
            raise ValueError(f"Unsafe crop output name: {filename}")
        if spec.get("coordinateSpace") != "native-screenshot-pixels":
            raise ValueError(f"{filename}: verify its box against native screenshot pixels")
        image_path = (HERE / spec["screenshot"]).resolve()
        if not image_path.is_relative_to((HERE / "screenshots").resolve()):
            raise ValueError(f"{filename}: source must be under screenshots/")
        with Image.open(image_path) as image:
            box = spec["box"]
            if len(box) != 4 or any(not isinstance(n, int) for n in box):
                raise ValueError(f"{filename}: expected four integer pixel coordinates")
            left, top, right, bottom = box
            if not (0 <= left < right <= image.width and 0 <= top < bottom <= image.height):
                raise ValueError(f"{filename}: box {box} exceeds screenshot {image.size}")
            image.crop(box).save(target / filename, optimize=False)
    print(f"components/crops: {len(manifest)} verified native pixel crops")


if __name__ == "__main__":
    build()
