"""drive.py <theme> <step> [<step> ...]: put Raycast in one state, capture it, put it back.

Raycast's windows are summoned with its own URL scheme (`open raycast://...`, the deeplinks Raycast
documents), keystrokes go through System Events (osascript) and pointer moves through the compiled
mouse.swift (CGEvents). Every keystroke and pointer event is sent from a script that first checks,
in the same call, that Raycast is the frontmost app, so no input lands in another app. Captures go
through shot.sh, which refuses unless Raycast is frontmost.

Look, don't act: steps type harmless queries and clear them, open menus and close them with
Escape, and never press Return on a result except to open a view (a Store page, Settings, AI chat).
Before pressing Return on a result or clicking a Settings sidebar row, the step reads the target's
accessibility text through the compiled ax.swift and stops when it is not the one the step expects.
"""
import json
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
BIN = pathlib.Path.home() / ".design-systems/raycast-desktop/bin"
THEME = "dark"   # set from argv in __main__; reading argv at import made a test runner's flags the theme
ESC, RET, TAB, DEL, LEFT, RIGHT, DOWN, UP = 53, 36, 48, 51, 123, 124, 125, 126


FRONT = ('use framework "AppKit"\nuse scripting additions\n'
         'set frontName to (current application\'s NSWorkspace\'s sharedWorkspace()\'s frontmostApplication()\'s localizedName()) as text\n')


def frontmost():
    """The frontmost app as AppKit sees it. Raycast's launcher is a panel that System Events does not
    report as frontmost, so the check uses NSWorkspace."""
    r = subprocess.run(["osascript", "-e", FRONT + "return frontName"], capture_output=True, text=True)
    return r.stdout.strip()


def guarded(action):
    """Send a System Events action only while Raycast is frontmost, checked in the same script."""
    script = (FRONT + 'if frontName is not "Raycast" then error "not front"\n'
              f'tell application "System Events"\n{action}\nend tell')
    for _ in range(6):
        r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
        if r.returncode == 0:
            return
        time.sleep(0.5)
    raise SystemExit(f"Raycast is not frontmost; stopped before sending input ({frontmost()})")


def key(k, *mods, wait=0.5):
    using = (" using {" + ", ".join(m + " down" for m in mods) + "}") if mods else ""
    guarded(f"key code {k}{using}" if isinstance(k, int) else f'keystroke "{k}"{using}')
    time.sleep(wait)


def typ(text, wait=0.8):
    guarded(f'keystroke "{text}"')
    time.sleep(wait)


def clear(wait=0.4):
    key("a", "command", wait=0.1)
    key(DEL, wait=wait)


def deeplink(url, wait=1.2):
    subprocess.run(["open", url], check=True)
    time.sleep(wait)


def mouse(action, x, y, *extra, wait=0.5):
    """Global screen points. Only while Raycast is frontmost."""
    if frontmost() != "Raycast":
        raise SystemExit("Raycast is not frontmost; stopped before pointer input")
    subprocess.run([str(BIN / "mouse"), action, str(x), str(y), *map(str, extra)], check=True)
    time.sleep(wait)


def shot(name, window=None, wait=0.6):
    time.sleep(wait)
    out = subprocess.run([str(HERE / "shot.sh"), THEME, name] + ([window] if window else []), capture_output=True, text=True)
    print(out.stdout.strip() or out.stderr.strip(), flush=True)
    if out.returncode:
        raise SystemExit(f"capture {name} failed")


def ax(*args):
    """Raycast's accessibility tree as ax.swift reads it (JSON). Stops when it cannot be read."""
    r = subprocess.run([str(BIN / "ax"), *map(str, args)], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"could not read the accessibility tree ({r.stderr.strip()}); stopped before acting")
    return json.loads(r.stdout)


def first_result(items):
    """The title of the launcher's first result row: the first text after the first section header, in the
    `ax results` items. Raycast's web view exposes no selected state, so the first row is the one a fresh query
    selects; nothing moves the selection between typing and this check."""
    seen_header = False
    for kind, value in items:
        if kind == "h":
            seen_header = True
        elif seen_header:
            return value
    return None


def row_matches(read, label):
    """True when an `ax at` reading is one of Raycast's rows labelled `label`: the element under the point is in
    a Raycast window and holds `label` among at most three texts (a row's label, a Pro badge, the account name).
    A wider reading (the whole sidebar) does not count."""
    t = read.get("texts") or []
    return read.get("owner") == "Raycast" and label in t and len(t) <= 3


