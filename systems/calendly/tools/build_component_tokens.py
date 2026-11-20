#!/usr/bin/env python3
"""Write raw/component-tokens.json, the token spec build_tokens.py reads.

calendly.com is two products signed out. The marketing site (Astro + Tailwind)
declares a real design-token layer — the --color-* / --text-ui-* / --radius-ui-*
/ --spacing-* / --font-* / --ease-* custom properties harvested into
raw/css-vars.json (tools/capture/vars.mjs) — and paints it light with .dark
islands (the hero card, the footer card, dark sections). Those become
{"var": ...} leaves resolved per theme.

The public booking surface (/calendly-demo/*) is a separate application bundle
that declares a second token system — the camelCase --coreColor* / --primary-color*
/ --fontFamily* / --fontSize* / --text-color* "booking-kit" layer plus the same
--color-* names. A leaf may carry "resolve": "bookingLight" so build_tokens.py
looks the variable up on the booking surface instead of the theme it sits in.
The booking blues that paint the calendar (#006bff selected day and time-slot
border, #004eba link ink, #f4f8ff enabled-day fill) are compiled into atomic
classes, never declared as variables, so they are **measured** leaves from
raw/components-computed.json:

  ink          #0a2540 Proxima Nova body ink on the booking pages
  blues        #006bff painted fill/border, #004eba text/link blue,
               #f4f8ff enabled-day wash, #d4e0ed card hairline,
               #a6bbd1 month-nav grey-blue
  marketing    #071a31 midnight ink and dark CTA fill on the #fcfbf8
               magnolia field; #6bb1ff cornflower focus rings
  type         the declared --text-ui ramp (huge 72 -> overline 12) at 1.1-1.4
               leading; booking runs 14px/21px body, 16px/700 time slots
  shape        --radius-ui 4-48px scale; buttons paint 16-20px, the login
               and signup cards 48px, plan cards 40px, days full circles
  states       2px solid #6bb1ff keyboard-focus outlines; the booking
               surface's own --primary-color ladder declared as vars

A leaf is {"var": "--name"} (resolved per theme by build_tokens.py, or on the
surface named by "resolve"), {"var": "--name", "resolve": "bookingLight"} for a
booking-declared variable, or {"value": ..., "source": "..."} for a measured
value. The site paints two themes: the light marketing surface and the .dark
islands inside it; the booking roles hang off the light set because the booking
surface paints light.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
V = json.loads((RAW / "css-vars.json").read_text())
RES = V.get("resolved", {})
RL = RES.get("light", {})
RB = RES.get("bookingLight", {})
C = json.loads((RAW / "components-computed.json").read_text())["components"]
R = {n: v.get("value", v.get("raw")) for n, v in RL.items()}
B = {n: v.get("value", v.get("raw")) for n, v in RB.items()}


def var(name, ty="color", **kw):
    d = {"var": name, "type": ty}
    d.update(kw)
    return d


def bvar(name, ty="color", **kw):
    """A variable declared on the booking surface (resolved in the bookingLight pass)."""
    d = {"var": name, "type": ty, "resolve": "bookingLight"}
    d.update(kw)
    return d


SPEC = {"_about": (
    "The token tree build_tokens.py turns into tokens.json. calendly.com's "
    "marketing site declares a --color-*/--text-ui-*/--radius-ui-* design-token "
    "layer in its Astro stylesheets and paints it light with .dark islands; "
    "the public booking pages are a second application declaring a booking-kit "
    "token layer (--coreColor*/--primary-color*/--fontFamily* plus the same "
    "--color-* names) and painting light. Declared variables become var leaves "
    "(booking variables carry resolve: bookingLight); the painted booking blues "
    "and measured geometry are measured leaves from "
    "raw/components-computed.json."),
    "core": {}, "light": {}, "dark": {}, "component": {}}


def descend(root, parts):
    node = root
    for p in parts[:-1]:
        child = node.setdefault(p, {})
        if "var" in child or "value" in child or "$value" in child:
            node[p] = {"default": child}
            child = node[p]
        node = child
    last = parts[-1]
    cur = node.get(last)
    if isinstance(cur, dict) and cur and not ("var" in cur or "value" in cur or "$value" in cur):
        node = cur
        node.setdefault("default", None)
        last = "default"
    return node, last


def emit(root, name, leaf):
    node, last = descend(root, name[2:].split("-"))
    node[last] = leaf


def st(comp, state):
    return C[comp]["states"][state]["style"]


def ts(comp, state, prop):
    """The first text node's reading (textStyle) when the kit recorded one —
    the wrapper's own fontSize can be the container's, not the text's."""
    try:
        c = C[comp]["states"][state]
        t = c.get("textStyle") or {}
        v = t.get(prop)
        return v if v else c["style"].get(prop)
    except KeyError:
        return None


def norm_color(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3,8})", v)
    if m:
        h = m.group(1).lower()
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + h[:6]
    m = re.fullmatch(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)", v)
    if m:
        r, g, b, a = m.groups()
        if a is None or float(a) >= 1:
            return "#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b)))
        return f"rgba({int(float(r))}, {int(float(g))}, {int(float(b))}, {'%g' % float(a)})"
    return v


def have(comp, state, prop=None):
    try:
        s = st(comp, state)
        return prop is None or bool((s.get(prop) or "").strip())
    except KeyError:
        return False


def painted(comp, state):
    """First painted fill on or under the component."""
    try:
        c = C[comp]["states"][state]
    except KeyError:
        return None
    for n in c.get("paint") or []:
        if n.get("bg"):
            return n["bg"]
    for n in c.get("ancestors") or []:
        if n.get("bg"):
            return n["bg"]
    return None


