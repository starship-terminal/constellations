# Fingerprint component measurements

Computed styles read from fingerprint.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the light :root marketing pages (home, identification, smart-signals, ai-agent-detection, a use-case, ai, pricing, demo, contact-sales, blog, case-studies, resources, security, integrations, sdk-libraries, bot-directory, about-us, careers), the Mintlify docs site at docs.fingerprint.com (its own token layer and a real light/dark preference), the product auth shell at dashboard.fingerprint.com /login and /signup (a third stack), and the mobile nav overlay — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). The marketing site ships no dark theme: an emulated prefers-color-scheme pass resolved :root identically, and the only dark redeclaration is the .dark-scoped --fpds-color-syntax-* set for code blocks. The /demo page and the IdentifySection panels paint the capture machine's own visitor ID, IP and geolocation, so the live-signal regions are masked in the committed shots (tools/redact-rules/fingerprint.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The sticky top bar on every marketing page: the Fingerprint wordmark, Product/Use Cases/Resources dropdown triggers, AI, Docs, Demo, Pricing, Login, Contact Sales and the "Get Started" CTA.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0.8 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px |
| Backdrop filter | blur(10px) |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.relative.z-[1]: Inter-c0aaf1024c6c51d7 13px/22px 500, #484946 |
| Transition | none |
| Painted layers | header.relative.z-[100] 1440.0x56.0 bg #ffffff @ 0.8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px; a.relative.select-none 109.0x32.0 bg #fefefd border T:1px solid #f35b22 / R:1px solid #f35b22 / B:1px solid #f35b22 / L:1px solid #f35b22 r 6px; a.relative.select-none 96.0x32.0 bg #f35820 border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px; span.absolute.left-0 0.0x0.0 bg #202021; span.absolute.left-0 0.0x0.0 bg #202021; span.absolute.left-0 0.0x0.0 bg #202021 |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Fingerprint wordmark in the header, linking home.

Page: home. Selector: `header a[href=/]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 137.59 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-dropdown-btn

Nav dropdown trigger. The "Product" header button — aria-expanded flips and the dropdown panel mounts beside it. The opened state was measured after its own toggle click; aria-expanded had to stay true.

Page: home. Selector: `header button Product`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 69 x 28 | = | = | = | = |
| Padding | 3px 10px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 4px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Inter-c0aaf1024c6c51d7 13px/22px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #484946 | = | = | = | = |
| Text node | span.relative.z-[1]: Inter-c0aaf1024c6c51d7 13px/22px 500, #484946 | = | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | default | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | span.absolute.inset-x-0 69.0x29.0 bg #fafaf8 border T:1px solid #e4e5e1 @ 0.8 / R:1px solid #e4e5e1 @ 0.8 / B:1px solid #e4e5e1 @ 0.8 / L:1px solid #e4e5e1 @ 0.8 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #77361c @ 0.2 0px 0.5px 0.5px 0px | button.relative.flex 69.0x28.0 r 4px outline 1px auto #101010 offset 0px; span.absolute.inset-x-0 69.0x29.0 bg #fafaf8 border T:1px solid #e4e5e1 @ 0.8 / R:1px solid #e4e5e1 @ 0.8 / B:1px solid #e4e5e1 @ 0.8 / L:1px solid #e4e5e1 @ 0.8 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #77361c @ 0.2 0px 0.5px 0.5px 0px | span.absolute.inset-x-0 69.0x29.0 bg #fafaf8 border T:1px solid #e4e5e1 @ 0.8 / R:1px solid #e4e5e1 @ 0.8 / B:1px solid #e4e5e1 @ 0.8 / L:1px solid #e4e5e1 @ 0.8 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #77361c @ 0.2 0px 0.5px 0.5px 0px | span.absolute.inset-x-0 69.0x29.0 bg #fafaf8 border T:1px solid #e4e5e1 @ 0.8 / R:1px solid #e4e5e1 @ 0.8 / B:1px solid #e4e5e1 @ 0.8 / L:1px solid #e4e5e1 @ 0.8 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #77361c @ 0.2 0px 0.5px 0.5px 0px |

Crops: `nav-dropdown-btn-default.png`, `nav-dropdown-btn-hover.png`, `nav-dropdown-btn-focus-visible.png`, `nav-dropdown-btn-pressed.png`, `nav-dropdown-btn-opened.png`.

#### nav-panel

Product dropdown panel. The dropdown panel opened by the "Product" trigger (Device Intelligence, Smart Signals, product entries); its links were never followed.

Page: home. Selector: `product dropdown panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1288 x 262 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.mb-4.pl-3: Inter-c0aaf1024c6c51d7 12px/16px 400, #a0a09d, ls 0.48px |
| Transition | none |
| Icon | 14 x 14, colour #000000 |
| Painted layers | div.relative.overflow-hidden 854.0x258.0 bg #fafaf8 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #77361c @ 0.2 0px 0.5px 0.5px 0px outline 1px solid #e4e5e1 @ 0.8 offset 0px; div.flex.flex-col 846.0x250.4 bg #ffffff border T:1px solid #d9d9d6 / R:1px solid #d9d9d6 / B:1px solid #d9d9d6 / L:1px solid #d9d9d6 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.4 0px 1px 0px 0px inset, #000000 @ 0.04 0px -2px 0px 0px inset; a.group/link.flex 280.0x58.8 r 8px outline 1px solid #000000 @ 0 offset 2px; span.flex.h-7 28.0x28.0 bg #ffffff image linear-gradient(301deg, #484946 @ 0.02 9.55%, #6e6f6c @ 0.02 67.28%) border T:1px solid #f0f0ed / R:1px solid #f0f0ed / B:1px solid #f0f0ed / L:1px solid #f0f0ed r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px; a.group/link.flex 280.0x58.8 r 8px outline 1px solid #000000 @ 0 offset 2px; span.flex.h-7 28.0x28.0 bg #ffffff image linear-gradient(301deg, #484946 @ 0.02 9.55%, #6e6f6c @ 0.02 67.28%) border T:1px solid #f0f0ed / R:1px solid #f0f0ed / B:1px solid #f0f0ed / L:1px solid #f0f0ed r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px |
| Ancestor paint | 3 up header.relative.z-[100] bg #ffffff @ 0.8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-menu-item

Dropdown item. The "Identification" item inside the opened product dropdown; measured, never followed.

Page: home. Selector: `product dropdown item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 280 x 58.8 | = |
| Padding | 8px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | #fafaf8 |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.02 0px 2px 1px 0px |
| Outline | 1px solid #000000 @ 0 offset 2px | 1px dashed #e8e8e8 offset 0px |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.text-[14px].font-medium: Inter-c0aaf1024c6c51d7 14px/22px 500, #181916 | = |
| Transition | background, outline 0.25s cubic-bezier(0, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 14 x 14, colour #000000 | = |
| Painted layers | a.group/link.flex 280.0x58.8 r 8px outline 1px solid #000000 @ 0 offset 2px; span.flex.h-7 28.0x28.0 bg #ffffff image linear-gradient(301deg, #484946 @ 0.02 9.55%, #6e6f6c @ 0.02 67.28%) border T:1px solid #f0f0ed / R:1px solid #f0f0ed / B:1px solid #f0f0ed / L:1px solid #f0f0ed r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px | a.group/link.flex 280.0x58.8 bg #fafaf8 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.02 0px 2px 1px 0px outline 1px dashed #e8e8e8 offset 0px; span.flex.h-7 28.0x28.0 bg #ffffff image linear-gradient(301deg, #484946 @ 0.02 9.55%, #6e6f6c @ 0.02 67.28%) border T:1px solid #f0f0ed / R:1px solid #f0f0ed / B:1px solid #f0f0ed / L:1px solid #f0f0ed r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px |
| How | at rest | mouse hover |

Crops: `nav-menu-item-default.png`, `nav-menu-item-hover.png`.

#### nav-pricing

Nav link. The "Pricing" header link; measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62 x 28 | = | = | = |
| Padding | 3px 10px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f35820 offset 2px | = |
| Font | Inter-c0aaf1024c6c51d7 13px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #484946 | = | = | = |
| Text node | span.relative.z-[1]: Inter-c0aaf1024c6c51d7 13px/22px 500, #484946 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | span.absolute.inset-x-0 62.0x29.0 bg #fafaf8 border T:1px solid #e4e5e1 @ 0.8 / R:1px solid #e4e5e1 @ 0.8 / B:1px solid #e4e5e1 @ 0.8 / L:1px solid #e4e5e1 @ 0.8 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #77361c @ 0.2 0px 0.5px 0.5px 0px | a.relative.flex 62.0x28.0 r 4px outline 2px solid #f35820 offset 2px; span.absolute.inset-x-0 62.0x29.0 bg #fafaf8 border T:1px solid #e4e5e1 @ 0.8 / R:1px solid #e4e5e1 @ 0.8 / B:1px solid #e4e5e1 @ 0.8 / L:1px solid #e4e5e1 @ 0.8 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #77361c @ 0.2 0px 0.5px 0.5px 0px | span.absolute.inset-x-0 62.0x29.0 bg #fafaf8 border T:1px solid #e4e5e1 @ 0.8 / R:1px solid #e4e5e1 @ 0.8 / B:1px solid #e4e5e1 @ 0.8 / L:1px solid #e4e5e1 @ 0.8 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #77361c @ 0.2 0px 0.5px 0.5px 0px |

Crops: `nav-pricing-default.png`, `nav-pricing-hover.png`, `nav-pricing-focus-visible.png`, `nav-pricing-pressed.png`.

#### nav-login

Login link. The "Login" header link to dashboard.fingerprint.com/login; measured, never followed.

Page: home. Selector: `header a Login`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 31 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter-c0aaf1024c6c51d7 12px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f35b22 | #be400f | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.relative.select-none 31.0x18.0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Header CTA. The orange "Get Started" header pill (the brand-primary fill); links to dashboard.fingerprint.com/signup, measured never followed.

Page: home. Selector: `header a Get Started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96 x 32 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #bd400f | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f35820 | #bd400f | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | Inter-c0aaf1024c6c51d7 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.select-none 96.0x32.0 bg #f35820 border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | a.relative.select-none 96.0x32.0 bg #bd400f border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | a.relative.select-none 96.0x32.0 bg #f35820 border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### chat-btn

