#!/usr/bin/env python3
"""Store the full-colour window captures as 256-colour PNGs in screenshots/<theme>/.

    python3 tools/capture/quantize.py ~/.design-systems/capy-desktop/raw-shots

RAW holds <theme>/<shot>.png from shots.mjs and <theme>/run/<frame>.png from run.mjs. Every shot that
<theme>/captures.json records is kept; of the run frames only those named in RUN_FRAMES (PRODUCT, adapt) are, renamed to
run-<state>.png. CDP's captureScreenshot tags the PNG with the display's profile, but its pixels are
the page's sRGB values (a check: Capy's light --card, oklch(100% 0 0), reads (255, 255, 255)), so the profile is
dropped, not converted. The native window captures in <theme>/native/ (frame.mjs, PRODUCT) are the window server's
Display P3 pixels and are converted to sRGB through their embedded profile. Flat UI colours survive the 256-colour palette exactly; read values from
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

# PRODUCT (adapt): run frames worth keeping, per theme: frame name -> screenshot name. Capy opened the new thread's
# page in its loading state, then refused to start it (no model connection is set up) and went back to the composer
# with an error toast, so the run is those two frames.
RUN_FRAMES = {
    "dark": {"start-thread-00": "run-loading", "start-thread-02": "run-refused"},
    "light": {"start-thread-00": "run-loading", "start-thread-02": "run-refused"},
}
# PRODUCT (adapt): native window captures kept, per theme: file in <theme>/native/ -> screenshot name.
NATIVE = {"window-frame.png": "window-frame"}


def store_p3(src, dst):
    """A screencapture PNG (Display P3, with its profile) -> sRGB, 256 colours."""
    from PIL import ImageCms
    import io
    im = Image.open(src)
    icc = im.info.get("icc_profile")
    im = im.convert("RGB")
    if icc:
        im = ImageCms.profileToProfile(im, ImageCms.ImageCmsProfile(io.BytesIO(icc)), ImageCms.createProfile("sRGB"), outputMode="RGB")
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(dst, optimize=True)


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
        for f, name in NATIVE.items():
            src = theme_dir / "native" / f
            if src.exists():
                store_p3(src, out / f"{name}.png"); keep.add(f"{name}.png"); n += 1
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
