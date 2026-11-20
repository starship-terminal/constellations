# fal.ai component measurements

Computed styles read from fal.ai on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the single-theme Webflow marketing pages (/, /pricing), the Next.js app in its dark theme (/explore, /models/krea/v3/text-to-image(+ /api), /login) and the fumadocs docs in light (/docs/documentation) — with consent overlays hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### App shell and navigation

#### mkt-header

Marketing header. The fixed top bar (div.nav-main, z-index 999): fal wordmark, Products / Docs / Pricing / Enterprise / Resources menus, Contact Sales and Get Started.

Page: home. Selector: `div.nav-main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Focal Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.dropdown-toggle-label: Focal Web 14px/14px 500, #000000 |
| Transition | none |
| Icon | 120 x 48, colour #000000 |
| Painted layers | a.nav-logo-holder.w-inline-block 140.0x68.0 bg #ffffff @ 0.88 r 4px; div.nav-list 502.0x35.2 bg #ffffff @ 0.88 r 4.8px; div::after.dropdown-toggle.w-dropdown-toggle 4.79688pxx4.79688px image radial-gradient(circle at 100% 0px, #000000 @ 0 0.3em, #adff00 calc(0.3em + 0.25px)); div.nav-dot 8.0x8.0 bg #999999 r 100%; nav.dropdown-content.w-dropdown-list 0.0x0.0 bg #ffffff @ 0; nav::before.dropdown-content.w-dropdown-list autoxauto bg #adff00 r 0px 4.8px 4.8px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The fal wordmark link (a.nav-logo-holder).

Page: home. Selector: `a.nav-logo-holder`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 140 x 68 |
| Padding | 10px |
| Border | none |
| Radius | 4px |
| Background | #ffffff @ 0.88 |
| Box shadow | none |
| Backdrop filter | blur(6px) |
| Outline | none |
| Font | Focal Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | width, background-color 0.3s, 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s |
| Cursor | pointer |
| Icon | 120 x 48, colour #000000 |
| Painted layers | a.nav-logo-holder.w-inline-block 140.0x68.0 bg #ffffff @ 0.88 r 4px |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### mkt-nav-products

Products menu trigger. The Products dropdown trigger in the marketing nav — a Webflow w-dropdown disclosure; measured, its links never followed.

Page: home. Selector: `.w-dropdown-toggle Products`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111 x 35.19 | = | = | = |
| Padding | 10px 18px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | 4.8px 4.8px 0px 0px | = | = |
| Background | transparent | #adff00 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4d65ff offset 2px | = |
| Font | Focal Web 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.dropdown-toggle-label: Focal Web 14px/14px 500, #000000 | = | = | = |
| Transition | none | background-color, color 0.1s, 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | = | = |
| Cursor | pointer | = | = | = |
| ::after | 4.79688px x 4.79688px, absolute, bg #000000 @ 0 radial-gradient(circle at 100% 0px, #000000 @ 0 0.3em, #adff00 calc(0.3em + 0.25px)), radius 0px | = | = | = |
| Painted layers | div::after.dropdown-toggle.w-dropdown-toggle 4.79688pxx4.79688px image radial-gradient(circle at 100% 0px, #000000 @ 0 0.3em, #adff00 calc(0.3em + 0.25px)); div.nav-dot 8.0x8.0 bg #999999 r 100% | div.dropdown-toggle.w-dropdown-toggle 111.0x35.2 bg #adff00 r 4.8px 4.8px 0px 0px; div::after.dropdown-toggle.w-dropdown-toggle 4.79688pxx4.79688px image radial-gradient(circle at 100% 0px, #000000 @ 0 0.3em, #adff00 calc(0.3em + 0.25px)); div.nav-dot 8.0x8.0 bg #999999 r 100% | div.dropdown-toggle.w-dropdown-toggle 111.0x35.2 outline 2px solid #4d65ff offset 2px; div::after.dropdown-toggle.w-dropdown-toggle 4.79688pxx4.79688px image radial-gradient(circle at 100% 0px, #000000 @ 0 0.3em, #adff00 calc(0.3em + 0.25px)); div.nav-dot 8.0x8.0 bg #999999 r 100% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mkt-nav-products-default.png`, `mkt-nav-products-hover.png`, `mkt-nav-products-focus-visible.png`, `mkt-nav-products-pressed.png`.

#### mkt-nav-pricing

Pricing link (marketing). The marketing nav Pricing link; measured, never followed.

Page: home. Selector: `a.nav-list-item Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87 x 35.19 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #ffc4d8 | #ffc4d8 | #ffc4d8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Focal Web 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.dropdown-toggle-label: Focal Web 14px/14px 500, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.nav-list bg #ffffff @ 0.88 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.nav-list-item.nav-hover-light-pink 87.0x35.2 bg #ffc4d8 r 4px | a.nav-list-item.nav-hover-light-pink 87.0x35.2 bg #ffc4d8 r 4px outline 1px auto #101010 offset 1px | a.nav-list-item.nav-hover-light-pink 87.0x35.2 bg #ffc4d8 r 4px |

Crops: `mkt-nav-pricing-default.png`, `mkt-nav-pricing-hover.png`, `mkt-nav-pricing-focus-visible.png`, `mkt-nav-pricing-pressed.png`.

#### mkt-btn-sales

Contact Sales button (marketing). The secondary Contact-Sales button in the marketing header; measured, never followed.

Page: home. Selector: `.nav-right Contact Sales`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 143 x 34.59 | = | = | = |
| Padding | 10px 26px | = | = | = |
| Border | 1px solid #e5ece7 | = | = | = |
| Radius | 2px | = | = | = |
| Background | #e5ece7 | #d9d9d9 | = | #d9d9d9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Focal Web 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.button-label.w-variant-c539965e-2a2e-14ba-3b68-3062a13d570d: Focal Web 14px/12.6px 500, #000000 | = | = | = |
| Transition | background-color, color 0.1s, 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94), cubic-bezier(0.25, 0.46, 0.45, 0.94) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.w-variant-c539965e-2a2e-14ba-3b68-3062a13d570d 143.0x34.6 bg #e5ece7 border T:1px solid #e5ece7 / R:1px solid #e5ece7 / B:1px solid #e5ece7 / L:1px solid #e5ece7 r 2px | a.button.w-variant-c539965e-2a2e-14ba-3b68-3062a13d570d 143.0x34.6 bg #d9d9d9 border T:1px solid #e5ece7 / R:1px solid #e5ece7 / B:1px solid #e5ece7 / L:1px solid #e5ece7 r 2px | a.button.w-variant-c539965e-2a2e-14ba-3b68-3062a13d570d 143.0x34.6 bg #e5ece7 border T:1px solid #e5ece7 / R:1px solid #e5ece7 / B:1px solid #e5ece7 / L:1px solid #e5ece7 r 2px outline 1px auto #101010 offset 1px | a.button.w-variant-c539965e-2a2e-14ba-3b68-3062a13d570d 143.0x34.6 bg #d9d9d9 border T:1px solid #e5ece7 / R:1px solid #e5ece7 / B:1px solid #e5ece7 / L:1px solid #e5ece7 r 2px |
| Ancestor paint | 1 up div.nav-right bg #ffffff @ 0.88 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mkt-btn-sales-default.png`, `mkt-btn-sales-hover.png`, `mkt-btn-sales-focus-visible.png`, `mkt-btn-sales-pressed.png`.

#### mkt-btn-start

Get Started button (marketing). The primary Get-Started button in the marketing header; measured, never followed.

Page: home. Selector: `.nav-right Get Started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128 x 34.59 | = | = | = |
| Padding | 10px 26px | = | = | = |
| Border | 1px solid #000000 | 1px solid #e5ece7 | 1px solid #e5ece7 | 1px solid #e5ece7 |
| Radius | 2px | = | = | = |
| Background | #000000 | #e5ece7 | #e5ece7 | #e5ece7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Focal Web 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #000000 | #000000 | #000000 |
| Text node | div.button-label.w-variant-03039704-b0b4-28e2-1972-4b9af245265e: Focal Web 14px/12.6px 500, #ffffff | div.button-label.w-variant-03039704-b0b4-28e2-1972-4b9af245265e: Focal Web 14px/12.6px 500, #000000 | div.button-label.w-variant-03039704-b0b4-28e2-1972-4b9af245265e: Focal Web 14px/12.6px 500, #000000 | div.button-label.w-variant-03039704-b0b4-28e2-1972-4b9af245265e: Focal Web 14px/12.6px 500, #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.w-variant-03039704-b0b4-28e2-1972-4b9af245265e 128.0x34.6 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | a.button.w-variant-03039704-b0b4-28e2-1972-4b9af245265e 128.0x34.6 bg #e5ece7 border T:1px solid #e5ece7 / R:1px solid #e5ece7 / B:1px solid #e5ece7 / L:1px solid #e5ece7 r 2px | a.button.w-variant-03039704-b0b4-28e2-1972-4b9af245265e 128.0x34.6 bg #e5ece7 border T:1px solid #e5ece7 / R:1px solid #e5ece7 / B:1px solid #e5ece7 / L:1px solid #e5ece7 r 2px outline 1px auto #101010 offset 1px | a.button.w-variant-03039704-b0b4-28e2-1972-4b9af245265e 128.0x34.6 bg #e5ece7 border T:1px solid #e5ece7 / R:1px solid #e5ece7 / B:1px solid #e5ece7 / L:1px solid #e5ece7 r 2px |
| Ancestor paint | 1 up div.nav-right bg #ffffff @ 0.88 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mkt-btn-start-default.png`, `mkt-btn-start-hover.png`, `mkt-btn-start-focus-visible.png`, `mkt-btn-start-pressed.png`.

