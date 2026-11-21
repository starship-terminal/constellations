#!/usr/bin/env python3
"""Write components.md from the signed-in Quizlet crops.

PRODUCT (adapt): the kit copy expected Claude's component-tokens.json. This
writes the inventory that this capture actually has.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "components.md"

TEXT = """# Quizlet components

Signed-in capture of quizlet.com on 2026-11-21, night theme (`body.theme-night`). Desktop shots were measured at 1440 by 900 CSS pixels, device pixel ratio 2. Phone shots were measured at 430 by 932, not the requested 390 by 844. The preview reported a 1280 by 800 tool viewport for both requests. The PNG sizes are the measured viewports at 2x.

Crops are 2x element screenshots in [components/crops/](components/crops). Page shots are in [screenshots/](screenshots).

## Discovery list

| Surface | URL | Screenshot |
|---|---|---|
| Your library | `/user/{handle}/sets` | [library-night-empty](screenshots/library-night-empty.png) |
| Settings, profile | `/settings` | [settings-night-profile](screenshots/settings-night-profile.png) |
| Settings, notifications | `/settings` | [settings-night-notifications](screenshots/settings-night-notifications.png) |
| Create a set, empty | `/create-set` | [create-set-night-empty](screenshots/create-set-night-empty.png) |
| Your Sets, phone | `/latest` | [home-night-phone](screenshots/home-night-phone.png) |
| Nav, phone | `/latest` | [nav-night-phone](screenshots/nav-night-phone.png) |
| Settings, phone | `/settings` | [settings-night-phone](screenshots/settings-night-phone.png) |

## Search field

Night search on the library page. Background `{color.gray.700}` (`#2E3856`), radius `{radius.field}` (`8px`).

![Search field](components/crops/search-field.png)

## Primary button

`Create a flashcard set` on the empty library. Background `{color.twilight.500}` (`#4255FF`), white label, 14px/20px weight 600, padding 10px 16px, radius `{radius.pill}` (`200px`).

![Primary button](components/crops/button-primary.png)

## Create menu

Opened from the header Create control. Items: Lecture recording, Flashcard set, Podcast, Study guide, Practice test, Folder, Study group. Nothing in the menu was submitted.

![Create menu](components/crops/menu-create-open.png)

## Account menu

Opened from the header avatar. Items: Achievements, Settings, Light mode, Log out, Privacy policy, Help and feedback, Upgrade. The crop was deleted because it showed the account email. Light mode was not switched. Log out and Upgrade were not clicked.

## Gaps

Hover, pressed, and focus-visible were not captured. Light mode was offered and not switched. Icons were not exported as SVG. The create form was left empty.
"""

def main():
    OUT.write_text(TEXT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
