# Brilliant design reference

A public refresh of the Brilliant package, read from https://brilliant.org/ on 2026-11-21, signed out. origin/main already had `systems/brilliant/`. The slug stayed `brilliant`. This pass did not open the signed-in app and did not repeat the 2026-10 lesson walk.

The marketing homepage uses `data-theme="light"`. The hero sits on oat `#F5F3F1`. Body text is black. The learner button face is `#29CC57` with a `#15B441` lip. Headlines are CoFo Robert. UI text is CoFo Brilliant. Desktop CSS viewport measured 1440 by 900 at device pixel ratio 2. Phone CSS viewport measured 390 by 844 at device pixel ratio 2.

`login_extracted` is `not-started`. catalog.json was left alone.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Brilliant mark already in the package |
| [tokens.json](tokens.json) | Public light roles read on 2026-11-21. Every token carries `$extensions.source` |
| [tokens.signed-in-2026-10.json](tokens.signed-in-2026-10.json) | The earlier signed-in token file, kept and not rebuilt |
| [DESIGN.md](DESIGN.md) | Written by hand from the public readings. `make design-md` was not run |
| [style-guide.html](style-guide.html) | Light public roles, rendered from tokens.json |
| [components.md](components.md) | Public controls that were measured |
| [patterns.md](patterns.md) | How the public nav, catalog, pricing page, and walls fit together |
| [site-tree.md](site-tree.md) | Which homepage control opens which page |
| [login-review.json](login-review.json) | Empty login and signup walls. `login_extracted` is `not-started` |
| [screenshots/public-2026-11/](screenshots/public-2026-11) | 13 public captures. 11 desktop at 2880 by 1800, 2 phone at 780 by 1688 |
| [raw/css-vars.json](raw/css-vars.json) | Public custom properties used by the builder |
| [raw/public-2026-11-21.json](raw/public-2026-11-21.json) | Viewport and component readings. The October computed dump stays in [raw/components-computed.json](raw/components-computed.json) |
| [tools/](tools) | Public builders, plus the October builders kept as `*.signed-in-2026-10.py` |

The 2026-10 signed-in crops, screenshots, and notes stay in this package. This refresh adds the public site tree and the public shots. It does not claim those older shots were retaken.

## Brief

<!-- brief:start -->
Brief is not regenerated. catalog.json was left alone, so `make brief` was not run. The public light roles are page `#FFFFFF`, hero oat `#F5F3F1`, text `#000000`, learner `#29CC57`.
<!-- brief:end -->

## Health

<!-- health:start -->
Health is not regenerated. catalog.json was left alone, so `make grade` was not run.
<!-- health:end -->

## How the values were read

Custom properties were read with `getComputedStyle(document.documentElement)` on the signed-out homepage. 705 names resolved. The builder keeps the roles that match the controls on screen. Component sizes were read with `getComputedStyle` on the h1, the hero paragraph, the learner face, the parent face, the Sign in button, and the login fields. The cookie host was hidden with CSS. Consent was not clicked. Login and signup pages were opened and left empty. Identity providers were not clicked. Forms were not submitted. Continue on the welcome screen was not clicked.

## What to distrust

Quantized screenshots are not in this refresh. The public PNGs are the browser captures. Read colours from tokens.json. The style guide falls back to Figtree and Georgia because CoFo Brilliant and CoFo Robert are not licensed for this package. Pricing prices were in SGD on this capture. A Cloudflare widget painted "Success!" on the login page without a click. That is the widget's own state, not a solved captcha. DESIGN.md was not produced by `make design-md`. The signed-in token file is the October reading and was not remeasured.

## Fonts

CoFo Robert for display headlines. CoFo Brilliant for UI text. Fallbacks in the product are `sans-serif`. Both faces are proprietary and are not in this package.

## Coverage

| Surface | Captured |
|---|---|
| Homepage, desktop | yes, [home-light-default](screenshots/public-2026-11/home-light-default.png) |
| Footer | yes, [home-dark-footer](screenshots/public-2026-11/home-dark-footer.png) |
| Topics catalog | yes |
| Pricing | yes, Subscribe now not clicked |
| Assessments, Help, About, Resources | yes |
| Login and signup walls, empty | yes |
| Welcome, first screen | yes, Continue not clicked |
| Homepage, phone | yes, 390 by 844 |
| Topics, phone | yes, 390 by 844 |
| Signed-in app | not this pass. `login_extracted` is `not-started` |
| Pressed, disabled, error | no |

## Do and don't

- **Do put the hero on oat.** The signed-out homepage sits on `#F5F3F1`. See [home-light-default](screenshots/public-2026-11/home-light-default.png).
- **Do give the learner action a green 3D face.** The face is `#29CC57` with a `#15B441` lip. The parent action is a white face with a gray lip.
- **Do keep the catalog public.** Topics lists courses without an account. See [courses-dark-default](screenshots/public-2026-11/courses-dark-default.png).
- **Don't treat this refresh as a signed-in capture.** The walls were photographed empty and left there.
- **Don't click Continue and call it a lesson.** The welcome screen is the first onboarding step. It was not continued.

## Rebuild

```bash
cd systems/brilliant && python3 tools/build_tokens.py && python3 tools/build_style_guide.py && python3 tools/build_components_md.py && python3 tools/test_brilliant.py
```

`make design-md` and `make brief` were not run. catalog.json was left alone.
