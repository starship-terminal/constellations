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

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((PKG / "tokens.json").read_text())
CAP = {t: json.loads((PKG / "raw" / f"components.{t}.json").read_text()) for t in ("dark", "light")}
CROPS = {p.name for p in (PKG / "components" / "crops").glob("*.png")}
STATE_ORDER = ["default", "selected", "hover", "focus-visible", "focus", "pressed", "filled", "empty"]

# PRODUCT (adapt): checklist component -> (parts that show it, note)
INVENTORY = [
    ("Button", ["button-neutral", "button-secondary", "button-danger", "button-quiet", "send-button"],
     "28px buttons with a 6px radius and 530-weight labels. Neutral buttons (New session, Create Git repository) are muted text with an icon and no fill until hovered (`bg.button-neutral`); secondary buttons (Cancel) are `text.base`. The destructive confirmation's Delete session is a neutral button with `state.danger.fg` text and the `shadow.button-neutral` ring, not a red fill. The primary action, Send, is an ink square (`role.contrast`, `shadow.button-contrast`) that greys out while the prompt is empty. Focus is a 2px `border.focus` outline at 2.5px."),
    ("Icon button", ["icon-button", "icon-button-home", "attach-button", "more-button", "context-button", "copy-button", "icon-button-small", "tab-close", "new-tab", "project-trigger"],
     "28px squares, 6px radius, `text.faint` icons with a `bg.button-neutral` wash under the pointer (Add project, Toggle review, Session details, More options, Add images and files). The Home button is the selected one, on `overlay.pressed`. Message actions (Copy, Revert) are 24px and appear on hover; a tab's close button is 20px. The context button pairs a progress ring with the token count and cost."),
    ("Link", ["link", "file-link"], "Links are `text.accent` without an underline: Learn more in Appearance, and file names in replies (hello.txt), which open the file."),
    ("Text field", ["search-field", "settings-search", "text-field", "palette-input", "menu-search", "filter-field"],
     "Home's session search is a 36px field on a faint layer, 720px wide; Settings' search and the model menu's search are 28px fields with a leading icon. Appearance's font fields and the project name are bordered inputs on the settings group. The palette's input sits at the top of the dialog without a box."),
    ("Text area", ["composer", "prompt-field", "textarea"],
     "The composer is a 10px-radius raised card (`shadow.raised`) with the prompt (13/20), then a row of the attach button, the model and variant buttons and Send. Typing turns Send from grey to ink; while the agent works it becomes a Stop square and the placeholder reads Add follow-up. The project's worktree startup script is a plain textarea."),
    ("Select", ["select", "listbox", "option", "option-selected", "project-select", "variant-button"],
     "Settings selects are borderless 24px triggers (value and a chevron, 4px radius) that wash on hover; their listbox is a floating menu with a check on the selected option. The composer's model and variant buttons open menus rather than listboxes."),
    ("Checkbox", [], "Not present in the reachable screens; switches and checkable menu rows take its place."),
    ("Radio", ["menu-row-checked", "color-swatch"], "Not present as radio buttons. The variant menu marks its single choice with a check; the project's colour is a row of swatches with the chosen one ringed."),
    ("Switch", ["switch", "switch-on"],
     "24 x 16, a 5px radius: off is a grey track (`shadow.switch-off`), on is the accent (`bg.accent`, `shadow.switch-on`)."),
    ("Tabs", ["settings-nav", "settings-nav-selected", "pane-tab-selected", "segmented-selected", "session-tab", "session-tab-selected", "draft-tab", "terminal-tab"],
     "Three kinds. Session tabs run across the title bar (28px, 214px wide, the project's letter avatar, the title, a close button); the open one is raised on `bg.layer-01`, the draft one carries a pencil. Settings' navigation is a vertical tab list of 28px rows that wash when selected. Panes (Review, Context, Terminal 1) and Extensions' MCPs / Plugins / Skills use small pill tabs."),
    ("Menu", ["menu", "model-menu", "menu-row", "menu-row-disabled", "menu-group-label", "menu-footer", "tag-free", "suggestions", "suggestion-row", "suggestion-row-active"],
     "Floating menus (`bg.layer-01`, 6px radius, `shadow.floating`) with 28px rows at a 4px radius and a wash under the pointer; a disabled row (Clear notifications) is faint. The model menu adds a search field, provider group labels (11px, 530) and Free tags. Typing / or @ in the composer opens a suggestion list above it with the same rows."),
    ("Context menu", ["context-menu", "menu-row"], "Right-clicking a session tab opens Rename and Close tab; a project's More options menu (New session, Import session, Edit project, Reveal in Finder, Clear notifications, Close) and a session's (Rename, Export, Delete) are the same floating menu."),
    ("Tooltip", ["tooltip", "kbd", "popover"],
     "A small raised label (11px, 530, 4px radius, `shadow.floating`) with the shortcut in key caps beside the name (Home ⌘B). Hovering a session tab opens a larger popover with the project, the title and the folder path."),
    ("Dialog", ["confirm-dialog", "dialog-overlay", "palette"],
     "Dialogs sit over a black scrim (`overlay.scrim`, 60% dark, 40% light). The delete confirmation is a 480px card with a title, a sentence and right-aligned Cancel and Delete session; the command palette is a 640px dialog of commands with shortcuts and recent sessions."),
    ("Toast", [], "Not captured: no action taken during the capture raised one (copying a message would, and was not done, since it writes to the clipboard)."),
    ("Card", ["settings-list", "settings-row", "code-block", "tool-output"],
     "Settings groups rows into an 8px-radius card on `bg.layer-01` with a 0.5px inset ring of `border.muted`; rows are separated by the same hairline. In the conversation, code blocks and shell output are bordered cards on the page colour."),
    ("List row", ["project-row", "project-row-selected", "session-row", "side-link", "palette-row", "palette-row-active", "back-link", "list-row", "group-label", "section-label"],
     "Home's project rows are 28px with a 16px letter avatar: `text.muted` at rest, `text.base` on `bg.layer-03` when selected. Session rows are 40px, the title in 530 and the project name muted beside it, grouped under Today and Older. Palette rows are 36px with the active one on `overlay.pressed`."),
    ("Table", [], "Not present: lists are rows and cards (the context pane's message list is rows)."),
    ("Avatar", ["project-avatar"], "Projects are drawn as a 16px rounded square with the name's first letter (`avatar.*`, grey unless the project has a colour or icon)."),
    ("Badge", ["tag", "tag-free", "kbd", "status-dot"], "Tags are 16px, 11px text on `bg.layer-02` with a 0.5px edge (Free, Environment, API key). Shortcuts are key caps; the server's connection is a green status dot."),
    ("Toolbar", ["titlebar", "header", "session-title"], "The title bar holds Home, the session tabs and a new-tab button on `bg.deep`; the session's header is a 28px row of the project, the title (13px, 530), More options, the context button and the pane toggles."),
    ("Inspector", ["pane", "pane-tab-selected", "terminal", "terminal-tab"],
     "The review pane opens on the right with Review and Context tabs (Review: No tracked changes and Create Git repository in a folder without Git; Context: the session's provider, model, token and cost figures and its raw messages). The terminal opens beside it as its own pane."),
    ("Conversation", ["user-message", "text-part", "markdown", "inline-code", "code-block", "tool-group", "tool-trigger-open", "tool-output", "turn-meta"],
     "Not on the checklist; the core of the product. The owner's prompt is a right-aligned bubble with `text.accent` text on a faint blue; the agent's reply is plain 14/22.4 text on the page, with inline code in IBM Plex Mono. Tool calls fold into one line (Used 1 Shell, Used 1 Write) that expands to the command and its output. While the agent works the turn shows Working, and a long command offers Move to background."),
    ("Progress", ["progress-circle"], "The context button's ring fills with the share of the model's context used."),
]
GAPS = [
    "Toast: no action taken during the capture raised one.",
    "Approval prompt: none appeared. Settings > Preferences > Auto-accept permissions is off, but OpenCode's default permissions let the agent list, write and run commands inside the project folder without asking; nothing was changed to force one.",
    "Disabled was seen on a menu row and on the grey Send button of an empty composer; loading buttons, a form validation error and an error state were not reachable.",
    "Checkbox, radio buttons and tables do not exist in the reachable screens.",
    "Onboarding and sign-in: the account's providers are already connected and first-launch onboarding is complete, so neither was shown. The empty project page (Nothing here yet) is captured.",
    "Loading at app start: the startup splash was not captured (the window was already up when the capture connected).",
    "Native windows are not in the DOM: Add project and Add images and files open macOS panels, and Export opens a save panel; only the first was used, to open the scratch folder.",
    "Focus rows: list rows draw focus as a wash and a 0.5px inset ring, not the outline buttons use; some icon buttons show no ring in their focus-visible crops.",
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
# PRODUCT (adapt): the token names a measured colour is written as first
CORE_NAMES = re.compile(r"^(text|bg|border|icon)\.(base|muted|faint|inverse|contrast|accent|deep|layer-0\d|strong|focus)$")
PREFER = ["text", "bg", "border", "icon", "overlay", "state", "legacy", "syntax", "markdown", "role"]


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
BY_PROP = {"background-color": ["bg.", "overlay.", "state.", "role."], "color": ["text.", "icon.", "state.", "role.text", "role."],
           "border-top-color": ["border.", "role.border", "role."]}


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
        v = "%gpx" % round(float(m.group(1)))
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
        if d["state"] == state and part in d["parts"]:
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


lines = ["# OpenCode desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from OpenCode 2.1.4 on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "as the stylesheets declare them (the window is not zoomed). States: hover is a real pointer over the part, focus-visible real keyboard focus "
         "after a key press, pressed `:active` forced through the DevTools protocol (nothing was clicked).", ""]
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
