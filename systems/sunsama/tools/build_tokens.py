#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json.

Read from www.sunsama.com on 2026-11-21. Marketing colours live on :root.
The public app-demo layer (.sslab) declares --ss-* for light, and again
under .sslab[data-theme="dark"]. vars.mjs resolves both. A name that
resolves empty is omitted and listed under $extensions.notTokenised.
Unread values stay Not captured. Nothing is invented.

Deterministic: same css-vars.json, same tokens.json.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
DECL = {
    t: {n: rec.get("value", rec.get("raw")) for n, rec in V["resolved"][t].items() if rec.get("value") is not None or rec.get("raw")}
    for t in ("light", "dark")
}

DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")


def norm_color(v):
    v = str(v).strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        if len(h) == 8:
            a = round(int(h[6:8], 16) / 255, 3)
            return "#%02x%02x%02x" % (r, g, b) if a >= 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a)
        return "#%02x%02x%02x" % (r, g, b)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+))?\s*\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(r), int(g), int(b))
        return "rgba(%d, %d, %d, %g)" % (int(r), int(g), int(b), float(a))
    raise ValueError("not a colour: " + v)


def color(name, theme, desc):
    raw = DECL[theme][name]
    return {
        "$value": norm_color(raw),
        "$type": "color",
        "$description": desc,
        "$extensions": {"source": f"css-var {name} ({theme}), resolved from www.sunsama.com stylesheets"},
    }


def dim(name, theme, desc):
    raw = str(DECL[theme][name])
    if not DIM.fullmatch(raw):
        raise ValueError(f"{name}: not a dimension: {raw}")
    return {
        "$value": raw,
        "$type": "dimension",
        "$description": desc,
        "$extensions": {"source": f"css-var {name} ({theme}), resolved from www.sunsama.com stylesheets"},
    }


def font(name, theme, desc):
    return {
        "$value": DECL[theme][name],
        "$type": "fontFamily",
        "$description": desc,
        "$extensions": {"source": f"css-var {name} ({theme}), resolved from www.sunsama.com stylesheets"},
    }


def number(name, theme, desc):
    raw = DECL[theme][name]
    val = float(raw) if isinstance(raw, str) else raw
    if val == int(val):
        val = int(val)
    return {
        "$value": val,
        "$type": "number",
        "$description": desc,
        "$extensions": {"source": f"css-var {name} ({theme}), resolved from www.sunsama.com stylesheets"},
    }


def shadow(name, theme, desc):
    raw = str(DECL[theme][name])
    # computed form: rgba(...) 0px 1px 2px 0px
    m = re.fullmatch(
        r"(rgba?\([^)]+\)|#[0-9a-fA-F]{3,8})\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)\s+(-?[\d.]+px)",
        raw,
    )
    if not m:
        raise ValueError(f"{name}: shadow not read: {raw}")
    col, x, y, blur, spread = m.groups()
    return {
        "$value": {"color": norm_color(col), "offsetX": x, "offsetY": y, "blur": blur, "spread": spread},
        "$type": "shadow",
        "$description": desc,
        "$extensions": {"source": f"css-var {name} ({theme}), computed box-shadow from www.sunsama.com"},
    }


def nest(path, token):
    node = {}
    cur = node
    parts = path.split(".")
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
    cur[parts[-1]] = token
    return node


def merge(a, b):
    for k, v in b.items():
        if k in a and isinstance(a[k], dict) and isinstance(v, dict) and "$value" not in v:
            merge(a[k], v)
        else:
            a[k] = v
    return a


