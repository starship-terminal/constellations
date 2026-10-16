# Brilliant components

Token-based specs for every component on the coverage checklist, measured on 2026-10-17 in the signed-in app (free account) in both themes, then the 2026-09-25 discovery list, product-specific components and icon index. Every value in the specs is the token in [tokens.json](tokens.json) that holds it for that theme; hover, focus-visible and pressed were forced on the element with the DevTools protocol, so they are the browser's own computed styles. The raw readings are in [raw/components-computed.json](raw/components-computed.json); crops of every state that changed something are in [components/crops/2026-10/](components/crops/2026-10).

Read a row as: what changes from the default in that state. "browser default ring" means the product sets no focus style there, so Chrome draws its own.

## Component specs (2026-10)

557 of 563 values in these specs are named by a token; the 6 others are printed raw and marked "no token".

16 of 19 checklist components are captured; select and checkbox are not present, and toast was never fired.

### Button

The 3D button (`data-slot=button3d`: a face lifted 4px over a same-hue lip) is the main action; flat buttons (`data-slot=button`) do everything else. Sizes: `size.control-md` for main and flat buttons, `size.control-sm` for outline buttons inside settings rows.

**button3d-blue** (Start; `[data-slot=button3d]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | size `size.control-md` high; radius `radius.button3d`; face: fill `bg.blue-primary`; face: text `text.primary`; face: shadow lip 0 4px 0 in `border.select`; face: size `size.control-md` high; face: radius `radius.button3d-face`; face: padding `spacing.3.5` `spacing.6`; face: type `typography.ui.actions.base` | size `size.control-md` high; radius `radius.button3d`; face: fill `bg.blue-primary`; face: text `text.inverse`; face: shadow lip 0 4px 0 in `border.blue-bold`; face: size `size.control-md` high; face: radius `radius.button3d-face`; face: padding `spacing.3.5` `spacing.6`; face: type `typography.ui.actions.base` | [dark](components/crops/2026-10/button3d-blue-dark-default.png) [light](components/crops/2026-10/button3d-blue-light-default.png) |
| hover | opacity `opacity.hover-premium` | opacity `opacity.hover-premium` | [dark](components/crops/2026-10/button3d-blue-dark-hover.png) [light](components/crops/2026-10/button3d-blue-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/button3d-blue-dark-focus-visible.png) [light](components/crops/2026-10/button3d-blue-light-focus-visible.png) |
| pressed | opacity `opacity.hover-premium`; face: shadow none; face: transform none (face drops onto its lip) | opacity `opacity.hover-premium`; face: shadow none; face: transform none (face drops onto its lip) | [dark](components/crops/2026-10/button3d-blue-dark-active.png) [light](components/crops/2026-10/button3d-blue-light-active.png) |

**button3d-neutral** (Keep learning; `[data-slot=modal-content] [data-slot=button3d]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | size `size.control-md` high; radius `radius.button3d`; face: fill `bg.inverse-secondary`; face: text `text.inverse`; face: shadow lip 0 4px 0 in `border.gray-bold`; face: size `size.control-md` high; face: radius `radius.button3d-face`; face: padding `spacing.3.5` `spacing.6`; face: type `typography.ui.actions.base` | size `size.control-md` high; radius `radius.button3d`; face: fill `bg.inverse-secondary`; face: text `text.inverse`; face: shadow lip 0 4px 0 in `border.active`; face: size `size.control-md` high; face: radius `radius.button3d-face`; face: padding `spacing.3.5` `spacing.6`; face: type `typography.ui.actions.base` | [dark](components/crops/2026-10/button3d-neutral-dark-default.png) [light](components/crops/2026-10/button3d-neutral-light-default.png) |
| hover | opacity `opacity.hover-premium` | opacity `opacity.hover-premium` | [dark](components/crops/2026-10/button3d-neutral-dark-hover.png) [light](components/crops/2026-10/button3d-neutral-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/button3d-neutral-dark-focus-visible.png) [light](components/crops/2026-10/button3d-neutral-light-focus-visible.png) |
| pressed | opacity `opacity.hover-premium`; face: shadow none; face: transform none (face drops onto its lip) | opacity `opacity.hover-premium`; face: shadow none; face: transform none (face drops onto its lip) | [dark](components/crops/2026-10/button3d-neutral-dark-active.png) [light](components/crops/2026-10/button3d-neutral-light-active.png) |

**button3d-disabled** (Check; `[data-slot=button3d][data-disabled]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | size `size.control-md` high; radius `radius.button3d`; face: fill `bg.disabled`; face: text `text.disabled`; face: shadow none; face: size `size.control-md` high; face: radius `radius.button3d-face`; face: padding `spacing.3.5` `spacing.6`; face: type `typography.ui.actions.base` | size `size.control-md` high; radius `radius.button3d`; face: fill `bg.alpha`; face: text `text.disabled`; face: shadow none; face: size `size.control-md` high; face: radius `radius.button3d-face`; face: padding `spacing.3.5` `spacing.6`; face: type `typography.ui.actions.base` | [dark](components/crops/2026-10/button3d-disabled-dark-default.png) [light](components/crops/2026-10/button3d-disabled-light-default.png) |

**button-inverse** (Add another email; `[data-slot=button]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.inverse-primary`; text `text.inverse`; border `borderWidth.default` transparent; shadow none; size `size.control-md` high; radius `radius.button`; padding `spacing.3` `spacing.5.5`; type `typography.ui.actions.base` | fill `bg.table-header`; text `text.inverse`; border `borderWidth.default` transparent; shadow none; size `size.control-md` high; radius `radius.button`; padding `spacing.3` `spacing.5.5`; type `typography.ui.actions.base` | [dark](components/crops/2026-10/button-inverse-dark-default.png) [light](components/crops/2026-10/button-inverse-light-default.png) |
| hover | opacity `opacity.hover-flat-button` | opacity `opacity.hover-flat-button` | [dark](components/crops/2026-10/button-inverse-dark-hover.png) [light](components/crops/2026-10/button-inverse-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/button-inverse-dark-focus-visible.png) [light](components/crops/2026-10/button-inverse-light-focus-visible.png) |
| pressed | opacity `opacity.pressed-flat-button` | opacity `opacity.pressed-flat-button` | [dark](components/crops/2026-10/button-inverse-dark-active.png) [light](components/crops/2026-10/button-inverse-light-active.png) |

**button-outline** (Send verification; `[data-slot=button]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.primary`; border `borderWidth.default` `border.primary`; shadow none; size `size.control-sm` high; radius `radius.button`; padding `spacing.2` `spacing.3.5`; type `typography.ui.actions.base` | text `text.primary`; border `borderWidth.default` `border.primary`; shadow none; size `size.control-sm` high; radius `radius.button`; padding `spacing.2` `spacing.3.5`; type `typography.ui.actions.base` | [dark](components/crops/2026-10/button-outline-dark-default.png) [light](components/crops/2026-10/button-outline-light-default.png) |
| hover | border `borderWidth.default` `border.hover` | border `borderWidth.default` `border.hover` | [dark](components/crops/2026-10/button-outline-dark-hover.png) [light](components/crops/2026-10/button-outline-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/button-outline-dark-focus-visible.png) [light](components/crops/2026-10/button-outline-light-focus-visible.png) |
| pressed | fill `bg.active`; border `borderWidth.default` `border.hover` | fill `bg.active`; border `borderWidth.default` `border.hover` | [dark](components/crops/2026-10/button-outline-dark-active.png) [light](components/crops/2026-10/button-outline-light-active.png) |

**button-danger-text** (Quit; `[data-slot=modal-content] [data-slot=button]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.red-primary`; border `borderWidth.default` transparent; shadow none; size `size.control-md` high; radius `radius.button`; padding `spacing.3` `spacing.5.5`; type `typography.ui.actions.base` | text `text.red-primary`; border `borderWidth.default` transparent; shadow none; size `size.control-md` high; radius `radius.button`; padding `spacing.3` `spacing.5.5`; type `typography.ui.actions.base` | [dark](components/crops/2026-10/button-danger-text-dark-default.png) [light](components/crops/2026-10/button-danger-text-light-default.png) |
| hover | fill `bg.red-tertiary` | fill `bg.red-tertiary` | [dark](components/crops/2026-10/button-danger-text-dark-hover.png) [light](components/crops/2026-10/button-danger-text-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/button-danger-text-dark-focus-visible.png) [light](components/crops/2026-10/button-danger-text-light-focus-visible.png) |
| pressed | fill `bg.danger-secondary-active` | fill `bg.red-secondary` | [dark](components/crops/2026-10/button-danger-text-dark-active.png) [light](components/crops/2026-10/button-danger-text-light-active.png) |

**button-disabled** (Update personal info; `[data-slot=button][data-disabled]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.disabled`; text `text.disabled`; border `borderWidth.default` transparent; shadow none; size `size.control-md` high; radius `radius.button`; padding `spacing.3` `spacing.5.5`; type `typography.ui.actions.base` | fill `bg.alpha`; text `text.disabled`; border `borderWidth.default` transparent; shadow none; size `size.control-md` high; radius `radius.button`; padding `spacing.3` `spacing.5.5`; type `typography.ui.actions.base` | [dark](components/crops/2026-10/button-disabled-dark-default.png) [light](components/crops/2026-10/button-disabled-light-default.png) |

**premium-button** (Go Premium; `[data-slot=premium-button]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill gradient (see crop); text `text.primary`; border `borderWidth.default` transparent; shadow none; size `size.premium-button` high; radius `radius.full`; padding `spacing.2` `spacing.4`; type 14px/21px 500 (no style) | fill gradient (see crop); text `text.iridescent-secondary`; border `borderWidth.default` transparent; shadow none; size `size.premium-button` high; radius `radius.full`; padding `spacing.2` `spacing.4`; type 14px/21px 500 (no style) | [dark](components/crops/2026-10/premium-button-dark-default.png) [light](components/crops/2026-10/premium-button-light-default.png) |
| hover | fill gradient (see crop) | fill gradient (see crop) | [dark](components/crops/2026-10/premium-button-dark-hover.png) [light](components/crops/2026-10/premium-button-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/premium-button-dark-focus-visible.png) [light](components/crops/2026-10/premium-button-light-focus-visible.png) |
| pressed | fill gradient (see crop); opacity 0.89 | fill gradient (see crop); opacity 0.89 | [dark](components/crops/2026-10/premium-button-dark-active.png) [light](components/crops/2026-10/premium-button-light-active.png) |

### Icon button

`data-slot=icon-button`: a 44px round button with a 16px glyph; the star toggle on topics is 40px with `aria-pressed`.

**icon-button** (no label; `[data-slot=icon-button][aria-label="Previous period"]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `icon.secondary`; border `borderWidth.default` transparent; shadow none; size `size.icon-button-sm` high; radius `radius.full`; padding `spacing.3`; type `typography.body.base` | text `text.secondary`; border `borderWidth.default` transparent; shadow none; size `size.icon-button-sm` high; radius `radius.full`; padding `spacing.3`; type `typography.body.base` | [dark](components/crops/2026-10/icon-button-dark-default.png) [light](components/crops/2026-10/icon-button-light-default.png) |
| hover | fill `bg.alpha` | fill `bg.hover` | [dark](components/crops/2026-10/icon-button-dark-hover.png) [light](components/crops/2026-10/icon-button-light-hover.png) |
| focus-visible | fill `bg.alpha`; shadow `focusRing.width` in `border.select` | fill `bg.hover`; shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/icon-button-dark-focus-visible.png) [light](components/crops/2026-10/icon-button-light-focus-visible.png) |
| pressed | fill `bg.active` | fill `bg.active` | [dark](components/crops/2026-10/icon-button-dark-active.png) [light](components/crops/2026-10/icon-button-light-active.png) |

**icon-button-disabled** (no label; `[data-slot=icon-button][aria-label="Next period"]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.disabled`; border `borderWidth.default` transparent; shadow none; size `size.icon-button-sm` high; radius `radius.full`; padding `spacing.3`; type `typography.body.base` | text `text.disabled`; border `borderWidth.default` transparent; shadow none; size `size.icon-button-sm` high; radius `radius.full`; padding `spacing.3`; type `typography.body.base` | [dark](components/crops/2026-10/icon-button-disabled-dark-default.png) [light](components/crops/2026-10/icon-button-disabled-light-default.png) |

**icon-button-toggle** (no label; `[data-slot=icon-button][aria-pressed]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.tertiary`; shadow none; size `size.control-sm` high; radius `radius.full`; type `typography.body.base` | text `text.tertiary`; shadow none; size `size.control-sm` high; radius `radius.full`; type `typography.body.base` | [dark](components/crops/2026-10/icon-button-toggle-dark-default.png) [light](components/crops/2026-10/icon-button-toggle-light-default.png) |
| hover | text `text.secondary` | text `text.secondary` | [dark](components/crops/2026-10/icon-button-toggle-dark-hover.png) [light](components/crops/2026-10/icon-button-toggle-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/icon-button-toggle-dark-focus-visible.png) [light](components/crops/2026-10/icon-button-toggle-light-focus-visible.png) |
| pressed | text `text.secondary` | text `text.secondary` | [dark](components/crops/2026-10/icon-button-toggle-dark-active.png) [light](components/crops/2026-10/icon-button-toggle-light-active.png) |

### Link

`data-slot=link`: footer and inline links are quiet (`text.secondary`) until hover, which turns them blue and underlined.

**link** (About us; `footer a[data-slot=link], a[data-slot=link]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.secondary`; shadow none | text `text.secondary`; shadow none | [dark](components/crops/2026-10/link-dark-default.png) [light](components/crops/2026-10/link-light-default.png) |
| hover | text `text.link`; decoration underline | text `text.link`; decoration underline | [dark](components/crops/2026-10/link-dark-hover.png) [light](components/crops/2026-10/link-light-hover.png) |
| focus-visible | fill `bg.primary`; shadow `focusRing.width` in `border.select` | fill `bg.primary`; shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/link-dark-focus-visible.png) [light](components/crops/2026-10/link-light-focus-visible.png) |
| pressed | text `text.link`; decoration underline | text `text.link`; decoration underline | [dark](components/crops/2026-10/link-dark-active.png) [light](components/crops/2026-10/link-light-active.png) |

### Text field

`data-slot=form-input`. Error state (not reached, see Gaps): the stylesheet sets `outline-color: border.danger-primary` on `:invalid, [data-invalid], [aria-invalid=true]` and `text.danger-primary` on the message (raw/css-rules.json).

**text-field** (no label; `input[type=text]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.primary`; border `borderWidth.default` `border.primary`; shadow none; size `size.control-lg` high; radius `radius.md`; padding `spacing.3` `spacing.4`; type `typography.body.base` | text `text.primary`; border `borderWidth.default` `border.primary`; shadow none; size `size.control-lg` high; radius `radius.md`; padding `spacing.3` `spacing.4`; type `typography.body.base` | [dark](components/crops/2026-10/text-field-dark-default.png) [light](components/crops/2026-10/text-field-light-default.png) |
| focus-visible | border `borderWidth.default` `border.active`; shadow inset 1px in `border.active` (`shadow.input-focus`) | border `borderWidth.default` `border.active`; shadow inset 1px in `border.active` (`shadow.input-focus`) | [dark](components/crops/2026-10/text-field-dark-focus-visible.png) [light](components/crops/2026-10/text-field-light-focus-visible.png) |

### Text area

The Koji prompt: a borderless auto-growing textarea inside a frosted pill (`blur.ask-pill`). It shows no focus ring; the caret is the only focus cue.

**text-area** (How do I find the slope of a line?; `textarea`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.primary`; shadow none; size `size.icon-lg` high; type `typography.body.base` | text `text.primary`; shadow none; size `size.icon-lg` high; type `typography.body.base` | [dark](components/crops/2026-10/text-area-dark-default.png) [light](components/crops/2026-10/text-area-light-default.png) |

**text-area-pill** (How do I find the slope of a line?; `textarea`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.primary`; shadow none; size 36px (no token) high; type `typography.body.base` | text `text.primary`; shadow none; size 36px (no token) high; type `typography.body.base` | [dark](components/crops/2026-10/text-area-pill-dark-default.png) [light](components/crops/2026-10/text-area-pill-light-default.png) |
| focus-visible | focus browser default ring (no product style) | focus browser default ring (no product style) | [dark](components/crops/2026-10/text-area-pill-dark-focus-visible.png) [light](components/crops/2026-10/text-area-pill-light-focus-visible.png) |

### Select

Not present: no screen reached on a free account uses one. The stylesheet carries a `select-icon` slot, but nothing rendered it.

### Checkbox

Not present as a visible control: every `type=checkbox` in the app is the hidden input behind a switch. The stylesheet carries `checkbox` and `checkbox-indicator` slots that no reached screen rendered.

### Radio

A real radio (`data-slot=radio`, 20px) in the account's connected-accounts list, and the segmented control, which is a Base UI radio group (`role=radiogroup`) of pill segments.

**radio** (no label; `[data-slot=radio]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.primary`; text `text.primary`; border `borderWidth.default` `border.primary`; shadow none; size `size.icon-md` high; radius `radius.full`; type `typography.body.base` | fill `bg.primary`; text `text.primary`; border `borderWidth.default` `border.primary`; shadow none; size `size.icon-md` high; radius `radius.full`; type `typography.body.base` | [dark](components/crops/2026-10/radio-dark-default.png) [light](components/crops/2026-10/radio-light-default.png) |
| hover | border `borderWidth.default` `border.hover` | border `borderWidth.default` `border.hover` | [dark](components/crops/2026-10/radio-dark-hover.png) [light](components/crops/2026-10/radio-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/radio-dark-focus-visible.png) [light](components/crops/2026-10/radio-light-focus-visible.png) |
| pressed | border `borderWidth.default` `border.hover` | border `borderWidth.default` `border.hover` | [dark](components/crops/2026-10/radio-dark-active.png) [light](components/crops/2026-10/radio-light-active.png) |

**segment-selected** (Auto; `[data-slot=segment][data-checked], [role=radio][data-checked]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.primary`; text `text.primary`; border `borderWidth.thin` `border.primary`; shadow `shadow.base`; size `size.icon-button-xs` high; radius `radius.full`; padding 0 `spacing.2.5`; type `typography.ui.nav.selected` | fill `bg.primary`; text `text.primary`; border `borderWidth.thin` `border.primary`; shadow `shadow.base`; size `size.icon-button-xs` high; radius `radius.full`; padding 0 `spacing.2.5`; type `typography.ui.nav.selected` | [dark](components/crops/2026-10/segment-selected-dark-default.png) [light](components/crops/2026-10/segment-selected-light-default.png) |

**segment** (Light; `[data-slot=segment][data-unchecked], [role=radio][data-unchecked]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.tertiary`; border `borderWidth.thin` transparent; shadow none; size `size.icon-button-xs` high; radius `radius.full`; padding 0 `spacing.2.5`; type `typography.ui.nav.selected` | text `text.tertiary`; border `borderWidth.thin` transparent; shadow none; size `size.icon-button-xs` high; radius `radius.full`; padding 0 `spacing.2.5`; type `typography.ui.nav.selected` | [dark](components/crops/2026-10/segment-dark-default.png) [light](components/crops/2026-10/segment-light-default.png) |
| hover | fill `bg.alpha`; text `text.primary` | fill `bg.hover`; text `text.primary` | [dark](components/crops/2026-10/segment-dark-hover.png) [light](components/crops/2026-10/segment-light-hover.png) |
| pressed | fill `bg.alpha`; text `text.primary` | fill `bg.hover`; text `text.primary` | [dark](components/crops/2026-10/segment-dark-active.png) [light](components/crops/2026-10/segment-light-active.png) |

**segment-track** (AutoLightDark; `[data-slot=radio-group], [role=radiogroup]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.elevated`; text `text.primary`; shadow none; size `size.icon-button-sm` high; radius `radius.full`; padding `spacing.1.5`; type `typography.body.base` | fill `bg.secondary`; text `text.primary`; shadow none; size `size.icon-button-sm` high; radius `radius.full`; padding `spacing.1.5`; type `typography.body.base` | [dark](components/crops/2026-10/segment-track-dark-default.png) [light](components/crops/2026-10/segment-track-light-default.png) |

### Switch

`data-slot=switch`, 48x32 track, 24px thumb; focus is a 3px outline in `border.select`.

**switch-on** (no label; `[data-slot=switch][data-checked]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.green-primary`; size `size.icon-button-xs` high; radius `radius.full`; padding `spacing.1`; face: fill `accent.on-accent`; face: text `text.primary`; face: shadow none; face: size `size.icon-lg` high; face: radius `radius.full`; face: type `typography.body.base` | fill `bg.green-primary`; size `size.icon-button-xs` high; radius `radius.full`; padding `spacing.1`; face: fill `bg.primary`; face: text `text.primary`; face: shadow none; face: size `size.icon-lg` high; face: radius `radius.full`; face: type `typography.body.base` | [dark](components/crops/2026-10/switch-on-dark-default.png) [light](components/crops/2026-10/switch-on-light-default.png) |
| focus-visible | outline `focusRing.width` `border.select` | outline `focusRing.width` `border.select` | [dark](components/crops/2026-10/switch-on-dark-focus-visible.png) [light](components/crops/2026-10/switch-on-light-focus-visible.png) |

**switch-off** (no label; `[data-slot=switch][data-unchecked]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.disabled`; size `size.icon-button-xs` high; radius `radius.full`; padding `spacing.1`; face: fill `accent.on-accent`; face: text `text.primary`; face: shadow none; face: size `size.icon-lg` high; face: radius `radius.full`; face: type `typography.body.base` | fill `bg.alpha`; size `size.icon-button-xs` high; radius `radius.full`; padding `spacing.1`; face: fill `bg.primary`; face: text `text.primary`; face: shadow none; face: size `size.icon-lg` high; face: radius `radius.full`; face: type `typography.body.base` | [dark](components/crops/2026-10/switch-off-dark-default.png) [light](components/crops/2026-10/switch-off-light-default.png) |
| focus-visible | outline `focusRing.width` `border.select` | outline `focusRing.width` `border.select` | [dark](components/crops/2026-10/switch-off-dark-focus-visible.png) [light](components/crops/2026-10/switch-off-light-focus-visible.png) |

### Tabs

Two tab sets: the app header (Home, Topics, You; selected has an underline bar and `text.primary`) and the settings side menu (selected gets `bg.active`).

**nav-tab-selected** (Home; `a[data-selected="true"]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.primary`; shadow none; size `size.appBar` less its 1px border (calc(100% - 1px)) | text `text.primary`; shadow none; size `size.appBar` less its 1px border (calc(100% - 1px)) | [dark](components/crops/2026-10/nav-tab-selected-dark-default.png) [light](components/crops/2026-10/nav-tab-selected-light-default.png) |
| focus-visible | focus browser default ring (no product style) | focus browser default ring (no product style) | [dark](components/crops/2026-10/nav-tab-selected-dark-focus-visible.png) [light](components/crops/2026-10/nav-tab-selected-light-focus-visible.png) |

**nav-tab** (Topics; `a[data-selected="false"]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.secondary`; shadow none; size `size.appBar` less its 1px border (calc(100% - 1px)) | text `text.secondary`; shadow none; size `size.appBar` less its 1px border (calc(100% - 1px)) | [dark](components/crops/2026-10/nav-tab-dark-default.png) [light](components/crops/2026-10/nav-tab-light-default.png) |
| hover | text `text.primary` | text `text.primary` | [dark](components/crops/2026-10/nav-tab-dark-hover.png) [light](components/crops/2026-10/nav-tab-light-hover.png) |
| focus-visible | focus browser default ring (no product style) | focus browser default ring (no product style) | [dark](components/crops/2026-10/nav-tab-dark-focus-visible.png) [light](components/crops/2026-10/nav-tab-light-focus-visible.png) |
| pressed | text `text.primary` | text `text.primary` | [dark](components/crops/2026-10/nav-tab-dark-active.png) [light](components/crops/2026-10/nav-tab-light-active.png) |

**settings-tab-selected** (Preferences; `button[data-slot=button]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.active`; text `text.primary`; border `borderWidth.default` transparent; shadow none; size `size.control-sm` high; radius `radius.md`; padding `spacing.2` `spacing.4`; type `typography.ui.nav.selected` | fill `bg.hover`; text `text.primary`; border `borderWidth.default` transparent; shadow none; size `size.control-sm` high; radius `radius.md`; padding `spacing.2` `spacing.4`; type `typography.ui.nav.selected` | [dark](components/crops/2026-10/settings-tab-selected-dark-default.png) [light](components/crops/2026-10/settings-tab-selected-light-default.png) |
| hover | fill `bg.alpha` | no change | [dark](components/crops/2026-10/settings-tab-selected-dark-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/settings-tab-selected-dark-focus-visible.png) [light](components/crops/2026-10/settings-tab-selected-light-focus-visible.png) |

**settings-tab** (Account; `button[data-slot=button]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.secondary`; border `borderWidth.default` transparent; shadow none; size `size.control-sm` high; radius `radius.md`; padding `spacing.2` `spacing.4`; type `typography.body.base` | text `text.secondary`; border `borderWidth.default` transparent; shadow none; size `size.control-sm` high; radius `radius.md`; padding `spacing.2` `spacing.4`; type `typography.body.base` | [dark](components/crops/2026-10/settings-tab-dark-default.png) [light](components/crops/2026-10/settings-tab-light-default.png) |
| hover | fill `bg.alpha` | fill `bg.hover` | [dark](components/crops/2026-10/settings-tab-dark-hover.png) [light](components/crops/2026-10/settings-tab-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/settings-tab-dark-focus-visible.png) [light](components/crops/2026-10/settings-tab-light-focus-visible.png) |
| pressed | fill `bg.active` | fill `bg.active` | [dark](components/crops/2026-10/settings-tab-dark-active.png) [light](components/crops/2026-10/settings-tab-light-active.png) |

### Menu

Base UI dropdown (`role=menu`). Hover and keyboard focus both set `data-highlighted`, which paints `bg.hover`; the item itself draws no ring.

**menu** (SettingsAboutHelpLog out; `[role=menu]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.elevated`; text `text.primary`; shadow `shadow.base` | fill `bg.primary`; text `text.primary`; shadow `shadow.base` | [dark](components/crops/2026-10/menu-dark-default.png) [light](components/crops/2026-10/menu-light-default.png) |

**menu-item** (Settings; `[data-slot=dropdown-menu-item]:not([data-highlighted])`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.primary`; shadow none; size `size.control-md` high; padding `spacing.3` `spacing.4`; type `typography.body.base` | text `text.primary`; shadow none; size `size.control-md` high; padding `spacing.3` `spacing.4`; type `typography.body.base` | [dark](components/crops/2026-10/menu-item-dark-default.png) [light](components/crops/2026-10/menu-item-light-default.png) |

**menu-item-highlighted** (About; `[data-slot=dropdown-menu-item][data-highlighted]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.alpha`; text `text.primary`; shadow none; size `size.control-md` high; padding `spacing.3` `spacing.4`; type `typography.body.base` | fill `bg.hover`; text `text.primary`; shadow none; size `size.control-md` high; padding `spacing.3` `spacing.4`; type `typography.body.base` | [dark](components/crops/2026-10/menu-item-highlighted-dark-default.png) [light](components/crops/2026-10/menu-item-highlighted-light-default.png) |

### Tooltip

Base UI tooltip on hover or focus of a 12px info icon; `bg.elevated`, `shadow.base`, `typography.body.sm` in `text.secondary`.

**tooltip** (Includes lessons, warm ups, and level ch; `[data-slot=tooltip-content]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.elevated`; text `text.secondary`; shadow `shadow.base` | fill `bg.primary`; text `text.secondary`; shadow `shadow.base` | [dark](components/crops/2026-10/tooltip-dark-default.png) [light](components/crops/2026-10/tooltip-light-default.png) |

**tooltip-trigger** (no label; `[data-slot=tooltip-trigger]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `icon.active`; shadow none; size `size.progress-lg` high; radius `radius.xs`; type `typography.body.sm` | text `icon.active`; shadow none; size `size.progress-lg` high; radius `radius.xs`; type `typography.body.sm` | [dark](components/crops/2026-10/tooltip-trigger-dark-default.png) [light](components/crops/2026-10/tooltip-trigger-light-default.png) |
| hover | text `icon.secondary` | text `text.secondary` | [dark](components/crops/2026-10/tooltip-trigger-dark-hover.png) [light](components/crops/2026-10/tooltip-trigger-light-hover.png) |
| focus-visible | shadow `focusRing.width` in `border.select` | shadow `focusRing.width` in `border.select` | [dark](components/crops/2026-10/tooltip-trigger-dark-focus-visible.png) [light](components/crops/2026-10/tooltip-trigger-light-focus-visible.png) |
| pressed | text `icon.secondary` | text `text.secondary` | [dark](components/crops/2026-10/tooltip-trigger-dark-active.png) [light](components/crops/2026-10/tooltip-trigger-light-active.png) |

### Dialog

Base UI dialog (`modal-content`), `shadow.md`, max `size.modal-max`; the scrim is `special.overlay.default`. Used for the destructive quit confirmation.

**dialog** (Are you sure?If you quit, you will lose ; `[data-slot=modal-content]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.elevated`; text `text.primary`; shadow `shadow.md` | fill `bg.primary`; text `text.primary`; shadow `shadow.md` | [dark](components/crops/2026-10/dialog-dark-default.png) [light](components/crops/2026-10/dialog-light-default.png) |

**dialog-scrim** (no label; `[data-slot=modal-overlay]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `special.overlay.default`; text `text.primary`; shadow none | fill `special.overlay.default`; text `text.primary`; shadow none | [dark](components/crops/2026-10/dialog-scrim-dark-default.png) [light](components/crops/2026-10/dialog-scrim-light-default.png) |

### Toast

Not captured: the Sonner toaster is mounted (`section[aria-label^=Notifications]`) but no look-only action fired a toast in either capture.

### Card

Course cards are 3D like the button (2px `border.solid` edge plus a 4px lip); summary cards are flat with a 2px border and a tinted gradient.

**card-course** (NewGR 4–5; `[data-slot=card]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.primary`; text `text.primary`; border `borderWidth.default` `border.solid`; shadow lip 0 4px 0 in `border.solid` | fill `bg.primary`; text `text.primary`; border `borderWidth.default` `border.solid`; shadow lip 0 4px 0 in `border.solid` | [dark](components/crops/2026-10/card-course-dark-default.png) [light](components/crops/2026-10/card-course-light-default.png) |
| focus-visible | focus browser default ring (no product style) | focus browser default ring (no product style) | [dark](components/crops/2026-10/card-course-dark-focus-visible.png) [light](components/crops/2026-10/card-course-light-focus-visible.png) |

**weekly-summary-card** (Weekly summaryOct 12 – Oct 17, 2026No pr; `section, [data-slot=box]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill gradient (see crop); text `text.primary`; border `borderWidth.default` `border.primary`; shadow none | fill gradient (see crop); text `text.primary`; border `borderWidth.default` `border.primary`; shadow none | [dark](components/crops/2026-10/weekly-summary-card-dark-default.png) [light](components/crops/2026-10/weekly-summary-card-light-default.png) |

### List row

Settings rows: a 1px `border.primary` box, `radius.xl`, label left and control right.

**list-row-setting** (Enable sound effects in lessons; `div`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | text `text.primary`; border `borderWidth.thin` `border.primary`; shadow none; size 58px (no token) high; radius `radius.xl`; padding `spacing.3` `spacing.4`; type `typography.body.base` | text `text.primary`; border `borderWidth.thin` `border.primary`; shadow none; size 58px (no token) high; radius `radius.xl`; padding `spacing.3` `spacing.4`; type `typography.body.base` | [dark](components/crops/2026-10/list-row-setting-dark-default.png) [light](components/crops/2026-10/list-row-setting-light-default.png) |

### Table

Captured 2026-09 on the public `/subscribe/` page (Free vs Premium comparison, both themes): see [raw/pricing-computed.json](raw/pricing-computed.json) and [premium-comparison-dark](components/crops/premium-comparison-dark.png). The You page also renders a screen-reader-only data table (`data-slot=table`, inside `panda-sr_true`) behind its bar chart.

### Avatar

An initials tile (48px, `radius.md`, `palette.blue.500`) on the You page at phone width; there is no photo avatar.

**avatar** (L; `[role=img][aria-label]`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.blue-primary`; text `text.primary`; shadow none; size `size.control-md` high; radius `radius.md`; type `typography.heading.sm` | fill `bg.blue-primary`; text `text.inverse`; shadow none; size `size.control-md` high; radius `radius.md`; type `typography.heading.sm` | [dark](components/crops/2026-10/avatar-dark-default.png) [light](components/crops/2026-10/avatar-light-default.png) |

### Badge

`.panda-badge` subtle variants: 12/13.2 700 uppercase on a tinted fill, `radius.lg`.

**badge-unverified** (Unverified; `.panda-badge--colorPalette_yellow`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.yellow-tertiary`; text `text.yellow-primary`; shadow none; size `size.badge-height` high; radius `radius.lg`; padding `spacing.1` `spacing.2`; type `typography.ui.actions.sm` | fill `bg.yellow-tertiary`; text `text.yellow-primary`; shadow none; size `size.badge-height` high; radius `radius.lg`; padding `spacing.1` `spacing.2`; type `typography.ui.actions.sm` | [dark](components/crops/2026-10/badge-unverified-dark-default.png) [light](components/crops/2026-10/badge-unverified-light-default.png) |

**badge-primary** (Primary; `.panda-badge--colorPalette_blue`)

| State | Dark | Light | Crops |
|---|---|---|---|
| default | fill `bg.blue-tertiary`; text `text.blue-primary`; shadow none; size `size.badge-height` high; radius `radius.lg`; padding `spacing.1` `spacing.2`; type `typography.ui.actions.sm` | fill `bg.blue-tertiary`; text `text.blue-primary`; shadow none; size `size.badge-height` high; radius `radius.lg`; padding `spacing.1` `spacing.2`; type `typography.ui.actions.sm` | [dark](components/crops/2026-10/badge-primary-dark-default.png) [light](components/crops/2026-10/badge-primary-light-default.png) |

## Earlier capture (2026-09-25)

Kept as written for the first capture, with values read live in Chrome at 1384x797. Where a 2026-10 spec above covers the same component, the spec wins.

### Discovery list

Every page, view and overlay found, with what was captured. D is dark, L is light, M is the 390x844 mobile width. Screenshot names are in [screenshots/](screenshots).

#### Public pages (headless Chromium, 1440x900 and 390x844)

| Surface | URL | Themes | Captured | Screenshots |
|---|---|---|---|---|
| Landing | `/` | L only (ignores dark) | desktop, M | `landing-light-default`, `mobile-landing-light-default` |
| Sign up | `/signup` → `/welcome/` | L only | desktop, M | `signup-light-default`, `mobile-signup-light-default` |
| Log in | `/login/` | L, D | desktop, M | `login-{light,dark}-default`, `mobile-login-*` |
| Course catalog (public) | `/courses/` | L, D | desktop, M | `courses-public-*`, `mobile-courses-public-*` |
| Course page (public) | `/courses/<slug>/` | L, D | desktop, M | `course-public-*`, `mobile-course-public-*` |
| Pricing | `/subscribe/` | L, D | viewport, full page, M | `pricing-{light,dark}-{default,fullpage}`, `mobile-pricing-*` |
| 404 (legacy Django) | any bad path | L only | desktop, M | `notfound-light-404`, `mobile-notfound-light-404` |

#### Signed-in app (Chrome, 1384x797 at 2x)

| Surface | Where | Captured | Screenshots |
|---|---|---|---|
| Onboarding: intro, voice choice, Koji demo, subject, level list, placement intro and question, result | `/welcome/…` | D; hover and selected card states | `onboarding-dark-*` (11) |
| Returning-learner promo | `/welcome/recommendations` | D | `promo-dark-returning-learner-offer` |
| "Creating your learning plan" loader | onboarding | D | `plan-dark-creating-plan-loading` |
| Learning plan intro | `#llp-preview-intro` | D | `plan-dark-learning-plan-intro` |
| Learning path | `#learning-path` | D | `plan-dark-learning-path` |
| In-app paywall | onboarding | not saved, see Gaps | covered by `pricing-*-fullpage` |
| Home | `/home/` | D, L | `home-dark-default`, `home-light-default` |
| Koji prompt (home) | `/home/` ask pill | D | `home-dark-koji-prompt-open` |
| Course catalog | `/courses/` | D, L; tile hover | `courses-dark-default`, `courses-dark-course-tile-hover`, `courses-light-default` |
| Course page | `/courses/<slug>/` | D, L | `course-dark-default`, `course-light-default` |
| Lesson player | `/courses/<course>/<chapter>/<lesson>/` | D: idle, answer placed, correct, retry. L: idle | `lesson-dark-*`, `lesson-light-default` |
| Koji tutor chat | lesson, "Get help" | D: open, typing, board highlight | `lesson-dark-tutor-*` |
| Quit dialog | lesson, close button | D: default, danger hover | `lesson-dark-quit-confirm-*` |
| You (progress) | `/you/` | D, L; chart tooltip | `you-dark-default`, `you-dark-chart-tooltip`, `you-light-default` |
| Settings: account | `/settings/account/` | D, L; input focus plus button hover | `settings-dark-account`, `settings-dark-input-focus-button-hover`, `settings-light-account` |
| Settings: preferences | `/settings/preferences/` | D, L; switches off | `settings-dark-preferences`, `settings-dark-preferences-switches-off`, `settings-light-preferences` |
| Legacy account page | `/account/` (Django) | L only | `legacy-light-account-settings` |

#### Overlays and transient states

| Overlay | Trigger | Captured |
|---|---|---|
| Header dropdown menu | ☰ in the app header | D (item hover), L (`settings-light-header-menu-open`) |
| Keys popover | keys stat pill | D, L |
| Streak popover | streak stat pill | D, L |
| Tooltip | You page, bar chart and strength chip | D |
| Modal | quit a lesson | D |
| Koji prompt overlay | home ask pill | D |
| Tutor chat panel | lesson "Get help" | D |
| Lesson feedback (correct, retry) | Check button | D |
| Empty state | You page, "No course progress yet." | D, L (in the page captures) |
| Error state | 404 page | L; invalid input read from CSS only |
| Toast (Sonner) | never fired in this session | not captured, see Gaps |
| Command palette | none exists in the product | n/a |
| Cookie banner | OneTrust, third party | hidden during capture, not documented |

### Core components

#### Button3d

The main call to action everywhere: a pill face lifted 4px over a same-hue lip. `data-slot=button3d` wrapping `button3d-face`.

| Part | Value | Token |
|---|---|---|
| Size | h48, full width or 272–367 wide in context | `size.button-height` |
| Face | radius 60, padding 14 24, gap 8 | `radius.full` |
| Label | CoFo Brilliant 16/20 500 | `typography.ui.actions.base` |
| Lift | face `translateY(-4px)`, `box-shadow: 0 4px 0 0 <lip>` | `component.button3d.*` |
| Press | lift and shadow go 4px → 0, `transform .1s ease-out, box-shadow .1s ease-out` | `duration.instant` (100ms), `easing.ease-out` |
| Focus | `0 0 0 3px border.select` on the outer button | `shadow.outline` |
| Disabled | outer opacity .85, face `bg.disabled`, text `text.disabled`, no lift | `component.button3d.disabled-face`, `disabled-text` |

Colour variants (face / lip, dark theme): primary gray.200 / gray.400 (light: black / gray.800), secondary fill `bg.tertiary` / whiteAlpha, green green.500 / green.600, blue blue.500 / blue.600, yellow yellow.500 with yellow.900 text / yellow.700, plus red, purple, orange, teal, pink, pear, papaya and mint in the same pattern. All are in `component.button3d`.

Premium variant: flat, no lift, face `gradient.iridescent-frame`, text `text.iridescent-primary`, `box-shadow: inset 0 -4px 0 0 rgba(20,37,99,.3)`, hover opacity .85.

Hover changes nothing in Chrome: the tint (`--button3d-hover-tint`) is scoped to Safari.

![button3d primary, dark](components/crops/button3d-primary-dark.png)
![button3d disabled, dark](components/crops/button3d-disabled-dark.png)
![lesson footer: secondary and green button3d](components/crops/lesson-footer-correct-dark.png)
![lesson footer: secondary and yellow button3d](components/crops/lesson-footer-retry-dark.png)
![premium variant in the keys popover, light](components/crops/popover-keys-light.png)

#### Flat button

`data-slot=button`. h48, padding 12 22, radius 54, border 2px, `ui.actions.base`.

| Variant | Background | Text | Hover |
|---|---|---|---|
| primary (inverse) | `bg.inverse-primary` (#f2f2f2 D / #000 L) | `text.inverse` | opacity .78 |
| outline | transparent, border `border.primary` | `text.primary` | `bg.hover` |
| ghost | transparent | `text.secondary` or `text.tertiary` | `bg.hover` |
| danger ghost | transparent | `text.danger-primary` | `bg.danger-secondary-hover` |
| disabled | `bg.disabled` | `text.disabled` | none, cursor not-allowed |
| danger disabled | `bg.danger-disabled` | `text.danger-disabled` | none |

The public header uses a green sign-up variant (`bg.green-primary`, white text) and a compact h40 outline "Sign in".

![primary button hover and outline "Send verification", dark](components/crops/button-primary-hover-dark.png)
![email row with outline button, light](components/crops/settings-email-badges-light.png)
![quit dialog: danger ghost button on hover](components/crops/modal-quit-danger-hover-dark.png)

#### Hue-shift pill

`data-slot=hue-shift-button`, used for quick answers (No / Maybe / Yes). h52, min-w 96, padding 16 24, radius full, `ui.actions.base`, background `gradient.hue-shift-action-gray`. Has a hidden loading layer with a spinner.

![hue-shift pills, dark](components/crops/hue-shift-pills-dark.png)

#### Icon button and glass button

Icon button (`data-slot=icon-button`): 44–48 square, padding 12, border 2px transparent, radius 6 or full. Play-sample variant sits on `bg.hover`. Focus is `shadow.outline` plus `bg.hover`.

Glass button (`data-slot=glass-button`, lesson rail): 48x48, radius 54, `backdrop-filter: blur(20px) saturate(1.8)`, icon `text.disabled`. The Koji dock pairs two as a split pill (60x52 each, radii 9999 0 0 9999 and 0 9999 9999 0).

![lesson top bar with close icon button, dark](components/crops/lesson-topbar-dark.png)
![Koji dock with split glass pill, dark](components/crops/lesson-koji-dock-dark.png)

#### Text input

`data-slot=form-input` inside `data-slot=field`.

| State | Value |
|---|---|
| Default | h52, padding 12 16, radius 8, border 2px `border.primary`, transparent bg, `typography.body.base` |
| Placeholder | `text.disabled` |
| Focus | border 2px `border.active` plus `inset 0 0 0 1px` the same colour (reads as a 3px ring), no outline |
| Disabled | `bg.secondary`, no border, `text.secondary`, field opacity .5 |
| Invalid | label and message `text.danger-primary` (read from CSS; no live error was triggered) |

Label is 16/20 500 `text.primary`, 8px above the input.

![inputs, light](components/crops/settings-inputs-light.png)
![inputs, dark](components/crops/settings-inputs-dark.png)
![input focus, dark](components/crops/input-focus-dark.png)
![login form, light](components/crops/login-form-light.png)

#### Chat input and ask pill

Chat input (tutor panel): h53, radius 24, bg `autoflip.black.100`, border .5px `autoflip.black.200`, auto-resizing textarea, send button 32 round inside it. The send button is transparent when empty and fills with `gradient.koji-send-button` once there is text.

Ask pill (home, fixed bottom): 552x68, radius 32, border 2px `border.secondary`, `shadow.base`, translucent fill, idle opacity .65, focused adds `blur(24px)` and opacity 1, `150ms ease`.

Keycaps (`kbd`) under the chat input: h21, padding 0 6 2, radius 5, 1px border with a 2px bottom.

![tutor input with text, dark](components/crops/tutor-input-filled-dark.png)
![ask pill, light](components/crops/home-ask-pill-light.png)
![ask pill, dark](components/crops/home-ask-pill-dark.png)

#### Search field (catalog)

A button styled as a field that opens Koji: 340x52, radius full, border 2px `border.primary`, padding 4 4 4 16, search icon 16, trailing disabled-look "Ask" pill. Hover `border.hover`; focus `border.active` plus `shadow.outline`.

![search field, light](components/crops/courses-search-light.png)
![search field, dark](components/crops/courses-search-dark.png)

#### Switch

`data-slot=switch`: 48x32 track, padding 4, radius full; thumb 24 white. Off `bg.disabled`, on `bg.green-primary`, thumb moves 16px with `transform .15s ease`. Focus ring 3px. Disabled plus checked uses `bg.disabled` with a `bg.primary` thumb. The onboarding voice switch uses a teal gradient in place of green. Tokens: `component.switch.*`.

![preferences: segmented controls and switches, light](components/crops/preferences-light.png)
![switches off, dark](components/crops/preferences-switches-off-dark.png)
![onboarding teal switch, dark](components/crops/switch-onboarding-dark.png)

#### Segmented control

Two sizes, same pattern: a `bg.secondary` track (radius full, padding 4–6, gap 4) with pill segments. Checked segment is `bg.primary`, `border.primary` 1px, `text.primary`, `shadow.base`; unchecked is `text.tertiary`. `transition: background-color, border-color, box-shadow, color .15s ease-out`.

| Where | Track | Segment | Type |
|---|---|---|---|
| Preferences (`data-slot=segment`) | h44, padding 6 | h32, padding 0 10 | `ui.nav.selected` 16/24 500 |
| You page time range | padding 4 | min-w 60, padding 8 12 | `body.sm` 14/21 |

![segmented control and stat cards, light](components/crops/segmented-and-stats-light.png)
![segmented control and switches, dark](components/crops/preferences-segmented-switch-dark.png)

#### Choice card

A card that acts as a radio (onboarding voice, subject and level). 158–178 wide, h228, radius 16, padding 32 24 24, bg `gradient.hue-shift-action-gray`, label `ui.actions.base` in `text.secondary`.

| State | Change |
|---|---|
| Hover | bg `bg.hover`, gradient removed |
| Selected (`data-checked`) | label `text.primary`; `::before` paints a hue-shift gradient (teal or blue); subject cards add `shadow.outline` |

![choice cards, default](components/crops/choice-card-states-dark.png)
![choice card hover](components/crops/choice-card-hover-dark.png)
![choice card selected](components/crops/choice-card-selected-dark.png)
![subject card selected](components/crops/subject-card-selected-dark.png)
![level option cards](components/crops/level-option-cards-dark.png)

#### Tabs and navigation

App header nav tabs: `a` h63, `ui.nav.default` 16/24 in `text.secondary`; selected is `text.primary`, weight 500 and a 2px underline that slides up with `transform 100ms linear`.

Settings side menu: `bg.primary` panel, 1px `border.primary`, radius 12, padding 16; items h40, radius 8; selected `bg.tertiary` with `ui.nav.selected`.

Pricing billing tabs (Base UI): 48 tall, 16/24; active is 500 `text.purple-primary` with an underline. Feature tabs (vertical) are 56 tall, radius 8, active `gray.100` light or `bg.hover` dark.

![app header, light](components/crops/app-header-light.png)
![app header, dark](components/crops/app-header-dark.png)
![settings side menu, light](components/crops/settings-sidenav-light.png)
![settings side menu, dark](components/crops/settings-sidenav-dark.png)

#### Badge

`.panda-badge`, recipe with `colorPalette` and `variant`. Text is `ui.actions.sm`: 12/13.2 700, uppercase, tracking .48px.

| Variant | Padding / radius | Example |
|---|---|---|
| subtle | 4 8, full | "RECOMMENDED" blue (L blue.200 on blue.700 text; D blue.900 with blue.200), "UNVERIFIED" yellow, "PRIMARY" blue |
| solid | 4 8, 12 | "NEW" green.600 with white, "SAVE xx%" purple.500 |
| minimal | none | grade eyebrows "GR 4–5" in `text.tertiary` |
| premium solid | 6 20, 12 | pink.300 → yellow.400 gradient, black text |

![badges in the email row, dark](components/crops/settings-email-badges-dark.png)
![RECOMMENDED badge, light](components/crops/home-recommended-card-light.png)
![premium badge over a display headline](components/crops/promo-badge-headline-dark.png)

#### Progress

`.panda-progress`, track radius full, indicator `bg.green-primary`.

| Size | Height | Where |
|---|---|---|
| sm | 4 | not seen in use |
| default | 8 | onboarding, 696 wide, indicator `width 200ms ease` |
| lg | 12 | lesson top bar, 592 wide, followed by 16x12 upcoming-section dots |

The learning-plan intro splits the bar into 3 segments with 4px gaps.

![onboarding progress](components/crops/progress-onboarding-dark.png)
![segmented progress and eyebrow](components/crops/segmented-progress-eyebrow-dark.png)
![lesson top bar, light](components/crops/lesson-topbar-light.png)

#### Spinner

`data-slot=spinner`: 16x16, 2px border, top in currentColor and the other sides at 25%, `spin 600ms linear infinite`. Seen inside hue-shift pills and the plan loader (`plan-dark-creating-plan-loading.png`).

#### Dropdown menu

`data-slot=dropdown-menu-content`: 280 wide, `bg.elevated`, radius 8, `shadow.base`, no padding. Items h48, padding 12 16, `body.base`; highlighted `bg.hover`. 1px `border.secondary` separators. Opens from scale .95 and opacity 0 with `opacity 150ms ease-in-out, transform 150ms ease-in-out`.

![dropdown menu, light](components/crops/dropdown-menu-light.png)
![dropdown menu with item hover, dark](components/crops/dropdown-menu-dark.png)

#### Popover

`data-slot=popover-content`: 353 (keys) or 384 (streak) wide, `bg.elevated`, radius 8, `shadow.base`, 20x10 arrow in `bg.elevated`. Same 150ms scale-and-fade as the menu.

![keys popover, dark](components/crops/popover-keys-dark.png)
![streak popover, light](components/crops/popover-streak-light.png)
![streak popover, dark](components/crops/popover-streak-dark.png)

#### Tooltip

`data-slot=tooltip-content`: max-w 280, padding 12 16, radius 12, `bg.elevated`, `shadow.base`; title `heading.sm`, body `body.sm` `text.secondary`; arrow is a 10px square rotated 45°. Same 150ms open transition.

![bar chart with tooltip, dark](components/crops/bar-chart-and-tooltip-dark.png)

#### Modal

Overlay `special.overlay.default` (rgba(11,11,11,.8) dark), `opacity 150ms`. Content max-w 448, `bg.elevated`, radius 20, `shadow.md`, padding 32 20 16, gap 24; title `heading.md`, body `body.base`; full-width button3d plus a danger ghost button. Opacity and transform 150ms.

![quit dialog, dark](components/crops/modal-quit-dark.png)

#### Card

Several shells share one pattern: `bg.primary`, 2px `border.primary` or `border.solid`, large radius, no shadow.

| Card | Radius | Padding | Notes |
|---|---|---|---|
| Course hero | 20 | 32 | 487 wide at xl |
| Stat card | 20 | 16 24 | label `body.sm`, value `heading.xl` |
| Home recommended | 24 | 24 | height `clamp(320px, 50dvh + banner, 500px)` |
| Home gamification | 32 | 0 | premium upsell footer strip |
| Figure card | 32 | 24 | `bg.elevated`, 1px border, `shadow.base` |
| Setting row | 16 | 18 16 | 1px border |
| Fixed footer card (course) | 40 | 24 16 16 | `bg.elevated`, `border.solid` |

![course hero card, light](components/crops/course-hero-card-light.png)
![course hero card, dark](components/crops/course-hero-card-dark.png)
![figure card, dark](components/crops/figure-card-dark.png)

### Product components

#### Promo banner

Under the app header: min-h 48, centred `body.sm` → `body.base` 500 with an underlined link, over a 25% blue → pink → yellow wash (80% `bg.primary` on top). Visible in every signed-in page crop of the header.

#### Premium header button and stat pills

"Go Premium" (`data-slot=premium-button`): h41, padding 8 16, radius full, 2px iridescent gradient border via `padding-box`/`border-box`, 14/21 500 `text.iridescent-secondary`.

Stat pills (keys, streak): h47, padding 9 20, radius 54, 2px `border.primary`, `ui.actions.base`, icon 24. They open the keys and streak popovers.

![header right side](components/crops/app-header-light.png)

#### Course tile

`data-inner-course-card`: 176 square at 2xl (152–218 by breakpoint), padding 22.72%, radius 20, 2px `border.solid`, lifted 4px with a `border.solid` lip. Hover changes the border and lip to `border.hover`. `transform .1s ease-out, box-shadow .1s ease-out, border-color .2s`. Grade badge top-left, "NEW" badge top-right, label below. Tiles on a shelf (`bg.secondary`, radius 12) are joined by 2px connectors.

![course shelf, light](components/crops/courses-shelf-light.png)
![course tile hover, dark](components/crops/course-tile-hover-dark.png)
![public course tiles, light](components/crops/course-tiles-light.png)

#### Learning-path tile and "START HERE" tag

Onboarding path: 176x174 artwork well, radius 36, padding 36; current tiles get `gradient.hue-shift-color-blue-primary`, locked tiles are `bg.primary` with a 2px `border.secondary` and `text.disabled` label. "START HERE" is a `gray.900` pill with gradient-clipped `ui.actions.sm` text, sitting on the tile's top edge.

![learning path tiles](components/crops/learning-path-tiles-dark.png)
![fixed bottom action bar](components/crops/bottom-action-bar-dark.png)

#### Course path (level header and nodes)

Level header: 456x64 button, radius 18, over a 3D lip in the level colour (blue.700 for Level 1); presses 4px on active. Eyebrow `ui.actions.sm` in the level colour. Path nodes are 3D discs with a label to the right; the current node glows blue with Koji on top, locked nodes are grey with `text.tertiary` labels. A fixed footer card holds a full-width blue button3d.

![course path, light](components/crops/course-path-light-app.png)
![course path, dark](components/crops/course-path-dark.png)

#### Home cards

Gamification card (streak, leagues, premium footer with an iridescent "Explore" pill) and recommended course card (badge, art, title, `LEVEL 1` eyebrow, lesson rows, blue button3d).

![gamification card, light](components/crops/home-gamification-card-light.png)
![gamification card, dark](components/crops/home-gamification-card-dark.png)
![recommended card, dark](components/crops/home-recommended-card-dark.png)

#### Koji prompt

Opened from the ask pill. Cards slide out, "Hey, Learner! How can I help?" (`body.lg` 600) sits over Koji, and suggestion cards float around. The suggestion cards are drawn on a `<canvas>`, so their styling is estimated from screenshot: about 130x84, radius 12, 5% white fill, active card with a 1px blue.400 border and glow.

![Koji prompt, dark](components/crops/home-koji-prompt-dark.png)

#### Lesson frame and interactive

The lesson panel is inset 34px, radius 24, `bg.primary`, with a 2px border that turns to the evaluation colour. The interactive (`<custom-interactive>`, CoFo Semi Mono) has tappy tiles, wells, a tray, answer slots and algebra tiles; every colour is in `component.lesson.*` for both themes.

| Part | Dark | Light |
|---|---|---|
| Tile face / edge | #141414 / gray.600 | white / gray.300 |
| Stacked lip | gray.900 over #666 | gray.200 |
| Tray | whiteAlpha 10% | blackAlpha 2.4% |
| Empty slot | gray.900, 2px dashed #666 | gray.50, 2px dashed gray.300 |
| Variable chip | #381d66, border #5a2ea3 | purple.100, border purple.200 |
| Algebra bar | pink.600 → pink.400 | pink.300 → pink.400 |

![lesson frame, light](components/crops/lesson-frame-light.png)
![interactive, light](components/crops/lesson-interactive-light.png)
![interactive with answer placed, dark](components/crops/lesson-interactive-dark.png)

#### Lesson feedback

| State | Panel | Tutor bubble | Footer |
|---|---|---|---|
| Correct | border green.700 plus `borderGlow` 1s | green.800, border green.700 | "Why?" secondary, "Continue" green button3d |
| Retry | border yellow.700, `shakeX .45s` | yellow.700 | "Get help" secondary, "Try again" yellow button3d |
| Neutral (tutor) | unchanged | `component.lesson.bubble-tutor` #172326e0, border #3e6a74 | n/a |

Tutor bubbles have radius 16 16 16 4 and padding 12 20, 16/24 500. The answer row gets a check or cross badge at its corner.

![correct badge](components/crops/lesson-answer-correct-badge-dark.png)
![retry badge](components/crops/lesson-answer-retry-badge-dark.png)

#### Koji tutor chat

A 400px column slides in from the left while the lesson panel moves right, using `--spring-smooth` over .833s. Messages: tutor (radius 16 16 16 4), user (right-aligned, `bg.tertiary`, 16 all round), and fading older messages at opacity .5. The board highlight is a pulsing `0 0 8px 0 rgba(255,255,255,.6)` glow.

![tutor chat panel](components/crops/tutor-chat-panel-dark.png)
![tutor board highlight](components/crops/tutor-highlight-dark.png)
![Koji question line](components/crops/koji-question-dark.png)

#### Weekly summary, stat cards and bar chart

Weekly summary: radius 20, 2px `border.primary`, `gradient` from `autoflip.green.100` to `autoflip.green.50`, Koji peeking bottom-left. Bar chart bars are plain divs in `bg.blue-primary`, radius 4 on top corners, a 2px bar for zero, with an accessible table underneath. Tokens: `component.chart.bar`.

Strength chip: h40, radius full, 1px border, delta pill `body.xs` 700 on `bg.green-secondary`.

![weekly summary, light](components/crops/weekly-summary-light.png)
![weekly summary, dark](components/crops/weekly-summary-dark.png)
![stat cards, dark](components/crops/segmented-and-stats-dark.png)

#### Pricing and Free vs Premium comparison

Hero: CoFo Robert 60/66 500 (`typography.display.5xl`) over `gradient.paywall-iridescent-bg-flipped`. Plan cards are a radio group (330x129), the checked one framed in `gradient.iridescent-frame` with a "MOST POPULAR" tab and Koji peeking over it (frame estimated from screenshot). The comparison table heading clips "Premium" to the iridescent gradient, and the Premium column is framed in the same gradient (about 4px, radius 16, estimated from screenshot).

![pricing hero, light](components/crops/pricing-hero-light.png)
![pricing hero, dark](components/crops/pricing-hero-dark.png)
![comparison, light](components/crops/premium-comparison-light.png)
![comparison, dark](components/crops/premium-comparison-dark.png)

#### Public header and landing CTAs

Public header: logo, nav, "Sign in" outline and "Sign up" green buttons. Landing CTAs are h60 pills, `ui.actions.lg` 20/25 500, `0 4px 7px 0 rgba(0,0,0,.05)`: green "I'm a learner" and white "I'm a parent or teacher".

![public header](components/crops/public-header-light.png)
![landing CTAs](components/crops/landing-ctas-light.png)

#### Legacy 404

The old Django UI, not part of the Panda system: h1 22/30.8 500 #333, body 15/24, "Go home" pill #f0f0f0. Kept for completeness.

![404](components/crops/notfound-legacy-light.png)

### Icons

App icons are a custom set of filled glyphs drawn at 16 (nav, menu), 24 (stats), 32 (XP) and 48 (lesson rail), all `fill="currentColor"` except the gold key. They were saved by hand from the signed-in pages into [icons/app/](icons/app), named by role and size.

| File | Where |
|---|---|
| `nav-home-16`, `nav-courses-16`, `nav-you-16` | app header tabs |
| `menu-16` | header menu trigger |
| `stat-key-24` (#f7c325), `stat-streak-bolt-24` | header stat pills |
| `xp-sparkle-32` | lesson XP counter |
| `lesson-report-flag-48`, `lesson-sound-48`, `lesson-chat-48`, `lesson-mic-18` | lesson rail and Koji dock |
| `play-16`, `close-16`, `arrow-up-16`, `arrow-down-16` | voice sample, close, strength deltas |

[icons/public/](icons/public) holds 32 SVGs pulled from the public pages by a script, named by content hash:

| Files | What | Size | Style |
|---|---|---|---|
| `91a27c79f8`, `35bbde23a3` | nav "Courses", "Next" chevron | 16, 12 | fill, currentColor black |
| `c29b0a1931`, `e950fc5c01` | course meta: lessons, exercises | 16 | fill |
| `93e06c447c`, `4fc06a14a3`, `38197ce722`, `197d4e7d65` | footer Facebook, Instagram, Twitter, LinkedIn | 20–22 | fill #999 |
| `f65ff86b03`, `9f2b7ed8f1` | Google and Apple login | 20, 17 | fill, brand colours |
| `b4ce175fcd`, `c6f4f6cb5b` | landing video pause and play | 16 | fill 30% black |
| `5ed2cd3d2e` | Koji peeking over the plan card | 40x26 | fill |
| `b7865a5607`, `6b48e24473`, `a38292d801`, `5baf88ce65`, `61a5187a65` | pricing feature list icons | 20–24 | fill with gradients |
| `13e7b9f445`, `2239dabbae`, `9d5342950c`, `f78cff109f` | pricing benefits | 32 | stroke 2.4px plus fills |
| `0cfb527962`, `f9abc0b2e7`, `c8b322698c`, `1c94002d26` | pricing tab icons | 20 | fill 60% black |
| `abefb23ce2`, `829a917deb`, `063a2fb769`, `0aa9540d2a`, `64e87ab675`, `b84ae4c3e9` | testimonial avatars (illustrated) | 28 | fill with stroke ring |

Course art, path nodes and Koji are raster or complex illustrations and are not included. All icons are Brilliant's property, kept for reference only.

## Gaps

What could not be captured, and why. Updated 2026-10-17; rows the recapture closed are gone (light theme for the quit dialog, the signed-in phone width, the Settings Premium tab, and button3d hover and pressed, which are now measured).

| Gap | Reason | What stands in |
|---|---|---|
| Toasts | Sonner is mounted, but no look-only action fires a toast; starring a topic or saving a setting would change the account | none |
| Select, checkbox | No reached screen renders one; the stylesheet defines `select-icon`, `checkbox` and `checkbox-indicator` slots | n/a |
| Form validation error | Errors appear only after a submit, and no form was submitted (the login field shows nothing on blur; clearing a settings field was not attempted because it could save) | the stylesheet's invalid rules: `outline-color: border.danger-primary` and `text.danger-primary` |
| In-app paywall | The onboarding paywall auto-advanced in 2026-09 | the same Free vs Premium table on `/subscribe/`, measured headless in both themes |
| Koji prompt suggestion cards | Drawn on a `<canvas>`, so there is no DOM to read | values estimated from screenshot |
| Lesson interactive in the 2026-10 copies | `<custom-interactive>` renders in a shadow root, which a DOM copy does not carry, so lesson copies show an empty frame | the 2026-09 lesson screenshots and `component.lesson.*` tokens |
| Light theme: onboarding, promo, plan, learning path | Onboarding runs once per account | tokens cover both themes; the components reappear on light pages |
| Lesson completion screen, lesson plan steps | Not reached on a new account without answering lessons | none |
| Focus on menu items, segments, text areas, cards, header tabs | The product draws no focus ring there: menu items show `bg.hover`, header tabs and cards fall back to the browser's own ring, segments and the Koji text area show nothing | recorded as measured in the specs |
| Duration tokens | Panda's `trs-dur_fast` and `normal` compile to invalid CSS in production, so no duration variable exists | `duration` lists the durations actually used in transitions |
| High-contrast theme | The product has none; only Auto, Light, Dark and Reduce motion | n/a |
| Proprietary fonts | CoFo Brilliant, CoFo Robert, CoFo Semi Mono are licensed and not committed | the style guide falls back to Figtree and Georgia |
| Legacy pages (`/account/`) | Old Django UI, not on the Panda tokens | documented separately above |
| Cookie banner, bug-report widget | OneTrust and Shake are third party (the lesson's report flag opens Shake's own form) | hidden during capture, not documented |
