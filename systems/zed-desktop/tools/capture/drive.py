"""drive.py <theme> <step> [<step> ...]: put Zed in one state, capture it, put it back.

Keystrokes go through System Events (osascript), pointer moves through bin/mouse (CGEvents),
captures through bin/shot.sh, which refuses unless Zed's window is frontmost. Coordinates are
global screen points; Zed's window fills the screen below the 33 pt menu bar, so a point in a
half-size preview (1 px = 1 pt) is (x, y + 33) on screen.
"""
import pathlib
import subprocess
import sys
import time

BIN = pathlib.Path(__file__).resolve().parent
SCR = pathlib.Path.home() / ".design-systems/harness-scratch/zed"
CLI = "/Applications/Zed.app/Contents/MacOS/cli"
THEME = sys.argv[1]
Y0 = 33


def osa(script):
    subprocess.run(["osascript", "-e", script], check=True, capture_output=True)


def front():
    osa('tell application "Zed" to activate')
    time.sleep(0.5)


def guarded(action):
    """Send a System Events action only while Zed is frontmost, checked in the same script.
    Other capture sessions share this Mac, so focus can move between activate and keystroke."""
    script = ('tell application "Zed" to activate\ndelay 0.3\ntell application "System Events"\n'
              'if (name of first application process whose frontmost is true) is not "Zed" then error "not front"\n'
              f'{action}\nend tell')
    for _ in range(10):
        r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
        if r.returncode == 0:
            return
        time.sleep(1.0)
    raise SystemExit("Zed would not stay frontmost; stopped before sending input")


def key(k, *mods, wait=0.6):
    using = (" using {" + ", ".join(m + " down" for m in mods) + "}") if mods else ""
    guarded(f"key code {k}{using}" if isinstance(k, int) else f'keystroke "{k}"{using}')
    time.sleep(wait)


def typ(text, wait=0.8):
    guarded(f'keystroke "{text}"')
    time.sleep(wait)


def zed_front():
    r = subprocess.run(["osascript", "-e", 'tell application "System Events" to name of first application process whose frontmost is true'],
                       capture_output=True, text=True)
    return r.stdout.strip().lower() == "zed"


ESC, RET, TAB, DEL, LEFT, RIGHT, DOWN, UP = 53, 36, 48, 51, 123, 124, 125, 126


def ensure_front():
    """Bring Zed forward and confirm it is frontmost before any pointer event; give up after 10 tries."""
    for _ in range(10):
        front()
        if zed_front():
            return
        time.sleep(1.0)
    raise SystemExit("Zed would not stay frontmost; stopped before pointer input")


def mouse(action, x, y, *extra, wait=0.6):
    ensure_front()
    subprocess.run([str(BIN / "mouse"), action, str(x), str(y + Y0), *map(str, extra)], check=True)
    time.sleep(wait)


def shot(name, wait=0.8, window=None):
    time.sleep(wait)
    front()
    out = subprocess.run([str(BIN / "shot.sh"), THEME, name] + ([window] if window else []), capture_output=True, text=True)
    print(out.stdout.strip() or out.stderr.strip())
    if out.returncode:
        raise SystemExit(f"capture {name} failed")


def palette(command, wait=1.2):
    key("p", "command", "shift")
    typ(command, wait=0.8)
    key(RET, wait=wait)


def open_file(name, wait=1.5):
    subprocess.run([CLI, "-a", str(SCR / name)], check=True)
    time.sleep(wait)


def park():
    """Move the pointer to a neutral spot (the empty file tree) so no hover shows."""
    mouse("move", 120, 600, wait=0.3)


def TODO_Y():
    """todo.txt's row in the file tree: the third row, or the fourth once the agent wrote hello.txt."""
    return 126 if (SCR / "hello.txt").exists() else 100


STEPS = {}


def step(fn):
    STEPS[fn.__name__.replace("_", "-")] = fn
    return fn


# ---------------------------------------------------------------- steps
# STEPS-BELOW
@step
def editor():
    open_file("inventory.py")
    park()
    shot("01-editor-python")


@step
def tabs():
    open_file("NOTES.md")
    park()
    shot("02-editor-markdown-tabs")


@step
def finder():
    open_file("inventory.py")
    key("p", "command")
    shot("03-file-finder")
    typ("no")
    shot("04-file-finder-typed")
    key(ESC)


@step
def palette_open():
    key("p", "command", "shift")
    shot("05-command-palette")
    typ("toggle")
    shot("06-command-palette-typed")
    key(DOWN)
    key(DOWN)
    shot("07-command-palette-selected")
    key(ESC)


@step
def hover_diag():
    open_file("inventory.py")
    mouse("move", 400, 511, wait=0.3)
    mouse("move", 419, 511, wait=2.0)
    shot("08-hover-diagnostic")
    park()


