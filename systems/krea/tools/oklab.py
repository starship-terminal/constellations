"""OKLab and OKLCH to sRGB, for the computed colours Chromium reports in Tailwind v4 pages.

The kit's conversion (tools/kit/build/build_tokens.py oklab_rgb), plus oklch(L C H) via its OKLab form.
Imported by build_component_tokens.py and build_tokens.py.
"""
import math
import re


def _lin(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def oklab_rgb(L, a, b):
    """OKLab to 8-bit sRGB, clamped to the gamut (the kit's conversion, tools/kit/build/build_tokens.py)."""
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb = [4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s, -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s]
    return [round(min(1, max(0, _lin(x))) * 255) for x in rgb]


def _num(x, pct_scale=1.0):
    x = x.strip()
    return float(x[:-1]) / 100 * pct_scale if x.endswith("%") else float(x)


def oklab_or_oklch(v):
    """oklab(L a b [/ A]) or oklch(L C H [/ A]) -> #rrggbb or rgba(...), else None."""
    m = re.fullmatch(r"(oklab|oklch)\(\s*([-\d.e%]+)\s+([-\d.e%]+)\s+([-\d.e%]+)(?:deg)?\s*(?:/\s*([\d.]+%?))?\s*\)", v)
    if not m:
        return None
    kind, L, x, y, alpha = m.groups()
    L = _num(L)
    if kind == "oklch":
        c, h = _num(x, 0.4), math.radians(_num(y))
        a, b = c * math.cos(h), c * math.sin(h)
    else:
        a, b = _num(x, 0.4), _num(y, 0.4)
    r, g, bl = oklab_rgb(L, a, b)
    al = 1.0 if alpha is None else _num(alpha)
    return "#%02x%02x%02x" % (r, g, bl) if al >= 1 else "rgba(%d, %d, %d, %g)" % (r, g, bl, round(al, 3))