Chat launcher. The floating "Open the chat" support-widget launcher pinned bottom-right; measured, never opened.

Page: home. Selector: `button Open the chat`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | = | = | = |
| Padding | 4px | = | = | = |
| Border | 1px dashed #e4e5e1 | = | = | = |
| Radius | 50% | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f35b22 offset 0px | = |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| Painted layers | button._root_16ia3_3 56.0x56.0 border T:1px dashed #e4e5e1 / R:1px dashed #e4e5e1 / B:1px dashed #e4e5e1 / L:1px dashed #e4e5e1 r 50%; div._inner_16ia3_16 46.0x46.0 bg #ffffff border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 50% shadow #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px 20px 25px -5px, #181916 @ 0.1 0px 8px 10px -6px, #000000 @ 0.12 0px 2px 3px 0px | button._root_16ia3_3 56.0x56.0 border T:1px dashed #e4e5e1 / R:1px dashed #e4e5e1 / B:1px dashed #e4e5e1 / L:1px dashed #e4e5e1 r 50%; div._inner_16ia3_16 46.0x46.0 bg #f0f0ed border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 50% shadow #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px 20px 25px -5px, #181916 @ 0.1 0px 8px 10px -6px, #000000 @ 0.12 0px 2px 3px 0px | button._root_16ia3_3 56.0x56.0 border T:1px dashed #e4e5e1 / R:1px dashed #e4e5e1 / B:1px dashed #e4e5e1 / L:1px dashed #e4e5e1 r 50% outline 2px solid #f35b22 offset 0px; div._inner_16ia3_16 46.0x46.0 bg #ffffff border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 50% shadow #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px 20px 25px -5px, #181916 @ 0.1 0px 8px 10px -6px, #000000 @ 0.12 0px 2px 3px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `chat-btn-default.png`, `chat-btn-hover.png`, `chat-btn-focus-visible.png`, `chat-btn-pressed.png`.

### Home

#### hero-h1

Hero headline. "Identify Every Visitor" — the fp-hero-block masthead.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 828.67 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 48px/56px 500 |
| Letter spacing | -3px |
| Colour | #000000 |
| Text node | span.fp-hero-word.fp-hero-first-word: Inter-c0aaf1024c6c51d7 48px/56px 500, #000000, ls -3px |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### prompt-expander

Install prompt expander. The "Prompt" expander in the hero that reveals the get-started prompt text and the AI-tool install links; opened by its own toggle.

Page: home. Selector: `hero Prompt expander`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 113.5 x 26 | = | = | = | = |
| Padding | 0px 8px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = | = |
| Radius | 4px 2px 2px 4px | = | = | = | = |
| Background | transparent | #f1f1ee | = | = | #e4e5e1 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #f35820 offset 2px | = | = |
| Font | Inter-c0aaf1024c6c51d7 14px/20px 500 | = | = | = | = |
| Letter spacing | -0.084px | = | = | = | = |
| Colour | #484946 | = | = | = | = |
| Text node | span.flex.flex-1: Inter-c0aaf1024c6c51d7 14px/20px 500, #484946, ls -0.084px | = | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #484946 | = | = | = | = |
| Painted layers | button.outline-primary.invalid:outline-red-500 113.5x26.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px 2px 2px 4px | button.outline-primary.invalid:outline-red-500 113.5x26.0 bg #f1f1ee border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px 2px 2px 4px | button.outline-primary.invalid:outline-red-500 113.5x26.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px 2px 2px 4px outline 2px solid #f35820 offset 2px | = | button.outline-primary.invalid:outline-red-500 113.5x26.0 bg #e4e5e1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px 2px 2px 4px |
| Ancestor paint | 2 up div.inline-flex.max-w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #171816 @ 0.03 0px 1px 2px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `prompt-expander-default.png`, `prompt-expander-hover.png`, `prompt-expander-focus-visible.png`, `prompt-expander-pressed.png`, `prompt-expander-opened.png`.

#### install-btn

Install button. The "Install Fingerprint with AI" hero button — a local UI toggle that reveals install options; measured, never toggled.

Page: home. Selector: `hero Install Fingerprint with AI`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 256.08 x 26 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 2px 4px 4px 2px | = | = | = |
| Background | transparent | #f1f1ee | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f35820 offset 2px | = |
| Font | Inter-c0aaf1024c6c51d7 14px/20px 500 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #171816 | = | = | = |
| Text node | span.truncate.font-mono: JetBrains Mono-c3e9177549e38394 14px/20px 500, #171816, ls -0.084px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #484946 | = | = | = |
| Painted layers | button.outline-primary.invalid:outline-red-500 256.1x26.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px 4px 4px 2px | button.outline-primary.invalid:outline-red-500 256.1x26.0 bg #f1f1ee border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px 4px 4px 2px | button.outline-primary.invalid:outline-red-500 256.1x26.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px 4px 4px 2px outline 2px solid #f35820 offset 2px | = |
| Ancestor paint | 1 up div.inline-flex.max-w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #171816 @ 0.03 0px 1px 2px 0px | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `install-btn-default.png`, `install-btn-hover.png`, `install-btn-focus-visible.png`, `install-btn-pressed.png`.

#### section-h2

Section heading. A marketing section heading further down the home page ("Not all bots are bad Not all humans are good") — a display-size h2, so transient microcopy such as a widget's error heading never counts.

Page: home. Selector: `h2 (display size)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 559 x 120 |
| Padding | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 36px/44px 500 |
| Letter spacing | -0.73px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### hero-pill

News pill. The "New — We now detect Claude Duet" announcement pill above the headline; links to a blog post, measured never followed.

Page: home. Selector: `hero news pill`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 329.77 x 42 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.mr-1.shrink-0: Inter-c0aaf1024c6c51d7 12px/16px 500, #f35820 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 14 x 14, colour #000000 | = |
| Painted layers | span.inline-flex.items-center 329.8x42.0 image linear-gradient(90deg, #f8f7fe @ 0.2 0%, #ffffff @ 0.2 100%) border T:1px dashed #e4e5e1 / R:1px dashed #e4e5e1 / B:1px dashed #e4e5e1 / L:1px dashed #e4e5e1 r 26px; span.mr-1.shrink-0 42.0x30.0 bg #f35820 @ 0.1 r 31px | span.inline-flex.items-center 329.8x42.0 image linear-gradient(90deg, #f8f7fe @ 0.35 0%, #ffffff @ 0.35 100%) border T:1px dashed #c1c1be / R:1px dashed #c1c1be / B:1px dashed #c1c1be / L:1px dashed #c1c1be r 26px; span.mr-1.shrink-0 42.0x30.0 bg #f35820 @ 0.1 r 31px |
| How | at rest | mouse hover |

Crops: `hero-pill-default.png`, `hero-pill-hover.png`.

### Footer

#### footer

Footer. The page footer: the newsletter subscribe field, the Product/Use Cases/Resources/Developers columns, social icons and company links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 516 |
| Padding | 0px |
| Border | T: 1px solid #e8e8e8; R: none; B: none; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.pb-3.text-[14px]: Inter-c0aaf1024c6c51d7 14px/21px 400, #6e6f6c |
| Transition | none |
| Icon | 14 x 14, colour #a0a09d |
| Painted layers | footer.border-t.border-[#e8e8e8] 1440.0x516.0 bg #ffffff border T:1px solid #e8e8e8; form.flex.h-[45px] 281.0x45.0 bg #fafaf8 border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px -1px 0px 0px inset; span.inline-flex.items-center 74.0x20.0 bg #ffffff image linear-gradient(301deg, #f35b22 @ 0.01 9.55%, #f35b22 @ 0.1 67.28%) border T:1px solid #ffcab5 / R:1px solid #ffcab5 / B:1px solid #ffcab5 / L:1px solid #ffcab5 r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #be400f @ 0.1 0px -1px 0px 0px inset, #ffffff @ 0.1 0px 1.5px 0px 0px inset, #000000 @ 0.03 0px 0.5px 0px 0px; div.flex.flex-col 1248.0x77.0 bg #fafaf8 border T:1px dashed #f0f0ed / R:1px dashed #f0f0ed / B:1px dashed #f0f0ed / L:1px dashed #f0f0ed r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px; a.border-l.pl-3 105.0x19.6 border L:1px solid #e8e8e8; a.border-l.pl-3 153.0x19.6 border L:1px solid #e8e8e8 |
| Ancestor paint | 1 up body.bg-gray-100.hide-hubspot-chat bg #f8f8f6 |
| How | at rest |

Crops: `footer-default.png`.

#### newsletter-field

Newsletter field. The "Email address*" subscribe input in the footer; focused and typed into then cleared — never subscribed.

Page: home. Selector: `footer input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 211 x 21 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter-c0aaf1024c6c51d7 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #6e6f6c | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #181916 @ 0.5, opacity 1 | = | = |
| Ancestor paint | 1 up form.flex.h-[45px] bg #fafaf8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px -1px 0px 0px inset | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`, `newsletter-field-filled.png`.