def shadow_layers(spec):
    """Parse 'rgba(...) x y blur sp, ...' into DTCG shadow layers, dropping fully transparent no-ops."""
    out = []
    for m in re.finditer(
            r"(rgba?\(\s*[\d.]+,?\s*[\d.]+,?\s*[\d.]+(?:,?\s*[\d.]+)?\)|#[0-9a-fA-F]{3,8})\s+"
            r"(-?[\d.]+)px\s+(-?[\d.]+)px\s+(-?[\d.]+)px(?:\s+(-?[\d.]+)px)?", spec):
        col, x, y, bl, sp = m.groups()
        if col.startswith("rgba") and col.rstrip(")").endswith(", 0"):
            continue  # 4x rgba(0,0,0,0) 0px 0px 0px 0px placeholders Tailwind emits
        out.append({"color": norm_color(col), "offsetX": f"{x}px", "offsetY": f"{y}px",
                    "blur": f"{bl}px", "spread": f"{sp or 0}px"})
    return out


# ------------------------------------------------------------------- fonts

fam = SPEC["core"].setdefault("font", {}).setdefault("family", {})
for key, vname, desc in [
    ("sans", "--font-calendly-sans", "Calendly Sans: headings, the wordmark, nav and button labels."),
    ("body", "--font-geist", "Geist: the marketing body and form-text stack."),
    ("serif", "--font-wulkan", "Wulkan Text: the editorial serif on section headings and pull quotes."),
    ("system", "--font-system", "The plain system fallback stack."),
    ("mono", "--font-mono", "The monospace stack (declared, used on code and IDs)."),
]:
    if vname in R:
        fam[key] = var(vname, "fontFamily", description=desc)
if have("bk-timeslot", "default", "fontFamily"):
    fam["booking"] = {"value": st("bk-timeslot", "default")["fontFamily"], "type": "fontFamily",
                      "source": "computed fontFamily of bk-timeslot default (raw/components-computed.json)",
                      "description": "Proxima Nova: the booking application's stack."}

# ------------------------------------------------------- declared neutrals

neutral = SPEC["core"].setdefault("color", {}).setdefault("neutral", {})
for key, vname, desc in [
    ("midnight", "--color-midnight", "Midnight #071a31: the brand ink, dark CTA fill and .dark island field."),
    ("magnolia", "--color-magnolia", "Magnolia #fcfbf8: the warm off-white page field and text-on-dark."),
    ("white", "--color-white", "Pure white: cards, fields and the booking surface."),
    ("black", "--color-black", "Pure black (the computed body color before text vars paint)."),
    ("linen", "--color-linen", "Linen #f5f3ee: the secondary surface tint."),
    ("ash", "--color-ash", "Ash #e4e6e9: light grey fills."),
    ("silver", "--color-silver", "Silver #d8dce0: the subtle border tone."),
    ("steel", "--color-steel", "Steel #5f6d77: secondary text grey-blue."),
    ("smoke", "--color-smoke", "Smoke #f5f5f7."),
    ("gray-50", "--color-gray-50", "Tailwind gray 50."),
    ("gray-200", "--color-gray-200", "Tailwind gray 200 (field borders)."),
    ("gray-300", "--color-gray-300", "Tailwind gray 300."),
    ("gray-500", "--color-gray-500", "Tailwind gray 500."),
    ("gray-600", "--color-gray-600", "Tailwind gray 600."),
    ("gray-700", "--color-gray-700", "Tailwind gray 700."),
    ("gray-900", "--color-gray-900", "Tailwind gray 900."),
    ("slate-100", "--color-slate-100", "Tailwind slate 100."),
    ("slate-900", "--color-slate-900", "Tailwind slate 900."),
]:
    if vname in R:
        neutral[key] = var(vname, "color", description=desc)

alpha = neutral.setdefault("alpha", {})
for key, vname in [
    ("midnight-a05", "--color-midnight-a05"), ("midnight-a10", "--color-midnight-a10"),
    ("midnight-a20", "--color-midnight-a20"), ("midnight-a40", "--color-midnight-a40"),
    ("midnight-a50", "--color-midnight-a50"), ("midnight-a60", "--color-midnight-a60"),
    ("midnight-a90", "--color-midnight-a90"),
    ("magnolia-a05", "--color-magnolia-a05"), ("magnolia-a10", "--color-magnolia-a10"),
    ("magnolia-a20", "--color-magnolia-a20"), ("magnolia-a30", "--color-magnolia-a30"),
    ("magnolia-a40", "--color-magnolia-a40"), ("magnolia-a70", "--color-magnolia-a70"),
    ("magnolia-a90", "--color-magnolia-a90"),
]:
    if vname in R:
        alpha[key] = var(vname, "color",
                         description="Declared translucency of the named neutral (badge, icon-button and veil fills).")

# ------------------------------------------------------------- brand blues

brand = SPEC["core"].setdefault("color", {}).setdefault("brand", {})
for key, vname, desc in [
    ("cobalt", "--color-cobalt", "Cobalt #1e5ea7: deep brand blue."),
    ("cornflower", "--color-cornflower", "Cornflower #6bb1ff: the focus-ring and info-badge blue."),
    ("navy", "--color-navy", "Navy #0e396a: dark-island emphasis surface."),
    ("lake", "--color-lake", "Lake #4890e3: mid brand blue."),
    ("sky", "--color-sky", "Sky #c1defe: pale brand blue."),
    ("rain", "--color-rain", "Rain #edf5ff: section tint."),
    ("cloud", "--color-cloud", "Cloud #f4f9ff: section tint."),
    ("haze", "--color-haze", "Haze #f7f4fc: section tint."),
    ("lavender", "--color-lavender", "Lavender #eae3fa: section tint."),
    ("lilac", "--color-lilac", "Lilac #b89ffa."),
    ("iris", "--color-iris", "Iris #d4c2ff."),
    ("plum", "--color-plum", "Plum #4d3589: the purple accent in gradients."),
]:
    if vname in R:
        brand[key] = var(vname, "color", description=desc)