def expect_top_result(query, title):
    """Stop unless the launcher's search field holds `query` and its first (selected) result is `title`."""
    got = ax("results")
    top = first_result(got.get("items") or [])
    if got.get("query") != query or top != title:
        raise SystemExit(f"the launcher shows {top!r} for {got.get('query')!r}, not {title!r} for {query!r}; stopped before Return")


def expect_row(x, y, label):
    """Stop unless the row at global point (x, y) is Raycast's row labelled `label`."""
    got = ax("at", round(x), round(y))
    if not row_matches(got, label):
        raise SystemExit(f"{got.get('owner')!r} shows {got.get('texts')!r} at {x:.0f},{y:.0f}, not the {label!r} row; stopped before clicking")


def expect_at(x, y, what, ok):
    """Stop unless the element at global point (x, y) is in a Raycast window and its texts pass `ok`.
    Used before every fixed-point click, so a layout shift cannot land a click on a real setting."""
    got = ax("at", round(x), round(y))
    if got.get("owner") != "Raycast" or not ok(got.get("texts") or []):
        raise SystemExit(f"{got.get('owner')!r} shows {got.get('texts')!r} at {x:.0f},{y:.0f}, not {what}; stopped before clicking")


# The General theme select shows the theme's own name (the owner's two, as captured). "Follow System
# Appearance" is a separate checkbox beside it, so it must not pass as the select.
THEME_VALUES = {"Raycast Dark", "Raycast Light"}


def theme_select(texts):
    return bool(THEME_VALUES & set(texts))


def footer_menu_button(texts):
    """The footer's round menu button holds no text, so ax reads the footer around it: the primary action's
    name and Actions, with their key caps (components.md, the toolbar). Nothing, or anything without
    Actions (a result row, the search field), stops the click."""
    return "Actions" in texts and len(texts) <= 6


def wins():
    return subprocess.run([str(BIN / "wins"), "Raycast"], capture_output=True, text=True).stdout


STEPS = {}


def step(fn):
    STEPS[fn.__name__.replace("_", "-")] = fn
    return fn


def origin(title):
    """Top-left of Raycast's window whose title contains `title`, in global screen points."""
    for line in wins().splitlines():
        if line.rstrip().endswith(title) or ("| " + title) in line:
            f = line.split()
            return float(f[3]), float(f[4])
    raise SystemExit(f"no Raycast window titled {title}")


def at(title, x, y):
    ox, oy = origin(title)
    return ox + x, oy + y


def park():
    """Move the pointer off Raycast's windows (the right edge of the screen), so no hover shows."""
    mouse("move", 1500, 120, wait=0.3)


def launcher(wait=0.9):
    """Show the launcher at its root, empty. If it is already showing, clear it instead."""
    if "Main Window" in wins() and frontmost() == "Raycast":
        clear()
    else:
        deeplink("raycast://", wait=wait)
    if "Main Window" not in wins():
        raise SystemExit("launcher did not open")


def close_launcher():
    if "Main Window" in wins() and frontmost() == "Raycast":
        clear(wait=0.2)
        key(ESC, wait=0.3)


def query(text, wait=1.5):
    launcher()
    park()
    typ(text, wait=wait)


# ---------------------------------------------------------------- the shot list (launcher)
@step
def root():
    launcher()
    park()
    shot("00-root", "Main Window", wait=1.0)
    close_launcher()


@step
def calc():
    query("12*7+2")
    shot("01-root-calculator", "Main Window")
    close_launcher()


@step
def results():
    query("color")
    shot("02-root-results", "Main Window")
    key(DOWN, wait=0.3)
    key(DOWN, wait=0.5)
    shot("03-root-selected", "Main Window")
    x, y = at("Main Window", 400, 240)
    mouse("move", x - 5, y, wait=0.2)
    mouse("move", x, y, wait=0.8)
    shot("04-root-hover", "Main Window")
    park()
    close_launcher()


@step
def commands():
    query("raycast")
    shot("05-root-commands", "Main Window")
    close_launcher()


@step
def actions():
    query("color")
    key("k", "command", wait=1.0)
    shot("06-actions-menu", "Main Window")
    typ("show", wait=0.8)
    shot("07-actions-menu-typed", "Main Window")
    key(ESC, wait=0.4)
    close_launcher()


