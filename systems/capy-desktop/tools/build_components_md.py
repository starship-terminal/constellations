#!/usr/bin/env python3
"""Write components.md from raw/components.<theme>.json, tokens.json and components/crops/.

    python3 tools/build_components_md.py

One entry per checklist component (docs/DESIGN-SYSTEM.md, desktop wording), listing the parts that
show it, the states captured in each theme with their crops, and the measured values written as the
token that holds them (the value after it). A value no token holds is written raw and counted.
PRODUCT (adapt): INVENTORY, GAPS, CORE_ORDER, PREFER, BY_PROP and the heading text. Standard library only, deterministic.
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
# The agent run's kept frames, read like shots under their screenshot names (see crops.py).
for _t in CAP:
    _run = PKG / "raw" / f"run.{_t}.json"
    if _run.exists():
        CAP[_t] = {**CAP[_t], **json.loads(_run.read_text())}
CROPS = {p.name for p in (PKG / "components" / "crops").glob("*.png")}
STATE_ORDER = ["default", "hover", "focus-visible", "focus", "pressed", "filled", "empty", "working", "thinking", "tool", "streaming", "done"]

# PRODUCT (adapt): checklist component -> (parts that show it, note)
INVENTORY = [
    ("Button", ["button-accent", "button-outline", "button-soft", "button-solid", "button-ghost", "button-selected", "button-inverse", "button-danger", "button-danger-text",
                "button-xs", "button-base", "button-loading", "row-button", "setup-button", "toast-button"],
     "Capy's button has seven looks, which its gallery shows on each surface it ships on (card, window, panel, overlay): ghost (text only), soft (`base.secondary`), "
     "outline (a `base.border-2` hairline), solid (`base.button`), selected (`base.secondary`, the soft look's fill, marked `data-selected`), accent (`base.primary` teal with white text) and "
     "inverse (`base.inverse`, the ink). Painted intents add a red fill (`base.destructive`) and red text for Discard and Remove key. Sizes are the control "
     "heights, xs 24, sm 28 and base 32 (`controlHeight.*`); every button has the 6px radius (`radius.button`). Loading replaces the first icon with a dot grid "
     "and lowers the opacity. Hover deepens the fill (`base.button-hover`, `base.secondary-hover`); focus-visible draws a `base.ring` outline. In the app, "
     "Settings rows use ghost and outline buttons, the setup card an outline one, and the Start button is the accent icon button."),
    ("Icon button", ["icon-button", "new-tab", "back-button", "add-button", "config-button", "voice-button", "send-button", "stop-button", "toolbar-icon-button", "tab-close"],
     "Square ghost controls on the same size tiers, the icon `base.icon-muted` until the pointer is over it. The composer's Start button is the accent fill "
     "(`base.primary`), square with the 6px radius, not round. While a run is going it becomes Stop run, the same teal square with a white stop glyph (the run's states)."),
    ("Link", ["link", "update-button"], "Links are the primary darkened with black (`base.text-link`); in markdown they are underlined. The title bar's Update is a teal text button."),
    ("Text field", ["input", "input-filled", "input-invalid", "input-disabled", "input-sm", "input-xs", "settings-search", "palette-input", "menu-search"],
     "The gallery's input in every state it ships: placeholder, filled, invalid (`aria-invalid` paints a `base.destructive` border), disabled, with icon, "
     "blank, ghost, and three sizes. A `base.input` fill with a 0.5px `base.border-2` hairline and the 6px radius; focus turns the edge to `base.ring`. The "
     "Settings search is the same control with a search icon."),
    ("Text area", ["composer", "composer-editor"],
     "The composer: a `base.popover` card with the 8px card radius and its own shadow (`shadow.composer`), a Lexical editor, and a toolbar of icon buttons "
     "(add, thread configuration, model, voice, Start). Above it sit the project, Run on and repository pickers."),
    ("Select", ["select", "model-button", "project-button", "run-on-button", "repos-button", "machine-button"],
     "Selects are menu triggers: an outline button with a chevron (Settings) or a ghost one (the composer's project, Run on and model pickers). They open menus; "
     "the selected row carries a check. Inside a thread the Machine picker under the composer names where the run is (the paired Mac, Current checkout) beside the branch."),
    ("Checkbox", ["checkbox-on", "checkbox-off", "checkbox-disabled"],
     "A 16px square with the 3px radius (`radius.sm`), `base.primary` with a white check when on, a hairline box when off, at reduced opacity when disabled. Seen only in "
     "the gallery; the app's settings use switches."),
    ("Radio", [], "Not present: single choice is a segmented control (Settings scope You and Org), a menu with a check, or the Appearance theme cards."),
    ("Switch", ["switch-on", "switch-off", "switch-disabled"],
     "28 x 16px: `base.primary` when on, `base.muted` when off, a white thumb with `shadow.plate`. Disabled lowers the opacity. Focus-visible adds the ring."),
    ("Tabs", ["tab", "tab-active", "segmented", "segmented-item", "segmented-active", "palette-tab", "palette-tab-selected"],
     "Three kinds. Desktop tabs in the title bar (224px, the 8px card radius): the active one raised on `base.popover` with a hairline and `shadow.card`, the "
     "others `base.tab-inactive-foreground` on the window, `base.tab-hover-foreground` under the pointer. Segmented tracks (Settings scope, Threads filters) "
     "where the selected item takes the soft fill. Filter tabs in the search palette."),
    ("Menu", ["menu", "menu-item", "menu-item-danger", "menu-label", "menu-separator", "menu-kbd", "menu-search"],
     "Base UI menus on `base.popover` with the 8px overlay radius and `shadow.overlay`; 28px rows (`controlHeight.menu-row`) with a `base.popover-hover` "
     "highlight, a 14px muted icon, shortcuts right-aligned, section labels in 12px `base.muted-foreground-2`. Destructive rows (Log out, Delete) are red. "
     "Pickers add a search row and sticky footer actions (New project, Manage projects)."),
    ("Context menu", ["context-menu", "context-item"],
     "Right-clicking a desktop tab or a sidebar thread opens the same menu as a context menu: tab actions with their shortcuts, and thread actions (Share, Pin, "
     "Move to, Tags, Rename, Archive A, Delete D in red)."),
    ("Tooltip", ["tooltip"], "A small raised label on `base.popover` with a `base.border-2` hairline, the 6px radius and 12px text, after a 300ms hover delay (the gallery's note), with the shortcut beside the name (Search, Command K)."),
    ("Dialog", ["confirm-dialog", "dialog", "dialog-title", "dialog-description", "scrim", "palette", "palette-row", "palette-row-selected"],
     "Dialogs sit on `base.popover` with a 12px radius (`component.confirm-dialog.radius`, the panel's radius) and `shadow.overlay`, the menus' level, over the `base.overlay` scrim. The delete confirmation (from the gallery, on "
     "fixture data) has a title, a sentence that names what is lost, a ghost Cancel and a red Delete thread. The search palette is a 720px command menu (`core.layout.palette`, 12px radius) with "
     "filter tabs, sections and a footer of keyboard hints; Customize sidebar is a plain modal."),
    ("Toast", ["toast", "toast-title", "toast-description", "toast-error"],
     "Sonner toasts restyled: constant width, an icon, a medium title and a muted description always, on `base.popover` with `shadow.overlay`, bottom right. The "
     "error toast adds an action button (the gallery's)."),
    ("Card", ["card", "card-header", "setup-card", "panel", "alert", "alert-title", "alert-description", "file-chip"],
     "Cards are `base.card` with the 8px radius; in light they have no border and are lifted by `shadow.card`, a 0.5px ring, and in dark they take a "
     "`base.border-1` hairline. Settings groups are cards of 67px rows. The content panel is the same shape at 12px (`radius.panel`). Alerts are cards with an icon, title and description."),
    ("List row", ["nav-row", "nav-row-selected", "thread-row", "section-header", "project-group", "settings-nav", "settings-nav-selected", "settings-row",
                  "row-label", "row-description", "list-row", "list-section", "setup-step", "user-button"],
     "Sidebar rows are 28px with the 6px radius: `base.muted-foreground-1` text, `base.fg` and a `base.secondary` wash when selected or hovered. Thread rows "
     "carry a title over the project key with the age right-aligned. Settings rows put a 13px medium label over a muted description, the control on the right."),
    ("Table", ["table", "table-header", "table-row", "table-cell"],
     "Grid tables (`role=table`) with 12px muted column headers, 50px rows separated by hairlines and the first column pinned when it scrolls; in the app, "
     "Members, the review bot list and Drive."),
    ("Avatar", ["avatar", "avatar-xs", "avatar-initials"], "A rounded square, never a circle (the gallery's rule), 16 or 24px; initials fall back on `base.muted`, never the accent."),
    ("Badge", ["badge", "badge-running", "badge-failed", "badge-passing", "badge-ghost", "badge-filled", "badge-count", "badge-interactive", "kbd"],
     "Pills in three looks (default soft tint, ghost, filled) across the status and hue colours, four heights (`badgeHeight.*`), a filled accent count chip, and "
     "interactive badges that take hover and focus. Shortcut hints are `kbd` chips."),
    ("Toolbar", ["tab-strip", "back-button", "new-tab", "update-button"],
     "The window's toolbar is the desktop tab strip, 40px on `base.chrome`: the macOS traffic lights at (16, 12) over its left end (drawn by macOS, see "
     "window-frame), Back and Forward, the tabs, New tab and Update."),
    ("Inspector", ["right-panel"],
     "A thread's right pane (`core.layout.inspector`, 520px), opened with Open pane in the thread's toolbar, here in the test run's own thread on Capy 0.5.0: its own tab strip "
     "(Overview, add a tab, Full screen, Close pane) over an illustration and three rows, Diffs (files, turns and the dirty count, +1 -0), Files (the root) and Shell. "
     "It takes the panel's colour behind a vertical rule, and the chat column narrows beside it."),
    ("Conversation", ["user-message", "agent-message", "message-text", "message-section", "message-footer", "chat-stamp", "activity-line", "work-group", "work-row", "tool-row",
                      "shimmer-live", "working-indicator", "code-block", "inline-code", "markdown-h1", "markdown-h2", "markdown-p", "thread-tab", "thread-cost", "token-budget"],
     "Not on the checklist. Two sources, told apart by state: `default` is the gallery's fixture transcript (Jam chat), its tool rows and markdown sections; "
     "`working`, `thinking`, `tool`, `streaming` and `done` are a real run in the app (Capy 0.5.0, Claude Haiku 5.5 through the account's Claude Code connection, "
     "on this Mac in the scratch folder). The user's message is a rounded bubble on the right (its fill is on an inner element the capture did not measure); the agent's "
     "reply sits on the page as markdown with a footer of Reply, Copy and More that shows on hover. Work collects under one activity line, Working for 3s while it runs "
     "(a shimmer over the word) and Worked for 7s after, which unfolds to rows: Thinking for 2s, then the tool as a sentence (Listing files in the working folder, "
     "Writing hello.txt +1 -0), each shimmering while live. The thread's tab carries a dot-grid Working glyph while the run lasts; the cost ($0.00) and the token "
     "budget ring sit in the toolbar and under the composer. While the thread page loads, its tab is a skeleton bar and the model chip reads Loading."),
]
GAPS = [
    "Approval prompt: none appeared in the real run. Capy ran the Claude Code connection's tools (listing the folder, writing hello.txt) without asking, and no "
    "permission setting was changed to force one; the gallery's Desktop request, Device access and Clarify sections show the request cards.",
    "A thread from the owner's history: not opened, by the capture's rules. The run's states come from three new threads in a project made for the capture.",
    "Diff review inside a thread: the inspector was opened at its Overview, not at a file's diff; the gallery's Diff section stands in.",
    "Radio: not present in the product.",
    "Disabled and loading states of app buttons were not reachable; the gallery shows disabled inputs, switches and checkboxes and loading buttons.",
    "A form validation error in the app: none reachable without saving a setting; the gallery's invalid input shows the error border.",
    "Colour themes other than the default (Absolutely, Bearded OLED, Catppuccin, Codex, Crimson Evernight, Everforest, Firecrawl, GitHub, Gruvbox, Hub, Linear, "
    "Notion, One, and a custom theme) are in the stylesheet as `[data-color-theme]` overrides and were not captured.",
    "Phone layout: Capy's web app has a touch layout under 768px (the `--responsive-*` sizes, recorded as `touch` on each core token); the desktop window was captured at 1280 x 800 only.",
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
CORE_ORDER = ["base.fg", "base.primary", "base.primary-text", "base.panel", "base.card", "base.popover", "base.bg", "base.chrome", "base.input", "base.button", "base.secondary", "base.muted", "base.border-1", "base.border-2", "base.border-3", "base.destructive", "base.overlay", "base.ring"]
PREFER = ["base", "role", "chart", "diff", "color"]


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
        v.sort(key=lambda p: (CORE_ORDER.index(".".join(p)) if ".".join(p) in CORE_ORDER else 99, PREFER.index(p[0]), len(".".join(p)), p))
    return {k: [".".join(x) for x in v] for k, v in idx.items()}


# The token group a value is looked up in first, by the property it was read from.
BY_PROP = {"background-color": ["base.", "role."], "color": ["base.", "role.text", "role."], "border-top-color": ["base.", "role.border", "role."]}


def pick(paths, prop):
    # A text colour is written as a text name (fg, *-text, *-foreground), a fill or edge as one that is not.
    textish = lambda x: any(w in x.split(".")[-1] for w in ("fg", "text", "foreground"))
    paths = [x for x in paths if textish(x) == (prop == "color")] or paths
    for pre in BY_PROP.get(prop, []):
        for x in paths:
            if x.startswith(pre):
                return x
    return paths[0]


CIDX = {t: colour_index(t) for t in SETS}
DIDX = {}
for group in ("radius", "controlHeight", "badgeHeight", "spacing", "fontSize", "lineHeight", "letterSpacing"):
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
        exact, v = "%gpx" % float(m.group(1)), "%gpx" % round(float(m.group(1)))
        group = {"border-top-left-radius": "radius", "height": "controlHeight", "padding-right": "spacing", "padding-left": "spacing",
                 "padding-top": "spacing", "font-size": "fontSize", "line-height": "lineHeight", "letter-spacing": "letterSpacing"}.get(prop)
        if v == "9999px" and prop == "border-top-left-radius":
            stats["token"] += 1
            return "`radius.full`"
        # Look the measured length up as measured (16.25px is lineHeight.sm), then rounded.
        for key in (exact, v):
            if (group, key) in DIDX:
                stats["token"] += 1
                return f"`{DIDX[(group, key)]}` {key}"
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


lines = ["# Capy desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Capy 0.4.7 on 2026-10-25), "
         "`raw/run.<theme>.json` (the agent run's kept frames, read from Capy 0.5.0 the same day), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px. "
         "Parts come from two places: the app on the owner's account, and Capy's own component gallery at /design, which ships in the bundle "
         "with fixture data (the shot names starting `design-`, and `conversation`, `tool-rows`, `delete-confirmation`, `toast`, `markdown`). "
         "States: hover is a real pointer over the part, focus-visible real keyboard focus (Capy draws its own ring), pressed `:active` forced "
         "through the DevTools protocol with the pointer over the part.", ""]
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
