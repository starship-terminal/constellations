#!/usr/bin/env python3
"""Store the full-colour window captures as 256-colour PNGs in screenshots/<theme>/.

    python3 tools/capture/quantize.py ~/.design-systems/notion-calendar-desktop/raw-shots

RAW holds <theme>/<shot>.png from shots.mjs and <theme>/run/<frame>.png from run.mjs. Every shot is
kept; of the run frames only those named in RUN_FRAMES (PRODUCT, adapt) are, renamed to
run-<state>.png. CDP's captureScreenshot tags the PNG with the display's profile, but its pixels are
the page's sRGB values (a check: Notion Calendar's dark page, --nds-surface-contr-page #191919, reads (25, 25, 25) in the dark week screenshot), so the profile is
dropped, not converted. Flat UI colours survive the 256-colour palette exactly; read values from
tokens.json, never from these files. Also copies <theme>/captures.json and <theme>/run/frames.json
into raw/ as components.<theme>.json and run.<theme>.json, and the readings vars.mjs and utilities.mjs
wrote beside them (<theme>/css-vars.json, css-vars.ide.json, utilities.json) as css-vars.<theme>.json,
css-vars.ide-<theme>.json and utilities.<theme>.json. Needs Pillow. Deterministic for the same
inputs.
"""
import json
import pathlib
import sys

from PIL import Image

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1]).expanduser()

# PRODUCT (adapt): run frames worth keeping, per theme. Notion Calendar has no agent run, so none.
RUN_FRAMES = {}


def store(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGB")
    im.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(dst, optimize=True)


def main():
    n = 0
    for theme_dir in sorted(p for p in RAW.iterdir() if p.is_dir()):
        theme = theme_dir.name
        out = PKG / "screenshots" / theme
        keep = set()
        for f in sorted(theme_dir.glob("*.png")):
            store(f, out / f.name); keep.add(f.name); n += 1
        for frame, name in RUN_FRAMES.get(theme, {}).items():
            f = theme_dir / "run" / f"{frame}.png"
            if f.exists():
                store(f, out / f"{name}.png"); keep.add(f"{name}.png"); n += 1
        for stale in out.glob("*.png"):
            if stale.name not in keep:
                stale.unlink()
        if (theme_dir / "captures.json").exists():
            (PKG / "raw" / f"components.{theme}.json").write_text((theme_dir / "captures.json").read_text())
        for src, dst in (("css-vars.json", f"css-vars.{theme}.json"), ("css-vars.ide.json", f"css-vars.ide-{theme}.json"),
                         ("utilities.json", f"utilities.{theme}.json")):
            if (theme_dir / src).exists():
                (PKG / "raw" / dst).write_text((theme_dir / src).read_text())
        if (theme_dir / "run" / "frames.json").exists():
            frames = json.loads((theme_dir / "run" / "frames.json").read_text())
            (PKG / "raw" / f"run.{theme}.json").write_text(json.dumps(frames, indent=1) + "\n")
    print(n, "screenshots ->", (PKG / "screenshots").relative_to(PKG))


if __name__ == "__main__":
    main()