#### subscribe-btn

Subscribe button. The newsletter subscribe button; its states were measured but the button was never clicked — nothing was submitted.

Page: home. Selector: `footer Subscribe to newsletter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter-c0aaf1024c6c51d7 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a0a09d | = | #f35b22 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 14 x 14, colour #a0a09d | = | 14 x 14, colour #f35b22 | = |
| Ancestor paint | 1 up form.flex.h-[45px] bg #fafaf8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px -1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.min-h-[44px] 44.0x44.0 outline 1px auto #101010 offset 0px | = |

Crops: `subscribe-btn-default.png`, `subscribe-btn-hover.png`, `subscribe-btn-focus-visible.png`, `subscribe-btn-pressed.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a Smart Signals`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 168 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f35820 offset 2px | = |
| Font | Inter-c0aaf1024c6c51d7 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6f6c | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |
| Painted layers | - | = | a.inline-flex.items-center 168.0x21.0 outline 2px solid #f35820 offset 2px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Product pages

#### prod-h1

Product headline. "Device identification_" — the /products/identification masthead.

Page: identification. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 175.16 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | JetBrains Mono-c3e9177549e38394 13px/20px 500 |
| Letter spacing | -0.039px |
| Colour | #6b6c6a |
| Transition | none |
| How | at rest |

Crops: `prod-h1-default.png`.

#### prod-select

Demo select. The native <select> in the page's interactive identification demo (a region/device picker); measured at rest, never changed.

Page: identification. Selector: `select`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 76 x 22 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 1px auto #101010 offset 0px |
| Font | Inter-c0aaf1024c6c51d7 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | default | = |
| How | at rest | clicked into the field |
| Painted layers | - | select 76.0x22.0 outline 1px auto #101010 offset 0px |

Crops: `prod-select-default.png`, `prod-select-focused.png`.

#### prod-cta

Product CTA. A "Get started" call-to-action on the product page; measured, never followed.

Page: identification. Selector: `product page CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109 x 32 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #f35b22 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #fefefd | #fff3ef | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter-c0aaf1024c6c51d7 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f35b22 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.select-none 109.0x32.0 bg #fefefd border T:1px solid #f35b22 / R:1px solid #f35b22 / B:1px solid #f35b22 / L:1px solid #f35b22 r 6px | a.relative.select-none 109.0x32.0 bg #fff3ef border T:1px solid #f35b22 / R:1px solid #f35b22 / B:1px solid #f35b22 / L:1px solid #f35b22 r 6px | a.relative.select-none 109.0x32.0 bg #fefefd border T:1px solid #f35b22 / R:1px solid #f35b22 / B:1px solid #f35b22 / L:1px solid #f35b22 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `prod-cta-default.png`, `prod-cta-hover.png`, `prod-cta-focus-visible.png`, `prod-cta-pressed.png`.

### Pricing

#### price-h1

Pricing headline. "Choose your plan" — the /pricing masthead.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 50px/52px 500 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-slider

Identification-volume slider. The "billing-slider" range input that re-prices the plans (20K/100K/200K/500K/1M+ identifications); measured at rest, never dragged.

Page: pricing. Selector: `input[type=range] billing-slider`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 444 x 10 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | default | = |
| Placeholder | #000000, opacity 1 | = |
| Ancestor paint | 1 up div.relative.flex bg #e4e5e1 | = |
| How | at rest | clicked into the field |

Crops: `price-slider-default.png`, `price-slider-focused.png`.

#### price-tick

Slider tick. A volume tick under the slider (100K identifications); a local UI control that re-prices the grid — measured, never pressed.

Page: pricing. Selector: `slider 100K tick`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.8 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | JetBrains Mono-c3e9177549e38394 14px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6f6c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.mt-10.flex-1 88.8x22.0 outline 1px auto #101010 offset 0px | = |

Crops: `price-tick-default.png`, `price-tick-hover.png`, `price-tick-focus-visible.png`, `price-tick-pressed.png`.

#### plan-card

Plan card. A plan card on /pricing — one bordered column of the three-card grid (Free/Pro/Enterprise): name, price, identification allowance and its CTA.

Page: pricing. Selector: `plan card (.rounded-2xl with h3)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 329.44 x 461.25 |
| Padding | 24px |
| Border | 1px solid #e4e5e1 |
| Radius | 16px |
| Background | #f8f8f6 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset, #181916 @ 0.04 0px 1px 3px 0px, #181916 @ 0.08 0px 1px 2px -1px |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.m-0.font-sans: Inter-c0aaf1024c6c51d7 20px/32px 500, #000000, ls -0.38px |
| Transition | none |
| Icon | 12 x 10, colour #f35b22 |
| Painted layers | div.m-2.flex-1 329.4x461.3 bg #f8f8f6 border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset, #181916 @ 0.04 0px 1px 3px 0px, #181916 @ 0.08 0px 1px 2px -1px; span.flex.items-center 34.0x19.0 border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 1px 0px 0px inset, #484946 @ 0.1 0px -1px 0px 0px inset; a.inline-flex.box-border 87.0x32.0 bg #f8f8f6 border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.02 0px 2px 1px 0px, #181916 @ 0.1 0px -1px 0px 0px inset; span.ml-2.inline-block 40.7x22.0 bg #ffffff image linear-gradient(301deg, #f35b22 @ 0.01 9.55%, #f35b22 @ 0.1 67.28%) border T:1px solid #ffcab5 / R:1px solid #ffcab5 / B:1px solid #ffcab5 / L:1px solid #ffcab5 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #be400f @ 0.1 0px -1.5px 0px 0px inset, #ffffff @ 0.1 0px 1.5px 0px 0px inset, #000000 @ 0.03 0px 0.5px 0px 0px |
| Ancestor paint | 1 up div.flex.bg-[#fcfcfb] bg #fcfcfb |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA. A plan card's primary action ("Start Free" on the Free/Pro cards, "Contact Sales" on Enterprise); measured, never followed.

Page: pricing. Selector: `plan card CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87 x 32 | = | = | = |
| Padding | 7.21px 14px | = | = | = |
| Border | 1px solid #dadad7 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f8f8f6 | #f1f1ee | = | #e4e5e1 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.02 0px 2px 1px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.4 0px 1px 0px 0px inset, #181916 @ 0.02 0px 2px 1px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.4 0px 1px 0px 0px inset, #181916 @ 0.02 0px 2px 1px 0px, #181916 @ 0.1 0px -1px 0px 0px inset |
| Outline | none | = | 2px solid #f35820 offset 2px | = |
| Font | Inter-c0aaf1024c6c51d7 12px/15.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171816 | = | = | = |
| Text node | span: Inter-c0aaf1024c6c51d7 12px/15.6px 500, #171816 | = | = | = |
| Transition | background-color, border-color, box-shadow, color, opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.box-border 87.0x32.0 bg #f8f8f6 border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.02 0px 2px 1px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | a.inline-flex.box-border 87.0x32.0 bg #f1f1ee border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.4 0px 1px 0px 0px inset, #181916 @ 0.02 0px 2px 1px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | a.inline-flex.box-border 87.0x32.0 bg #f8f8f6 border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.02 0px 2px 1px 0px, #181916 @ 0.1 0px -1px 0px 0px inset outline 2px solid #f35820 offset 2px | a.inline-flex.box-border 87.0x32.0 bg #e4e5e1 border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.4 0px 1px 0px 0px inset, #181916 @ 0.02 0px 2px 1px 0px, #181916 @ 0.1 0px -1px 0px 0px inset |
| Ancestor paint | 1 up div.m-2.flex-1 bg #f8f8f6 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset, #181916 @ 0.04 0px 1px 3px 0px, #181916 @ 0.08 0px 1px 2px -1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### compare-btn

Compare features control. The "Compare all features" control that opens the feature-comparison grid; a local UI toggle — measured at rest, never toggled.

Page: pricing. Selector: `Compare all features`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1038.33 x 62 | = | = | = |
| Padding | 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | T: none; R: 1px dashed #e4e5e1; B: none; L: 1px dashed #e4e5e1 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h5.m-0.cursor-pointer: Inter-c0aaf1024c6c51d7 14px/14px 400, #f35b22 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #f35b22 | = | = | = |
| Painted layers | button.col-[2/12].flex 1038.3x62.0 border R:1px dashed #e4e5e1 / L:1px dashed #e4e5e1 | = | button.col-[2/12].flex 1038.3x62.0 border R:1px dashed #e4e5e1 / L:1px dashed #e4e5e1 outline 1px auto #101010 offset 0px | = |
| Ancestor paint | 3 up section.border-b.border-dashed bg #fafaf8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `compare-btn-default.png`, `compare-btn-hover.png`, `compare-btn-focus-visible.png`, `compare-btn-pressed.png`.

