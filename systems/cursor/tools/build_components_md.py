#!/usr/bin/env python3
"""Write components.md from the public capture notes. No crops were cut."""
import pathlib

ADAPTED_FOR = "cursor"
HERE = pathlib.Path(__file__).resolve().parent.parent
text = """# Components

Public marketing components on cursor.com, signed out, 2026-11-22. Crops were not cut. The screenshots in [screenshots/](../screenshots/) are the evidence.

| Component | Seen | States measured |
|---|---|---|
| Button | Nav Download is a light pill on the dark page. Contact sales is a ghost pill. | Default only. Hover, focus, pressed, disabled, and loading were not measured. |
| Link | Nav, footer, and in-page text links. Accent links use the declared orange. | Default only. |
| Text field | Login wall email field, empty. Placeholder "Your email address". | Empty. Nothing typed. |
| Menu | Desktop Models, Product, and Resources menus are in the header markup. Phone Open navigation opens a full-screen list. | Phone menu photographed. Desktop menus were read from the DOM, not expanded in a screenshot. |
| Card | Pricing plan cards and download platform cards. | Default. |
| Tabs | Pricing Individual and Teams. Individual was painted. Teams was not switched. | Default. |
| Badge | Pricing "Most popular" on Premium. | Default. |

Not present on the measured public pages: text area, select, checkbox, radio, switch, tooltip, toast, avatar, table, list row.

Dialog: the cookie notice was removed before the screenshots. It was not accepted or rejected. The signup route is a Cloudflare verification page. That checkbox was not clicked.
"""
(HERE / "components.md").write_text(text)
print("wrote components.md")
