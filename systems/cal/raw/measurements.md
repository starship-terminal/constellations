# Component measurements

Computed styles read from cal.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's three public hosts — the marketing pages on cal.com, the auth cards on app.cal.com and the public booking page on i.cal.com/peer (including its supported ?theme=dark&embed=true dark mode) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The floating rounded nav bar: wordmark, the Products/Use-cases/Features/Resources dropdowns, Enterprise and Pricing links, Sign in and the dark Get-started button.

Page: home. Selector: `nav.sticky`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1320 x 64 |
| Padding | 0px 14px |
| Gap | 24px |
| Border | none |
| Radius | 18px |
| Background | #f4f4f4 @ 0.72 |
| Box shadow | none |
| Backdrop filter | blur(12px) |
| Outline | none |
| Font | calSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #242424 |
| Text node | button.flex.h-9: calSans 14px/21px 500, #242424 |
| Transition | none |
| Icon | 12 x 12, colour #242424 |
| Painted layers | nav.sticky.top-2 1320.0x64.0 bg #f4f4f4 @ 0.72 r 18px; li.nav-highlight.-z-10 0.0x36.0 bg #242424 @ 0.05 r 10px; span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; div.absolute.top-full 250.8x295.4 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 18px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; button.flex.h-10 106.4x38.0 bg #0f234b @ 0.05 r 10px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Cal.com wordmark anchor.

Page: home. Selector: `nav.sticky a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 101 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | calSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #242424 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Products button that opens the header dropdown; toggled, never followed.

Page: home. Selector: `nav button "Products"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 104.27 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9ca3af 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | calSans 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #242424 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 12 x 12, colour #242424 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.h-9 104.3x36.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9ca3af 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. A plain header link (Pricing).

Page: home. Selector: `nav a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.03 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9ca3af 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | calSans 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #242424 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.flex.h-9 97.0x36.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9ca3af 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-signin

Sign-in link. The Sign-in header action, linking to app.cal.com; measured never followed.

Page: home. Selector: `nav a "Sign in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.09 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #242424 @ 0.04 | = | #242424 @ 0.04 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9ca3af 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | calSans 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #242424 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.h-9.shrink-0 73.1x36.0 bg #242424 @ 0.04 r 10px | a.h-9.shrink-0 73.1x36.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9ca3af 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.h-9.shrink-0 73.1x36.0 bg #242424 @ 0.04 r 10px |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Nav CTA. The dark Get-started header button, linking to app.cal.com/signup; measured never followed.

Page: home. Selector: `nav a "Get started"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.13 x 36 | = | = | = |
| Padding | 1px 14px 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #242424 | = | = | = |
| Radius | 12px | = | = | = |
| Background | #242424 | #242424 @ 0.9 | = | #242424 @ 0.9 |
| Box shadow | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | calSans 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | background-color, box-shadow 0.1s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer | = | = | = |
| ::before | 104.125px x 34px, absolute, bg #000000 @ 0, radius 11px | = | = | = |
| Painted layers | a.relative.inline-flex 106.1x36.0 bg #242424 border T:1px solid #242424 / R:1px solid #242424 / B:1px solid #242424 / L:1px solid #242424 r 12px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | a.relative.inline-flex 106.1x36.0 bg #242424 @ 0.9 border T:1px solid #242424 / R:1px solid #242424 / B:1px solid #242424 / L:1px solid #242424 r 12px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | a.relative.inline-flex 106.1x36.0 bg #242424 border T:1px solid #242424 / R:1px solid #242424 / B:1px solid #242424 / L:1px solid #242424 r 12px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | a.relative.inline-flex 106.1x36.0 bg #242424 @ 0.9 border T:1px solid #242424 / R:1px solid #242424 / B:1px solid #242424 / L:1px solid #242424 r 12px shadow #000000 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Nav dropdown. The Products mega-menu panel, opened by its own trigger: product links beside a booking-app preview card.

Page: home. Selector: `div[role="presentation"].z-50`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 954 x 518.89 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | calSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #242424 |
| Text node | span.text-center.font-semibold: -apple-system 15px/15px 600, #111111, ls -0.15px |
| Transition | none |
| Icon | 10.2 x 6.6, colour #111111 |
| ::before | 954px x 22px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | nav.relative.h-(--popup-height) 954.0x518.9 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 18px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; div.relative.overflow-hidden 896.0x132.0 bg #f3f4f6 r 10px; div.as-phone.relative 204.0x409.2 bg #1a1a1a r 54px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.absolute.top-[110px] 1.8x16.8 bg #2a2a2a r 4px 0px 0px 4px; span.absolute.top-[160px] 1.8x33.6 bg #2a2a2a r 4px 0px 0px 4px; span.absolute.top-[228px] 1.8x33.6 bg #2a2a2a r 4px 0px 0px 4px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A product card inside the opened Products dropdown (title, blurb, thumbnail).

Page: home. Selector: `dropdown item`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 216 x 219.7 | = | = |
| Padding | 8px | = | = |
| Border | none | = | = |
| Radius | 18px | = | = |
| Background | transparent | #242424 @ 0.04 | #242424 @ 0.04 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | calSans 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #242424 | = | = |
| Text node | span.mt-3.flex: calSans 14px/20px 500, #242424 @ 0.85 | span.mt-3.flex: calSans 14px/20px 500, #242424 | span.mt-3.flex: calSans 14px/20px 500, #242424 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | div.ev-photo.relative 200.0x133.3 bg #f3f4f6 r 10px shadow #000000 @ 0.06 0px 1px 2px 0px, #000000 @ 0.22 0px 10px 18px -10px; div::after.ev-photo.relative 200pxx133.328px image radial-gradient(120% 90%, #000000 @ 0 55%, #000000 @ 0.28 100%), url(data:…)'/%3E%3C/svg%3 | a.group.-m-2 216.0x219.7 bg #242424 @ 0.04 r 18px; div.ev-photo.relative 200.0x133.3 bg #f3f4f6 r 10px shadow #000000 @ 0.06 0px 1px 2px 0px, #000000 @ 0.22 0px 10px 18px -10px; div::after.ev-photo.relative 200pxx133.328px image radial-gradient(120% 90%, #000000 @ 0 55%, #000000 @ 0.28 100%), url(data:…)'/%3E%3C/svg%3 | a.group.-m-2 216.0x219.7 bg #242424 @ 0.04 r 18px; div.ev-photo.relative 200.0x133.3 bg #f3f4f6 r 10px shadow #000000 @ 0.06 0px 1px 2px 0px, #000000 @ 0.22 0px 10px 18px -10px; div::after.ev-photo.relative 200pxx133.328px image radial-gradient(120% 90%, #000000 @ 0 55%, #000000 @ 0.28 100%), url(data:…)'/%3E%3C/svg%3 |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-pressed.png`.

