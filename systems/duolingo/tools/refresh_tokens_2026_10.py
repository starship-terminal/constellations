#!/usr/bin/env python3
"""Apply the 2026-10-17 refresh to tokens.json, in place.

The original token builder read scratch inputs that are not shipped, so tokens.json is the
source of record and this script is the record of what the refresh changed. It is idempotent:
run it on the committed tokens.json and nothing changes. Every value it writes is either an
alias to a palette entry already in the file, or a number read in raw/2026-10/; each token
names its source and evidence label (docs/EVIDENCE.md) in $extensions.

    python3 tools/refresh_tokens_2026_10.py && python3 tools/build_style_guide.py
"""
import json, pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = PKG / "tokens.json"
LIVE = "raw/2026-10/live-measurements.json"
COPIES = "raw/2026-10/copy-measurements.json"
CSSEV = "raw/2026-10/css-evidence.json"
t = json.loads(TOK.read_text())
core, pal = t["core"], t["core"]["palette"]


def tok(value, typ, desc, source, evidence):
    return {"$value": value, "$type": typ, "$description": desc, "$extensions": {"source": source, "evidence": evidence}}


def both(path, make):
    """Set the same semantic key in light and dark; make(theme) returns the token."""
    for th in ("light", "dark"):
        node = t[th]
        *parents, leaf = path.split(".")
        for p in parents:
            node = node.setdefault(p, {})
        node[leaf] = make(th)


def hexof(th, name):
    return pal[th][name]["$value"]


def brightness(hex_, k):
    """CSS filter brightness(k): each sRGB channel times k, clamped (Filter Effects 1, a linear feComponentTransfer)."""
    h = hex_.lstrip("#")
    rgb = [min(255, round(int(h[i:i + 2], 16) * k)) for i in (0, 2, 4)]
    return "#" + "".join(f"{c:02x}" for c in rgb)


# --- Type: family stacks (F8) -------------------------------------------------------------
core["fontFamily"]["body"]["$value"] = ["duolingo-sans", "sans-serif"]
core["fontFamily"]["body"]["$extensions"] = {
    "source": f"{LIVE} (2026-10-17): computed font-family on <html> 'duolingo-sans, sans-serif'; css global rule '*,:after,:before,button,input,textarea{{font-family:duolingo-sans,sans-serif}}'",
    "evidence": "Measured"}
core["fontFamily"]["display"]["$value"] = ["feather", "sans-serif"]
core["fontFamily"]["display"]["$extensions"]["evidence"] = "Measured"

# --- Sizing: icons and focus ring (F11) ---------------------------------------------------
size = core["size"]
for key, px, use in (("xs", 16, "inline glyphs in buttons and lists"), ("sm", 18, "top-bar and lesson glyphs"), ("md", 20, "lesson header and settings glyphs"),
                     ("lg", 24, "close, clear and eye buttons (24x24 hit area)"), ("nav", 32, "sidebar and phone tab-bar icons")):
    size.setdefault("icon", {})[key] = tok(
        f"{px}px", "dimension", f"Icon size {px}px: {use}.",
        f"icons.md 'Sizes actually used' (dump node rects); {LIVE}: sidebar <img> 32x32 at 1440 and 1000, tab bar 32x32 at 390" if key == "nav"
        else "icons.md 'Sizes actually used' (dump node rects, distinct assets per size)",
        "Measured")
core["focusRing"] = {
    "width": tok("0px", "dimension",
        "Duolingo draws no focus ring. A live pass on 2026-10-17 pressed Tab 33 times across the learn page, two settings pages and a lesson (sidebar links, text links, outline buttons, an icon button, the theme select, switches, a radio card, word-bank tiles, hint tokens, text fields); every focused control matched :focus-visible, and none but the text fields changed visibly; the only outline property left is the UA outline-offset of 1px on links, with outline-style none. Text fields show focus by turning their 2px border border.focus, and menu rows by a polar fill.",
        f"{LIVE} focus[]; {CSSEV} outline_declarations ('*,:after,:before,button,button:focus,input,textarea{{outline:none}}', '._7jW2t:not(._1ZhE5){{outline:none}}'), focus_visible count 0",
        "Measured"),
    "offset": tok("0px", "dimension", "No ring, so no offset. Kept so a consumer that needs a ring knows Duolingo has none.", f"{LIVE} focus[]", "Measured"),
}

# --- Layout columns (F14) -----------------------------------------------------------------
core["layout"] = {
    "columns": {
        "wide": tok(2, "number", "At 1440: a fixed 256px sidebar, then a centred row (max 1056px, 24px padding, flex row-reverse, 48px gap) holding the main column (flex 1, 592px) and the 368px sticky right rail. No CSS grid; the columns are flex children.",
            f"{LIVE} light/learn/layout-1440 (.wl71D flex row-reverse gap 48px; ._2HEhk 592; ._2SBm1 368 sticky; .AkzqY max-width 1056)", "Measured"),
        "tablet": tok(2, "number", "At 1000: the sidebar collapses to 88px icons and the same two columns remain (main 448px, rail 368px).",
            f"{LIVE} light/learn/layout-1000; screenshots/learn-light-tablet.png", "Measured"),
        "phone": tok(1, "number", "At 390 (below 700px): one 390px column; a 58px top bar and an 82px bottom tab bar replace the sidebar and the rail.",
            f"{LIVE} light/learn/layout-390; {COPIES} learn-light-phone topBar, tabBar", "Measured"),
    }
}

