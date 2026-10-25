"""Colour and length helpers shared by the builders. Generic: nothing here is Cursor's.

Every colour string Chromium computes (hex, rgb(), rgba(), color(srgb ...), oklch(), oklab())
becomes '#rrggbb' or 'rgba(r, g, b, a)' in sRGB, 8 bits a channel.
"""
import math
import re


def _lin_to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def oklab_rgb(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb = [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s]
    return [round(min(1, max(0, _lin_to_srgb(x))) * 255) for x in rgb]


def lab_rgb(L, a, b):
    """CIE Lab (D50, as CSS lab()/lch()) -> 8-bit sRGB, through XYZ with the Bradford D50 -> D65 adaptation."""
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    e, k = 216 / 24389, 24389 / 27
    inv = lambda t: t ** 3 if t ** 3 > e else (116 * t - 16) / k
    X, Y, Z = inv(fx) * 0.3457 / 0.3585, (fy ** 3 if L > k * e else L / k), inv(fz) * (1 - 0.3457 - 0.3585) / 0.3585
    X, Y, Z = (0.9554734527042182 * X - 0.023098536874261423 * Y + 0.0632593086610217 * Z,
               -0.028369706963208136 * X + 1.0099954580058226 * Y + 0.021041398966943008 * Z,
               0.012314001688319899 * X - 0.020507696433808497 * Y + 1.3303659366080753 * Z)
    rgb = [3.2409699419045226 * X - 1.537383177570094 * Y - 0.4986107602930034 * Z,
           -0.9692436362808796 * X + 1.8759675015077202 * Y + 0.04155505740717559 * Z,
           0.05563007969699366 * X - 0.20397695888897652 * Y + 1.0569715142428786 * Z]
    return [round(min(1, max(0, _lin_to_srgb(x))) * 255) for x in rgb]


def fmt(rgb, a=1):
    a = round(float(a), 3)
    if a >= 1:
        return "#%02x%02x%02x" % tuple(rgb)
    return "rgba(%d, %d, %d, %s)" % (rgb[0], rgb[1], rgb[2], "%g" % a)


NUM = r"(-?[\d.]+(?:e-?\d+)?%?)"


def _f(x):
    return float(x[:-1]) / 100 if x.endswith("%") else float(x)


def color(c):
    """A computed colour string -> '#rrggbb' or 'rgba(r, g, b, a)'. Raises on anything else."""
    c = c.strip()
    if c in ("transparent", "none"):
        return "rgba(0, 0, 0, 0)"
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", c)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(ch * 2 for ch in h)
        return fmt([int(h[i:i + 2], 16) for i in (0, 2, 4)], int(h[6:8], 16) / 255 if len(h) == 8 else 1)
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", c)
    if m:
        return fmt([round(float(m.group(i))) for i in (1, 2, 3)], m.group(4) or 1)
    m = re.fullmatch(rf"color\(srgb {NUM} {NUM} {NUM}(?: / {NUM})?\)", c)
    if m:
        return fmt([round(min(1, max(0, _f(m.group(i)))) * 255) for i in (1, 2, 3)], _f(m.group(4)) if m.group(4) else 1)
    m = re.fullmatch(rf"oklch\({NUM} {NUM} {NUM}(?: / {NUM})?\)", c)
    if m:
        L, C, H = _f(m.group(1)), float(m.group(2)), float(m.group(3))
        return fmt(oklab_rgb(L, C * math.cos(math.radians(H)), C * math.sin(math.radians(H))), _f(m.group(4)) if m.group(4) else 1)
    m = re.fullmatch(rf"(lch|lab)\({NUM} {NUM} {NUM}(?: / {NUM})?\)", c)
    if m:
        L, x, y = float(m.group(2).rstrip("%")), float(m.group(3)), float(m.group(4))
        a, b = (x * math.cos(math.radians(y)), x * math.sin(math.radians(y))) if m.group(1) == "lch" else (x, y)
        return fmt(lab_rgb(L, a, b), _f(m.group(5)) if m.group(5) else 1)
    m = re.fullmatch(rf"oklab\({NUM} {NUM} {NUM}(?: / {NUM})?\)", c)
    if m:
        return fmt(oklab_rgb(_f(m.group(1)), float(m.group(2)), float(m.group(3))), _f(m.group(4)) if m.group(4) else 1)
    raise ValueError("colour not understood: " + c)


def is_color(c):
    try:
        color(c)
        return True
    except ValueError:
        return False


def split_top(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


COLOR_RE = r"(#[0-9a-fA-F]{3,8}|(?:rgba?|color|oklab|oklch|lab|lch)\((?:[^()]|\([^()]*\))*\))"


def px(v):
    m = re.fullmatch(r"(-?\d*\.?\d+(?:e[-+]?\d+)?)px", str(v).strip())
    if not m:
        raise ValueError("not a px length: %r" % v)
    f = float(m.group(1))
    if abs(f) > 1e6:
        f = 9999
    return ("%g" % round(f, 2)) + "px"


def shadow(v):
    """A computed box-shadow -> DTCG shadow layers ([] for none)."""
    if not v or v.strip() == "none":
        return []
    layers = []
    for part in split_top(v):
        inset = bool(re.search(r"\binset\b", part))
        part = re.sub(r"\binset\b", "", part).strip()
        m = re.search(COLOR_RE, part)
        if not m:
            raise ValueError("shadow without a colour: " + part)
        nums = (part[:m.start()] + " " + part[m.end():]).split()
        nums = [n if n.endswith("px") else n + "px" for n in nums] + ["0px"] * (4 - len(nums))
        layers.append({"color": color(m.group(1)), "offsetX": px(nums[0]), "offsetY": px(nums[1]), "blur": px(nums[2]),
                       "spread": px(nums[3]), "inset": inset})
    return layers


def ms(v):
    m = re.fullmatch(r"([\d.]+)(m?s)", v.strip())
    if not m:
        raise ValueError(v)
    return ("%g" % (float(m.group(1)) * (1 if m.group(2) == "ms" else 1000))) + "ms"


def bezier(v):
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", v.strip())
    if m:
        return [float("%g" % float(x)) for x in m.group(1).split(",")]
    return {"linear": [0, 0, 1, 1], "ease": [0.25, 0.1, 0.25, 1], "ease-in": [0.42, 0, 1, 1], "ease-out": [0, 0, 0.58, 1],
            "ease-in-out": [0.42, 0, 0.58, 1]}.get(v.strip())