# Marketing :root colours. Same in both probe passes.
MARKETING = {
    "color.ink": ("--black", "Page ink. Declared on :root as --black."),
    "color.ink-soft": ("--light-black", "Secondary ink. Declared as --light-black."),
    "color.orange": ("--ss-orange", "Brand orange used on headlines and the wordmark accent."),
    "color.orange-deep": ("--ss-dark-organge", "Deeper orange. The stylesheet spells the name organge."),
    "color.orange-wash": ("--orange-light", "Light orange wash."),
    "color.blue": ("--blue", "Marketing blue."),
    "color.page": ("--bg-light-grey-new", "Page ground."),
    "color.page-secondary": ("--bg-secondary-new", "Warm secondary ground."),
    "color.page-grey": ("--gradient-bg-grey", "Grey section ground."),
    "color.border": ("--border-new", "Hairline border."),
    "color.border-strong": ("--border-dark", "Stronger border."),
    "color.border-warm": ("--border-2-new", "Warm translucent border."),
    "color.card-veil": ("--card-bg-white-50-new", "Half-white card veil."),
    "color.grey": ("--grey", "Neutral grey."),
}

# App demo tokens that change, or exist, on .sslab.
APP_COLOR = {
    "page": ("--ss-bg", "App demo page."),
    "surface": ("--ss-bg-muted", "Muted surface."),
    "base": ("--ss-bg-base", "Base well."),
    "raised": ("--ss-bg-highlight", "Raised highlight."),
    "raised-muted": ("--ss-bg-muted-highlight", "Muted raised surface."),
    "overlay": ("--ss-bg-overlay", "Overlay scrim."),
    "text": ("--ss-text", "Primary text."),
    "text-secondary": ("--ss-text-secondary", "Secondary text."),
    "text-muted": ("--ss-text-muted", "Muted text."),
    "border": ("--ss-border", "Default border."),
    "border-divider": ("--ss-border-divider", "Divider."),
    "border-input": ("--ss-border-input", "Input border."),
    "border-layout": ("--ss-border-layout", "Layout border."),
    "ghost": ("--ss-ghost", "Ghost fill."),
    "accent": ("--ss-blue", "App blue."),
    "success": ("--ss-green", "Success green."),
    "danger": ("--ss-red", "Danger red."),
    "warning": ("--ss-caution", "Caution yellow."),
    "warning-text": ("--ss-caution-text", "Text on caution."),
    "alert": ("--ss-alert", "Alert orange."),
    "info": ("--ss-purple-objective", "Objective purple."),
    "urgent": ("--ss-urgent", "Urgent."),
    "urgent-bg": ("--ss-urgent-bg", "Urgent background."),
    "important": ("--ss-important", "Important."),
    "important-bg": ("--ss-important-bg", "Important background."),
    "low": ("--ss-low", "Low priority."),
    "low-bg": ("--ss-low-bg", "Low priority background."),
    "channel-blue": ("--ss-channel-blue", "Channel blue."),
    "channel-purple": ("--ss-channel-purple", "Channel purple."),
    "channel-green": ("--ss-channel-green", "Channel green."),
    "channel-orange": ("--ss-channel-orange", "Channel orange."),
    "channel-grey": ("--ss-channel-grey", "Channel grey."),
}

APP_DIM = {
    "radius": ("--ss-radius", "Default radius."),
    "radius-sm": ("--ss-radius-sm", "Small radius."),
    "radius-pill": ("--ss-radius-pill", "Pill radius."),
    "radius-circle": ("--ss-radius-circle", "Circle radius."),
    "text-1": ("--ss-text-1", "Smallest text size."),
    "text-2": ("--ss-text-2", "Caption size."),
    "text-3": ("--ss-text-3", "Body size."),
    "text-4": ("--ss-text-4", "Large body size."),
    "text-6": ("--ss-text-6", "Title size. --ss-text-5 is not declared."),
    "column-width": ("--ss-column-width", "Task column width."),
    "calendar-gutter": ("--ss-calendar-gutter", "Calendar gutter."),
    "card-padding": ("--ss-card-padding", "Card padding."),
    "card-gap": ("--ss-card-gap", "Card gap."),
    "calendar-pane": ("--ss-calendar-pane", "Calendar pane width."),
}

not_tokenised = []
core = {}
for path, (name, desc) in MARKETING.items():
    if name not in DECL["light"]:
        not_tokenised.append(name)
        continue
    merge(core, nest(path, color(name, "light", desc)))