for key, vname in [
    ("cornflower-a20", "--color-cornflower-a20"), ("cornflower-a30", "--color-cornflower-a30"),
    ("cornflower-a60", "--color-cornflower-a60"), ("cornflower-a70", "--color-cornflower-a70"),
]:
    if vname in R:
        brand.setdefault("alpha", {})[key] = var(vname, "color",
                                                 description="Declared cornflower translucency (info badge on dark, highlights).")

hue = SPEC["core"].setdefault("color", {}).setdefault("hue", {})
for key, vname, desc in [
    ("jade", "--color-jade", "Jade #5ddfd7."),
    ("seafoam", "--color-seafoam", "Seafoam #baf0ec."),
    ("lime", "--color-lime", "Lime #dbee9f (the success-badge green)."),
    ("honeydew", "--color-honeydew", "Honeydew #f2f8de: section tint."),
    ("olive", "--color-olive", "Olive #556425."),
    ("avocado", "--color-avocado", "Avocado #343c17."),
    ("sunbeam", "--color-sunbeam", "Sunbeam #fcf1de: warm section tint."),
    ("peach", "--color-peach", "Peach #ffd39d."),
    ("tangerine", "--color-tangerine", "Tangerine #f8961f."),
    ("coffee", "--color-coffee", "Coffee #5d3e20."),
    ("lovely-lavender", "--color-lovely-lavender", "Lovely lavender #c6afff (booking accent name)."),
    ("beachy-blue", "--color-beachy-blue", "Beachy blue #f4f9ff (booking accent name)."),
    ("nice-navy", "--color-nice-navy", "Nice navy #114580 (the booking link/action navy)."),
]:
    if vname in R:
        hue[key] = var(vname, "color", description=desc)

ramp = SPEC["core"].setdefault("color", {}).setdefault("ramp", {})
for group, names in [
    ("blue", ["100", "150", "250", "700", "800"]),
    ("green", ["150", "200", "700"]),
    ("neutral", ["200", "300", "350", "450", "650", "700", "750"]),
    ("orange", ["025"]),
    ("red", ["100", "150", "500", "700"]),
    ("yellow", ["100", "150", "750"]),
]:
    for n in names:
        vname = f"--color-ramp-{group}-{n}"
        if vname in R:
            ramp.setdefault(group, {})[n] = var(vname, "color",
                description=f"Declared {group} ramp step {n} (badge and status fills/text).")

status = SPEC["core"].setdefault("color", {}).setdefault("status", {})
for key, vname, desc in [
    ("error", "--color-status-error", "Error #b32812."),
    ("success", "--color-success", "Success teal #07857c (declared in the booking bundle)."),
    ("error-bright", "--color-error", "Error #d93d24 (booking bundle)."),
    ("error-darker", "--color-error-darker-10", "Error darker 10% #c93119."),
    ("alert", "--color-alert", "Alert amber #f8c51f."),
    ("alert-2", "--color-alert-2", "Alert orange #f8961f."),
    ("alert-tint", "--color-alert-lighter-90", "Alert tint #fff8e1."),
]:
    if vname in R:
        status[key] = var(vname, "color", description=desc)

# ------------------------------------------------- booking declared layer
# The booking bundle resolves the same --color-* names plus its own camelCase
# system; these resolve in the bookingLight pass.

bk = SPEC["core"].setdefault("color", {}).setdefault("booking", {})
for key, vname, desc in [
    ("blue-025", "--coreColorBlue025", "Booking blue ramp 025 #f4f9ff."),
    ("blue-050", "--coreColorBlue050", "Booking blue ramp 050 #edf5ff."),
    ("blue-100", "--coreColorBlue100", "Booking blue ramp 100 #d5e8fe."),
    ("blue-150", "--coreColorBlue150", "Booking blue ramp 150 #c1defe."),
    ("blue-200", "--coreColorBlue200", "Booking blue ramp 200 #a3d0ff."),
    ("blue-250", "--coreColorBlue250", "Booking blue ramp 250 #84c1ff."),
    ("blue-300", "--coreColorBlue300", "Booking blue ramp 300 #6bb1ff."),
    ("blue-350", "--coreColorBlue350", "Booking blue ramp 350 #58a1f2."),
    ("blue-400", "--coreColorBlue400", "Booking blue ramp 400 #4890e3."),
    ("blue-450", "--coreColorBlue450", "Booking blue ramp 450 #3c84d6."),
    ("blue-500", "--coreColorBlue500", "Booking blue ramp 500 #3278c8."),
    ("blue-550", "--coreColorBlue550", "Booking blue ramp 550 #286cb9."),
    ("blue-600", "--coreColorBlue600", "Booking blue ramp 600 #1e5ea7."),
    ("blue-650", "--coreColorBlue650", "Booking blue ramp 650 #175295."),
    ("blue-700", "--coreColorBlue700", "Booking blue ramp 700 #114580."),
    ("primary", "--primary-color", "Declared booking primary #3c84d6."),
    ("primary-alt", "--primary-color-alternative", "Booking primary alternative #3278c8."),
    ("primary-darker-10", "--primary-color-darker-10", "Booking primary darker 10% #286cb9."),
    ("primary-darker-30", "--primary-color-darker-30", "Booking primary darker 30% #175295."),
    ("primary-level2", "--primary-color-level2", "Booking primary level 2 #6bb1ff."),
    ("primary-level3", "--primary-color-level3", "Booking primary level 3 #d5e8fe."),
    ("primary-level4", "--primary-color-level4", "Booking primary level 4 #edf5ff."),
    ("primary-text", "--primary-text-color", "White text on the booking primary."),
    ("text", "--text-color", "Booking text #0b0d0f."),
    ("text-level2", "--text-color-level2", "Booking muted text #545f69."),
    ("static-text", "--static-text-color", "Booking static text #0b0d0f."),
    ("text-secondary-1", "--text-color-secondary-1", "Booking secondary text #272e33."),
    ("text-secondary-2", "--text-color-secondary-2", "Booking secondary blue #286cb9."),
    ("text-secondary-3", "--text-color-secondary-3", "Booking secondary deep blue #1e5ea7."),
    ("text-secondary-4", "--text-color-secondary-4", "Booking secondary white."),
    ("grey-1", "--color-grey-1", "Booking grey 1 #545f69."),
    ("grey-2", "--color-grey-2", "Booking grey 2 #a4aeb7."),
    ("grey-3", "--color-grey-3", "Booking grey 3 #b5bdc4."),
    ("grey-4", "--color-grey-4", "Booking grey 4 #e4e6e9."),
    ("bg-grey", "--color-bg-grey-2", "Booking alt field #f8f9f9."),
    ("bg-white-veil", "--color-bg-white-l-2", "Booking white veil 70%."),
]:
    if vname in B:
        bk[key] = bvar(vname, "color", description=desc)

