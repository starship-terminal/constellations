# Parallel design reference

A token set and component reference for Parallel's public surface, for building pages in the style of the real site. It was read from **www.useparallel.com** on **2026-11-21**, signed out, in headless Chromium at 1440 x 900 and 390 x 844. Parallel is the hiring and job-matching product ("Find your life's work"), not parallel.ai.

Captured: the talent home, the employer marketing pages, the public job search, one job, one company, paths, companies, collections, case studies, resources, help, release notes, careers, legal pages, blog, pricing, templates, and the login and signup walls as walls only. **Boundary:** `/login` asks for email and password or LinkedIn. Signup is LinkedIn only. Employer signup asks for a name and a work email. Those branches stop. Nothing was submitted.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Parallel's site icon, 128 px PNG, fetched from `/images/logo/new-colored-png.png` |
| [site-tree.md](site-tree.md) | The control map written before screenshots: which control opens which page, menu, dialog, or wall |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the declared `--color-*`, `--font-*`, `--prll-*` and shadow values. `light` holds the roles measured on the home page. No dark set: the public site did not offer a dark toggle. Every token carries `$extensions.source`. |
| DESIGN.md | Missing on purpose. `make design-md` writes it from a catalog entry, and this capture does not edit catalog.json. |
| [style-guide.html](style-guide.html) | One page that renders the measured colours and a few controls from `tokens.json` |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | How the public pages are put together |
| [components/crops/](components/crops) | 9 focus crops from the measurement pass |
| [screenshots/](screenshots) | 86 captures, `{page}-light-{state}.png`, desktop 1440 x 900 at 1x and phone 390 x 844 at 2x, quantised to 256 colours |
| [raw/](raw) | [css-vars.json](raw/css-vars.json), [home-roles.json](raw/home-roles.json), [components-computed.json](raw/components-computed.json) |
| [tools/](tools) | The kit copy, adapted, plus `build_tokens.py`, `build_style_guide.py`, and the capture scripts |

## Brief