@step
def diagnostics():
    key("m", "command", "shift", wait=1.5)
    park()
    shot("09-diagnostics-panel")
    key("w", "command")


@step
def undo():
    open_file("inventory.py")
    key(ESC)
    key("z", "command")
    park()
    shot("zz-check")


@step
def buffer_search():
    open_file("inventory.py")
    key(ESC)
    palette("buffer search: deploy")
    typ("count")
    park()
    shot("10-buffer-search")
    key(ESC)


@step
def completions():
    open_file("inventory.py")
    key(ESC)
    key(UP, "command")
    typ("count", wait=2.0)
    park()
    shot("12-completions-menu")
    key(ESC)
    key("z", "command")


@step
def project_search():
    key("f", "command", "shift")
    typ("item")
    key(RET, wait=1.5)
    park()
    shot("11-project-search")
    key("w", "command")


@step
def terminal():
    open_file("inventory.py")
    palette("terminal panel: toggle", wait=2.5)
    park()
    shot("13-terminal-panel")
    palette("terminal panel: toggle")


@step
def git_panel():
    open_file("inventory.py")
    palette("git panel: toggle focus", wait=1.5)
    park()
    shot("14-git-panel")


@step
def project_diff():
    palette("git: diff", wait=2.0)
    park()
    shot("15-project-diff")
    key("w", "command")
    palette("git panel: toggle focus")
    palette("git panel: toggle")


@step
def ctx_file():
    open_file("inventory.py")
    mouse("rclick", 60, TODO_Y(), wait=1.0)
    shot("16-context-menu-file")
    key(ESC)


@step
def ctx_editor():
    open_file("inventory.py")
    mouse("rclick", 520, 300, wait=1.0)
    shot("17-context-menu-editor")
    key(ESC)


@step
def ctx_tab():
    mouse("rclick", 470, 50, wait=1.0)
    shot("18-context-menu-tab")
    key(ESC)


@step
def reset():
    key(ESC)
    palette("workspace: close all docks")
    palette("project panel: toggle focus")
    open_file("inventory.py")
    park()
    shot("zz-check")


@step
def delete_confirm():
    open_file("inventory.py")
    mouse("rclick", 60, TODO_Y(), wait=1.0)   # todo.txt
    mouse("click", 100, 586 + TODO_Y() - 100, wait=1.5)  # Trash (recoverable); the confirmation is captured, then cancelled
    shot("19-delete-confirm")
    key(ESC, wait=1.0)   # Cancel
    assert (SCR / "todo.txt").exists(), "todo.txt went missing"


@step
def tooltip():
    open_file("inventory.py")
    mouse("move", 1330, 933, wait=0.2)
    mouse("move", 1332, 933, wait=2.0)
    shot("20-tooltip")
    park()


@step
def hover_tab():
    mouse("move", 1440, 50, wait=1.5)
    shot("21-hover-icon-button")
    mouse("move", 1395, 17, wait=1.0)
    shot("22-hover-button")
    mouse("move", 530, 50, wait=1.0)
    shot("23-hover-tab")
    park()


@step
def tidy():
    key(ESC)
    palette("pane: close all items", wait=1.0)
    open_file("inventory.py")
    open_file("NOTES.md")
    open_file("inventory.py")
    park()
    shot("zz-check")


@step
def theme_selector():
    open_file("inventory.py")
    palette("theme selector: toggle", wait=1.5)
    shot("24-theme-selector")
    key(ESC)


@step
def keymap_editor():
    open_file("inventory.py")
    key("k", "command")
    key("s", "command", wait=2.0)
    park()
    shot("25-keymap-editor")
    key("w", "command")


@step
def markdown_preview():
    open_file("NOTES.md")
    palette("markdown: open preview to the side", wait=2.0)
    park()
    shot("26-markdown-preview")
    key("w", "command")


@step
def split():
    open_file("inventory.py")
    palette("pane: split right", wait=1.5)
    park()
    shot("27-split-panes")
    key("w", "command")


@step
def multi_select():
    open_file("inventory.py")
    key(ESC)
    palette("go to line: toggle")
    typ("10")
    key(RET)
    key(RIGHT, "option")
    key(RIGHT, "option")
    key("d", "command")
    key("d", "command")
    key("d", "command")
    park()
    shot("28-multi-cursor-selection")
    key(ESC)
    key(UP, "command")


@step
def symbols():
    open_file("inventory.py")
    palette("outline: toggle", wait=1.2)
    shot("29-outline-symbols")
    key(ESC)


@step
def branch_picker():
    mouse("click", 128, 17, wait=1.5)
    shot("30-branch-picker")
    key(ESC)


@step
def user_menu():
    mouse("click", 1495, 17, wait=1.2)
    shot("31-user-menu")
    key(ESC)


