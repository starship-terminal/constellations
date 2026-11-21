# FeedHive design reference

A token set and site map for FeedHive's public marketing site (https://www.feedhive.com/). Captured signed out on 2026-11-21 in Playwright at 1440×900 and 390×844. Catalog name: FeedHive.

The walk stopped at the auth wall. Login opens https://app.feedhive.com/signin (the header href is https://app.feedhive.io/signin, which redirects). The form shows email, password, and Sign in with Google. Nothing was typed. Google was not clicked. No account was created. https://www.feedhive.com/login is a 404.

The signed-in app was not captured. Unread token values are Not captured.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, fetched from www.feedhive.com |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (fonts, type sizes, radii, control heights) and `light` (14 colours). No dark set. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | A short export of the same tokens. Take values from tokens.json. |
| [style-guide.html](style-guide.html) | The measured colours and the marketing buttons, rendered from those values |
| [components.md](components.md) | Buttons, links, fields, menus, tabs, cards, and the sign-in dialog, with crops |
| [patterns.md](patterns.md) | Header shell, pricing toggle, public tool forms, and the auth stop |
| [site-tree.md](site-tree.md) | Header, footer, and in-page controls, and which page or wall each one opens |
| [login-review.json](login-review.json) | The wall that was reached. `signed_in` is false. |
| [components/crops/](components/crops) | 9 element crops from the screenshots |
| [icons/](icons) | Index only. Icons were not extracted. |
| [screenshots/](screenshots) | 27 captures: home, four desktop menus, pricing, blog, tools, the 404, the sign-in wall, and the phone drawer |
| [raw/](raw) | `component-tokens.json` (the builder input) and `css-vars.json` (why no product token sheet was promoted) |
| [tools/](tools) | `build_tokens.py` |

## How the values were read

Headless Chromium loaded www.feedhive.com and the sign-in URL. Computed styles were read from the live elements: header Login and Sign Up, the hero CTA, the home h1, the pricing Monthly and Yearly buttons, and the sign-in email field and Sign in button. Hover on Sign Up was a real pointer hover (`#3347fb`). Focus on the email field was keyboard focus, with no text entered.

The marketing CSS is Tailwind. `bg-primary` paints `#4457ff`. There is no FeedHive custom-property sheet on `:root`. Cookie-consent `--cc-*` variables and Tailwind's default `--font-sans` were seen and not promoted. See [raw/css-vars.json](raw/css-vars.json).

Screenshots are full colour. Read values from the tokens, not the images.

## What to distrust

- The sign-in button blue (`#3b82f6`) is not the marketing primary (`#4457ff`). They were read on different hosts.
- Type tokens store the measured font-size only. Weight, line-height, and letter-spacing are in the source string, not separate tokens.
- Pill radius on the sign-in fields is the computed `9999px`, not a named scale step.
- No dark theme was offered. A dark set was not invented.
- Plan prices in the pricing screenshot are what the page painted in this locale. They are not tokens.

## Fonts

Inter is the UI face, with an "Inter Fallback" in the marketing computed style. Plus Jakarta Sans is the display face on headings. Both are loaded by the site. This package does not ship the font files.

## Coverage

| Item | Status | Where, or why not |
|---|---|---|
| Colour roles | captured | [tokens.json](tokens.json) `light.color` |
| Type | partly | Families and four sizes measured. No full scale. |
| Spacing, elevation, motion | not captured | No spacing or motion token was declared. Shadows seen only as the sign-in focus ring. |
| Button | captured | Login, Sign Up, hero CTA, sign-in submit |
| Link | captured | Header and footer |
| Text field | partly | Sign-in fields and public tool textareas. Not submitted. |
| Menu | captured | Four desktop menus and the phone drawer |
| Tabs | captured | Pricing Monthly / Yearly, home demo tabs |
| Dialog | captured | Sign-in wall only |
| Card | captured | Pricing cards |
| Search | not present | No search control on the pages opened |
| Icon button, select, checkbox, radio, switch, tooltip, toast, table, avatar, badge | not captured | Not on the public pages, or behind the wall |
| Signed-in app | not captured | Auth wall. See [login-review.json](login-review.json) |
| Dark theme | not present | No switch |

## Do and don't

- Do use one blue for marketing actions. Sign Up and Get started for free share `#4457ff`. See [home-light-default.png](screenshots/home-light-default.png).
- Do keep Login quiet. It is a warm grey face, not an outline of the primary. See [button-login-default.png](components/crops/button-login-default.png).
- Do set headings in Plus Jakarta Sans and controls in Inter.
- Don't treat the sign-in button blue as the brand primary. It was measured on the app host.
- Don't invent the signed-in product. The walk stopped at the wall.

## Rebuild

```bash
cd systems/feedhive && python3 tools/build_tokens.py
```

`catalog.json` is not part of this capture. Register the package in a later change if the gallery should list it.
