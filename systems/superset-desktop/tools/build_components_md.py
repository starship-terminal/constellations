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
STATE_ORDER = ["default", "hover", "focus-visible", "focus", "pressed", "filled", "empty"]

# PRODUCT (adapt): checklist component -> (parts that show it, note)
INVENTORY = [
    ("Button", ["button-primary", "button-primary-sm", "button-primary-disabled", "button-outline", "button-secondary", "button-secondary-lg", "button-ghost", "button-ghost-sm", "button-destructive", "button-new-workspace", "setup-button"],
     "shadcn's button in five looks. Primary is ink: `ui.primary` (the foreground colour) with `ui.primary-foreground` text, 8px radius, 32 or 36px high; hover and pressed are the same fill at 90%. Outline and secondary sit on the page colour with a 1px `ui.border` edge and shadow-xs (32px, or 36px for `button-secondary-lg`: Sign out, the Pro dialog's Cancel); ghost is text only and takes `ui.accent` under the pointer (36px in Create a new project, 28px in the delete confirmation); destructive is the one coloured button (`ui.destructive`, white text). Disabled is the same button at opacity 0.5 (`button-primary-disabled`: Create project before the dialog has a name). Small ink buttons (`button-primary-sm`) are Create workspace, Create with AI, Save profile and Add script."),
    ("Icon button", ["icon-button", "settings-button", "plus-button", "dictate-button", "history-button", "tab-add", "tab-close", "dialog-close", "sessions-button", "send-button", "input-submit"],
     "Ghost squares (24, 26, 28 or 32px, 8px radius) in `ui.muted-foreground` that turn `ui.foreground` on a 7% wash (`ui.fill-hover`). The send button is a 22px circle on `ui.fill-selected` until there is text."),
    ("Link", ["link"], "Inline links in settings descriptions are `ui.foreground`, medium, underlined on hover, with an external-link glyph; `link.default` (blue) is declared for markdown and the terminal."),
    ("Text field", ["text-field", "text-field-mono", "settings-search", "search-field", "command-input", "palette-input"],
     "shadcn's input: 36px, 8px radius, a 1px `ui.input` edge on a transparent fill with shadow-xs; focus turns the edge `ui.ring` and adds the 3px ring. Search fields are 32px on `ui.muted` at 50% with a leading icon; paths use the monospace field."),
    ("Text area", ["composer", "composer-editor", "textarea", "input-group"],
     "The composer: `ui.card` fill, 16px radius, a 1px ring of `ui.border` drawn as a box-shadow, 14px text, chips and icon buttons in a toolbar row, and a footer row of selects outside it. The settings bio field is shadcn's textarea; the workspace's Rich input (⌘I) is an input group with a 13px radius."),
    ("Select", ["select-trigger", "select-trigger-sm", "agent-select", "model-button", "footer-chip", "title-select", "listbox", "option", "option-selected", "select-label", "select-separator", "popover", "command-item"],
     "Two triggers: the outlined settings select (36px, or 32px for the theme select; 1px `ui.input` edge, shadow-xs) and the composer's chips (22px, `ui.fill-hover`-like 4% wash, a half-pixel edge, 11px text). Lists open on `ui.popover` with a 1px edge, 10px radius and shadow-md; the selected option carries a check and `ui.accent`. Project and branch pickers are command popovers with a search row."),
    ("Checkbox", [], "Not present. Settings use switches; multi-choice lists use menus."),
    ("Radio", ["option-selected", "segment-selected", "dialog-nav-row-selected"], "Not present as radio buttons. Single choice is a select, a segmented control (List or Board) or a nav list."),
    ("Switch", ["switch-on", "switch-off"],
     "32 x 18px, `ui.primary` (ink) when on and `ui.input` when off, a page-coloured thumb, shadow-xs, the 3px ring on focus."),
    ("Tabs", ["tab", "panel-tab", "panel-tab-selected", "segmented", "segment", "segment-selected", "tabs-list", "dialog-nav-row", "dialog-nav-row-selected"],
     "Three kinds. Workspace tabs and the right panel's Files, Changes and Review are folder tabs: the selected one takes the page colour and a 1px edge open at the bottom. Segmented controls (List and Board, All and Open) are a `ui.muted` track with the selected segment on the page colour and shadow-sm. Settings > Usage uses shadcn's tabs list."),
    ("Menu", ["menu", "menu-row", "menu-separator", "menu-shortcut", "menu-sub-trigger", "context-menu", "command-menu", "command-option"],
     "shadcn's dropdown and context menus: `ui.popover`, 1px `ui.border`, 10px radius, shadow-md, 4px padding, 32px rows with a 6px radius and `ui.accent` under the pointer, separators full width, shortcuts in `ui.muted-foreground` with wide tracking, destructive rows in `ui.destructive`. The composer's plus menu is a command list."),
    ("Context menu", ["context-menu", "menu-row", "menu-sub-trigger", "menu-shortcut"], "Right-clicking a project or a workspace row opens the same menu component at the pointer, with Delete at the bottom."),
    ("Tooltip", ["tooltip"], "A small label on the page colour (`ui.background`) in `ui.muted-foreground` text, 6px radius, shadow-sm, after a hover delay; shortcut hints sit inside it."),
    ("Dialog", ["dialog", "confirm-dialog", "palette", "scrim"],
     "Dialogs sit on the page colour (`ui.background`, not the card colour) with a 1px edge, 10px radius, 24px padding and shadow-lg over a black 50% scrim. The delete confirmation is an alert dialog with the destructive button; the search palette is a 720px command dialog. The Pro upsell is a wide dialog with a nav list and artwork."),
    ("Toast", ["toast"], "Sonner toasts at the bottom right: `ui.card` fill, a 1px edge, 10px radius and Sonner's own shadow, an icon, and the message. Captured as the error toast a failed Create project raises; a success toast (Project created.) was seen once, outside the shot list."),
    ("Card", ["setup-card", "setup-badge", "plugin-row", "board-column", "empty-state"],
     "Cards are `ui.card` with a 1px `ui.border` edge and a 10px radius (the sidebar's Lifecycle scripts card, plugin rows); the Workspaces board's columns are `ui.muted` at 30% (a workspace card on the board is in workspaces.png; its reading matched the column's content area and was removed). Empty states are an icon, a line of text and one outline button, centred."),
    ("List row", ["sidebar-row", "project-row", "workspace-row", "workspace-row-selected", "settings-nav", "settings-nav-selected", "list-row", "list-row-selected", "palette-row", "palette-row-selected", "file-row", "file-row-selected", "suggestion-row"],
     "28px rows with an 8px radius in 13px medium text. At rest `ui.muted-foreground`; hover adds `ui.fill-hover` (7%) and selection `ui.fill-selected` (10%) with `ui.foreground` text (measured on the selected workspace and settings rows; the selected Workspaces row is in workspaces.png). Workspace rows carry a diff count (+1 in emerald, -0 in red) and a ⌘1 hint on hover. Palette rows are 44px with `ui.accent` on the highlighted one."),
    ("Table", ["table", "table-head", "table-row"], "shadcn's table: a 40px header in `ui.muted-foreground`, 48px rows divided by `ui.border`, no fill (Organization members, Teams)."),
    ("Avatar", ["avatar"], "16px rounded squares in the sidebar footer (the organisation's emoji) and on project rows (a letter on `ui.muted`); the account avatar in Settings is a photo circle."),
    ("Badge", ["badge", "badge-pro", "kbd", "update-pill", "palette-shortcut"],
     "Outline badges (MCP, SKILL: 16px, 4px radius, 9px uppercase), the solid PRO pill (`ui.primary`), keyboard hints (`kbd`, 20px, a 10% fill) and the sidebar's monospace update pill."),
    ("Toolbar", ["pane-header", "run-button", "run-menu", "open-in", "activity-button", "open-changes", "preset-button"],
     "The workspace's top strip: tabs on the left, then activity, changes count, Open in (a split button) and the right panel's Set Run split button; under it the agent preset bar (Claude, Codex, OpenCode, ...) and, per pane, a 28px header on `ui.muted` at 30%."),
    ("Inspector", ["panel-tab", "panel-tab-selected", "file-row", "diff-card", "diff-pane-header"], "The workspace's right panel (340px): Files, Changes and Review, with the changed files listed and a diff opening as a second pane."),
    ("Terminal", [], "Not on the checklist; the core of the product. Every agent runs as a CLI in an xterm.js terminal pane painted on a canvas with the theme's `terminal.*` palette and JetBrains Mono (`fontFamily.terminal`); no CSS holds its colours. The pane itself was not measured: the reading taken was of an .xterm Superset keeps off screen, so it gives only the font (kept as `terminal-offscreen` in raw/). See workspace-default.png and the run-*.png frames."),
]
GAPS = [
    "Checkbox and radio buttons do not exist in the captured screens (switches, selects, segmented controls and menus take their place).",
    "Loading buttons, a form validation error under a field, and the app's start-up loading state were not seen. The error states captured are the failed Create project toast and the Pull requests page's no-GitHub-remote message.",
    "Approval prompt: Superset starts Claude with --dangerously-skip-permissions, so the agent asked for no tool approvals. The only prompt was Claude Code's own folder-trust question on the first trial run, kept as run-approval in dark only.",
    "Onboarding and sign-in: the account was already signed in and set up; no onboarding screen was reachable without signing out.",
    "Automations and Tasks are Pro features; on this plan they open the Pro upsell dialog over sample data, which is what was captured.",
    "The terminal's colours and glyphs are painted on a canvas; `terminal.*` holds the palette from the theme engine. The visible terminal pane, the selected Workspaces sidebar row and a Workspaces board card were not measured (their readings hit another element and were removed after review); they show in the screenshots.",
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
CORE_NAMES = re.compile(r"^ui\.(background|foreground|card|popover|primary|primary-foreground|muted|muted-foreground|accent|border|input|ring|sidebar|fill-hover|fill-selected)$")
PREFER = ["ui", "role", "link", "palette", "terminal", "syntax"]


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
BY_PROP = {"background-color": ["ui.", "role.", "palette."], "color": ["ui.", "role.text", "link.", "role."],
           "border-top-color": ["ui.border", "ui.input", "ui.", "role.border", "role."]}


def pick(paths, prop):
    for pre in BY_PROP.get(prop, []):
        for x in paths:
            if x.startswith(pre):
                return x
    return paths[0]


CIDX = {t: colour_index(t) for t in SETS}
DIDX = {}
for group in ("radius", "controlHeight", "spacing", "fontSize", "lineHeight"):
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
    # Chromium computes rounded-full (9999px or calc(infinity)) as 1.67772e+07px, so the number may carry an exponent.
    m = re.fullmatch(r"([\d.]+(?:e[+-]?\d+)?)px", raw)
    if m:
        # Match the measured length exactly; a fractional length no token holds is written as measured.
        v = "%gpx" % round(float(m.group(1)), 2)
        group = {"border-top-left-radius": "radius", "height": "controlHeight", "padding-right": "spacing", "padding-left": "spacing",
                 "padding-top": "spacing", "font-size": "fontSize", "line-height": "lineHeight", "letter-spacing": "letterSpacing"}.get(prop)
        if float(m.group(1)) > 1e6 and prop == "border-top-left-radius":
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


lines = ["# Superset desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Superset 1.39.0 on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "(the window is not zoomed). States: hover is a real pointer over the part, focus-visible real keyboard focus, pressed `:active` "
         "forced through the DevTools protocol with the pointer over the part.", ""]
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