@step
def peek():
    """Look up command names: type a word into the palette, capture to a check file, close."""
    key("p", "command", "shift")
    typ(__import__("os").environ.get("PEEK", "welcome"), wait=1.0)
    shot("zz-check")
    key(ESC)


@step
def extensions():
    palette("zed: extensions", wait=3.0)
    park()
    shot("41-extensions")
    key("w", "command")


@step
def onboarding():
    palette("zed: open onboarding", wait=2.5)
    park()
    shot("42-onboarding")
    key("w", "command")


@step
def agent_open():
    open_file("inventory.py")
    palette("agent: toggle focus", wait=2.5)
    park()
    shot("43-agent-panel")


# Agent panel controls, window points (the panel docks right; its composer row sits at y 896).
AG = {"mode": (1135, 896), "model": (1200, 896), "effort": (1265, 896), "profile": (1440, 896),
      "attach": (896, 896), "composer": (1100, 86)}


@step
def agent_menus():
    for i, (name, what) in enumerate([("mode", "45-agent-mode-menu"), ("model", "46-agent-model-picker"),
                                      ("effort", "47-agent-effort-menu"), ("profile", "48-agent-profile-menu"),
                                      ("attach", "49-agent-attach-menu")]):
        mouse("click", *AG[name], wait=1.2)
        shot(what)
        key(ESC, wait=0.8)


@step
def agent_prompt1():
    mouse("click", *AG["composer"], wait=0.6)
    typ("List the files in this folder", wait=0.8)
    park()
    shot("50-agent-composer-typed")
    key(RET, wait=1.2)
    shot("51-agent-running", wait=0.2)
    time.sleep(12)
    park()
    shot("52-agent-result")


@step
def agent_prompt2():
    name = "hello.txt" if THEME == "dark" else "hello-light.txt"
    mouse("click", 1100, 819, wait=0.6)   # the composer, docked at the bottom once a thread has messages
    typ(f"Create {name} here with one line", wait=0.8)
    key(RET, wait=2.0)
    shot("53-agent-tool-running", wait=0.2)
    time.sleep(4)
    shot("54-agent-tool-progress", wait=0.2)
    time.sleep(14)
    park()
    shot("55-agent-edit-result")


@step
def agent_header_menus():
    mouse("click", 1445, 50, wait=1.2)
    shot("56-agent-new-thread-menu")
    key(ESC)
    mouse("click", 1497, 50, wait=1.2)
    shot("57-agent-options-menu")
    key(ESC)
    palette("agent: toggle focus")   # close the panel
    park()


@step
def agent_new():
    """A fresh Claude Agent thread from the panel's + menu."""
    mouse("click", 1445, 50, wait=1.2)
    mouse("click", 1336, 160, wait=6.0)
    park()
    shot("44-agent-thread-empty")


@step
def launch():
    palette("pane: close all items", wait=1.0)
    park()
    shot("00-launch")


SETTINGS_AT = (306, 132)   # the Settings window's top-left, global points
NAV = {"general": 94, "appearance": 122, "keymap": 150, "editor": 178, "languages": 206, "search": 234,
       "window": 262, "panels": 290, "debugger": 318, "terminal": 346, "vcs": 374, "collab": 402,
       "ai": 430, "network": 458, "developer": 486}


def smouse(action, x, y, wait=0.8):
    """A pointer action in Settings-window coordinates. Never aimed at 'Fix in settings.json'."""
    ensure_front()
    subprocess.run([str(BIN / "mouse"), action, str(SETTINGS_AT[0] + x), str(SETTINGS_AT[1] + y)], check=True)
    time.sleep(wait)


@step
def settings():
    mouse("click", 1495, 17, wait=1.2)    # the user menu
    shot("zz-check")
    mouse("click", 1300, 138, wait=2.5)   # its Settings item (opens the Settings window, not the file)
    smouse("click", 80, NAV["general"], wait=1.5)
    smouse("move", 600, 740, wait=0.3)
    shot("32-settings-general", window="Settings")
    for i, pane in enumerate(["appearance", "editor", "panels", "terminal", "vcs", "ai"]):
        smouse("click", 80, NAV[pane], wait=1.5)
        smouse("move", 600, 740, wait=0.3)
        shot(f"{33 + i}-settings-{pane}", window="Settings")
    smouse("click", 110, 54, wait=0.8)
    typ("font size", wait=1.5)
    smouse("move", 600, 740, wait=0.3)
    shot("39-settings-search", window="Settings")
    smouse("move", 849, 253, wait=1.0)   # hover a switch (General > Accessible Mode position)
    shot("40-settings-search-hover", window="Settings")
    key("w", "command", wait=1.0)


if __name__ == "__main__":
    for name in sys.argv[2:]:
        print("--", name)
        STEPS[name]()
