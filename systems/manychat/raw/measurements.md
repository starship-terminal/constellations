# Component measurements

Computed styles read from manychat.com on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-banner

Promo banner. The Creator World 27 strip above the nav. A marketing link; measured, never followed.

Page: home. Selector: `a[href*="creatorworld"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #0f0f0f |
| Box shadow | none |
| Outline | none |
| Font | Rooftop 15px/19.5px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.relative.z-2: CoFo Sans Mono 14px/10px 400, #0f0f0f |
| Transition | color 0.3s ease |
| Cursor | pointer |
| Painted layers | a.flex.h-(--creatorworld-banner-height) 1440.0x68.0 bg #0f0f0f; span.relative.z-2 162.8x30.0 bg #79ff72 r 43px; span.relative.z-2 162.8x30.0 bg #79ff72 r 43px; span.relative.z-2 162.8x30.0 bg #79ff72 r 43px; span.relative.z-2 162.8x30.0 bg #79ff72 r 43px |
| How | at rest |

Crops: `promo-banner-default.png`.

#### header-nav

Header. The sticky nav: logo, Product/Solutions/Agencies/Pricing/Resources, locale, Log in, Get started. The site paints no <header> element.

Page: home. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Rooftop 15px/19.5px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.uppercase.opacity-0: CoFo Sans Mono 12px/16.32px 400, #ffffff, ls 0.12px |
| Transition | transform 0.45s cubic-bezier(0.43, 0.195, 0.02, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 151 x 28, colour #ffffff |
| Painted layers | div::before._4Y2iAa_menu 1400pxx900px bg #edf2ed; a.p_y-s.p_x-l 150.0x48.0 bg #fa0cf7 r 999px; a::before.p_y-s.p_x-l 149.953pxx48px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px; div.mb-0.4rem.flex 1336.0x48.3 bg #ffffff r 8px; span._4Y2iAa_underline_item.mc-text-label 51.3x16.3 image linear-gradient(#ffffff, #ffffff); span._4Y2iAa_underline_item.ml-0.8rem 121.4x29.0 image linear-gradient(#ffffff, #ffffff) |
| How | at rest |

Crops: `header-nav-default.png`.

#### nav-logo

Logo. The Manychat wordmark in the nav.

Page: home. Selector: `nav a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 151 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Rooftop 15px/19.5px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | color 0.3s ease |
| Cursor | pointer |
| Icon | 151 x 28, colour #ffffff |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-link

Nav item (dropdown). "Product" is a div, not a button. It opens the channel mega-menu. A local toggle; its links were never followed.

