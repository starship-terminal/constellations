# Lemni components

Public controls measured on 2026-11-21. Values are token names from [tokens.json](tokens.json). Crops sit in [components/crops/](components/crops). A control the public site does not ship is listed under Gaps, not invented. The workplace app was not entered.

## Checklist

| Component | Status | Where |
|---|---|---|
| Button | captured | `hero-continue`, `plan-cta`, `auth-continue`, `watch-video` |
| Icon button | captured | `menu-button` (44 px square, phone bar) |
| Link | captured | `nav-link`, `footer-link`, `docs-side-link` |
| Text field | captured | `email-field` on the sign-in shell, empty |
| Text area | not present | No textarea on the captured public pages |
| Select | not captured | The role select sits on `/company/apply`. The form was left empty and the select was not opened |
| Checkbox | not present | No checkbox on the captured public pages |
| Radio | not present | No radio on the captured public pages |
| Switch | not present | No switch on the captured public pages |
| Tabs | captured | `docs-tabs` (Basics, Knowledge, Agents, Actions, Inbox). The labels are links |
| Menu | captured | Phone menu overlay in [screenshots/mobile-home-dark-menu-open.png](screenshots/mobile-home-dark-menu-open.png) |
| Tooltip | not present | None on the captured public pages |
| Dialog | partly | Watch Video opens a YouTube embed on the home page. Opened and closed. Not cropped |
| Toast | not present | None on the captured public pages |
| Card | captured | Pricing plan card on [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) |
| List row | captured | Docs side list (`docs-side-link`) |
| Table | not present | No data table on the captured public pages |
| Avatar | not present | None on the captured public pages |
| Badge | not present | None on the captured public pages |

Captured on the public site: button, icon button, link, text field, tabs, menu, card, list row. Dialog is the video overlay only. Text area, checkbox, radio, switch, tooltip, toast, table, avatar and badge are not on these pages.

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

Resting page only. Continue and Continue with Google were not clicked. The email field was photographed empty. Nothing was typed.

### Title

`core.typography.auth-title`. system-ui 32 px / 500, tracking -0.32 px, black.

![Auth title](components/crops/auth-title-default.png)

### Google button

360 × 44, radius `core.radius.md` (12 px). Hover shifts the label toward `rgba(0, 0, 0, 0.6)`. Pressed shrinks the box to about 356 × 44. Not clicked.

![Google button](components/crops/google-button-default.png)

### Email field

360 × 44, fill `light.background.field`, radius `core.radius.md`, shadow `core.shadow.field`.

![Email field](components/crops/email-field-default.png)

### Continue

360 × 44, black fill, radius `core.radius.md`. The label's computed colour is `color.ink.500`, not white. The crop is the source for that reading. Not clicked.

![Auth continue](components/crops/auth-continue-default.png)

## Workplace app

Not captured. The sign-in wall was photographed empty and not submitted. `login-extracted` stays not-started.

## Shared

Focus-visible was forced on the interactive controls. The marketing bar does not paint a separate focus ring; the current light item is black (`light.border.focus`). Pressed on the Google button is a slight shrink. Other pressed states do not restyle.

Motion lives in `core.motion`. The home `dots` loop (1 s, infinite, transform) keeps running under reduced motion. See [raw/motion.json](raw/motion.json).

## Gaps

- Wordmark: the logo locator matched two nodes and the crop was dropped. The mark is in [screenshots/home-dark-default.png](screenshots/home-dark-default.png) and [icon.png](icon.png).
- `footer` as an element: the site has no `<footer>`. Use `footer-link`.
- `docs-link` is the Agents section link. The agents page itself was mapped and not screenshotted.
- `feature-card` matched a large decorative region. Do not treat that crop as a card spec.
- Text area, checkbox, radio, switch, tooltip, toast, table, avatar and badge: not on the captured public pages.
- Select sits on the apply form and was not opened.
- Error and destructive confirm: not shown.
- Billing checkout and the workplace app: behind the sign-in wall. Not entered.
