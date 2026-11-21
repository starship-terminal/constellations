# ElevenMusic design reference

ElevenMusic is ElevenLabs' public music app at elevenmusic.io. This package was read on 2026-11-21, signed out, in headless Chromium at 1440×900 and 390×844. Dark is the live default. Light was applied with the footer Light theme control. The catalog, tools, sounds, pricing, blog, and terms pages are public. Studio, library, composer, chat, and billing stop at a login wall and were not entered.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from the apple-touch-icon |
| [tokens.json](tokens.json) | Measured colour, type, radius, and control sizes for the public chrome |
| [DESIGN.md](DESIGN.md) | Generated from the tokens and this README |
| [style-guide.html](style-guide.html) | Renders the public chrome colours and the main controls |
| [components.md](components.md) | Buttons, prompt, menus, dialogs, cards, and the gaps |
| [patterns.md](patterns.md) | Shell, catalog, pricing, and the login wall |
| [site-tree.md](site-tree.md) | Every public control and what it opens |
| [login-review.json](login-review.json) | What the login wall offers, and where each branch stopped |
| [components/crops/](components/crops) | Sidebar, header actions, and the prompt |
| [screenshots/](screenshots) | Home, explore, tools, sounds, pricing, login, and phone. Viewport shots. The home page did not report a scroll height past the viewport, so there is no separate full-page tile. |
| [raw/](raw) | The computed-style dump the tokens were read from |
| [tools/](tools) | Checks that every token names its source |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Playwright opened the live site. `getComputedStyle` was read on the body, the hero heading, Sign in, Start free, the prompt, and the suggestion chips, in dark and after the light theme click. Colours arrived as CSS `lab()` and were converted to sRGB. The site does not publish a product token layer. The custom properties on the page were Tailwind internals and were not copied into tokens.json.

The Cookiebot banner was hidden with CSS. No consent button was clicked. No form was submitted.

## What to distrust

Screenshots are 256-colour PNGs. Read colours from tokens.json.

The accent is the inverted text colour, not a separate brand hue. Artwork on the home page (the planet, the orange disc) is not a token.

Light theme was applied in the page. It is a real control, and the light screenshot shows it. Hover, focus, and pressed were not measured.

Pill radii computed as a huge pixel value. tokens.json stores 9999px.

Signed-in studio UI is not in this package.

## Fonts

Display is Waldenburg, with an Arial fallback, weight 300. UI is Inter. Neither file is in the package. The style guide uses Georgia and system sans.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured for page, surface, text, muted, accent, border, in dark and light. Overlay is the login dialog scrim. Success, warning, danger, and info were not on the public chrome. |
| Type | Captured: display, body, prompt, control, chip. Code was not present. |
| Spacing, radii, sizing | Captured for the controls that were measured. No full spacing scale is declared. |
| Motion | Not captured. |
| Button, link, text field, tabs, menu, dialog, card, list row, avatar, badge | Captured as they appear on the public pages. |
| Text area, select, radio, switch, tooltip, toast, table | Not present on the public chrome. |
| Checkbox | The terms checkbox is in the email step. It was not checked. |
| Patterns | Shell, catalog, pricing, and login wall. Onboarding was not filled. |
| Themes and widths | Dark and light at 1440. Dark at 390. |
| Signed-in app | Not captured. Every branch stops at the login wall. See [login-review.json](login-review.json). |

## Do and don't

- **Keep the chrome monochrome.** Sign in and Start free invert the same near-black and near-white. Colour belongs to artwork. [screenshots/home-dark-default.png](screenshots/home-dark-default.png)
- **Use pills for controls.** Sign in, Start free, chips, and the provider buttons are fully rounded. [screenshots/login-dark-default.png](screenshots/login-dark-default.png)
- **Set display type light and tight.** The hero is Waldenburg 300 at 40px with negative tracking. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Stop at the login wall.** Studio, library, composer, and chat are not in this package. [screenshots/login-dialog-dark.png](screenshots/login-dialog-dark.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks sources. It does not refetch the site.
