# Deezer design reference

A token set and component reference for Deezer's public web (https://www.deezer.com), the music streaming site. Captured signed out on 2026-11-21 from the marketing homepage, offers, feature pages, the public channel player, support, legal, and the login wall. Dark is the player shell (`color-scheme: dark`). Light is the marketing homepage. Widths are 1440 and 390. No account was created. No email or password was typed.

The package holds screenshots of the public surface, Tempo custom properties read from the player, and computed styles from the homepage and login wall. Brand artwork stays in the screenshots. Do not lift the logo or the purple as a mark for another product ([docs/RIGHTS.md](../../docs/RIGHTS.md)).

| File | What it is |
|---|---|
| [icon.png](icon.png) | Apple touch icon, resized to 128 px |
| [tokens.json](tokens.json) | DTCG tokens: `core` scales, `dark` Tempo roles, `light` marketing computed colours |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json and this README |
| [style-guide.html](style-guide.html) | Swatches and a few controls rendered from the tokens |
| [components.md](components.md) | Component inventory with crops |
| [patterns.md](patterns.md) | Marketing shell, player shell, login wall, search |
| [components/](components/) | 13 crops in `crops/` |
| [icons/](icons/) | `INDEX.tsv` only. Product icons were not extracted |
| [screenshots/](screenshots/) | 24 public captures, desktop and phone |
| [raw/](raw/) | `css-vars.json` (689 Tempo and GDPR properties), `computed-samples.json`, `search-field.json` |
| [tools/](tools/) | `build_tokens.py`, `build_style_guide.py`, `build_components_md.py`, `quantize.py` |
| [site-tree.md](site-tree.md) | Public control map and login-wall stops |
| [login-review.json](login-review.json) | What the login wall asked for, and that nothing was submitted |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Playwright (headless Chromium) opened public URLs. Cookie UI was hidden in the DOM and not accepted or refused. Custom properties were read from `getComputedStyle(document.documentElement)` on https://www.deezer.com/en/channels/explore, which ships the Tempo set (about 1400 names). Semantic roles, type, space, radii and motion were copied into [raw/css-vars.json](raw/css-vars.json). Hue ramps other than purple and neutralPurple were left out of that file. Homepage button, hero and login-field colours were read with `getComputedStyle` on the live elements and stored in [raw/computed-samples.json](raw/computed-samples.json). `tools/build_tokens.py` writes [tokens.json](tokens.json) from those two files.

## What to distrust

- Marketing purple (`#a238ff`) and player accent (`#ad47ff`) are both measured. They are not the same token.
- Light page background is recorded as white from the screenshot. The computed body background was transparent.
- Header black is observed, not a named Tempo role on the marketing page.
- Hover and pressed fills are Tempo declarations. Those states were not photographed except search focus and email focus.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- The player previewed a public track while signed out. That is the site's own preview, not a signed-in library.
- No dark marketing theme was found. `color-scheme` on the player was dark. A light player theme was not switched.

## Fonts

| Family | Used for |
|---|---|
| Deezer Brand | Marketing display. Proprietary. The style guide falls back to Tahoma |
| Deezer Product | Tempo headings. Proprietary |
| Deezer Headline VF | Player screen titles, condensed. Proprietary |
| Inter | Body, buttons, fields. The style guide names Inter and falls back to Arial |
| SFMono-Regular stack | `core.fontFamily.mono`. Not seen in the public UI |

## Coverage

| Checklist item | Status | Where |
|---|---|---|
| Colour roles, dark | Captured | `dark.background`, `dark.text`, `dark.border` from Tempo |
| Colour roles, light | Partly | Marketing computed colours only. No full light semantic set |
| Accent hover and pressed | Partly | Declared in Tempo (`accentHover`, `accentPressed`). Not photographed |
| Status colours | Captured as tokens | Success, warning, danger fills, text and borders in Tempo. Info not present as a named role |
| Type roles | Captured | `core.fontSize`, `core.lineHeight`, `core.fontFamily` |
| Spacing, radii, borders, sizes | Captured | `core.space`, `core.radius`, `core.borderWidth`, `core.size` |
| Elevation | Partly | Tempo shadow tokens exist. Not isolated in a crop |
| Motion | Captured as tokens | Durations and easings. No motion stills |
| Button | Captured, default only | Marketing Sign up, Log in, login submit |
| Icon button | Observed | Player controls in [player-bar-default.png](components/crops/player-bar-default.png) |
| Link | Captured | Header and footer links in site-tree.md |
| Text field | Captured, empty | Login email and password |
| Text area | Not present | No public text area |
| Select | Not captured | Native language select was focused. No styled menu opened |
| Checkbox, radio, switch | Not present | Not on the public pages captured |
| Tabs | Not present | Channel pages use cards, not tabs |
| Menu | Captured | Phone burger drawer |
| Tooltip | Not captured | Not held |
| Dialog | Captured | Cookie notice. Not dismissed by a click |
| Toast | Not captured | No action was submitted |
| Card | Captured | Channel tiles |
| List row | Partly | Footer link columns and FAQ summaries |
| Table | Not present | |
| Avatar | Not present | Signed out |
| Badge | Not captured | No badge component isolated |
| App shell | Captured | Marketing and player, desktop and phone |
| Form with validation error | Not captured | Login form was not submitted |
| Empty, loading, error | Not captured | |
| Destructive confirmation | Not present | |
| Feedback after an action | Not captured | |
| Search | Partly | Field focused. No query typed |
| Onboarding | Not captured | Signup wall. Stopped |
| Themes and widths | Captured | Dark player, light marketing, 1440 and 390 |

## Do and don't

- **Do use one purple for the primary action.** Marketing Sign up is `#a238ff`. The player and login submit use Tempo accent `#ad47ff`. See [home-desktop-default.png](screenshots/home-desktop-default.png) and [login-wall-desktop-default.png](screenshots/login-wall-desktop-default.png).
- **Do set the marketing hero in a condensed black display, uppercase.** The homepage headline is 140px Deezer Brand, weight 800, line-height 126px. See [display-hero.png](components/crops/display-hero.png).
- **Do keep the player shell black with a pale signup strip.** Signed-out Explore sits on black, with a lilac banner above the player. See [explore-desktop-default.png](screenshots/explore-desktop-default.png).
- **Don't treat the login wall as a captured signed-in app.** Email and password are empty. OAuth buttons were not used. See [login-review.json](login-review.json).
- **Do round controls.** Marketing buttons are 12px. Login fields, the login submit and search are 16px. See [search-field-default.png](components/crops/search-field-default.png).

## Rebuild

```bash
cd systems/deezer
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
```

`catalog.json` was not edited in this capture. Register the package in a follow-up that owns the catalog.
