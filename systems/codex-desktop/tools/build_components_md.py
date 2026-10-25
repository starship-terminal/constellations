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
    ("Button", ["button-primary", "button-primary-block", "button-ghost", "button-outline-block", "button-secondary", "button-secondary-sm", "button-danger", "button-danger-text", "text-button"],
     "OpenAI's kit button (`_Button_*` with data-variant, data-color and data-size). The primary action is an ink pill: the ink colour as the fill (near-white in dark, the Catppuccin ink in light) with the surface colour as its text, as on Create project and Trust folder. Secondary buttons are soft fills of the ink at a low alpha (Change, Unarchive), ghost buttons have no fill until hover (Cancel), and the danger button is red text on a red-tinted fill (Remove project, Delete). Radii come from the control radius scale times the corner-radius scale (1.25), drawn as squircles."),
    ("Icon button", ["icon-button", "rail-button", "rail-button-selected", "composer-tool", "dictate-button", "voice-button", "send-button", "hooks-button", "header-icon-button", "header-toggle-pressed", "message-action", "message-action-user", "sidebar-toggle", "dialog-close", "tab-close"],
     "Ghost squares in the secondary text colour that take a soft ink fill under the pointer. The rail's selected destination keeps that fill. The composer's voice button is the one solid control: an ink circle that turns into the send arrow when text is typed and a stop square while the agent runs."),
    ("Link", ["link", "file-mention"],
     "Links in settings are the accent colour. In replies a file is an inline mention (a file icon and the name in the accent colour) rather than an underlined link."),
    ("Text field", ["text-field-focused", "settings-search", "settings-search-input", "search-field", "popover-search", "palette-input", "url-field", "color-field"],
     "Inputs are soft fills with no edge at rest; the focused Create project name field gains a 1px accent edge. Settings search is a pill (`radius.full`) with a search icon."),
    ("Text area", ["composer", "composer-editor", "utility-bar"],
     "The composer is a raised rounded box on the elevated fill with a hairline edge, a ProseMirror editor, and a footer of chips (add, permissions, hooks, model and effort, dictate, voice). On the new-chat page a utility bar above it holds the project and Work in chips."),
    ("Select", ["select", "theme-select", "model-button", "permissions-button", "project-chip", "work-in-chip", "option", "menu-row-checked"],
     "Settings selects are outlined triggers with a chevron that open a menu (the default file open destination lists Codex's editors and terminals: the open-in list). The composer's pickers are ghost chips; the permission chip turns the warning colour on Full access."),
    ("Checkbox", [], "Not present on the screens captured: yes or no settings are switches."),
    ("Radio", ["radio", "radio-selected", "menu-radio-row"],
     "Appearance > Mode is a radio group of three theme thumbnails (System, Light, Dark): native radio inputs inside labels, the selected one ringed in the accent. Menus use radio rows with a dot indicator (Sort chats by)."),
    ("Switch", ["switch-on", "switch-off", "switch-disabled"],
     "A 32 x 19px track: the accent colour when on, the ink at a low alpha when off, a white 13px thumb with a small shadow. The disabled switch (Default permissions) is the same control at reduced opacity."),
    ("Tabs", ["tab", "tab-selected"],
     "Plugins uses segmented tabs (Public, NUS, Personal). The right panel has browser-style tabs with a close button."),
    ("Menu", ["menu", "menu-row", "menu-row-checked", "submenu", "composer-menu", "composer-menu-row", "composer-menu-row-active", "popover", "slider", "kbd"],
     "Menus are elevated surfaces with a hairline ring and a soft shadow (`shadow.menu-box-shadow`), a 20px radius (`radius.menu`), 13px rows with a 15px row radius and a soft ink highlight. The composer's add menu is its own floating panel above the composer with Add and Plugins sections. The model picker is a popover with an effort slider."),
    ("Tooltip", ["tooltip"], "A small elevated label with a shortcut hint (Search, Command K), 13px at weight 430, with the kit's tooltip shadow."),
    ("Dialog", ["dialog", "dialog-confirm", "dialog-stacked-under", "dialog-title", "palette", "palette-row", "palette-row-selected", "palette-heading"],
     "Dialogs are elevated cards (`radius.dialog`, 15px) with no tinted scrim: a 1px backdrop blur and a deep shadow separate them. Confirmations put the title, one sentence and the buttons right-aligned (Cancel ghost, the action danger). The folder trust dialog stacks over Create project with full-width buttons. The search palette is a dialog of chats, quick actions and shortcuts."),
    ("Toast", [], "Not captured: no action raised a toast. Codex mounts Sonner (its variables are in raw/css-vars.*.json)."),
    ("Card", ["settings-card", "summary-panel", "tool-card"],
     "Settings groups are rounded cards of rows on the elevated fill with a hairline edge. The chat's Outputs panel is a floating card at the top right; the new-tab page offers tool cards (Files, Terminal, Side chat, New page)."),
    ("List row", ["new-chat-row", "project-row", "project-row-selected", "thread-row", "thread-row-selected", "settings-nav", "settings-nav-selected", "settings-row", "list-row", "section-title"],
     "Sidebar rows are 30px with a pill highlight (`radius.row` is 9999px); the selected project or chat takes the soft ink fill. Section titles (Projects, Recents) are muted. Settings rows put a label over a muted description with the control on the right."),
    ("Table", [], "Not present: lists are rows and cards. The kit has a table for markdown (`_Table_*`)."),
    ("Avatar", ["avatar"], "The profile button at the bottom of the rail shows the account's picture in a circle."),
    ("Badge", ["update-button", "context-usage"], "An accent-filled round Update available button on the rail, and the composer's context usage ring. The hooks review lists New pills in green."),
    ("Toolbar", ["thread-title", "mode-button", "header-icon-button", "header-toggle-pressed"],
     "The window header carries back and forward, the sidebar toggle, the chat title and the chat's actions; the sidebar header holds the Codex / ChatGPT mode switch, the activity bell and search."),
    ("Navigation rail", ["rail", "rail-button", "rail-button-selected"],
     "Not on the checklist: a 52px rail of destinations (Home, Space, Scheduled, Plugins, Explore, Code Review) with the update button and the profile at the bottom."),
    ("Conversation", ["user-message", "assistant-message", "worked-row", "worked-row-expanded", "tool-row", "inline-code", "file-mention", "message-action"],
     "Not on the checklist. The prompt is a right-aligned bubble on a soft fill; the reply is plain text on the page; each turn's work folds into a muted Worked for 9s row that expands to the agent's narration and tool rows (Listed files, Ran printf ...). Inline code sits on a soft fill in the mono font."),
    ("Terminal", ["terminal"], "The right panel's Terminal tab is xterm in the code font on the page colour, opened in the project folder."),
]
GAPS = [
    "Approval prompt: none appeared. The composer's permission mode is the owner's Full access, which runs commands without asking; the capture did not change it. The folder trust dialog (dark only) is the one permission prompt captured.",
    "Toast: no action raised one.",
    "Checkbox: none on the screens captured.",
    "A form validation error and a loading button were not reachable: settings apply on change, and Create project was cancelled.",
    "Codex's default theme: the owner's themes (Absolutely dark, Catppuccin light, the Garamond UI font setting) are what was captured; Codex's built-in default is recorded from the bundle under core.seed only.",
    "ChatGPT mode, Space, Images and Maps were seen only as menus or start pages; the capture stayed in Codex mode and opened none of the owner's chats, projects or cloud environments.",
    "The folder trust dialog exists in dark only: it appears once, when a folder is first added.",
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
CORE_NAMES = re.compile(r"^(token\.(main-surface-primary|side-bar-background)|bg\.(elevated-primary|accent-action)|text\.(primary|secondary|tertiary)|border\.(default|heavy|light))$")
PREFER = ["token", "bg", "text", "border", "ring", "role", "codex", "app", "alpha", "gray", "color"]


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
BY_PROP = {"background-color": ["bg.", "token.", "role."], "color": ["text.", "token.", "role.text", "role."],
           "border-top-color": ["border.", "token.", "role.border", "role."]}


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


lines = ["# Codex desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Codex 26.1013 on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "(the window is unzoomed). States: hover is a real pointer over the part, focus-visible real keyboard focus (Codex draws its own ring), "
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