# --- Motion: reduced motion (F13) ---------------------------------------------------------
core["duration"]["reducedMotion"] = tok("0ms", "duration",
    "Under reduced motion the app sets html[reduced-motion] (from matchMedia('(prefers-reduced-motion: reduce)') at load), and 11 rules switch entrance animations (.4s ease-in-out, onboarding and path elements) and the Duo slide transition (.7s) to animation:none or transition:none, so they jump to their end state. The three-dot loader keeps only its opacity keyframes (class _1pK2q). No stylesheet uses @media (prefers-reduced-motion).",
    f"{CSSEV} reduced_motion_attribute (11 rules), prefers_reduced_motion_media (0); js app-4d4b32e8.js useLayoutEffect setAttribute('reduced-motion') and module 70220 matchMedia; js 4779-9b5aed3c.js loader class map 'reduced-motion':'_1pK2q'",
    "Measured")

# --- Colour ramps (F1) --------------------------------------------------------------------
RAMPS = {
    "neutral": ["snow", "polar", "swan", "hare", "wolf", "eel"],
    "green": ["sea-sponge", "turtle", "owl", "tree-frog"],
    "blue": ["iguana", "blue-jay", "macaw", "whale", "humpback", "narwhal"],
    "red": ["walking-fish", "flamingo", "pig", "crab", "cardinal", "fire-ant"],
    "orange": ["cheetah", "fox", "guinea-pig"],
    "yellow": ["canary", "duck", "bee", "camel"],
}
for hue, names in RAMPS.items():
    for i, name in enumerate(names):
        step = str((i + 1) * 100)
        both(f"ramp.{hue}.{step}", lambda th, name=name, hue=hue, step=step: tok(
            "{palette.%s.%s}" % (th, name), "color",
            f"{hue} ramp step {step}: palette '{name}'. Duolingo publishes no ramps; the steps are its own palette names for this hue, ordered lightest to darkest by their light values. In dark the same names invert (snow is the darkest neutral), so this set keeps the names, not the order.",
            "derived from core.palette (palette app-54af2130.js; light and dark checked live, raw/2026-10/rootvars-live.json)", "Derived"))

# --- Background roles (F2) ----------------------------------------------------------------
both("surface.overlay", lambda th: tok("{palette.%s.snow}" % th, "color",
    "Dialog panel (quit, notifications, invite, friend-streak and lesson report dialogs): the page fill, 16px radius, no border and no shadow, on background.scrim.",
    f"{LIVE} light/modal panel ._1yFTM rgb(255,255,255) (2026-10-17); {COPIES} lesson-{th}-report-form-checked popover; dump learn-dark-modal-notifications#358 cl=_1yFTM (dark)",
    "Measured"))
for th in ("light", "dark"):
    t[th]["surface"]["raised"]["$extensions"]["evidence"] = "Measured"

# --- Accent states (F5) -------------------------------------------------------------------
for role, face in (("primary", "owl"), ("secondary", "macaw"), ("danger", "cardinal")):
    both(f"accent.{role}.hover", lambda th, face=face, role=role: tok(
        brightness(hexof(th, face), 1.1), "color",
        f"{role.title()} button on hover: the face colour under filter brightness(1.1), the web-ui button's only hover change (inside @media (hover:hover)). Worked out from the palette value, not read off pixels: the product applies a filter, not a colour.",
        f"{CSSEV} hover_filters ('--__internal__filter-hover:var(--web-ui_button-filter-hover,brightness(1.1))'); captured lesson-dark-check-hover#136 filter brightness(1.1)",
        "Derived"))
    both(f"accent.{role}.pressed", lambda th, face=face, role=role: tok(
        "{palette.%s.%s}" % (th, face), "color",
        f"{role.title()} button pressed: the face keeps its colour; the lip shadow is removed and the face moves down by the lip (4px) while the JS pressed class _2cMtD is on.",
        f"{CSSEV} active_on_buttons ('._1VYyp._2cMtD:not(._2wryV){{transform:translateY(var(--__internal__lip-width))}}', '...:before{{box-shadow:none}}')",
        "Measured"))

# --- Status triples (F6) ------------------------------------------------------------------
STATUS = {
    "successBorder": ("turtle", "Success border: the correct-answer tile border (feedback.tile.correctBorder).", "dump lesson-light-match-pair-matched tile border; css ._3v-Hx"),
    "dangerBorder": ("flamingo", "Danger border: the wrong-answer tile border (feedback.tile.wrongBorder).", "css ._2noWf border (feedback.tile.wrongBorder)"),
    "infoBorder": ("blue-jay", "Info border: the selected-choice border, Duolingo's blue state edge (border.selected).", "dump lesson-light-select-selected border"),
    "infoText": ("whale", "Info text: the blue label on a selected choice card (text.selected).", "dump lesson-light-select-selected label colour"),
    "warningText": ("fox", "Warning text: the orange 'Previous mistake' label. Same value as status.warning, named for the triple.", "dump lesson-dark-previous-mistake cl=w2K8w color (dark); light inferred from the same palette name"),
    "warningBorder": ("guinea-pig", "Warning border: the lip under the orange (fox) button, the one place an orange edge is drawn.", "css ._121Sh { --web-ui_button-background-color:fox; --web-ui_button-border-color:guinea-pig }"),
}
for key, (name, desc, src) in STATUS.items():
    both(f"status.{key}", lambda th, name=name, desc=desc, src=src: tok(
        "{palette.%s.%s}" % (th, name), "color",
        desc + " Duolingo has no status component with its own border; the role is assigned from the component that draws it.", src, "Derived"))

TOK.write_text(json.dumps(t, indent=2, ensure_ascii=False) + "\n")
print("tokens.json updated")
