# Pi

Pi is Inflection's personal AI. This package measures the public marketing site at [hey.pi.ai](https://hey.pi.ai/) and the signed-out chat at [pi.ai](https://pi.ai/), captured on 21 November 2026 with no account. The chat was read in light and dark. The marketing site ships one cream theme. Desktop captures are 1440×900 CSS (PNG 2880×1800 at devicePixelRatio 2). Phone captures are 390×844 CSS (PNG 780×1688).

The homepage is a signed-out chat, not a marketing page. `https://pi.ai` redirects to `/talk/<id>`. That id is an anonymous session. Login and signup stop at an empty wall. Nothing was typed. No identity provider was clicked. No form was submitted. No chat message was sent.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [DESIGN.md](DESIGN.md) | Generated from [tokens.json](tokens.json). Do not edit by hand |
| [tokens.json](tokens.json) | DTCG tokens: `core`, `light`, `dark` |
| [style-guide.html](style-guide.html) | Swatches, type and the signed-out controls, with a theme toggle |
| [components.md](components.md) | Controls that were on the signed-out pages, with measured values |
| [patterns.md](patterns.md) | Chat shell, login wall, help page and marketing home |
| [site-tree.md](site-tree.md) | Which public control opens which page, menu, drawer or wall |
| [screenshots/](screenshots/) | 16 public page captures, 256-colour PNGs |
| [raw/](raw/) | Declared colour custom properties from the live chat |
| [tools/](tools/) | Capture helpers and the token test. Tokens were written from the live readings |
| [icon.png](icon.png) | Site icon |

<!-- brief:start -->
<!-- brief:end -->

<!-- health:start -->
<!-- health:end -->

## How the values were read

Headed Chrome (Playwright, channel `chrome`) opened `https://pi.ai` and `https://hey.pi.ai/`. Headless Chromium stopped on a Cloudflare "Just a moment" page, so that route was not used for readings. The T3 preview tab loaded the chat but returned no screenshot frames, so the frames in [screenshots/](screenshots/) come from the headed Chrome session.

Custom properties were read from the CSSOM on `:root` and after adding `html.dark`. Resolved values were read with `getComputedStyle(document.documentElement)`. Component boxes, fonts, radii and colours were read with `getComputedStyle` on the painted buttons, the name field, the sidebar and the login heading.

Light mode is the page without the `dark` class. Dark mode is the same page after `classList.add('dark')`. That is a class toggle, not an account setting. The marketing site has no dark theme. Its colours are Framer tokens on `body`. Its hero type was computed on the `h1`.

`--sidebar-width` was `280px` with the sidebar open, `64px` after Toggle sidebar, and `0px` on the login wall and at 390px.

Viewport, device pixel ratio and visual viewport scale were read from `window` at each size. The 1440×900 context landed at 1440×900. The 390×844 context landed at 390×844. Both had `devicePixelRatio` 2 and visual viewport scale 1.

## What to distrust

Screenshots are 256-colour PNGs. Read colours from [tokens.json](tokens.json), not from the images.

The focus ring on the name field is Tailwind's default blue, `rgb(59 130 246 / 0.5)`. It is not a Pi token. It is left out of [tokens.json](tokens.json).

`--color-feed-feature-intro-graphic` stays `#FAF3EA` in the dark block. That is what the stylesheet declares. It was not seen painted.

Grenette on hey.pi.ai is "Grenette Pro Regular". Grenette in the app is the family `GRENETTE`. They are recorded as one family. The files are different: the marketing face is served by Framer, the app face by `/_next/static/media/`.

The login wall was measured in both themes by the class toggle. The painted header Log in fill in the second headed session was `rgb(26, 73, 51)`, one step from the declared `--color-primary-default` `#1A4631`. The token keeps the declared value. The first session's computed button fill matched `#1A4631`.

A status banner ("Pi is responding more slowly than usual") was on every app page during this capture. It is incident chrome, not a token.

A wrapping container around the greeting computes as DM Sans 16px. The paragraph itself, `p.text-body-alt-m-desktop`, is Grenette 18px on 25.2px, tracking -0.36px, colour `#1A4631`, in a 576px column. The token records that paragraph, not the wrapper.