#### feature-acc

Feature-group accordion. A feature-group accordion in the comparison table ("Identification Features", "Smart Signals", "Support", ...); the opened state was measured after its own toggle click — a local UI toggle.

Page: pricing. Selector: `feature accordion`. States: default, opened, hover.

| Property | default | opened | hover |
|---|---|---|---|
| Size (w x h) | 1036.33 x 73 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | h3.m-0.font-sans: Inter-c0aaf1024c6c51d7 18px/28px 500, #181916 | = | = |
| Transition | none | = | = |
| Icon | 16 x 30, colour #f35b22 | = | = |
| Painted layers | button.relative.flex 414.5x73.0 bg #fcfcfb border R:1px dashed #e4e5e1 / B:1px dashed #e4e5e1; button::before.relative.flex 1.5pxx72px bg #f35b22; div.h-full.border-b 207.3x73.0 border R:1px dashed #e4e5e1 / B:1px dashed #e4e5e1; div.h-full.w-full 190.3x72.0 bg #f7f7f5 border R:1px solid #e4e5e1 / L:1px solid #e4e5e1; div.h-full.border-b 207.3x73.0 border R:1px dashed #e4e5e1 / B:1px dashed #e4e5e1; div.h-full.w-full 190.3x72.0 bg #ffffff border R:1px solid #e4e5e1 / L:1px solid #e4e5e1 | = | = |
| How | at rest | own toggle | mouse hover |

Crops: `feature-acc-default.png`, `feature-acc-opened.png`, `feature-acc-hover.png`.

#### faq-acc

FAQ accordion. A question row in the pricing FAQ ("How does billing for Fingerprint work?", "Do you offer annual billing...", ...); the opened state was measured after its own toggle — a local UI toggle.

Page: pricing. Selector: `pricing FAQ row`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 508.17 x 54.41 | = |
| Padding | 16px 24px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h5.m-0.font-sans: Inter-c0aaf1024c6c51d7 16px/22.4px 500, #484946 | h5.m-0.font-sans: Inter-c0aaf1024c6c51d7 16px/22.4px 500, #f35b22 |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 17 x 16, colour #484946 | 16 x 17, colour #f35b22 |
| How | at rest | own toggle |

Crops: `faq-acc-default.png`, `faq-acc-opened.png`.

### Demo surface

#### demo-h1

Demo headline. "See Fingerprint in Action" — the /demo masthead over the live device-intelligence demo.

Page: demo. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 565.83 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 48px/56px 500 |
| Letter spacing | -1.92px |
| Colour | #181916 |
| Text node | span.inline-block.animate-[demo-heroTranslateUp_300ms_forwards]: Inter-c0aaf1024c6c51d7 48px/56px 500, #181916, ls -1.92px |
| Transition | none |
| How | at rest |

Crops: `demo-h1-default.png`.

#### demo-analyze

Re-analyze button. The "Analyze my browser again" control — it re-runs the public demo on the visitor's own browser; measured, never pressed.

Page: demo. Selector: `Analyze my browser again`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146 x 23 | 164 x 23 | 164 x 23 | 164 x 23 |
| Padding | 4px 8px | = | = | = |
| Border | 1px solid #e4e5e1 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #f8f8f6 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter-c0aaf1024c6c51d7 10px/13px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #181916 | = | = | = |
| Text node | span.inline-block: Inter-c0aaf1024c6c51d7 10px/13px 500, #181916 | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 12, colour #181916 | 16.97 x 16.97, colour #181916 | 14.09 x 14.09, colour #181916 | 15.23 x 15.23, colour #181916 |
| Painted layers | button.mr-2.cursor-pointer 146.0x23.0 bg #f8f8f6 border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset | button.mr-2.cursor-pointer 164.0x23.0 bg #f8f8f6 border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset | button.mr-2.cursor-pointer 164.0x23.0 bg #f8f8f6 border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset outline 1px auto #101010 offset 0px | button.mr-2.cursor-pointer 164.0x23.0 bg #f8f8f6 border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset |
| Ancestor paint | 1 up div.flex.w-full bg #ffffff @ 0.92; 3 up div.relative.overflow-hidden bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.1 0px 4px 6px -1px, #181916 @ 0.1 0px 2px 4px -2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-analyze-default.png`, `demo-analyze-hover.png`, `demo-analyze-focus-visible.png`, `demo-analyze-pressed.png`.

#### demo-field

Demo checkout field. A mock card-number input inside the demo's fake checkout; typed into then cleared — the demo form was never placed.

Page: demo. Selector: `demo card input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 262 x 40 | = | = |
| Padding | 7.5px 50px | = | = |
| Border | 1px solid #e4e5e1 | = | = |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | JetBrains Mono-c3e9177549e38394 14px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #484946 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #484946 @ 0.5, opacity 1 | = | = |
| Painted layers | input.mt-3.h-10 262.0x40.0 bg #ffffff border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 4px | = | = |
| Ancestor paint | 2 up div.flex.size-full bg #fef7f9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset | = | = |
| How | at rest | clicked into the field | typed "4242 4242 4242 4242", then deleted; nothing sent |

Crops: `demo-field-default.png`, `demo-field-focused.png`, `demo-field-filled.png`.

#### demo-order

Demo order button. The fake checkout's "Place Order" button inside the demo pane; measured, never pressed.

Page: demo. Selector: `demo Place Order`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 262 x 38 | = | = | = |
| Padding | 12px 15.045px | = | = | = |
| Gap | 7.522px | = | = | = |
| Border | 1px solid #f1739d | = | = | = |
| Radius | 4px | = | = | = |
| Background | #c2336c | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.2 0px -1px 0px 0px inset, #ffffff @ 0.6 0px 1px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter-c0aaf1024c6c51d7 12px/12px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border, opacity, color 0.25s, 0.25s, 0.25s, 0.25s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.box-border.inline-flex 262.0x38.0 bg #c2336c border T:1px solid #f1739d / R:1px solid #f1739d / B:1px solid #f1739d / L:1px solid #f1739d r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.2 0px -1px 0px 0px inset, #ffffff @ 0.6 0px 1px 0px 0px inset | = | button.box-border.inline-flex 262.0x38.0 bg #c2336c border T:1px solid #f1739d / R:1px solid #f1739d / B:1px solid #f1739d / L:1px solid #f1739d r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.2 0px -1px 0px 0px inset, #ffffff @ 0.6 0px 1px 0px 0px inset outline 1px auto #101010 offset 0px | = |
| Ancestor paint | 2 up div.flex.size-full bg #fef7f9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `demo-order-default.png`, `demo-order-hover.png`, `demo-order-focus-visible.png`, `demo-order-pressed.png`.

#### demo-login

Demo login button. The fake sign-in "Log In" inside the demo pane; measured, never pressed.

Page: demo. Selector: `demo Log In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 262 x 38 | = | = | = |
| Padding | 12px 15.045px | = | = | = |
| Gap | 7.522px | = | = | = |
| Border | 1px solid #52a5e1 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #0174b3 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.2 0px -1px 0px 0px inset, #ffffff @ 0.6 0px 1px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter-c0aaf1024c6c51d7 12px/12px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border, opacity, color 0.25s, 0.25s, 0.25s, 0.25s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.box-border.inline-flex 262.0x38.0 bg #0174b3 border T:1px solid #52a5e1 / R:1px solid #52a5e1 / B:1px solid #52a5e1 / L:1px solid #52a5e1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.2 0px -1px 0px 0px inset, #ffffff @ 0.6 0px 1px 0px 0px inset | = | button.box-border.inline-flex 262.0x38.0 bg #0174b3 border T:1px solid #52a5e1 / R:1px solid #52a5e1 / B:1px solid #52a5e1 / L:1px solid #52a5e1 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.2 0px -1px 0px 0px inset, #ffffff @ 0.6 0px 1px 0px 0px inset outline 1px auto #101010 offset 0px | = |
| Ancestor paint | 2 up div.flex.size-full bg #f3f9fe shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `demo-login-default.png`, `demo-login-hover.png`, `demo-login-focus-visible.png`, `demo-login-pressed.png`.

#### demo-signal

Signal reveal button. A "See <signal> in the signals below" control that scrolls the signal panel to a row — a local UI toggle; measured, never pressed. The signal values it points at can name this machine's IP and rough location, so the panel's crops are masked before commit.

Page: demo. Selector: `demo signal reveal`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 14 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter-c0aaf1024c6c51d7 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a0a09d | #484946 | = | #484946 |
| Transition | opacity 0.2s ease | = | = | = |
| Opacity | 0 | - | - | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #a0a09d | 14 x 14, colour #484946 | = | 14 x 14, colour #484946 |
| Ancestor paint | 2 up div.group/card.relative bg #fafaf8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset, #181916 @ 0.02 0px 2px 1px 0px | 2 up div.group/card.relative bg #fafaf8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 1px 0px 0px inset, #181916 @ 0.05 0px 2px 4px 2px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.size-[14px] 14.0x14.0 outline 1px auto #101010 offset 0px | = |