### Home

#### hero-title

Hero headline. The "Where people find the time to meet" display headline (it wraps the product mock, so its rect covers the mock too — the text readings are the headline's).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 980 x 172.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | calSans 80px/86.4px 700 |
| Letter spacing | -0.8px |
| Colour | #242424 |
| Transition | none |
| Icon | 13.67 x 13.67, colour #cc4510 |
| Painted layers | span.relative.inline-block 120.0x68.8 bg #f3f4f6 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e7eb 0px 0px 0px 1px inset; canvas.block.size-full 120.0x68.8 bg #e3dccd; canvas.block.size-full 120.0x68.8 bg #e3dccd; canvas.block.size-full 120.0x68.8 bg #e3dccd; span.relative.inline-block 133.0x68.6 bg #f3f4f6 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e7eb 0px 0px 0px 1px inset; span.rounded-[0.35em].bg-hp-line 41.3x17.1 bg #e5e7eb r 4.788px |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede under the headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1292 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | calSans 20px/28px 500 |
| Letter spacing | normal |
| Colour | #6a6e78 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-google

Google signup. The hero Sign-up-with-Google action, linking to app.cal.com SSO; measured never followed.

Page: home. Selector: `a "Sign up with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 312 x 64 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #242424 | = | = | = |
| Radius | 14px | = | = | = |
| Background | #242424 | #242424 @ 0.9 | = | #242424 @ 0.9 |
| Box shadow | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | calSans 20px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 310px x 62px, absolute, bg #000000 @ 0, radius 9px | = | = | = |
| Painted layers | a.relative.inline-flex 312.0x64.0 bg #242424 border T:1px solid #242424 / R:1px solid #242424 / B:1px solid #242424 / L:1px solid #242424 r 14px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | a.relative.inline-flex 312.0x64.0 bg #242424 @ 0.9 border T:1px solid #242424 / R:1px solid #242424 / B:1px solid #242424 / L:1px solid #242424 r 14px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | a.relative.inline-flex 312.0x64.0 bg #242424 border T:1px solid #242424 / R:1px solid #242424 / B:1px solid #242424 / L:1px solid #242424 r 14px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | a.relative.inline-flex 312.0x64.0 bg #242424 @ 0.9 border T:1px solid #242424 / R:1px solid #242424 / B:1px solid #242424 / L:1px solid #242424 r 14px shadow #000000 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-google-default.png`, `hero-google-hover.png`, `hero-google-focus-visible.png`, `hero-google-pressed.png`.

#### hero-microsoft

Microsoft signup. The hero Sign-up-with-Microsoft action; measured never followed.

Page: home. Selector: `a "Sign up with Microsoft"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 312 x 64 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e5e7eb | = | = | = |
| Radius | 14px | = | = | = |
| Background | #ffffff | #f3f4f6 @ 0.5 | = | #f3f4f6 @ 0.5 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | calSans 20px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #242424 | = | = | = |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 310px x 62px, absolute, bg #000000 @ 0, radius 9px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 1px 0px 0px | = | = | 310px x 62px, absolute, bg #000000 @ 0, radius 9px |
| Painted layers | a.relative.inline-flex 312.0x64.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; a::before.relative.inline-flex 310pxx62px r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 1px 0px 0px | a.relative.inline-flex 312.0x64.0 bg #f3f4f6 @ 0.5 border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; a::before.relative.inline-flex 310pxx62px r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 1px 0px 0px | a.relative.inline-flex 312.0x64.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px; a::before.relative.inline-flex 310pxx62px r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 1px 0px 0px | a.relative.inline-flex 312.0x64.0 bg #f3f4f6 @ 0.5 border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-microsoft-default.png`, `hero-microsoft-hover.png`, `hero-microsoft-focus-visible.png`, `hero-microsoft-pressed.png`.

#### hero-email

Email signup link. The quiet "Sign up with email." link under the SSO buttons.

Page: home. Selector: `a "Sign up with email."`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126.86 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #9ca3af @ 0.5 offset 1px | = |
| Font | calSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #242424 | #676b75 | = | #676b75 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.font-medium.text-foreground 126.9x16.0 outline 1px auto #9ca3af @ 0.5 offset 1px | = |

Crops: `hero-email-default.png`, `hero-email-hover.png`, `hero-email-focus-visible.png`, `hero-email-pressed.png`.

#### changelog

Changelog badge. The NEW "Cal.com launches" release pill under the hero.

Page: home. Selector: `changelog pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 228.09 x 32 | = | = | = |
| Padding | 0px 12px 0px 3px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e5e7eb | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #f5f6f8 | = | #f5f6f8 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | calSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #242424 | = | = | = |
| Text node | span.inline-flex.h-6: calSans 11px/11px 500, #242424, ls 0.66px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.inline-flex 228.1x32.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 8px; span.inline-flex.h-6 44.8x24.0 bg #f3f4f6 r 4px | a.relative.inline-flex 228.1x32.0 bg #f5f6f8 border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 8px; span.inline-flex.h-6 44.8x24.0 bg #f3f4f6 r 4px | a.relative.inline-flex 228.1x32.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #9ca3af 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; span.inline-flex.h-6 44.8x24.0 bg #f3f4f6 r 4px | a.relative.inline-flex 228.1x32.0 bg #f5f6f8 border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 8px; span.inline-flex.h-6 44.8x24.0 bg #f3f4f6 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `changelog-default.png`, `changelog-hover.png`, `changelog-focus-visible.png`, `changelog-pressed.png`.

#### hero-mock

Product mock. The booking-page mock inside the hero (Intro call card with the 12:30 slot chips and the Booked badge).

Page: home. Selector: `hero booking mock`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1320 x 676.78 |
| Padding | 168px 14px 96px 14px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | calSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #242424 |
| Text node | span.inline-flex.h-6: calSans 11px/11px 500, #242424, ls 0.66px |
| Transition | none |
| Icon | 13.67 x 13.67, colour #cc4510 |
| Painted layers | a.relative.inline-flex 228.1x32.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 8px; span.inline-flex.h-6 44.8x24.0 bg #f3f4f6 r 4px; span.relative.inline-block 120.0x68.8 bg #f3f4f6 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e7eb 0px 0px 0px 1px inset; canvas.block.size-full 120.0x68.8 bg #e3dccd; canvas.block.size-full 120.0x68.8 bg #e3dccd; canvas.block.size-full 120.0x68.8 bg #e3dccd |
| Ancestor paint | 1 up div.hp.relative bg #ffffff |
| How | at rest |

Crops: `hero-mock-default.png`.

### Pricing

#### pricing-h1

Pricing title. The "Choose your Cal.com subscription" display heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | calSans 64px/64px 700 |
| Letter spacing | -0.64px |
| Colour | #242424 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### pricing-sub

Pricing copy. The lede under the pricing heading.

Page: pricing. Selector: `pricing lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | calSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #676b75 |
| Transition | none |
| How | at rest |

Crops: `pricing-sub-default.png`.

#### plan-tab

Plan tab. A plan-group tab (Individuals/Teams/Organizations/Enterprise); toggled, never checked out.

Page: pricing. Selector: `plan group tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.97 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #9ca3af @ 0.5 offset 0px | = |
| Font | calSans 22px/22px 700 | = | = | = |
| Letter spacing | -0.22px | = | = | = |
| Colour | #242424 | #676b75 | = | #676b75 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #676b75 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.mt-14.mb-4 93.0x22.0 outline 1px auto #9ca3af @ 0.5 offset 0px | = |

Crops: `plan-tab-default.png`, `plan-tab-hover.png`, `plan-tab-focus-visible.png`, `plan-tab-pressed.png`.

#### billing-toggle

Billing switch. The YEARLY billing switch; toggled locally, never checked out.

Page: pricing. Selector: `role=switch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #242424 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #9ca3af @ 0.5 offset 0px | = |
| Font | calSans 10px/15px 400 | = | = | = |
| Letter spacing | 1.2px | = | = | = |
| Colour | #242424 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| ::after | 32px x 32px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.tap-32.h-[18px] 30.0x18.0 bg #242424 r 3.35544e+07px; span.absolute.top-[2px] 14.0x14.0 bg #ffffff r 3.35544e+07px | = | button.tap-32.h-[18px] 30.0x18.0 bg #242424 r 3.35544e+07px outline 1px auto #9ca3af @ 0.5 offset 0px; span.absolute.top-[2px] 14.0x14.0 bg #ffffff r 3.35544e+07px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-focus-visible.png`, `billing-toggle-pressed.png`.

#### plan-card

Plan card. The Free plan card ("Everything you could need for scheduling as an individual").

Page: pricing. Selector: `Free plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 311.75 x 598.44 |
| Padding | 16px |
| Border | 1px solid #dee1e6 |
| Radius | 14px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | calSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #242424 |
| Text node | h2.font-display.text-[19px]: calSans 19px/24.7px 700, #242424, ls -0.19px |
| Transition | none |
| Icon | 14 x 14, colour #ffffff |
| Painted layers | div.@container.flex 311.8x598.4 bg #ffffff border T:1px solid #dee1e6 / R:1px solid #dee1e6 / B:1px solid #dee1e6 / L:1px solid #dee1e6 r 14px; a.flex.w-full 277.8x36.0 bg #242424 r 12px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA. The Free plan "Use for free" action; measured never followed.

Page: pricing. Selector: `Use for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 277.75 x 36 | = | = | = |
| Padding | 6px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #242424 | #242424 @ 0.9 | = | #242424 @ 0.8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #9ca3af @ 0.5 offset 1px | = |
| Font | calSans 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #ffffff | = | = | = |
| Painted layers | a.flex.w-full 277.8x36.0 bg #242424 r 12px | a.flex.w-full 277.8x36.0 bg #242424 @ 0.9 r 12px | a.flex.w-full 277.8x36.0 bg #242424 r 12px outline 1px auto #9ca3af @ 0.5 offset 1px | a.flex.w-full 277.8x36.0 bg #242424 @ 0.8 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### sales-cta

Sales CTA. The Talk-to-sales action beside the heading; measured never followed.

Page: pricing. Selector: `Talk to sales`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 155.55 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #242424 @ 0.04 | = | #242424 @ 0.04 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9ca3af 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | calSans 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #242424 | = | = | = |
| Text node | span: calSans 14px/21px 500, #242424 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.flex.h-9 155.5x36.0 bg #242424 @ 0.04 r 10px; span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.flex.h-9 155.5x36.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9ca3af 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.flex.h-9 155.5x36.0 bg #242424 @ 0.04 r 10px; span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.size-6 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sales-cta-default.png`, `sales-cta-hover.png`, `sales-cta-focus-visible.png`, `sales-cta-pressed.png`.

#### feature-accordion

Feature accordion. A feature-breakdown accordion section; measured closed, never expanded.

Page: pricing. Selector: `feature accordion button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 223.7 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #9ca3af @ 0.5 offset 0px | = |
| Font | calSans 22px/22px 700 | = | = | = |
| Letter spacing | -0.22px | = | = | = |
| Colour | #242424 | #676b75 | = | #676b75 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #676b75 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.mt-14.mb-4 223.7x22.0 outline 1px auto #9ca3af @ 0.5 offset 0px | = |

Crops: `feature-accordion-default.png`, `feature-accordion-hover.png`, `feature-accordion-focus-visible.png`, `feature-accordion-pressed.png`.

### Booking page (public)

#### bk-page

Booker canvas. The booking page's outer container on the lab-grey canvas.

Page: booking. Selector: `main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.text-subtle.mt-2: Inter 14px/20px 600, #6b7280 |
| Transition | none |
| Icon | 16 x 16, colour #3c3e44 |
| Painted layers | div.[--booker-timeslots-width:240px].lg:[--booker-timeslots-width:280px] 1040.0x489.8 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 8px; span::before.current-timezone.flex 163pxx28px bg #eeeff2 r 8px; div.font-normal.border-default 121.6x36.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.[grid-area:main].md:border-subtle 480.0x487.8 border L:1px solid #e5e7eb; button.group.whitespace-nowrap 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px; button.group.whitespace-nowrap 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px |
| Ancestor paint | 1 up body.dRF1rW_variable.upghpG_variable bg #fafafa |
| How | at rest |

Crops: `bk-page-default.png`.

#### bk-title

Event title. The event name ("15 Minute Meeting").

Page: booking. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 232 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/28px 600 |
| Letter spacing | normal |
| Colour | #3c3e44 |
| Transition | none |
| How | at rest |

Crops: `bk-title-default.png`.

#### bk-host

Host line. The host line under the title (other people's names stay per policy).

Page: booking. Selector: `host line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 232 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #3c3e44 |
| Text node | p: Inter 14px/20px 400, #3c3e44 |
| Transition | none |
| How | at rest |

Crops: `bk-host-default.png`.

#### bk-badge

Confirmation badge. The "Requires confirmation" badge under the title.

Page: booking. Selector: `confirmation badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 232 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 500 |
| Letter spacing | normal |
| Colour | #3c3e44 |
| Text node | div.relative.z-10: Inter 14px/20px 500, #3c3e44 |
| Transition | none |
| Icon | 16 x 16, colour #3c3e44 |
| How | at rest |

Crops: `bk-badge-default.png`.

#### bk-meta

Timezone row. The timezone meta row (Asia/Singapore).

Page: booking. Selector: `timezone row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 232 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | normal |
| Colour | #3c3e44 |
| Text node | p.truncate: Inter 14px/20px 400, #3c3e44 |
| Transition | none |
| Icon | 16 x 16, colour #3c3e44 |
| Painted layers | span::before.current-timezone.flex 163pxx28px bg #eeeff2 r 8px; div.font-normal.border-default 121.6x36.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `bk-meta-default.png`.

#### bk-calendar

Calendar grid. The month grid (grid-cols-7) holding the day buttons.

Page: booking. Selector: `button[data-testid=day] grid ancestor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 439 x 375.78 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #3c3e44 |
| Text node | button.disabled:text-bookinglighter.absolute: Inter 14px/20px 300, #3c3e44 |
| Transition | none |
| Painted layers | button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `bk-calendar-default.png`.

#### bk-day

Day button. A bookable day in the month grid; clicking it is a local toggle that shows that day's slots.

Page: booking. Selector: `button[data-testid=day]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 59.28 x 59.3 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #292929 | = | 2px solid #292929 |
| Radius | 8px | = | = | = |
| Background | #e5e7eb | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #a1a1a1 @ 0.5 offset 0px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #070a0d | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.disabled:text-bookinglighter.absolute 59.3x59.3 bg #e5e7eb border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px | button.disabled:text-bookinglighter.absolute 59.3x59.3 bg #e5e7eb border T:2px solid #292929 / R:2px solid #292929 / B:2px solid #292929 / L:2px solid #292929 r 8px | button.disabled:text-bookinglighter.absolute 59.3x59.3 bg #e5e7eb border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px outline 1px auto #a1a1a1 @ 0.5 offset 0px | button.disabled:text-bookinglighter.absolute 59.3x59.3 bg #e5e7eb border T:2px solid #292929 / R:2px solid #292929 / B:2px solid #292929 / L:2px solid #292929 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bk-day-default.png`, `bk-day-hover.png`, `bk-day-focus-visible.png`, `bk-day-pressed.png`.

#### bk-day-today

Today cell. The today cell in the month grid (its "Today" label is sr-only; the date number paints).

Page: booking. Selector: `button[data-testid=day] Today`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 59.3 x 59.3 |
| Padding | 0px |
| Border | 2px solid #000000 @ 0 |
| Radius | 8px |
| Background | #292929 |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Painted layers | button.disabled:text-bookinglighter.absolute 59.3x59.3 bg #292929 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; span.absolute.left-1/2 5.0x5.0 bg #ffffff r 3.35544e+07px |
| How | at rest |

Crops: `bk-day-today-default.png`.

#### bk-slot

Time slot. An available time slot; clicking it opens the guest details form (captured, never filled or confirmed).

Page: booking. Selector: `time slot`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 239 x 36 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #d1d5db | 1px solid #292929 | = | 1px solid #292929 |
| Radius | 10px | = | = | = |
| Background | #ffffff | #f6f7f9 | #eeeff2 | #f6f7f9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 2px 3px 0px, #000000 @ 0.03 0px 2px 2px -1px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px, #000000 @ 0.1 0px 0px 0px 2px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 2px 1px 0px inset |
| Outline | none | = | = | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3c3e44 | #070a0d | = | #070a0d |
| Text node | time.tabular-nums.text-center: Inter 14px/14px 500, #3c3e44 | time.tabular-nums.text-center: Inter 14px/14px 500, #070a0d | = | time.tabular-nums.text-center: Inter 14px/14px 500, #070a0d |
| Transition | box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group.whitespace-nowrap 239.0x36.0 bg #ffffff border T:1px solid #d1d5db / R:1px solid #d1d5db / B:1px solid #d1d5db / L:1px solid #d1d5db r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 2px 3px 0px, #000000 @ 0.03 0px 2px 2px -1px | button.group.whitespace-nowrap 239.0x36.0 bg #f6f7f9 border T:1px solid #292929 / R:1px solid #292929 / B:1px solid #292929 / L:1px solid #292929 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 2px 3px 0px, #000000 @ 0.03 0px 2px 2px -1px | button.group.whitespace-nowrap 239.0x36.0 bg #eeeff2 border T:1px solid #d1d5db / R:1px solid #d1d5db / B:1px solid #d1d5db / L:1px solid #d1d5db r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px, #000000 @ 0.1 0px 0px 0px 2px | button.group.whitespace-nowrap 239.0x36.0 bg #f6f7f9 border T:1px solid #292929 / R:1px solid #292929 / B:1px solid #292929 / L:1px solid #292929 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 2px 1px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bk-slot-default.png`, `bk-slot-hover.png`, `bk-slot-focus-visible.png`, `bk-slot-pressed.png`.

#### bk-form

Details form. The guest details form a slot opens: name/email/notes fields and the confirm action. Measured, never filled or submitted.

Page: booking. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 371 x 429.33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #3c3e44 |
| Text node | label.text-emphasis.mb-2: Inter 14px/14px 500, #070a0d |
| Transition | none |
| Icon | 0 x 0, colour #070a0d |
| Painted layers | button.relative.inline-flex 0.0x0.0 bg #ffffff border T:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 10px 0px 0px 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; button::before.relative.inline-flex autoxauto r 9px 0px 0px 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111111 @ 0.04 0px 1px 0px 0px; div.shrink-0.data-[orientation=horizontal]:h-px 0.0x0.0 bg #111111 @ 0.1; div.relative.inline-flex 0.0x0.0 bg #ffffff border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 r 0px 10px 10px 0px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div::before.relative.inline-flex autoxauto r 0px 9px 9px 0px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111111 @ 0.04 0px 1px 0px 0px; input.border.bg-default 371.0x32.0 bg #ffffff border T:1px solid #d1d5db / R:1px solid #d1d5db / B:1px solid #d1d5db / L:1px solid #d1d5db r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 2px 3px 0px, #000000 @ 0.03 0px 2px 2px -1px |
| How | at rest |

Crops: `bk-form-default.png`.

#### bk-field

Form field. A text field in the details form; focused by a click, never typed into or submitted.

Page: booking. Selector: `form input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 371 x 32 | = |
| Padding | 8px 12px | = |
| Border | 1px solid #d1d5db | 1px solid #9ca3b0 |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 2px 3px 0px, #000000 @ 0.03 0px 2px 2px -1px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px, #000000 @ 0.1 0px 0px 0px 2px |
| Outline | none | = |
| Font | Inter 14px/14px 500 | = |
| Letter spacing | normal | = |
| Colour | #3c3e44 | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #9ca3b0, opacity 1 | = |
| Painted layers | input.border.bg-default 371.0x32.0 bg #ffffff border T:1px solid #d1d5db / R:1px solid #d1d5db / B:1px solid #d1d5db / L:1px solid #d1d5db r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 2px 3px 0px, #000000 @ 0.03 0px 2px 2px -1px | input.border.bg-default 371.0x32.0 bg #ffffff border T:1px solid #9ca3b0 / R:1px solid #9ca3b0 / B:1px solid #9ca3b0 / L:1px solid #9ca3b0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px, #000000 @ 0.1 0px 0px 0px 2px |
| How | at rest | clicked into the field |

Crops: `bk-field-default.png`, `bk-field-focused.png`.

#### bk-confirm

Confirm button. The booking confirm action; measured only — a real press would create a booking, so it was never clicked (pressed is a CDP-forced state).

Page: booking. Selector: `form confirm button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76.06 x 32 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #292929 | = | = | = |
| Radius | 10px | = | = | = |
| Background | #292929 | #696969 | #696969 | #696969 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 2px 3px 0px, #000000 @ 0.08 0px 1px 1px 0px, #000000 @ 0.12 1px 4px 8px 0px, #ffffff @ 0.12 0px 2px 0.4px 0px inset, #000000 @ 0.04 0px -3px 2px 0px inset | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 1px 0px, #000000 @ 0.08 0px 2px 3px 0px, #000000 @ 0.12 1px 4px 8px 0px, #000000 @ 0.1 0px -3px 2px 0px inset, #ffffff @ 0.24 0px 2px 0.4px 0px inset | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 1px 0px, #000000 @ 0.08 0px 2px 3px 0px, #000000 @ 0.12 1px 4px 8px 0px, #000000 @ 0.1 0px -3px 2px 0px inset, #ffffff @ 0.24 0px 2px 0.4px 0px inset | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0.1 0px 3px 1px 0px inset, #000000 @ 0.1 0px 0px 2px 0px inset |
| Outline | none | = | = | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | transform, translate, scale, rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group.whitespace-nowrap 76.1x32.0 bg #292929 border T:1px solid #292929 / R:1px solid #292929 / B:1px solid #292929 / L:1px solid #292929 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 2px 3px 0px, #000000 @ 0.08 0px 1px 1px 0px, #000000 @ 0.12 1px 4px 8px 0px, #ffffff @ 0.12 0px 2px 0.4px 0px inset, #000000 @ 0.04 0px -3px 2px 0px inset | button.group.whitespace-nowrap 76.1x32.0 bg #696969 border T:1px solid #292929 / R:1px solid #292929 / B:1px solid #292929 / L:1px solid #292929 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 1px 0px, #000000 @ 0.08 0px 2px 3px 0px, #000000 @ 0.12 1px 4px 8px 0px, #000000 @ 0.1 0px -3px 2px 0px inset, #ffffff @ 0.24 0px 2px 0.4px 0px inset | button.group.whitespace-nowrap 76.1x32.0 bg #696969 border T:1px solid #292929 / R:1px solid #292929 / B:1px solid #292929 / L:1px solid #292929 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 1px 0px, #000000 @ 0.08 0px 2px 3px 0px, #000000 @ 0.12 1px 4px 8px 0px, #000000 @ 0.1 0px -3px 2px 0px inset, #ffffff @ 0.24 0px 2px 0.4px 0px inset | button.group.whitespace-nowrap 76.1x32.0 bg #696969 border T:1px solid #292929 / R:1px solid #292929 / B:1px solid #292929 / L:1px solid #292929 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0.1 0px 3px 1px 0px inset, #000000 @ 0.1 0px 0px 2px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bk-confirm-default.png`, `bk-confirm-hover.png`, `bk-confirm-focus-visible.png`, `bk-confirm-pressed.png`.

### Booking page, dark

#### bkd-canvas

Dark booker canvas. The booking page under its supported ?theme=dark&embed=true mode: the real dark theme, not a forced class.

Page: bookingdark. Selector: `main (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.text-subtle.mt-2: Inter 14px/20px 600, #a3a3a3 |
| Transition | none |
| Icon | 16 x 16, colour #d4d4d4 |
| Painted layers | div.[--booker-timeslots-width:240px].lg:[--booker-timeslots-width:280px] 1040.0x489.8 bg #171717 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 8px; span::before.current-timezone.flex 163pxx28px bg #262626 r 8px; div.font-normal.border-default 121.6x36.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.[grid-area:main].md:border-subtle 480.0x487.8 border L:1px solid #262626; button.group.whitespace-nowrap 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px; button.group.whitespace-nowrap 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px |
| Ancestor paint | 1 up body.dRF1rW_variable.upghpG_variable bg #111111 |
| How | at rest |

Crops: `bkd-canvas-default.png`.

#### bkd-title

Dark event title.

Page: bookingdark. Selector: `h1 (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 232 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/28px 600 |
| Letter spacing | normal |
| Colour | #d4d4d4 |
| Transition | none |
| How | at rest |

Crops: `bkd-title-default.png`.

#### bkd-calendar

Dark calendar.

Page: bookingdark. Selector: `calendar grid (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 439 x 375.78 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #d4d4d4 |
| Text node | button.disabled:text-bookinglighter.absolute: Inter 14px/20px 300, #d4d4d4 |
| Transition | none |
| Painted layers | button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.disabled:text-bookinglighter.absolute 59.3x59.3 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `bkd-calendar-default.png`.

#### bkd-slot

Dark time slot. A dark-mode slot button; measured, never followed.

Page: bookingdark. Selector: `time slot (dark)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 239 x 36 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #4d4d4d | 1px solid #fafafa | = | 1px solid #fafafa |
| Radius | 10px | = | = | = |
| Background | #0f0f0f | #171717 | #262626 | #171717 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 2px 3px 0px, #000000 @ 0.03 0px 2px 2px -1px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px, #000000 @ 0.1 0px 0px 0px 2px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 2px 1px 0px inset |
| Outline | none | = | = | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #d4d4d4 | #fafafa | = | #fafafa |
| Text node | time.tabular-nums.text-center: Inter 14px/14px 500, #d4d4d4 | time.tabular-nums.text-center: Inter 14px/14px 500, #fafafa | = | time.tabular-nums.text-center: Inter 14px/14px 500, #fafafa |
| Transition | box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group.whitespace-nowrap 239.0x36.0 bg #0f0f0f border T:1px solid #4d4d4d / R:1px solid #4d4d4d / B:1px solid #4d4d4d / L:1px solid #4d4d4d r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 2px 3px 0px, #000000 @ 0.03 0px 2px 2px -1px | button.group.whitespace-nowrap 239.0x36.0 bg #171717 border T:1px solid #fafafa / R:1px solid #fafafa / B:1px solid #fafafa / L:1px solid #fafafa r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 2px 3px 0px, #000000 @ 0.03 0px 2px 2px -1px | button.group.whitespace-nowrap 239.0x36.0 bg #262626 border T:1px solid #4d4d4d / R:1px solid #4d4d4d / B:1px solid #4d4d4d / L:1px solid #4d4d4d r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px, #000000 @ 0.1 0px 0px 0px 2px | button.group.whitespace-nowrap 239.0x36.0 bg #171717 border T:1px solid #fafafa / R:1px solid #fafafa / B:1px solid #fafafa / L:1px solid #fafafa r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 2px 1px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bkd-slot-default.png`, `bkd-slot-hover.png`, `bkd-slot-focus-visible.png`, `bkd-slot-pressed.png`.

### Auth cards

#### auth-card

Login card. The sign-in card on app.cal.com: SSO buttons, the email and password fields, Forgot?, Continue. Captured as a boundary — never filled or submitted.

Page: login. Selector: `login card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 446 x 516 |
| Padding | 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | h1.font-heading.mb-1: fontHeading 20px/28px 700, #070a0d |
| Transition | none |
| Icon | 16 x 16, colour #262626 |
| Painted layers | button.relative.inline-flex 366.0x36.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 10px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px; button.relative.inline-flex 366.0x36.0 bg #111111 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px; div.bg-border.data-[orientation=horizontal]:h-px 160.2x1.0 bg #111111 @ 0.08; div.bg-border.data-[orientation=horizontal]:h-px 160.2x1.0 bg #111111 @ 0.08; span.relative.inline-flex 366.0x32.0 bg #ffffff border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span::before.relative.inline-flex 364pxx30px r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111111 @ 0.04 0px 1px 0px 0px |
| Ancestor paint | 1 up div.relative.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; 2 up div.relative.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 10px 15px -3px, #000000 @ 0.05 0px 4px 6px -4px |
| How | at rest |

Crops: `auth-card-default.png`.

#### auth-title

Login title. The "Welcome back! Sign in to continue" heading.

Page: login. Selector: `welcome back`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #696969 |
| Transition | none |
| Ancestor paint | 2 up div.relative.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; 3 up div.relative.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 10px 15px -3px, #000000 @ 0.05 0px 4px 6px -4px |
| How | at rest |

Crops: `auth-title-default.png`.

#### sso-google

Google SSO. The Sign-in-with-Google button; measured never followed.

Page: login. Selector: `SSO button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 366 x 36 | = | = | = |
| Padding | 0px 13px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #262626 | = | = | = |
| Radius | 10px | = | = | = |
| Background | #262626 | #262626 @ 0.9 | = | #262626 @ 0.9 |
| Box shadow | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px | = | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #262626 @ 0.24 0px 1px 2px 0px | #111111 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | fontSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | span: fontSans 14px/20px 500, #fafafa | = | = | = |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 364px x 34px, absolute, bg #000000 @ 0, radius 9px | = | = | = |
| Painted layers | button.relative.inline-flex 366.0x36.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 10px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px | button.relative.inline-flex 366.0x36.0 bg #262626 @ 0.9 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 10px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px | button.relative.inline-flex 366.0x36.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 10px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #262626 @ 0.24 0px 1px 2px 0px | button.relative.inline-flex 366.0x36.0 bg #262626 @ 0.9 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 10px shadow #111111 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 3 up div.relative.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-google-default.png`, `sso-google-hover.png`, `sso-google-focus-visible.png`, `sso-google-pressed.png`.

#### email-field

Email field. The email input; focused by a click, never typed into or submitted.

Page: login. Selector: `input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 364 x 30 | = |
| Padding | 0px 11px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | fontSans 14px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #262626 | = |
| Transition | background-color 5e+06s ease-in-out | = |
| Cursor | text | = |
| Placeholder | #262626, opacity 1 | = |
| Ancestor paint | 1 up span.relative.inline-flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | 1 up span.relative.inline-flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a1a1a1 @ 0.24 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |

Crops: `email-field-default.png`, `email-field-focused.png`.

#### pass-field

Password field. The password input; focused by a click, never typed into or submitted.

Page: login. Selector: `input[type=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 337 x 30 | = |
| Padding | 0px 8px 0px 11px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | fontSans 14px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #262626 | = |
| Transition | background-color 5e+06s ease-in-out | = |
| Cursor | text | = |
| Placeholder | #262626, opacity 1 | = |
| Ancestor paint | 2 up div.relative.inline-flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | 2 up div.relative.inline-flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a1a1a1 @ 0.24 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |

Crops: `pass-field-default.png`, `pass-field-focused.png`.

#### forgot-link

Forgot link. The "Forgot?" password link.

Page: login. Selector: `a "Forgot?"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 51.25 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #a1a1a1 @ 0.5 offset 1px | = |
| Font | fontSans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #696969 | #262626 | = | #262626 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.col-start-2.row-start-1 51.3x20.0 outline 1px auto #a1a1a1 @ 0.5 offset 1px | = |

Crops: `forgot-link-default.png`, `forgot-link-hover.png`, `forgot-link-focus-visible.png`, `forgot-link-pressed.png`.

#### continue-btn

Continue button. The sign-in submit; measured only, never clicked (pressed is CDP-forced).

Page: login. Selector: `button "Continue"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 366 x 36 | = | = | = |
| Padding | 0px 13px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #262626 | = | = | = |
| Radius | 10px | = | = | = |
| Background | #262626 | #262626 @ 0.9 | = | #262626 @ 0.9 |
| Box shadow | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px | = | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #262626 @ 0.24 0px 1px 2px 0px | #111111 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | fontSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 364px x 34px, absolute, bg #000000 @ 0, radius 9px | = | = | = |
| Painted layers | button.relative.inline-flex 366.0x36.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 10px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px | button.relative.inline-flex 366.0x36.0 bg #262626 @ 0.9 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 10px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px | button.relative.inline-flex 366.0x36.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 10px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #262626 @ 0.24 0px 1px 2px 0px | button.relative.inline-flex 366.0x36.0 bg #262626 @ 0.9 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 10px shadow #111111 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 3 up div.relative.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `continue-btn-default.png`, `continue-btn-hover.png`, `continue-btn-focus-visible.png`, `continue-btn-pressed.png`.

#### saml-link

SAML link. The "Sign in with SAML/OIDC" action.

Page: login. Selector: `SAML/OIDC`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 163.81 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | fontSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262626 | = | = | = |
| Text node | span: fontSans 14px/20px 500, #262626 | = | = | = |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 161.812px x 30px, absolute, bg #000000 @ 0, radius 9px | = | = | = |
| Painted layers | button.relative.inline-flex 163.8x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px | = | button.relative.inline-flex 163.8x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Ancestor paint | 2 up div.relative.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 10px 15px -3px, #000000 @ 0.05 0px 4px 6px -4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `saml-link-default.png`, `saml-link-hover.png`, `saml-link-focus-visible.png`, `saml-link-pressed.png`.

#### signup-title

Signup title. The "Claim cal.com/you" heading on the signup card.

Page: signup. Selector: `claim cal.com/you`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontHeading 56px/56px 700 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| Ancestor paint | 3 up div.relative.not-dark:bg-clip-padding shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `signup-title-default.png`.

#### signup-google

Google continue. The Continue-with-Google button; measured never followed.

Page: signup. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 440 x 40 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #262626 | = | = | = |
| Radius | 14px | = | = | = |
| Background | #262626 | #262626 @ 0.9 | = | #262626 @ 0.9 |
| Box shadow | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px | = | #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #262626 @ 0.24 0px 1px 2px 0px | #111111 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | fontSans 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 438px x 38px, absolute, bg #000000 @ 0, radius 9px | = | = | = |
| Painted layers | button.relative.inline-flex 440.0x40.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 14px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px | button.relative.inline-flex 440.0x40.0 bg #262626 @ 0.9 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 14px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px | button.relative.inline-flex 440.0x40.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 14px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #262626 @ 0.24 0px 1px 2px 0px | button.relative.inline-flex 440.0x40.0 bg #262626 @ 0.9 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 14px shadow #111111 @ 0.08 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-google-default.png`, `signup-google-hover.png`, `signup-google-focus-visible.png`, `signup-google-pressed.png`.

#### signup-email

Email continue. The Continue-with-Email button; measured never followed.

Page: signup. Selector: `Continue with Email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 440 x 40 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #111111 @ 0.1 | = | = | = |
| Radius | 14px | = | = | = |
| Background | #ffffff | #111111 @ 0.02 | = | #111111 @ 0.02 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | fontSans 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262626 | = | = | = |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #262626 | = | = | = |
| ::before | 438px x 38px, absolute, bg #000000 @ 0, radius 9px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111111 @ 0.04 0px 1px 0px 0px | = | = | 438px x 38px, absolute, bg #000000 @ 0, radius 9px |
| Painted layers | button.relative.inline-flex 440.0x40.0 bg #ffffff border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; button::before.relative.inline-flex 438pxx38px r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111111 @ 0.04 0px 1px 0px 0px | button.relative.inline-flex 440.0x40.0 bg #111111 @ 0.02 border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; button::before.relative.inline-flex 438pxx38px r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111111 @ 0.04 0px 1px 0px 0px | button.relative.inline-flex 440.0x40.0 bg #ffffff border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #a1a1a1 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px; button::before.relative.inline-flex 438pxx38px r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111111 @ 0.04 0px 1px 0px 0px | button.relative.inline-flex 440.0x40.0 bg #111111 @ 0.02 border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-email-default.png`, `signup-email-hover.png`, `signup-email-focus-visible.png`, `signup-email-pressed.png`.

#### trust-row

Trust row. The rating row (Trustpilot / Product Hunt / G2) beside the signup card.

Page: signup. Selector: `rating row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 78 x 13 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSans 13px/13px 400 |
| Letter spacing | normal |
| Colour | #696969 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `trust-row-default.png`.

#### signup-card

Signup card. The signup card on app.cal.com: Continue-with-SSO buttons and the plan pitch. Captured as a boundary — never followed.

Page: signup. Selector: `signup card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 184 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | button.relative.inline-flex: fontSans 16px/24px 500, #fafafa |
| Transition | none |
| Icon | 18 x 18, colour #262626 |
| Painted layers | button.relative.inline-flex 440.0x40.0 bg #262626 border T:1px solid #262626 / R:1px solid #262626 / B:1px solid #262626 / L:1px solid #262626 r 14px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #262626 @ 0.24 0px 1px 2px 0px; button.relative.inline-flex 440.0x40.0 bg #ffffff border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; button::before.relative.inline-flex 438pxx38px r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111111 @ 0.04 0px 1px 0px 0px; button.relative.inline-flex 440.0x40.0 bg #ffffff border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; button::before.relative.inline-flex 438pxx38px r 9px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111111 @ 0.04 0px 1px 0px 0px; button.relative.inline-flex 440.0x40.0 bg #ffffff border T:1px solid #111111 @ 0.1 / R:1px solid #111111 @ 0.1 / B:1px solid #111111 @ 0.1 / L:1px solid #111111 @ 0.1 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 3 up div.relative.not-dark:bg-clip-padding shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `signup-card-default.png`.

### Footer

#### footer

Footer. The near-black footer: link columns, app-store badges, social links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1487.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #111111 |
| Box shadow | none |
| Outline | none |
| Font | calSans 14px/21px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.6 |
| Text node | p.m-0.max-w-[300px]: calSans 14px/21px 400, #ffffff @ 0.6 |
| Transition | none |
| Icon | 16 x 16, colour #ffffff @ 0.85 |
| Painted layers | footer.relative.mt-12 1440.0x1487.3 bg #111111; div.h-12.rounded-b-[40px] 1440.0x48.0 bg #ffffff r 0px 0px 40px 40px; a.inline-flex.h-9 192.6x36.0 bg #ffffff @ 0.05 r 10px; span.size-2.rounded-full 8.0x8.0 bg #00d492 r 3.35544e+07px; button.flex.h-9 117.8x36.0 bg #ffffff @ 0.05 r 10px; fieldset.m-0.flex 100.0x36.0 bg #ffffff @ 0.06 r 11px |
| Ancestor paint | 1 up body.bg-(--page-surface).text-foreground bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.47 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #9ca3af @ 0.5 offset 1px | = |
| Font | calSans 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.6 | #ffffff | = | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-white/85 118.5x16.0 outline 1px auto #9ca3af @ 0.5 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `nav at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 374 x 64 |
| Padding | 0px 14px |
| Gap | 16px |
| Border | none |
| Radius | 18px |
| Background | #f4f4f4 @ 0.72 |
| Box shadow | none |
| Backdrop filter | blur(12px) |
| Outline | none |
| Font | calSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #242424 |
| Text node | a.relative.inline-flex: calSans 14px/21px 500, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #242424 |
| Painted layers | nav.sticky.top-2 374.0x64.0 bg #f4f4f4 @ 0.72 r 18px; li.nav-highlight.-z-10 0.0x0.0 bg #242424 @ 0.05 r 10px; span.relative.size-6 0.0x0.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.size-6 0.0x0.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; div.absolute.top-full 0.0x0.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 18px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; button.flex.h-10 0.0x0.0 bg #0f234b @ 0.05 r 10px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The nav menu toggle at 390px.

Page: mobile. Selector: `mobile menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 0px |
| Gap | 8px |
| Border | 1px solid #000000 @ 0 |
| Radius | 10px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | calSans 16px/24px 500 |
| Letter spacing | normal |
| Colour | #242424 |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 18 x 18, colour #242424 |
| ::before | 34px x 34px, absolute, bg #000000 @ 0, radius 9px |
| ::after | 44px x 44px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | button.relative.inline-flex 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The full-screen nav drawer opened by its own toggle.

Page: mobile. Selector: `div[role=dialog]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | T: none; R: none; B: none; L: 1px solid #e5e7eb |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| Outline | none |
| Font | calSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #242424 |
| Text node | button.flex.w-full: calSans 16px/24px 500, #242424 |
| Transition | opacity, translate 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 16, colour #242424 |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 0px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 1px 0px 0px |
| Painted layers | div.relative.flex 390.0x844.0 bg #ffffff border L:1px solid #e5e7eb shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; div::before.relative.flex autoxauto shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 1px 0px 0px; div.flex.px-6 389.0x169.0 bg #f3f4f6 @ 0.72 border T:1px solid #e5e7eb; a.relative.inline-flex 0.0x0.0 bg #242424 border T:1px solid #242424 / R:1px solid #242424 / B:1px solid #242424 / L:1px solid #242424 r 12px shadow #ffffff @ 0.16 0px 1px 0px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; a.relative.inline-flex 341.0x40.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; a::before.relative.inline-flex 339pxx38px r 11px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 1px 0px 0px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A link inside the opened nav drawer.

Page: mobile. Selector: `mobile menu link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 341 x 48 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #242424 @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | calSans 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #242424 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.flex.w-full 341.0x48.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #242424 @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 346 x 136.08 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | calSans 42px/45.36px 700 |
| Letter spacing | -0.42px |
| Colour | #242424 |
| Transition | none |
| Icon | 8.13 x 8.13, colour #cc4510 |
| Painted layers | span.relative.inline-block 63.0x41.2 bg #f3f4f6 r 8.4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e7eb 0px 0px 0px 1px inset; canvas.block.size-full 63.0x41.2 bg #e3dccd; canvas.block.size-full 63.0x41.2 bg #e3dccd; canvas.block.size-full 63.0x41.2 bg #e3dccd; span.relative.inline-block 81.3x41.5 bg #f3f4f6 r 8.4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e7eb 0px 0px 0px 1px inset; span.rounded-[0.35em].bg-hp-line 24.8x10.2 bg #e5e7eb r 2.84445px |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

cal.com serves its Next.js CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- booking: `background-color 5e+06s ease-in-out`, `transform 0.5s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.5s, height 0.15s, background-color 0.5s`, `translate 0.15s, border-radius 0.15s, scale 0.1s 0.1s, transform-origin 0.15s`, `opacity 0.5s, height 0.15s, background-color 0.5s`, `color 150ms`, `100ms`

- home: `background-color 5e+06s ease-in-out`, `translate 0.15s, border-radius 0.15s, scale 0.1s 0.1s, transform-origin 0.15s`, `opacity 0.5s, transform 0.5s`, `transform 0.3s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `opacity 1.2s`, `background 0.2s`, `opacity 0.12s ease-out, filter 0.18s ease-out`, `rotate 0.2s ease-in, scale 0.2s ease-in`, `opacity 0.2s ease-in`, `opacity 0.15s ease-in, transform 0.2s ease-in, visibility linear 0.2s`, `opacity 0.12s ease-in, transform 0.12s ease-in, visibility linear 0.12s`

- pricing: `background-color 5e+06s ease-in-out`, `translate 0.15s, border-radius 0.15s, scale 0.1s 0.1s, transform-origin 0.15s`, `opacity 0.5s, transform 0.5s`, `transform 0.3s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `opacity 1.2s`, `background 0.2s`, `opacity 0.12s ease-out, filter 0.18s ease-out`, `rotate 0.2s ease-in, scale 0.2s ease-in`, `opacity 0.2s ease-in`, `opacity 0.15s ease-in, transform 0.2s ease-in, visibility linear 0.2s`, `opacity 0.12s ease-in, transform 0.12s ease-in, visibility linear 0.12s`
