# SoundCloud design reference

SoundCloud's public web UI, captured on 2026-11-21 from https://soundcloud.com/ while signed out. Desktop is the dark player at 1440 by 900. Phone is the light shell at https://m.soundcloud.com/, 390 by 844, which the desktop host redirects to at that width. Company, help, checkout, and developer pages are separate public sites and are included as their own screens. No account was created. Sign-in walls were recorded and not passed.

The player has no public theme switch. Dark is what the signed-out desktop shows. Light is the phone shell, not a second theme of the same player.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, fetched from the product site |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds scales. `dark` is the desktop player. `light` is the phone shell and Help Center orange. Every token has `$extensions.source` |
| DESIGN.md | Not generated. `make design-md` reads `catalog.json`, and this capture was not allowed to edit that file |
| [style-guide.html](style-guide.html) | Swatches and a few specimens, with a dark and light toggle |
| [components.md](components.md) | Component inventory with crops and token names, plus gaps |
| [patterns.md](patterns.md) | Shell, search, lists, the sign-in wall, and the phone sheet |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or dialog, mapped before screenshots |
| [components/](components/) | Crops in `components/crops/` |
| [icons/](icons/) | Index only. Artwork is not extracted |
| [screenshots/](screenshots/) | 68 viewport captures, 1440 and 780 px wide, quantised to 256 colours |
| [raw/](raw/) | `readings.json`, computed styles from the live pages |
| [tools/](tools/) | Capture runner and the builders that write tokens and the style guide |

## Brief

<!-- brief:start -->
Public capture of the signed-out SoundCloud player, the phone shell, and the company, help, checkout, and developer sites. Desktop is dark. Phone is a separate light shell. Sign-in walls were recorded and not passed. Brief and Health generators were not run, because they read catalog.json, which this capture does not edit.
<!-- brief:end -->

## Health

<!-- health:start -->
DESIGN.md is absent on purpose. make design-md, make brief, and make health need a catalog.json entry. catalog.json and webapps-manifest.json were not edited. make check will report that systems/soundcloud has no catalog entry.
<!-- health:end -->

## How the values were read

Playwright loaded the public pages headless. `getComputedStyle` was read on the desktop player at 1440 by 900, devicePixelRatio 1, and on the phone shell at 390 by 844, devicePixelRatio 2. The readings are in [raw/readings.json](raw/readings.json). The player declares almost no custom properties (three names, none of them a colour system), so values are computed styles, not a published token file.

The OneTrust banner was hidden with CSS. It was not accepted or rejected. No form was submitted. Facebook, Google, and Apple were not clicked.

Screenshots were taken with the kit's screenshot helper, then quantised to 256 colours. Values were not sampled from those PNGs except the phone search fill, which is marked Sampled.

## What to distrust

- **Light is a different site.** `m.soundcloud.com` is not the desktop player with a light class. Do not mix its 4px radius with the desktop pill radius and call it one theme.
- **The sign-in dialog is an iframe.** Its colours were not read. The screenshot shows the wall. It is not a measurement.
- **Hover does not change the fill.** Create account and Sign in fade the label to 40 percent. That alpha is listed under `$extensions.notTokenised`, not as a colour token.
- **Search focus border is translucent.** `rgba(153, 153, 153, 0.77)` was not flattened into a hex.
- **Söhne is not in the repo.** The font stack names it. The style guide falls back to the system sans.
- **Screenshots are 256-colour.** Read colours from tokens.json.
- **Private strings were painted out of screenshots.** A geoavailability line on [profile-dark-default.png](screenshots/profile-dark-default.png), and street, phone, email, and court lines on [imprint-dark-default.png](screenshots/imprint-dark-default.png), [terms-dark-default.png](screenshots/terms-dark-default.png), and [careers-dark-default.png](screenshots/careers-dark-default.png). The paint is a flat rectangle in the page colour. Those strings are not written in this package.

## Fonts

The desktop player and the phone shell use Söhne, then system-ui. Söhne is proprietary and is not committed. Company pages and the Help Center use Inter. The checkout body names Interstate, which was not used for a token because the visible headline on that page computed as Inter.

## Coverage

