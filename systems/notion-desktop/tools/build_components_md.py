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
    ("Button", ["button-new", "button-share", "button-primary", "button-secondary", "button-danger", "toolbar-button"],
     "Notion has one filled button: the blue New button on a database (white text on `blue.bg-accent-primary`, a split chevron beside it). Everything else is a ghost: Share and the topbar's buttons are text or icons in the primary text colour that take a translucent fill under the pointer (`misc.button-hover-bg`). Share's Invite is blue; the delete confirmation's Delete is red text in a hairline box above a plain Cancel."),
    ("Icon button", ["topbar-icon-button", "sidebar-icon-button", "tabbar-icon-button", "new-tab", "tab-close", "ai-button", "ai-header-button", "ai-submit", "drag-handle", "toolbar-icon-button", "page-control", "dialog-close", "toggle-button"],
     "28px squares with a 6px radius in the icon colour, a translucent hover fill. The floating Notion AI button at the bottom right is the one round, raised control: a 40px circle with the outlined shadow."),
    ("Link", ["link"], "Links in pages are the body colour with a muted underline (`misc.line-decoration-color`); in settings they are the blue accent."),
    ("Text field", ["sidebar-search", "palette-input", "text-field", "settings-search", "menu-search", "ai-input"],
     "Inputs are soft translucent fills with a 6 to 8px radius and no edge at rest; focus adds Notion's blue ring (two box-shadow layers of the accent). The sidebar's Search or ask is a button styled as a field with its shortcut."),
    ("Text area", ["paragraph", "paragraph-empty", "page-title", "ai-input"],
     "The page itself is the text area: blocks are contenteditable, with a placeholder on the empty focused block (Press 'space' for AI or '/' for commands). The AI panel's input is a rounded, raised box with chips under it."),
    ("Select", ["select", "select-pill", "select-pill-green", "select-option", "menu-row-checked", "ai-chip"],
     "Settings selects are ghost triggers (the value and a chevron) that open a menu. Database select values are coloured pills with a small radius, one hue family per option (`red.bg-*`, `green.bg-*`)."),
    ("Checkbox", ["checkbox", "checkbox-box", "checkbox-checked"],
     "To-do and database checkboxes are 16px squares: an edge in the icon colour when empty, the blue accent with a white tick when checked, and the to-do's text struck through and dimmed."),
    ("Radio", [], "Not present on the screens captured: single choices are selects and menus with a check."),
    ("Switch", ["switch-on", "switch-off", "menu-switch"], "A small pill switch: the blue accent when on, a grey translucent track when off, a white round thumb."),
    ("Tabs", ["tab", "tab-selected", "tab-pinned", "view-tab", "view-tab-selected", "nav-tab", "nav-tab-selected"],
     "Three kinds: the window's tab strip (pinned icon tabs, then titled tabs up to 200px; the active tab takes the page colour), the sidebar's Home, Chat and Meetings tabs (a soft fill when selected), and a database's view tabs (a soft fill on the selected view)."),
    ("Menu", ["menu", "menu-row", "menu-row-selected", "menu-row-checked", "menu-row-danger", "menu-heading", "menu-search", "popover", "toolbar"],
     "Menus are raised panels on `misc.popover-bg` with a 10px radius, a 1px ring and a soft drop shadow (`shadow.outline-*`). Rows are 28px with an icon, label and right-aligned shortcut, a translucent hover fill and a 6px radius; sections are introduced by small muted headings; many menus open with a search field. The slash menu and the block menu are the same component."),
    ("Tooltip", ["tooltip"], "A small dark label with the shortcut in a muted colour beside the name."),
    ("Dialog", ["dialog", "button-danger", "button-secondary", "settings-dialog", "palette", "palette-row", "palette-row-selected", "peek"],
     "Confirmations are small centred cards over a dark scrim (`misc.modal-underlay-bg`) with the question, a red action and Cancel stacked full width. Settings is a large two-column window on the same scrim. The search palette and a database row's side peek are their own surfaces."),
    ("Toast", ["toast"], "A dark bar at the bottom left of the page with one line of text and an action (Copy link raised one)."),
    ("Card", ["callout", "callout-fill", "code-fill", "board-card", "database-inline"],
     "Blocks that sit on a fill: the callout (a rounded box on a translucent grey with an emoji), the code block, and board cards."),
    ("List row", ["page-row", "page-row-selected", "page-row-selected-fill", "add-row", "section-title", "section-label", "settings-nav", "settings-nav-selected", "palette-row", "chat-row"],
     "Sidebar rows are 30px with an icon, a 14px label and a 6px-radius translucent fill when selected or hovered; hover reveals the row's add and more buttons. Section labels (Favorites, Private, Teamspaces) are small and muted."),
    ("Table", ["table-header-cell", "table-cell", "table-row", "add-row", "database-inline"],
     "A database table: a header row of muted property names with type icons, 1px cell rules in the border colour, rows that take a faint hover, coloured select pills and a + New page row at the end."),
    ("Avatar", ["switcher"], "The workspace switcher shows the workspace icon and name; people appear as small round photos in the topbar and in menus."),
    ("Badge", ["select-pill", "ai-banner"], "Labels are pills: the New and Beta tags in settings, Notion's select pills, and the AI panel's out-of-responses notice."),
    ("Toolbar", ["topbar", "breadcrumb", "button-share", "topbar-icon-button", "toolbar", "toolbar-button"],
     "The page topbar is 44px: the breadcrumb on the left, Edited time, Share, link, favourite and more on the right; it fades out while typing. Selecting text raises a floating formatting toolbar."),
    ("Sidebar", ["sidebar", "sidebar-surface", "sidebar-search", "switcher", "nav-tab", "nav-tab-selected"],
     "Not on the checklist: the 270px sidebar on the secondary background, from the search field and the three tabs down to the workspace switcher."),
    ("Blocks", ["page-title", "heading-1", "heading-2", "heading-3", "paragraph", "bulleted-list", "numbered-list", "to-do", "toggle", "quote", "quote-bar", "callout", "code", "inline-code", "divider", "block-selected"],
     "Not on the checklist: the editor's blocks. A 40px bold title, three heading levels, 16px body at a 24px line, lists, a quote with a bar, the callout and code blocks on fills. A selected block takes the blue selection tint."),
    ("Notion AI", ["ai-button", "ai-panel", "ai-input", "ai-submit", "ai-chip", "ai-header-button", "ai-banner"],
     "Not on the checklist: the AI side panel docks at the right of the page, with suggestions, an input box with the model chip and submit, and a notice when the account's free responses are used up."),
]
GAPS = [
    "Notion AI responses: the account had run out of free AI responses on 2026-10-25, so Submit stayed disabled; no prompt was sent and no streaming, tool or finished response was captured. The panel, its suggestions, the typed state and the model menu were.",
    "Radio: none on the screens captured.",
    "A form validation error and a loading button: not reached. The Sidebar settings pane was caught loading (Loading sidebar presets...).",
    "Onboarding and sign-in: the account is signed in; no first-run screen appeared.",
    "People settings: left out on purpose (other people's email addresses).",
    "Calendar, timeline, gallery and chart views, comments and page history: not opened; the sample database has a table and a board.",
    "The owner's pages were seen only as the sidebar, tab titles and the search palette's preview; none was opened for editing.",
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
CORE_NAMES = re.compile(r"^(bg\.(primary|secondary|tertiary)|text\.(primary|secondary|tertiary)|border\.(primary|strong)|blue\.bg-accent-primary)$")
PREFER = ["bg", "text", "border", "icon", "role", "blue", "misc", "gray", "red", "green", "palette"]


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
BY_PROP = {"background-color": ["bg.", "misc.", "role."], "color": ["text.", "icon.", "role.text", "role."],
           "border-top-color": ["border.", "role.border", "role."]}


def pick(paths, prop):
    for pre in BY_PROP.get(prop, []):
        for x in paths:
            if x.startswith(pre):
                return x
    return paths[0]


CIDX = {t: colour_index(t) for t in SETS}
DIDX = {}
for group in ("radius", "controlHeight", "spacing", "fontSize", "lineHeight", "letterSpacing"):
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
        group = {"border-top-left-radius": "radius", "height": "controlHeight", "padding-right": "spacing", "padding-left": "spacing",
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


lines = ["# Notion desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Notion 7.40.0 on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "(the app runs at the owner's 90% zoom, so 1 CSS px is 1.8 device px). States: hover is a real pointer over the part, focus-visible real keyboard focus (Notion draws its own ring), "
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