Crops: `demo-signal-default.png`, `demo-signal-hover.png`, `demo-signal-focus-visible.png`, `demo-signal-pressed.png`.

#### demo-tab

Signal-group tab. The "01 IDENTIFICATION SIGNALS" tab in the demo (02 BROWSER SMART SIGNALS, 03 MOBILE SMART SIGNALS are its siblings); opened by its own toggle — a local UI tab.

Page: demo. Selector: `demo signal tab`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 199.09 x 37 | = | = | = | = |
| Padding | 8px 16px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | T: none; R: 1px solid #e4e5e1; B: 1px solid #ffffff; L: none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #f35b22 offset 2px | = | = |
| Font | JetBrains Mono-c3e9177549e38394 11px/20px 300 | = | = | = | = |
| Letter spacing | -0.33px | = | = | = | = |
| Colour | #331105 | = | = | = | = |
| Text node | span.opacity-60.max-[641px]:font-mono: JetBrains Mono-c3e9177549e38394 11px/20px 300, #f35b22, ls -0.33px | = | = | = | = |
| Transition | color 0.2s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| ::after | 198.094px x 2px, absolute, bg #000000 @ 0 linear-gradient(90deg, #f35b22 0%, #f35b22 @ 0.05 100%), radius 0px | = | = | = | = |
| Painted layers | button.relative.inline-flex 199.1x37.0 border R:1px solid #e4e5e1 / B:1px solid #ffffff; button::after.relative.inline-flex 198.094pxx2px image linear-gradient(90deg, #f35b22 0%, #f35b22 @ 0.05 100%) | = | button.relative.inline-flex 199.1x37.0 border R:1px solid #e4e5e1 / B:1px solid #ffffff outline 2px solid #f35b22 offset 2px; button::after.relative.inline-flex 198.094pxx2px image linear-gradient(90deg, #f35b22 0%, #f35b22 @ 0.05 100%) | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `demo-tab-default.png`, `demo-tab-hover.png`, `demo-tab-focus-visible.png`, `demo-tab-pressed.png`, `demo-tab-opened.png`.

### Contact sales form

#### contact-h1

Contact headline. "Talk to Our Sales Team" — the /contact-sales masthead over the form.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 597 x 45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 36px/45px 500 |
| Letter spacing | -0.456px |
| Colour | #181916 |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### contact-email

Email field. The e-mail input on the sales form; focused and typed into then cleared — never submitted.

Page: contact. Selector: `contact-sales input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 413 x 40.39 | = | = |
| Padding | 9px 12px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e8e8e8 0px 0px 0px 1px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f35b22 0px 0px 0px 1px, #f35b22 @ 0.2 0px 0px 0px 6px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f35b22 0px 0px 0px 1px, #f35b22 @ 0.2 0px 0px 0px 6px |
| Outline | none | = | = |
| Font | Inter-c0aaf1024c6c51d7 14px/22.4px 400 | = | = |
| Letter spacing | 0.14px | = | = |
| Colour | #181916 | = | = |
| Transition | box-shadow 0.1s cubic-bezier(0.36, 0.19, 0.29, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #a0a09d, opacity 1 | = | = |
| Painted layers | input.w-full.appearance-none 413.0x40.4 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e8e8e8 0px 0px 0px 1px | input.w-full.appearance-none 413.0x40.4 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f35b22 0px 0px 0px 1px, #f35b22 @ 0.2 0px 0px 0px 6px | input.w-full.appearance-none 413.0x40.4 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f35b22 0px 0px 0px 1px, #f35b22 @ 0.2 0px 0px 0px 6px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `contact-email-default.png`, `contact-email-focused.png`, `contact-email-filled.png`.

#### contact-submit

Submit button. The sales form's "Submit" button; its states were measured but the button was never clicked — the form was never sent.

Page: contact. Selector: `contact-sales Submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 413 x 37.59 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #be400f | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f35b22 | #be400f | = | #be400f |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | = | = | = |
| Outline | none | = | 2px solid #f35b22 offset 2px | = |
| Font | Inter-c0aaf1024c6c51d7 14px/19.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, opacity, color 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.w-full 413.0x37.6 bg #f35b22 border T:1px solid #be400f / R:1px solid #be400f / B:1px solid #be400f / L:1px solid #be400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | button.inline-flex.w-full 413.0x37.6 bg #be400f border T:1px solid #be400f / R:1px solid #be400f / B:1px solid #be400f / L:1px solid #be400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | button.inline-flex.w-full 413.0x37.6 bg #f35b22 border T:1px solid #be400f / R:1px solid #be400f / B:1px solid #be400f / L:1px solid #be400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset outline 2px solid #f35b22 offset 2px | button.inline-flex.w-full 413.0x37.6 bg #be400f border T:1px solid #be400f / R:1px solid #be400f / B:1px solid #be400f / L:1px solid #be400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `contact-submit-default.png`, `contact-submit-hover.png`, `contact-submit-focus-visible.png`, `contact-submit-pressed.png`.

### Blog and resource indexes

#### blog-h1

Blog headline. "Fingerprint Blog" — the /blog index masthead.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1248 x 37.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | JetBrains Mono 32px/37.44px 700 |
| Letter spacing | normal |
| Colour | #141415 |
| Transition | none |
| How | at rest |

Crops: `blog-h1-default.png`.

#### blog-card

Article card. An article card in the blog index; measured, never followed.

Page: blog. Selector: `blog article card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 290.66 x 206.31 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #141415 | = |
| Text node | span.Post-module--publishDate--9686f: Inter 14px/21px 400, #141415 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Ancestor paint | - | 2 up div.Post-module--post--3a994 bg #ffffff shadow #0d102b @ 0.1 0px 8px 32px 0px |

Crops: `blog-card-default.png`, `blog-card-hover.png`.

#### blog-subscribe

Blog subscribe field. The newsletter e-mail input on the blog index; focused and typed into then cleared — never subscribed.

Page: blog. Selector: `blog input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 370 x 57 | = | = |
| Padding | 16px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #c4cdd5 0px 0px 0px 1px | #ff5e24 0px 0px 0px 2px | #ff5e24 0px 0px 0px 2px |
| Outline | none | = | = |
| Font | Inter 16px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #5b5b5b, opacity 1 | = | = |
| Painted layers | input.SubscribeNewsletterForm-module--input--e0a56 370.0x57.0 bg #ffffff r 6px shadow #c4cdd5 0px 0px 0px 1px | input.SubscribeNewsletterForm-module--input--e0a56 370.0x57.0 bg #ffffff r 6px shadow #ff5e24 0px 0px 0px 2px | input.SubscribeNewsletterForm-module--input--e0a56 370.0x57.0 bg #ffffff r 6px shadow #ff5e24 0px 0px 0px 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `blog-subscribe-default.png`, `blog-subscribe-focused.png`, `blog-subscribe-filled.png`.

#### blog-subscribe-btn

Blog subscribe button. The blog subscribe button; measured, never pressed.

Page: blog. Selector: `blog Subscribe`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109 x 57 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Border | 1px solid #be400f | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f35b22 | #be400f | = | #be400f |
| Box shadow | #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | = | = | = |
| Outline | none | = | 2px solid #f35b22 offset 2px | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter 14px/19.6px 500, #ffffff | = | = | = |
| Transition | background-color, border, opacity, color 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button-module--button--3b10c.Button-module--primary--379ca 109.0x57.0 bg #f35b22 border T:1px solid #be400f / R:1px solid #be400f / B:1px solid #be400f / L:1px solid #be400f r 6px shadow #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | button.Button-module--button--3b10c.Button-module--primary--379ca 109.0x57.0 bg #be400f border T:1px solid #be400f / R:1px solid #be400f / B:1px solid #be400f / L:1px solid #be400f r 6px shadow #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | button.Button-module--button--3b10c.Button-module--primary--379ca 109.0x57.0 bg #f35b22 border T:1px solid #be400f / R:1px solid #be400f / B:1px solid #be400f / L:1px solid #be400f r 6px shadow #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset outline 2px solid #f35b22 offset 2px | button.Button-module--button--3b10c.Button-module--primary--379ca 109.0x57.0 bg #be400f border T:1px solid #be400f / R:1px solid #be400f / B:1px solid #be400f / L:1px solid #be400f r 6px shadow #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `blog-subscribe-btn-default.png`, `blog-subscribe-btn-hover.png`, `blog-subscribe-btn-focus-visible.png`, `blog-subscribe-btn-pressed.png`.

#### careers-h1

Careers headline. The /careers masthead.

Page: careers. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1248 x 64 |
| Padding | 0px 0px 8px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 48px/56px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `careers-h1-default.png`.

#### res-h1

Resources headline. The /resources resource-center masthead.

Page: resources. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 744 x 67.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 56px/67.2px 600 |
| Letter spacing | normal |
| Colour | #141415 |
| Transition | none |
| How | at rest |

Crops: `res-h1-default.png`.

#### res-card

Resource card. A resource card on the /resources index — an anchor holding a thumbnail and a kicker label (ARTICLE/TUTORIAL/..., painted by text-transform); measured, never followed.