#### app-header

App header. The app navigation header (header.dashboard-navigation-header): fal mark, Products / Documentation / Pricing / Enterprise / Resources menus, Contact Sales, Log-in, Sign-up.

Page: explore. Selector: `header.dashboard-navigation-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | publicSansRounded 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.inline-flex.items-center: publicSansRounded 14px/normal 600, #f4f4f5, ls -0.14px |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | div.dashboard-navigation-surface 1440.0x48.0 bg #19191a border B:1px solid #ffffff @ 0.05; div.dashboard-navigation-seam 1440.0x1.0 border B:1px solid #ffffff @ 0.05; button.inline-flex.items-center 0.0x0.0 bg #202022 r 4px; button::after.inline-flex.items-center autoxauto r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; a.inline-flex.items-center 0.0x0.0 bg #202022 r 4px; a::after.inline-flex.items-center autoxauto r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `app-header-default.png`.

#### app-announce

Announcement banner. The dismissible announcement strip above the header; the Dismiss button is measured, never pressed.

Page: explore. Selector: `announcement strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 32 |
| Padding | 6px 44px |
| Border | none |
| Radius | 0px |
| Background | #142657 |
| Box shadow | none |
| Outline | none |
| Font | focal 14px/14px 500 |
| Letter spacing | -0.28px |
| Colour | #99edff |
| Text node | span.wrap-break-word: focal 14px/18px 500, #99edff, ls -0.28px |
| Transition | none |
| Icon | 6 x 6, colour #115ef3 |
| Painted layers | div.[--product-banner-bg:var(--product-banner-blue-dark-background)].[--product-banner-fg:var(--product-banner-blue-dark-foreground)] 1440.0x32.0 bg #142657; button.inline-flex.items-center 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest |

Crops: `app-announce-default.png`.

#### app-announce-x

Dismiss-announcement button. The X that closes the announcement strip — a local dismiss; measured, never pressed.

Page: explore. Selector: `button[aria-label="Dismiss announcement"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | 27.44 x 27.44 |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/14px 600 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #99edff | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #99edff | = | = | 15.68 x 15.68, colour #99edff |
| Painted layers | button.inline-flex.items-center 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.inline-flex.items-center 28.0x28.0 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.inline-flex.items-center 28.0x28.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 27.4x27.4 bg #ffffff @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-announce-x-default.png`, `app-announce-x-hover.png`, `app-announce-x-focus-visible.png`, `app-announce-x-pressed.png`.

#### app-nav-products

Products menu trigger (app). The Products dropdown trigger in the app header — a local disclosure; the opened state was measured after clicking it, its links never followed.

Page: explore. Selector: `header Products`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 91.77 x 48 | = | = | = | = |
| Padding | 0px 6px 0px 10px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | 4px | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #ffffff @ 0.2 offset -2px | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = | = |
| Letter spacing | -0.28px | = | = | = | = |
| Colour | #ffffff @ 0.65 | #ffffff @ 0.8 | #ffffff @ 0.8 | #ffffff @ 0.8 | #ffffff @ 0.8 |
| Text node | span.font-sans.text-sm: publicSansRounded 14px/22.4px 600, #ffffff @ 0.65, ls -0.28px | span.font-sans.text-sm: publicSansRounded 14px/22.4px 600, #ffffff @ 0.8, ls -0.28px | span.font-sans.text-sm: publicSansRounded 14px/22.4px 600, #ffffff @ 0.8, ls -0.28px | span.font-sans.text-sm: publicSansRounded 14px/22.4px 600, #ffffff @ 0.8, ls -0.28px | span.font-sans.text-sm: publicSansRounded 14px/22.4px 600, #f4f4f5, ls -0.28px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #ffffff @ 0.65 | = | = | = | 16 x 16, colour #f4f4f5 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.group.inline-flex 91.8x48.0 r 4px outline 2px solid #ffffff @ 0.2 offset -2px | = | = |

Crops: `app-nav-products-hover.png`, `app-nav-products-focus-visible.png`, `app-nav-products-pressed.png`, `app-nav-products-opened.png`.

#### app-nav-menu

Products menu. The dropdown opened by the Products trigger (div.top-center ~322x201, holding ul.p-1.5 product links); its links were never followed.

Page: explore. Selector: `products dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 322 x 201 |
| Padding | 0px |
| Border | 1px solid #ffffff @ 0.05 |
| Radius | 4px |
| Background | #19191a |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.03 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px, #000000 @ 0.4 0px 1px 3px 0px |
| Outline | none |
| Font | publicSansRounded 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: publicSansRounded 14px/17.5px 500, #f4f4f5 |
| Transition | none |
| Icon | 16 x 16, colour #ffffff @ 0.8 |
| ::before | 320px x 8px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div.top-center.absolute 322.0x201.0 bg #19191a border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.03 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px, #000000 @ 0.4 0px 1px 3px 0px; div.flex.size-9 36.0x36.0 bg #ffffff @ 0.05 r 4px; div.flex.size-9 36.0x36.0 bg #ffffff @ 0.05 r 4px; div.flex.size-9 36.0x36.0 bg #ffffff @ 0.05 r 4px |
| How | at rest |

Crops: `app-nav-menu-default.png`.

#### app-nav-menu-item

Products menu item. A product entry inside the opened dropdown (a.text-content-subtle); measured, never followed.

Page: explore. Selector: `products menu link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 308 x 65.5 | = |
| Padding | 8px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | #ffffff @ 0.03 |
| Box shadow | none | = |
| Outline | none | = |
| Font | publicSansRounded 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff @ 0.65 | #fafafa |
| Text node | span: publicSansRounded 14px/17.5px 500, #f4f4f5 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #ffffff @ 0.8 | = |
| ::before | 308px x 69.5px, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | div.flex.size-9 36.0x36.0 bg #ffffff @ 0.05 r 4px | a.text-content-subtle.hover:bg-surface-alpha-light 308.0x65.5 bg #ffffff @ 0.03 r 4px; div.flex.size-9 36.0x36.0 bg #ffffff @ 0.05 r 4px |
| Ancestor paint | 3 up div.top-center.absolute bg #19191a shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.03 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px, #000000 @ 0.4 0px 1px 3px 0px | = |
| How | at rest | mouse hover |

Crops: `app-nav-menu-item-hover.png`.

#### app-nav-docs

Documentation link (app). The app header Documentation link; measured, never followed.

Page: explore. Selector: `header Documentation`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.38 x 48 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff @ 0.2 offset -2px | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #ffffff @ 0.65 | #ffffff @ 0.8 | #ffffff @ 0.8 | #ffffff @ 0.8 |
| Text node | span.font-sans.text-sm: publicSansRounded 14px/22.4px 600, #ffffff @ 0.65, ls -0.28px | span.font-sans.text-sm: publicSansRounded 14px/22.4px 600, #ffffff @ 0.8, ls -0.28px | span.font-sans.text-sm: publicSansRounded 14px/22.4px 600, #ffffff @ 0.8, ls -0.28px | span.font-sans.text-sm: publicSansRounded 14px/22.4px 600, #ffffff @ 0.8, ls -0.28px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.inline-flex 118.4x48.0 r 4px outline 2px solid #ffffff @ 0.2 offset -2px | = |

Crops: `app-nav-docs-default.png`, `app-nav-docs-hover.png`, `app-nav-docs-focus-visible.png`, `app-nav-docs-pressed.png`.

#### app-btn-login

Log-in button (app). The Log-in button in the app header; measured, never followed.

Page: explore. Selector: `header Log-in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.17 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #202022 | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/normal 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 64.1719px x 32px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | 64.1719px x 32px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | 64.1719px x 32px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Painted layers | a.inline-flex.items-center 64.2x32.0 bg #202022 r 4px; a::after.inline-flex.items-center 64.1719pxx32px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 64.2x32.0 bg #ffffff @ 0.05 r 4px; a::after.inline-flex.items-center 64.1719pxx32px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 64.2x32.0 bg #202022 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; a::after.inline-flex.items-center 64.1719pxx32px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 64.2x32.0 bg #ffffff @ 0.05 r 4px; a::after.inline-flex.items-center 64.1719pxx32px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-btn-login-default.png`, `app-btn-login-hover.png`, `app-btn-login-focus-visible.png`, `app-btn-login-pressed.png`.

#### app-btn-signup

Sign-up button (app). The primary Sign-up button in the app header; measured, never followed.