## Fonts

DM Sans is the UI face. The app ships it as `DM_SANS` from `/_next/static/media/`. hey.pi.ai loads DM Sans from Google Fonts. The tokens name the family DM Sans and fall back to the system sans.

Grenette is the display face. It is proprietary. The style guide uses Source Serif 4 as a stand-in and says so. The login title uses `GRENETTE_CONDENSED` at 32px.

Fragment Mono is the marketing mono, loaded on hey.pi.ai at weight 400. The app names its mono role `MONO`. The family in the tokens is Fragment Mono, with a system mono fallback.

Twemoji Country Flags is prepended to every app font stack for emoji. It is not a text face.

## Coverage

| Item | Status |
|---|---|
| Colour, both themes | Captured. Declared `:root` and `.dark` custom properties, checked against computed values. [raw/css-vars.json](raw/css-vars.json) |
| Type roles | Captured for the greeting (Grenette 18px), login heading, body, label, hero and marketing CTA |
| Spacing and radii | Captured on the painted controls and the sidebar |
| Borders and elevation | Border colours captured. No elevated dialog was opened |
| Motion | Not captured. Resting pages only |
| Button, icon button, link, text field | Captured at rest. [screenshots/home-light-default.png](screenshots/home-light-default.png), [screenshots/login-light-empty.png](screenshots/login-light-empty.png) |
| Menu | Captured. Chat options shows Auto-read. [screenshots/home-light-chat-menu.png](screenshots/home-light-chat-menu.png) |
| Drawer | Captured at phone width. Chat history. [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Hover, pressed, disabled, loading, error | Not captured. Not painted. Not forced |
| Select, checkbox, radio, switch, tabs, tooltip, toast, dialog, table, avatar, badge | Not present on these public surfaces |
| Login and signup walls | Captured empty. OAuth, email and phone were not entered. [screenshots/login-light-empty.png](screenshots/login-light-empty.png), [screenshots/signup-dark-empty.png](screenshots/signup-dark-empty.png) |
| Help page and help center | Captured. Support and feedback forms were not submitted |
| Marketing home | Captured at 1440 and 390. [screenshots/marketing-light-default.png](screenshots/marketing-light-default.png), [screenshots/mobile-marketing-light-default.png](screenshots/mobile-marketing-light-default.png) |
| Download section | Captured on the marketing page. Store badges were not followed |
| Empty 404 | Captured on the app and on the marketing site |
| Signed-in chat, settings, voice | Not captured. Login is OAuth plus email and phone. The wall was photographed and the branch stopped |
| `login-extracted` | Left not-started |

## Do and don't

**Use the cream page and the forest pill.** The light page is `#FAF3EA` and the filled Log in pill is `#1A4631` with `#FCFAF7` text. See [screenshots/home-light-default.png](screenshots/home-light-default.png).

**Keep the open sidebar at 280px.** The side menu is 280px on desktop, and the page sets `--sidebar-width: 280px`. Collapsed it is 64px. See [screenshots/home-light-sidebar-collapsed.png](screenshots/home-light-sidebar-collapsed.png).

**Set display type in Grenette and UI type in DM Sans.** The greeting is Grenette 18px in a 576px column. The login title is Grenette Condensed 32px. Buttons and the name field are DM Sans 16px. The marketing hero is Grenette 64px. See [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/marketing-light-default.png](screenshots/marketing-light-default.png).

**Use 48px pills for the chat actions and 40px pills for the marketing CTA.** Chat Log in and Sign up for free are radius 48px. hey.pi.ai Try Pi is radius 40px. The send button is a 40px circle.

**Stop at the login wall.** The wall offers Google, Apple, Facebook, email and phone. This capture measured the buttons and did not open them. See [screenshots/signup-dark-empty.png](screenshots/signup-dark-empty.png).

## Rebuild

The tokens were written from [raw/css-vars.json](raw/css-vars.json) and the computed readings in this README. There is no token builder for this package.

```bash
python3 tools/catalog.py design-md pi
python3 tools/package_tests.py pi
```

A repo-wide `python3 tools/catalog.py check` fails in a sparse checkout because other `systems/` folders are absent. Check this slug on its own.
