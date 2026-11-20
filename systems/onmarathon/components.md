# Components

Public controls on the Marathon archive, measured in headless Chromium on 2026-11-21. Crops are in [components/crops/](components/crops). Values are the computed style of the named element. A colour that matches a token names that token.

The product is an archive. Sign In and Get Started redirect to the homepage and were measured, not followed.

## Shell

### Archive banner

Lime strip, 1440 by 44px at desktop, 13.2px Inter medium, text `light.accentText`. Fill is `light.accent` (`#d7fd51`). It links off-site. Hover and pressed do not change the fill. Keyboard focus draws a 1px auto outline `#005fcc` at 1px offset.

![Archive banner](components/crops/banner-default.png)

### Wordmark

Homepage link, Inter 17.6px, colour `light.text`. Crop: [wordmark-default.png](components/crops/wordmark-default.png). Hover, focus and pressed were not remeasured after the first locator missed the banner's "Marathon" text. Gap.

### Nav link

"For Agencies", 15.4px / 22px, weight 500. Resting colour `light.muted`. Hover and the CDP pressed state move the colour to `light.text`. Focus draws the same `#005fcc` ring and leaves the resting colour.

![Nav link](components/crops/nav-link-default.png)

### Sign in

Same type as the nav link, 50 by 22px. Following the link redirects to the homepage with no form. Measured only.

![Sign in](components/crops/sign-in-default.png)

### Primary button

"Get Started", 110 by 40px, radius 9999px, horizontal padding 13.2px. Fill `light.button`, label `light.onAccent`. Hover and CDP pressed fill `#404040` (`light.buttonHover`). Focus keeps the resting fill and adds the `#005fcc` ring. Following the link redirects to the homepage with no signup form.

![Primary button](components/crops/button-primary-default.png)

### Display heading

Homepage h1, graphik 81.4px / 81.4px, weight 500, colour `light.text`.

![Display heading](components/crops/heading-default.png)

## Pricing

### Billing toggle

Two pills inside a rounded track. Selected half ("Pay Annually" on load) is a black pill, white label, 140 by 40px, radius 9999px. Idle half is transparent, colour `light.muted`, hover colour `light.text`. Clicking Pay Monthly is a local price change ($49 to $59 on Pro). No form.

![Selected billing half](components/crops/billing-selected-default.png)

### Popular badge

Black pill, white 13.2px label, padding 2.2px 8.8px, radius 9999px. Sits on the Pro card.

![Popular badge](components/crops/badge-default.png)

### Plan cards

Free is white, 560 by 526px, radius 17.6px, padding 44px. Pro is the same size and radius with fill `#d7fd51` (`light.accent`). No shadow.

![Free plan](components/crops/plan-card-default.png)

![Pro plan](components/crops/plan-card-pro-default.png)

## Error page

### Return home

The only control on `/changelog` (404). Black pill, 172 by 48px, radius 9999px, 17.6px medium label. Hover and CDP pressed do not change the fill. Transition is opacity 0.15s, not the colour transition used by Get Started.

![Return home](components/crops/button-return-default.png)

## Phone (390)

### Menu button

Round 40px icon button, labelled "Open menu". Hidden at 1440. Hover and CDP pressed fill `rgba(0, 0, 0, 0.05)`. Keyboard focus on this phone capture drew an orange auto outline `rgb(229, 151, 0)`, not the desktop `#005fcc` ring. Both readings are kept. The phone ring is the browser's mobile focus colour, not a site token.

![Menu button](components/crops/menu-button-default.png)

### Phone menu

Opened panel, 390 by 348px, padding 17.6px 26.4px. Links: Product, For Agencies, Pricing, Sign In, Get Started. Close control is a 40px round button labelled "Close menu", same hover fill as Open menu.

![Phone menu](components/crops/menu-panel-opened.png)

## Shared values

| Role | Value | Where |
|---|---|---|
| Page | `#ffffff` | `html.light --background` |
| Text | `#0b0b0b` | `--foreground`, h1, wordmark |
| Muted text | `#717171` | `--muted-foreground`, resting links |
| Accent | `#d7fd51` | `--primary`, banner, Pro card |
| Button | `#0b0b0b` | Get Started, selected billing half, badge |
| Button hover | `#404040` | Get Started hover |
| Radius, card | `17.6px` | `--radius` (1rem at 110% root) |
| Radius, control | `9999px` | buttons, toggle, badge, menu button |
| Motion | `150ms cubic-bezier(0.4, 0, 0.2, 1)` | links and Get Started |

## Gaps

- No text field, text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table or avatar on the public pages.
- Sign In and Register redirect to the homepage. No login or signup form was captured.
- The SavvyCal iframe on `/demo` is a booking form. It was not filled. Its resting shell is in the demo screenshot only.
- Destructive colour is declared (`--destructive`) and not painted on a captured control.
- Disabled, loading and error states of controls are not present.
- Wordmark hover, focus and pressed were not captured.
- Dark theme is a CSS class with no public switch. Values sit on tokens as `darkProbe`, labelled Not a live theme.
- Choc Chip cookie CSS is linked and was not readable from the CSSOM. No banner mounted, so it was not clicked. Its colours are not tokens.
- The footer studio line is not a control. It is not a token and is not copied into the package.
