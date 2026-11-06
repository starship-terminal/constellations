#!/usr/bin/env python3
"""Store the full-colour window captures as 256-colour PNGs in screenshots/<theme>/.

    python3 tools/capture/quantize.py ~/.design-systems/superset-desktop/raw-shots

RAW holds <theme>/<shot>.png from shots.mjs and <theme>/run/<frame>.png from run.mjs. Every shot is
kept; of the run frames only those named in RUN_FRAMES (PRODUCT, adapt) are, renamed to
run-<state>.png. CDP's captureScreenshot tags the PNG with the display's profile, but its pixels are
the page's sRGB values (a check: Superset's dark --background #151110 reads (21, 17, 16)), so the profile is
dropped, not converted. Flat UI colours survive the 256-colour palette exactly; read values from
tokens.json, never from these files. Also copies <theme>/captures.json and <theme>/run/frames.json
into raw/ as components.<theme>.json and run.<theme>.json. Needs Pillow. Deterministic for the same
inputs.
"""
import json
import pathlib
import sys

from PIL import Image

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1]).expanduser()

# PRODUCT (adapt): run frames worth keeping, per theme: frame name -> screenshot name. approval-00 is
# not a run.mjs frame: it is the first trial run's window (dark), where Claude Code asked whether to
# trust the scratch folder before starting (see README); copied into run/ by hand.
RUN_FRAMES = {
    "dark": {"approval-00": "run-approval", "list-files-00": "run-started", "list-files-02": "run-thinking",
             "list-files-04": "run-tool-call", "list-files-07": "run-finished", "create-file-04": "run-editing",
             "create-file-06": "run-file-changed", "create-file-07": "run-result"},
    "light": {"list-files-00": "run-started", "list-files-01": "run-thinking", "list-files-04": "run-tool-call",
              "list-files-06": "run-finished", "create-file-02": "run-editing", "create-file-03": "run-file-changed",
              "create-file-06": "run-result"},
}


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
        # Only shots captures.json records: a shot that failed on a later run is dropped from it, and its
        # older PNG must not be published again without a current reading.
        shots = json.loads((theme_dir / "captures.json").read_text()) if (theme_dir / "captures.json").exists() else {}
        for f in sorted(theme_dir.glob("*.png")):
            if f.stem not in shots:
                print("skipped (no reading in captures.json):", f.name)
                continue
            store(f, out / f.name); keep.add(f.name); n += 1
        for frame, name in RUN_FRAMES.get(theme, {}).items():
            f = theme_dir / "run" / f"{frame}.png"
            if f.exists():
                store(f, out / f"{name}.png"); keep.add(f"{name}.png"); n += 1
            elif (out / f"{name}.png").exists():
                # A recapture clears run/ (approval-00 included) and a faster run has fewer frames: never
                # delete a stored run screenshot because its source is gone. Keep it and say so.
                keep.add(f"{name}.png")
                print(f"warning: {theme}/run/{frame}.png missing; kept the stored {name}.png (re-map RUN_FRAMES)")
            else:
                print(f"warning: {theme}/run/{frame}.png missing and no stored {name}.png")
        for stale in out.glob("*.png"):
            if stale.name not in keep:
                stale.unlink()
        if (theme_dir / "captures.json").exists():
            (PKG / "raw" / f"components.{theme}.json").write_text((theme_dir / "captures.json").read_text())
        if (theme_dir / "run" / "frames.json").exists():
            frames = json.loads((theme_dir / "run" / "frames.json").read_text())
            (PKG / "raw" / f"run.{theme}.json").write_text(json.dumps(frames, indent=1) + "\n")
    print(n, "screenshots ->", (PKG / "screenshots").relative_to(PKG))


if __name__ == "__main__":
    main()
