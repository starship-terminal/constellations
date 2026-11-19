# Components

Inventory from the signed-out pages measured on 2026-11-19. Crops are missing because the preview browser did not produce screenshot frames.

## Button

Primary marketing button `.button` is `#165dfb`, white text, 10px radius, padding 11px 22px, Figtree 16px weight 500, line-height 24px. Computed height on home was 46px.

Outline button `.button.button-transparent` is transparent with a 1px `#d7d3d1` border, text `#45403c`, same 10px radius and 11px 22px padding. Computed height was 48px.

Nav signup is `#454745` with white text, 10px radius, padding 11px 16px, height 42px. Nav login is a 1px `#98989873` border, 10px radius, padding 10px 22px, height 42px.

Pricing CTA `.button.pricing` is `#12b981`, 18px, weight 500, same 10px radius. Computed height 46px.

App submit on login and signup is `#4f77ff`, 8px radius, padding 12px 20px, height 48px, weight 500.

Features page CTA `.features-signup-button` is `#2e52cc`, 6px radius, padding 0 40px, height 62px.

Hover: `.navbar-button:hover` sets background `#f5f5f4`. `.button-primary:hover` is `#32343a` and `:active` is `#43464d`. Those primary rules were not the painted marketing buttons. Pressed, disabled and loading were not captured.

## Link

Nav links are Figtree 16px weight 500, `#111111`, 4px radius, padding 6px 12px. Login helper links are `#4f77ff`, 16px, weight 500. Footer links are declared `#222222`, 16px, line-height 32px, no underline. The first footer anchor computed as a browser-default blue underline; that node had no `.footer-link` class.

## Text field

Login and signup wrap the input in a 6px radius, 48px tall control. Rest ring is `#d6d3d1` plus `0 1px 3px #0000001a` and `0 1px 2px #0000000f`. Focus ring is `#335dec`. Input padding is 12px 16px, Figtree 16px. Placeholder copy is `your.name@company.com`. The field was focused and not filled.

## Text area, select, checkbox, radio

Not present on the pages opened.

## Switch

Pricing billing control `.toggle-button` is `#e3e3e3`, 70 by 36, radius 20px. Knob `.toggle-switch` is `#878787`, 28px, radius 100%. It was not toggled, so the annual position is a gap.

## Tabs, menu, tooltip, toast

Not captured. Sonner toast custom properties are declared for `[data-sonner-toaster]`. No toast was on screen. Intercom's launcher computed `#4f77ff` and was not opened.

## Dialog

Not captured. Webflow's `.w-modal` rules exist in the shared sheet. No product dialog was opened.

## Card

`.section-heading-pill` is `#f4f4f4`, radius 120px, padding 7px 18px, height 34px. Plan columns are 269px wide with a 1px `#5050504d` border. Free is `#f5f5f4`. Enterprise is `#e9e4ff`. `.messages-section` is `#bae6fc`. Features callout pill is `#dbeafe` with text `#2563eb`, radius 100px, padding 4px 14px. Quote cards are declared with a 1.1px `#d1dee8` border, 9px radius, and the two-layer black 10% shadow.

## List row, table, avatar, badge

Not captured as their own components. The "New" callout pill is the closest badge.

## Icon button

Not captured. The wordmark is a 96 by 30 image. The Google button is a 420 by 44 iframe titled "Sign in with Google Button".

## Gaps

- No crops. Preview snapshot failed with "The browser is not producing screenshot frames".
- Hover was read from the stylesheet, not from a painted pointer.
- Focus was painted only on the login email wrapper.
- Disabled, loading, error, pressed and selected states were not on the pages.
- Checkbox, radio, select, text area, tabs, menu, tooltip, dialog and toast were not opened.
- The billing switch was not moved.