# The painted booking blues are compiled into atomic classes, never declared —
# measured off the live components.
for key, comp, state, prop, desc in [
    ("ink", "bk-panel", "default", "color", "The #0a2540 booking ink (not a declared var)."),
    ("blue", "bk-timeslot", "default", "borderTopColor", "The #006bff painted blue: time-slot border and selected-day fill."),
    ("blue-text", "bk-day", "default", "color", "The #004eba link/day-number blue."),
    ("day-fill", "bk-day", "default", "paint", "The #f4f8ff enabled-day wash."),
    ("hairline", "bk-event", "default", "borderTopColor", "The #d4e0ed card hairline on booking pages."),
    ("month-nav", "bk-month-nav", "default", "color", "The #a6bbd1 month-nav grey-blue."),
]:
    try:
        v = norm_color(painted(comp, state) if prop == "paint" else st(comp, state)[prop])
        if v and v != "transparent" and v != "rgba(0, 0, 0, 0)":
            bk[key] = {"value": v, "type": "color",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}
    except KeyError:
        pass

# -------------------------------------------------------------------- roles

ALIAS = "role alias over the core palette"
DECLARED = "declared --color-* role on the marketing sheet"

light = SPEC["light"]
for name, desc in [
    ("--color-text-primary", "Body and heading ink (#071a31)."),
    ("--color-text-secondary", "Secondary text (#5f6d77)."),
    ("--color-text-tertiary", "Tertiary text (#93a0aa)."),
    ("--color-surface-bg-primary", "The page field (#fcfbf8 magnolia)."),
    ("--color-surface-bg-secondary", "The alt field (#f5f3ee linen)."),
    ("--color-surface-fg-secondary-emphasis", "The raised secondary surface (#ffffff)."),
    ("--color-border-default", "Field and card borders (#c6ccd2)."),
    ("--color-border-strong", "Strong borders (#93a0aa)."),
    ("--color-border-subtle", "Subtle borders (#d8dce0)."),
    ("--color-divider", "Dividers (10% midnight)."),
    ("--color-action-primary-bg", "Primary button fill (#071a31)."),
    ("--color-action-primary-text", "Text on the primary fill (#fcfbf8)."),
    ("--color-action-secondary-border", "Secondary-button outline (#071a31)."),
    ("--color-action-focus-border", "Focus ring (#6bb1ff cornflower)."),
    ("--color-iconbutton-bg", "Icon-button rest fill."),
    ("--color-iconbutton-bg-hover", "Icon-button hover fill."),
    ("--color-iconbutton-bg-pressed", "Icon-button pressed fill."),
    ("--color-iconbutton-border", "Icon-button border."),
    ("--color-iconbutton-text", "Icon-button glyph."),
    ("--color-badge-error-bg", "Error badge fill."),
    ("--color-badge-error-bg-hover", "Error badge hover fill."),
    ("--color-badge-error-text", "Error badge text."),
    ("--color-badge-info-bg", "Info badge fill."),
    ("--color-badge-neutral-bg", "Neutral badge fill."),
    ("--color-badge-neutral-bg-hover", "Neutral badge hover fill."),
    ("--color-badge-neutral-text", "Neutral badge text."),
    ("--color-badge-success-bg", "Success badge fill."),
    ("--color-badge-success-bg-hover", "Success badge hover fill."),
    ("--color-badge-success-text", "Success badge text."),
    ("--color-badge-warning-bg", "Warning badge fill."),
    ("--color-badge-warning-bg-hover", "Warning badge hover fill."),
    ("--color-badge-warning-text", "Warning badge text."),
]:
    if name in R:
        emit(light, name, {"var": name, "type": "color",
                           "source": DECLARED, "description": desc})
# tinted surfaces the sheet declares (page sections)
for name, desc in [
    ("--color-surface-bg-cloud", "Cloud-tinted section field."),
    ("--color-surface-bg-honeydew", "Honeydew-tinted section field."),
    ("--color-surface-bg-rain", "Rain-tinted section field."),
]:
    if name in R:
        emit(light, name, {"var": name, "type": "color",
                           "source": DECLARED, "description": desc})
# aliases onto named hues
emit(light, "--text-on-dark", {"value": "{color.neutral.magnolia}", "type": "color",
                               "source": ALIAS, "description": "Text on midnight fills (the .dark islands)."})
emit(light, "--action-link", {"value": "{color.brand.cobalt}", "type": "color",
                              "source": ALIAS, "description": "Inline link blue (#1e5ea7)."})

