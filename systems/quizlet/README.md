# Quizlet design reference

A public refresh of the Quizlet package, read from https://quizlet.com/ on 2026-11-21, signed out. origin/main already had `systems/quizlet/`. The slug stayed `quizlet`. This pass did not open the signed-in app and did not repeat the earlier night walk.

The marketing page uses body class `theme-default`. Page background `{color.gray.200}` (`#F6F7FB`), body text `{color.gray.800}` (`#282E3E`), twilight-500 pills (`#4255FF`), and a sunset-400 trial pill (`#FFCD1F`) on the public upgrade page. The face is Hurme Geometric Sans 2 (`hurme_no2-webfont`), then the system sans. Desktop CSS viewport measured 1440 by 900 at device pixel ratio 2. Phone CSS viewport measured 390 by 844 at device pixel ratio 2.

`login_extracted` is `not-started`. catalog.json was left alone.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Quizlet's q-twilight mark, already in the package, resized to 128 px |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` ramps, type, radius, and size, plus `light` and `night` semantic sets. Every token carries `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Written by hand from the public readings. `make design-md` was not run |
| [style-guide.html](style-guide.html) | Light roles, ramps, and the prior night roles, rendered from tokens.json |
| [components.md](components.md) | Public controls that were measured: Log in, Sign up, search, trial |
| [patterns.md](patterns.md) | How the public header, menus, footer, pricing page, and phone drawer fit together |
| [site-tree.md](site-tree.md) | Which homepage control opens which page, menu, or dialog |
| [login-review.json](login-review.json) | Empty login and signup walls. `login_extracted` is `not-started` |
| [components/crops/](components/crops) | 3 element screenshots: Log in, Sign up, search field |
| [screenshots/](screenshots) | 12 public captures. 10 desktop at 2880 by 1800, 2 phone at 780 by 1688 |
| [raw/](raw) | Public custom properties, the prior night copy, and computed component styles |
| [tools/](tools) | Builders rewritten for the public readings |

## Brief

<!-- brief:start -->
Brief is not regenerated. catalog.json was left alone, so `make brief` was not run. The public light roles are page `{color.gray.200}`, text `{color.gray.800}`, accent `{color.twilight.500}`.
<!-- brief:end -->

## Health

<!-- health:start -->
Health is not regenerated. catalog.json was left alone, so `make grade` was not run.
<!-- health:end -->

## How the values were read

Custom properties were read with `getComputedStyle(document.documentElement)` on the signed-out homepage. 51 product ramp names resolved. Cross-origin stylesheets on assets.quizlet.com were CSSOM-blocked, so the ramps are computed custom properties. Component sizes were read with `getComputedStyle` on the body, the h1, the Log in pill, the Sign up pill, the teacher link, the search field, and the upgrade trial button. The cookie host was hidden with CSS. Consent was not clicked. Login and signup dialogs were opened and left empty. Identity providers were not clicked. Forms were not submitted.

## What to distrust

Quantized screenshots are 256-colour. Read colours from tokens.json. The style guide falls back to the system sans because Hurme Geometric Sans 2 is not licensed for this package. The homepage h1 computed as `rgb(0, 0, 0)`, which is not a ramp step. `light.text-strong` aliases gray-900 as the nearest ramp and says so. The night set is the prior signed-in reading. This pass did not re-open that shell, and the night screenshots are not in this refresh. `emulateMedia` dark did not switch the public theme. Focus rings were not observed as painted outlines. DESIGN.md was not produced by `make design-md`.

## Fonts

Hurme Geometric Sans 2, served as `hurme_no2-webfont`. Fallbacks measured on the body: `-apple-system`, `system-ui`, `sans-serif`. The face is proprietary and is not in this package.

## Coverage

| Surface | Captured |
|---|---|
| Homepage, desktop | yes, [home-light-default](screenshots/home-light-default.png) |
| Nav menus | yes, Study tools clean. Subjects and Create still show the earlier menus |
| Footer | yes |
| Flashcards marketing | yes |
| Pricing | yes, trial not started |
| Login and signup walls, empty | yes |
| Homepage, phone, and phone drawer | yes, 390 by 844 |
| Public study set | no, a later navigation hit Press and Hold |
| Teachers, Learn, explanations | no, captcha, shots discarded |
| Phone inner page | no, captcha, shot discarded |
| Signed-in app | not this pass. `login_extracted` is `not-started` |
| Pressed, disabled, error, SVG icons | no |

## Do and don't

- **Do use the gray page on marketing.** The signed-out shell sits on `#F6F7FB`. See [home-light-default](screenshots/home-light-default.png).
- **Do pill the actions.** Log in, Sign up, and the trial button all use a 200px radius. See [button-login-default](components/crops/button-login-default.png).
- **Do keep the trial pill sunset, even on the dark upgrade page.** The control is `#FFCD1F` with `#282E3E` text. See [pricing-light-default](screenshots/pricing-light-default.png).
- **Don't treat this refresh as a signed-in capture.** The walls were photographed empty and left there.
- **Don't invent a public study-set screenshot.** That navigation hit a captcha and was stopped.

## Rebuild

```bash
cd systems/quizlet && python3 tools/build_tokens.py && python3 tools/build_style_guide.py && python3 tools/build_components_md.py && python3 tools/test_quizlet.py
```

`make design-md` and `make brief` were not run. catalog.json was left alone.
