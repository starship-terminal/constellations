#!/usr/bin/env python3
"""Store the window captures as 256-colour PNGs in screenshots/<theme>/.

    /opt/homebrew/bin/python3.14 tools/capture/quantize.py ~/.design-systems/conductor-desktop/raw-shots

RAW holds <theme>/<shot>.png from inspector/shots.py and <theme>/run/<frame>.png from inspector/run.py:
`screencapture -l` of the window, converted from Display P3 to sRGB by `sips` (the P3 original stays
beside it as <shot>.raw.png and is never published). Every shot that <theme>/captures.json records is kept,
plus EXTRA (screens with no reading); of the run frames only those named in RUN_FRAMES (PRODUCT, adapt) are,
renamed to run-<state>.png. Flat UI colours survive the 256-colour palette; read values from tokens.json,
never from these files. Also copies <theme>/captures.json, css-vars.<theme>.json and <theme>/run/frames.json
(trimmed to what the builders read) into raw/. Needs Pillow. Deterministic for the same inputs.
"""
import json
import pathlib
import sys

from PIL import Image

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1]).expanduser()

# PRODUCT (adapt): screens kept without a reading, and the run frames worth keeping (frame -> screenshot name).
EXTRA = {"dark": ["home-empty"]}
RUN_FRAMES = {
    "dark": {"list-00": "run-list-streaming", "write-00": "run-write-thinking", "write-01": "run-write-tool-calls",
             "write-02": "run-write-finished"},
    "light": {"list-00": "run-list-streaming", "list-01": "run-list-working", "list-02": "run-list-finished",
              "write-00": "run-write-thinking", "write-01": "run-write-tool-calls", "write-02": "run-write-finished"},
}
TRIM = ("color", "background-color", "border-top-color", "border-top-width", "border-top-left-radius", "font-family", "font-size",
        "font-weight", "line-height", "height", "width", "padding-left", "padding-top", "opacity", "_box", "_tag", "_role", "_cls")


def store(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGB")
    im.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(dst, optimize=True)


def main():
    n = 0
    for theme_dir in sorted(p for p in RAW.iterdir() if p.is_dir() and p.name in ("light", "dark")):
        theme = theme_dir.name
        out = PKG / "screenshots" / theme
        keep = set()
        # Only shots captures.json records: a shot that failed on a later run is dropped from it, and its
        # older PNG must not be published again without a current reading.
        shots = json.loads((theme_dir / "captures.json").read_text()) if (theme_dir / "captures.json").exists() else {}
        for f in sorted(theme_dir.glob("*.png")):
            if f.name.endswith(".raw.png"):
                continue
            if f.stem not in shots and f.stem not in EXTRA.get(theme, []):
                print("skipped (no reading in captures.json):", f.name)
                continue
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
        if (theme_dir / "run" / "frames.json").exists():
            frames = json.loads((theme_dir / "run" / "frames.json").read_text())
            for fr in frames.values():
                fr.pop("viewport", None)
                for e in fr.get("els", []):
                    e["style"] = {k: v for k, v in e.get("style", {}).items() if k in TRIM}
                if fr.get("send"):
                    fr["send"]["style"] = {k: v for k, v in fr["send"].get("style", {}).items() if k in TRIM}
            (PKG / "raw" / f"run.{theme}.json").write_text(json.dumps(frames, indent=1) + "\n")
    for theme in ("light", "dark"):
        v = RAW / f"css-vars.{theme}.json"
        if v.exists():
            (PKG / "raw" / f"css-vars.{theme}.json").write_text(v.read_text())
    print(n, "screenshots ->", (PKG / "screenshots").relative_to(PKG))


if __name__ == "__main__":
    main()
