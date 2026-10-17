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
        "Duolingo draws no focus ring on its controls. Two live passes on 2026-10-17 pressed Tab (or an arrow key in a menu) 84 times across the learn, characters, profile, settings and sections pages, the MORE and courses menus, a lesson, its quit dialog and its report form (components/focus.md); every focused control matched :focus-visible, and none but the text fields, the courses-menu rows and the Math section-group rows (core.focusRing.listRow) changed visibly; the only outline property left is the UA outline-offset of 1px on links, with outline-style none. Text fields show focus by turning their 2px border border.focus, and menu rows by a polar fill.",
        f"{LIVE} focus[]; {CSSEV} outline_declarations ('*,:after,:before,button,button:focus,input,textarea{{outline:none}}', '._7jW2t:not(._1ZhE5){{outline:none}}'), focus_visible count 0",
        "Measured"),
    "offset": tok("0px", "dimension", "No ring, so no offset. Kept so a consumer that needs a ring knows Duolingo has none.", f"{LIVE} focus[]", "Measured"),
    # the one exception, in a chunk the /learn page does not load (pathSections)
    "listRow": {
        "width": tok("2px", "dimension",
            "The app's only ring: the section-group rows of the Math course's section picker (._3DGr8, role=button) draw a 2px solid border.focus (macaw) outline on :focus-visible. Read live by Tab in both themes.",
            "raw/2026-10/live-measurements-2.json sections-math-dark / sections-math-light; css pathSections-c1a583d8.css '._3DGr8:focus-visible{outline:2px solid rgb(var(--color-macaw));outline-offset:-2px}'",
            "Measured"),
        "offset": tok("-2px", "dimension", "Inset by its own width, so the ring is drawn inside the row.",
            "raw/2026-10/live-measurements-2.json sections-math-*: outline-offset -2px", "Measured"),
    },
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
# Every step is a colour the palette already holds (none is interpolated). For each hue: the
# palette entries in its hue window (HLS saturation >= 0.3; neutral: <= 0.05), one name per
# distinct value, the original core names kept, others added where they sit at least 4 L* from
# every kept step, ordered lightest to darkest by CIE L* of the light value. Green, yellow and
# pink stop short of 10 because the palette has no more distinct values in those hues.
RAMPS = {
    "neutral": ["snow", "polar", "swan", "koala", "hare", "gray-text", "wolf", "freetail", "eel", "orca"],
    "green": ["sea-sponge", "turtle", "mask-green", "duo-shine", "owl", "tree-frog", "kiwi-dark", "duo-radio"],
    "blue": ["iguana", "blue-jay", "bea-junior-shine", "macaw", "whale", "blue-tang", "humpback", "narwhal", "blue-space", "manta-ray"],
    "red": ["walking-fish", "flamingo", "pig", "crab", "cardinal", "fire-ant", "eddy-radio", "discoverer-progress-bar", "discoverer"],
    "orange": ["hv-light-peach", "cheetah", "traveler-progress-bar", "fox", "grizzly-lite", "guinea-pig", "lin-lucy-radio", "falstaff-secondary", "falstaff-radio"],
    "yellow": ["canary", "duck", "bee", "streak-society-light-orange", "camel"],
    "purple": ["lily-shine", "beetle", "max-ad82e6", "betta", "lily-radio", "butterfly", "super-gradient-neutral-purple", "super-gradient-bottom-halo", "max-purple", "streak-revival-background"],
    "pink": ["pearl-stat", "starfish", "explorer", "zari-secondary", "zari-radio", "rosefinch", "vikram-radio"],
}


def lstar(hex_):
    c = [int(hex_[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    y = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    return 116 * (y ** (1 / 3) if y > 0.008856 else 7.787 * y + 16 / 116) - 16


def ramp_names(th, hue):
    """Light: the list as written. Dark: the same entries sorted by their dark L*, so step 100
    is the lightest in both sets and both sets hold the same steps. Duolingo's dark theme turns
    the light tints (walking-fish, sea-sponge, canary) into its dark surfaces, so in dark those
    entries sort to the dark end of the ramp, and a few neutral names share one dark value."""
    names = RAMPS[hue]
    return names if th == "light" else sorted(names, key=lambda n: -lstar(hexof("dark", n)))


for th in ("light", "dark"):
    if "ramp" in t[th]:
        t[th]["ramp"].clear()  # keep the group's place in the set; rebuild its steps
    for hue in RAMPS:
        names = ramp_names(th, hue)
        for i, name in enumerate(names):
            step = str((i + 1) * 100)
            node = t[th].setdefault("ramp", {}).setdefault(hue, {})
            order = "their light values" if th == "light" else "their dark values (the dark set reorders the light ramp's entries; the light tints are dark surfaces in this theme, so they sit at the dark end)"
            node[step] = tok(
                "{palette.%s.%s}" % (th, name), "color",
                f"{hue} ramp step {step} of {len(names)}: palette '{name}'. Duolingo publishes no ramps; the steps are colours its palette already holds in this hue, ordered lightest to darkest by CIE L* of {order}, none interpolated.",
                "derived from core.palette (palette app-54af2130.js; light and dark checked live, raw/2026-10/rootvars-live.json)", "Derived")

# --- Strong border (F4) -------------------------------------------------------------------
both("border.strong", lambda th: tok("{palette.%s.hare}" % th, "color",
    "Strong neutral edge, one step darker than border.default. Every solid resting neutral border is swan (117 rules); hare is the only darker neutral edge, on three rules: the ghost letter avatar's 2px dashed border (._1wd57, coloured by color: hare), the hover border of the pill chip ._3ahVn (2px swan at rest, 16px radius) and the divider .uzb3k, drawn at 40% opacity. The role name is this package's; the colour and its uses are the product's.",
    f"{CSSEV} dark_neutral_borders ('._1wd57{{border-style:dashed;border-width:2px;color:rgb(var(--color-hare))}}', '._3ahVn:hover{{border-color:rgb(var(--color-hare))}}', '.uzb3k{{border-color:rgb(var(--color-hare));...;opacity:.4}}'); border_colour_use swan 117, no wolf or eel",
    "Derived"))

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
