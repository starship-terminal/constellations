"""Write raw/crop-scales.json: the saved pixel size and effective scale of every
crop the measurement pass recorded.

New captures write `cropScale`/`cropPixels` into each state reading (lib.mjs's
quantize reports whether the >1.2-megapixel halving fired); this file derives
the same for readings captured before that field existed, by comparing the
committed PNG's width to the element's recorded CSS rect. A ratio of about 1 is
a halved crop, about 2 is full 2x — the padding around the element makes the
ratio slightly above the nominal scale, so the label rounds to the nearer of
{1, 2}. Run after build_components_md.py inputs exist:

    PYTHON=<python with Pillow> python3 tools/build_crop_scales.py
"""
import ast, json, pathlib

from PIL import Image

REF = pathlib.Path(__file__).resolve().parent.parent
C = json.load(open(REF / "raw/components-computed.json"))["components"]


def focus_not_captured(v):
    """A skipped state, or a focus-visible reading where keyboard focus never landed ("focus
    failed") or did not match :focus-visible: its crop is the element at rest, not that state, so it
    is not a crop of the state (the kit's rule, tools/kit/build/build_components_md.py)."""
    return bool(v.get("skipped")) or v.get("via") == "focus failed" or (v.get("focus") or {}).get("matches") is False


out = {}
for key, c in C.items():
    for state, st in c["states"].items():
        file = st.get("crop")
        if not file or focus_not_captured(st):
            continue
        p = REF / file
        if not p.exists():
            continue
        px = st.get("cropPixels")
        scale = st.get("cropScale")
        if px is None:
            im = Image.open(p)
            px = [im.width, im.height]
        if scale is None:
            try:
                rect = ast.literal_eval(st["rect"]) if isinstance(st.get("rect"), str) else st.get("rect") or {}
            except (ValueError, SyntaxError):
                rect = {}
            w = rect.get("w")
            scale = min((1, 2), key=lambda s: abs(px[0] / w - s)) if w else None
        out[file] = {"component": key, "state": state, "pixels": px, "scale": scale}

dst = REF / "raw/crop-scales.json"
json.dump(out, open(dst, "w"), indent=1)
one = sum(1 for v in out.values() if v["scale"] == 1)
two = sum(1 for v in out.values() if v["scale"] == 2)
print(f"{dst.name}: {len(out)} crops — {two} at 2x, {one} halved to 1x")
