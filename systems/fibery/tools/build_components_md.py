#!/usr/bin/env python3
"""Write components.md from the measured public controls. No invented states."""
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
text = """# Fibery components

Public marketing site only, measured 2026-11-21. The signed-in workspace was not opened.

## Button

The header signup link is a filled control: 40px tall, 6px radius, 16px horizontal padding, Suisse Intl 16/40 weight 600, ink fill `#251d1a`, soup text `#faebd6`. See [home-light-default](screenshots/home-light-default.png).

Hover on that link did not change the computed background.

## Quiet button

Log in uses the cream fill `#fdf7ef`, ink text, the same 40px height and 6px radius. See [login-light-providers](screenshots/login-light-providers.png).

## Pill

Audience pills (Startup, Enterprise, Agency, Non-profit) and view pills (Table, Board, Gallery, List, Timeline, Gantt, Calendar, Report, Map, Feed, Form, Dashboard) are `TabPillButton`: 34px tall, 48px radius, peach fill `rgb(240, 215, 200)`. See [home-light-pill-startup](screenshots/home-light-pill-startup.png) and [home-light-view-table](screenshots/home-light-view-table.png).

## Link

Footer and menu links are ink `#251d1a`, 14px, no underline. Header menus are hover panels, not buttons.

## Text field

The login email path shows empty Work Email and Password fields. They were not filled. See [login-light-email-empty](screenshots/login-light-email-empty.png).

## Menu

Solutions, Platform and Support open hover panels. Pricing is a link. Book a demo opens the cookie banner, then stops. See [home-light-menu-solutions](screenshots/home-light-menu-solutions.png).

## Dialog

The cookie banner is the only dialog captured: "Unexpected cookie banner", Deny and Accept. It was photographed, then hidden. Accept was not clicked. See [home-light-cookie-banner](screenshots/home-light-cookie-banner.png).

## Gaps

Select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar and badge were not present as product controls on the public pages that were opened. Search on the marketing site was not found. The user-guide search control was not identified. Signed-in workspace controls were not captured.
"""
(HERE / "components.md").write_text(text)
print("wrote components.md")
