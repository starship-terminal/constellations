# Quizlet design reference

A signed-in capture of Quizlet's night web app, read from quizlet.com on 2026-11-21 in the T3 in-app preview (default profile). The account was already signed in. The page title was Your Sets. The body class was `theme-night`. Desktop CSS viewport measured 1440 by 900 at device pixel ratio 2. Phone CSS viewport measured 430 by 932 after the iphone-14-pro-max preset. A requested 390 by 844 width did not stick.

The product paints a twilight page (`#0A092D`), gray text (`#F6F7FB`), a twilight-500 pill (`#4255FF`), and a sunset-400 trial pill (`#FFCD1F`). The face is Hurme Geometric Sans 2 (`hurme_no2-webfont`), then the system sans. Cross-origin stylesheets on assets.quizlet.com were CSSOM-blocked, so the ramps are computed custom properties, not parsed rules.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Quizlet's q-twilight mark, fetched in the signed-in page and resized to 128 px |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` colour ramps, type, radius, and space, plus a `night` semantic set. No light set. Every token carries `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Written by hand for this package. `make design-md` needs a catalog.json entry, and that entry is deferred |
| [style-guide.html](style-guide.html) | One night page that renders the ramps and the two pills from tokens.json |
| [components.md](components.md) | The signed-in inventory: search, primary button, create menu, account menu |
| [patterns.md](patterns.md) | How the sidebar, library, settings, create form, and phone shell fit together |
| [login-review.json](login-review.json) | The signed-in walk: nav, settings, and create that were offered, the screens, the gaps, and what was not submitted |
| [components/crops/](components/crops) | 3 element screenshots. The account-menu crop was deleted because it showed the account email |
| [screenshots/](screenshots) | 7 night captures: 4 desktop at 2880 by 1800, 3 phone at 860 by 1864. The desktop home-with-menus shot was deleted because it showed the account email. The privacy shot was deleted because it still showed a timezone city |
| [raw/](raw) | [css-vars.json](raw/css-vars.json) and [components-computed.json](raw/components-computed.json) |
| [tools/](tools) | The kit copy, with the three builders rewritten for this product |

## Brief

<!-- brief:start -->
Brief is not generated. catalog.json has no quizlet entry, so `make brief` cannot write this section. The night roles are page `{color.twilight.900}`, text `{color.gray.200}`, accent `{color.twilight.500}`.
<!-- brief:end -->

## Health

<!-- health:start -->
Health is not generated. There is no scorecard row for quizlet, and `make grade` needs a catalog entry. That entry is deferred.
<!-- health:end -->

## How the values were read

Custom properties were read with `getComputedStyle(document.documentElement)` on the signed-in settings page. 107 names resolved. Product ramps are gray, error, lemon, lilac, mint, sherbert, sky, sunset, and twilight. Toastify names were dropped. Component sizes were read with `getComputedStyle` on the body, an h2, the search field, the primary button, the trial button, and the phone settings h1. Ad iframes were hidden with CSS. A promo banner was closed with its own Close control. Consent was not clicked. The account email was replaced in the settings DOM before those shots and painted out of the account-menu crop. The timezone city was painted out of the notifications shot.

## What to distrust

Quantized screenshots are 256-colour. Read colours from tokens.json. The style guide falls back to the system sans because Hurme Geometric Sans 2 is not licensed for this package. Light mode was not measured. The phone shots are 430 by 932, not 390 by 844. The preview tool reported 1280 by 800 while CSS `innerWidth` was 1440 and 430. DESIGN.md was not produced by `make design-md`.

## Fonts

Hurme Geometric Sans 2, served as `hurme_no2-webfont`. Fallbacks measured on the body: `-apple-system`, `system-ui`, `sans-serif`. The face is proprietary and is not in this package.

## Coverage

| Surface | Captured |
|---|---|
| Your Sets, desktop, menus open | deleted, the shot showed the account email |
| Your library, empty flashcard sets | yes |
| Settings profile, notifications | yes |
| Settings account and privacy | opened, screenshot deleted |
| Create a set, empty form | yes |
| Phone home, nav, settings | yes, at 430 by 932 |
| Light theme | no |
| Study groups, games, explanations, achievements | no |
| Hover, pressed, focus-visible | no |
| SVG icons | no |

## Do and don't

- **Do use the twilight page.** The signed-in shell sits on `#0A092D`. See [library-night-empty](screenshots/library-night-empty.png).
- **Do pill the actions.** The primary button and the trial button both use a 200px radius. See [button-primary](components/crops/button-primary.png).
- **Do keep the trial pill sunset, not twilight.** The free-trial control is `#FFCD1F` with `#282E3E` text. See [home-night-phone](screenshots/home-night-phone.png).
- **Don't invent a light theme from this package.** Light mode was offered and not switched.
- **Don't treat the phone shots as 390 wide.** They were measured at 430.

## Rebuild

```bash
cd systems/quizlet && python3 tools/build_tokens.py && python3 tools/build_style_guide.py && python3 tools/build_components_md.py
```

`make check` fails until catalog.json has a quizlet entry. That entry is deferred and is not part of this package.
