# District design reference

A token set and component reference for District's public site, the going-out product at district.in (movies, events, dining, play, activities, stores). Captured signed out on 2026-11-21 in headless Chromium at 1440×900 and 390×844. The public pages paint one theme, light. Stylesheets also declare `html[data-theme=dark]`; no toggle was found, so dark is tokenised and not shown.

The login control opens an in-page phone OTP dialog. `https://www.district.in/login` is a not-found page. That branch stopped. No account wall URL was reached beyond the dialog. Checkout, bookings, and profile were not opened.

| File | What it is |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Which control opens which page or in-page interaction |
| [tokens.json](tokens.json) | DTCG tokens from the public stylesheet, plus a few computed control values |
| [DESIGN.md](DESIGN.md) | Generated export. Take values from tokens.json |
| [style-guide.html](style-guide.html) | Light roles and four control specimens |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | How the public pages combine |
| [screenshots/](screenshots) | 47 captures, 256-colour. Location text and the login phone field are painted over. Contact phone, email, and street address are painted over |
| [raw/](raw) | [css-vars.json](raw/css-vars.json): declared custom properties, light and dark |
| [tools/](tools) | Builders and the adapted capture kit |

## Brief

<!-- brief:start -->
Read [tokens.json](tokens.json) before designing in this style. Public UI is light: white page, near-black text, brand purple on the selected nav and primary actions.

1. Keep the page white and the type near-black.
2. Use purple for the selected nav and the primary action.
3. Make header controls pills.
4. Use 16px radius on dialogs and posters.
5. Do not invent a signed-in shell from these pages.
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded in this capture. catalog.json was not edited, so the scorecard does not list this package yet.
<!-- health:end -->

## How the values were read

Custom properties were parsed from the public district-web stylesheets (`:root,html[data-theme=light]` and `html[data-theme=dark]`). Semantic roles alias those ramps. A few control colours (Login, chips, selected nav `#5815fd`, disabled Continue) were read with `getComputedStyle` on the live page. Screenshots are 256-colour and are not a source of values.

## What to distrust

Dark tokens were not painted. `#5815fd` is a computed nav colour and is not a declared `--color-*` name in the harvested sheet. Disabled Continue is the empty login button, not a general disabled style. Contact and login shots have painted-over regions. Play and Stores were empty in this session.

## Fonts

BeVietnamPro, sans-serif, read from the body. The font file is not in this package. Weights 400, 500, 600, and 700 are declared as `--font-regular` through `--font-bold`.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured in tokens.json from CSS |
| Colour roles, dark | Declared in CSS. Not shown. No toggle |
| Type | Captured: BeVietnamPro and the declared size scale |
| Spacing, radii, sizing | Captured from computed controls and declared sizes |
| Motion | Durations and one easing from the stylesheet |
| Button, link, field, select, radio, tabs, menu, dialog, card, list row, avatar | Captured on public pages. See components.md |
| Checkbox, switch, tooltip, toast, table | Not present on the captured pages |
| Focus, pressed, loading, error | Not captured |
| App shell, search, filters, empty, login wall | Captured. See screenshots/ and site-tree.md |
| Form validation, destructive confirm, onboarding | Not captured. Form was not submitted. Signed-out |
| Desktop 1440 and phone 390 | Captured |

## Do and don't

- Do keep primary actions purple and header controls as pills. See [contact-light-default.png](screenshots/contact-light-default.png) and [home-light-default.png](screenshots/home-light-default.png).
- Do mark the current nav item with a purple label and a 3px underline. See [home-light-default.png](screenshots/home-light-default.png).
- Do use a white 16px dialog for login and location. See [home-light-login-wall.png](screenshots/home-light-login-wall.png).
- Don't treat `/login` as the account screen. It is a missing page. See [login-url-light-missing.png](screenshots/login-url-light-missing.png).
- Don't design the signed-in app from these pages. The login branch stopped at the OTP dialog.

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Run both from `systems/district`, or pass the paths above from the repo root as `python3 systems/district/tools/build_tokens.py`.