@step
def appmenu():
    launcher()
    x, y = at("Main Window", 25, 448)
    expect_at(x, y, "the launcher's footer menu button", footer_menu_button)
    mouse("click", x, y, wait=1.0)
    park()
    shot("08-app-menu", "Main Window")
    key(ESC, wait=0.4)
    close_launcher()


@step
def empty():
    query("qqzzxv", wait=2.5)
    shot("09-root-no-results", "Main Window")
    close_launcher()


@step
def loading():
    launcher()
    park()
    typ("project", wait=0.05)
    shot("10-root-loading", "Main Window", wait=0.0)
    time.sleep(1.0)
    close_launcher()


@step
def emoji():
    query("emoji")
    expect_top_result("emoji", "Search Emoji & Symbols")
    key(RET, wait=2.0)
    park()
    shot("11-emoji-grid", "Main Window")
    typ("heart", wait=1.5)
    shot("12-emoji-grid-typed", "Main Window")
    key(ESC, wait=0.4)
    key(ESC, wait=0.4)
    close_launcher()


# ---------------------------------------------------------------- the shot list (settings)
def settings_open():
    if "Settings" not in wins():
        launcher()
        key(",", "command", wait=2.0)
    elif frontmost() != "Raycast":
        launcher()
        key(",", "command", wait=2.0)
    if "Settings" not in wins():
        raise SystemExit("Settings did not open")


def side(scroll, y, label):
    """Click the sidebar row labelled `label`: scroll the sidebar (lines, negative is down) from the top, then
    click at y pt once the row there reads `label`."""
    settings_open()
    sx, sy = at("Settings", 120, 500)      # a point inside the sidebar, wherever the window sits
    mouse("scroll", sx, sy, 80, wait=0.6)
    if scroll:
        mouse("scroll", sx, sy, scroll, wait=0.8)
    x, yy = at("Settings", 77, y)
    expect_row(x, yy, label)
    mouse("click", x, yy, wait=1.5)
    park()


@step
def settings():
    side(0, 176, "General")
    shot("20-settings-general", "Settings")
    x, y = at("Settings", 200, 296)
    mouse("move", x, y, wait=0.2)
    mouse("move", x + 3, y, wait=0.8)
    shot("21-settings-sidebar-hover", "Settings")
    park()


# step: (sidebar scroll, row y in the window, the row's label as Raycast's accessibility tree reads it, shot)
SETTINGS = {
    "settings-launcher": (0, 210, "Launcher", "22-settings-launcher"),
    "settings-shortcuts": (0, 244, "Shortcuts", "23-settings-shortcuts"),
    "settings-keyboard": (0, 278, "Keyboard", "24-settings-keyboard"),
    "settings-advanced": (0, 346, "Advanced", "25-settings-advanced"),
    "settings-about": (0, 414, "About", "26-settings-about"),
    "settings-ai": (0, 462, "AI", "27-settings-ai"),
    "settings-account": (0, 120, "Account", "28-settings-account"),
    "settings-raycast": (-15, 405, "Raycast", "29-settings-extension-raycast"),
}


def _settings_pane(name):
    sc, y, label, out = SETTINGS[name]
    def fn():
        side(sc, y, label)
        shot(out, "Settings")
    fn.__name__ = name.replace("-", "_")
    return fn


for _n in SETTINGS:
    step(_settings_pane(_n))


@step
def settings_search():
    settings_open()
    x, y = at("Settings", 130, 68)
    expect_at(x, y, "the Settings search field", lambda t: any("Search" in v for v in t))
    mouse("click", x, y, wait=0.6)
    park()
    shot("30-settings-search-focused", "Settings")
    typ("theme", wait=1.2)
    shot("31-settings-search-typed", "Settings")
    clear()
    key(ESC, wait=0.4)


@step
def settings_theme_menu():
    side(0, 176, "General")
    x, y = at("Settings", 700, 315)
    # The theme select shows its value; anything else here (a checkbox after a layout shift) would be
    # a real setting, so the click stops instead.
    expect_at(x, y, "the General theme select", theme_select)
    mouse("click", x, y, wait=1.0)
    park()
    shot("32-settings-select-open", "Settings")
    key(ESC, wait=0.6)


if __name__ == "__main__":
    THEME = sys.argv[1] if len(sys.argv) > 1 else "dark"
    for name in sys.argv[2:]:
        STEPS[name]()