Page: explore. Selector: `header Sign-up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.03 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #fafafa | #e4e4e7 | = | #e4e4e7 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/normal 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #161618 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 74.0x32.0 bg #fafafa r 4px | a.inline-flex.items-center 74.0x32.0 bg #e4e4e7 r 4px | a.inline-flex.items-center 74.0x32.0 bg #fafafa r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 74.0x32.0 bg #e4e4e7 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-btn-signup-default.png`, `app-btn-signup-hover.png`, `app-btn-signup-focus-visible.png`, `app-btn-signup-pressed.png`.

### Home (marketing)

#### mkt-hero-h1

Hero headline. The home hero display heading — Focal Web 96px, the cyan brand colour on the olive field.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1028.56 x 172.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Focal Web 96px/86.4px 500 |
| Letter spacing | -3.84px |
| Colour | #99edff |
| Transition | none |
| How | at rest |

Crops: `mkt-hero-h1-default.png`.

#### mkt-hero-field

Hero field. The home hero section: the dark bronze field (background-color-darkbronze) behind the cyan display headline.

Page: home. Selector: `section ancestor of the hero h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 800 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #403700 |
| Box shadow | none |
| Outline | none |
| Font | Focal Web 13.7143px/20.5714px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1.heading: Focal Web 96px/86.4px 500, #99edff, ls -3.84px |
| Transition | none |
| Icon | 394.28 x 310.45, colour #ffffff |
| Painted layers | section.section.background-color-darkbronze 1440.0x800.0 bg #403700; div.bar-fill.is-lightblue 6.8x358.0 bg #f57ec3; div.bar-fill.is-white 6.8x197.2 bg #ffffff; div.bar-fill.is-neon 6.8x134.7 bg #ec0648; a.button.w-inline-block 132.8x44.0 bg #adff00 border T:1px solid #adff00 / R:1px solid #adff00 / B:1px solid #adff00 / L:1px solid #adff00 r 2px; a.button.w-variant-17bbad85-716d-5add-8937-bb0206da92fe 150.0x44.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 2px |
| How | at rest |

Crops: `mkt-hero-field-default.png`.

#### mkt-hero-cta

Hero CTA. The primary call-to-action inside the hero; measured never followed.

Page: home. Selector: `hero primary CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 134.56 x 44.05 | = | = | = |
| Padding | 13.7143px 22.2857px | = | = | = |
| Border | 1px solid #adff00 | 1px solid #71a600 | = | 1px solid #71a600 |
| Radius | 2px | = | = | = |
| Background | #adff00 | #71a600 | = | #71a600 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Focal Web 13.7143px/13.7143px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #403700 | #ffffff | = | #ffffff |
| Text node | div.button-label: Focal Web 16.2857px/14.6571px 500, #403700 | div.button-label: Focal Web 16.2857px/14.6571px 500, #ffffff | = | div.button-label: Focal Web 16.2857px/14.6571px 500, #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.w-inline-block 134.6x44.0 bg #adff00 border T:1px solid #adff00 / R:1px solid #adff00 / B:1px solid #adff00 / L:1px solid #adff00 r 2px | a.button.w-inline-block 134.6x44.0 bg #71a600 border T:1px solid #71a600 / R:1px solid #71a600 / B:1px solid #71a600 / L:1px solid #71a600 r 2px | a.button.w-inline-block 134.6x44.0 bg #adff00 border T:1px solid #adff00 / R:1px solid #adff00 / B:1px solid #adff00 / L:1px solid #adff00 r 2px outline 1px auto #101010 offset 1px | a.button.w-inline-block 134.6x44.0 bg #71a600 border T:1px solid #71a600 / R:1px solid #71a600 / B:1px solid #71a600 / L:1px solid #71a600 r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mkt-hero-cta-default.png`, `mkt-hero-cta-hover.png`, `mkt-hero-cta-focus-visible.png`, `mkt-hero-cta-pressed.png`.

#### mkt-section-h2

Section heading (marketing). A marketing section heading further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 822.84 x 106.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Focal Web 59.1429px/53.2286px 500 |
| Letter spacing | -1.18286px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: none.

### Footer

#### mkt-footer

Marketing footer. The marketing page footer (section.is-footer): link columns, socials, legal.

Page: home. Selector: `section.is-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 537.22 |
| Padding | 17.1429px |
| Border | none |
| Radius | 0px |
| Background | #ffc4d8 |
| Box shadow | none |
| Outline | none |
| Font | Focal Web 13.7143px/20.5714px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.text-size-tiny.text-weight-medium: Focal Web 15.2px/19.152px 500, #000000 |
| Transition | none |
| Icon | 540 x 217.02, colour #000000 |
| ::before | 1440px x 1px, absolute, bg #000000 @ 0 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='1' viewBox='0 0 8 1'%3E%3Cpath d='M0, radius 0px |
| Painted layers | section.section.background-color-pink 1440.0x537.2 bg #ffc4d8; section::before.section.background-color-pink 1440pxx1px image url(data:…); a::after.footer-link 42pxx1px image url(data:…); a::after.footer-link 105pxx1px image url(data:…); a::after.footer-link 48pxx1px image url(data:…); a::after.footer-link 71pxx1px image url(data:…) |
| How | at rest |

Crops: `mkt-footer-default.png`.

#### app-footer

App footer. The app page footer: product/learn/social columns, legal and privacy links.

Page: model. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 886.19 |
| Padding | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | focal 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.8 |
| Text node | h2.font-heading.text-2xl: focal 30px/36px 500, #fafafa, ls -0.6px |
| Transition | none |
| Icon | 563 x 225.19, colour #99edff |
| Painted layers | a.inline-flex.items-center 144.9x44.0 bg #fafafa border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div.shrink-0.bg-stroke-base 1440.0x1.0 bg #ffffff @ 0.05 |
| Ancestor paint | 1 up div.footer-container.container-full bg #202022 |
| How | at rest |

Crops: `app-footer-default.png`.

### Pricing (marketing)

#### pr-h1

Pricing headline. The pricing page display heading.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1028.56 x 172.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Focal Web 96px/86.4px 500 |
| Letter spacing | -3.84px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pr-h1-default.png`.

#### pr-plan-cta

Plan CTA. A call-to-action inside a plan column; measured never followed.

Page: pricing. Selector: `plan CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 151.56 x 44.05 | = | = | = |
| Padding | 13.7143px 22.2857px | = | = | = |
| Border | 1px solid #ffffff | 1px solid #e5ece7 | = | 1px solid #e5ece7 |
| Radius | 2px | = | = | = |
| Background | #ffffff | #e5ece7 | = | #e5ece7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Focal Web 13.7143px/13.7143px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.button-label: Focal Web 16.2857px/14.6571px 500, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.w-variant-17bbad85-716d-5add-8937-bb0206da92fe 151.6x44.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 2px | a.button.w-variant-17bbad85-716d-5add-8937-bb0206da92fe 151.6x44.0 bg #e5ece7 border T:1px solid #e5ece7 / R:1px solid #e5ece7 / B:1px solid #e5ece7 / L:1px solid #e5ece7 r 2px | a.button.w-variant-17bbad85-716d-5add-8937-bb0206da92fe 151.6x44.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 2px outline 1px auto #101010 offset 1px | a.button.w-variant-17bbad85-716d-5add-8937-bb0206da92fe 151.6x44.0 bg #e5ece7 border T:1px solid #e5ece7 / R:1px solid #e5ece7 / B:1px solid #e5ece7 / L:1px solid #e5ece7 r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pr-plan-cta-default.png`, `pr-plan-cta-hover.png`, `pr-plan-cta-focus-visible.png`, `pr-plan-cta-pressed.png`.

#### pr-price-table

Pricing table. A div.pricing-row-table block under the "Serverless & Compute Pricing" heading — fal prices GPU compute and model APIs per usage; there is no plan card or billing toggle.

Page: pricing. Selector: `.pricing-row-table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1337.16 x 364.36 |
| Padding | 17.1429px |
| Gap | 13.7143px 0px |
| Border | none |
| Radius | 0px |
| Background | #e5ece7 |
| Box shadow | none |
| Outline | none |
| Font | Focal Web 13.7143px/20.5714px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div: Focal Text 16.2857px/19.5429px 400, #000000 |
| Transition | none |
| Icon | 294.86 x 1, colour #000000 |
| Painted layers | div.pricing-row-table 1337.2x364.4 bg #e5ece7; div.price-card-pill 81.1x33.0 bg #ffffff r 3.66429px; div.price-card-pill.is-regular 51.0x33.0 bg #ffffff @ 0 r 3.66429px; div.price-card-pill.is-regular 55.0x33.0 bg #ffffff @ 0 r 3.66429px; div.price-card-pill.is-regular 51.0x33.0 bg #ffffff @ 0 r 3.66429px; div.price-card-pill 93.1x33.0 bg #ffffff r 3.66429px |
| How | at rest |

Crops: `pr-price-table-default.png`.

#### pr-price-row

Pricing row. A .pricing-table-row line inside a compute/model pricing table.

Page: pricing. Selector: `.pricing-table-row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1302.88 x 32.97 | = |
| Padding | 0px | = |
| Gap | 0px 41.1429px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Focal Text 16.2857px/19.5429px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | div.text-color-red: Focal Text 14.6571px/17.5886px 500, #ec0648 | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Icon | 21.98 x 21.98, colour #000000 | = |
| Painted layers | div.price-card-pill 81.1x33.0 bg #ffffff r 3.66429px; div.price-card-pill.is-regular 51.0x33.0 bg #ffffff @ 0 r 3.66429px; div.price-card-pill.is-regular 55.0x33.0 bg #ffffff @ 0 r 3.66429px; div.price-card-pill.is-regular 51.0x33.0 bg #ffffff @ 0 r 3.66429px | = |
| Ancestor paint | 1 up div.pricing-row-table bg #e5ece7 | = |
| How | at rest | mouse hover |

