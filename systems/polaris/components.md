# Polaris components

One entry per component of the archived Polaris React system, each with its source rules, the gallery screenshots and crops that show it and its SVG redraws, then the focus-visible values shared across controls and the Gaps. Moved here on 2026-10-17 from `evidence/component-findings.md` and the README's "Buttons", "Badges, tags and forms" and "Other components" sections, with no new readings.

Source: archived `Shopify/polaris-react-archive` at [`3f7954ae42fabf26d63cee68c23ceebfd7ef0972`](https://github.com/Shopify/polaris-react-archive/tree/3f7954ae42fabf26d63cee68c23ceebfd7ef0972). These are source rules for that commit, not a claim that a gallery using another published React package version renders identically. Token names below are the exact CSS variables or component prop values in the archive. Component CSS contains PostCSS mixins, so the authored CSS is not a standalone stylesheet.

How to read an entry:

- A `--p-*` variable is the token of the same name in the theme sets of [tokens.json](tokens.json): `--p-color-bg-fill` is `light.color.color-bg-fill`, and [tokens/light.css](tokens/light.css) lists every light value. Component sizes the archive sets in component CSS are `core.size.*`, `core.focusRing.*` and `core.layout.*` tokens; the README's "Sizing and focus ring" table lists them.
- Every image is of the local reference gallery, rendered by the published React package; none is a Shopify admin screen. Whole sections are in [screenshots/](screenshots) (light at 1440 px, with [dark/](screenshots/dark) and [phone/](screenshots/phone) copies of the nine component sections), and focus-visible crops at 2x in [screenshots/focus/](screenshots/focus).
- [components/](components) holds SVG redraws built from the tokens by `tools/build_vectors.py`. They keep editable geometry and text but flatten layered bevels, gradients, pseudo-elements and responsive behaviour, so they are reconstructions, not captures.

## Components

### Actions and status

#### Button

Secondary is the default variant; primary, tertiary, plain and monochromePlain express other hierarchy. Success and critical are tone overrides. Loading preserves the button label's width while hiding its normal content and announcing progress. Disabled suppresses activation, not merely a color change.

`secondary` is the default variant and `medium` the default size; the other variants are `primary`, `tertiary`, `plain`, and `monochromePlain`, with `success` and `critical` tones. Primary uses the brand fill gradient, brand on-fill text, and primary button shadows; secondary uses `--p-color-bg-fill` plus its hover/active tokens and `--p-shadow-button`; tertiary is transparent until hover; plain uses link text colors and underlines on interaction. Success/critical override the corresponding text or primary fill/shadow tokens. The CSS resolves base, hover, active/open, pressed, disabled, and focus-visible states through component variables. Focus-visible gets a `--p-border-width-050` solid `--p-color-border-focus` outline offset by `--p-space-025`; disabled loses shadow and pointer events. See [props/defaults](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Button/Button.tsx#L23-L49), [variant and tone CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Button/Button.module.css#L73-L212), and [state/focus CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Button/Button.module.css#L3-L115).

Micro, slim, medium and large have responsive minimum heights. At desktop the primary size minima are 24/28/32px; slim and medium share their authored minimum and padding. Text-only medium examples have 12px inline padding on each side. Icon-bearing buttons intentionally adjust the icon edge independently. Use content sizing, not a fixed width inferred from a specimen frame.

Button sizes `micro`, `slim`, `medium`, `large` use `--p-height-700/800/900` minimum heights on narrow screens and `--p-height-600/700/800` at `md` and above. `slim` and `medium` have the same authored minimum height and padding. Icon-only buttons use tighter token padding; plain icon-only buttons remove padding and set `--p-height-500`/`--p-width-500` minima. SVG fills are controlled separately by variant/state, with secondary icon colors for tertiary/plain icon-only cases. An icon sits left of text; disclosure sits right. Loading hides the normal content, shows a small Spinner with a translated accessibility label, and disables activation. Text uses `bodySm` except large or non-micro plain buttons (`bodyMd`); primary is semibold on narrow screens and medium at `md` and above. See [sizes and icon rules](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Button/Button.module.css#L214-L325), [icon/state CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Button/Button.module.css#L43-L70), and [rendering](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Button/Button.tsx#L118-L246).

Primary and secondary buttons use compound inset/drop shadows and state-dependent fills. The live gallery and bundled CSS are the fidelity reference for these effects. Editable SVG controls flatten these details to their semantic fill/border. Use Tab on the live controls to inspect keyboard focus.

Seen in: [05-buttons](screenshots/05-buttons.png), [20-delete-confirm](screenshots/20-delete-confirm.png), [focus/button-primary](screenshots/focus/button-primary.png), [focus/button-secondary](screenshots/focus/button-secondary.png), [focus/button-tertiary](screenshots/focus/button-tertiary.png), [focus/button-critical](screenshots/focus/button-critical.png), [focus/button-plain](screenshots/focus/button-plain.png), [focus/icon-button](screenshots/focus/icon-button.png), [focus/button-segmented](screenshots/focus/button-segmented.png).

Redraws (token-based reconstructions, not captures): [button-primary](components/button-primary.svg), [button-secondary](components/button-secondary.svg), [button-tertiary](components/button-tertiary.svg), [button-critical](components/button-critical.svg), [button-disabled](components/button-disabled.svg), [button-icon-micro](components/button-icon-micro.svg), [button-icon-medium](components/button-icon-medium.svg), [button-icon-large](components/button-icon-large.svg).

#### Badge

Progress badges represent incomplete, partially complete or complete status.

Base badge is inline-flex with `--p-space-050` block and `--p-space-200` inline padding, `--p-border-radius-200`, secondary transparent fill, secondary text, and medium weight. `large` changes block padding to `--p-space-100`; `small` and `medium` share the base CSS. Tone families are `info`, `success`, `attention` (caution tokens), `warning`, `critical`, their `-strong` counterparts, plus `new`, `magic`, `read-only`, and `enabled`. Regular tones use the matching secondary fill and semantic text/icon; strong tones use solid fill and on-fill text/icon. `new` is bold, `read-only` has transparent fill, and `enabled` uses a success icon. Badge text is `bodySm`. `progress` uses a pip icon and accessible progress/tone label; a caller `icon` and `progress` are mutually exclusive. See [CSS tones and size](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Badge/Badge.module.css#L1-L184), [tone/size types](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Badge/types.ts#L1-L42), and [render/accessibility](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Badge/Badge.tsx#L63-L120).

Seen in: [06-badges-tags](screenshots/06-badges-tags.png), [01-overview](screenshots/01-overview.png).

Redraws (token-based reconstructions, not captures): [badge-paid](components/badge-paid.svg), [badge-draft](components/badge-draft.svg), [badge-pending](components/badge-pending.svg), [badge-overdue](components/badge-overdue.svg), [badge-information](components/badge-information.svg), [badge-warning](components/badge-warning.svg).

#### Tag

Tags represent removable choices and give their remove control a separate accessible name. Keep text content-sized and account for the remove target at the end.

Base fill is `--p-color-bg-fill-tertiary`, radius `--p-border-radius-200`, text `--p-color-text`, with `bodySm` truncated label. Clickable/linkable tags use tertiary hover/active fills and a focus-ring mixin; disabled uses disabled fill/text/icon. The remove button is a separate accessible button with `XSmallIcon`, a literal 18 by 18 px box and 7 px radius, plus its own hover/focus/active rules. The sole size prop is `large`: minimum height 24 px (`core.size.tag-large-min-height`); its 20 by 20 px remove button appears on hover or focus, while touch devices keep it visible. See [Tag CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Tag/Tag.module.css#L1-L245) and [separate link/remove semantics](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Tag/Tag.tsx#L57-L119).

Seen in: [06-badges-tags](screenshots/06-badges-tags.png), [focus/tag-remove](screenshots/focus/tag-remove.png).

Redraws (token-based reconstructions, not captures): [tag-wholesale](components/tag-wholesale.svg), [tag-vip-customer](components/tag-vip-customer.svg), [tag-summer-collection](components/tag-summer-collection.svg).

### Inputs and selection

#### TextField

TextField and Select have distinct default, hover, focus, invalid, read-only and disabled treatments. Labels remain visible; helper text supplies context; errors explain recovery. Text fields use prefix/suffix regions for units without turning them into value text.

Native input sits over a tokenized backdrop: `--pg-control-height` minimum (`core.size.control-height`), `--p-space-150` block and `--p-space-300` inline padding, `--p-font-size-400`/`--p-font-line-height-600` on narrow screens and `--p-font-size-325`/`--p-font-line-height-500` from `md` upward. The surface is `--p-color-input-bg-surface` with a `--p-border-width-0165` `--p-color-input-border` border and `--p-border-radius-200`; the top border is explicitly `#898f94` for the cited accessibility issue. Hover, active/focus, error, read-only, disabled, and `magic` have separate semantic tokens. Focus moves to the backdrop with active input border/background plus a `--p-border-width-050` focus outline. Borderless minimum is `--p-space-800`; slim minimum is a literal 28 px (`core.size.text-field-slim-min-height`). Prefix/suffix text is secondary, and icons use secondary icon color until disabled or magic overrides it. A clear button appears only on focus within; number input native spinners are suppressed for custom controls. See [base and states](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/TextField/TextField.module.css#L1-L194) and [input/backdrop/sizes](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/TextField/TextField.module.css#L253-L420).

Seen in: [07-forms](screenshots/07-forms.png), [19-states](screenshots/19-states.png), [focus/text-field](screenshots/focus/text-field.png), [focus/text-area](screenshots/focus/text-area.png), [focus/search-field](screenshots/focus/search-field.png).

Redraws (token-based reconstructions, not captures): [textfield-default](components/textfield-default.svg), [textfield-focus](components/textfield-focus.svg), [textfield-error](components/textfield-error.svg), [textfield-disabled](components/textfield-disabled.svg).

#### Checkbox and RadioButton

Native select, checkbox and radio semantics remain intact under custom visual layers. Indeterminate checkbox state is semantically mixed.

Both use `Choice`'s 18 px control at desktop and 20 px at `md` and below (`core.size.choice-control`, `core.size.choice-control-narrow`), with label/description space managed by `Choice`. Checkbox keeps the native input transparent above its visible backdrop; checked and indeterminate use brand-selected fill, and the check/line icon uses brand on-fill text. It supports error, magic, disabled, and `aria-checked="mixed"` for indeterminate. RadioButton visually hides its native input; its round backdrop has `--p-border-width-0165` input border, full radius, brand-selected checked fill, and a literal 8 px dot (10 px at `md` and below). Both draw a `--p-border-width-050` focus outline with `--p-space-025` offset; hover and disabled colors use control-specific semantic tokens. See [Choice sizing](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Choice/Choice.module.css#L110-L129), [Checkbox CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Checkbox/Checkbox.module.css#L1-L220), [Checkbox semantics](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Checkbox/Checkbox.tsx#L126-L201), and [RadioButton CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/RadioButton/RadioButton.module.css#L1-L147).

Seen in: [07-forms](screenshots/07-forms.png), [focus/checkbox](screenshots/focus/checkbox.png), [focus/radio](screenshots/focus/radio.png), [focus/list-row-checkbox](screenshots/focus/list-row-checkbox.png).

Redraws (token-based reconstructions, not captures): [checkbox-unchecked](components/checkbox-unchecked.svg), [checkbox-checked](components/checkbox-checked.svg), [checkbox-indeterminate](components/checkbox-indeterminate.svg), [radio-off](components/radio-off.svg), [radio-on](components/radio-on.svg).

#### Select

A visually transparent native `<select>` covers the control, preserving native option behavior and keyboard access; a content layer shows selected text and icon above a backdrop. Content uses `--pg-control-height`, `--p-space-150` block and `--p-space-200` end/`--p-space-300` start padding, and the same responsive input font pair as TextField. Backdrop uses input surface/border and `--p-border-radius-200`. Hover, active, focus, error, disabled, and magic each change backdrop/text/icon tokens; focus-visible draws a `--p-border-width-050` focus outline around the backdrop. The real select receives `aria-invalid`, `aria-describedby`, and required semantics; decorative content is `aria-hidden`. See [Select CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Select/Select.module.css#L1-L220) and [native select markup](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Select/Select.tsx#L182-L220).

Seen in: [07-forms](screenshots/07-forms.png), [focus/select](screenshots/focus/select.png).

### Surfaces, navigation, and overlays

#### Card

Cards group related content using surface, padding and bevel.

Current `Card` has no component CSS module. It composes `ShadowBevel` and `Box`, defaults to `bg-surface` and `xs: '400'` padding, uses shadow `100`, and applies radius `300` from the `sm` breakpoint upward (zero below). It clips X/Y overflow and creates `WithinContentContext`, which changes descendant Banner presentation. The prop comment mentions a different padding default; the function default is the executable value. See [Card implementation](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Card/Card.tsx#L17-L65) and [ShadowBevel token mapping](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/ShadowBevel/ShadowBevel.tsx#L29-L71).

Seen in: [10-surfaces](screenshots/10-surfaces.png).

Redraws (token-based reconstructions, not captures): [card](components/card.svg).

#### Banner

Banners use semantic status families and change presentation inside content containers. Critical/warning banners announce alerts; info/success announce status.

Tones are success, info (default), warning, critical. Page banners use solid semantic fill with on-fill text/icon and `--p-shadow-200` bevel; embedded banners use semantic surface/text colors and `--p-border-radius-200`. Default icons are Check, Info, AlertTriangle, and AlertDiamond; custom icons are documented as major icons. Warning/critical set `role="alert"`, while success/info use `role="status"`; the wrapper is keyboard focusable and can show a `--p-border-width-050` focus outline. Dismiss is a tertiary icon button with an accessible label. See [tone map](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Banner/utilities.ts#L30-L83), [surface/focus CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Banner/Banner.module.css#L1-L37), and [role/dismiss rendering](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Banner/Banner.tsx#L58-L164).

Seen in: [08-feedback](screenshots/08-feedback.png).

Redraws (token-based reconstructions, not captures): [banner-info](components/banner-info.svg), [banner-success](components/banner-success.svg), [banner-warning](components/banner-warning.svg), [banner-critical](components/banner-critical.svg).

#### Tabs

Tabs show selected state and preserve tab roles.

The tab row has `--p-space-100` gaps. Tabs use transparent fill, brand text, `--p-border-radius-200`, `--p-space-100` by `--p-space-300` padding, and `--p-height-700` height. Selected state uses transparent-selected fill and normal text; hover, focus, active, disabled, and focus-visible have distinct token colors/focus-ring mixins. Tab SVG paths inherit current text color; disabled icons use `--p-color-icon-disabled`. Tabs expose `tablist`/`tab`/`tabpanel`, `aria-selected`, and panel relationships, so the gallery should keep real tab markup. See [Tabs CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Tabs/Tabs.module.css#L40-L155), [tab markup](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Tabs/components/Tab/Tab.tsx#L275-L299), and [panel/row roles](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Tabs/Tabs.tsx#L542-L578).

Seen in: [09-navigation](screenshots/09-navigation.png), [focus/tab](screenshots/focus/tab.png).

Redraws (token-based reconstructions, not captures): [tabs](components/tabs.svg).

#### Modal

Modals use a focus-managed dialog with title and actions.

Dialog is bottom anchored on small screens; from `md` upward it centers and gets `--p-border-radius-400`. Surface is `--p-color-bg-surface`, shadow `--p-shadow-600`; regular max width is 620 px, small is 380 px, large reaches 980 px at `lg` (`core.layout.modal-width`, `-small`, `-large`), and fullScreen fills height on narrow screens. The dialog has `role="dialog"`, `aria-modal`, title labeling, focus handling, and an assertive live region. See [size/surface CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Modal/components/Dialog/Dialog.module.css#L1-L89), [dialog accessibility](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Modal/components/Dialog/Dialog.tsx#L60-L117), and [size API](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Modal/Modal.tsx#L23-L54).

Seen in: [14-modal-open](screenshots/14-modal-open.png), [20-delete-confirm](screenshots/20-delete-confirm.png).

#### Popover

Popovers have bounded surfaces, action lists and dismissal.

Surface uses `--p-color-bg-surface`, `--p-shadow-300` bevel, and `--p-border-radius-300`; default content maxes at 400 by 500 px, while fluid/full-height options remove those limits. Entry shifts by a literal -5 px and fades using `--p-motion-duration-100`. A subdued pane uses `--p-color-bg-surface-secondary`; adjacent sections get a secondary border. The activator gets `aria-controls`, `aria-owns`, `aria-expanded`, optional `aria-haspopup`, and `data-state`, which Button styling also reads for open/active appearance. See [Popover CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Popover/Popover.module.css#L1-L147) and [activator attributes](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Popover/set-activator-attributes.ts#L3-L29).

Seen in: [15-popover-open](screenshots/15-popover-open.png), [09-navigation](screenshots/09-navigation.png), [focus/menu-activator](screenshots/focus/menu-activator.png).

#### Tooltip

Tooltips explain controls and must not be the sole home of essential instructions.

Overlay uses surface/text tokens, `--p-shadow-300` bevel, `--p-shadow-400` shadow, token radius/padding passed as scoped CSS properties, and a 19 by 11 px SVG tail. Width is 200 px by default or 275 px for `wide`; default padding is `--p-space-100` by `--p-space-200`. Animation uses appear-above/below motion tokens and is removed for reduced motion. Tooltip content has `role="tooltip"`; its activator receives `aria-describedby` and a focus-ring attribute. An optional activator underline is a dotted `--p-border-width-050` border. See [overlay CSS](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Tooltip/components/TooltipOverlay/TooltipOverlay.module.css#L1-L118), [padding/radius/tail and role](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Tooltip/components/TooltipOverlay/TooltipOverlay.tsx#L98-L130), and [activator accessibility](https://github.com/Shopify/polaris-react-archive/blob/3f7954ae42fabf26d63cee68c23ceebfd7ef0972/polaris-react/src/components/Tooltip/Tooltip.tsx#L120-L132).

Seen in: [21-tooltip-open](screenshots/21-tooltip-open.png), [08-feedback](screenshots/08-feedback.png), [focus/tooltip-activator](screenshots/focus/tooltip-activator.png).

### Other compositions in the guide

Tables align numeric content separately from labels; empty states explain what belongs there and offer an action.

The live guide includes card, banner, tabs, pagination, popover, modal, tooltip, avatar, data table, progress bar, spinner, range slider and empty-state compositions in addition to core controls. Sample actions do not modify any store.

Seen in: [08-feedback](screenshots/08-feedback.png), [10-surfaces](screenshots/10-surfaces.png), [11-data](screenshots/11-data.png), [16-app-shell](screenshots/16-app-shell.png), [19-states](screenshots/19-states.png).

Redraws (token-based reconstructions, not captures): [progress](components/progress.svg).

## Shared values

### Focus-visible, measured (2026-10-17)

Read from the live gallery (published 13.9.5) in headless Chromium at 1440 px, light theme, after a Tab key press put the page in keyboard modality; every control below matched `:focus-visible`. The colour is `--p-color-border-focus` (`#005BD3`, `rgb(0, 91, 211)`), the width `--p-border-width-050` (2 px) and the offset `--p-space-025` (1 px) unless the row says otherwise. Raw computed changes are in [raw/focus-states.json](raw/focus-states.json); crops in [screenshots/focus/](screenshots/focus/).

| Control | Where the ring is drawn | Ring | Other change on focus | Crop |
|---|---|---|---|---|
| Button (primary, secondary, tertiary, critical, icon-only, disclosure, segmented, pagination) | the button | 2 px solid outline, 1 px offset | fill moves to its hover token (primary `color-bg-fill-brand-hover` `#1A1A1A`, secondary `color-bg-fill-hover` `#FAFAFA`, tertiary `color-bg-fill-transparent-hover` 5% black, critical `color-bg-fill-critical-hover` `#A30A24`; the pagination button read `#CCCCCC`, the value of `color-bg-fill-selected`) | [button-primary](screenshots/focus/button-primary.png), [icon-button](screenshots/focus/icon-button.png), [button-segmented](screenshots/focus/button-segmented.png) |
| Plain button | the button | 2 px solid outline, offset -6 px (inside the text box) | none | [button-plain](screenshots/focus/button-plain.png) |
| Link | the link | browser default `auto` outline, 2 px, 2 px offset | none | [link](screenshots/focus/link.png) |
| Text field, text area, search field | the `Backdrop` sibling | 2 px solid outline, 1 px offset | border `color-input-border-active` (`#1A1A1A`), fill `color-input-bg-surface-active` (`#F7F7F7`) | [text-field](screenshots/focus/text-field.png), [search-field](screenshots/focus/search-field.png) |
| Select | the `Backdrop` sibling | 2 px solid outline, 1 px offset | border `color-input-border-active` (`#1A1A1A`), fill `color-input-bg-surface-active` (`#F7F7F7`); the transparent native select also gets the browser outline | [select](screenshots/focus/select.png) |
| Checkbox, radio (and the list-row checkbox) | the `Backdrop` sibling | 2 px solid outline, 1 px offset | none | [checkbox](screenshots/focus/checkbox.png), [radio](screenshots/focus/radio.png) |
| Tab | `::after` on the tab | 2 px `box-shadow` ring, no offset | fill `color-bg-fill-transparent-hover` (5% black) | [tab](screenshots/focus/tab.png) |
| Tag remove button | `::after` on the button | 2 px `box-shadow` ring | fill `color-bg-fill-tertiary-hover` (`#D4D4D4`) | [tag-remove](screenshots/focus/tag-remove.png) |
| Range slider | the thumb pseudo-element (not readable through computed style) | ring visible on the thumb in the crop | none readable | [range-slider](screenshots/focus/range-slider.png) |
| Navigation item | the item | 2 px outline, 1 px offset | none | [nav-item](screenshots/focus/nav-item.png) |
| Resource list row | the row's overlay link | browser `auto` outline on the link; the row gets `ResourceItem--focused`, drawn as a full-row ring in the crop | none | [list-row](screenshots/focus/list-row.png) |

Every ring that uses a `box-shadow` (Tab, Tag) also sets a 1 px transparent outline, which only shows in forced-colours mode.

## Gaps

- Hover was read from CSS only: `tools/screenshots.mjs` does not shoot it. The only hover tokens this file names are the button, tab and tag-remove fills that focus also moves to (Shared values); the other entries say hover has its own tokens without naming them.
- States the gallery did not render, from the README's Coverage table: Select and text area show only default and focus-visible (no error or disabled), Radio only on, off and focus-visible (no disabled), and Tabs only selected, default and focus-visible (no disabled).
- There is no switch: Polaris React 13 has none, and the only `role="switch"` is on the deprecated `SettingToggle`, which renders an ordinary `Button` (README, Coverage).
- The rules above are read from the archive source (React 13.10.1); the gallery and every image run the published 13.9.5. The README's "Sizing and focus ring" section lists the spot checks against the 13.9.5 compiled CSS, which all matched.
- The range slider draws its focus ring on the thumb pseudo-element, which computed style cannot read; only the [range-slider](screenshots/focus/range-slider.png) crop shows it.
- Several values are literals in the component CSS with no token: the tag remove button's 18 by 18 px box and 7 px radius, the radio dot (8 px, 10 px at `md` and below), the popover's 400 by 500 px content limit and -5 px entry shift, and the tooltip's 19 by 11 px tail and 200 or 275 px width.
- Themes: every component section is rendered in `light` and `dark-experimental`; `light-high-contrast-experimental` and `light-mobile` are tokens only. In `dark-experimental` inputs keep the light surface while text turns light, so typed text is 1.26:1, and the critical tokens do not change; see [dark/07-forms](screenshots/dark/07-forms.png) and [dark/05-buttons](screenshots/dark/05-buttons.png).