Page: resources. Selector: `resources card link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 296 x 390.97 | = |
| Padding | 0px | = |
| Gap | 24px | = |
| Border | 1px solid #e8e8e8 | 1px solid #000000 @ 0 |
| Radius | 6px | = |
| Background | #ffffff | = |
| Box shadow | #d1d1d1 @ 0.15 0px 2px 4px 0px | #141415 @ 0.02 0px 100px 80px 0px, #141415 @ 0.02 0px 42px 33px 0px, #141415 @ 0.03 0px 22px 18px 0px, #141415 @ 0.03 0px 12px 10px 0px, #141415 @ 0.04 0px 7px 6px 0px, #737373 @ 0.15 0px 0px 1px 0px, #141415 @ 0.02 0px 3px 2px 0px |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #141415 | = |
| Text node | span.RelatedResourcesSection-module--orangeLabel--64ee2: JetBrains Mono 11px/16px 400, #f5614b | = |
| Transition | box-shadow, border 0.25s ease | = |
| Cursor | pointer | = |
| Painted layers | a.RelatedResourcesSection-module--card--2d030 296.0x391.0 bg #ffffff border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 6px shadow #d1d1d1 @ 0.15 0px 2px 4px 0px; div 294.0x172.8 bg #381808; span.RelatedResourcesSection-module--orangeLabel--64ee2 65.0x24.0 image linear-gradient(94deg, #f5614b @ 0.2, #f5614b @ 0.2 0.01%, #fa7545 @ 0.2) r 4px | a.RelatedResourcesSection-module--card--2d030 296.0x391.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px shadow #141415 @ 0.02 0px 100px 80px 0px, #141415 @ 0.02 0px 42px 33px 0px, #141415 @ 0.03 0px 22px 18px 0px, #141415 @ 0.03 0px 12px 10px 0px, #141415 @ 0.04 0px 7px 6px 0px, #737373 @ 0.15 0px 0px 1px 0px, #141415 @ 0.02 0px 3px 2px 0px; div 294.0x172.8 bg #381808; span.RelatedResourcesSection-module--orangeLabel--64ee2 65.0x24.0 image linear-gradient(94deg, #f5614b @ 0.2, #f5614b @ 0.2 0.01%, #fa7545 @ 0.2) r 4px |
| How | at rest | mouse hover |

Crops: `res-card-default.png`, `res-card-hover.png`.

#### cs-h1

Case-studies headline. The /case-studies index masthead.

Page: case-studies. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1248 x 67.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 56px/67.2px 600 |
| Letter spacing | normal |
| Colour | #171816 |
| Transition | none |
| How | at rest |

Crops: `cs-h1-default.png`.

#### cs-card

Case-study card. A case-study card on the index; measured, never followed.

Page: case-studies. Selector: `case-studies card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 402.66 x 405.67 | = |
| Padding | 0px | = |
| Border | 1px solid #e8e8e8 | 1px solid #000000 @ 0 |
| Radius | 6px | = |
| Background | #ffffff | = |
| Box shadow | #d0d0d0 @ 0.15 0px 2px 4px 0px | #141415 @ 0.02 0px 100px 80px 0px, #141415 @ 0.02 0px 42px 33px 0px, #141415 @ 0.03 0px 22px 18px 0px, #141415 @ 0.03 0px 12px 10px 0px, #141415 @ 0.04 0px 7px 6px 0px, #727273 @ 0.15 0px 0px 1px 0px, #141415 @ 0.02 0px 3px 2px 0px |
| Outline | none | = |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h2.text-2xl/[1.4].font-semibold: Inter-c0aaf1024c6c51d7 20px/28px 600, #171816 | = |
| Transition | box-shadow, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = |
| Cursor | pointer | = |
| Painted layers | a.card.flex 402.7x405.7 bg #ffffff border T:1px solid #e8e8e8 / R:1px solid #e8e8e8 / B:1px solid #e8e8e8 / L:1px solid #e8e8e8 r 6px shadow #d0d0d0 @ 0.15 0px 2px 4px 0px | a.card.flex 402.7x405.7 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px shadow #141415 @ 0.02 0px 100px 80px 0px, #141415 @ 0.02 0px 42px 33px 0px, #141415 @ 0.03 0px 22px 18px 0px, #141415 @ 0.03 0px 12px 10px 0px, #141415 @ 0.04 0px 7px 6px 0px, #727273 @ 0.15 0px 0px 1px 0px, #141415 @ 0.02 0px 3px 2px 0px |
| How | at rest | mouse hover |

Crops: `cs-card-default.png`, `cs-card-hover.png`.

#### about-h1

About headline. "About us" — the /about-us masthead.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 244 x 67.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 56px/67.2px 600 |
| Letter spacing | normal |
| Colour | #141415 |
| Transition | none |
| How | at rest |

Crops: `about-h1-default.png`.

#### about-value

Value card heading. A "Our Values" card heading (No Nonsense., Fail. Learn. Grow., Be level 5 helpful.).

Page: about. Selector: `values card heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 20px/28px 500 |
| Letter spacing | normal |
| Colour | #141415 |
| Transition | none |
| How | at rest |

Crops: `about-value-default.png`.

#### careers-cta

Careers CTA. The "Explore Our Jobs" button on /careers — a local anchor to the jobs list; measured, never followed.

Page: careers. Selector: `careers Explore Our Jobs`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.66 x 32 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #bd400f | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f35820 | #bd400f | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | Inter-c0aaf1024c6c51d7 14px/20px 500 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.select-none 138.7x32.0 bg #f35820 border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | a.relative.select-none 138.7x32.0 bg #bd400f border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | a.relative.select-none 138.7x32.0 bg #f35820 border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| Ancestor paint | 2 up section.mt-5.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #a1a1a1 @ 0.15 0px 4px 15px 0px, #e8e8e8 @ 0.35 0px 0px 1px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `careers-cta-default.png`, `careers-cta-hover.png`, `careers-cta-focus-visible.png`, `careers-cta-pressed.png`.

### Docs site (Mintlify)

#### docs-h1

Doc page headline. "Quick Start Guide" — a docs article headline on the Mintlify stack.

Page: docs. Selector: `docs article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 294.7 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 500 |
| Letter spacing | -0.9px |
| Colour | #181916 |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-nav-tab

Docs nav tab. A docs top-nav tab (Home/Start/AI/Guides/API Reference/Changelogs); measured, never followed.

Page: docs-home. Selector: `docs nav tab`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 56.59 x 48 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 500 | = |
| Letter spacing | -0.084px | = |
| Colour | #8b8b89 | #484946 |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #8b8b89 | 16 x 16, colour #484946 |
| How | at rest | mouse hover |

Crops: `docs-nav-tab-default.png`, `docs-nav-tab-hover.png`.

#### docs-search

Search trigger. The docs' "Open search" button — a local UI toggle for the search overlay; measured, never opened.

Page: docs. Selector: `docs Open search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 437.33 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #f8f8f6 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d9d9d6 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 1px auto #f35b22 offset 0px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #a0a09d | = | = | = |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #a0a09d, ls -0.084px | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #6b6c69, fill #000000 | 16 x 16, colour #484946, fill #000000 | = | 16 x 16, colour #484946, fill #000000 |
| Painted layers | button.group/search.flex 437.3x36.0 bg #f8f8f6 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d9d9d6 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | button.group/search.flex 437.3x36.0 bg #f8f8f6 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d9d9d6 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #f35b22 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-theme-btn

Theme toggle. The docs' "Change theme preference" button — a local UI toggle that flips data-theme-preference between light and dark; measured at rest, never switched here (the dark surface is captured in the screenshots pass).

Page: docs. Selector: `docs Change theme preference`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #f35b22 offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #181916 @ 0.5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #6b6c69, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.group.disabled:pointer-events-none 32.0x32.0 r 8px outline 1px auto #f35b22 offset 0px | = |

Crops: `docs-theme-btn-default.png`, `docs-theme-btn-hover.png`, `docs-theme-btn-focus-visible.png`, `docs-theme-btn-pressed.png`.

#### docs-side-link

Sidebar link. A sidebar navigation link in the docs tree; measured, never followed.

Page: docs. Selector: `docs sidebar link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 256 x 36 | = |
| Padding | 6px 12px 6px 16px | = |
| Gap | normal 12px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | #f35b22 @ 0.1 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f35b22 | = |
| Text node | span.min-w-0.max-w-full: Inter 14px/24px 400, #f35b22 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #f35b22, fill #000000 | = |
| Painted layers | a.group.flex 256.0x36.0 bg #f35b22 @ 0.1 r 4px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #f35b22 | = |
| How | at rest | mouse hover |

Crops: `docs-side-link-default.png`, `docs-side-link-hover.png`.

#### docs-code

Code block. A code block on the docs article; the site's .dark syntax-highlight scope paints these.

