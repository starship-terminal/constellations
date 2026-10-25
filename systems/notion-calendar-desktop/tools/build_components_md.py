#!/usr/bin/env python3
"""Write components.md from raw/components.<theme>.json, tokens.json and components/crops/.

    python3 tools/build_components_md.py

One entry per checklist component (docs/DESIGN-SYSTEM.md, desktop wording), listing the parts that
show it, the states captured in each theme with their crops, and the measured values written as the
token that holds them (the value after it). A value no token holds is written raw and counted.
PRODUCT (adapt): INVENTORY, NOTES and GAPS. Standard library only, deterministic.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from colour import color, is_color  # noqa: E402
from prefer import skip  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((PKG / "tokens.json").read_text())
CAP = {t: json.loads((PKG / "raw" / f"components.{t}.json").read_text()) for t in ("dark", "light")}
CROPS = {p.name for p in (PKG / "components" / "crops").glob("*.png")}
STATE_ORDER = ["default", "hover", "focus-visible", "focus", "pressed", "filled", "empty"]

# PRODUCT (adapt): checklist component -> (parts that show it, note)
INVENTORY = [
    ("Button", ["button-primary", "button-secondary", "today-button", "view-button", "button-danger", "button-danger-sm", "text-link-button", "text-link-button-sm", "panel-button"],
     "Notion's button (styled-components `sc-gfyskm-3`, the variant in the second class). Secondary is the everyday button: a faint top-to-bottom gradient (`gradient.neutral`, in `component.button-secondary.bg-gradient`, read from background-image), a 1px inset hairline (`shadow.input-border`), "
     "13px medium text, 30px tall with 12px side padding and a 6px radius; hover and pressed lay `state.hover` and `state.pressed` over it as a gradient. "
     "The primary button is the accent fill (`fill.uiBlue`) with white text and a slightly stronger inset edge (Create recurring link). Danger buttons keep the "
     "secondary shape with red text (`calendar.text-red`: Delete Notion Calendar account, Disconnect). Some actions are text links with an arrow (Edit in Notion, Configure)."),
    ("Icon button", ["nav-arrow", "sidebar-toggle", "search-button", "create-button", "context-toggle", "help-button", "add-timezone", "days-button", "panel-icon-button", "dialog-close"],
     "30px ghost squares in the secondary text colour (`text.secondary`) with an 18px icon; hover adds `state.hover` and the icon turns primary. The grid's small controls "
     "(add time zone, number of days) are the 20px and 16px sizes."),
    ("Link", ["link", "text-link-button", "text-link-button-sm"],
     "Settings links are underlined secondary text with a chevron (keyboard shortcuts ›) or an arrow (Edit in Notion ↗); no blue link appears on the captured screens."),
    ("Text field", ["text-field", "meet-with", "command-input", "search-field", "panel-title"],
     "Fields are 30px with a 6px radius and the inset hairline; the sidebar's Meet with… field is a soft grey fill. The command menu's input is 17px with no box. "
     "The event title in the popover is an inline field that looks like text until focused."),
    ("Text area", [], "Not captured as a typed state: the event description field in the editor was not typed into (typing into the new-event editor saves the event on close)."),
    ("Select", ["select", "view-button", "menu-row-checked"],
     "Selects are secondary-button-shaped triggers with a chevron (Start week on: Monday) that open a menu; the header's view switcher (Week ⌄) is the same control. "
     "The open menu ticks the chosen row."),
    ("Checkbox", ["checkbox"], "A native checkbox styled in the accent appears in General settings (Ask to change time zone to new locations); its box was not measured on its own."),
    ("Radio", ["radio", "radio-selected"], "Settings > General > Theme is a radio list (Auto, Light mode, Dark mode) of native radios filled with the accent."),
    ("Switch", ["switch-on", "switch-label"],
     "A small 24 x 14px track (7px radius) in `fill.uiBlue` when on with a 12px white thumb; hover deepens it to the 600 step of the accent. Labels sit to the right."),
    ("Tabs", [], "Not present: views switch through the Week ⌄ menu and single-letter shortcuts, and settings use a navigation list."),
    ("Menu", ["menu", "menu-row", "menu-row-checked", "menu-row-danger", "submenu", "menu-header", "colour-swatch", "command-menu", "command-row", "command-row-selected", "command-heading", "command-footer", "kbd"],
     "Menus are dark in both themes: `surface.contr-elevated` (#252525) with a hairline, a 10px radius and `shadow.elevation-middle`; 30px rows with a 6px radius, "
     "a check for the current choice, shortcut hints on the right and red for Delete. The event menu opens with a row of calendar colour swatches. "
     "The command menu (Cmd+K) is a translucent 680px panel (`surface.elevated-wax` with the 12px wax blur) of 36px rows under small group headings, with a key-hint footer."),
    ("Tooltip", ["tooltip"], "A dark 30px label (dark in both themes) with the shortcut in a key cap: Go to today T."),
    ("Dialog", ["dialog", "dialog-close", "settings-nav", "settings-nav-selected", "settings-heading", "settings-section-label", "settings-text"],
     "Settings is a 954 x 650px modal over a dim scrim (`material.dim`): a navigation list on the left (Account, Calendar accounts, Notion workspaces) and a scrolling pane, "
     "12px radius, `shadow.elevation-high`. No destructive confirmation was opened (see Gaps)."),
    ("Toast", [], "Not captured: no action raised one, and the capture took none that would."),
    ("Card", ["panel", "panel-header", "panel-section", "shortcuts-panel", "settings-card", "pane"],
     "The event popover is a floating 284px context panel: translucent (`surface.elevated-wax`), 12px radius, the high elevation, sections split by hairlines. "
     "The same panel docks to the right edge (the \\ shortcut) and also holds the keyboard shortcuts list. Settings groups rows inside 8px-radius cards; the scheduling pane is a 300px side pane."),
    ("List row", ["calendar-row", "calendar-swatch", "account-header", "scheduling-row", "scheduling-row-selected", "participant-row", "editor-row", "settings-nav"],
     "Sidebar rows are 28px with a 6px radius: a rounded colour swatch, the calendar name and, on hover, an eye to hide it. Account headers are secondary text. "
     "The selected row (Scheduling while its pane is open) takes `state.hover`."),
    ("Table", [], "Not present as a table: the calendar grid and the month view are the app's tabular layouts (below)."),
    ("Avatar", ["avatar"], "The 24px round profile picture in the header opens the profile menu; participants in the popover are 22px initials discs with an RSVP mark."),
    ("Badge", ["now-badge", "mini-day-today", "day-header-today", "kbd"],
     "Today is marked in red (`app.secondary500`): the current-time badge in the time column, today's date in the day header and the mini calendar. Key caps are 16px grey chips in SF Compact."),
    ("Toolbar", ["view-button", "today-button", "nav-arrow", "context-toggle", "month-title", "week-label"],
     "The header carries the month and year in 22px bold with the week number, and on the right the avatar, the view switcher, Today, previous and next, and the context panel toggle."),
    ("Calendar grid", ["day-header", "day-header-today", "timezone-label", "time-column", "all-day-chip", "event-chip", "event-chip-other", "event-chip-selected", "draft-chip", "month-week-row", "month-chip", "mini-calendar", "mini-day", "mini-weekday"],
     "Not on the checklist. Day columns with 48px hours, two time-zone columns (SF and SG), an all-day row and the red now line. An event chip is a 6px-radius block in its "
     "calendar's colour, mixed toward the page, with a darker ribbon on the left, an 11px medium title and a 9px time; the colours are computed per calendar in script, so "
     "they are not tokens. A selected chip turns solid with white text. The month view stacks 19px chips per day."),
]
GAPS = [
    "Event editor typed: the capture opened the new-event editor and closed it untouched. On 2026-10-25 Escape on a typed draft saved it as a real event (twice, on the owner's own calendar, with no participants); both were deleted at once and the event list checked against the baseline. The editor is shown empty only.",
    "Destructive confirmation: not opened. The destructive actions on these screens (Delete event, Delete Notion Calendar account, Disconnect, Log out) act on real data or start immediately; none was clicked.",
    "Toast: no action raised one.",
    "Form validation error, loading button and disabled controls: not reachable without editing an event or a setting.",
    "Event chip colours: computed per calendar in script from the calendar's colour, not declared as custom properties; component.event-chip holds the shape only. The screenshots show them.",
    "Scheduling links: the owner has none; the pane's empty state is captured, and neither link type was created.",
    "Sign-in and onboarding: the app was signed in; no sign-in screen showed, and the Welcome checklist was not opened.",
]


def flat(tree, prefix=()):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + (k,), v
        elif isinstance(v, dict):
            yield from flat(v, prefix + (k,))


CORE = dict(flat(TOK["core"]))
SETS = {t: dict(flat(TOK[t])) for t in ("light", "dark")}
CORE_NAMES = re.compile(r"^(surface\.(page|wash|elevated|elevated-wax|contr-elevated)|text\.(primary|secondary|tertiary|contr-primary)|stroke\.(primary|secondary)|state\.(hover|pressed)|fill\.uiBlue)$")
PREFER = ["surface", "text", "state", "stroke", "fill", "tint", "icon", "material", "role", "object", "appText", "app", "layout", "calendar", "palette", "public", "glass", "color"]


def resolve(t, v):
    while isinstance(v, str) and re.fullmatch(r"\{[^{}]+\}", v):
        p = tuple(v[1:-1].split("."))
        v = (SETS[t].get(p) or CORE[p])["$value"]
    return v


def colour_index(t):
    idx = {}
    for p, tok in SETS[t].items():
        if tok["$type"] == "color" and p[0] in PREFER:
            idx.setdefault(resolve(t, tok["$value"]), []).append(p)
    for v in idx.values():
        v.sort(key=lambda p: (not CORE_NAMES.match(".".join(p)), PREFER.index(p[0]), len(".".join(p)), p))
    return {k: [".".join(x) for x in v] for k, v in idx.items()}


# The token group a value is looked up in first, by the property it was read from.
BY_PROP = {"background-color": ["surface.", "state.", "fill.", "role."], "color": ["text.", "role.text", "role."],
           "border-top-color": ["stroke.", "role.border", "role."]}


def pick(paths, prop):
    for pre in BY_PROP.get(prop, []):
        for x in paths:
            if x.startswith(pre):
                return x
    return paths[0]


CIDX = {t: colour_index(t) for t in SETS}
DIDX = {}
for group in ("radius", "size", "spacing", "fontSize", "lineHeight", "letterSpacing"):
    for p, tok in CORE.items():
        if p[0] == group and isinstance(tok["$value"], str):
            DIDX.setdefault((group, tok["$value"]), ".".join(p))
stats = {"written": 0, "token": 0}


def as_token(t, prop, raw):
    stats["written"] += 1
    if prop in ("background-color", "color", "border-top-color") and is_color(raw):
        v = color(raw)
        if v == "rgba(0, 0, 0, 0)":
            stats["written"] -= 1
            return None
        if v in CIDX[t]:
            stats["token"] += 1
            return f"`{pick(CIDX[t][v], prop)}` {v}"
        return f"{v}"
    m = re.fullmatch(r"([\d.]+)px", raw)
    if m:
        v = "%gpx" % round(float(m.group(1)), 2)   # CSS px as computed, not rounded to whole pixels
        group = {"border-top-left-radius": "radius", "height": "size", "padding-right": "spacing", "padding-left": "spacing",
                 "padding-top": "spacing", "font-size": "fontSize", "line-height": "lineHeight", "letter-spacing": "letterSpacing"}.get(prop)
        if v == "9999px" and prop == "border-top-left-radius":
            stats["token"] += 1
            return "`radius.full`"
        if (group, v) in DIDX:
            stats["token"] += 1
            return f"`{DIDX[(group, v)]}` {v}"
        if prop == "font-weight":
            stats["written"] -= 1
            return None
        return v
    stats["written"] -= 1
    return None


PROPS = [("background-color", "fill"), ("color", "text"), ("border-top-color", "edge"), ("border-top-left-radius", "radius"),
         ("height", "height"), ("padding-left", "padding"), ("font-size", "size"), ("line-height", "line")]


def first(t, part, state):
    for shot, d in CAP[t].items():
        if d["state"] == state and part in d["parts"] and not skip(shot, part, state):
            return shot, d["parts"][part]["style"]
    return None, None


def states_of(t, part):
    return sorted({d["state"] for d in CAP[t].values() if part in d["parts"]}, key=lambda s: STATE_ORDER.index(s) if s in STATE_ORDER else 99)


def crop_links(part, state):
    out = []
    for suffix, label in (("", "dark"), ("-light", "light")):
        name = f"{part}-{state}{suffix}.png"
        if name in CROPS:
            out.append(f"[{label}](components/crops/{name})")
    return " ".join(out)


lines = ["# Notion Calendar desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Notion Calendar 1.142.0 on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "(the window is unzoomed). States: hover is a real pointer over the part, focus-visible real keyboard focus (Notion draws its own ring, a 1px accent box-shadow with a tinted halo), "
         "pressed `:active` forced through the DevTools protocol with the pointer over the part.", ""]
lines.append("| Component | Parts | Captured |")
lines.append("|---|---|---|")
for name, parts, note in INVENTORY:
    present = [p for p in parts if states_of("dark", p) or states_of("light", p)]
    lines.append(f"| [{name}](#{name.lower().replace(' ', '-')}) | {len(present)} | {'yes' if present else 'not captured'} |")
lines.append("")
seen = set()
for name, parts, note in INVENTORY:
    lines += [f"## {name}", "", note, ""]
    rows = []
    for part in dict.fromkeys(parts):
        for state in sorted(set(states_of("dark", part)) | set(states_of("light", part)), key=lambda s: STATE_ORDER.index(s) if s in STATE_ORDER else 99):
            vals = []
            for t in ("dark", "light"):
                shot, s = first(t, part, state)
                if not s:
                    continue
                cells = [f"{label} {v}" for prop, label in PROPS if not (prop == "border-top-color" and s.get("border-top-width") == "0px") and (v := as_token(t, prop, s.get(prop, "")))] if (part, state, t) not in seen else []
                seen.add((part, state, t))
                vals.append(f"{t}: " + "; ".join(cells) if cells else f"{t}: see crop")
            rows.append(f"| `{part}` | {state} | {crop_links(part, state) or 'no crop'} | {'<br>'.join(vals)} |")
    if rows:
        lines += ["| Part | State | Crops | Values |", "|---|---|---|---|"] + rows + [""]
lines += ["## Gaps", ""] + [f"- {g}" for g in GAPS] + [""]
lines.insert(4, f"{stats['token']} of {stats['written']} values written below are tokens ({round(100 * stats['token'] / max(1, stats['written']))}%); the rest no token holds and are written raw.")
lines.insert(5, "")
(PKG / "components.md").write_text("\n".join(lines))
print("components.md", len(INVENTORY), "components", stats)
