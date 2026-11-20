#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json and tokens.json.

Values are the measured cells. A colour is hex plus the semantic token whose
value matches, when one does. Re-running on the same inputs is deterministic.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.loads((ROOT / "raw" / "components-computed.json").read_text())
T = json.loads((ROOT / "tokens.json").read_text())
C = J["components"]


def flat(node, prefix=""):
    for k, v in node.items():
        if str(k).startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


# One colour map per theme: a dark row is labelled from the dark set, a light
# row from the light set, so a value both sets hold names the theme it was read in.
BY_COLOR = {"light": {}, "dark": {}}
for theme in ("light", "dark"):
    for name, tok in flat(T[theme]):
        if tok.get("$type") == "color":
            BY_COLOR[theme].setdefault(tok["$value"].lower(), f"{theme}.{name}")


def theme_of(comp):
    """The theme a component was read in, from its recorded theme or page."""
    t = comp.get("theme") or ("dark" if str(comp.get("page", "")).endswith("-dark") else "light")
    return "dark" if t == "dark" else "light"


def hex_of(css):
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+)\s*)?\)", css.strip())
    if not m:
        return css
    r, g, b = (int(round(float(m.group(i)))) for i in (1, 2, 3))
    a = m.group(4)
    if a is None or float(a) >= 0.999:
        return "#%02x%02x%02x" % (r, g, b)
    if float(a) == 0:
        return "transparent"
    return "rgba(%d, %d, %d, %g)" % (r, g, b, round(float(a), 3))


def colour(css, theme="light"):
    h = hex_of(css)
    tok = BY_COLOR[theme].get(h.lower())
    return f"{h} `{tok}`" if tok else h


def px(v):
    if isinstance(v, (int, float)):
        return f"{v:g}px" if not isinstance(v, str) else v
    s = str(v)
    if re.fullmatch(r"-?\d+(\.\d+)?", s):
        n = float(s)
        return f"{int(n)}px" if n == int(n) else f"{n:.2f}px"
    return s


def box(rect):
    return f"{rect['w']:.0f} x {rect['h']:.0f}" if rect else ""


GROUPS = [
    ("Header", ["logo", "nav-explore", "nav-signin", "nav-join", "nav-join-dark", "search", "m-join", "m-search"]),
    ("Home", ["hero-title", "hero-title-dark", "join-free", "app-store", "m-hero"]),
    ("Sign in", ["signin-title", "email-field", "email-field-dark", "password-field", "forgot", "signin-submit", "signin-submit-dark", "apple", "signup-link"]),
    ("Book", ["book-title", "want-to-read", "show-more", "review-like", "review-comment", "author-link", "book-card"]),
    ("Profile", ["follow", "profile-tab", "avatar"]),
]


def state_line(name, state, data, theme="light"):
    style = data.get("style", {})
    bits = [f"**{state}**"]
    if data.get("rect"):
        bits.append(box(data["rect"]))
    if style.get("backgroundColor") and style["backgroundColor"] != "rgba(0, 0, 0, 0)":
        bits.append("bg " + colour(style["backgroundColor"], theme))
    if style.get("color"):
        bits.append("text " + colour(style["color"], theme))
    if style.get("fontSize"):
        bits.append(f"{style.get('fontSize')} / {style.get('fontWeight')} {style.get('fontFamily', '').split(',')[0]}")
    # The capture records radius as the four corner longhands, never the shorthand.
    corners = [style.get(k) for k in ("borderTopLeftRadius", "borderTopRightRadius", "borderBottomRightRadius", "borderBottomLeftRadius")]
    if any(c and c != "0px" for c in corners):
        bits.append("radius " + (corners[0] if len(set(corners)) == 1 else " ".join(corners)))
    crop = ROOT / "components" / "crops" / f"{name}-{state}.png"
    shot = f"[{name}-{state}](components/crops/{name}-{state}.png)" if crop.exists() else "no crop"
    return f"- {shot}: " + "; ".join(bits)


lines = [
    "# Literal.club components",
    "",
    "Measured signed out on literal.club, 2026-11-18, desktop 1440 x 900 and phone 390 x 844. "
    "Hover is a real pointer. Pressed is a forced `:active` state, so no control was activated. "
    "Email and password were not typed. Dark rows were read with `prefers-color-scheme: dark`.",
    "",
    "Crops live in [components/crops/](components/crops). Colours that match a token name that token. "
    "Read the number from [tokens.json](tokens.json), not from the crop.",
    "",
]
for title, names in GROUPS:
    lines += [f"## {title}", ""]
    for name in names:
        comp = C.get(name)
        if not comp:
            continue
        lines.append(f"### {name}")
        lines.append("")
        for state, data in comp.get("states", {}).items():
            lines.append(state_line(name, state, data, theme_of(comp)))
        lines.append("")

lines += [
    "## Gaps",
    "",
    "These controls were measured and not activated. No measurement was invented for a state that did not paint.",
    "",
    "- Sign in, Join, Continue, and Sign in with Apple (OAuth) were not followed. The account after sign-in was not opened.",
    "- Want to read, Follow, Like, and Comment need an account and were not activated.",
    "- Forgot password was not followed.",
    "- No text area, switch, dialog, toast, table, or tooltip was open on the public pages that were measured.",
    "- Dark accent hover, active, and disabled resolve to the same greens as light, because the dark block does not redeclare them.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("wrote", ROOT / "components.md")
