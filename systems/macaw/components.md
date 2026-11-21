# Macaw components

Public marketing site only (`https://macawhq.com/`), captured 2026-11-21, signed out, light theme, desktop 1440×900. Crops are 1x CSS pixels of the measured element. The signed-in app at `https://app.macawhq.com/` did not resolve, so nothing behind Log in or Start for free is here.

| Component | States | Crop |
|---|---|---|
| Nav link | default, hover (ink turns coral) | [nav-link-default.png](components/crops/nav-link-default.png), [nav-link-hover.png](components/crops/nav-link-hover.png) |
| Primary button | default, hover (coral darkens) | [button-primary-default.png](components/crops/button-primary-default.png), [button-primary-hover.png](components/crops/button-primary-hover.png) |
| Secondary button | default, hover (warm grey fill) | [button-secondary-default.png](components/crops/button-secondary-default.png), [button-secondary-hover.png](components/crops/button-secondary-hover.png) |
| Plan CTA | default, hover | [plan-cta-default.png](components/crops/plan-cta-default.png), [plan-cta-hover.png](components/crops/plan-cta-hover.png) |
| Submit button | default, hover, focus-visible | [submit-button-default.png](components/crops/submit-button-default.png), [submit-button-hover.png](components/crops/submit-button-hover.png), [submit-button-focus-visible.png](components/crops/submit-button-focus-visible.png) |
| Text field | default, hover, focus-visible (4px blush ring) | [text-field-default.png](components/crops/text-field-default.png), [text-field-focus-visible.png](components/crops/text-field-focus-visible.png) |
| Text area | default, hover, focus-visible | [text-area-default.png](components/crops/text-area-default.png), [text-area-focus-visible.png](components/crops/text-area-focus-visible.png) |
| Example card | default | [example-card-default.png](components/crops/example-card-default.png) |
| Example dialog | default (published sample article) | [example-dialog-default.png](components/crops/example-dialog-default.png) |
| Plan card | default (Starter wash) | [plan-card-default.png](components/crops/plan-card-default.png) |
| Pricing toggle | default, hover | [pricing-toggle-default.png](components/crops/pricing-toggle-default.png), [pricing-toggle-hover.png](components/crops/pricing-toggle-hover.png) |
| Logo link | default, hover | [logo-link-default.png](components/crops/logo-link-default.png) |

Pressed was not captured. CDP `forcePseudoState` did not return a node id for these anchors, so no pressed crop was written. Disabled, loading, and error-on-field were not on the public pages. The contact form was not submitted, so validation was not shown.

Dialog close (`.tingle-modal__close`) missed the crop selector. The close control is visible in [home-light-example-dialog.png](screenshots/home-light-example-dialog.png).

## Shared values

- Primary fill is `light.accent.default` (`#f66658`), hover `light.accent.hover` (`#de4f31`), label `light.text.onAccent`.
- Height is `core.size.button` (46px) with radius `core.radius.control` (8px) and shadow `core.shadow.control`.
- Fields are 44px, radius 8px, focus ring `light.border.focus` at `core.size.focus` (4px).
- Body type is Inter 16px / 24px. Display is Inter 53.6px / 64.32px weight 700.

## Gaps

- Icon button: the phone menu button is a 40×48 control with `aria-label="menu"`. No desktop icon-button crop. Not captured as a tokenised component.
- Link: nav links are captured. Inline body links were not measured separately.
- Select, checkbox, radio, switch, tabs, tooltip, toast, avatar, badge (as a tokenised component), table header styles: not present as interactive controls on the public pages. The pricing comparison is a set of rows, shown in [pricing-light-yearly.png](screenshots/pricing-light-yearly.png), not a `<table>` with header tokens.
- Resources menu: present in the DOM, `display: none` at 1440. Opens on the phone menu. Not captured as a desktop dropdown. See [site-tree.md](site-tree.md).
- Menu (phone): captured as a page state, [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). No separate crop.
- Focus ring on the coral button is the browser outline (`1px auto` blue) plus the blush shadow. Recorded on the submit button only.
- Status colours (success, warning, danger, info): not present.
- Dark theme: not present.
- Signed-in app, search, filters, empty, loading, error, destructive confirmation, onboarding: not captured. Login and sign-up URLs do not resolve.
