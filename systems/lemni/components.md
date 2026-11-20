# Lemni components

Public and signed-in free controls measured on 2026-11-18. Values are token names from [tokens.json](tokens.json). Crops sit in [components/crops/](components/crops). A control the product does not ship is listed under Gaps, not invented.

## Checklist

| Component | Status | Where |
|---|---|---|
| Button | captured | `hero-continue`, `plan-cta`, `auth-continue`, `watch-video` |
| Icon button | captured | `menu-button` (44 px square, phone bar) |
| Link | captured | `nav-link`, `footer-link`, `docs-side-link` |
| Text field | captured | `email-field` on the sign-in shell. App invite and name fields |
| Text area | not present | No textarea on the captured pages |
| Select | captured | Editor role select on the workplace invite row. Screenshot only, not cropped |
| Checkbox | not present | No checkbox on the captured pages |
| Radio | not present | No radio on the captured pages |
| Switch | captured | Plan feature toggles on `/welcome/subscribe`, resting off. Screenshot only, not cropped |
| Tabs | captured | `docs-tabs` (Basics, Knowledge, Agents, Actions, Inbox). Workplace settings uses a vertical tab list (Members, Details, Connections, Usage, Plan, About) |
| Menu | captured | Phone menu overlay in [screenshots/mobile-home-dark-menu-open.png](screenshots/mobile-home-dark-menu-open.png). Workplace nav on phone in [screenshots/mobile-app-inbox-light-nav-open.png](screenshots/mobile-app-inbox-light-nav-open.png) |
| Tooltip | not present | None on the captured pages |
| Dialog | captured | Workplace members and Account dialogs. Overlay `light.background.overlay` |
| Toast | captured | Reconnecting pill on the inbox. Crop missed the pill; the screenshot is the evidence |
| Card | captured | Pricing plan card on [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png). Action store cards on [screenshots/app-actions-light-default.png](screenshots/app-actions-light-default.png) |
| List row | captured | Docs side list (`docs-side-link`). Agent rows and knowledge datasets in the app |
| Table | not present | No data table on the captured pages |
| Avatar | captured | Sidebar initial M, member avatar in the workplace dialog |
| Badge | captured | Disabled on stock agents. Owner on the member row |

Captured: 14 of 19. Text area, checkbox, radio, tooltip and table were not on the free product.

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

## Workplace app

The signed-in product is a separate React app on `lemni.com`, system-ui, light ground `#f6f6f8`, a 260 px sidebar `#f1f3f4`. App buttons are 28 px tall, 8 px radius (`core.radius.sm`), black fill. Fields are 28 px, fill `light.background.field`. Upgrade was measured and never pressed.

![Inbox](screenshots/app-inbox-light-default.png)

![Agents](screenshots/app-agents-light-default.png)

![Knowledge](screenshots/app-knowledge-light-default.png)

![Actions](screenshots/app-actions-light-default.png)

### Sidebar Upgrade

219 × 28, black, radius `core.radius.sm`, white 13 px system-ui. Not followed.

![Upgrade](components/crops/app-upgrade-default.png)

### Enable Agent

299 × 28, same recipe. Not pressed.

![Enable Agent](components/crops/app-enable-default.png)

### Invite field

461 × 28, fill `light.background.field`, radius `core.radius.sm`. Invite was not pressed.

![Invite field](components/crops/app-invite-field-default.png)

### Workplace dialog

Members dialog over `light.background.overlay` (`rgba(255, 255, 255, 0.8)`).

![Workplace settings](screenshots/app-workspace-settings-light-default.png)

![Account](screenshots/app-profile-light-default.png)

### Empty inbox

"No threads todo" in `color.ink.300`.

![Empty](components/crops/app-empty-default.png)

## Shared

Focus-visible was forced on the interactive controls. The marketing bar does not paint a separate focus ring; the current light item is black (`light.border.focus`). Pressed on the Google button is a slight shrink. Other pressed states do not restyle.

Motion lives in `core.motion`. The home `dots` loop (1 s, infinite, transform) keeps running under reduced motion. See [raw/motion.json](raw/motion.json).

## Gaps

- Wordmark: the logo crop missed. The mark is in [screenshots/home-dark-default.png](screenshots/home-dark-default.png) and [icon.png](icon.png).
- `footer` as an element: the site has no `<footer>`. Use `footer-link`.
- `docs-link` for the word Agents: the section row is `docs-tabs`. Agents as its own page was not screenshotted.
- `feature-card` matched a large decorative region. Do not treat that crop as a card spec.
- Text area, checkbox, radio, tooltip, table: not on the captured pages.
- Select (Editor) and switch (plan feature toggles) appear in screenshots and were not cropped.
- Error and destructive confirm: not shown on the free product.
- Billing checkout: `/welcome/subscribe` Upgrade was not pressed.
- Toast, dialog and member-row crops matched the page root. Use the full screenshots.