# booking roles paint light — they hang off the light set
bkg = light.setdefault("booking", {})
for key, ref, desc in [
    ("text-primary", "{color.booking.ink}", "The booking body ink (#0a2540)."),
    ("text-link", "{color.booking.blue-text}", "Booking link / day-number blue (#004eba)."),
    ("action-primary", "{color.booking.blue}", "The painted booking blue (#006bff): selected day, slot border, confirm button."),
    ("action-primary-text", "{color.booking.primary-text}", "White on the booking blue."),
    ("surface-page", "{color.neutral.white}", "The booking field (white)."),
    ("surface-alt", "{color.booking.bg-grey}", "The booking alt field (#f8f9f9)."),
    ("surface-day", "{color.booking.day-fill}", "The enabled-day wash (#f4f8ff)."),
    ("border-card", "{color.booking.hairline}", "Booking card hairline (#d4e0ed)."),
    ("action-muted", "{color.booking.month-nav}", "The month-nav grey-blue (#a6bbd1)."),
    ("focus-ring", "{color.brand.cornflower}", "Booking focus ring (cornflower)."),
]:
    bkg[key] = {"value": ref, "type": "color", "source": ALIAS, "description": desc}
if "--modal-scrim-backdrop" in B:
    bkg["surface-scrim"] = bvar("--modal-scrim-backdrop", "color",
                                description="The booking modal scrim (50% dark).")

dark = SPEC["dark"]
for name, desc in [
    ("--color-text-primary", "Text on .dark islands (#fcfbf8)."),
    ("--color-text-secondary", "Secondary text on dark (#fcfbf8 — same as primary here)."),
    ("--color-text-tertiary", "Tertiary text on dark (unchanged: #93a0aa)."),
    ("--color-surface-bg-primary", "The .dark island field (#071a31 midnight)."),
    ("--color-surface-bg-secondary", "The .dark secondary field (#0c2d54)."),
    ("--color-surface-fg-secondary-emphasis", "The .dark raised secondary surface (#0e396a navy)."),
    ("--color-border-default", "Field and card borders (unchanged on dark)."),
    ("--color-border-strong", "Strong borders (unchanged on dark)."),
    ("--color-border-subtle", "Subtle borders (unchanged on dark)."),
    ("--color-divider", "Dividers (unchanged on dark)."),
    ("--color-action-primary-bg", "Primary fill inverted on dark (#fcfbf8)."),
    ("--color-action-primary-text", "Text on the inverted fill (#071a31)."),
    ("--color-action-secondary-border", "Secondary-button outline on dark (#fcfbf8)."),
    ("--color-action-focus-border", "Focus ring (cornflower)."),
    ("--color-iconbutton-bg", "Icon-button rest fill on dark."),
    ("--color-iconbutton-bg-hover", "Icon-button hover fill on dark."),
    ("--color-iconbutton-bg-pressed", "Icon-button pressed fill on dark."),
    ("--color-iconbutton-border", "Icon-button border on dark."),
    ("--color-iconbutton-text", "Icon-button glyph on dark."),
    ("--color-badge-error-bg", "Error badge fill."),
    ("--color-badge-error-bg-hover", "Error badge hover fill."),
    ("--color-badge-error-text", "Error badge text."),
    ("--color-badge-info-bg", "Info badge fill on dark (60% cornflower)."),
    ("--color-badge-neutral-bg", "Neutral badge fill on dark (20% magnolia)."),
    ("--color-badge-neutral-bg-hover", "Neutral badge hover fill on dark."),
    ("--color-badge-neutral-text", "Neutral badge text on dark."),
    ("--color-badge-success-bg", "Success badge fill."),
    ("--color-badge-success-bg-hover", "Success badge hover fill."),
    ("--color-badge-success-text", "Success badge text."),
    ("--color-badge-warning-bg", "Warning badge fill."),
    ("--color-badge-warning-bg-hover", "Warning badge hover fill."),
    ("--color-badge-warning-text", "Warning badge text."),
    ("--color-surface-bg-cloud", "Cloud-tinted section field (unchanged on dark)."),
    ("--color-surface-bg-honeydew", "Honeydew-tinted section field (unchanged on dark)."),
    ("--color-surface-bg-rain", "Rain-tinted section field (unchanged on dark)."),
]:
    if name in V["resolved"]["dark"]:
        emit(dark, name, {"var": name, "type": "color",
                          "source": "declared --color-* role re-bound on the marketing sheet's .dark scope",
                          "description": desc})

# ------------------------------------------------------------- type scale

size = SPEC["core"].setdefault("font", {}).setdefault("size", {})
for name in ["huge", "h1", "h2", "h3", "h4", "h5", "h6",
             "body-xl", "body-lg", "body-md", "body-sm", "body-xs",
             "caption", "overline"]:
    vname = f"--text-ui-{name}"
    if vname in R:
        size[name] = var(vname, "dimension",
                         description=f"Declared --text-ui-{name} step of the marketing type ramp.")
# measured steps the declared ramp doesn't cover / the booking surface
for key, comp, state, desc in [
    ("booking-body", "bk-panel", "default", "The booking body size (14px)."),
    ("booking-slot", "bk-timeslot", "default", "The time-slot label size (16px)."),
    ("mobile-hero", "m-hero", "default", "The hero size at 390px."),
]:
    v = ts(comp, state, "fontSize")
    if v:
        size[key] = {"value": v, "type": "dimension",
                     "source": f"computed fontSize of {comp} {state} (raw/components-computed.json)",
                     "description": desc}

leading = SPEC["core"].setdefault("font", {}).setdefault("lineHeight", {})
for name in ["huge", "h1", "h2", "h3", "h4", "h5", "h6",
             "body-xl", "body-lg", "body-md", "body-sm", "body-xs",
             "caption", "overline"]:
    vname = f"--leading-ui-{name}"
    if vname in R:
        leading[name] = var(vname, "number",
                            description=f"Declared --leading-ui-{name} ({R[vname]}).")