Page: home. Selector: `div (text PRODUCT, nav band)`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 51.25 x 18 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | CoFo Sans Mono 12px/18px 400 | = | - | = | = |
| Letter spacing | 0.12px | = | - | = | = |
| Colour | #ffffff | #000000 | - | #000000 | #000000 |
| Text node | span._4Y2iAa_underline_item: CoFo Sans Mono 12px/18px 400, #ffffff, ls 0.12px | span._4Y2iAa_underline_item: CoFo Sans Mono 12px/18px 400, #000000, ls 0.12px | - | span._4Y2iAa_underline_item: CoFo Sans Mono 12px/18px 400, #000000, ls 0.12px | span._4Y2iAa_underline_item: CoFo Sans Mono 12px/18px 400, #000000, ls 0.12px |
| Transition | transform 0.45s cubic-bezier(0.43, 0.195, 0.02, 1) | = | - | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Painted layers | span._4Y2iAa_underline_item 51.3x14.0 image linear-gradient(#ffffff, #ffffff) | span._4Y2iAa_underline_item 51.3x14.0 image linear-gradient(#000000, #000000) | - | span._4Y2iAa_underline_item 51.3x14.0 image linear-gradient(#000000, #000000) | span._4Y2iAa_underline_item 51.3x14.0 image linear-gradient(#000000, #000000) |
| Ancestor paint | 1 up div._4Y2iAa_nav_item._4Y2iAa_underline shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | own toggle |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-pressed.png`, `nav-link-opened.png`.

#### nav-plain-link

Nav link. "Pricing" is a plain nav anchor. Measured, never followed from this shot.

Page: home. Selector: `a (text PRICING, nav band)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 51.25 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CoFo Sans Mono 12px/18px 400 | = | = | = |
| Letter spacing | 0.12px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span._4Y2iAa_underline_item: CoFo Sans Mono 12px/18px 400, #000000, ls 0.12px | = | = | = |
| Transition | transform 0.45s cubic-bezier(0.43, 0.195, 0.02, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span._4Y2iAa_underline_item 51.3x14.0 image linear-gradient(#000000, #000000) | = | = | = |
| Ancestor paint | 1 up div._4Y2iAa_nav_item._4Y2iAa_underline shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-plain-link-default.png`, `nav-plain-link-hover.png`, `nav-plain-link-focus-visible.png`, `nav-plain-link-pressed.png`.

#### nav-locale

Locale switch. The EN language switch is a div. Measured; the locale was never changed.

Page: home. Selector: `div (text EN, nav band)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 14.64 x 16.31 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Background image | linear-gradient(#000000, #000000) | = | - | = |
| Box shadow | #000000 0px -1px 1px -1px inset, #000000 0px -1px 1px -1px inset | = | - | = |
| Outline | none | = | - | = |
| Font | CoFo Sans Mono 12px/16.32px 400 | = | - | = |
| Letter spacing | 0.12px | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.uppercase.opacity-0: CoFo Sans Mono 12px/16.32px 400, #000000, ls 0.12px | = | - | = |
| Transition | background-size 0.3s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | div.underline_link.!absolute 14.6x16.3 image linear-gradient(#000000, #000000) shadow #000000 0px -1px 1px -1px inset, #000000 0px -1px 1px -1px inset | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-locale-default.png`, `nav-locale-hover.png`, `nav-locale-pressed.png`.

#### nav-login

Log in link. "Log in" points at app.manychat.com/signin. Measured, never followed. Sign-in boundary.

Page: home. Selector: `a[href*="/signin"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99.92 x 44.31 | = | = | = |
| Padding | 14px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CoFo Sans Mono 12px/16.32px 400 | = | = | = |
| Letter spacing | 0.12px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | hidden duplicate span: CoFo Sans Mono 12px/16.32px 400, #000000 @ 0, ls 0.12px | = | = | = |
| Transition | background, transform 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 99.9219px x 44.3125px, absolute, bg #000000 @ 0, radius 999px | = | = | = |
| Painted layers | a::before.p_y-s.p_x-l 99.9219pxx44.3125px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Get started pill. The nav "Get started" pill. It opens the sign-up flow. Measured, never followed.

Page: home. Selector: `a (text GET STARTED, nav band y 60-180)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136.53 x 44.31 | = | = | = |
| Padding | 14px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CoFo Sans Mono 12px/16.32px 400 | = | = | = |
| Letter spacing | 0.12px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | hidden duplicate span: CoFo Sans Mono 12px/16.32px 400, #000000 @ 0, ls 0.12px | = | = | = |
| Transition | background, transform 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 136.531px x 44.3125px, absolute, bg #000000 @ 0, radius 999px | = | = | = |
| Painted layers | a.p_y-s.p_x-l 136.5x44.3 bg #ffffff r 999px; a::before.p_y-s.p_x-l 136.531pxx44.3125px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### menu-item

Mega-menu item. The closed Product menu keeps these links in the DOM at opacity 0. They are not a captured open state. A refresh must wait until a menu link paints before saving them.

Page: home. Selector: `a[href="/product/instagram"]`. States: .

Not found on the page at capture time.

#### channel-card

Channel menu item. The closed Product menu keeps these links in the DOM at opacity 0. They are not a captured open state. A refresh must wait until a menu link paints before saving them.

Page: home. Selector: `a[href^="/product/"]`. States: .

Not found on the page at capture time.

#### footer

Footer. The footer band: product, company and legal columns.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 942.22 |
| Padding | 40px 0px |
| Border | T: 1px solid #ffffff @ 0.25; R: none; B: none; L: none |
| Radius | 0px |
| Background | #0f0f0f |
| Box shadow | none |
| Outline | none |
| Font | Rooftop 15px/19.5px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.mc-text-label.text-nowrap: CoFo Sans Mono 12px/16.32px 400, #ffffff, ls 0.12px |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | footer.border-t.border-raw-neutral-0/25 1440.0x942.2 bg #0f0f0f border T:1px solid #ffffff @ 0.25; div.transition-scale.flex 0.0x0.0 bg #fff100 r 999px; a.underline_link.group/footer-link 64.4x14.0 image linear-gradient(#ffffff, #ffffff) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.underline_link.group/footer-link 40.4x14.0 image linear-gradient(#ffffff, #ffffff) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.underline_link.group/footer-link 63.7x14.0 image linear-gradient(#ffffff, #ffffff) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.underline_link.group/footer-link 69.7x14.0 image linear-gradient(#ffffff, #ffffff) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. "About" in the footer. Measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 37.67 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#ffffff, #ffffff) | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | Rooftop 12px/16.32px 400 | = | = | = |
| Letter spacing | 0.12px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-size 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.underline_link.group/footer-link 37.7x14.0 image linear-gradient(#ffffff, #ffffff) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Home

#### hero-h1

Hero heading. "Social smarter, not harder." set in ManyChatGravity.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 692 x 118.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ManyChatGravity 72px/59.04px 400 |
| Letter spacing | -1.44px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero Get started. The neon-pink hero pill. It opens sign-up. Measured, never followed.

Page: home. Selector: `main a[href*="signup"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149.95 x 48 | = | = | = |
| Padding | 14px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #fa0cf7 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CoFo Sans Mono 14px/20px 400 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | hidden duplicate span: CoFo Sans Mono 14px/20px 400, #000000 @ 0, ls 0.14px | = | = | = |
| Transition | background, transform 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 149.953px x 48px, absolute, bg #000000 @ 0, radius 999px | = | = | = |
| Painted layers | a.p_y-s.p_x-l 150.0x48.0 bg #fa0cf7 r 999px; a::before.p_y-s.p_x-l 149.953pxx48px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### section-heading

Section heading. A Rooftop section heading below the hero.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 930 x 118.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ManyChatGravity 72px/59.04px 400 |
| Letter spacing | -1.44px |
| Colour | #0f0f0f |
| Transition | opacity, transform 0.7s, 0.7s cubic-bezier(0.43, 0.195, 0.02, 1), cubic-bezier(0.43, 0.195, 0.02, 1) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `section-heading-default.png`.

#### quote-card

Creator quote. A published creator quote on the home page. Marketing copy, not an account.

Page: home. Selector: `blockquote, figure`. States: .

Not found on the page at capture time.

#### faq-item

FAQ accordion. A home FAQ summary. Opened by its own click. Nothing was submitted.

Page: home. Selector: `button`. States: default, opened, focus-visible.

| Property | default | opened | focus-visible |
|---|---|---|---|
| Size (w x h) | 841.33 x 62.39 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Rooftop 15px/19.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | h3.transition-transform.duration-300: Rooftop 16px/22.4px 400, #ffffff | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| How | at rest | own toggle | Shift+Tab, Tab |

Crops: `faq-item-default.png`, `faq-item-opened.png`, `faq-item-focus-visible.png`.

### Pricing

#### price-h1

Pricing heading. "Plans that scale when you do".

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 38.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Rooftop 36px/38.88px 600 |
| Letter spacing | -1.44px |
| Colour | #0f0f0f |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### billing-toggle

Billing toggle. The Annual side of the Monthly/Annual switch. The control is a label, not a button. A local UI toggle. Checkout was never opened.

Page: pricing. Selector: `label (text ANNUAL)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 51.25 x 19.59 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | CoFo Sans Mono 14px/19.6px 400 | = | - | = |
| Letter spacing | 0.14px | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-pressed.png`.

#### price-card

Price card. The Free plan card: $0, 25 active contacts, Start for free.

Page: pricing. Selector: `card ancestor of the Free heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 368.53 x 661.53 |
| Padding | 32px 32px 40px 32px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Rooftop 15px/19.5px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | h4.text-left.font-rooftop: Rooftop 20px/28px 700, #0f0f0f |
| Transition | none |
| Cursor | grab |
| Icon | 16 x 16, colour #0f0f0f @ 0.2 |
| Painted layers | div.relative.h-full 368.5x661.5 bg #ffffff r 24px; span.underline_link.cursor-pointer 250.9x16.0 image linear-gradient(#0f0f0f, #0f0f0f) shadow #0f0f0f 0px -1px 1px -1px inset, #0f0f0f 0px -1px 1px -1px inset; a.p_y-s.p_x-l 304.5x48.0 bg #0f0f0f r 999px; a::before.p_y-s.p_x-l 304.531pxx48px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px; div.relative.rounded-[1.2rem] 200.0x83.2 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 60px 0px; div::before.relative.rounded-[1.2rem] 11pxx6px bg #ffffff |
| How | at rest |

Crops: `price-card-default.png`.

#### price-cta

Price CTA. "Start for free" on the Free card. It opens sign-up. Measured, never followed. Checkout was not submitted.

Page: pricing. Selector: `a[href*="signup"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 304.53 x 48 | = | = | = |
| Padding | 14px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #0f0f0f | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CoFo Sans Mono 12px/20px 400 | = | = | = |
| Letter spacing | 0.12px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | hidden duplicate span: CoFo Sans Mono 12px/20px 400, #000000 @ 0, ls 0.12px | = | = | = |
| Transition | background, transform 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 304.531px x 48px, absolute, bg #000000 @ 0, radius 999px | = | = | = |
| Painted layers | a.p_y-s.p_x-l 304.5x48.0 bg #0f0f0f r 999px; a::before.p_y-s.p_x-l 304.531pxx48px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | = | = | = |
| Ancestor paint | 1 up div.relative.h-full bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-cta-default.png`, `price-cta-hover.png`, `price-cta-focus-visible.png`, `price-cta-pressed.png`.

#### price-faq

Pricing FAQ. A pricing FAQ summary, opened by its own click. Nothing was submitted.

Page: pricing. Selector: `button, summary`. States: .

Not found on the page at capture time.

### Instagram product

#### product-h1

Product heading. "Your Instagram just got smarter".

Page: instagram. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 590 x 118.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ManyChatGravity 72px/59.04px 400 |
| Letter spacing | -1.44px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `product-h1-default.png`.

#### product-cta

Product CTA. A product-page Get started pill. Measured, never followed.

Page: instagram. Selector: `a[href*="signup"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136.53 x 44.31 | = | = | = |
| Padding | 14px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CoFo Sans Mono 12px/16.32px 400 | = | = | = |
| Letter spacing | 0.12px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | hidden duplicate span: CoFo Sans Mono 12px/16.32px 400, #000000 @ 0, ls 0.12px | = | = | = |
| Transition | background, transform 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 136.531px x 44.3125px, absolute, bg #000000 @ 0, radius 999px | = | = | = |
| Painted layers | a.p_y-s.p_x-l 136.5x44.3 bg #ffffff r 999px; a::before.p_y-s.p_x-l 136.531pxx44.3125px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `product-cta-default.png`, `product-cta-hover.png`, `product-cta-focus-visible.png`, `product-cta-pressed.png`.

### How-to resources

#### howto-h1

How-to heading. "How to Use Manychat". A public guide index, not the bot builder.

Page: how-to. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1041.31 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ManyChatGravity 80px/72px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Transition | none |
| How | at rest |

Crops: `howto-h1-default.png`.

#### howto-card

Guide card. A public how-to card. Measured, never followed into a form.

Page: how-to. Selector: `main a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 368 x 372.17 | = |
| Padding | 0px | = |
| Border | 1px solid #f5f5f5 | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0.08 0px 4px 8px 0px | #000000 @ 0.08 0px 8px 16px 10px |
| Outline | none | = |
| Font | Rooftop 15px/19.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #0f0f0f | = |
| Text node | i: Rooftop 20px/24px 600, #0f0f0f @ 0.4 | i: Rooftop 20px/24px 600, #0f0f0f |
| Transition | transform, box-shadow 0.3s, 0.3s ease, ease delay 0s, 0s | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, -4) |
| Cursor | pointer | = |
| Painted layers | a.b_a.o_hidden 368.0x372.2 border T:1px solid #f5f5f5 / R:1px solid #f5f5f5 / B:1px solid #f5f5f5 / L:1px solid #f5f5f5 shadow #000000 @ 0.08 0px 4px 8px 0px | a.b_a.o_hidden 368.0x372.2 border T:1px solid #f5f5f5 / R:1px solid #f5f5f5 / B:1px solid #f5f5f5 / L:1px solid #f5f5f5 shadow #000000 @ 0.08 0px 8px 16px 10px |
| How | at rest | mouse hover |

Crops: `howto-card-default.png`, `howto-card-hover.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The nav at phone width. The site paints no <header> element.

Page: home. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Rooftop 15px/19.5px 400 |
| Letter spacing | normal |
| Colour | #0f0f0f |
| Text node | span.uppercase.opacity-0: CoFo Sans Mono 12px/16.32px 400, #ffffff, ls 0.12px |
| Transition | transform 0.45s cubic-bezier(0.43, 0.195, 0.02, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 107.84 x 20, colour #ffffff |
| Painted layers | div::before._4Y2iAa_menu 390pxx844px bg #edf2ed; a.p_y-s.p_x-l 150.0x48.0 bg #fa0cf7 r 999px; a::before.p_y-s.p_x-l 149.953pxx48px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 999px; div.mb-0.4rem.flex 358.0x48.3 bg #ffffff r 8px; span._4Y2iAa_underline_item.mc-text-label 51.3x16.3 image linear-gradient(#ffffff, #ffffff); span._4Y2iAa_underline_item.ml-0.8rem 101.2x24.0 image linear-gradient(#ffffff, #ffffff) |
| How | at rest |

Crops: `m-header-default.png`.

#### m-logo

Mobile logo.

Page: home. Selector: `a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 107.84 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Rooftop 15px/19.5px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | color 0.3s ease |
| Cursor | pointer |
| Icon | 107.84 x 20, colour #ffffff |
| How | at rest |

Crops: `m-logo-default.png`.

#### m-hamburger

Mobile menu button. The menu trigger at 390px. A local toggle.

Page: home. Selector: `header button`. States: .

Not found on the page at capture time.

#### m-h1

Mobile hero heading. The hero h1 at 390px.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 72.16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ManyChatGravity 44px/36.08px 400 |
| Letter spacing | -0.88px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-h1-default.png`.

#### m-cta

Mobile Get started. A Get started link at 390px. Measured, never followed.

Page: home. Selector: `a[href*="signup"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128.53 x 32.31 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #fa0cf7 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CoFo Sans Mono 12px/16.32px 400 | = | = | = |
| Letter spacing | 0.12px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | hidden duplicate span: CoFo Sans Mono 12px/16.32px 400, #000000 @ 0, ls 0.12px | = | = | = |
| Transition | background, transform 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Opacity | 0 | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 128.531px x 32.3125px, absolute, bg #000000 @ 0, radius 32px | = | = | = |
| Painted layers | a.p_y-xs.p_x-m 128.5x32.3 bg #fa0cf7 r 32px; a::before.p_y-xs.p_x-m 128.531pxx32.3125px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 32px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

## Transitions declared in the readable stylesheets

Manychat serves its marketing CSS from mccdn.me. Cross-origin sheets are invisible to the CSSOM, so this list holds only what each page could read. The per-state Transition rows above are computed values and cover the painted rules.

- home: none

- how-to: none

- instagram: none

- pricing: none