merge(core, nest("font.app", font("--ss-font", "light", "App demo stack. Marketing headlines use DM Sans, which is a @font-face, not a custom property.")))
merge(core, nest("font.leading", number("--ss-leading", "light", "App demo line height.")))
for path, (name, desc) in APP_DIM.items():
    if name not in DECL["light"]:
        not_tokenised.append(name)
        continue
    merge(core, nest("size." + path, dim(name, "light", desc)))
for path, (name, desc) in {
    "card": ("--ss-shadow-card", "Card shadow."),
    "button": ("--ss-shadow-button", "Button shadow."),
    "modal": ("--ss-shadow-modal", "Modal shadow."),
}.items():
    merge(core, nest("shadow." + path, shadow(name, "light", desc + " Dark values differ; see the dark set.")))

def semantic(theme):
    out = {}
    roles = {
        "page": ("--bg-light-grey-new", "Marketing page ground."),
        "surface": ("--bg-secondary-new", "Warm secondary ground."),
        "text": ("--black", "Marketing ink."),
        "muted": ("--light-black", "Secondary ink."),
        "accent": ("--ss-orange", "Brand orange."),
        "border": ("--border-dark", "Strong border."),
        "link": ("--blue", "Marketing blue link colour."),
    }
    for role, (name, desc) in roles.items():
        merge(out, nest(role, color(name, "light", desc + " Marketing :root. Same in both themes.")))
    app = {}
    for role, (name, desc) in APP_COLOR.items():
        if name not in DECL[theme]:
            not_tokenised.append(f"{theme}:{name}")
            continue
        app[role.replace("-", "_") if False else role] = color(name, theme, desc + f" Declared on .sslab{'' if theme == 'light' else '[data-theme=dark]'}.")
    # keys with hyphens are fine in DTCG
    out["app"] = {}
    for role, (name, desc) in APP_COLOR.items():
        if name not in DECL[theme]:
            continue
        key = role.replace("-", "_")
        # keep readable hyphenated groups via nesting
        parts = role.split("-")
        if len(parts) == 1:
            out["app"][role] = color(name, theme, desc)
        else:
            out["app"].setdefault(parts[0], {})
            out["app"][parts[0]]["-".join(parts[1:])] = color(name, theme, desc)
    for path, (name, desc) in {
        "card": ("--ss-shadow-card", "Card elevation in this theme."),
        "button": ("--ss-shadow-button", "Button elevation in this theme."),
        "modal": ("--ss-shadow-modal", "Modal elevation in this theme."),
    }.items():
        if name in DECL[theme]:
            out.setdefault("elevation", {})[path] = shadow(name, theme, desc)
    return out


light = semantic("light")
dark = semantic("dark")
# Marketing roles are identical. Dark set keeps them so a theme toggle still has a page colour,
# and adds the app demo colours that actually change.
light["$extensions"] = {
    "notTokenised": sorted(set(not_tokenised)),
    "note": "Marketing roles come from :root. App roles come from .sslab. Dark app roles come from .sslab[data-theme=dark], declared in the public CSS. The marketing pages do not paint that attribute.",
}
dark["$extensions"] = {
    "note": "App colours that differ under .sslab[data-theme=dark]. Marketing :root colours do not change. The public site has no theme switch that sets this attribute.",
}

tokens = {
    "core": core,
    "light": light,
    "dark": dark,
    "$themes": [
        {
            "id": "light",
            "name": "Light",
            "selectedTokenSets": {"core": "source", "light": "enabled"},
            "$description": "The public marketing site and the light app-demo tokens on .sslab.",
        },
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$description": "App-demo tokens declared on .sslab[data-theme=dark]. Not painted by the marketing pages.",
        },
    ],
    "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2) + "\n")


def count(d):
    if not isinstance(d, dict) or "$value" in d:
        return 1 if isinstance(d, dict) and "$value" in d else 0
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in tokens.items() if k in ("core", "light", "dark")})
