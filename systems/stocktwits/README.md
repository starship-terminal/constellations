# Stocktwits design reference

Public design system of Stocktwits, captured from https://stocktwits.com/ on 2026-11-21, signed out, in headless Playwright. One theme: light (`html.light`, `data-theme="light"`). Widths: desktop 1440x900 at 1x, phone 390x844 at 2x. No account was created. No email, username, or password was typed. No form was submitted. Google, Apple, Facebook, and X were not clicked.

The control map is [site-tree.md](site-tree.md).

| File | What it is |
|---|---|
| [icon.png](icon.png) | 128 px crop of the wordmark from the home screenshot. The site's apple-touch-icon returned a Cloudflare challenge, so this is a crop, not the fetched icon. |
| [tokens.json](tokens.json) | DTCG tokens. `core` plus `light`. No dark set. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Generated. Do not edit. |
| [style-guide.html](style-guide.html) | Renders the measured colours and controls. Light only. |
| [components.md](components.md) | Measured components and gaps. |
| [patterns.md](patterns.md) | How the public pages are put together. |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or wall. |
| [components/](components) | Crops of measured controls. |
| [icons/](icons) | Index only. Icons were not extracted. |
| [screenshots/](screenshots) | 53 public captures, 256-colour. |
| [raw/](raw) | Computed styles, resolved custom properties, and the extra sign-in and chip readings. |
| [tools/](tools) | Capture scripts and builders. |

## Brief

<!-- brief:start -->
Brief is written by `make brief` after the catalog entry exists. This capture does not edit catalog.json, so the generated Brief is not in this commit.
<!-- brief:end -->

## Health

<!-- health:start -->
Health is written by `make grade` from the scorecard. This capture does not edit catalog.json, so no grade row was written.
<!-- health:end -->

## How the values were read

Custom properties were read from `document.styleSheets` on `/` and resolved with `getComputedStyle(document.documentElement)` in the light theme at 1440x900. Component colours, type, and radii were read with `getComputedStyle` on the live elements. Sign-in fields and Bullish and Bearish chips were read in a fresh browser context and stored in [raw/extra-readings.json](raw/extra-readings.json). Screenshots were taken with Playwright and quantised to 256 colours. Colours in this package come from CSS, not from the PNGs.

## What to distrust

The filled Sign Up button paints black. `--primary-button-background` is `#1b66e7` and is not what that button uses. Card radius was not read. Focus ring colour was not read. The live-calls badge purple was not read. Dark greys exist as custom properties (`--dark-grey-*`) but the public site did not switch to them. The icon is a screenshot crop.

## Fonts

Source Sans 3 is the UI face, with a fallback named Source Sans 3 Fallback. It is loaded from the site. This package does not commit the font files. Font Awesome 6 is the icon font and is not committed.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json). Page, surface, text, muted, border, link, up, down. |
| Colour roles, dark | Not present as a public theme. `prefers-color-scheme: dark` still painted light. |
| Type | Captured for body, button, nav, tab, link, field, auth heading. Display sizes on marketing pages not measured. |
| Spacing | Field and button padding captured. A full spacing scale was not declared. |
| Radii | Pill and field captured. Card radius not captured. |
| Border widths | Hairline `#e5e5ea` captured as a colour. Widths beyond the field (0) and the disabled button (1px) not fully mapped. |
| Elevation | Not captured. Measured controls had `box-shadow: none`. |
| Motion | Not captured. Durations were not read. |
| Sizing | Button 40px, icon button 24px, field 40px. |
| Layout | Desktop 1440 and phone 390 captured. Content widths not tokenised. |
| Button | Captured. [screenshots/home-light-default.png](screenshots/home-light-default.png). Hover of Sign Up captured as a computed style. Pressed not captured. |
| Icon button | Pause ticker captured. |
| Link | Captured. Blue `#1b66e7`. |
| Text field | Captured on `/signin`. Focused, nothing typed. [screenshots/signin-light-login-focus.png](screenshots/signin-light-login-focus.png). |
| Text area | Not present on public pages reached. |
| Select | Not present. |
| Checkbox | Present only inside the OneTrust dialog, which was hidden and not submitted. Not captured. |
| Radio | Not present. |
| Switch | Not present on public pages. |
| Tabs | For You / Following and symbol tabs captured. |
| Menu | Phone menu captured. [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). Experience dialog captured. [screenshots/home-light-experience.png](screenshots/home-light-experience.png). Ticker filter captured as the Equities state. [screenshots/home-light-ticker-filter.png](screenshots/home-light-ticker-filter.png). |
| Tooltip | Not captured. |
| Dialog | Experience chooser captured. Destructive confirm not present. |
| Toast | CSS variables exist (`--stocktwits-toastify-*`). No toast was triggered. Not captured. |
| Card | Trending cards and plan cards captured as screenshots. Radius not read. |
| List row | Watchlist rows in screenshots. |
| Table | Sentiment table. [screenshots/sentiment-light-default.png](screenshots/sentiment-light-default.png). |
| Avatar | Message avatars in screenshots. Other people's names and pictures stay, per the repo rule. |
| Badge | Live-calls chip is in screenshots. Its purple was not read. |
| App shell | Captured at both widths. |
| Form with validation error | Not captured. Forms were not submitted. |
| Empty | Signed-in empty states not reached. |
| Loading | Not captured as a held state. |
| Error | Cloudflare challenges blocked some second navigations. That is a capture gap, not a product error screen. |
| Destructive confirmation | Not present while signed out. |
| Feedback after an action | Not captured. No action was submitted. |
| Search | Focus opens a trending list. [screenshots/home-light-search.png](screenshots/home-light-search.png). Nothing typed. |
| Filtering | Sentiment chips and ticker Equities filter captured. |
| Onboarding | Signup wall recorded and not entered. [screenshots/signup-light-default.png](screenshots/signup-light-default.png). |
| Themes | Light only. |
| Widths | 1440x900 and 390x844. |

## Do and don't

1. **Do use black pills for the main action.** Sign Up is black with white type, fully rounded. [screenshots/home-light-default.png](screenshots/home-light-default.png).
2. **Do use green for up and red for down.** Gains are `#128760`. Losses are `#dd331d`. [screenshots/sentiment-light-default.png](screenshots/sentiment-light-default.png).
3. **Do keep the page white and the fields grey.** Page is `#ffffff`. Fields and secondary surfaces are `#f2f2f7`. [screenshots/signin-light-default.png](screenshots/signin-light-default.png).
4. **Don't invent a dark theme.** The public site stayed light. Dark custom properties exist and were not applied.
5. **Don't treat the blue token as the Sign Up fill.** `--primary-button-background` is `#1b66e7`. The button on screen is black.
6. **Don't submit the auth form to see more.** Reply, like, watchlist, and profile stop at `/signin` or `/signup`.

## Rebuild

```bash
cd systems/stocktwits
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
```

Capture (needs Playwright):

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/stocktwits/raw-shots
```

`make design-md` and `make brief` need a catalog entry. This capture does not add one.
