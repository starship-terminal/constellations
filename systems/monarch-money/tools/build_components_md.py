#!/usr/bin/env python3
"""Write components.md from raw/components-computed.json.

Values are the measured computed styles. Colours are named with a token when
the hex matches. A state row lists only what differs from default.
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
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


BY = {}
for name, tok in list(flat(T.get("light", {}))) + list(flat(T.get("core", {}))):
    if tok.get("$type") == "color" and isinstance(tok.get("$value"), str) and tok["$value"].startswith("#"):
        BY.setdefault(tok["$value"].lower(), name)


def hex_of(c):
    m = re.fullmatch(r"rgb\((\d+), (\d+), (\d+)\)", c or "")
    if m:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    m = re.fullmatch(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", c or "")
    if m and float(m.group(4)) >= 1:
        return "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
    return None


def colour(c):
    if not c or c == "rgba(0, 0, 0, 0)":
        return "transparent"
    h = hex_of(c)
    if not h or h not in BY:
        return c
    name = BY[h]
    # White ink on the orange strip is not the card surface.
    if h == "#ffffff" and name == "light.surface":
        return h
    return f"{h} `{name}`"


def fam(f):
    return (f or "").split(",")[0].replace('"', "")


def row(state, s, base):
    if s.get("via") == "focus failed":
        # D4: keyboard focus never reached the element, so the reading is the element at rest. It is
        # listed as not captured rather than as "same as default", as the kit does.
        return f"| {state} | not captured: keyboard focus did not reach the element |  |  |"
    if not s or "style" not in s:
        return f"| {state} | not measured | | | |"
    st = s["style"]
    bits = []
    bg = colour(st.get("backgroundColor"))
    fg = colour(st.get("color"))
    if base is None or colour(base.get("backgroundColor")) != bg:
        bits.append(f"fill {bg}")
    if base is None or colour(base.get("color")) != fg:
        bits.append(f"ink {fg}")
    radius = st.get("borderTopLeftRadius")
    if base is None or (base.get("borderTopLeftRadius") != radius and radius not in (None, "0px")):
        bits.append(f"radius {radius}")
    h = st.get("height")
    if base is None:
        bits.append(f"{st.get('fontSize')}/{st.get('fontWeight')} {fam(st.get('fontFamily'))}")
        bits.append(f"height {h}")
    via = s.get("via") or ""
    crop = s.get("crop") or ""
    link = f"[crop]({crop})" if crop else ""
    return f"| {state} | {'; '.join(bits) or 'same as default'} | {via} | {link} |"


lines = [
    "# Monarch Money components",
    "",
    "Measured on the public marketing site and the sign-in wall, 2026-11-19, light, 1440. Hover is a real pointer. Focus-visible is keyboard. Pressed is a forced `:active` and was not clicked. Sign up, Sign in, Apple, Google, the trial link and the consent banner were not followed.",
    "",
]
order = [
    "announcement", "nav-link", "nav-features", "sign-in-button", "sign-up-button",
    "hero-title", "footer-cta", "footer", "pricing-title", "plan-card", "plan-cta",
    "faq-item", "oauth-apple", "oauth-google", "email-field", "password-field",
    "signin-submit", "stay-signed-in", "forgot-link", "signup-link", "signup-oauth",
]
seen = set()
for key in order + list(C):
    if key in seen or key not in C:
        continue
    seen.add(key)
    c = C[key]
    lines.append(f"## {c.get('title') or key}")
    lines.append("")
    if c.get("desc"):
        lines.append(c["desc"])
        lines.append("")
    if c.get("missing"):
        lines.append("Not found on the page that was opened.")
        lines.append("")
        continue
    lines.append("| State | What was measured | How | Crop |")
    lines.append("|---|---|---|---|")
    states = c.get("states") or {}
    base = (states.get("default") or {}).get("style")
    for name, s in states.items():
        lines.append(row(name, s, None if name == "default" else base))
    lines.append("")

lines += [
    "## Gaps",
    "",
    "Text area, select, radio, tooltip, toast, table, avatar and badge were not on the captured public pages.",
    "The Stay signed in control is a switch. It was photographed and not toggled.",
    "The Features menu was measured closed. It was not opened.",
    "FAQ rows were measured closed.",
    "The sign-up email field arrived with the site's own placeholder `email@address.com`. Nothing was typed into it and Sign up with email was not pressed.",
    "Disabled, loading and field-error states were not reached. The sign-in submit is half orange while the password is empty. That is the resting state, not an error.",
    "The signed-in app (accounts, transactions, budget, goals, settings) was not entered.",
    "",
]
(ROOT / "components.md").write_text("\n".join(lines))
print("wrote components.md", len(seen), "entries")
