#!/usr/bin/env python3
"""Write components.md from the screens that were actually captured.

ADAPTED_FOR is vercel. Crops are not cut: the live browser screenshots are
viewport frames, and a crop box was not measured against the PNG. The
inventory points at the full screenshots instead.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ADAPTED_FOR = "vercel"

SCREENS = [
    ("App shell", "overview-dark-desktop.png", "Sidebar, top bar, usage card, project list."),
    ("Create menu", "create-menu-dark-desktop.png", "Create New menu, opened and not submitted."),
    ("Team settings", "settings-general-dark-desktop.png", "Settings replaces the main nav. General form."),
    ("Deployments", "deployments-dark-desktop.png", "Filter chips and deployment rows."),
    ("Domains empty", "domains-empty-dark-desktop.png", "Empty domain list. Buy, Transfer In and Connect External were not submitted."),
    ("Phone overview", "overview-dark-phone.png", "390 CSS px. Sidebar becomes a Find bar."),
    ("Scope switcher", "scope-switcher-dark-phone.png", "Team switcher sheet. Create Team was not submitted."),
]


def build():
    lines = [
        "# Components",
        "",
        "Signed-in Vercel dashboard, dark theme, 2026-11-21. Values are the readings in [raw/](raw/). Screenshots are the evidence for layout.",
        "",
    ]
    for title, filename, note in SCREENS:
        path = HERE / "screenshots" / filename
        if not path.exists():
            raise SystemExit(f"missing screenshot: {filename}")
        lines += [
            f"## {title}",
            "",
            f"![{title}](screenshots/{filename})",
            "",
            f"{note} Source: [screenshots/{filename}](screenshots/{filename}).",
            "",
        ]
    lines += [
        "## Observed controls",
        "",
        "| Control | Where | Reading |",
        "|---|---|---|",
        "| Primary button (Save) | Team Settings | 32px tall, 6px radius, fill rgb(237, 237, 237), text rgb(10, 10, 10), 14px / 500 |",
        "| Sidebar link | Projects | 36px tall, 6px radius, text rgb(161, 161, 161), 14px |",
        "| Page title | Deployments h1 | 24px / 600 |",
        "| Body | dashboard | GeistSans, 16px / 24px, page rgb(0, 0, 0), text rgb(237, 237, 237) |",
        "| Filter chip | Deployments | 32px tall, pill radius |",
        "| Search field | Domains | 36px tall, fill rgb(26, 26, 26) |",
        "",
        "## Gaps",
        "",
        "Hover, pressed, focus-visible, disabled and error states were not forced. Light theme was offered and not switched. No dialog was submitted. No crop set was cut from these frames.",
        "",
    ]
    (HERE / "components.md").write_text("\n".join(lines))
    print("wrote", HERE / "components.md", "adapted for", ADAPTED_FOR)


if __name__ == "__main__":
    build()