v = ts("bk-panel", "default", "lineHeight")
if v:
    leading["booking-body"] = {"value": v, "type": "dimension",
                               "source": "computed lineHeight of bk-panel default (raw/components-computed.json)",
                               "description": "The booking body leading (21px on 14px)."}

tracking = SPEC["core"].setdefault("font", {}).setdefault("tracking", {})
for name, desc in [
    ("tighter", "The -2px display tracking (hero and section heads)."),
    ("tight", "The -1px tracking."),
    ("none", "Zero tracking."),
    ("loose", "The +1px loose tracking (overlines)."),
]:
    vname = f"--tracking-ui-{name}"
    if vname in R:
        tracking[name] = var(vname, "dimension", description=desc)

weight = SPEC["core"].setdefault("font", {}).setdefault("weight", {})
for name, desc in [
    ("regular", "400 body weight."), ("medium", "500 heading/label weight."),
    ("semibold", "600."), ("bold", "700 (booking time slots, strong text)."),
]:
    vname = f"--font-weight-{name}"
    if vname in R:
        weight[name] = var(vname, "fontWeight", description=desc)

# booking's own camelCase type declarations
for key, vname, ty, desc in [
    ("booking-body", "--fontSizeBodyMedium", "dimension", "Booking declared body size (14px)."),
    ("booking-body-large", "--fontSizeBodyLarge", "dimension", "Booking declared large body (16px)."),
    ("booking-small", "--fontSizeBodySmall", "dimension", "Booking declared small text (12px)."),
    ("booking-headline-1", "--fontSizeHeadline1", "dimension", "Booking headline 1 (32px)."),
    ("booking-headline-2", "--fontSizeHeadline2", "dimension", "Booking headline 2 (28px)."),
    ("booking-headline-3", "--fontSizeHeadline3", "dimension", "Booking headline 3 (24px)."),
    ("booking-title-large", "--fontSizeTitleLarge", "dimension", "Booking title large (22px)."),
    ("booking-xsmall", "--fontSizeXSmall", "dimension", "Booking extra small (11px)."),
    ("booking-button", "--fontWeightButton", "fontWeight", "Booking button label weight (500)."),
    ("booking-lineheight", "--lineHeightBodyMedium", "number", "Booking body leading (1.4286)."),
]:
    if vname in B:
        bag = {"dimension": size, "fontWeight": weight, "number": leading}[ty]
        bag[key] = bvar(vname, ty, description=desc)

# ---------------------------------------------------------- radius, easing