| Item | Status |
|---|---|
| Colour roles, dark player | Captured. [tokens.json](tokens.json) `dark.color`. Page, surface, text, muted, link, accent, focus, button. Overlay and scrim were not measured. |
| Colour roles, light shell | Captured in part. Phone text and button, Help Center orange and border. Raised, overlay, and scrim not captured. |
| Type | Captured. Display, title, heading, body, label, mobile title, help title. |
| Spacing | Captured in part. Four padding steps from the header button and search. No published scale. |
| Radii | Captured. Pill, field, phone control, help search. |
| Border widths | Captured in part. Focus ring 2px. Search border 1px. |
| Elevation | Not captured. No shadow was read on the player controls. |
| Motion | Not captured. Durations and easings were not in the computed styles that were read. |
| Sizing | Captured. Button 32, search 36 by 440, phone button 40, phone CTA 48, tab 50. |
| Layout | Captured as screenshots at 1440 and 390. Content widths were not measured as tokens. |
| Button | Captured. Default, hover, focus. Pressed, disabled, loading not captured. |
| Icon button | Captured as the header more control. States other than default not captured. |
| Link | Captured. Player blue, help orange, checkout blue. |
| Text field | Captured. Default and focus on desktop. Phone field fill is Sampled. |
| Text area | Not present on the public pages opened. |
| Select | Not present. |
| Checkbox, radio, switch | Not present. |
| Tabs | Captured. Search filters and profile tabs. |
| Menu | Captured. Settings menu and track more menu. |
| Tooltip | Not captured. None was held. |
| Dialog | Captured. Shortcuts, language, sign-in wall. Wall colours not read. |
| Toast | Not present. |
| Card | Captured. Playlist tile, help topic, plan card. |
| List row | Captured. Search and profile rows. |
| Table | Not present. |
| Avatar | Observed on the profile. Size not measured. |
| Badge | Observed as genre tags. Fill not measured. |
| App shell | Captured. Desktop and phone. |
| Form with validation | Not captured. The sign-in form was not submitted. A known probe of email Continue failed and was not repeated. |
| Empty | Not captured. |
| Loading | Observed. A spinner on the phone home. Colour not read. |
| Error | Not captured. |
| Destructive confirmation | Not present. |
| Feedback after an action | Captured in part. Play starts in the bottom bar. No toast. |
| Search and filtering | Captured. |
| Onboarding | Captured as the signed-out home and the phone sign-in sheet. Account creation was not followed. |
| Themes | Dark player and light phone shell. No desktop light theme exists while signed out. |
| Widths | 1440 and 390. Phone PNGs are 780 px wide because devicePixelRatio is 2. |

## Do and don't

- **Do keep the player near-black and the primary action white.** Create account is a white pill on #121212. See [discover-dark-default.png](screenshots/discover-dark-default.png).
- **Do use orange for the caret and the help header, and blue for player links.** They are different roles. See [help-light-default.png](screenshots/help-light-default.png) and the Learn More link in the player banner.
- **Do keep secondary actions quiet.** Sign in has no fill. Upload is a text link. See [button-signin-default.png](components/crops/button-signin-default.png).
- **Don't treat the phone site as a light theme of the desktop player.** It is a separate shell with 4px corners and a tab bar. See [mobile-discover-light-default.png](screenshots/mobile-discover-light-default.png).
- **Don't follow Feed, Library, or Like past the sign-in wall.** Those branches stop. See [wall-feed-dark-default.png](screenshots/wall-feed-dark-default.png).

## Rebuild

```bash
cd systems/soundcloud
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Recapture with Playwright, from the repo root:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/soundcloud/tools/capture/public/shoot.mjs
python3 systems/soundcloud/tools/capture/quantize.py ~/.design-systems/soundcloud/raw-shots
```

`quantize.py` takes the raw-shot directory, not `screenshots/`. Raw shots land in `~/.design-systems/soundcloud/raw-shots` and are not committed. The icon is the site apple-touch image, padded to 128 px. `python3 tools/fetch_icon.py soundcloud` needs a catalog entry, which this capture does not add.

## Surfaces

The desktop player, the phone shell, the company site, the Help Center, checkout marketing, and the developer site were each loaded. Signed-in Feed, Library, upload, and settings were not. The site tree records each wall.
