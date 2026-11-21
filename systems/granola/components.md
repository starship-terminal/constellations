# Granola components

Public marketing site, 2026-11-21. Values are from [raw/components.json](raw/components.json) and [tokens.json](tokens.json). Crops were not cut. The screenshots show the components in place.

## Button

Hero "Download for free": fill `#5b6f00` (`light.accent`), text `rgb(252, 252, 248)` (`light.text-on-accent`), height 56 px, padding 9 px 24 px, font 16 px / weight 430, pill radius. Screenshot: [screenshots/home-light-default.png](screenshots/home-light-default.png).

Header "Download": height 40 px, padding 0 12 px, font 14 px, fill `rgba(98, 90, 34, 0.06)` at rest and `rgba(86, 81, 46, 0.12)` on hover. Pill radius.

Dialog "Send link": height 36 px, fill `#5b6f00`, text white, weight 500, pill radius. Not clicked.

Pressed and disabled were not held. Loading was not shown.

## Link

Header "Pricing": 14 px, colour `rgb(41, 41, 41)`, transparent fill, pill padding 6 px 12 px, height 38 px.

## Text field

Dialog email field, placeholder "Your work email". Height 36 px, padding 8 px 24 px, font 16 px, pill radius, empty. Not typed. Not submitted. Screenshot: [screenshots/home-light-mobile-dialog.png](screenshots/home-light-mobile-dialog.png).

Error and disabled states were not shown.

## Menu

Features hover menu. Items: Notepad, Chat, Mobile & Watch, MCP, Voice typing. Opens on pointer enter. Screenshot: [screenshots/home-light-features-menu.png](screenshots/home-light-features-menu.png).

Phone drawer: Open menu becomes Close menu. Screenshot: [screenshots/home-light-mobile-menu.png](screenshots/home-light-mobile-menu.png).

## Dialog

"Granola for mobile". Overlay `oklab(0 0 0 / 0.6)`. Email field and Send link as above. iOS and Android labels. Close dismisses it. Send link was not clicked.

## Login wall

https://notes.granola.ai/login returned HTTP 500 and painted "Login to get started" with Sign in with Google, Sign in with Microsoft, and Sign in with SSO. None were clicked. Screenshot: [screenshots/notes-login-error.png](screenshots/notes-login-error.png).

## Not present on the photographed pages

Checkbox, radio, switch, select, text area, tabs (beyond the iOS / Android labels), tooltip, toast, table, avatar, badge, card as a named component. Pricing plan cards are a pattern, in [patterns.md](patterns.md).

## Gaps

- Focus-visible on the hero button was not measured. Header Download focus used the browser default outline, not `--oats-border-focus`.
- Hover was measured on the header Download link only.
- Pressed, disabled, and loading were not captured.
- No component crops were cut.