Crops: `pr-price-row-default.png`, `pr-price-row-hover.png`.

### Explore catalog (app, dark)

#### search-models

Model search field. The "Search models" input over the catalog; focused and typed into then cleared — the catalog only filters locally.

Page: explore. Selector: `input[aria-label="Search models"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 953.08 x 24 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #ffffff @ 0.8 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #ffffff @ 0.8 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | publicSansRounded 16px/24px 400 | = | = |
| Letter spacing | -0.16px | = | = |
| Colour | #ffffff @ 0.8 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff @ 0.8, opacity 1 | = | = |
| Painted layers | input.flex.min-w-0 953.1x24.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | input.flex.min-w-0 953.1x24.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #ffffff @ 0.8 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | input.flex.min-w-0 953.1x24.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #ffffff @ 0.8 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | focused the field | typed "flux", then deleted; nothing sent |

Crops: `search-models-default.png`, `search-models-focused.png`, `search-models-filled.png`.

#### model-card

Model card. A model tile in the explore grid (a.page-model-card): artwork, endpoint id, publisher and description; measured, never followed.

Page: explore. Selector: `a.page-model-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 360 x 350.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | publicSansRounded 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | div.badge.badge-role-lime: publicSansRounded 12px/18px 600, #163200, ls -0.12px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #163200 | = |
| Painted layers | div::after.flex.h-full 360pxx350.5px border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px; div.relative.aspect-[16/9] 360.0x202.5 image linear-gradient(to right in oklab, #ffffff @ 0.03 0%, #ffffff @ 0.05 50%, #ffffff @ 0.03 1; div.badge.badge-role-lime 44.6x16.0 bg #a2d81c border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div::before.relative.flex 358pxx1px bg #ffffff @ 0.1; div.grid.shrink-0 16.0x16.0 bg #202022 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 2px; button.inline-flex.items-center 16.0x16.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px | div::after.flex.h-full 360pxx350.5px border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px; div.relative.aspect-[16/9] 360.0x202.5 image linear-gradient(to right in oklab, #ffffff @ 0.03 0%, #ffffff @ 0.05 50%, #ffffff @ 0.03 1; div.badge.badge-role-lime 44.6x16.0 bg #a2d81c border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div::before.relative.flex 358pxx1px bg #ffffff @ 0.2; div.grid.shrink-0 16.0x16.0 bg #202022 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 2px; button.inline-flex.items-center 16.0x16.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px |
| How | at rest | mouse hover |

Crops: `model-card-default.png`, `model-card-hover.png`.

#### model-card-title

Model card endpoint line. The endpoint-id text line inside a card (e.g. blackforestlabs/flux-3-max/text-to-video) — a span.truncate, cards carry no heading elements.

Page: explore. Selector: `a.page-model-card .truncate`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 286 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | focal 16px/20px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.shrink-0.font-normal: focal 16px/20px 400, #ffffff @ 0.8 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `model-card-title-default.png`.

#### card-cta

Card CTA. The "Try it now!" pill on a hero-carousel slide; measured, never followed.

Page: explore. Selector: `Try it now`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.47 x 36 | = | = | 99.44 x 35.28 |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #fafafa | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #161618 | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 101.5x36.0 bg #fafafa border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | = | a.inline-flex.items-center 101.5x36.0 bg #fafafa border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 99.4x35.3 bg #fafafa border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `card-cta-hover.png`, `card-cta-focus-visible.png`, `card-cta-pressed.png`.

#### carousel-dot

Carousel dot. A "Go to slide N" dot in the hero carousel — a local pager; measured, never clicked.

Page: explore. Selector: `button[aria-label^="Go to slide"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80 x 40 | = | = | 192 x 40 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | publicSansRounded 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.relative.mt-0.5: publicSansRounded 10px/15px 600, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.relative.h-1.5 80.0x8.0 bg #ffffff @ 0.2 | div.relative.h-1.5 80.0x24.0 bg #783afb | button.group.pointer-events-auto 80.0x40.0 outline 2px solid #ffffff offset 2px; div.relative.h-1.5 80.0x8.0 bg #ffffff @ 0.2 | div.relative.h-1.5 192.0x8.0 bg #ffffff @ 0.2; span.absolute.inset-0 12.2x8.0 bg #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-dot-default.png`, `carousel-dot-hover.png`, `carousel-dot-focus-visible.png`, `carousel-dot-pressed.png`.

#### pager-next

Section pager arrow. A "Next page" arrow button scrolling a catalog section (~48x96); a local scroller — measured, never clicked.

Page: explore. Selector: `button[aria-label="Next page"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 96 | = | = | 0 x 0 |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | 1px solid #ffffff @ 0.2 |
| Radius | 4px | = | = | = |
| Background | transparent | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.65 | #f4f4f5 | = | #f4f4f5 |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | - |
| Opacity | 0 | - | = | - |
| Cursor | pointer | = | = | = |
| Icon | 30 x 30, colour #787881, fill #000000 | = | = | 0 x 0, colour #787881 |
| Painted layers | button.inline-flex.items-center 48.0x96.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.inline-flex.items-center 48.0x96.0 bg #ffffff @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.inline-flex.items-center 48.0x96.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 0.0x0.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `pager-next-default.png`, `pager-next-hover.png`, `pager-next-focus-visible.png`.

#### card-docs-link

Card docs link. The "See docs" pill on a hero-carousel slide; measured, never followed.

Page: explore. Selector: `See docs`. States: default, focus-visible, pressed, hover.

| Property | default | focus-visible | pressed | hover |
|---|---|---|---|---|
| Size (w x h) | 92.89 x 36 | = | 91.03 x 35.28 | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | = | 1px solid #ffffff @ 0.2 | = |
| Radius | 4px | = | = | = |
| Background | #202022 | = | #ffffff @ 0.05 | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 92.9x36.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px | a.inline-flex.items-center 92.9x36.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 91.0x35.3 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px | = |
| How | at rest | Shift+Tab, Tab | CDP forcePseudoState :active:hover | mouse hover |

Crops: `card-docs-link-default.png`, `card-docs-link-focus-visible.png`, `card-docs-link-pressed.png`, `card-docs-link-hover.png`.

#### pager-dot

Section pager dot. A "Go to page N" dot paging a catalog section — a local pager; measured, never clicked.

Page: explore. Selector: `button[aria-label^="Go to page"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 6 x 6 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #a6a6ae | #f4f4f5 | = | #f4f4f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | publicSansRounded 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.h-1.5.transition-all 6.0x6.0 bg #a6a6ae | button.h-1.5.transition-all 6.0x6.0 bg #f4f4f5 | button.h-1.5.transition-all 6.0x6.0 bg #a6a6ae outline 1px auto #101010 offset 0px | button.h-1.5.transition-all 6.0x6.0 bg #f4f4f5 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pager-dot-default.png`, `pager-dot-hover.png`, `pager-dot-focus-visible.png`, `pager-dot-pressed.png`.

### Model page (app, dark)

#### mp-back

Back to Gallery link. The breadcrumb-style link back to the catalog; measured, never followed.

Page: model. Selector: `Back to Gallery`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 45 x 12 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | publicSansRounded 12px/12px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #f4f4f5 | = | - | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `mp-back-default.png`, `mp-back-hover.png`, `mp-back-pressed.png`.

#### mp-h1

Model heading. "krea/v3/text-to-image" — the model endpoint heading.

Page: model. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 355.75 x 32 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | focal 20px/28px 300 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.shrink-0.font-normal: focal 30px/32px 400, #ffffff @ 0.8, ls 0.75px |
| Transition | none |
| Painted layers | div.grid.shrink-0 32.0x32.0 bg #202022 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 2px |
| How | at rest |

Crops: `mp-h1-default.png`.

#### mp-badge

Model badge. A .badge-role-* pill under the heading (Inference / Commercial use / Idle).

Page: model. Selector: `.badge-role-*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 65.11 x 14 |
| Padding | 0px 3px |
| Gap | 2px |
| Border | 1px solid #000000 @ 0 |
| Radius | 4px |
| Background | #783afb @ 0.2 |
| Box shadow | none |
| Outline | none |
| Font | publicSansRounded 10px/15px 600 |
| Letter spacing | -0.1px |
| Colour | #cac4fe |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Icon | 10 x 10, colour #cac4fe |
| Painted layers | div.badge.badge-role-brand 65.1x14.0 bg #783afb @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest |

Crops: `mp-badge-default.png`.

#### mp-tab

Model page tab. A Playground/API/Examples tab on the model page — an in-page tab link; measured, the active tab was not switched for state capture.

Page: model. Selector: `model tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95.2 x 40 | = | = | = |
| Padding | 4px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/16.8px 600 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, border-color, color, transform 0.16s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | auto x 2px, absolute, bg #fafafa, radius 0px | = | = | = |
| Painted layers | a.group/tab.relative 95.2x40.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; a::after.group/tab.relative autox2px bg #fafafa | = | a.group/tab.relative 95.2x40.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; a::after.group/tab.relative autox2px bg #fafafa | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-tab-default.png`, `mp-tab-hover.png`, `mp-tab-focus-visible.png`, `mp-tab-pressed.png`.

#### mp-endpoint-btn

Model endpoint button. The endpoint-id chip button; measured, never activated.

Page: model. Selector: `button[aria-label="Model endpoint"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132.19 x 32 | = | = | = |
| Padding | 0px 10px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | 1px solid #ffffff @ 0.2 | = | 1px solid #ffffff @ 0.2 |
| Radius | 4px | = | = | = |
| Background | #202022 | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #787881 | = | = | = |
| Painted layers | button.inline-flex.items-center 132.2x32.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px | button.inline-flex.items-center 132.2x32.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px | button.inline-flex.items-center 132.2x32.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 132.2x32.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-endpoint-btn-default.png`, `mp-endpoint-btn-hover.png`, `mp-endpoint-btn-focus-visible.png`, `mp-endpoint-btn-pressed.png`.

#### mp-copy

Copy button. A clipboard Copy icon button (endpoint / code); measured, never pressed.

Page: model. Selector: `button[aria-label="Copy"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 31.36 x 31.36 |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 20px/28px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff @ 0.5 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| Painted layers | button.inline-flex.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.inline-flex.items-center 32.0x32.0 bg #ffffff @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.inline-flex.items-center 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 31.4x31.4 bg #ffffff @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-copy-default.png`, `mp-copy-hover.png`, `mp-copy-focus-visible.png`, `mp-copy-pressed.png`.

#### mp-agent-btn

Onboard-your-agent button. The "Onboard your agent" button that copies a setup prompt; measured, never pressed.

Page: model. Selector: `Onboard your agent`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 216.48 x 32 | = | = | = |
| Padding | 0px 12px 0px 6px | = | = | = |
| Gap | 6px | = | = | = |
| Border | T: 1px solid #ffffff @ 0.1; R: none; B: 1px solid #ffffff @ 0.1; L: 1px solid #ffffff @ 0.1 | T: 1px solid #ffffff @ 0.2; R: none; B: 1px solid #ffffff @ 0.2; L: 1px solid #ffffff @ 0.2 | = | T: 1px solid #ffffff @ 0.2; R: none; B: 1px solid #ffffff @ 0.2; L: 1px solid #ffffff @ 0.2 |
| Radius | 4px 0px 0px 4px | = | = | = |
| Background | #202022 | #ffffff @ 0.1 | = | #ffffff @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Text node | span: publicSansRounded 14px/20px 600, #f4f4f5, ls -0.14px | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #787881 | = | = | = |
| Painted layers | button.inline-flex.items-center 216.5x32.0 bg #202022 border T:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px 0px 0px 4px; span.flex.size-4.5 18.0x18.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px; span.flex.size-4.5 18.0x18.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px; span.flex.size-4.5 18.0x18.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px | button.inline-flex.items-center 216.5x32.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px 0px 0px 4px; span.flex.size-4.5 18.0x18.0 bg #19191a border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px; span.flex.size-4.5 18.0x18.0 bg #19191a border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px; span.flex.size-4.5 18.0x18.0 bg #19191a border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px | button.inline-flex.items-center 216.5x32.0 bg #202022 border T:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px 0px 0px 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; span.flex.size-4.5 18.0x18.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px; span.flex.size-4.5 18.0x18.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px; span.flex.size-4.5 18.0x18.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px | button.inline-flex.items-center 216.5x32.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px 0px 0px 4px; span.flex.size-4.5 18.0x18.0 bg #19191a border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px; span.flex.size-4.5 18.0x18.0 bg #19191a border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px; span.flex.size-4.5 18.0x18.0 bg #19191a border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-agent-btn-default.png`, `mp-agent-btn-hover.png`, `mp-agent-btn-focus-visible.png`, `mp-agent-btn-pressed.png`.

#### mp-sandbox-link

Open in Sandbox link. The Open-in-Sandbox link on the model page (a 120x32 pill, text "SandboxOpen in Sandbox" — a hidden twin ships beside it); measured, never followed.

Page: model. Selector: `a[href*="/sandbox"] "Open in Sandbox"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120.2 x 32 | = | = | 117.8 x 31.36 |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | 1px solid #ffffff @ 0.2 | = | 1px solid #ffffff @ 0.2 |
| Radius | 4px | = | = | = |
| Background | #202022 | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 12px/16px 600 | = | = | = |
| Letter spacing | -0.12px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Text node | span.max-md:hidden: publicSansRounded 12px/16px 600, #f4f4f5, ls -0.12px | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 120.2x32.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px | a.inline-flex.items-center 120.2x32.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px | a.inline-flex.items-center 120.2x32.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 117.8x31.4 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-sandbox-link-default.png`, `mp-sandbox-link-hover.png`, `mp-sandbox-link-focus-visible.png`, `mp-sandbox-link-pressed.png`.

#### mp-prompt

Prompt textarea. The playground prompt field ("Write your prompt here..."); focused and typed into then cleared — inference was never run.

Page: model. Selector: `playground textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 654 x 98 | = | = |
| Padding | 8px 12px | = | = |
| Border | 1px solid #ffffff @ 0.1 | = | = |
| Radius | 4px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | publicSansRounded 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 @ 0 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff @ 0.65, opacity 1 | = | = |
| Painted layers | textarea.flex.w-full 654.0x98.0 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px | textarea.flex.w-full 654.0x98.0 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | textarea.flex.w-full 654.0x98.0 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | focused the field | typed "a lighthouse on a cliff at dusk", then deleted; nothing sent |

Crops: `mp-prompt-default.png`, `mp-prompt-focused.png`, `mp-prompt-filled.png`.

#### mp-param

Parameter option. A playground parameter option pill (an aspect/size choice) — a local option button; measured, never toggled.

Page: model. Selector: `param option pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 192 x 40 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | 1px solid #ffffff @ 0.2 | = | 1px solid #ffffff @ 0.2 |
| Radius | 4px | = | = | = |
| Background | #202022 | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Text node | span: publicSansRounded 14px/20px 600, #f4f4f5 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #787881 | = | = | = |
| Painted layers | button.flex.items-center 192.0x40.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px | button.flex.items-center 192.0x40.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px | button.flex.items-center 192.0x40.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.flex.items-center 192.0x40.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-param-default.png`, `mp-param-hover.png`, `mp-param-focus-visible.png`, `mp-param-pressed.png`.

#### mp-param-more

More-params button. The "More" disclosure for extra playground parameters — a local disclosure; measured, never opened.

Page: model. Selector: `More`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75.53 x 32 | = | = | 74.02 x 31.36 |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | 1px solid #ffffff @ 0.2 | = | 1px solid #ffffff @ 0.2 |
| Radius | 4px | = | = | = |
| Background | #202022 | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 12px/16px 600 | = | = | = |
| Letter spacing | -0.12px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Text node | span: publicSansRounded 12px/16px 600, #f4f4f5, ls -0.12px | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #787881 | = | = | 15.68 x 15.68, colour #787881 |
| Painted layers | button.inline-flex.items-center 75.5x32.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px | button.inline-flex.items-center 75.5x32.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px | button.inline-flex.items-center 75.5x32.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 74.0x31.4 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-param-more-default.png`, `mp-param-more-hover.png`, `mp-param-more-focus-visible.png`, `mp-param-more-pressed.png`.

#### mp-run

Sign-in-to-run button. The playground run button — it links to login signed out; measured, never activated.

Page: model. Selector: `Sign in to run`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.05 x 40 | = | = | 116.67 x 39.2 |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #783afb | #6910e9 | = | #6910e9 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 119.0x40.0 bg #783afb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | a.inline-flex.items-center 119.0x40.0 bg #6910e9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | a.inline-flex.items-center 119.0x40.0 bg #783afb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 116.7x39.2 bg #6910e9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-run-default.png`, `mp-run-hover.png`, `mp-run-focus-visible.png`, `mp-run-pressed.png`.

#### mp-result-tab

Result view toggle. The Preview/JSON toggle on the Result pane — a local view switch; measured, never switched.

Page: model. Selector: `Preview/JSON toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.05 x 28 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | #ffffff @ 0.05 | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Text node | span: publicSansRounded 14px/20px 600, #f4f4f5, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff @ 0.65 | = | = | = |
| Painted layers | button.inline-flex.h-full 93.0x28.0 bg #ffffff @ 0.05 r 2px | = | button.inline-flex.h-full 93.0x28.0 bg #ffffff @ 0.05 r 2px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Ancestor paint | 1 up div.inline-flex.shrink-0 bg #19191a shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.05 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-result-tab-default.png`, `mp-result-tab-hover.png`, `mp-result-tab-focus-visible.png`, `mp-result-tab-pressed.png`.

#### mp-download

Download button. The result Download button — a licensed download; measured, never pressed.

Page: model. Selector: `Download`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.89 x 36 | = | = | 117.49 x 35.28 |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | 1px solid #ffffff @ 0.2 | = | 1px solid #ffffff @ 0.2 |
| Radius | 4px | = | = | = |
| Background | #202022 | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #787881 | = | = | 15.68 x 15.68, colour #787881 |
| Painted layers | button.inline-flex.items-center 119.9x36.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px | button.inline-flex.items-center 119.9x36.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px | button.inline-flex.items-center 119.9x36.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 117.5x35.3 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-download-default.png`, `mp-download-hover.png`, `mp-download-focus-visible.png`, `mp-download-pressed.png`.

### API tab (app, dark)

#### api-tab

API tab (active). The "API" tab of the model page tab bar, active (aria-selected true); measured, never switched.

Page: api. Selector: `a[href$="/api"] "API"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 44.42 x 40 |
| Padding | 4px 10px |
| Gap | 6px |
| Border | 1px solid #000000 @ 0 |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | publicSansRounded 14px/16.8px 600 |
| Letter spacing | -0.28px |
| Colour | #fafafa |
| Transition | background-color, border-color, color, transform 0.16s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| ::after | auto x 2px, absolute, bg #fafafa, radius 0px |
| Painted layers | a.group/tab.relative 44.4x40.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; a::after.group/tab.relative autox2px bg #fafafa |
| How | at rest |

Crops: `api-tab-default.png`.

#### api-code

API code block. A code sample on the API tab (client subscribe / queue call).

Page: api. Selector: `code block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1070 x 347 |
| Padding | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | chivoMono 14px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.token: chivoMono 14px/21px 400, #c678dd |
| Transition | none |
| Ancestor paint | 1 up div.group.relative bg #ffffff @ 0.05 |
| How | at rest |

Crops: `api-code-default.png`.

#### api-copy

Copy button (API). The code-block Copy button (top-right of the first code sample); measured, never pressed.

Page: api. Selector: `code block button[aria-label="Copy"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 35.28 x 35.28 |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Transition | background-color, border-color, color, transform, opacity 0.16s cubic-bezier(0.25, 0.46, 0.45, 0.94) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff @ 0.5 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| Painted layers | button.inline-flex.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.inline-flex.items-center 36.0x36.0 bg #ffffff @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.inline-flex.items-center 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 35.3x35.3 bg #ffffff @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `api-copy-default.png`, `api-copy-hover.png`, `api-copy-focus-visible.png`, `api-copy-pressed.png`.

#### api-lang-tab

Language tab. A client-language tab on the API samples ("JavaScript / Node.js") — a local view switch; measured, never switched.

Page: api. Selector: `language tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 256 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.1 | 1px solid #ffffff @ 0.2 | = | 1px solid #ffffff @ 0.2 |
| Radius | 4px | = | = | = |
| Background | #202022 | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Text node | span: publicSansRounded 14px/20px 600, #f4f4f5 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #787881 | = | = | = |
| Painted layers | button.flex.items-center 256.0x36.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px | button.flex.items-center 256.0x36.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px | button.flex.items-center 256.0x36.0 bg #202022 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.flex.items-center 256.0x36.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `api-lang-tab-default.png`, `api-lang-tab-hover.png`, `api-lang-tab-focus-visible.png`, `api-lang-tab-pressed.png`.

### Login (app, dark)

#### li-card

Login card. The OAuth-only login/signup card: fal mark, "Login or sign up", the Continue-with-* buttons and Use SSO; measured at rest, nothing followed.

Page: login. Selector: `login card (h1 ancestor)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 388.91 |
| Padding | 0px |
| Gap | 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | publicSansRounded 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1.font-heading.text-[30px]: focal 36px/34.92px 400, #f4f4f5, ls -1.44px |
| Transition | none |
| Icon | 40 x 40, colour #f4f4f5 |
| Painted layers | a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `li-card-default.png`.

#### li-h1

Login heading. "Welcome to fal" over the card.

Page: login. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 34.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | focal 36px/34.92px 400 |
| Letter spacing | -1.44px |
| Colour | #f4f4f5 |
| Transition | none |
| How | at rest |

Crops: `li-h1-default.png`.

#### li-oauth-github

Continue-with-GitHub button. A Continue-with-* OAuth button; measured, never followed (it starts the OAuth flow).

Page: login. Selector: `Continue with GitHub`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 16px/normal 600 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #f4f4f5 | = | = | = |
| ::after | 400px x 40px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | 400px x 40px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | 400px x 40px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Painted layers | a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 400.0x40.0 bg #ffffff @ 0.05 r 4px; a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 400.0x40.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 400.0x40.0 bg #ffffff @ 0.05 r 4px; a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `li-oauth-github-default.png`, `li-oauth-github-hover.png`, `li-oauth-github-focus-visible.png`, `li-oauth-github-pressed.png`.

#### li-oauth-google

Continue-with-Google button. The Continue-with-Google OAuth button; measured, never followed.

Page: login. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 16px/normal 600 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 400px x 40px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | 400px x 40px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | 400px x 40px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Painted layers | a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 400.0x40.0 bg #ffffff @ 0.05 r 4px; a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 400.0x40.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 400.0x40.0 bg #ffffff @ 0.05 r 4px; a::after.inline-flex.items-center 400pxx40px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `li-oauth-google-default.png`, `li-oauth-google-hover.png`, `li-oauth-google-focus-visible.png`, `li-oauth-google-pressed.png`.

#### li-sso

Use SSO button. The Use-SSO button; measured, never followed.

Page: login. Selector: `Use SSO`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.03 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/14px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #ffffff @ 0.65 | #f4f4f5 | = | #f4f4f5 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #787881 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.focus-ring.inline-flex 101.0x32.0 bg #ffffff @ 0.05 r 4px | button.focus-ring.inline-flex 101.0x32.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.focus-ring.inline-flex 101.0x32.0 bg #ffffff @ 0.05 r 4px |

Crops: `li-sso-default.png`, `li-sso-hover.png`, `li-sso-focus-visible.png`, `li-sso-pressed.png`.

#### li-support

Contact-support link. The Contact-support link under the card; measured, never followed.

Page: login. Selector: `Contact support`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146.91 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #ffffff @ 0.05 | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | publicSansRounded 14px/normal 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #ffffff @ 0.65 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #787881 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.inline-flex.items-center 146.9x32.0 bg #ffffff @ 0.05 r 4px | a.inline-flex.items-center 146.9x32.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 146.9x32.0 bg #ffffff @ 0.05 r 4px |

Crops: `li-support-default.png`, `li-support-hover.png`, `li-support-focus-visible.png`, `li-support-pressed.png`.

### Documentation (docs, light)

#### docs-topbar

Docs top bar. The docs tab strip (.nav-tabs): Documentation / Examples / Model API Reference / SDK Reference / Inference API / Platform API / Changelog.

Page: docs. Selector: `.nav-tabs`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 966 x 47 |
| Padding | 0px |
| Gap | normal 24px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Public Sans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #727075 |
| Text node | a.link.nav-tabs-item: Public Sans 14px/20px 500, #27262b |
| Transition | none |
| Painted layers | div.absolute.bottom-0 126.0x1.5 bg #5718c0 r 4px |
| Ancestor paint | 1 up div.z-20.hidden bg #ffffff |
| How | at rest |

Crops: `docs-topbar-default.png`.

#### docs-search

Docs search trigger. The "Search… Ctrl K" command trigger at the top of the sidebar — a local overlay trigger; measured, never opened.

Page: docs. Selector: `button.group/search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 232 x 36 | = | = | = |
| Padding | 0px 12px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a19fa4 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #525055 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #525055 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #5718c0 offset 0px | = |
| Font | Public Sans 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #727075 | = | = | = |
| Text node | div.truncate.min-w-0: Public Sans 14px/24px 400, #727075 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #413f44, fill #000000 | 16 x 16, colour #27262b, fill #000000 | = | 16 x 16, colour #27262b, fill #000000 |
| Painted layers | button.group/search.flex 232.0x36.0 bg #ffffff r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a19fa4 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 232.0x36.0 bg #ffffff r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #525055 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 232.0x36.0 bg #ffffff r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a19fa4 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #5718c0 offset 0px | button.group/search.flex 232.0x36.0 bg #ffffff r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #525055 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-theme-btn

Theme switcher. One segment of the light/system/dark theme control — a local display toggle; measured, never cycled (the page was captured at its light default).

Page: docs. Selector: `button[aria-label*="theme"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #5718c0 offset 0px | = |
| Font | Public Sans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a19fa4 | #525055 | = | #525055 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #a19fa4, fill #000000 | 12 x 12, colour #525055, fill #000000 | = | 12 x 12, colour #525055, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.switch-option.z-10 20.0x20.0 r 4px outline 1px auto #5718c0 offset 0px | = |

Crops: `docs-theme-btn-default.png`, `docs-theme-btn-hover.png`, `docs-theme-btn-focus-visible.png`, `docs-theme-btn-pressed.png`.

#### docs-nav-section

Docs nav item. A sidebar navigation item on the docs tree (a.group); measured, never followed.

Page: docs. Selector: `docs sidebar link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 286 x 32 | = |
| Padding | 6px 12px 6px 16px | = |
| Gap | normal 12px | = |
| Border | T: none; R: none; B: none; L: 1px solid #5718c0 | = |
| Radius | 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Public Sans 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #5718c0 | = |
| Text node | span.min-w-0.max-w-full: Public Sans 14px/20px 400, #5718c0 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.group.flex 286.0x32.0 border L:1px solid #5718c0 r 4px | = |
| How | at rest | mouse hover |

Crops: `docs-nav-section-default.png`, `docs-nav-section-hover.png`.

#### docs-h1

Docs heading. "Build with fal" — the docs hero heading (Focal, h1.fal-hero-title).

Page: docs. Selector: `h1.fal-hero-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 309 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Focal Medium 56px/56px 500 |
| Letter spacing | -1.12px |
| Colour | #242426 |
| Text node | span.cursor-pointer: Focal Medium 56px/56px 500, #242426, ls -1.12px |
| Transition | none |
| Painted layers | a::before.anchor-link 24pxx24px bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a19fa4 @ 0.3 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px; a::after.anchor-link 12pxx12px bg #a19fa4 |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-prose

Docs body text. A hero/body paragraph in the docs prose (Public Sans, p.fal-hero-body).

Page: docs. Selector: `p.fal-hero-body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 309 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Focal Medium 20px/20px 500 |
| Letter spacing | -0.4px |
| Colour | #242426 |
| Transition | none |
| How | at rest |

Crops: `docs-prose-default.png`.

#### docs-card

Docs section card. A section card in the docs .columns grid (Model APIs / Serverless / Compute); measured, its link never followed.

Page: docs. Selector: `.columns .card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 650 x 444 | = |
| Padding | 0px | = |
| Gap | 0px 16px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Public Sans 16px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #413f44 | = |
| Text node | h2.not-prose.font-semibold: Focal 16px/24px 600, #27262b | = |
| Transition | none | = |
| Icon | 0 x 0, colour #a19fa4, fill #000000 | = |
| Painted layers | div.card.block 317.0x206.0 bg #ffffff border T:1px solid #0c0a10 @ 0.1 / R:1px solid #0c0a10 @ 0.1 / B:1px solid #0c0a10 @ 0.1 / L:1px solid #0c0a10 @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; a 0.0x0.0 border B:1px solid #5718c0 r 4px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 24.0x24.0 bg #5718c0 r 4px; div.card.block 317.0x206.0 bg #ffffff border T:1px solid #0c0a10 @ 0.1 / R:1px solid #0c0a10 @ 0.1 / B:1px solid #0c0a10 @ 0.1 / L:1px solid #0c0a10 @ 0.1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; a 0.0x0.0 border B:1px solid #5718c0 r 4px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 24.0x24.0 bg #5718c0 r 4px | = |
| How | at rest | mouse hover |

Crops: `docs-card-default.png`, `docs-card-hover.png`.

#### docs-toc

On-this-page TOC. The right-hand "On this page" table of contents.

Page: docs. Selector: `docs toc`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 264 x 208 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Public Sans 14px/24px 400 |
| Letter spacing | normal |
| Colour | #525055 |
| Text node | span: Focal 14px/24px 500, #413f44 |
| Transition | none |
| Icon | 12 x 12, colour #413f44, fill #000000 |
| Painted layers | a.text-primary.dark:text-primary-light 264.0x32.0 border L:1px solid #5718c0 r 4px; a 264.0x32.0 border L:1px solid #0c0a10 @ 0.05 r 4px; a 264.0x32.0 border L:1px solid #0c0a10 @ 0.05 r 4px; a 264.0x32.0 border L:1px solid #0c0a10 @ 0.05 r 4px |
| How | at rest |

Crops: `docs-toc-default.png`.

#### docs-code

Docs code block. A .code-group sample block in the docs (Python/JavaScript/cURL tabs).

Page: docs. Selector: `.code-group`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 650 x 212 |
| Padding | 2px |
| Border | 1px solid #0c0a10 @ 0.1 |
| Radius | 4px |
| Background | #f5f3f8 |
| Box shadow | none |
| Outline | none |
| Font | Public Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0c0a10 |
| Text node | div.peer/title.flex: Public Sans 12px/24px 500, #5718c0 |
| Transition | none |
| Icon | 16 x 16, colour #a19fa4, fill #000000 |
| Painted layers | div.code-group.p-0.5 650.0x212.0 bg #f5f3f8 border T:1px solid #0c0a10 @ 0.1 / R:1px solid #0c0a10 @ 0.1 / B:1px solid #0c0a10 @ 0.1 / L:1px solid #0c0a10 @ 0.1 r 4px; div.absolute.-bottom-1.5 53.0x2.0 bg #5718c0 r 9999px; div.w-0.min-w-full 644.0x172.0 bg #ffffff r 14px; div.size-full.rounded-[inherit] 644.0x172.0 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.min-w-full!.h-full 612.0x144.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.font-mono.whitespace-pre 612.0x144.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `docs-code-default.png`.

#### docs-tab-item

Docs tab item. A tab inside the docs tab strip; measured, never followed.

Page: docs. Selector: `a.nav-tabs-item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 126 x 47 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Public Sans 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #27262b | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.absolute.bottom-0 126.0x1.5 bg #5718c0 r 4px | = |
| How | at rest | mouse hover |

Crops: `docs-tab-item-default.png`, `docs-tab-item-hover.png`.

#### docs-hero-search

Docs hero search. The "Search or ask…" field in the docs hero — a local overlay trigger; measured, never opened.

Page: docs. Selector: `.fal-hero-search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 309 x 40.75 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Border | 1px solid #121216 @ 0.1 | 1px solid #121216 @ 0.2 | = | 1px solid #121216 @ 0.2 |
| Radius | 4px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #5718c0 offset 0px | = |
| Font | Public Sans 13px/22.75px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9ca3af | = | = | = |
| Text node | span.fal-hero-search-text: Public Sans 13px/22.75px 400, #9ca3af | = | = | = |
| Transition | border-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #787881 | = | = | = |
| Painted layers | button.fal-hero-search 309.0x40.8 bg #ffffff border T:1px solid #121216 @ 0.1 / R:1px solid #121216 @ 0.1 / B:1px solid #121216 @ 0.1 / L:1px solid #121216 @ 0.1 r 4px | button.fal-hero-search 309.0x40.8 bg #ffffff border T:1px solid #121216 @ 0.2 / R:1px solid #121216 @ 0.2 / B:1px solid #121216 @ 0.2 / L:1px solid #121216 @ 0.2 r 4px | button.fal-hero-search 309.0x40.8 bg #ffffff border T:1px solid #121216 @ 0.1 / R:1px solid #121216 @ 0.1 / B:1px solid #121216 @ 0.1 / L:1px solid #121216 @ 0.1 r 4px outline 1px auto #5718c0 offset 0px | button.fal-hero-search 309.0x40.8 bg #ffffff border T:1px solid #121216 @ 0.2 / R:1px solid #121216 @ 0.2 / B:1px solid #121216 @ 0.2 / L:1px solid #121216 @ 0.2 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-hero-search-default.png`, `docs-hero-search-hover.png`, `docs-hero-search-focus-visible.png`, `docs-hero-search-pressed.png`.

#### docs-sidebar

Docs sidebar. The fixed docs sidebar: search, Status/Community/Blog and the grouped nav tree.

Page: docs. Selector: `docs sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 900 |
| Padding | 0px |
| Border | T: none; R: 1px solid #e1dfe4 @ 0.7; B: none; L: none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Public Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #727075 |
| Text node | div.truncate.min-w-0: Public Sans 14px/24px 400, #727075 |
| Transition | none |
| Icon | 12 x 12, colour #a19fa4, fill #000000 |
| Painted layers | nav.hidden.lg:flex 350.0x900.0 border R:1px solid #e1dfe4 @ 0.7 r 4px; div.min-w-0.flex-1 350.0x811.0 bg #f7f7f8; div::before.min-w-0.flex-1 1440pxx811px bg #f7f7f8; div.flex.items-center 76.0x28.0 border T:1px solid #e1dfe4 @ 0.7 / R:1px solid #e1dfe4 @ 0.7 / B:1px solid #e1dfe4 @ 0.7 / L:1px solid #e1dfe4 @ 0.7 r 9999px; button.switch-option.z-10 20.0x20.0 bg #e1dfe4 @ 0.5 r 4px; button.group/search.flex 232.0x36.0 bg #ffffff r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a19fa4 @ 0.3 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `docs-sidebar-default.png`.

#### docs-code-copy

Docs code-copy button. The Copy button on a docs code block; measured, never pressed.

Page: docs. Selector: `button[aria-label="Copy the contents from the code block"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 26 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #5718c0 offset 0px | = |
| Font | Public Sans 16px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0c0a10 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #a19fa4, fill #000000 | 16 x 16, colour #727075, fill #000000 | = | 16 x 16, colour #727075, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.size-6.5.flex 26.0x26.0 r 4px outline 1px auto #5718c0 offset 0px | = |

Crops: `docs-code-copy-default.png`, `docs-code-copy-hover.png`, `docs-code-copy-focus-visible.png`, `docs-code-copy-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone top bar (header.dashboard-navigation-header): fal mark and the "Open navigation" trigger.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | publicSansRounded 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.inline-flex.items-center: publicSansRounded 14px/normal 600, #f4f4f5, ls -0.14px |
| Transition | none |
| Icon | 20 x 20, colour #ffffff |
| Painted layers | div.dashboard-navigation-surface 390.0x48.0 bg #19191a border B:1px solid #ffffff @ 0.05; div.dashboard-navigation-seam 0.0x0.0 border B:1px solid #ffffff @ 0.05; button.inline-flex.items-center 48.0x32.0 bg #202022 r 4px; button::after.inline-flex.items-center 48pxx32px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; a.inline-flex.items-center 64.2x32.0 bg #202022 r 4px; a::after.inline-flex.items-center 64.1719pxx32px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hamburger

Mobile menu trigger. The "Open navigation" icon button — a local disclosure; the opened state was measured after clicking it.

Page: mobile. Selector: `button[aria-label*=navigation]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 4px | = | = | = | = |
| Background | #202022 | = | = | = | #ffffff @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | publicSansRounded 14px/normal 600 | = | = | = | = |
| Letter spacing | -0.14px | = | = | = | = |
| Colour | #f4f4f5 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #f4f4f5 | = | = | = | = |
| ::after | 32px x 32px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = | = | 32px x 32px, absolute, bg #000000 @ 0, radius 4px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Painted layers | button.inline-flex.items-center 32.0x32.0 bg #202022 r 4px; button::after.inline-flex.items-center 32pxx32px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | button.inline-flex.items-center 32.0x32.0 bg #202022 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 1px, #a284ff 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; button::after.inline-flex.items-center 32pxx32px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | button.inline-flex.items-center 32.0x32.0 bg #ffffff @ 0.05 r 4px; button::after.inline-flex.items-center 32pxx32px r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-focus-visible.png`, `m-hamburger-pressed.png`, `m-hamburger-opened.png`.

#### m-nav-item

Mobile nav link. A menuitem row inside the opened vaul bottom-sheet nav; measured, never followed.

Page: mobile. Selector: `mobile nav menuitem`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 499 x 32 |
| Padding | 12px 16px |
| Gap | 12px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | publicSansRounded 14px/20px 400 |
| Letter spacing | normal |
| Colour | #f4f4f5 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #ffffff @ 0.8 |
| How | at rest |

Crops: none.

#### m-search

Mobile search field. The model search field at phone width.

Page: mobile. Selector: `mobile search`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 206.95 x 19.99 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | publicSansRounded 16px/22.8571px 400 |
| Letter spacing | -0.182857px |
| Colour | #ffffff @ 0.8 |
| Transition | none |
| Cursor | text |
| Placeholder | #ffffff @ 0.8, opacity 1 |
| Painted layers | input.flex.min-w-0 207.0x20.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `m-search-default.png`.

#### m-model-card

Mobile model card. A model tile (a.page-model-card) in the phone catalog grid.

Page: mobile. Selector: `mobile model card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 283.19 x 307.28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | publicSansRounded 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.badge.badge-role-lime: publicSansRounded 12px/18px 600, #163200, ls -0.12px |
| Transition | none |
| Cursor | pointer |
| Icon | 12 x 12, colour #163200 |
| Painted layers | div::after.flex.h-full 283.188pxx307.281px border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 4px; div.relative.aspect-[16/9] 283.2x159.3 image linear-gradient(to right in oklab, #ffffff @ 0.03 0%, #ffffff @ 0.05 50%, #ffffff @ 0.03 1; div.badge.badge-role-lime 44.6x16.0 bg #a2d81c border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div::before.relative.flex 281.188pxx1px bg #ffffff @ 0.1; div.grid.shrink-0 16.0x16.0 bg #202022 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 2px; button.inline-flex.items-center 16.0x16.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px |
| How | at rest |

Crops: `m-model-card-default.png`.

## Transitions declared in the readable stylesheets

fal.ai serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- api: `grid-template-rows .16s var(--ease-out-quint) 60ms,opacity .1s var(--ease-out-quint)`, `grid-template-rows .2s var(--ease-out-quint),opacity .15s var(--ease-out-quint) 60ms`, `opacity 90ms var(--ease-out-quint)`, `opacity .18s var(--ease-out-quint) 90ms`, `opacity .15s var(--ease-out-quint)`, `opacity var(--sidebar-transition-duration) var(--sidebar-transition-ease), visibility 0s linear var(--sidebar-transition-duration)`, `width var(--sidebar-transition-duration) var(--sidebar-transition-ease), opacity var(--sidebar-transition-duration) var(--sidebar-transition-ease), visibility 0s linear var(--sidebar-transition-duration)`, `none`, `transform 0.55s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.55s, translate 0.18s ease-out`, `transform 0.55s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s`, `opacity 0.24s, transform 0.24s`, `background-color 0.25s 0.5s`

- docs: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long) var(--timing),height var(--duration-long) var(--timing),background var(--duration-short) ease,scale var(--duration-short) var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration)) var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration) var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`, `background-color 0.2s`

- explore: `grid-template-rows .16s var(--ease-out-quint) 60ms,opacity .1s var(--ease-out-quint)`, `grid-template-rows .2s var(--ease-out-quint),opacity .15s var(--ease-out-quint) 60ms`, `opacity 90ms var(--ease-out-quint)`, `opacity .18s var(--ease-out-quint) 90ms`, `opacity .15s var(--ease-out-quint)`, `opacity var(--sidebar-transition-duration) var(--sidebar-transition-ease), visibility 0s linear var(--sidebar-transition-duration)`, `width var(--sidebar-transition-duration) var(--sidebar-transition-ease), opacity var(--sidebar-transition-duration) var(--sidebar-transition-ease), visibility 0s linear var(--sidebar-transition-duration)`, `none`, `transform 0.55s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.55s, translate 0.18s ease-out`, `transform 0.55s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s`, `opacity 0.24s, transform 0.24s`, `background-color 0.25s 0.5s`

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.1s cubic-bezier(0.55, 0.085, 0.68, 0.53), background-color 0.1s cubic-bezier(0.55, 0.085, 0.68, 0.53)`, `color 0.2s, background-color 0.2s`, `color 0.1s cubic-bezier(0.55, 0.055, 0.675, 0.19), background-color 0.1s cubic-bezier(0.55, 0.085, 0.68, 0.53)`, `all`, `background-color 0.2s`, `background-color 0.1s cubic-bezier(0.55, 0.055, 0.675, 0.19)`, `background-color 0.1s cubic-bezier(0.55, 0.085, 0.68, 0.53)`, `none ease-out`, `none`

- login: `grid-template-rows .16s var(--ease-out-quint) 60ms,opacity .1s var(--ease-out-quint)`, `grid-template-rows .2s var(--ease-out-quint),opacity .15s var(--ease-out-quint) 60ms`, `opacity 90ms var(--ease-out-quint)`, `opacity .18s var(--ease-out-quint) 90ms`, `opacity .15s var(--ease-out-quint)`, `opacity var(--sidebar-transition-duration) var(--sidebar-transition-ease), visibility 0s linear var(--sidebar-transition-duration)`, `width var(--sidebar-transition-duration) var(--sidebar-transition-ease), opacity var(--sidebar-transition-duration) var(--sidebar-transition-ease), visibility 0s linear var(--sidebar-transition-duration)`, `none`, `transform 0.55s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.55s, translate 0.18s ease-out`, `transform 0.55s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s`, `opacity 0.24s, transform 0.24s`, `background-color 0.25s 0.5s`

- model: `grid-template-rows .16s var(--ease-out-quint) 60ms,opacity .1s var(--ease-out-quint)`, `grid-template-rows .2s var(--ease-out-quint),opacity .15s var(--ease-out-quint) 60ms`, `opacity 90ms var(--ease-out-quint)`, `opacity .18s var(--ease-out-quint) 90ms`, `opacity .15s var(--ease-out-quint)`, `opacity var(--sidebar-transition-duration) var(--sidebar-transition-ease), visibility 0s linear var(--sidebar-transition-duration)`, `width var(--sidebar-transition-duration) var(--sidebar-transition-ease), opacity var(--sidebar-transition-duration) var(--sidebar-transition-ease), visibility 0s linear var(--sidebar-transition-duration)`, `none`, `transform 0.55s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.55s, translate 0.18s ease-out`, `transform 0.55s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s`, `opacity 0.24s, transform 0.24s`, `background-color 0.25s 0.5s`

- pricing: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.1s cubic-bezier(0.55, 0.085, 0.68, 0.53), background-color 0.1s cubic-bezier(0.55, 0.085, 0.68, 0.53)`, `color 0.2s, background-color 0.2s`, `color 0.1s cubic-bezier(0.55, 0.055, 0.675, 0.19), background-color 0.1s cubic-bezier(0.55, 0.085, 0.68, 0.53)`, `all`, `background-color 0.2s`, `background-color 0.1s cubic-bezier(0.55, 0.055, 0.675, 0.19)`, `background-color 0.1s cubic-bezier(0.55, 0.085, 0.68, 0.53)`, `none ease-out`, `none`
