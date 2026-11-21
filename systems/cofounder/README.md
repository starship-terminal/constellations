# Cofounder design reference

A measured reference for Cofounder's public marketing site at https://cofounder.co, plus the signed-out login wall at https://app.cofounder.co/os/login. Captured on 2026-11-21, signed out, in headless Chromium at 1440×900 and 390×844. The signed-in product was not entered. Google, GitHub and Email were not clicked.

The site paints one light theme: warm paper `#f5f5f2`, near-black text `#171717`, Neoris for UI type, and a full-bleed pixel illustration behind the hero. Primary actions are white 41px pills with an 8px radius. There is no named colour scale in the marketing CSS. Tailwind declares a few theme variables (`--color-lime-200`, radii, easings). Those are labelled declared.

This package is not registered in catalog.json. The capture task forbade that edit.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, resized from the favicon to 128px |
| [tokens.json](tokens.json) | Measured colours, type, radii and a few declared Tailwind variables. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Written for this package. Not generated, because the package is not in catalog.json. |
| [style-guide.html](style-guide.html) | Renders the measured page colour, text, focus, and the two hero controls. Neoris is not loaded. |
| [components.md](components.md) | Controls that were measured, and the ones the public site does not have |
| [patterns.md](patterns.md) | Shell, primary action, capability dialog, pricing, login wall |
| [site-tree.md](site-tree.md) | Every public control and the page or overlay it opens |
| [login-review.json](login-review.json) | What the login wall shows. Email field: none. Providers not clicked. |
| [components/crops/](components/crops) | Five crops from the raw captures |
| [screenshots/](screenshots) | Quantised page captures, desktop and phone |
| [raw/](raw) | Computed-style readings and declared custom properties |
| [tools/](tools) | Kit copy plus a check script that does not rewrite tokens |

## Brief

Read [tokens.json](tokens.json) before using a value. Screenshots are 256-colour PNGs.

The page is warm paper `#f5f5f2`. Text is `#171717`. The header CTA is a white pill, 41px tall, 8px radius. Hero type is Neoris at 46px, weight 400. Focus on a nav link is `#005fcc`.

## Health

Not graded. catalog.json was not edited, so `make grade` cannot see this package.

## How the values were read

Computed styles on https://cofounder.co/ in headless Chromium: body, header, nav link, header CTA, hero `h1`, Copy Setup Prompt, a capability button, the capability dialog, and a pricing FAQ row. Custom properties were listed from the same-origin stylesheets. The login wall was photographed and its controls counted. The Google button fill was sampled from the raw screenshot, not from CSS, and the token says so.

Nothing was submitted. Identity buttons were not clicked. Copy Setup Prompt was clicked. It stays on the page.

## What to distrust

- **No named palette.** Most colours are computed styles, not custom properties. Do not treat Tailwind's `--color-lime-*` as the brand accent. They are declared and were not seen as a control fill.
- **Muted text is Not captured.** No secondary text colour was isolated. It is not in the token file.
- **Login button colours are sampled**, except where a computed style was read. The Google hover and focus readings were taken without clicking.
- **Dialog fill is translucent.** `rgba(247, 247, 243, 0.68)` plus a backdrop. A flattened hex would be wrong.
- **Screenshots are quantised.** Read colours from tokens.json or raw/.
- **Neoris is not in the repo.** The guide uses a system fallback.
- **Docs dark mode was not measured.**

## Fonts

Neoris (and a fallback of the same name) is the UI face, loaded by the site. IBM Plex Mono, departureMono and Inter are declared. Licences were not captured. The webfonts are not in this package.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured, with gaps | page, text, surface, focus in [tokens.json](tokens.json). Muted and a painted border are Not captured. |
| Type | captured | hero, body, nav, control |
| Spacing | captured | header 91px, controls 41px and 47px, FAQ row 68px |
| Radii | captured | 8px, 10px, 16px, plus declared Tailwind steps |
| Borders | not captured | header border is transparent on the hero |
| Elevation | captured | dialog shadow |
| Motion | captured | nav 200ms ease-in-out. Other durations Not captured. |
| Sizing, layout | captured | 1440 and 390 |
| Button | captured | header CTA, copy, capability, login |
| Icon button | captured | phone menu open/close |
| Link | captured | nav and footer |
| Text field | not present | no field on marketing pages or the first login screen |
| Text area, select, checkbox, radio, switch | not present | public marketing surface |
| Tabs | captured | home workflow tabs, pressed only |
| Menu | captured | phone overlay |
| Tooltip | not present | none appeared |
| Dialog | captured | capability details |
| Toast | not present | copy showed none |
| Card | observed | resources and chapters. Values not isolated. |
| List row | captured | capability buttons and FAQ rows |
| Table | not present | |
| Avatar, badge | not present | |
| App shell | captured | [patterns.md](patterns.md) |
| Form with error | not present | no form was shown, and none was submitted |
| Empty, loading, error | not captured | signed-in product |
| Destructive confirmation | not present | |
| Feedback after an action | not present | copy produced no toast |
| Search | not present | on the marketing site. Docs have search. Not measured. |
| List or table | captured as lists | resources index, FAQ |
| Onboarding | not captured | behind the login wall. Not filled. |
| Dark theme | not present | on the marketing site |
| Phone width | captured | 390 |

## Do and don't

- **Do** ground marketing pages on `#f5f5f2` and set UI type in Neoris. [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png)
- **Do** make the primary action a white 41px pill with an 8px radius. [components/crops/nav-cta-default.png](components/crops/nav-cta-default.png)
- **Do** open capability details in a 16px dialog rather than a new page. [screenshots/home-light-capability-dialog.png](screenshots/home-light-capability-dialog.png)
- **Don't** invent an email field on the first login screen. The wall offers Google, GitHub and Email, and Email is a button. [screenshots/login-light-default.png](screenshots/login-light-default.png)
- **Don't** treat declared lime tokens as the accent. The measured actions are black and white.
- **Don't** follow "Run a company" and design the signed-in app from memory. That path is the login wall.

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks sources. It does not rewrite tokens.json. style-guide.html is hand-written from the same readings because the kit builder expects a catalog entry this package does not have.
