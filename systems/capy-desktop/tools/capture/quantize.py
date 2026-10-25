#!/usr/bin/env python3
"""Store the full-colour window captures as 256-colour PNGs in screenshots/<theme>/.

    python3 tools/capture/quantize.py ~/.design-systems/capy-desktop/raw-shots

RAW holds <theme>/<shot>.png from shots.mjs and <theme>/run/<frame>.png from run.mjs. Every shot that
<theme>/captures.json records is kept; of the run frames only those RUN_FRAMES (PRODUCT, adapt) picks are, under
the names it gives them. CDP's captureScreenshot tags the PNG with the display's profile, but its pixels are
the page's sRGB values (a check: Capy's light --card, oklch(100% 0 0), reads (255, 255, 255)), so the profile is
dropped, not converted. The native window captures in <theme>/native/ (frame.mjs, PRODUCT) are the window server's
Display P3 pixels and are converted to sRGB through their embedded profile. Flat UI colours survive the 256-colour palette exactly; read values from
tokens.json, never from these files. Also copies <theme>/captures.json into raw/ as
components.<theme>.json, and writes the kept run frames' readings from <theme>/run/frames.json to raw/run.<theme>.json. Needs Pillow. Deterministic for the same
inputs.
"""
import json
import pathlib
import sys

from PIL import Image

PKG = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = pathlib.Path(sys.argv[1]).expanduser()

# PRODUCT (adapt): run frames worth keeping, chosen by the state run.mjs recorded for each frame (product.mjs's
# RUN.state), so a new run is picked the same way although its timing differs: screenshot name -> (step, pick).
# A pick is a frame-name suffix ("00", "done") or a function of the step's frames [(name, state), ...] that
# returns one name. Capy 0.5.0 ran each prompt on this Mac in a few seconds: the thread page loads, the agent
# thinks, runs one tool, streams its reply and stops; the inspector step only opens the right pane.
def _before_first(state, then):
    """The last `state` frame before the first `then` frame."""
    def pick(frames):
        i = next(i for i, (_, s) in enumerate(frames) if s == then)
        return [n for n, s in frames[:i] if s == state][-1]
    return pick


def _first_after_last(state, after):
    """The first `state` frame after the last `after` frame: the reply a moment after its first words."""
    def pick(frames):
        i = max(i for i, (_, s) in enumerate(frames) if s == after)
        return next(n for n, s in frames[i:] if s == state)
    return pick


def _end_of_first(state):
    """The last frame of the first unbroken run of `state` frames: the tool row as late as it still runs."""
    def pick(frames):
        i = next(i for i, (_, s) in enumerate(frames) if s == state)
        while i + 1 < len(frames) and frames[i + 1][1] == state:
            i += 1
        return frames[i][0]
    return pick


RUN_FRAMES = {
    "run-loading": ("list-files", "00"),
    "run-thinking": ("list-files", _before_first("thinking", "tool")),
    "run-tool": ("list-files", _end_of_first("tool")),
    "run-streaming": ("list-files", _first_after_last("streaming", "tool")),
    "run-done": ("list-files", "done"),
    "run-tool-write": ("create-file", _end_of_first("tool")),
    "run-result": ("create-file", "done"),
    "run-inspector": ("inspector", "done"),
}

# PRODUCT (adapt): the parts each kept frame contributes to raw/run.<theme>.json, and so to crops and components.md.
# run.mjs measures every RUN.part on every frame; most repeat from frame to frame (the composer, the timestamp)
# or are hidden until hovered (the message footer), so each frame keeps the parts it is the best view of. A part
# and state are cropped once, from the first frame here that has them.
RUN_PARTS = {
    "run-loading": ["composer", "thread-tab"],
    "run-thinking": ["activity-line", "work-row", "shimmer-live", "working-indicator"],
    "run-tool": ["activity-line", "stop-button"],
    "run-streaming": ["agent-message", "inline-code"],
    "run-done": ["user-message", "agent-message", "activity-line", "chat-stamp", "composer", "machine-button", "thread-cost", "token-budget"],
    "run-tool-write": ["work-row", "shimmer-live"],
    "run-result": [],
    "run-inspector": ["right-panel", "thread-tab"],
}


def run_frames(frames):
    """Screenshot name -> frame name, for one theme's frames.json."""
    steps = {}
    for name, f in frames.items():
        steps.setdefault(f["step"], []).append((name, f["state"]))
    out = {}
    for shot, (step, pick) in RUN_FRAMES.items():
        fr = steps.get(step, [])
        out[shot] = f"{step}-{pick}" if isinstance(pick, str) else pick(fr)
    return out


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
        frames_json = theme_dir / "run" / "frames.json"
        frames = json.loads(frames_json.read_text()) if frames_json.exists() else {}
        kept = {}
        for name, frame in run_frames(frames).items():
            f = theme_dir / "run" / f"{frame}.png"
            if f.exists():
                store(f, out / f"{name}.png"); keep.add(f"{name}.png"); n += 1
                f_ = frames[frame]
                kept[name] = {"frame": frame, **{k: v for k, v in f_.items() if k not in ("parts", "inventory")},
                              "parts": {k: v for k, v in f_["parts"].items() if k in RUN_PARTS.get(name, [])},
                              "inventory": f_["inventory"]}
        for f, name in NATIVE.items():
            src = theme_dir / "native" / f
            if src.exists():
                store_p3(src, out / f"{name}.png"); keep.add(f"{name}.png"); n += 1
        for stale in out.glob("*.png"):
            if stale.name not in keep:
                stale.unlink()
        if (theme_dir / "captures.json").exists():
            (PKG / "raw" / f"components.{theme}.json").write_text((theme_dir / "captures.json").read_text())
        if frames:
            # Only the frames kept as screenshots, under their screenshot names, so crops.py and
            # build_components_md.py can read their parts like a shot's.
            (PKG / "raw" / f"run.{theme}.json").write_text(json.dumps(kept, indent=1) + "\n")
    print(n, "screenshots ->", (PKG / "screenshots").relative_to(PKG))


if __name__ == "__main__":
    main()