The generated Brief needs a catalog entry. This capture does not add one. Read [tokens.json](tokens.json) and [Do and don't](#do-and-dont) before designing in this style.

## Health

The generated Health section needs a catalog entry and a scorecard review. This capture does not add either. The coverage table below is the record of what was reached.

## How the values were read

Every value came off the running signed-out site in headless Chromium:

- **Tokens.** [tools/capture/harvest.mjs](tools/capture/harvest.mjs) reads the home page stylesheets through the CSSOM (all ten sheets were same-origin) and resolves each declared custom property in a probe document. The site declares `--color-black` `#0f0f0f`, `--color-yellow` `#eafa35`, `--color-pink` `#f54cb2`, `--color-red` `#ff2222`, `--app-background` `#fbfaf9`, `--font-family-primary` Work Sans, `--font-family-secondary` Termina, `--font-family-tertiary` Cousine, a 12-column `--prll-g-*` grid, and hard offset shadows. Results in [raw/css-vars.json](raw/css-vars.json).
- **Roles the new shell paints without a custom property.** Body background `#fbfaf9`, body text black, and the hero `h1` (Advercase Demo, 100.8px, white) are computed styles in [raw/home-roles.json](raw/home-roles.json).
- **Components.** [tools/capture/measure.mjs](tools/capture/measure.mjs) opens the main public routes and reads computed styles, plus a forced focus-visible state. Results in [raw/components-computed.json](raw/components-computed.json).
- **Screenshots.** [tools/capture/public/public.mjs](tools/capture/public/public.mjs) takes viewport and full-page shots. [tools/capture/quantize.py](tools/capture/quantize.py) posterises them to 256 colours.

Nothing was signed into, bought, or submitted. Login, signup, LinkedIn, Google, and Apple controls were not clicked past recording the wall URL. The cookie banner, where one mounted, was hidden, never answered.

## What to distrust

- **This is the public site, not Hire or the candidate app.** Matches, saved jobs, messages, profile, and Hire sit behind a login or LinkedIn wall. Treat those screens as unknown.
- **One painted theme.** No dark toggle was found. `tokens.json` has no dark set.
- **Two visual generations.** The talent home, employer pages, and job search are the new shell (warm `#fbfaf9` page, white pills, photo hero). Pricing, templates, and the older manifesto pages still paint a darker product chrome. Both were captured. Do not treat them as one theme.
- **Display face.** Advercase Demo is named in the computed `h1` stack. It is not distributed with this package. The style guide falls back to a serif.
- **Quantised screenshots.** Read colours from `tokens.json`, not from the PNGs.
- **Search field animation.** The home search types sample queries on its own. The first Explore-menu shot caught one of those queries and was recaptured with the field cleared.
- **Job and company pages are templates.** One public job and one public company (Vercel) stand for the rest. The server sitemap lists tens of thousands of the same two templates.

## Fonts

The stylesheets declare three families: **Work Sans** (`--font-family-primary`), **Termina** (`--font-family-secondary`), and **Cousine** (`--font-family-tertiary`). The hero `h1` computes to **Advercase Demo**, then a Next.js fallback, then system serif. None of these faces is committed. The style guide uses the declared Work Sans stack when the browser has it, and a serif fallback for display.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured | `core.color.*` from declared `--color-*` and `--app-background`; `light.surface.page` `#fbfaf9` and `light.text.primary` black from computed body styles |
| Type | captured | declared Work Sans, Termina, Cousine; computed Advercase Demo display at 100.8px / 114.912px line-height / -3.024px tracking |
| Spacing | captured | `--prll-gt-1` 24px, `--prll-gt-2` 48px, and the 12-column `--prll-g-*` scale from 70px to 1104px |
| Radii | not captured | no radius custom properties were declared; control radii are visible in screenshots and were not tokenised |
| Borders | captured | `--border-primary` is `2px solid #0f0f0f`; input hover and focus colours are declared |
| Elevation | captured | `--shadow-primary` `8px 8px 0 #0f0f0f`, `--shadow-secondary` `6px 6px 0 #0f0f0f` |
| Motion | not captured | no duration or easing custom properties were resolved |
| Sizing | partly | scrollbar tokens only; control heights are in the screenshots, not tokenised |
| Button, link | captured | header Sign up, Start Free, footer links, job cards |
| Text field | captured | home "Search roles"; job search field. Not submitted |
| Menu | captured | Explore menu, employer Overview menu, phone Open menu |
| Tabs | captured | Talent and Employers header tabs; Jobs and Companies on search |
| Dialog | captured | login wall and signup wall, as walls, not filled |
| Card, list row | captured | job cards on `/app/candidate/search` |
| Accordion | captured | employer FAQ, one item opened |
| Checkbox, radio, switch, select, tooltip, toast, table, avatar, badge | partly | search has a Remote Only switch and Location, Salary, Job Type, and Sort menus in [search-light-default](screenshots/search-light-default.png). No checkbox, radio, tooltip, toast, or data table was found on the public pages |
| States: default, hover, focus-visible | partly | default is in every screenshot; focus-visible was forced in the measurement pass. Hover and pressed were not separately tokenised |
| States: disabled, loading, error | not present | none on the public pages that were opened |
| Form with a validation error | not captured | no form was submitted |
| Signed-in Hire and candidate app | not captured | `/login`, `/signup`, `/employers/login`, `/employers/signup`, `/app/candidate`, `/app/hire` |
| Themes | captured | light only. Dark is not present as a toggle |
| Widths: 1440, 390 | captured | desktop and phone passes |

## Do and don't

1. **Do sit the page on warm paper.** The measured page background is `#fbfaf9`, not pure white. White is for cards and pills. See [home-light-default](screenshots/home-light-default.png).
2. **Do put the display type in white over a photograph.** The hero headline computes to 100.8px, white, tight tracking. See [home-light-default](screenshots/home-light-default.png).
3. **Do use the yellow as a small signal.** `#eafa35` shows up as a dot and an accent, not as a page fill. See the live-jobs chip on [home-light-default](screenshots/home-light-default.png).
4. **Do keep primary actions as black pills.** Sign in, Sign up, and Start Free are black or near-black rounded controls. See [login-wall-light-default](screenshots/login-wall-light-default.png).
5. **Do use the hard offset shadow on the older chrome.** `--shadow-primary` is `8px 8px 0 #0f0f0f`. The new marketing shell is flatter.
6. **Don't style Hire from this package.** The signed-in hiring product was not reached.
7. **Don't invent a dark theme.** None was offered on the captured routes.

## Rebuild

From `systems/parallel/`:

```sh
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Live recapture needs Playwright at `PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs`:

```sh
node tools/capture/harvest.mjs
node tools/capture/measure.mjs
RAW=~/.design-systems/parallel/raw-shots node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/parallel/raw-shots
```

`make design-md` and `make brief` need a catalog entry. This capture does not add one.