Page: docs. Selector: `docs pre/code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656.81 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | paperMono 14px/24px 400 |
| Letter spacing | -0.084px |
| Colour | #adbac7 |
| Text node | span: paperMono 14px/24px 400, #f69d50, ls -0.084px |
| Transition | none |
| Painted layers | pre.shiki.shiki-themes 656.8x24.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; code 656.8x24.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.line 118.8x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 23.8x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span 95.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.font-mono.whitespace-pre shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #f8f8f6; 2 up div.min-w-full!.h-full shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #f8f8f6; 3 up div.size-full.rounded-[inherit] shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 0px solid #f8f8f6 |
| How | at rest |

Crops: `docs-code-default.png`.

### Login and signup (dashboard shell)

#### login-panel

Login panel. The dashboard-shell sign-in card on dashboard.fingerprint.com/login — the elevated MuiPaper card holding "Log In", the Google/GitHub/Microsoft SSO buttons and "Continue with email" — not the full-page main behind it.

Page: login. Selector: `login .MuiPaper-root card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 352 |
| Padding | 24px |
| Border | 1px solid #e4e5e1 |
| Radius | 4px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.08 0px 3px 15px 0px |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | -0.084px |
| Colour | #171816 |
| Text node | h1.text-gray-1000.font-medium: Inter 20px/28px 500, #171816, ls -0.34px |
| Transition | box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 17, colour #484946, fill #000000 |
| Painted layers | div.MuiPaper-root.MuiPaper-elevation 384.0x352.0 bg #ffffff border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 4px shadow #000000 @ 0.08 0px 3px 15px 0px; button.relative.select-none 334.0x36.0 bg #ffffff border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px; button.relative.select-none 334.0x36.0 bg #ffffff border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px; button.relative.select-none 334.0x36.0 bg #ffffff border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px; div::before.MuiDivider-root.MuiDivider-fullWidth 149.078pxx1px border T:1px solid #f2f2f2; div::after.MuiDivider-root.MuiDivider-fullWidth 149.078pxx1px border T:1px solid #f2f2f2 |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-google

Google SSO button. The "Continue with Google" button; measured, never pressed.

Page: login. Selector: `login Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 334 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #dadad7 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | #f1f1ee | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #171816 | = | = | = |
| Text node | span.opacity-100.transition-opacity: Inter 14px/20px 500, #171816, ls -0.084px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 17, colour #484946, fill #000000 | = | = | = |
| Painted layers | button.relative.select-none 334.0x36.0 bg #ffffff border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | button.relative.select-none 334.0x36.0 bg #f1f1ee border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | button.relative.select-none 334.0x36.0 bg #ffffff border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-github

GitHub SSO button. The "Continue with GitHub" button; measured, never pressed.

Page: login. Selector: `login Continue with GitHub`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 334 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #dadad7 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | #f1f1ee | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #171816 | = | = | = |
| Text node | span.opacity-100.transition-opacity: Inter 14px/20px 500, #171816, ls -0.084px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 17, colour #484946 | = | = | = |
| Painted layers | button.relative.select-none 334.0x36.0 bg #ffffff border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | button.relative.select-none 334.0x36.0 bg #f1f1ee border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | button.relative.select-none 334.0x36.0 bg #ffffff border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-github-default.png`, `login-github-hover.png`, `login-github-focus-visible.png`, `login-github-pressed.png`.

#### login-email-btn

Continue with email. The "Continue with email" control that reveals the e-mail form; measured, never pressed — the form was never opened or submitted.

Page: login. Selector: `login Continue with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 334 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #dadad7 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | #f1f1ee | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #171816 | = | = | = |
| Text node | span.opacity-100.transition-opacity: Inter 14px/20px 500, #171816, ls -0.084px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.select-none 334.0x36.0 bg #ffffff border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | button.relative.select-none 334.0x36.0 bg #f1f1ee border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | button.relative.select-none 334.0x36.0 bg #ffffff border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px | = |
| Ancestor paint | 3 up div.MuiPaper-root.MuiPaper-elevation bg #ffffff shadow #000000 @ 0.08 0px 3px 15px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-email-btn-default.png`, `login-email-btn-hover.png`, `login-email-btn-focus-visible.png`, `login-email-btn-pressed.png`.

#### login-signup-link

Sign up link. The "Sign up" link beside "New to Fingerprint?"; measured, never followed.

Page: login. Selector: `login Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 49.42 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #f35820 offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #f35820 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up div.MuiPaper-root.MuiPaper-elevation bg #ffffff shadow #000000 @ 0.08 0px 3px 15px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.MuiTypography-root.MuiTypography-inherit 49.4x17.0 outline 1px auto #f35820 offset 2px | = |

Crops: `login-signup-link-default.png`, `login-signup-link-hover.png`, `login-signup-link-focus-visible.png`, `login-signup-link-pressed.png`.

#### signup-panel

Signup panel. The dashboard-shell sign-up card on dashboard.fingerprint.com/signup — the elevated MuiPaper card holding "Sign up" and the SSO/email controls, not the full-page main behind it.

Page: signup. Selector: `signup .MuiPaper-root card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 302 |
| Padding | 24px |
| Border | 1px solid #e4e5e1 |
| Radius | 4px |
| Background | #ffffff |
| Box shadow | #171816 @ 0.03 0px 1px 2px 0px |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | -0.084px |
| Colour | #171816 |
| Text node | h1.text-gray-1000.font-medium: Inter 20px/28px 500, #171816, ls -0.34px |
| Transition | box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 17, colour #484946 |
| Painted layers | div.MuiPaper-root.MuiPaper-elevation 384.0x302.0 bg #ffffff border T:1px solid #e4e5e1 / R:1px solid #e4e5e1 / B:1px solid #e4e5e1 / L:1px solid #e4e5e1 r 4px shadow #171816 @ 0.03 0px 1px 2px 0px; button.relative.select-none 334.0x36.0 border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px; button.relative.select-none 334.0x36.0 border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px; hr._0kLbOq_separator 334.0x1.0 bg #f2f2f2; span 35.8x26.0 bg #ffffff; button.relative.select-none 334.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px |
| How | at rest |

Crops: `signup-panel-default.png`.

#### signup-google

Google SSO button (signup). The "Continue with Google" button on /signup; measured, never pressed.

Page: signup. Selector: `signup Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 334 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #dadad7 | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #f1f1ee | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #171816 | = | = | = |
| Text node | span.opacity-100.transition-opacity: Inter 14px/20px 500, #171816, ls -0.084px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 17, colour #484946 | = | = | = |
| Painted layers | button.relative.select-none 334.0x36.0 border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px | button.relative.select-none 334.0x36.0 bg #f1f1ee border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px | button.relative.select-none 334.0x36.0 border T:1px solid #dadad7 / R:1px solid #dadad7 / B:1px solid #dadad7 / L:1px solid #dadad7 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Ancestor paint | 3 up div.MuiPaper-root.MuiPaper-elevation bg #ffffff shadow #171816 @ 0.03 0px 1px 2px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-google-default.png`, `signup-google-hover.png`, `signup-google-focus-visible.png`, `signup-google-pressed.png`.

#### signup-email-btn

Continue with email (signup). The "Continue with email" control on /signup; measured, never pressed.

Page: signup. Selector: `signup Continue with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 334 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #f1f1ee | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.084px | = | = | = |
| Colour | #171816 | = | = | = |
| Text node | span.opacity-100.transition-opacity: Inter 14px/20px 500, #171816, ls -0.084px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.select-none 334.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px | button.relative.select-none 334.0x36.0 bg #f1f1ee border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px | button.relative.select-none 334.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #f35820 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Ancestor paint | 3 up div.MuiPaper-root.MuiPaper-elevation bg #ffffff shadow #171816 @ 0.03 0px 1px 2px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-email-btn-default.png`, `signup-email-btn-hover.png`, `signup-email-btn-focus-visible.png`, `signup-email-btn-pressed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: the wordmark, the CTA and the "Mobile Menu" button.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0.8 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px |
| Backdrop filter | blur(10px) |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | header.relative.z-[100] 390.0x56.0 bg #ffffff @ 0.8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px; a.relative.select-none 0.0x0.0 bg #fefefd border T:1px solid #f35b22 / R:1px solid #f35b22 / B:1px solid #f35b22 / L:1px solid #f35b22 r 6px; a.relative.select-none 0.0x0.0 bg #f35820 border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #000000 @ 0.02 0px -1px 0px 0px inset, #171816 @ 0.03 0px 1px 2px 0px; span.absolute.left-0 16.0x2.0 bg #202021; span.absolute.left-0 16.0x2.0 bg #202021; span.absolute.left-0 16.0x2.0 bg #202021 |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-menu-btn

Mobile menu button. The "Mobile Menu" button — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `Mobile Menu button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = | = |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | default | = | = | = | = |
| Painted layers | span.absolute.left-0 16.0x2.0 bg #202021; span.absolute.left-0 16.0x2.0 bg #202021; span.absolute.left-0 16.0x2.0 bg #202021; span.absolute.left-0 16.0x2.0 bg #202021 | = | button.relative.ml-4 16.0x16.0 outline 1px auto #e59700 offset 0px; span.absolute.left-0 16.0x2.0 bg #202021; span.absolute.left-0 16.0x2.0 bg #202021; span.absolute.left-0 16.0x2.0 bg #202021; span.absolute.left-0 16.0x2.0 bg #202021 | = | span.absolute.block 0.0x2.0 bg #202021; span.absolute.left-0 12.7x12.7 bg #202021; span.absolute.left-0 12.7x12.7 bg #202021; span.absolute.block 0.0x2.0 bg #202021 |
| Ancestor paint | 3 up header.relative.z-[100] bg #ffffff @ 0.8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.06 0px 1px 2px 0px | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The navigation overlay opened by the menu button (the same destinations as the desktop header); its links were never followed.

