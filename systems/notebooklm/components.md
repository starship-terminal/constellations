# NotebookLM components

Built by `tools/build_components_md.py` from [raw/components-computed.json](raw/components-computed.json) (computed styles read on 2026-10-17 from redacted copies of the signed-in app, every state in dark and light) and [tokens.json](tokens.json). Every value below is the token that holds it; a value no token holds is written raw and marked `(raw)`. One token name covers both themes, since each semantic token resolves per theme; where the two themes land on different tokens the cell reads `dark / light`. Colour tokens without a set prefix are in the `light` and `dark` sets; `core.palette.*`, `radius.*`, `spacing.*`, `size.*`, `typography.*`, `focusRing.*`, `borderWidth.*` and `opacity.*` are in `core`.

States are real: `hover` is a pointer hover, `focus-visible` a keyboard focus (Shift+Tab, Tab), `pressed` the mouse held down, each in headless Chromium on the static copy. Other states (`selected`, `open`, `typed`, `error`, `disabled`, ...) are other elements or other copies captured in that state. The full per-state property tables are in [raw/measurements.md](raw/measurements.md).

## Discovery

| Checklist component | Entry | States measured |
|---|---|---|
| Button | [Accent button (New notebook)](#button-accent), [Tonal button (Add sources)](#button-tonal), [Text button (Create notebook, header)](#button-text), [Outlined button (Upload files)](#button-outlined), [Dialog confirm button (Save, Configure Chat)](#button-dialog-primary), [Disabled filled button (Insert)](#button-disabled), [Delete confirmation buttons (Delete)](#button-confirm-delete) | default, hover, focus-visible, pressed, cancel, cancel-focus-visible, cancel-hover, disabled |
| Icon button | [Icon button (Settings, 36px)](#icon-button), [Icon button, small (card actions, 28px)](#icon-button-small) | default, hover, focus-visible, pressed |
| Link | [Link (Learn more, Notifications dialog)](#link), [Inline link in help text (learn more)](#link-inline) | default, hover, focus-visible |
| Text field | [Text field (Add people and groups)](#text-field), [Search field (expanded header search)](#search-field) | default, hover, focus-visible, typed |
| Text area | [Text area (chat composer)](#text-area), [Text area, outlined (Website URLs)](#text-area-outlined), [Text area with counter (Custom chat prompt)](#text-area-custom) | default, hover, focus-visible, error, typed |
| Select | [Select (Notebook access)](#select), [Menu trigger (Web source type)](#menu-trigger) | default, hover, focus-visible, pressed, open, option, option-hover, option-selected |
| Checkbox | [Checkbox (source row, checked)](#checkbox) | default, hover, focus-visible, notify-checked |
| Radio | [Radio group drawn as toggle chips (Configure Chat)](#radio) | default, hover, focus-visible, pressed, group, selected |
| Switch | [Switch (Web notifications, off and disabled)](#switch) | default, hover |
| Tabs | [Header tab (All, My notebooks, Discover, Collections)](#tab), [Segmented control (Grid view, List view)](#segmented), [Panel tab at 390 (Sources, Chat, Studio)](#mobile-tab) | default, hover, focus-visible, pressed, bar, group, selected |
| Menu | [Menu (notebook card actions)](#menu), [Menu (Settings) and its Theme submenu](#menu-settings) | default, item, item-focus-visible, item-hover, item-pressed, submenu |
| Tooltip | [Tooltip](#tooltip) | default |
| Dialog | [Dialog (Delete this notebook?)](#dialog), [Dialog, large (Configure Chat)](#dialog-large), [Announcement dialog (what is new)](#dialog-announcement), [Dialog scrim](#scrim) | default |
| Toast | [Toast (Failed to copy.)](#toast) | default |
| Card | [Notebook card](#card), [Studio tile (Audio Overview)](#studio-tile) | default, hover, focus-visible, pressed |
| List row | [List row (source)](#list-row), [List row (Studio output)](#list-row-output), [User chat bubble](#chat-bubble) | default, hover, focus-visible, pressed |
| Table | [Table row (notebook list view)](#table-row), [Table header row](#table-header), [Notebook row at 390](#mobile-list-row) | default, hover |
| Avatar | [Avatar (account, 32px)](#avatar) | default |
| Badge | [Badge (PRO)](#badge-pro), [Badge (New! on a Studio tile)](#badge-new), [Status chip (Blocked by browser)](#status-chip) | default |

## Buttons

<a id="button-accent"></a>
### Accent button (New notebook)

nb-button type accent: the one filled page action.

![button-accent default](components/crops/button-accent-default.png) ![button-accent hover](components/crops/button-accent-hover.png) ![button-accent focus-visible](components/crops/button-accent-focus-visible.png) ![button-accent pressed](components/crops/button-accent-pressed.png) ![button-accent light](components/crops/button-accent-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 147 x `size.control-compact` | 147 x `size.control-compact` | 147 x `size.control-compact` | 147 x `size.control-compact` |
| Fill | `accent.default` / `surface.accent` | `accent.default` / `surface.accent` | `accent.default` / `surface.accent` | `accent.default` / `surface.accent` |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 0 `spacing.12` 0 `spacing.8` | 0 `spacing.12` 0 `spacing.8` | 0 `spacing.12` 0 `spacing.8` | 0 `spacing.12` 0 `spacing.8` |
| State layer | none | `surface.inverse` at `opacity.hover` | none | `surface.inverse` at `opacity.pressed` |
| Focus ring | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none |

<a id="button-tonal"></a>
### Tonal button (Add sources)

mat-tonal-button, full panel width.

![button-tonal default](components/crops/button-tonal-default.png) ![button-tonal hover](components/crops/button-tonal-hover.png) ![button-tonal focus-visible](components/crops/button-tonal-focus-visible.png) ![button-tonal pressed](components/crops/button-tonal-pressed.png) ![button-tonal light](components/crops/button-tonal-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x `size.control-compact` | 336 x `size.control-compact` | 336 x `size.control-compact` | 336 x `size.control-compact` |
| Fill | `surface.card` | `surface.card` | `surface.card` | `surface.card` |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 0 `spacing.12` 0 `spacing.8` | 0 `spacing.12` 0 `spacing.8` | 0 `spacing.12` 0 `spacing.8` | 0 `spacing.12` 0 `spacing.8` |
| State layer | none | `surface.inverse` at `opacity.hover` | none | `surface.inverse` at `opacity.pressed` |
| Focus ring | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none |

<a id="button-text"></a>
### Text button (Create notebook, header)

![button-text default](components/crops/button-text-default.png) ![button-text hover](components/crops/button-text-hover.png) ![button-text focus-visible](components/crops/button-text-focus-visible.png) ![button-text pressed](components/crops/button-text-pressed.png) ![button-text light](components/crops/button-text-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171 x `size.control-compact` | 171 x `size.control-compact` | 171 x `size.control-compact` | 171 x `size.control-compact` |
| Fill | none | none | none | none |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 0 `spacing.16` 0 `spacing.12` | 0 `spacing.16` 0 `spacing.12` | 0 `spacing.16` 0 `spacing.12` | 0 `spacing.16` 0 `spacing.12` |
| State layer | none | `surface.inverse` at `opacity.hover` | none | `surface.inverse` at `opacity.pressed` |
| Focus ring | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none |

<a id="button-outlined"></a>
### Outlined button (Upload files)

![button-outlined default](components/crops/button-outlined-default.png) ![button-outlined hover](components/crops/button-outlined-hover.png) ![button-outlined focus-visible](components/crops/button-outlined-focus-visible.png) ![button-outlined pressed](components/crops/button-outlined-pressed.png) ![button-outlined light](components/crops/button-outlined-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140 x `size.control-dialog` | 140 x `size.control-dialog` | 140 x `size.control-dialog` | 140 x `size.control-dialog` |
| Fill | none | `state.hover-on-surface` / `surface.badge` | none | `state.hover-on-surface` / `surface.badge` |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.label-large` | `typography.label-large` | `typography.label-large` | `typography.label-large` |
| Border | `borderWidth.hairline` `border.default` | `borderWidth.hairline` `border.default` | `borderWidth.hairline` `border.default` | `borderWidth.hairline` `border.default` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 6px (raw) 14px (raw) | 6px (raw) 14px (raw) | 6px (raw) 14px (raw) | 6px (raw) 14px (raw) |
| State layer | none | `surface.inverse` at `opacity.hover` | none | `surface.inverse` at `opacity.pressed` |
| Focus ring | none | none | `focusRing.checkbox-width` ring `border.focus-strong` (.mat-focus-indicator) | none |

<a id="button-dialog-primary"></a>
### Dialog confirm button (Save, Configure Chat)

Disabled while the Custom prompt is empty.

![button-dialog-primary default](components/crops/button-dialog-primary-default.png) ![button-dialog-primary hover](components/crops/button-dialog-primary-hover.png) ![button-dialog-primary focus-visible](components/crops/button-dialog-primary-focus-visible.png) ![button-dialog-primary pressed](components/crops/button-dialog-primary-pressed.png) ![button-dialog-primary disabled](components/crops/button-dialog-primary-disabled.png) ![button-dialog-primary light](components/crops/button-dialog-primary-light.png)

| Property | default | hover | focus-visible | pressed | disabled |
|---|---|---|---|---|---|
| Size (w x h) | 80 x `size.control-dialog` | 80 x `size.control-dialog` | 80 x `size.control-dialog` | 80 x `size.control-dialog` | 80 x `size.control-dialog` |
| Fill | `accent.brand` | `accent.brand` | `accent.brand` | `accent.brand` | `state.pressed-on-surface` |
| Text | `text.on-brand` | `text.on-brand` | `text.on-brand` | `text.on-brand` | `text.disabled-button` |
| Type | Google Sans Flex 15px/normal 370 (raw) | Google Sans Flex 15px/normal 370 (raw) | Google Sans Flex 15px/normal 370 (raw) | Google Sans Flex 15px/normal 370 (raw) | Google Sans Flex 15px/normal 370 (raw) |
| Radius | `radius.dialog-button` | `radius.dialog-button` | `radius.dialog-button` | `radius.dialog-button` | `radius.dialog-button` |
| Padding | 0 `spacing.24` | 0 `spacing.24` | 0 `spacing.24` | 0 `spacing.24` | 0 `spacing.24` |
| State layer | none | `state.brand-layer` at `opacity.hover` / `surface.panel` at `opacity.hover` | none | `state.brand-layer` at `opacity.pressed` / `surface.panel` at `opacity.pressed` | none |
| Focus ring | none | none | `focusRing.checkbox-width` ring `border.focus-strong` (.mat-focus-indicator) | none | none |

<a id="button-disabled"></a>
### Disabled filled button (Insert)

Stays disabled while the URL field is empty or invalid.

![button-disabled default](components/crops/button-disabled-default.png) ![button-disabled light](components/crops/button-disabled-light.png)

| Property | default |
|---|---|
| Size (w x h) | 87 x `size.control-dialog` |
| Fill | `state.pressed-on-surface` |
| Text | `text.disabled-button` |
| Type | Google Sans Flex 15px/normal 370 (raw) |
| Radius | `radius.dialog-button` |
| Padding | 0 `spacing.24` |

<a id="button-confirm-delete"></a>
### Delete confirmation buttons (Delete)

The destructive action is a tonal button; it was never clicked.

![button-confirm-delete default](components/crops/button-confirm-delete-default.png) ![button-confirm-delete hover](components/crops/button-confirm-delete-hover.png) ![button-confirm-delete focus-visible](components/crops/button-confirm-delete-focus-visible.png) ![button-confirm-delete pressed](components/crops/button-confirm-delete-pressed.png) ![button-confirm-delete cancel](components/crops/button-confirm-delete-cancel.png) ![button-confirm-delete cancel-focus-visible](components/crops/button-confirm-delete-cancel-focus-visible.png) ![button-confirm-delete light](components/crops/button-confirm-delete-light.png)

| Property | default | hover | focus-visible | pressed | cancel | cancel-focus-visible | cancel-hover |
|---|---|---|---|---|---|---|---|
| Size (w x h) | 76 x `size.control-medium` | 76 x `size.control-medium` | 76 x `size.control-medium` | 76 x `size.control-medium` | 79 x `size.control-medium` | 79 x `size.control-medium` | 79 x `size.control-medium` |
| Fill | `surface.card` | `surface.card` | `surface.card` | `surface.card` | none | none | none |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 0 `spacing.16` | 0 `spacing.16` | 0 `spacing.16` | 0 `spacing.16` | 0 `spacing.16` | 0 `spacing.16` | 0 `spacing.16` |
| State layer | none | none | none | `surface.inverse` at `opacity.pressed` | none | none | `surface.inverse` at `opacity.hover` |
| Focus ring | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none |

<a id="icon-button"></a>
### Icon button (Settings, 36px)

![icon-button default](components/crops/icon-button-default.png) ![icon-button hover](components/crops/icon-button-hover.png) ![icon-button focus-visible](components/crops/icon-button-focus-visible.png) ![icon-button pressed](components/crops/icon-button-pressed.png) ![icon-button light](components/crops/icon-button-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x `size.control-compact` | 36 x `size.control-compact` | 36 x `size.control-compact` | 36 x `size.control-compact` |
| Fill | none | none | none | none |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 6px (raw) | 6px (raw) | 6px (raw) | 6px (raw) |
| State layer | none | `surface.inverse` at `opacity.hover` | none | `surface.inverse` at `opacity.pressed` |
| Focus ring | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none |

<a id="icon-button-small"></a>
### Icon button, small (card actions, 28px)

![icon-button-small default](components/crops/icon-button-small-default.png) ![icon-button-small hover](components/crops/icon-button-small-hover.png) ![icon-button-small focus-visible](components/crops/icon-button-small-focus-visible.png) ![icon-button-small pressed](components/crops/icon-button-small-pressed.png) ![icon-button-small light](components/crops/icon-button-small-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x `size.tab-mobile` | 28 x `size.tab-mobile` | 28 x `size.tab-mobile` | 28 x `size.tab-mobile` |
| Fill | none | none | none | none |
| Text | `text.disabled-button` | `text.disabled-button` | `text.disabled-button` | `text.disabled-button` |
| Type | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | `spacing.2` | `spacing.2` | `spacing.2` | `spacing.2` |
| State layer | none | `state.disabled-content` at `opacity.hover` | none | `state.disabled-content` at `opacity.pressed` |
| Focus ring | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none |

<a id="search-pill"></a>
### Search pill (outlined button that opens search)

![search-pill default](components/crops/search-pill-default.png) ![search-pill hover](components/crops/search-pill-hover.png) ![search-pill focus-visible](components/crops/search-pill-focus-visible.png) ![search-pill pressed](components/crops/search-pill-pressed.png) ![search-pill light](components/crops/search-pill-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 256 x `size.control-compact` | 256 x `size.control-compact` | 256 x `size.control-compact` | 256 x `size.control-compact` |
| Fill | none | none | none | none |
| Text | `text.secondary` | `text.secondary` | `text.secondary` | `text.secondary` |
| Type | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` |
| Border | `borderWidth.hairline` `border.default` | `borderWidth.hairline` `border.default` | `borderWidth.hairline` `border.default` | `borderWidth.hairline` `border.default` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 0 `spacing.12` 0 `spacing.8` | 0 `spacing.12` 0 `spacing.8` | 0 `spacing.12` 0 `spacing.8` | 0 `spacing.12` 0 `spacing.8` |
| Focus ring | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none |

## Links

<a id="link"></a>
### Link (Learn more, Notifications dialog)

![link default](components/crops/link-default.png) ![link hover](components/crops/link-hover.png) ![link focus-visible](components/crops/link-focus-visible.png) ![link light](components/crops/link-light.png)

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 76 x 18px | 76 x 18px | 76 x 18px |
| Fill | none | none | none |
| Text | `text.link` | `text.link` | `text.link` |
| Type | Google Sans Flex 14px/21px 400 (raw) | Google Sans Flex 14px/21px 400 (raw) | Google Sans Flex 14px/21px 400 (raw) |
| Focus ring | none | none | browser default ring (outline auto), no product ring |

<a id="link-inline"></a>
### Inline link in help text (learn more)

![link-inline default](components/crops/link-inline-default.png) ![link-inline hover](components/crops/link-inline-hover.png) ![link-inline focus-visible](components/crops/link-inline-focus-visible.png) ![link-inline light](components/crops/link-inline-light.png)

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 64 x 15px | 64 x 15px | 64 x 15px |
| Fill | none | none | none |
| Text | `border.focus-strong` / `text.link` | `border.focus-strong` / `text.link` | `border.focus-strong` / `text.link` |
| Type | Google Sans Flex 12px/20px 400 (raw) | Google Sans Flex 12px/20px 400 (raw) | Google Sans Flex 12px/20px 400 (raw) |
| Focus ring | none | none | browser default ring (outline auto), no product ring |

## Inputs

<a id="text-field"></a>
### Text field (Add people and groups)

![text-field default](components/crops/text-field-default.png) ![text-field hover](components/crops/text-field-hover.png) ![text-field focus-visible](components/crops/text-field-focus-visible.png) ![text-field light](components/crops/text-field-light.png)

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 386 x `size.field` | 386 x `size.field` | 386 x `size.field` |
| Fill | none | none | none |
| Text | rgba(233,233,233,0.92) (raw) / `text.primary` | `text.primary` | `text.primary` |
| Type | Google Sans Flex 17px/normal 400 (raw) | Google Sans Flex 17px/normal 400 (raw) | Google Sans Flex 17px/normal 400 (raw) |
| Border | `borderWidth.hairline` `border.subtle` (div) | `borderWidth.hairline` `border.field` (div) | `borderWidth.field-focus` `border.field` (div) |
| Focus ring | none | none | outline thickens to `borderWidth.field-focus` `border.field` |

<a id="search-field"></a>
### Search field (expanded header search)

![search-field default](components/crops/search-field-default.png) ![search-field hover](components/crops/search-field-hover.png) ![search-field focus-visible](components/crops/search-field-focus-visible.png) ![search-field typed](components/crops/search-field-typed.png) ![search-field light](components/crops/search-field-light.png)

| Property | default | hover | focus-visible | typed |
|---|---|---|---|---|
| Size (w x h) | 650 x 44px | 650 x 44px | 650 x 44px | 650 x 44px |
| Fill | `surface.panel` (inner) | `surface.panel` (inner) | `surface.panel` (inner) | `surface.panel` |
| Text | `text.secondary` | `text.secondary` | `text.secondary` | `text.secondary` |
| Type | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` |
| Radius | 0 | 0 | 0 | `radius.full` |
| Padding | 0 | 0 | 0 | 0 `spacing.4` 0 `spacing.8` |
| Shadow | none | none | none | `shadow.level1` |

<a id="text-area"></a>
### Text area (chat composer)

A cdk-autosize <textarea> inside the rounded composer.

![text-area default](components/crops/text-area-default.png) ![text-area hover](components/crops/text-area-hover.png) ![text-area focus-visible](components/crops/text-area-focus-visible.png) ![text-area typed](components/crops/text-area-typed.png) ![text-area light](components/crops/text-area-light.png)

| Property | default | hover | focus-visible | typed |
|---|---|---|---|---|
| Size (w x h) | 628 x `size.composer` | 628 x `size.composer` | 628 x `size.composer` | 628 x `size.composer` |
| Fill | `surface.panel` | `surface.panel` | `surface.panel` | `surface.panel` |
| Text | `text.disabled-button` | `text.disabled-button` | `text.disabled-button` | `text.body` |
| Type | `typography.body-small` | `typography.body-small` | `typography.body-small` | Google Sans Flex 16px/24px 400 (raw) |
| Radius | `radius.xl-increased` | `radius.xl-increased` | `radius.xl-increased` | `radius.xl-increased` |
| Padding | `spacing.12` | `spacing.12` | `spacing.12` | `spacing.12` |
| Shadow | `shadow.level1` | `shadow.level1` | `shadow.level1` | `shadow.level1` |

<a id="text-area-outlined"></a>
### Text area, outlined (Website URLs)

![text-area-outlined default](components/crops/text-area-outlined-default.png) ![text-area-outlined hover](components/crops/text-area-outlined-hover.png) ![text-area-outlined focus-visible](components/crops/text-area-outlined-focus-visible.png) ![text-area-outlined error](components/crops/text-area-outlined-error.png) ![text-area-outlined typed](components/crops/text-area-outlined-typed.png) ![text-area-outlined light](components/crops/text-area-outlined-light.png)

| Property | default | hover | focus-visible | error | typed |
|---|---|---|---|---|---|
| Size (w x h) | 626 x 220px | 626 x 220px | 626 x 220px | 626 x 220px | 626 x 220px |
| Fill | none | none | none | none | none |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-large` | `typography.body-large` | `typography.body-large` | `typography.body-large` | `typography.body-large` |
| Border | `borderWidth.hairline` `border.subtle` (div) | `borderWidth.hairline` `border.field` (div) | `borderWidth.field-focus` `border.field` (div) | `borderWidth.hairline` `border.error` (div) | `borderWidth.field-focus` `border.field` (div) |
| Focus ring | none | none | outline thickens to `borderWidth.field-focus` `border.field` | none | none |

<a id="error-text"></a>
### Field error message

![error-text default](components/crops/error-text-default.png) ![error-text light](components/crops/error-text-light.png)

| Property | default |
|---|---|
| Size (w x h) | 594 x 20px |
| Fill | none |
| Text | `text.error` |
| Type | Google Sans Flex 13px/16px 400 (raw) |

<a id="text-area-custom"></a>
### Text area with counter (Custom chat prompt)

![text-area-custom default](components/crops/text-area-custom-default.png) ![text-area-custom hover](components/crops/text-area-custom-hover.png) ![text-area-custom focus-visible](components/crops/text-area-custom-focus-visible.png) ![text-area-custom light](components/crops/text-area-custom-light.png)

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 808 x 124px | 808 x 124px | 808 x 124px |
| Fill | none | none | none |
| Text | `text.body` | `text.body` | `text.body` |
| Type | Google Sans Flex 13px/16px 400 (raw) | Google Sans Flex 13px/16px 400 (raw) | Google Sans Flex 13px/16px 400 (raw) |
| Border | `borderWidth.hairline` `border.subtle` (div) | `borderWidth.hairline` `border.field` (div) | `borderWidth.field-focus` `border.field` (div) |
| Focus ring | none | none | outline thickens to `borderWidth.field-focus` `border.field` |

<a id="select"></a>
### Select (Notebook access)

![select default](components/crops/select-default.png) ![select hover](components/crops/select-hover.png) ![select focus-visible](components/crops/select-focus-visible.png) ![select open](components/crops/select-open.png) ![select option](components/crops/select-option.png) ![select option-hover](components/crops/select-option-hover.png) ![select light](components/crops/select-light.png)

| Property | default | hover | focus-visible | open | option | option-hover | option-selected |
|---|---|---|---|---|---|---|---|
| Size (w x h) | 212 x 24px | 212 x 24px | 212 x 24px | 212 x 160px | 212 x `size.control-medium` | 212 x `size.control-medium` | 212 x `size.control-medium` |
| Fill | none | none | none | `surface.panel` | `surface.panel` (on parent) | `state.hover-on-surface` / `surface.badge` | `state.pressed-on-surface` |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | Google Sans Flex 14px/24px 400 (raw) | Google Sans Flex 14px/24px 400 (raw) | Google Sans Flex 14px/24px 400 (raw) | Google Sans Flex 16px/20px 400 (raw) | Google Sans Flex 16px/20px 400 (raw) | Google Sans Flex 16px/20px 400 (raw) | Google Sans Flex 16px/20px 400 (raw) |
| Border | none | none | none | `borderWidth.field-focus` #c2e7ff (raw) (mat-pseudo-checkbox) / `borderWidth.field-focus` #004a77 (raw) (mat-pseudo-checkbox) | none | none | `borderWidth.field-focus` #c2e7ff (raw) (mat-pseudo-checkbox) / `borderWidth.field-focus` #004a77 (raw) (mat-pseudo-checkbox) |
| Padding | 0 | 0 | 0 | `spacing.8` 0 | 0 `spacing.16` | 0 `spacing.16` | 0 `spacing.16` |
| Shadow | none | none | none | `shadow.select` | none | none | none |

<a id="menu-trigger"></a>
### Menu trigger (Web source type)

![menu-trigger default](components/crops/menu-trigger-default.png) ![menu-trigger hover](components/crops/menu-trigger-hover.png) ![menu-trigger focus-visible](components/crops/menu-trigger-focus-visible.png) ![menu-trigger pressed](components/crops/menu-trigger-pressed.png) ![menu-trigger light](components/crops/menu-trigger-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102 x `size.control-compact` | 102 x `size.control-compact` | 102 x `size.control-compact` | 102 x `size.control-compact` |
| Fill | `surface.panel` | `surface.panel` | `surface.panel` | `surface.panel` |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` | `typography.body-medium` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 0 `spacing.12` | 0 `spacing.12` | 0 `spacing.12` | 0 `spacing.12` |
| State layer | none | `surface.inverse` at `opacity.hover` | none | `surface.inverse` at `opacity.pressed` |
| Focus ring | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none |

<a id="checkbox"></a>
### Checkbox (source row, checked)

![checkbox default](components/crops/checkbox-default.png) ![checkbox hover](components/crops/checkbox-hover.png) ![checkbox focus-visible](components/crops/checkbox-focus-visible.png) ![checkbox notify-checked](components/crops/checkbox-notify-checked.png) ![checkbox light](components/crops/checkbox-light.png)

| Property | default | hover | focus-visible | notify-checked |
|---|---|---|---|---|
| Size (w x h) | 32 x `size.checkbox-target` | 32 x `size.checkbox-target` | 32 x `size.checkbox-target` | 30 x 30px |
| Fill | none | none | none | none |
| Text | `text.body` | `text.body` | `text.body` | `text.body` |
| Type | Times 16px/normal 400 (raw) | Times 16px/normal 400 (raw) | Times 16px/normal 400 (raw) | Times 16px/normal 400 (raw) |
| State layer | none | `surface.inverse` at `opacity.hover` | `surface.inverse` at `opacity.pressed` | none |
| Focus ring | none | none | browser default ring on input (outline auto), no product ring | none |

<a id="radio"></a>
### Radio group drawn as toggle chips (Configure Chat)

mat-button-toggle-group with role radiogroup; each chip is a role=radio button. The checked chip gains a leading check.

![radio default](components/crops/radio-default.png) ![radio hover](components/crops/radio-hover.png) ![radio focus-visible](components/crops/radio-focus-visible.png) ![radio pressed](components/crops/radio-pressed.png) ![radio group](components/crops/radio-group.png) ![radio selected](components/crops/radio-selected.png) ![radio light](components/crops/radio-light.png)

| Property | default | hover | focus-visible | pressed | group | selected |
|---|---|---|---|---|---|---|
| Size (w x h) | 127 x `size.control-dialog` | 127 x `size.control-dialog` | 127 x `size.control-dialog` | 127 x `size.control-dialog` | 816 x 50px | 103 x `size.control-dialog` |
| Fill | none | none | none | none | `accent.brand` (inner) | `accent.brand` (on parent) |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.on-brand` | `text.on-brand` |
| Type | Google Sans Flex 15px/40px 370 (raw) | Google Sans Flex 15px/40px 370 (raw) | Google Sans Flex 15px/40px 370 (raw) | Google Sans Flex 15px/40px 370 (raw) | Google Sans Flex 15px/40px 370 (raw) | Google Sans Flex 15px/40px 370 (raw) |
| Border | `borderWidth.field-focus` `text.on-brand` (mat-pseudo-checkbox) / `borderWidth.field-focus` `state.brand-layer` (mat-pseudo-checkbox) | `borderWidth.field-focus` `text.on-brand` (mat-pseudo-checkbox) / `borderWidth.field-focus` `state.brand-layer` (mat-pseudo-checkbox) | `borderWidth.field-focus` `text.on-brand` (mat-pseudo-checkbox) / `borderWidth.field-focus` `state.brand-layer` (mat-pseudo-checkbox) | `borderWidth.field-focus` `text.on-brand` (mat-pseudo-checkbox) / `borderWidth.field-focus` `state.brand-layer` (mat-pseudo-checkbox) | `borderWidth.hairline` `border.subtle` (mat-button-toggle) | `borderWidth.field-focus` `text.on-brand` (mat-pseudo-checkbox) / `borderWidth.field-focus` `state.brand-layer` (mat-pseudo-checkbox) |
| Radius | 0 | 0 | 0 | 0 | `radius.lg-max` | 0 |
| Padding | 0 | 0 | 0 | 0 | 0 | 0 0 0 30px (raw) |
| Focus ring | none | none | `focusRing.checkbox-width` ring `border.focus-strong` (.mat-focus-indicator) | none | none | none |

<a id="switch"></a>
### Switch (Web notifications, off and disabled)

Disabled because the browser blocks notifications; no enabled switch appeared.

![switch default](components/crops/switch-default.png) ![switch hover](components/crops/switch-hover.png) ![switch light](components/crops/switch-light.png)

| Property | default | hover |
|---|---|---|
| Size (w x h) | 52 x `size.checkbox-target` | 52 x `size.checkbox-target` |
| Fill | `border.divider-material` (inner) | `border.divider-material` (inner) |
| Text | rgba(255,255,255,0.3) (raw) / rgba(16,16,16,0.3) (raw) | rgba(255,255,255,0.3) (raw) / rgba(16,16,16,0.3) (raw) |
| Type | Arial 13.3333px/normal 400 (raw) | Arial 13.3333px/normal 400 (raw) |
| Border | `borderWidth.field-focus` `border.field` (span) | `borderWidth.field-focus` `border.field` (span) |

<a id="progress"></a>
### Progress bar (source limit)

![progress default](components/crops/progress-default.png) ![progress light](components/crops/progress-light.png)

| Property | default |
|---|---|
| Size (w x h) | 600 x 16px |
| Fill | rgba(163,163,163,0.2) (raw) (inner) |
| Text | `text.primary` |
| Type | `typography.body-medium` |
| Border | 16px (raw) `border.field` (span) |
| Radius | `radius.lg` |

## Navigation

<a id="tab"></a>
### Header tab (All, My notebooks, Discover, Collections)

nb-buttons: the selected one is tonal, the rest text.

![tab default](components/crops/tab-default.png) ![tab hover](components/crops/tab-hover.png) ![tab focus-visible](components/crops/tab-focus-visible.png) ![tab pressed](components/crops/tab-pressed.png) ![tab selected](components/crops/tab-selected.png) ![tab light](components/crops/tab-light.png)

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 44 x `size.control-compact` | 44 x `size.control-compact` | 44 x `size.control-compact` | 44 x `size.control-compact` | 110 x `size.control-compact` |
| Fill | none | none | none | none | `surface.card` |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-small` | `typography.body-small` | `typography.body-small` | `typography.body-small` | `typography.body-small` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 0 `spacing.12` | 0 `spacing.12` | 0 `spacing.12` | 0 `spacing.12` | 0 `spacing.12` |
| State layer | none | `surface.inverse` at `opacity.hover` | none | `surface.inverse` at `opacity.pressed` | none |
| Focus ring | none | none | `focusRing.width` `border.field` offset `focusRing.offset` / 3px solid `border.field` on button | none | none |

<a id="segmented"></a>
### Segmented control (Grid view, List view)

![segmented default](components/crops/segmented-default.png) ![segmented hover](components/crops/segmented-hover.png) ![segmented focus-visible](components/crops/segmented-focus-visible.png) ![segmented pressed](components/crops/segmented-pressed.png) ![segmented group](components/crops/segmented-group.png) ![segmented selected](components/crops/segmented-selected.png) ![segmented light](components/crops/segmented-light.png)

| Property | default | hover | focus-visible | pressed | group | selected |
|---|---|---|---|---|---|---|
| Size (w x h) | 36 x `size.checkbox-target` | 36 x `size.checkbox-target` | 36 x `size.checkbox-target` | 36 x `size.checkbox-target` | 76 x `size.control-compact` | 36 x `size.checkbox-target` |
| Fill | none | none | none | none | `surface.card` | none |
| Text | `text.secondary` | `text.secondary` | `text.secondary` | `text.secondary` | `text.primary` | `text.primary` |
| Type | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` | icon glyph `size.icon-m` |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 1px (raw) `spacing.8` | 1px (raw) `spacing.8` | 1px (raw) `spacing.8` | 1px (raw) `spacing.8` | `spacing.2` | 1px (raw) `spacing.8` |
| Focus ring | none | none | browser default ring (outline auto), no product ring | none | none | none |

<a id="mobile-tab"></a>
### Panel tab at 390 (Sources, Chat, Studio)

![mobile-tab default](components/crops/mobile-tab-default.png) ![mobile-tab focus-visible](components/crops/mobile-tab-focus-visible.png) ![mobile-tab pressed](components/crops/mobile-tab-pressed.png) ![mobile-tab bar](components/crops/mobile-tab-bar.png) ![mobile-tab selected](components/crops/mobile-tab-selected.png) ![mobile-tab light](components/crops/mobile-tab-light.png)

| Property | default | focus-visible | pressed | bar | selected |
|---|---|---|---|---|---|
| Size (w x h) | 118 x `size.tab-mobile` | 118 x `size.tab-mobile` | 118 x `size.tab-mobile` | 358 x `size.checkbox-target` | 118 x `size.tab-mobile` |
| Fill | `surface.card` (on parent) | `surface.card` (on parent) | `surface.card` (on parent) | `surface.card` | `surface.card` (on parent) |
| Text | `text.secondary` | `text.secondary` | `text.primary` | `text.secondary` | `text.primary` |
| Type | Google Sans Flex 14px/20px 500 (raw) | Google Sans Flex 14px/20px 500 (raw) | Google Sans Flex 14px/20px 500 (raw) | Google Sans Flex 14px/20px 500 (raw) | Google Sans Flex 14px/20px 500 (raw) |
| Radius | `radius.full` | `radius.full` | `radius.full` | `radius.full` | `radius.full` |
| Padding | 0 | 0 | 0 | `spacing.2` | 0 |
| Focus ring | none | browser default ring (outline auto), no product ring | none | none | none |

## Overlays

<a id="menu"></a>
### Menu (notebook card actions)

![menu default](components/crops/menu-default.png) ![menu item](components/crops/menu-item.png) ![menu item-focus-visible](components/crops/menu-item-focus-visible.png) ![menu item-hover](components/crops/menu-item-hover.png) ![menu item-pressed](components/crops/menu-item-pressed.png) ![menu light](components/crops/menu-light.png)

| Property | default | item | item-focus-visible | item-hover | item-pressed |
|---|---|---|---|---|---|
| Size (w x h) | 206 x 160px | 190 x `size.control-compact` | 190 x `size.control-compact` | 190 x `size.control-compact` | 190 x `size.control-compact` |
| Fill | `surface.panel` | `surface.panel` (on parent) | `surface.panel` (on parent) | `state.hover-on-surface` / `surface.badge` | `state.hover-on-surface` / `surface.badge` |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-small` | `typography.body-small` | `typography.body-small` | `typography.body-small` | `typography.body-small` |
| Radius | `radius.lg-increased` | `radius.md` | `radius.md` | `radius.md` | `radius.md` |
| Padding | 0 | `spacing.8` | `spacing.8` | `spacing.8` | `spacing.8` |
| Shadow | `shadow.level1` | none | none | none | none |
| Focus ring | none | none | `focusRing.checkbox-width` ring `border.focus-strong` (.mat-focus-indicator) | none | none |

<a id="menu-settings"></a>
### Menu (Settings) and its Theme submenu

![menu-settings default](components/crops/menu-settings-default.png) ![menu-settings submenu](components/crops/menu-settings-submenu.png) ![menu-settings light](components/crops/menu-settings-light.png)

| Property | default | submenu |
|---|---|---|
| Size (w x h) | 211 x 393px | 129 x 124px |
| Fill | `surface.panel` | `surface.panel` |
| Text | `text.primary` | `text.primary` |
| Type | `typography.body-small` | `typography.body-small` |
| Border | `borderWidth.hairline` `border.divider-material` (mat-divider) | none |
| Radius | `radius.lg-increased` | `radius.lg-increased` |
| Shadow | `shadow.level1` | `shadow.level1` |

<a id="tooltip"></a>
### Tooltip

Its text was scrubbed, since tooltips repeat titles; the live one read "Audio Overview - Generate an AI podcast based on your sources".

![tooltip default](components/crops/tooltip-default.png) ![tooltip light](components/crops/tooltip-light.png)

| Property | default |
|---|---|
| Size (w x h) | 111 x 33px |
| Fill | `surface.inverse` |
| Text | `text.inverse` |
| Type | `typography.body-small` |
| Radius | `radius.md` |
| Padding | `spacing.8` `spacing.16` |

<a id="dialog"></a>
### Dialog (Delete this notebook?)

![dialog default](components/crops/dialog-default.png) ![dialog light](components/crops/dialog-light.png)

| Property | default |
|---|---|
| Size (w x h) | 456 x 224px |
| Fill | `surface.dialog` |
| Text | `text.primary` |
| Type | `typography.headline-small` |
| Radius | `radius.xl` |

<a id="dialog-large"></a>
### Dialog, large (Configure Chat)

| Property | default |
|---|---|
| Size (w x h) | 864 x 482px |
| Fill | `surface.dialog` |
| Text | `text.title` |
| Type | Google Sans Flex 22px/36px 400 (raw) |
| Border | `borderWidth.hairline` `border.subtle` (div) |
| Radius | `radius.xl` |
| State layer | `surface.inverse` at `opacity.pressed` |

<a id="dialog-announcement"></a>
### Announcement dialog (what is new)

| Property | default |
|---|---|
| Size (w x h) | 1000 x 543px |
| Fill | `surface.dialog` |
| Text | `text.title` |
| Type | Google Sans Flex 24px/32px 400 (raw) |
| Border | `borderWidth.hairline` `border.subtle` (div) |
| Radius | `radius.xl` |
| State layer | `surface.inverse` at `opacity.pressed` |

<a id="scrim"></a>
### Dialog scrim

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900px |
| Fill | `bg.scrim` |
| Text | `text.body` |
| Type | Times 16px/normal 400 (raw) |

<a id="toast"></a>
### Toast (Failed to copy.)

The clipboard is blocked in the capture browser, so the copy action reported a failure.

![toast default](components/crops/toast-default.png) ![toast light](components/crops/toast-light.png)

| Property | default |
|---|---|
| Size (w x h) | 344 x `size.control-medium` |
| Fill | `surface.toast` / `surface.inverse` |
| Text | `text.on-toast` |
| Type | `typography.body-medium` |
| Radius | `radius.lg` |
| Padding | 0 `spacing.8` 0 0 |
| Shadow | `shadow.toast` |

## Lists

<a id="card"></a>
### Notebook card

![card default](components/crops/card-default.png) ![card hover](components/crops/card-hover.png) ![card focus-visible](components/crops/card-focus-visible.png) ![card pressed](components/crops/card-pressed.png) ![card light](components/crops/card-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 272 x `size.card-height` | 272 x `size.card-height` | 272 x `size.card-height` | 272 x `size.card-height` |
| Fill | `surface.card` | none | `surface.card` | none |
| Text | `text.body` | `text.body` | `text.body` | `text.body` |
| Type | Times 36px/36px 400 (raw) | Times 36px/36px 400 (raw) | Times 36px/36px 400 (raw) | Times 36px/36px 400 (raw) |
| Radius | `radius.xl-max` | `radius.xl-max` | `radius.xl-max` | `radius.xl-max` |
| Padding | `spacing.container-padding-large` | `spacing.container-padding-large` | `spacing.container-padding-large` | `spacing.container-padding-large` |
| Focus ring | none | none | browser default ring on a (outline auto), no product ring | none |

<a id="studio-tile"></a>
### Studio tile (Audio Overview)

![studio-tile default](components/crops/studio-tile-default.png) ![studio-tile hover](components/crops/studio-tile-hover.png) ![studio-tile focus-visible](components/crops/studio-tile-focus-visible.png) ![studio-tile pressed](components/crops/studio-tile-pressed.png) ![studio-tile light](components/crops/studio-tile-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 164 x `size.control-medium` | 162 x 47px | 164 x `size.control-medium` | 159 x 47px |
| Fill | `surface.card` (inner) / `surface.panel` (inner) | `surface.card` (inner) / `surface.panel` (inner) | `surface.card` (inner) / `surface.panel` (inner) | `surface.card` (inner) / `surface.panel` (inner) |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-small` | `typography.body-small` | `typography.body-small` | `typography.body-small` |
| Border | none / `borderWidth.hairline` `border.default` (inset shadow) | none / `borderWidth.hairline` `border.default` (inset shadow) | none / `borderWidth.hairline` `border.default` (inset shadow) | none / `borderWidth.hairline` `border.default` (inset shadow) |
| Radius | `radius.lg-increased` | `radius.lg-increased` | `radius.lg-increased` | `radius.lg-increased` |
| Padding | `spacing.4` `spacing.12` `spacing.4` `spacing.8` | `spacing.4` `spacing.12` `spacing.4` `spacing.8` | `spacing.4` `spacing.12` `spacing.4` `spacing.8` | `spacing.4` `spacing.12` `spacing.4` `spacing.8` |
| Shadow | rgba(0, 0, 0, 0) 0px 0px 0px 1px inset (raw) / rgba(0, 0, 0, 0.08) 0px 0px 0px 1px inset (raw) | rgba(0, 0, 0, 0) 0px 0px 0px 1px inset (raw) / rgba(0, 0, 0, 0.08) 0px 0px 0px 1px inset (raw) | rgba(0, 0, 0, 0) 0px 0px 0px 1px inset (raw) / rgba(0, 0, 0, 0.08) 0px 0px 0px 1px inset (raw) | rgba(0, 0, 0, 0) 0px 0px 0px 1px inset (raw) / rgba(0, 0, 0, 0.08) 0px 0px 0px 1px inset (raw) |
| Focus ring | none | none | `borderWidth.field-focus` `border.field` offset `focusRing.offset` / 2px solid `border.field` on div | none |

<a id="list-row"></a>
### List row (source)

![list-row default](components/crops/list-row-default.png) ![list-row hover](components/crops/list-row-hover.png) ![list-row focus-visible](components/crops/list-row-focus-visible.png) ![list-row pressed](components/crops/list-row-pressed.png) ![list-row light](components/crops/list-row-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x `size.control-compact` | 336 x `size.control-compact` | 336 x `size.control-compact` | 336 x `size.control-compact` |
| Fill | none | `surface.card` | none | `surface.card` |
| Text | `text.title` | `text.title` | `text.title` | `text.title` |
| Type | Google Sans Flex 14px/24px 400 (raw) | Google Sans Flex 14px/24px 400 (raw) | Google Sans Flex 14px/24px 400 (raw) | Google Sans Flex 14px/24px 400 (raw) |
| Radius | `radius.sm` | `radius.sm` | `radius.sm` | `radius.sm` |
| Padding | 0 `spacing.8` | 0 `spacing.8` | 0 `spacing.8` | 0 `spacing.8` |
| Focus ring | none | none | browser default ring on button (outline auto), no product ring | none |

<a id="list-row-output"></a>
### List row (Studio output)

![list-row-output default](components/crops/list-row-output-default.png) ![list-row-output hover](components/crops/list-row-output-hover.png) ![list-row-output focus-visible](components/crops/list-row-output-focus-visible.png) ![list-row-output pressed](components/crops/list-row-output-pressed.png) ![list-row-output light](components/crops/list-row-output-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x `size.list-row-output` | 336 x `size.list-row-output` | 336 x `size.list-row-output` | 336 x `size.list-row-output` |
| Fill | none | none | none | none |
| Text | `text.primary` | `text.primary` | `text.primary` | `text.primary` |
| Type | `typography.body-small` | `typography.body-small` | `typography.body-small` | `typography.body-small` |
| Radius | `radius.lg-increased` | `radius.lg-increased` | `radius.lg-increased` | `radius.lg-increased` |
| State layer | none | `surface.inverse` at `opacity.hover` | none | `surface.inverse` at `opacity.pressed` |
| Focus ring | none | none | `focusRing.checkbox-width` ring `border.focus-strong` (.mat-focus-indicator) | none |

<a id="chat-bubble"></a>
### User chat bubble

![chat-bubble default](components/crops/chat-bubble-default.png) ![chat-bubble light](components/crops/chat-bubble-light.png)

| Property | default |
|---|---|
| Size (w x h) | 162 x `size.composer` |
| Fill | `surface.card` |
| Text | `text.body` |
| Type | Google Sans Flex 16px/24px 400 (raw) |
| Radius | `radius.xl-max` |

<a id="citation"></a>
### Citation marker

![citation default](components/crops/citation-default.png) ![citation hover](components/crops/citation-hover.png) ![citation focus-visible](components/crops/citation-focus-visible.png) ![citation pressed](components/crops/citation-pressed.png) ![citation light](components/crops/citation-light.png)

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 22 x 22px | 22 x 22px | 22 x 22px | 22 x 22px |
| Fill | `surface.card` | `surface.card` | `surface.card` | `surface.card` |
| Text | `text.disabled-button` | `text.disabled-button` | `text.disabled-button` | `text.disabled-button` |
| Type | Google Sans Flex 11.008px/16px 500 (raw) | Google Sans Flex 11.008px/16px 500 (raw) | Google Sans Flex 11.008px/16px 500 (raw) | Google Sans Flex 11.008px/16px 500 (raw) |
| Radius | `radius.circle` | `radius.circle` | `radius.circle` | `radius.circle` |
| Focus ring | none | none | browser default ring (outline auto), no product ring | none |

## Tables

<a id="table-row"></a>
### Table row (notebook list view)

![table-row default](components/crops/table-row-default.png) ![table-row hover](components/crops/table-row-hover.png) ![table-row light](components/crops/table-row-light.png)

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1392 x `size.table-row` | 1392 x `size.table-row` |
| Fill | none | none |
| Text | `text.primary` | `text.primary` |
| Type | Google Sans Flex 16px/20px 400 (raw) | Google Sans Flex 16px/20px 400 (raw) |
| Border | `borderWidth.hairline` `border.divider` (td) | `borderWidth.hairline` `border.divider` (td) |

<a id="table-header"></a>
### Table header row

![table-header default](components/crops/table-header-default.png) ![table-header light](components/crops/table-header-light.png)

| Property | default |
|---|---|
| Size (w x h) | 1392 x `size.field` |
| Fill | none |
| Text | `text.primary` |
| Type | `typography.label-medium` |
| Border | `borderWidth.hairline` `border.divider` (th) |

<a id="mobile-list-row"></a>
### Notebook row at 390

![mobile-list-row default](components/crops/mobile-list-row-default.png) ![mobile-list-row light](components/crops/mobile-list-row-light.png)

| Property | default |
|---|---|
| Size (w x h) | 342 x `size.table-row` |
| Fill | none |
| Text | `text.primary` |
| Type | Google Sans Flex 16px/20px 400 (raw) |
| Border | `borderWidth.hairline` `border.divider` (td) |

## Display

<a id="avatar"></a>
### Avatar (account, 32px)

The photo was replaced by a grey disc with an L in the copy; size and shape are the product's, the fill is not.

| Property | default |
|---|---|
| Size (w x h) | 40 x `size.control-dialog` |
| Fill | #8a8a8a (raw) (inner) |
| Text | `text.on-brand` |
| Type | Google Sans Text 12px/27px 600 (raw) |
| Border | `borderWidth.hairline` #202124 (raw) (span) |
| Radius | `radius.circle` |
| Padding | `spacing.4` |

<a id="badge-pro"></a>
### Badge (PRO)

![badge-pro default](components/crops/badge-pro-default.png) ![badge-pro light](components/crops/badge-pro-light.png)

| Property | default |
|---|---|
| Size (w x h) | 40 x 24px |
| Fill | `surface.badge` |
| Text | `text.secondary` |
| Type | Google Sans Flex 11px/16px 500 (raw) |
| Radius | `radius.sm` |
| Padding | 0 `spacing.8` |

<a id="badge-new"></a>
### Badge (New! on a Studio tile)

![badge-new default](components/crops/badge-new-default.png) ![badge-new light](components/crops/badge-new-light.png)

| Property | default |
|---|---|
| Size (w x h) | 47 x 24px |
| Fill | `surface.badge` |
| Text | `text.primary` |
| Type | Google Sans Flex 13px/24px 400 (raw) |
| Radius | `radius.full` |
| Padding | 0 `spacing.8` |

<a id="status-chip"></a>
### Status chip (Blocked by browser)

![status-chip default](components/crops/status-chip-default.png) ![status-chip light](components/crops/status-chip-light.png)

| Property | default |
|---|---|
| Size (w x h) | 163 x `size.tab-mobile` |
| Fill | `status.danger.fill` |
| Text | `status.danger.text` |
| Type | Google Sans Flex 12px/20px 400 (raw) |
| Radius | `radius.lg` |
| Padding | `spacing.4` `spacing.12` |

<a id="banner"></a>
### Inline banner (Studio, Try it)

![banner default](components/crops/banner-default.png) ![banner light](components/crops/banner-light.png)

| Property | default |
|---|---|
| Size (w x h) | 336 x `size.list-row-output` |
| Fill | `surface.panel` |
| Text | `text.primary` |
| Type | Google Sans Flex 16px/16px 500 (raw) |
| Radius | `radius.lg` |
| Padding | `spacing.12` |
| Shadow | `shadow.level1` |

<a id="skeleton"></a>
### Loading skeleton row

![skeleton default](components/crops/skeleton-default.png) ![skeleton light](components/crops/skeleton-light.png)

| Property | default |
|---|---|
| Size (w x h) | 1392 x `size.field` |
| Fill | none |
| Text | `text.body` |
| Type | Times 16px/normal 400 (raw) |
| Radius | `radius.xs` |

<a id="empty-state"></a>
### Empty state (No notebooks found)

![empty-state default](components/crops/empty-state-default.png) ![empty-state action](components/crops/empty-state-action.png) ![empty-state action-focus-visible](components/crops/empty-state-action-focus-visible.png) ![empty-state action-hover](components/crops/empty-state-action-hover.png) ![empty-state light](components/crops/empty-state-light.png)

| Property | default | action | action-focus-visible | action-hover |
|---|---|---|---|---|
| Size (w x h) | 1392 x 320px | 134 x `size.control-dialog` | 134 x `size.control-dialog` | 134 x `size.control-dialog` |
| Fill | `surface.empty` | `surface.empty` (on parent) | `surface.empty` (on parent) | `surface.empty` (on parent) |
| Text | `text.primary` | `text.title` | `text.title` | `text.title` |
| Type | Google Sans Flex 24px/32px 400 (raw) | Google Sans Flex 15px/normal 370 (raw) | Google Sans Flex 15px/normal 370 (raw) | Google Sans Flex 15px/normal 370 (raw) |
| Border | `borderWidth.hairline` `border.subtle` (button) | `borderWidth.hairline` `border.subtle` | `borderWidth.hairline` `border.subtle` | `borderWidth.hairline` `border.subtle` |
| Radius | `radius.lg` | 100px (raw) | 100px (raw) | 100px (raw) |
| Padding | 64px (raw) `spacing.16` | 0 `spacing.24` | 0 `spacing.24` | 0 `spacing.24` |
| State layer | none | none | none | `surface.inverse` at `opacity.hover` |
| Focus ring | none | none | `focusRing.checkbox-width` ring `border.focus-strong` (.mat-focus-indicator) | none |

## Shell

<a id="header"></a>
### Page header (home)

| Property | default |
|---|---|
| Size (w x h) | 1440 x `size.composer` |
| Fill | `surface.dialog` |
| Text | `text.title` |
| Type | Google Sans Flex 23px/29px 475 (raw) |

<a id="panel-sources"></a>
### Sources panel

| Property | default |
|---|---|
| Size (w x h) | 354 x 824px |
| Fill | `surface.panel` |
| Text | `text.primary` |
| Type | `typography.body-medium` |
| Radius | `radius.xl-increased` |
| Padding | `spacing.8` |

<a id="panel-chat"></a>
### Chat panel

| Property | default |
|---|---|
| Size (w x h) | 680 x 836px |
| Fill | `surface.dialog` |
| Text | `text.primary` |
| Type | Times 40px/40px 400 (raw) |

<a id="panel-studio"></a>
### Studio panel

| Property | default |
|---|---|
| Size (w x h) | 354 x 824px |
| Fill | `surface.panel` |
| Text | `text.primary` |
| Type | `typography.body-medium` |
| Radius | `radius.xl-increased` |
| Padding | `spacing.8` |

## Type

<a id="type-page-title"></a>
### Page title (My notebooks)

| Property | default |
|---|---|
| Size (w x h) | 154 x `size.checkbox-target` |
| Fill | none |
| Text | `text.title` |
| Type | Google Sans Flex 24px/32px 400 (raw) |

<a id="type-cover-title"></a>
### Notebook cover title

| Property | default |
|---|---|
| Size (w x h) | 592 x 44px |
| Fill | none |
| Text | `text.primary` |
| Type | `typography.display-medium` |

<a id="type-panel-header"></a>
### Panel header (Sources)

| Property | default |
|---|---|
| Size (w x h) | 296 x 20px |
| Fill | none |
| Text | `text.primary` |
| Type | `typography.body-medium` |

<a id="type-dialog-title"></a>
### Dialog title

| Property | default |
|---|---|
| Size (w x h) | 400 x `size.checkbox-target` |
| Fill | none |
| Text | `text.primary` |
| Type | `typography.headline-small` |
| Padding | `spacing.4` 0 |

<a id="type-heading"></a>
### Answer heading

| Property | default |
|---|---|
| Size (w x h) | 550 x 24px |
| Fill | none |
| Text | `text.body` |
| Type | `typography.headline-small` |

<a id="type-body"></a>
### Answer body paragraph

| Property | default |
|---|---|
| Size (w x h) | 550 x 24px |
| Fill | none |
| Text | `text.body` |
| Type | `typography.body-large` |

<a id="type-caption"></a>
### Card meta line (date, source count)

| Property | default |
|---|---|
| Size (w x h) | 76 x 18px |
| Fill | none |
| Text | `text.secondary` |
| Type | `typography.body-medium` |

<a id="type-code"></a>
### Inline code

| Property | default |
|---|---|
| Size (w x h) | 147 x 22px |
| Fill | `surface.card` |
| Text | `text.secondary` |
| Type | Google Sans Code 15px/14px 400 (raw) |
| Radius | `radius.full` |
| Padding | `spacing.4` 6px (raw) |

<a id="type-disclaimer"></a>
### Composer footnote

| Property | default |
|---|---|
| Size (w x h) | 628 x 41px |
| Fill | none |
| Text | `text.secondary` |
| Type | `typography.body-small` |
| Padding | `spacing.12` 0 |

## Gaps

- **Loading in a component**: no button or field showed a spinner; the only loading state captured is the search results skeleton ([skeleton](#skeleton)).
- **Disabled**: captured on the dialog Save and Insert buttons and on the switch (disabled because the browser blocks notifications). No disabled text field, checkbox or menu item appeared.
- **Error**: captured on the Website URL text area and its message ([text-area-outlined](#text-area-outlined), [error-text](#error-text)); no other field validates before submit.
- **Switch on**: the only switch is disabled and off; its on state was not reachable without granting notification permission.
- **Hover on 390 copies** is not measured (no pointer on a phone).
- **Avatar**: the photo was replaced by a grey disc in the copy, so only its size and shape are the product's.
- **Studio outputs** (Audio and Video Overviews, mind map, flashcards, quiz) open player or iframe views that were not recaptured on 2026-10-17; the 2026-09-25 package measured some from screenshots and those readings are not carried over.

Token coverage: 1703 cells name a token, 225 are raw values.