radius = SPEC["core"].setdefault("radius", {})
for name in ["xxs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "full"]:
    vname = f"--radius-ui-{name}"
    if vname in R:
        radius[name] = var(vname, "dimension",
                           description=f"Declared --radius-ui-{name} ({R[vname]}).")
for name, desc in [
    ("btn-small", "Small button radius (8px)."),
    ("btn-standard", "Standard button radius (10px) — declared; marketing buttons paint larger."),
]:
    vname = f"--radius-{name}"
    if vname in R:
        radius[name] = var(vname, "dimension", description=desc)
# measured radii that diverge from the scale or are painted
for key, comp, state, prop, desc in [
    ("button-pill", "signup-google", "default", "paint-radius", "The 20px pill the Google button paints."),
    ("cta", "nav-cta", "default", "borderTopLeftRadius", "The 16px radius on the header CTA / nav buttons."),
    ("card-modal", "login-card", "default", "paint-radius", "The 48px radius the login/signup cards paint."),
    ("card-plan", "plan-card", "default", "paint-radius", "The 40px radius plan cards paint."),
    ("field", "email-field", "default", "paint-radius", "The 16px input radius."),
    ("day", "bk-day", "default", "paint-radius", "Booking day cells are full circles (50%)."),
    ("slot", "bk-timeslot", "default", "borderTopLeftRadius", "The 8px time-slot radius."),
]:
    if prop == "paint-radius":
        try:
            pr = next((n.get("radius") for n in C[comp]["states"][state].get("paint", [])
                       if n.get("radius") and n["radius"] != "0px"), None)
            # billing-radio paints 3.3e7px circles: skip a computed rounded-full (a px radius
            # above 9999px), not every radius that starts "3." (3.5px is a real radius)
            if pr and not (pr.endswith("px") and float(pr.split()[0][:-2]) > 9999):
                if pr.endswith("%"):  # a proportional radius is a number, not a dimension
                    radius[key] = {"value": float(pr[:-1]) / 100, "type": "number",
                                   "source": f"painted layer radius under {comp} {state} (raw/components-computed.json)",
                                   "description": desc}
                else:
                    radius[key] = {"value": pr, "type": "dimension",
                                   "source": f"painted layer radius under {comp} {state} (raw/components-computed.json)",
                                   "description": desc}
        except KeyError:
            pass
        continue
    if have(comp, state, prop):
        radius[key] = {"value": st(comp, state)[prop], "type": "dimension",
                       "source": f"computed {prop} of {comp} {state} (raw/components-computed.json)",
                       "description": desc}

easing = SPEC["core"].setdefault("easing", {})
for key, vname, desc in [
    ("in", "--ease-in", "Declared ease-in (.4,0,1,1)."),
    ("out", "--ease-out", "Declared ease-out (0,0,.2,1)."),
    ("in-out", "--ease-in-out", "Declared ease-in-out (.4,0,.2,1)."),
    ("default", "--default-transition-timing-function", "The default transition curve."),
]:
    if vname in R:
        easing[key] = var(vname, "cubicBezier", description=desc)

duration = SPEC["core"].setdefault("duration", {})
if "--default-transition-duration" in R:
    duration["default"] = var("--default-transition-duration", "duration",
                              description="The declared default transition duration (0.15s).")

# ------------------------------------------------------------- space, layout

spacing = SPEC["core"].setdefault("spacing", {})
for name in ["xxs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl"]:
    vname = f"--spacing-{name}"
    if vname in R:
        spacing[name] = var(vname, "dimension",
                            description=f"Declared --spacing-{name} ({R[vname]}).")
for name, desc in [
    ("section-default", "Default section padding (120px)."),
    ("section-large", "Large section padding (96px)."),
    ("section-medium", "Medium section padding (64px)."),
    ("section-small", "Small section padding (48px)."),
    ("page-padding-horizontal", "Page horizontal padding (120px)."),
    ("btn-vertical-standard", "Button vertical padding (12px)."),
    ("btn-vertical-small", "Small-button vertical padding (12px)."),
    ("btn-vertical-tertiary", "Tertiary-button vertical padding (8px)."),
    ("ui-section-y", "UI section y padding (96px)."),
]:
    vname = f"--spacing-{name}"
    if vname in R:
        spacing[name] = var(vname, "dimension", description=desc)

gap = SPEC["core"].setdefault("spacing", {}).setdefault("gap", {})
for name in ["xxs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "8xl"]:
    vname = f"--gap-{name}"
    if vname in R:
        gap[name] = var(vname, "dimension", description=f"Declared --gap-{name} ({R[vname]}).")

layout = SPEC["core"].setdefault("layout", {})
for key, vname, desc in [
    ("max-width", "--layout-max-width", "The 1920px layout cap."),
    ("header-height", "--header-height", "The 68px desktop header."),
    ("header-height-mobile", "--header-height-mobile", "The 56px compact header var (the measured mobile header is 64px)."),
    ("mobile-nav-height", "--mobile-nav-height", "The 64px mobile nav bar."),
    ("header-panel-default", "--header-panel-width-default", "Mega-menu panel width (924px)."),
    ("header-panel-product", "--header-panel-width-product", "Product menu panel width (576px)."),
    ("header-panel-resources", "--header-panel-width-resources", "Resources menu panel width (1005px)."),
    ("max-width-heading", "--max-width-heading", "The 640px heading measure."),
    ("max-width-subhead", "--max-width-subhead", "The 560px subhead measure."),
    ("section-padding-x", "--section-padding-x", "Section horizontal padding (40px)."),
    ("breakpoint-tb", "--breakpoint-ui-tb", "Tablet breakpoint (768px)."),
    ("breakpoint-sdsk", "--breakpoint-ui-sdsk", "Small-desktop breakpoint (1024px)."),
    ("breakpoint-dsk", "--breakpoint-ui-dsk", "Desktop breakpoint (1280px)."),
]:
    if vname in R:
        layout[key] = var(vname, "dimension", description=desc)

# ----------------------------------------------------------------- shadows

shadow = SPEC["core"].setdefault("shadow", {})
for key, vname, desc in [
    ("ui-sm", "--var-shadow-ui-sm", "Small UI elevation."),
    ("ui-md", "--var-shadow-ui-md", "Medium UI elevation."),
    ("ui-lg", "--var-shadow-ui-lg", "Large UI elevation (the plan cards paint this)."),
    ("ui-xl", "--var-shadow-ui-xl", "Extra-large UI elevation."),
    ("ui-2xl", "--var-shadow-ui-2xl", "2xl UI elevation."),
    ("dark-sm", "--var-shadow-ui-dark-sm", "Small elevation on dark surfaces."),
    ("dark-md", "--var-shadow-ui-dark-md", "Medium elevation on dark."),
    ("dark-lg", "--var-shadow-ui-dark-lg", "Large elevation on dark."),
    ("dark-xl", "--var-shadow-ui-dark-xl", "XL elevation on dark."),
    ("dark-2xl", "--var-shadow-ui-dark-2xl", "2xl elevation on dark."),
    ("overlay", "--overlay-shadow", "Overlay/dropdown elevation (booking bundle)."),
    ("spotlight", "--spotlight-shadow", "Spotlight card elevation (booking bundle)."),
    ("modal", "--shadowModal", "Modal elevation (booking bundle)."),
]:
    # the marketing sheet declares the --var-shadow-ui-* scale; the booking
    # bundle declares --overlay-shadow, --spotlight-shadow, --shadowModal
    src = R if vname in R else B
    srcname = "light" if vname in R else "bookingLight"
    if vname in src:
        layers = shadow_layers(src[vname])
        if layers:
            leaf = {"value": layers, "type": "shadow",
                    "source": f"css-var {vname} ({srcname})",
                    "description": desc}
            if srcname != "light":
                leaf["resolve"] = srcname
            shadow[key] = leaf
if "--card-shadow" in B:
    layers = shadow_layers(B["--card-shadow"])
    if layers:
        shadow["booking-card"] = {"value": layers, "type": "shadow",
                                  "source": "css-var --card-shadow (bookingLight)",
                                  "description": "The booking card elevation rgba(11,13,15,.1) 0 1 6."}
# the login/signup card's painted Tailwind shadow (measured; not a named var)
try:
    layers = shadow_layers(st("login-card", "default")["boxShadow"])
    if layers:
        shadow["card-auth"] = {"value": layers, "type": "shadow",
                               "source": "computed boxShadow of login-card default (raw/components-computed.json)",
                               "description": "The shadow-xl the login and signup cards paint (0 20px 25px -5px + 0 8px 10px -6px, 10% black)."}
except KeyError:
    pass

# ---------------------------------------------------------------- measured

meas = SPEC["core"].setdefault("measured", {})
# the marketing focus ring: a 2px solid cornflower outline
try:
    s = st("plan-cta", "focus-visible")
    if s.get("outlineStyle") == "solid" and s.get("outlineWidth"):
        meas["focus-ring"] = {"value": norm_color(s["outlineColor"]), "type": "color",
                              "source": "computed outline of plan-cta focus-visible (raw/components-computed.json)",
                              "description": f"The {s['outlineWidth']} solid {norm_color(s['outlineColor'])} keyboard-focus outline (offset {s.get('outlineOffset')})."}
        meas["focus-ring-width"] = {"value": s["outlineWidth"], "type": "dimension",
                                    "source": "computed outlineWidth of plan-cta focus-visible (raw/components-computed.json)",
                                    "description": "The 2px focus outline width."}
except KeyError:
    pass
# billing radio: the checked dot paints midnight inside a white circle
try:
    fill = next((n.get("bg") for n in C["billing-radio"]["states"]["default"].get("paint", [])
                 if n.get("bg") and "7, 26, 49" in n["bg"]), None)
    if fill:
        meas["radio-checked"] = {"value": norm_color(fill), "type": "color",
                                 "source": "painted checked dot under billing-radio default (raw/components-computed.json)",
                                 "description": "The midnight dot inside a checked billing radio."}
except KeyError:
    pass
# transitions worth naming
for key, comp, state, desc in [
    ("dropdown-transition", "nav-dropdown", "default", "The mega-menu open animation."),
    ("slot-transition", "bk-timeslot", "default", "The time-slot hover transition."),
    ("menu-item-transition", "m-nav-item", "default", "The mobile nav item transition."),
]:
    try:
        s = st(comp, state)
        d = (s.get("transitionDuration") or "").split(",")[0].strip()
        if d and d != "0s":
            meas[key] = {"value": d, "type": "duration",
                         "source": f"computed transition of {comp} {state} (raw/components-computed.json)",
                         "description": desc + f" ({s.get('transitionProperty')})"}
    except (KeyError, TypeError):
        pass

# ------------------------------------------------------------------ component

comp = SPEC["component"]
for key, cname, state, prop, desc in [
    ("header.height", "header", "default", "height", "The 68px marketing header."),
    ("header.height-mobile", "m-header", "default", "height", "The 64px mobile header."),
    ("logo.width", "logo", "default", "width", "The Calendly wordmark width."),
    ("button.height", "nav-cta", "default", "height", "The 48px header CTA (Get started)."),
    ("button.radius", "nav-cta", "default", "borderTopLeftRadius", "Header CTA radius (16px)."),
    ("nav-link.height", "nav-link", "default", "height", "Nav link height."),
    ("mega-menu.width", "nav-dropdown", "default", "width", "The Products mega-menu panel width."),
    ("hero-title.width", "hero-title", "default", "width", "The hero heading measure (640px)."),
    ("hero-card.height", "hero-card", "default", "height", "The hero gradient card height."),
    ("hero-card.radius", "hero-card", "default", "paint-radius", "The hero card's 48px painted radius."),
    ("button-google.height", "signup-google", "default", "height", "The 50px SSO button."),
    ("badge.height", "badge", "default", "height", "The badge chip height."),
    ("plan-card.width", "plan-card", "default", "width", "Plan card width."),
    ("plan-cta.height", "plan-cta", "default", "height", "The 50px plan CTA."),
    ("icon-button.size", "icon-button", "default", "height", "The 32px square icon button."),
    ("auth-card.width", "login-card", "default", "width", "The login card width (464px)."),
    ("auth-card.radius", "login-card", "default", "paint-radius", "The auth card's 48px radius."),
    ("signup-card.width", "signup-card", "default", "width", "The wider two-column signup card (912px)."),
    ("field.height", "email-field", "default", "height", "Auth input height (48px)."),
    ("field.radius", "email-field", "default", "paint-radius", "Auth input radius (16px)."),
    ("continue.height", "continue-btn", "default", "height", "The continue button height."),
    ("booking-panel.width", "bk-panel", "default", "width", "The booking dialog width (~1058px)."),
    ("booking-calendar.width", "bk-calendar", "default", "width", "The month grid width (~399px)."),
    ("booking-day.size", "bk-day", "default", "height", "The 44px day cell."),
    ("booking-month-nav.size", "bk-month-nav", "default", "height", "The 40px month-nav button."),
    ("booking-slot.height", "bk-timeslot", "default", "height", "The 52px time slot."),
    ("booking-slot.width", "bk-timeslot", "default", "width", "The time-slot width."),
    ("booking-event-card.width", "bk-event", "default", "width", "The booking event card width."),
    ("mobile-nav-item.height", "m-nav-item", "default", "height", "Mobile menu item height (57px)."),
]:
    if prop == "paint-radius":
        try:
            pr = next((n.get("radius") for n in C[cname]["states"][state].get("paint", [])
                       if n.get("radius") and n["radius"] != "0px"), None)
            if pr:
                node = comp
                parts = key.split(".")
                for p in parts[:-1]:
                    node = node.setdefault(p, {})
                node[parts[-1]] = {"type": "dimension", "value": pr,
                                   "source": f"painted layer radius under {cname} {state} (raw/components-computed.json)",
                                   "description": desc}
        except KeyError:
            pass
        continue
    if have(cname, state, prop):
        node = comp
        parts = key.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = {"type": "dimension", "value": st(cname, state)[prop],
                           "source": f"computed {prop} of {cname} {state} (raw/components-computed.json)",
                           "description": desc}

(RAW / "component-tokens.json").write_text(json.dumps(SPEC, indent=1, ensure_ascii=False) + "\n")


def count(d):
    if not isinstance(d, dict):
        return 1
    if "var" in d or "value" in d or "$value" in d:
        return 1
    return sum(count(v) for v in d.values())


print({k: count(v) for k, v in SPEC.items() if not k.startswith("_")})
