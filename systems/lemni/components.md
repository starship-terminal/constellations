# Lemni components

Public controls measured signed out on 2026-11-18. Values are token names from [tokens.json](tokens.json). Crops sit in [components/crops/](components/crops). A control the product does not ship is listed under Gaps, not invented.

## Checklist

| Component | Status | Where |
|---|---|---|
| Button | captured | `hero-continue`, `plan-cta`, `auth-continue`, `watch-video` |
| Icon button | captured | `menu-button` (44 px square, phone bar) |
| Link | captured | `nav-link`, `footer-link`, `docs-side-link` |
| Text field | captured | `email-field` on the sign-in shell |
| Text area | not present | No public textarea |
| Select | not present | No public select |
| Checkbox | not present | No public checkbox |
| Radio | not present | No public radio |
| Switch | not present | No public switch |
| Tabs | captured | `docs-tabs` (Basics, Knowledge, Agents, Actions, Inbox) |
| Menu | captured | Phone menu overlay in [screenshots/mobile-home-dark-menu-open.png](screenshots/mobile-home-dark-menu-open.png) |
| Tooltip | not present | None on the public pages |
| Dialog | not present | None opened without a submission |
| Toast | not present | None on the public pages |
| Card | captured | Pricing plan card on [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png). The home `feature-card` crop is a decorative region, not a card |
| List row | captured | Docs side list (`docs-side-link`) |
| Table | not present | No public data table |
| Avatar | not present | No public avatar |
| Badge | not present | No public badge |

Captured: 8 of 19. The other 11 are not on the signed-out surfaces.

## Shell

### Dark bar

The home bar. 1440 × 50, fill `dark.background.surface` (`rgba(13, 13, 18, 0.4)`). Labels use `core.typography.body` in `dark.text.muted`.

![Dark bar](components/crops/nav-dark-default.png)

### Light bar

Pricing, docs and the other light pages. 1440 × 50, fill `light.background.page`, padding `core.spacing.5` (20 px). Labels use `light.text.muted`.

![Light bar](components/crops/nav-light-default.png)

### Phone bar

390 × 64 on the home page, fill `dark.background.page`. The menu button is 44 × 44.

![Phone bar](components/crops/nav-mobile-default.png)

![Menu button](components/crops/menu-button-default.png)

### Nav link

15 px, `core.font.family.sans`. Dark rest `dark.text.muted`. Light rest `light.text.muted`. Hover, focus-visible and pressed were forced; the dark link does not paint a separate ring.

![Nav link](components/crops/nav-link-default.png)

### Continue (nav)

The bar's Continue label is `dark.text.link` (`#ccd1e9`), `core.font.family.sans-medium`. It points at `https://lemni.com/signup`, which redirects to the sign-in shell. It was not followed as a submit.

![Nav continue](components/crops/nav-continue-default.png)

### Footer link

There is no `<footer>` element. The link band uses `core.typography.caption` (13 px, TWK Lausanne 300). Rest `color.ink.400`. Hover lightens to `color.ink.200`.

![Footer link](components/crops/footer-link-default.png)

![Footer hover](components/crops/footer-link-hover.png)

## Home

### Display title

`core.typography.display`. 94 px, TWK Lausanne 250, computed weight 400, line-height 81.78 px, tracking -4.7 px, colour `dark.text.primary`.

![Hero title](components/crops/hero-title-default.png)

### Glass pill

The home Continue control. 138 × 40, fill `dark.background.action`, radius `core.radius.full` (140 px), label `dark.text.on-action`, shadow `core.shadow.pill` (a 1.5 px white inset plus a 3 px drop). Hover, focus-visible and pressed were forced with DevTools and were not clicked.

![Glass pill](components/crops/hero-continue-default.png)

### Watch video

145 × 40, fill `dark.background.raised`, radius `core.radius.pill` (40 px), white label. A resting control. The video was not played.

![Watch video](components/crops/watch-video-default.png)

## Pricing

### Page title

`core.typography.display-page`. 76 px, TWK Lausanne 250, tracking -3.04 px, `light.text.primary`.

![Pricing title](components/crops/pricing-title-default.png)

### Price

`core.typography.price`. 46 px, TWK Lausanne 400, tracking -1.84 px. A struck figure uses `core.color.price.struck`.

![Price](components/crops/price-default.png)

### Plan button

340 × 40, fill `light.background.action`, label `light.text.on-action`, radius `core.radius.pill`. The label points at sign-up. It was not clicked.

![Plan button](components/crops/plan-cta-default.png)

![Plan hover](components/crops/plan-cta-hover.png)

## Docs

### Section tabs

A horizontal row: Basics (current, black, hairline under), Knowledge, Agents, Actions, Inbox. The measured cell is 168 × 40, `core.typography.body`, `light.text.primary`.

![Docs tabs](components/crops/docs-tabs-default.png)

### Side link

Overview and the other page names in the left list. 13 px, TWK Lausanne 300, rest `light.text.muted`, hover `#646465` (`color.ink.500`).

![Docs side link](components/crops/docs-side-link-default.png)

![Docs side hover](components/crops/docs-side-link-hover.png)

## Sign-in shell

Resting page only. Continue and Continue with Google were not clicked. The email field was filled with `visitor@example.com` and then cleared.

### Title

`core.typography.auth-title`. system-ui 32 px / 500, tracking -0.32 px, black.

![Auth title](components/crops/auth-title-default.png)

### Google button

360 × 44, radius `core.radius.md` (12 px). Hover shifts the label toward `rgba(0, 0, 0, 0.6)`. Pressed shrinks the box to about 356 × 44. Not clicked.

![Google button](components/crops/google-button-default.png)

### Email field

360 × 44, fill `light.background.field`, radius `core.radius.md`, shadow `core.shadow.field`.

![Email field](components/crops/email-field-default.png)

![Email filled](components/crops/email-field-filled.png)

### Continue

360 × 44, black fill, radius `core.radius.md`. The label's computed colour is `color.ink.500`, not white. The crop is the source for that reading. Not clicked.

![Auth continue](components/crops/auth-continue-default.png)

## Shared

Focus-visible was forced on the interactive controls. The marketing bar does not paint a separate focus ring; the current light item is black (`light.border.focus`). Pressed on the Google button is a slight shrink. Other pressed states do not restyle.

Motion lives in `core.motion`. The home `dots` loop (1 s, infinite, transform) keeps running under reduced motion. See [raw/motion.json](raw/motion.json).

## Gaps

- Wordmark: the logo crop missed. The mark is in [screenshots/home-dark-default.png](screenshots/home-dark-default.png) and [icon.png](icon.png).
- `footer` as an element: the site has no `<footer>`. Use `footer-link`.
- `docs-link` for the word Agents: the section row is `docs-tabs`. Agents as its own page was not screenshotted.
- `feature-card` matched a large decorative region. Do not treat that crop as a card spec.
- Text area, select, checkbox, radio, switch, tooltip, dialog, toast, table, avatar, badge: not on the public pages.
- Disabled, loading, error and selected states: not shown signed out.
- Authenticated agent builder, knowledge, actions, inbox, workplace and billing: behind sign-in. Recorded in the catalog gaps, not captured.