Page: mobile. Selector: `mobile nav overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 812 |
| Padding | 0px |
| Gap | 32px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.mb-2.text-[12px]: Inter-c0aaf1024c6c51d7 12px/12px 400, #89898a |
| Transition | none |
| Painted layers | span.inline-flex.items-center 74.0x20.0 bg #ffffff image linear-gradient(301deg, #f35b22 @ 0.01 9.55%, #f35b22 @ 0.1 67.28%) border T:1px solid #ffcab5 / R:1px solid #ffcab5 / B:1px solid #ffcab5 / L:1px solid #ffcab5 r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #be400f @ 0.1 0px -1px 0px 0px inset, #ffffff @ 0.1 0px 1.5px 0px 0px inset, #000000 @ 0.03 0px 0.5px 0px 0px |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 348 x 80 |
| Padding | 0px 0px 0px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter-c0aaf1024c6c51d7 32px/40px 500 |
| Letter spacing | -0.672px |
| Colour | #000000 |
| Text node | span.fp-hero-word.fp-hero-first-word: Inter-c0aaf1024c6c51d7 32px/40px 500, #000000, ls -0.672px |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-cta

Mobile CTA. A "Get Started" action at 390 wide (the header pill is hidden on phones); measured never followed.

Page: mobile. Selector: `mobile Get Started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 141 x 34.8 | = | = | = |
| Padding | 8px 14px | = | = | = |
| Border | 1px solid #bd400f | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f35820 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | = | = | = |
| Outline | none | = | 2px solid #f35820 offset 2px | = |
| Font | Inter-c0aaf1024c6c51d7 12px/16.8px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter-c0aaf1024c6c51d7 12px/16.8px 500, #ffffff | = | = | = |
| Transition | background-color, border-color, box-shadow, color, opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.box-border 141.0x34.8 bg #f35820 border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset | = | a.inline-flex.box-border 141.0x34.8 bg #f35820 border T:1px solid #bd400f / R:1px solid #bd400f / B:1px solid #bd400f / L:1px solid #bd400f r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset, #181916 @ 0.06 0px 1px 2px 0px, #181916 @ 0.1 0px -1px 0px 0px inset outline 2px solid #f35820 offset 2px | = |
| Ancestor paint | 2 up header.col-[1/7].m-[9px] bg #fafaf8 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #181916 @ 0.1 0px 4px 6px -1px, #181916 @ 0.1 0px 2px 4px -2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

## Transitions declared in the readable stylesheets

fingerprint.com serves its CSS as linked `/_astro/*.css` bundles plus small inline blocks; docs.fingerprint.com ships a separate Mintlify sheet. This list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- about: `0.2s`, `0.35s`, `background-color 0.5s`, `background-color 0.25s, border 0.25s, opacity 0.25s, color 0.25s`, `background 0.3s`, `background 0.35s, border-top-color 0.35s`, `background 0.35s`, `background 0.12s, color 0.12s, border-color 0.12s`, `background 0.12s, opacity 0.12s`, `border 0.1s ease-in-out, outline 0.1s ease-in-out`, `box-shadow 0.2s`, `color 0.2s, transform 0.2s`

- blog: `background-color 0.1s`, `background-color 0.16s ease-out, color 0.16s ease-out, opacity 0.16s ease-out, box-shadow 0.16s ease-out`, `fill 0.5s linear`, `max-height 0.42s ease-in-out`, `opacity 0.3s`, `transform 0.2s, top 0.2s, -moz-transform 0.2s`, `transform 0.2s, left 0.2s, -moz-transform 0.2s`, `transform 0.2s, right 0.2s, -moz-transform 0.2s`, `0.2s ease-out`, `fill 0.25s linear`, `opacity 0.2s`, `0.3s`

- careers: `0.2s`, `0.35s`, `background-color 0.5s`, `background-color 0.25s, border 0.25s, opacity 0.25s, color 0.25s`, `background 0.3s`, `background 0.35s, border-top-color 0.35s`, `background 0.35s`, `background 0.12s, color 0.12s, border-color 0.12s`, `background 0.12s, opacity 0.12s`, `border 0.1s ease-in-out, outline 0.1s ease-in-out`, `box-shadow 0.2s`, `color 0.2s, transform 0.2s`

- case-studies: `0.2s`, `0.35s`, `background-color 0.5s`, `background-color 0.25s, border 0.25s, opacity 0.25s, color 0.25s`, `background 0.3s`, `background 0.35s, border-top-color 0.35s`, `background 0.35s`, `background 0.12s, color 0.12s, border-color 0.12s`, `background 0.12s, opacity 0.12s`, `border 0.1s ease-in-out, outline 0.1s ease-in-out`, `box-shadow 0.2s`, `color 0.2s, transform 0.2s`

- contact: `0.2s`, `0.35s`, `background-color 0.5s`, `background-color 0.25s, border 0.25s, opacity 0.25s, color 0.25s`, `background 0.3s`, `background 0.35s, border-top-color 0.35s`, `background 0.35s`, `background 0.12s, color 0.12s, border-color 0.12s`, `background 0.12s, opacity 0.12s`, `border 0.1s ease-in-out, outline 0.1s ease-in-out`, `box-shadow 0.2s`, `color 0.2s, transform 0.2s`

- demo: `0.2s`, `0.35s`, `background-color 0.5s`, `background-color 0.25s, border 0.25s, opacity 0.25s, color 0.25s`, `background 0.3s`, `background 0.35s, border-top-color 0.35s`, `background 0.35s`, `background 0.12s, color 0.12s, border-color 0.12s`, `background 0.12s, opacity 0.12s`, `border 0.1s ease-in-out, outline 0.1s ease-in-out`, `box-shadow 0.2s`, `color 0.2s, transform 0.2s`

- docs: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long)var(--timing),height var(--duration-long)var(--timing),background var(--duration-short)ease,scale var(--duration-short)var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration))var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration)var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`, `200ms`

- docs-home: none

- home: `0.2s`, `0.35s`, `background-color 0.5s`, `background-color 0.25s, border 0.25s, opacity 0.25s, color 0.25s`, `background 0.3s`, `background 0.35s, border-top-color 0.35s`, `background 0.35s`, `background 0.12s, color 0.12s, border-color 0.12s`, `background 0.12s, opacity 0.12s`, `border 0.1s ease-in-out, outline 0.1s ease-in-out`, `box-shadow 0.2s`, `color 0.2s, transform 0.2s`

- identification: `0.2s`, `0.35s`, `background-color 0.5s`, `background-color 0.25s, border 0.25s, opacity 0.25s, color 0.25s`, `background 0.3s`, `background 0.35s, border-top-color 0.35s`, `background 0.35s`, `background 0.12s, color 0.12s, border-color 0.12s`, `background 0.12s, opacity 0.12s`, `border 0.1s ease-in-out, outline 0.1s ease-in-out`, `box-shadow 0.2s`, `color 0.2s, transform 0.2s`

- login: `box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 0.2s linear`, `color 0.2s ease-in-out`, `opacity 0.2s ease-out`, `opacity 0.2s ease-in`, `background-color 600000s, color 600000s`, `opacity 0.15s 0.3s`, `transform 0.2s ease-out`, `background-color 0.25s`, `--_m 0.3s linear`, `0.3s cubic-bezier(0.645, 0.045, 0.355, 1)`

- pricing: `0.2s`, `0.35s`, `background-color 0.5s`, `background-color 0.25s, border 0.25s, opacity 0.25s, color 0.25s`, `background 0.3s`, `background 0.35s, border-top-color 0.35s`, `background 0.35s`, `background 0.12s, color 0.12s, border-color 0.12s`, `background 0.12s, opacity 0.12s`, `border 0.1s ease-in-out, outline 0.1s ease-in-out`, `box-shadow 0.2s`, `color 0.2s, transform 0.2s`

- resources: `background-color 0.1s`, `background-color 0.16s ease-out, color 0.16s ease-out, opacity 0.16s ease-out, box-shadow 0.16s ease-out`, `fill 0.5s linear`, `max-height 0.42s ease-in-out`, `opacity 0.3s`, `transform 0.2s, top 0.2s, -moz-transform 0.2s`, `transform 0.2s, left 0.2s, -moz-transform 0.2s`, `transform 0.2s, right 0.2s, -moz-transform 0.2s`, `0.2s ease-out`, `fill 0.25s linear`, `opacity 0.2s`, `0.3s`

- signup: `box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)`, `color 0.2s ease-in-out`, `opacity 0.2s ease-out`, `opacity 0.2s ease-in`, `background-color 600000s, color 600000s`, `opacity 0.15s 0.3s`, `transform 0.2s ease-out`, `background-color 0.25s`, `--_m 0.3s linear`, `0.3s cubic-bezier(0.645, 0.045, 0.355, 1)`

## Reduced motion

- home (`header a[href*="dashboard.fingerprint.com/signup"]` under prefers-reduced-motion): transition `color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1)`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
