# Rivian patterns

Public site only, captured 2026-11-21. Screenshots are in [screenshots/](screenshots). The control map is [site-tree.md](site-tree.md).

## App shell

A white bar, 56px tall, with the wordmark, five text menus (Vehicles, Charging, Technology, Discover, Gear Shop), an amber Demo drive pill, a chat icon and a sign-in icon. On a 390-wide viewport the menus collapse into one Open accordion. See `home-light-default.png` and `mobile-home-light-menu.png`.

Sign in goes to `https://rivian.com/auth/login`. That branch stops. Password was not submitted.

## Mega-menu

Each header label opens a panel of model cards plus a text list. Vehicles is the fullest: R1S, R1T, R2 cards, then Compare, Demo drive, Trade-in, offers, inventory, purchasing, financing, insurance, R3, Fleet. See `home-light-vehicles-menu.png`.

## Hero

Full-bleed photograph, white display type, a white pill and an outline pill, carousel dots. See `home-light-default.png`.

## Model page

A long marketing page per vehicle (R1S, R1T, R2, R3, Tri). Same header, same Adventure type, amber used sparingly. See `r2-light-default.png`.

## Inventory and offers

Inventory at `/configurations/list` opens an empty postal-code dialog before the list. The field was left empty and Continue was not clicked. See `inventory-light-default.png`. Offers is a list of current deals. See `offers-light-default.png`.

## Assistant

Have a question? opens a side panel. The greeting is the product's own. The message field was left empty. See `home-light-question.png`.

## Video

Watch the video opens a full-screen player. See `home-light-video.png`.

## Cookie banner

Ketch dialog, "We respect your privacy", Accept All, Reject All, Manage Preferences. Reject All was clicked. Manage Preferences opens a purposes dialog with switches (Strictly Necessary always on, others opted out) and a Confirm button. Confirm was not clicked. The preferences dialog is a captured state, not a saved choice.

## Forms not submitted

Demo drive booking, trade-in, Get updates, newsletter Subscribe, and the charging trip planner are public forms. They were not filled and not submitted. Coverage rows mark them not captured.
