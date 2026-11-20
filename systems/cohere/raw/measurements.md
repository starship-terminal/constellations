# Component measurements

Computed styles read from cohere.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) on the site's light surface (no consent overlay mounted on the captured routes), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-banner

Promo banner. The dismissible announcement strip above the nav ("Rerank 5 is here…"), bg-pureBlack, with its Learn-more link and close control.

Page: home. Selector: `div.bg-pureBlack first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 48 |
| Padding | 12px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-web3-16.font-body: Unica77 Cohere Web 16px/22.4px 400, #ffffff |
| Transition | none |
| Painted layers | div.relative.z-nav 1440.0x48.0 bg #000000; a.border.border-x-0 73.0x20.6 border B:1px solid #ffffff |
| How | at rest |

Crops: `promo-banner-default.png`.

#### banner-close

Banner close. The promo banner close button (icon-close, hover rotate-90). A local dismiss toggle — pressing it only hides the banner.

Page: home. Selector: `button[aria-label="Close banner"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 24 | 24 x 16 | = | 24 x 16 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.relative.z-nav bg #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0, 1, -1, 0, 0, 0) | = | matrix(0, 1, -1, 0, 0, 0) |
| Painted layers | - | = | button.mt-1.self-start 16.0x24.0 outline 1px auto #101010 offset 0px | = |

Crops: `banner-close-default.png`, `banner-close-hover.png`, `banner-close-focus-visible.png`, `banner-close-pressed.png`.

#### header

Nav bar. The fixed site nav (nav.z-nav, h-[60px] inner bar): Cohere mark, roll-hover nav links, Sign in + Request-a-demo CTAs.

Page: home. Selector: `nav first visible`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-web3-14.font-body: Unica77 Cohere Web 14px/19.6px 400, #000000 |
| Transition | transform 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | div.relative.z-10 1440.0x60.0 bg #ffffff; a.whitespace-nowrap.pt-1.5 42.0x31.6 outline 2px solid #000000 @ 0 offset 2px; div.ease-button-gradient.absolute 0.0x1.0 image linear-gradient(to right, #ff7759, #7670c5, #4c6ee6); a.whitespace-nowrap.relative 139.0x36.0 bg #17171c border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.whitespace-nowrap.relative 135pxx32px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px; div.border-neutral-85.bg-pureWhite 1440.0x1899.8 bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Cohere mark home anchor in the nav (h-5 w-[118px] svg).

Page: home. Selector: `nav a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 118 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. A flat nav link with the roll-hover duplicate text (group/nav-link, hover translates the label -100%).

Page: home. Selector: `nav a.group/nav-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 31.59 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | #f2f2f2 @ 0.93 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-web3-14.font-body: Unica77 Cohere Web 14px/19.6px 400, #000000 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group/nav-link.inline-flex 81.0x31.6 bg #f2f2f2 @ 0.93 r 9999px outline 1px auto #101010 offset 1px | = |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-signin

Nav sign-in. The transparent "Sign in" ghost control linking to dashboard.cohere.com; measured never followed.

Page: home. Selector: `nav a:has-text("Sign in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42 x 31.59 | = | = | = |
| Padding | 6px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #4c6ee6 offset 2px | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #212121 | = | = | = |
| Text node | span.text-web3-14.font-body: Unica77 Cohere Web 14px/19.6px 400, #212121 | = | = | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.whitespace-nowrap.pt-1.5 42.0x31.6 outline 2px solid #000000 @ 0 offset 2px; div.ease-button-gradient.absolute 0.0x1.0 image linear-gradient(to right, #ff7759, #7670c5, #4c6ee6) | a.whitespace-nowrap.pt-1.5 42.0x31.6 outline 2px solid #000000 @ 0 offset 2px; div.ease-button-gradient.absolute 42.0x1.0 image linear-gradient(to right, #ff7759, #7670c5, #4c6ee6) | a.whitespace-nowrap.pt-1.5 42.0x31.6 outline 2px solid #4c6ee6 offset 2px; div.ease-button-gradient.absolute 0.0x1.0 image linear-gradient(to right, #ff7759, #7670c5, #4c6ee6) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Nav CTA. The dark "Request a demo" ease-button-gradient pill in the nav; links to the contact form, never followed.

Page: home. Selector: `nav a:has-text("Request a demo")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | 2px solid #fafafa | = |
| Radius | 9999px | = | = | = |
| Background | #17171c | #000000 | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4c6ee6 0px 0px 0px 2px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-web3-14.font-body: Unica77 Cohere Web 14px/19.6px 400, #ffffff | = | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 135px x 32px, absolute, bg #000000 @ 0 linear-gradient(270deg, #d18ee2, #ff7759), radius 32px | = | = | = |
| Painted layers | a.whitespace-nowrap.relative 139.0x36.0 bg #17171c border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.whitespace-nowrap.relative 135pxx32px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | a.whitespace-nowrap.relative 139.0x36.0 bg #000000 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.whitespace-nowrap.relative 135pxx32px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | a.whitespace-nowrap.relative 139.0x36.0 bg #17171c border T:2px solid #fafafa / R:2px solid #fafafa / B:2px solid #fafafa / L:2px solid #fafafa r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4c6ee6 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 2px; a::before.whitespace-nowrap.relative 135pxx32px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title. "Your AI. Your rules." — the hero headline (web3 display scale).

Page: home. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1128 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CohereText 96px/96px 400 |
| Letter spacing | -1.92px |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The first ease-button-gradient CTA in page content ("Explore now"-style pill); links onward, never followed.

Page: home. Selector: `main a.ease-button-gradient`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152 x 53.2 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17171c | #000000 | = | = |
| Text node | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #17171c | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #000000 | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 148px x 49.2031px, absolute, bg #000000 @ 0 linear-gradient(270deg, #d18ee2, #ff7759), radius 32px | = | = | = |
| Painted layers | a.relative.flex 152.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 148pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = | a.relative.flex 152.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 148pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### cta-dark

Dark CTA. A dark ease-button-gradient pill (bg-neutral-15 text-pureWhite, gradient hover sweep) in page content.

Page: home. Selector: `main a.ease-button-gradient.bg-neutral-15`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146 x 53.2 | - | = | = |
| Padding | 12px 24px | - | = | = |
| Border | 2px solid #000000 @ 0 | - | 2px solid #fafafa | = |
| Radius | 9999px | - | = | = |
| Background | #17171c | - | = | = |
| Box shadow | none | - | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4c6ee6 0px 0px 0px 2px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | - | = | = |
| Font | Unica77 Cohere Web 16px/24px 400 | - | = | = |
| Letter spacing | normal | - | = | = |
| Colour | #ffffff | - | = | = |
| Text node | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #ffffff | - | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | - | = | = |
| Cursor | pointer | - | = | = |
| ::before | 142px x 49.2031px, absolute, bg #000000 @ 0 linear-gradient(270deg, #d18ee2, #ff7759), radius 32px | - | = | = |
| Painted layers | a.relative.flex 146.0x53.2 bg #17171c border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 142pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | - | a.relative.flex 146.0x53.2 bg #17171c border T:2px solid #fafafa / R:2px solid #fafafa / B:2px solid #fafafa / L:2px solid #fafafa r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4c6ee6 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 142pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = |
| How | at rest | - | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Error | - | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('main a[class*="ease-button-gradient"].bg-neutral-15, section a[class*="ease-button-gradient"].bg-neutral-15').first().firs | = | = |

Crops: `cta-dark-default.png`, `cta-dark-focus-visible.png`, `cta-dark-pressed.png`.

#### cta-light

Light CTA. A light ease-button-gradient pill (bg-pureWhite text-neutral-15) in page content.

Page: home. Selector: `main a.ease-button-gradient.bg-pureWhite`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152 x 53.2 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17171c | #000000 | = | = |
| Text node | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #17171c | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #000000 | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 148px x 49.2031px, absolute, bg #000000 @ 0 linear-gradient(270deg, #d18ee2, #ff7759), radius 32px | = | = | = |
| Painted layers | a.relative.flex 152.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 148pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = | a.relative.flex 152.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 148pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-light-default.png`, `cta-light-hover.png`, `cta-light-focus-visible.png`, `cta-light-pressed.png`.

#### callout-card

Callout card. A callout-module card anchor (group/calloutCard, rounded-lg/xl).

Page: home. Selector: `a.group/calloutCard`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 437.33 x 492.81 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 22px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #212121 | = | = | = |
| Text node | p.text-web3-14-eyebrow.uppercase: CohereMono 14px/19.6px 400, #212121, ls 0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 438.33 x 72.61, colour #212121, fill #000000 | = | = | = |
| Painted layers | div.flex.w-full 437.3x421.2 bg #f0eee9 r 22px 22px 0px 0px | = | a.group/calloutCard.relative 437.3x492.8 r 22px outline 1px auto #101010 offset 1px; div.flex.w-full 437.3x421.2 bg #f0eee9 r 22px 22px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `callout-card-default.png`, `callout-card-hover.png`, `callout-card-focus-visible.png`, `callout-card-pressed.png`.

#### marquee-logo

Customer logo. A logo in the customer marquee (Oracle/Dell/RBC row, rendered twice for the loop).

Page: home. Selector: `img[alt$=" Logo"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 148 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: none.

#### section-title

Section title. A section heading under the hero (web3 display scale).

Page: home. Selector: `first visible h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 675.2 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CohereText 60px/60px 400 |
| Letter spacing | -1.2px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### page-ground

Page ground. The body element painted fill — the page ground.

Page: home. Selector: `document.body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 8680.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: Unica77 Cohere Web 16px/24px 400, #000000 |
| Transition | none |
| Icon | 0 x 0, colour #00754e |
| Painted layers | body.bg-surface-inverse.user-is-tabbing 1440.0x8680.1 bg #ffffff; div.cky-hide.cky-overlay 0.0x0.0 bg #000000; div.cky-consent-bar 0.0x0.0 bg #ffffff border T:1px solid #f4f4f4 @ 0 / R:1px solid #f4f4f4 @ 0 / B:1px solid #f4f4f4 @ 0 / L:1px solid #f4f4f4 @ 0 r 8px shadow #acabab @ 0.3 0px -1px 10px 0px; button.cky-banner-btn-close 0.0x0.0 bg #ffffff @ 0; div.cky-modal 845.0x304.0 bg #ffffff r 6px shadow #000000 @ 0.3 0px 32px 68px 0px; div.cky-preference-center 845.0x304.0 bg #ffffff r 8px |
| How | at rest |

Crops: none.

### Pricing

#### pricing-title

Pricing title. The pricing headline.

Page: pricing. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1128 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CohereText 72px/72px 400 |
| Letter spacing | -1.44px |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### price-tab

Category tab (selected). The selected model-category tab (role=tab aria-selected=true — "Workplace systems") switching the rate table. Measured at rest, never switched.

Page: pricing. Selector: `[role=tab][aria-selected=true]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160 x 34 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #212121 | = | = | = |
| Text node | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #17171c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.relative.py-1 160.0x34.0 outline 1px auto #101010 offset 0px | = |

Crops: `price-tab-default.png`, `price-tab-hover.png`, `price-tab-focus-visible.png`, `price-tab-pressed.png`.

#### price-tab-off

Category tab (unselected). An unselected model-category tab (aria-selected=false); never pressed — it would swap the rate table.

Page: pricing. Selector: `[role=tab][aria-selected=false]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 153 x 34 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #212121 | = | = | = |
| Text node | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #17171c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.relative.py-1 153.0x34.0 outline 1px auto #101010 offset 0px | = |

Crops: `price-tab-off-default.png`, `price-tab-off-hover.png`, `price-tab-off-focus-visible.png`, `price-tab-off-pressed.png`.

#### price-rate

Rate figure. A per-model rate figure in the pricing table (the "$3.00"-style cells).

Page: pricing. Selector: `text=/\$\d+/`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 46 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 18px/25.2px 400 |
| Letter spacing | normal |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: `price-rate-default.png`.

#### faq-item

FAQ row. A pricing-FAQ accordion row (closed state; its own press opens the answer — a local toggle).

Page: pricing. Selector: `button:has-text("How do I")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 660 x 61.2 | = | = | = |
| Padding | 0px 0px 36px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #212121 | = | = | = |
| Text node | h5.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #17171c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.w-full 660.0x61.2 outline 1px auto #101010 offset 0px | = |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`.

#### faq-item-open

FAQ row, open. The FAQ item after its question button's own press (a local UI toggle) — the enclosing row is measured so the expanded answer lands in the state, not just the toggle.

Page: pricing. Selector: `parent of button:has-text("How do I")`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 660 x 206.2 |
| Padding | 8px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(to right, #ff7759, #7670c5, #4c6ee6) |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #212121 |
| Text node | h5.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #17171c |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.w-full.transition-colors 660.0x206.2 image linear-gradient(to right, #ff7759, #7670c5, #4c6ee6) |
| How | own toggle |

Crops: `faq-item-open-opened.png`.

### North product page

#### north-title

North title. "North 2: Enterprise AI without compromises" — the product page headline.

Page: north. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1128 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CohereText 72px/72px 400 |
| Letter spacing | -1.44px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `north-title-default.png`.

#### north-cta

North CTA. The first ease-button-gradient CTA on the North page; links onward, never followed.

Page: north. Selector: `main a.ease-button-gradient`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146 x 53.2 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17171c | #000000 | = | = |
| Text node | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #17171c | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #000000 | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 142px x 49.2031px, absolute, bg #000000 @ 0 linear-gradient(270deg, #d18ee2, #ff7759), radius 32px | = | = | = |
| Painted layers | a.relative.flex 146.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 142pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = | a.relative.flex 146.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 142pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `north-cta-default.png`, `north-cta-hover.png`, `north-cta-focus-visible.png`, `north-cta-pressed.png`.

### Command model page

#### command-title

Command title. "Secure, production-ready efficiency for agentic intelligence" — the model page headline.

Page: command. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1128 x 216 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CohereText 72px/72px 400 |
| Letter spacing | -1.44px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `command-title-default.png`.

#### command-cta

Command CTA. The first ease-button-gradient CTA on the Command page; links onward, never followed.

Page: command. Selector: `main a.ease-button-gradient`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 185 x 53.2 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17171c | #000000 | = | = |
| Text node | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #17171c | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #000000 | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 181px x 49.2031px, absolute, bg #000000 @ 0 linear-gradient(270deg, #d18ee2, #ff7759), radius 32px | = | = | = |
| Painted layers | a.relative.flex 185.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 181pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = | a.relative.flex 185.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 181pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `command-cta-default.png`, `command-cta-hover.png`, `command-cta-focus-visible.png`, `command-cta-pressed.png`.

### App sign-in (boundary)

#### signin-card

Sign-in card. The dashboard.cohere.com/welcome/login surface: the sign-in card the app paints. Measured at rest, never submitted.

Page: signin. Selector: `main/first visible login container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 566 x 235 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CohereText 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-label.uppercase: CohereMono 12px/16.32px 400, #212121, ls 0.48px |
| Transition | none |
| Painted layers | input.disabled:text-volcanic-700.[-moz-appearance:_textfield] 566.0x60.0 bg #fafafa border T:1px solid #bdbdbd / R:1px solid #bdbdbd / L:1px solid #bdbdbd r 8px 8px 0px 0px; input.disabled:text-volcanic-700.[-moz-appearance:_textfield] 566.0x61.0 bg #fafafa border T:1px solid #bdbdbd / R:1px solid #bdbdbd / B:1px solid #bdbdbd / L:1px solid #bdbdbd r 0px 0px 8px 8px; a.group.cursor-pointer 133.0x26.0 border T:1px solid #000000 @ 0 / B:1px solid #000000 @ 0; span.bg-green-700.h-full 12.0x40.0 bg #39594d r 6px 0px 0px 6px; div.bg-green-700.text-white 56.2x40.0 bg #39594d; span.bg-green-700.h-full 39.4x40.0 bg #39594d r 0px 10px 4px 0px |
| How | at rest |

Crops: `signin-card-default.png`.

#### signin-oauth

OAuth button. A "Continue with" OAuth button on the sign-in card; measured never pressed.

Page: signin. Selector: `button:has-text("Continue with Google")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 281 x 40 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Border | 1px solid #dadce0 | 1px solid #757575 | = | 1px solid #212121 |
| Radius | 4px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #fafafa |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #616161 offset 4px | = |
| Font | CohereText 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #212121 | = | = | = |
| Text node | span.text-p.font-body: CohereText 14px/21px 400, #212121, ls 0.035px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #212121, fill #000000 | = | = | = |
| Painted layers | button.group.items-center 281.0x40.0 bg #ffffff border T:1px solid #dadce0 / R:1px solid #dadce0 / B:1px solid #dadce0 / L:1px solid #dadce0 r 4px | button.group.items-center 281.0x40.0 bg #f5f5f5 border T:1px solid #757575 / R:1px solid #757575 / B:1px solid #757575 / L:1px solid #757575 r 4px | button.group.items-center 281.0x40.0 bg #ffffff border T:1px solid #dadce0 / R:1px solid #dadce0 / B:1px solid #dadce0 / L:1px solid #dadce0 r 4px outline 1px solid #616161 offset 4px | button.group.items-center 281.0x40.0 bg #fafafa border T:1px solid #212121 / R:1px solid #212121 / B:1px solid #212121 / L:1px solid #212121 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-oauth-default.png`, `signin-oauth-hover.png`, `signin-oauth-focus-visible.png`, `signin-oauth-pressed.png`.

#### signin-field

Email field. The sign-in email input — a focus reading only; nothing typed, nothing sent.

Page: signin. Selector: `input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 566 x 60 | = |
| Padding | 28px 12px 10px 12px | = |
| Border | T: 1px solid #bdbdbd; R: 1px solid #bdbdbd; B: none; L: 1px solid #bdbdbd | = |
| Radius | 8px 8px 0px 0px | = |
| Background | #fafafa | = |
| Box shadow | none | = |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | CohereText 14px/21px 400 | = |
| Letter spacing | 0.035px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #9ca3af, opacity 1 | = |
| Painted layers | input.disabled:text-volcanic-700.[-moz-appearance:_textfield] 566.0x60.0 bg #fafafa border T:1px solid #bdbdbd / R:1px solid #bdbdbd / L:1px solid #bdbdbd r 8px 8px 0px 0px | input.disabled:text-volcanic-700.[-moz-appearance:_textfield] 566.0x60.0 bg #fafafa border T:1px solid #bdbdbd / R:1px solid #bdbdbd / L:1px solid #bdbdbd r 8px 8px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `signin-field-default.png`, `signin-field-focused.png`.

#### signin-submit

Log-in button. The "Log in" submit on the sign-in card; measured never pressed — it would submit the form.

Page: signin. Selector: `button:has-text("Log in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130.22 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | CohereText 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-p.font-body: CohereText 14px/21px 400, #fafafa, ls 0.035px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.bg-green-700.h-full 12.0x40.0 bg #39594d r 6px 0px 0px 6px; div.bg-green-700.text-white 56.2x40.0 bg #39594d; span.bg-green-700.h-full 39.4x40.0 bg #39594d r 0px 10px 4px 0px; span.bg-green-700.h-full 39.4x40.0 bg #39594d r 4px 0px 0px 10px; div.bg-green-700.text-white 16.0x40.0 bg #39594d; span.bg-green-700.h-full 12.0x40.0 bg #39594d r 0px 6px 6px 0px | span.bg-green-900.h-full 12.0x40.0 bg #16211c r 6px 0px 0px 6px; div.bg-green-900.text-white 40.2x40.0 bg #16211c; span.bg-green-900.h-full 39.4x40.0 bg #16211c r 0px 10px 4px 0px; span.bg-green-900.h-full 39.4x40.0 bg #16211c r 4px 0px 0px 10px; div.bg-green-900.text-white 32.0x40.0 bg #16211c; span.bg-green-900.h-full 12.0x40.0 bg #16211c r 0px 6px 6px 0px | button.mt-10.w-full 130.2x40.0 outline 2px solid #000000 @ 0 offset 2px; span.bg-green-700.h-full 12.0x40.0 bg #39594d r 6px 0px 0px 6px; div.bg-green-700.text-white 56.2x40.0 bg #39594d; span.bg-green-700.h-full 39.4x40.0 bg #39594d r 0px 10px 4px 0px; span.bg-green-700.h-full 39.4x40.0 bg #39594d r 4px 0px 0px 10px; div.bg-green-700.text-white 16.0x40.0 bg #39594d | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-submit-default.png`, `signin-submit-hover.png`, `signin-submit-focus-visible.png`, `signin-submit-pressed.png`.

### Footer

#### footer

Footer. The dark footer band (bg near-black): link columns (Platforms/Models/…), social icons and the legal row; the certification strip sits just above it on the home page.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1430.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.text-web3-32-heading.lg:text-web3-60: CohereText 60px/60px 400, #ffffff, ls -1.2px |
| Transition | none |
| Painted layers | section.relative.px-4 1440.0x600.0 bg #355146; a.relative.flex 185.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 181pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px; section.relative.w-full 1440.0x830.4 bg #17171c; li.w-full.border-b 0.0x0.0 border B:1px solid #525260; li.w-full.border-b 0.0x0.0 border B:1px solid #525260 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A link in a footer link column (group/footer-link text-white, inside the lg:flex desktop block; the md:hidden accordion copies measure 0x0).

Page: home. Selector: `footer .lg\:flex a.group/footer-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 19.59 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | p.text-web3-14.font-body: Unica77 Cohere Web 14px/19.6px 400, #fafafa | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group/footer-link.inline-flex 36.0x19.6 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link. A footer social icon (LinkedIn/X) — the img inside the social anchor.

Page: home. Selector: `footer img[alt=LinkedIn/X]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #212121 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-pressed.png`.

#### footer-cta

Footer CTA. The footer "Request a demo" ease-button-gradient pill; links to the contact form, never followed.

Page: home. Selector: `footer a.ease-button-gradient`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 185 x 53.2 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #17171c | = | = | = |
| Text node | span.text-web3-16.lg:text-web3-18: Unica77 Cohere Web 18px/25.2px 400, #17171c | = | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 181px x 49.2031px, absolute, bg #000000 @ 0 linear-gradient(270deg, #d18ee2, #ff7759), radius 32px | = | = | = |
| Painted layers | a.relative.flex 185.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 181pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = | a.relative.flex 185.0x53.2 bg #ffffff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px, #4c6ee6 0px 0px 0px 4px, #ffffff 0px 0px 0px 6px outline 2px solid #000000 @ 0 offset 2px; a::before.relative.flex 181pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-cta-default.png`, `footer-cta-hover.png`, `footer-cta-focus-visible.png`, `footer-cta-pressed.png`.

#### footer-badge

Trust badge. A certification badge anchor in the compliance strip on the home page (SOC2/GDPR/ISO/CCPA, w-[120px]).

Page: home. Selector: `a[aria-label=SOC2/GDPR/ISO]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 120 x 139.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-web3-14.font-body: Unica77 Cohere Web 14px/19.6px 400, #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.flex.w-[120px] 120.0x139.6 outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `footer-badge-default.png`.

### Mobile (390 wide)

#### m-header

Mobile bar. The 390 mobile nav bar (aria-label="Mobile navigation"): logo + menu toggle; the desktop nav unmounts to 0x0 at this width.

Page: home. Selector: `nav[aria-label="Mobile navigation"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | transform, background-color, color 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | nav.z-nav.flex 390.0x60.0 bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger (aria-label="Open navigation menu"); its own press opens the drawer.

Page: home. Selector: `button[aria-label="Open navigation menu"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up nav.z-nav.flex bg #ffffff |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The menu overlay after the hamburger press (min-h-[100vh] bg-black/20 backdrop-blur scrim + panel).

Page: home. Selector: `opened mobile menu overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 682.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Unica77 Cohere Web 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.text-web3-24-heading.lg:text-web3-32: Unica77 Cohere Web 24px/28.8px 400, #000000 |
| Transition | clip-path 0.5s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.group/navContent.fixed 390.0x682.6 bg #ffffff; a.!w-full.whitespace-nowrap 358.0x51.2 border T:1px solid #17171c / R:1px solid #17171c / B:1px solid #17171c / L:1px solid #17171c r 9999px outline 2px solid #000000 @ 0 offset 2px; a.!w-full.whitespace-nowrap 358.0x53.2 bg #17171c border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a::before.!w-full.whitespace-nowrap 354pxx49.2031px image linear-gradient(270deg, #d18ee2, #ff7759) r 32px; hr.mx-4.h-px 0.0x0.0 bg #f2f2f2; hr.mx-4.h-px 0.0x0.0 bg #f2f2f2 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-link

Menu link. A link/accordion row inside the open mobile menu (min-h-[44px] rows).

Page: home. Selector: `first row inside the open menu`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | Unica77 Cohere Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.text-web3-24-heading.lg:text-web3-32: Unica77 Cohere Web 24px/28.8px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.min-h-[44px] 358.0x44.0 outline 1px auto #e59700 offset 0px | = |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile headline. The hero headline at 390.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CohereText 60px/60px 400 |
| Letter spacing | -1.2px |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `opacity 0.5s ease-out`, `width 0.1s linear`, `opacity 1.5s ease-in`, `opacity 0.2s ease-in-out`, `max-width 0.2s ease-in-out`, `0.35s ease-in-out`, `opacity 0.35s ease-in-out`, `0.3s`, `border-color 0.2s`, `0.2s`, `transform 0.3s`, `background-color 0.2s, border-color 0.2s`
