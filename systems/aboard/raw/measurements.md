# Component measurements

Computed styles read from aboard.com on 2026-11-09 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-bar

Top navigation bar. The fixed 78px header: the Aboard wordmark, the section links (How We Work / Case Studies / Foundry / Perspectives / About) and the boxed "Get in Touch" CTA.

Page: home. Selector: `header.site-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 78 |
| Padding | 18px 56px 0px 56px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #271503 |
| Text node | a: Work Sans 15.04px/24.064px 400, #271503 |
| Transition | none |
| Icon | 107.05 x 26, colour #271503 |
| Painted layers | nav::before.rd-nav.rd-focus-nav 1328pxx60px bg #f0f1ef @ 0.84 r 999px; a::after 9pxx9px bg #271503; ul.sub-menu 210.0x223.7 bg #faf5ef @ 0.97 r 14px shadow #271503 @ 0.18 0px 14px 34px -22px; a::after 9pxx9px bg #271503; ul.sub-menu 210.0x140.6 bg #faf5ef @ 0.97 r 14px shadow #271503 @ 0.18 0px 14px 34px -22px; a.rd-nav-cta 157.3x42.0 bg #de4c00 r 999px |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-logo

Logo. The Aboard wordmark linking home.

Page: home. Selector: `a.aboard-logo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 107.05 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #271503 offset 2px | = |
| Font | Work Sans 16px/25.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #271503 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 107.05 x 26, colour #271503 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.aboard-logo.rd-nav-logo 107.0x26.0 r 2px outline 2px solid #271503 offset 2px | = |

Crops: `nav-logo-default.png`, `nav-logo-hover.png`, `nav-logo-focus-visible.png`, `nav-logo-pressed.png`.

#### nav-link

Nav link. A section link in the top bar.

Page: home. Selector: `nav.rd-nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 129.73 x 42.06 | = | = | = |
| Padding | 9px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | transparent | #808080 @ 0.16 | #808080 @ 0.16 | #808080 @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #271503 offset 2px | = |
| Font | Work Sans 15.04px/24.064px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #271503 | = | = | = |
| Transition | background 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a 129.7x42.1 bg #808080 @ 0.16 r 999px | a 129.7x42.1 bg #808080 @ 0.16 r 999px outline 2px solid #271503 offset 2px | a 129.7x42.1 bg #808080 @ 0.16 r 999px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-cta

Get-in-touch CTA. The boxed "Get in Touch" button at the right of the nav; jumps to the contact section. Hovered and focused only.

Page: home. Selector: `a.rd-nav-cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 157.31 x 42 | = | = | = |
| Padding | 5px 5px 5px 18px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #de4c00 | #291503 | = | #321803 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #271503 offset 2px | = |
| Font | Work Sans 14.72px/23.552px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffefb | = | = | = |
| Transition | background, color 0.5s, 0.5s cubic-bezier(0.65, 0, 0.35, 1), cubic-bezier(0.65, 0, 0.35, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13 x 13, colour #fffefb | = | = | = |
| Painted layers | a.rd-nav-cta 157.3x42.0 bg #de4c00 r 999px; span.rd-nav-cta-ico 32.0x32.0 bg #ffffff @ 0.2 r 50% | a.rd-nav-cta 157.3x42.0 bg #291503 r 999px; span.rd-nav-cta-ico 32.0x32.0 bg #ffffff @ 0.2 r 50% | a.rd-nav-cta 157.3x42.0 bg #de4c00 r 999px outline 2px solid #271503 offset 2px; span.rd-nav-cta-ico 32.0x32.0 bg #ffffff @ 0.2 r 50% | a.rd-nav-cta 157.3x42.0 bg #321803 r 999px; span.rd-nav-cta-ico 32.0x32.0 bg #ffffff @ 0.2 r 50% |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### skip-link

Skip link. The fixed "Skip to content" link, offscreen until focused.

Page: home. Selector: `a.rd-skip-link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 153.3 x 45.59 |
| Padding | 10px 16px |
| Border | none |
| Radius | 0px |
| Background | #271503 |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.rd-skip-link 153.3x45.6 bg #271503 |
| Ancestor paint | 1 up body.home.wp-singular bg #fffefb |
| How | at rest |

Crops: none.

#### footer

Footer. The bright-citrus footer: "We Can Help" display heading, the newsletter-signup iframe, link columns, the legal row and the social links.

Page: home. Selector: `footer.rd`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1237.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #de4c00 |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #fffefb |
| Text node | h2.font-rd-serif.text-rd-footer-h: Tobias 32px/35.2px 300, #fffefb, ls -0.32px |
| Transition | none |
| Painted layers | footer.rd.rd-focus-on-orange 1440.0x1237.8 bg #de4c00; div.block-contact-form.bg-bright-citrus 1120.0x442.2 bg #de4c00; div.relative.overflow-hidden 1440.0x555.6 border T:1px solid #fffefb @ 0.3; hr.w-full.border-t 101.5x1.0 border T:1px solid #fffefb @ 0.3; hr.w-full.border-t 98.6x1.0 border T:1px solid #fffefb @ 0.3; hr.w-full.border-t 67.4x1.0 border T:1px solid #fffefb @ 0.3 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-heading

Footer heading. "We Can Help" — the serif display heading of the citrus footer.

Page: home. Selector: `h2.text-rd-footer-h`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 178.25 x 35.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 32px/35.2px 300 |
| Letter spacing | -0.32px |
| Colour | #fffefb |
| Transition | none |
| How | at rest |

Crops: `footer-heading-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.47 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #fffefb offset 4px | = |
| Font | Work Sans 15px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffefb | #f3d9c8 | = | #f3d9c8 |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-off-white.transition-[color] 101.5x18.0 r 2px outline 2px solid #fffefb offset 4px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link. A social link in the footer column (LinkedIn New York / Lebanon, YouTube, Instagram, Facebook, X).

Page: home. Selector: `footer social link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149.5 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #fffefb offset 4px | = |
| Font | Work Sans 15px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffefb | #f3d9c8 | = | #f3d9c8 |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-off-white.transition-[color] 149.5x18.0 r 2px outline 2px solid #fffefb offset 4px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

### Home

#### hero-title

Hero title. "Your partner for the big AI leap" — the display headline, per-word animated (rd-words).

Page: home. Selector: `h1.rd-words`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 933.11 x 155.53 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 77.76px/77.76px 400 |
| Letter spacing | -1.5552px |
| Colour | #271503 |
| Text node | span: Tobias 77.76px/77.76px 400, #271503, ls -1.5552px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### eyebrow

Eyebrow label. A small caps section label ("WHAT WE DO", "PERSPECTIVES").

Page: home. Selector: `p.rd-eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 435.19 x 20.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 12.8px/20.48px 600 |
| Letter spacing | 1.92px |
| Colour | #766757 |
| Transition | none |
| How | at rest |

Crops: `eyebrow-default.png`.

#### section-title

Section title. A section heading ("Your roadmap, realized", "We've got opinions").

Page: home. Selector: `h2.text-rd-h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 421.55 x 229.08 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 74.88px/76.3776px 400 |
| Letter spacing | -1.4976px |
| Colour | #271503 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### feed-row

Feed row. A content row in the home feed: kind tag, title and date in a three-column grid (EVENT / NEWSLETTER / PODCAST).

Page: home. Selector: `a.rd-feed-row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1328 x 242.39 | = |
| Padding | 24px 0px | = |
| Gap | 43.2px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Work Sans 16px/25.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #271503 | = |
| Text node | span.rd-meta.inline-flex: Work Sans 11.52px/18.432px 600, #271503, ls 1.6128px | = |
| Transition | transform 0.6s cubic-bezier(0.32, 0.72, 0, 1) | = |
| Cursor | pointer | = |
| Icon | 13 x 13, colour #de4c00 | = |
| Painted layers | span.relative.aspect-[4/3] 259.2x194.4 bg #efe7db r 12px | = |
| How | at rest | mouse hover |
| Transform | - | matrix(1, 0, 0, 1, 7.93877, 0) |

Crops: `feed-row-default.png`, `feed-row-hover.png`.

#### feed-row-tag

Feed row kind tag. The small caps kind label on a feed row.

Page: home. Selector: `rd-feed-row kind`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 525.48 x 18.42 |
| Padding | 0px |
| Gap | 7px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 11.52px/18.432px 600 |
| Letter spacing | 1.6128px |
| Colour | #271503 |
| Transition | none |
| Cursor | pointer |
| Icon | 13 x 13, colour #de4c00 |
| How | at rest |

Crops: `feed-row-tag-default.png`.

#### carousel-tick

Carousel tick. A pagination tick of the home media carousel (cc-*); is-on marks the current one.

Page: home. Selector: `button.cc-tick`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 35 x 20 | = | = | = |
| Padding | 9px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Work Sans 16px/25.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffefb | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | i 35.0x2.0 bg #fffefb @ 0.3 r 2px; i::after 35pxx2px bg #fffefb | = | i 35.0x2.0 bg #fffefb @ 0.3 r 2px outline 2px solid #ffffff offset 3px; i::after 35pxx2px bg #fffefb | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-tick-default.png`, `carousel-tick-hover.png`, `carousel-tick-focus-visible.png`, `carousel-tick-pressed.png`.

#### carousel-pause

Carousel pause. The carousel's pause control.

Page: home. Selector: `button.cc-pause`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 28 x 28 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Work Sans 16px/25.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #fffefb @ 0.85 | #ffffff |
| Transition | color 0.3s ease | = |
| Cursor | pointer | = |
| Icon | 14 x 14, colour #fffefb @ 0.85, fill #000000 | 14 x 14, colour #ffffff, fill #000000 |
| How | at rest | mouse hover |

Crops: `carousel-pause-default.png`, `carousel-pause-hover.png`.

#### contact-iframe

Contact iframe. The embedded form frame in the contact section (same-origin newsletter signup). Measured as a frame; the fields inside live under Newsletter signup.

Page: home. Selector: `iframe[src*=contact-form]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1120 x 375 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #fffefb |
| Transition | none |
| Ancestor paint | 1 up div.block-contact-form.bg-bright-citrus bg #de4c00 |
| How | at rest |

Crops: `contact-iframe-default.png`.

### Consent overlay

#### cookie-bar

Cookie consent strip. The CookieYes strip pinned at the bottom: "We use cookies..." copy with Customize and Accept All. Re-shown for the measurement, never answered.

Page: home. Selector: `.cky-consent-container`. States: .

Not found on the page at capture time.

#### cookie-accept

Accept-all button. The "Accept All" button of the consent strip. Measured in every state — never pressed (it would post consent).

Page: home. Selector: `button.cky-btn-accept`. States: .

Not found on the page at capture time.

#### cookie-customize

Customize button. The "Customize" button, which opens the preferences modal. Measured, never pressed.

Page: home. Selector: `button.cky-btn-customize`. States: .

Not found on the page at capture time.

#### cookie-close

Consent close button. The small close control of the consent strip. Measured, never pressed.

Page: home. Selector: `button.cky-btn-close`. States: .

Not found on the page at capture time.

### How We Work

#### hww-title

Page title. "95% of AI software initiatives fail. Why do ours ship?" — the interior display headline.

Page: how-we-work. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000.08 x 372.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 95.04px/93.1392px 400 |
| Letter spacing | -1.9008px |
| Colour | #06070a |
| Text node | span: Tobias 95.04px/93.1392px 400, #06070a, ls -1.9008px |
| Transition | none |
| Painted layers | i.hww-strike 482.6x6.6 bg #de4c00 r 3.8016px |
| How | at rest |

Crops: `hww-title-default.png`.

#### hww-card

Principle card heading. A principle card heading ("We evolved the process").

Page: how-we-work. Selector: `h3.text-rd-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656.16 x 34.77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 30.24px/34.776px 400 |
| Letter spacing | -0.6048px |
| Colour | #06070a |
| Transition | none |
| How | at rest |

Crops: `hww-card-default.png`.

#### hww-step

Process step. A step of the Landscape → Audit → Blueprint → Architecture → Migrate process row.

Page: how-we-work. Selector: `h3 process step`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 541.52 x 51.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 51.2px/51.2px 400 |
| Letter spacing | -1.024px |
| Colour | #06070a |
| Transition | none |
| How | at rest |

Crops: `hww-step-default.png`.

#### hww-body

Body text.

Page: how-we-work. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 312.25 x 77.77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 17.28px/25.92px 400 |
| Letter spacing | normal |
| Colour | #3d3a36 |
| Transition | none |
| How | at rest |

Crops: `hww-body-default.png`.

### Case studies

#### cases-title

Page title.

Page: case-studies. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 988.08 x 232.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 123.84px/116.41px 400 |
| Letter spacing | -4.3344px |
| Colour | #271503 |
| Transition | none |
| How | at rest |

Crops: `cases-title-default.png`.

#### case-card-feature

Featured case card. The lead case-study card (the full-width SageSure feature).

Page: case-studies. Selector: `a.rd-case-feature`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1328 x 703.02 | = |
| Padding | 30px 0px 0px 0px | = |
| Gap | 30px normal | = |
| Border | T: 1px solid #271503 @ 0.114; R: none; B: none; L: none | T: 1px solid #271503 @ 0.1; R: none; B: none; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Work Sans 16px/25.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #271503 | = |
| Text node | span.leading-[1.1]: Work Sans 11.52px/12.672px 400, #766757, ls 2.304px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.rd-case.rd-case-feature 1328.0x703.0 border T:1px solid #271503 @ 0.114; figure.rd-case-figure.relative 1328.0x569.1 bg #808080 @ 0.12 r 12px shadow #000000 @ 0 0px 40px 80px -48px; div.tb.is-live 1328.0x569.1 bg #1a110a; div.tb-shade 1328.0x996.0 image linear-gradient(#000000 @ 0.08, #000000 @ 0.08 40%, #000000 @ 0.42); i 0.0x0.0 bg #1f8a5b r 50% shadow #ffffff @ 0.95 0px 0px 0px 2.8457px, #000000 @ 0.4 0px 2px 8px 0px; i::after 20.4531pxx20.4531px border T:1px solid #1f8a5b / R:1px solid #1f8a5b / B:1px solid #1f8a5b / L:1px solid #1f8a5b r 50% | a.rd-case.rd-case-feature 1328.0x703.0 border T:1px solid #271503 @ 0.1; figure.rd-case-figure.relative 1328.0x569.1 bg #808080 @ 0.12 r 12px shadow #000000 @ 0.537 0px 40px 80px -48px; div.tb.is-live 1328.0x569.1 bg #1a110a; div.tb-shade 1328.0x996.0 image linear-gradient(#000000 @ 0.08, #000000 @ 0.08 40%, #000000 @ 0.42); i 10.2x10.2 bg #1f8a5b r 50% shadow #ffffff @ 0.95 0px 0px 0px 2.8457px, #000000 @ 0.4 0px 2px 8px 0px; i::after 20.4531pxx20.4531px border T:1px solid #1f8a5b / R:1px solid #1f8a5b / B:1px solid #1f8a5b / L:1px solid #1f8a5b r 50% |
| How | at rest | mouse hover |

Crops: `case-card-feature-default.png`, `case-card-feature-hover.png`.

#### case-card

Case card. A case-study card in the grid: industry tag, title, client.

Page: case-studies. Selector: `a.rd-case`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 632.31 x 599.17 | = |
| Padding | 30px 0px 0px 0px | = |
| Gap | 30px normal | = |
| Border | T: 1px solid #271503 @ 0.1; R: none; B: none; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Work Sans 16px/25.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #271503 | = |
| Text node | span.leading-[1.1]: Work Sans 11.52px/12.672px 400, #766757, ls 2.304px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 11.23 x 11.23, colour #2a2a33, fill #ffffff | 12.15 x 12.15, colour #2a2a33, fill #ffffff |
| Painted layers | a.rd-case.group 632.3x599.2 border T:1px solid #271503 @ 0.1; figure.rd-case-figure.relative 632.3x474.2 bg #808080 @ 0.12 r 12px shadow #000000 @ 0 0px 40px 80px -48px; div.tb.is-live 632.3x474.2 bg #1a110a; div.tb-shade 711.3x474.2 image linear-gradient(#000000 @ 0.06, #000000 @ 0 40%, #140a28 @ 0.4); div.tb-ins 200.7x98.1 bg #ffffff @ 0.97 r 7.58775px shadow #000000 @ 0.55 0px 20px 50px -16px; span.tb-spark 20.1x20.1 image linear-gradient(135deg, #ffb347, #ff5f6d 45%, #a855f7) r 50% shadow #a855f7 @ 0.6 0px 4px 12px -4px | a.rd-case.group 632.3x599.2 border T:1px solid #271503 @ 0.1; figure.rd-case-figure.relative 632.3x474.2 bg #808080 @ 0.12 r 12px shadow #000000 @ 0.537 0px 40px 80px -48px; div.tb.is-live 632.3x474.2 bg #1a110a; div.tb-shade 711.3x474.2 image linear-gradient(#000000 @ 0.06, #000000 @ 0 40%, #140a28 @ 0.4); div.tb-ins 217.3x106.2 bg #ffffff @ 0.97 r 7.58775px shadow #000000 @ 0.55 0px 20px 50px -16px; span.tb-spark 21.7x21.7 image linear-gradient(135deg, #ffb347, #ff5f6d 45%, #a855f7) r 50% shadow #a855f7 @ 0.6 0px 4px 12px -4px |
| How | at rest | mouse hover |

Crops: `case-card-default.png`, `case-card-hover.png`.

#### case-tag

Case industry tag. The small caps industry label on a case card.

Page: case-studies. Selector: `rd-case tag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 87.13 x 12.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 11.52px/12.672px 400 |
| Letter spacing | 2.304px |
| Colour | #766757 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `case-tag-default.png`.

#### cs-title

Case study title. "City of Boston" detail page title.

Page: case-study. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 988.09 x 120.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 59.04px/60.2208px 400 |
| Letter spacing | -1.476px |
| Colour | #271503 |
| Text node | span: Tobias 59.04px/60.2208px 400, #271503, ls -1.476px |
| Transition | none |
| How | at rest |

Crops: `cs-title-default.png`.

#### cs-body

Case study body.

Page: case-study. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 691.19 x 96.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 23.04px/32.256px 400 |
| Letter spacing | normal |
| Colour | #271503 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `cs-body-default.png`.

#### cs-meta

Case study meta. The detail page's fact labels (client, sector, platform).

Page: case-study. Selector: `case meta`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308.23 x 18.55 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 12.8px/18.56px 500 |
| Letter spacing | normal |
| Colour | #766757 |
| Transition | none |
| How | at rest |

Crops: `cs-meta-default.png`.

### Foundry

#### foundry-title

Page title. "Software we build for ourselves" — the Foundry page title.

Page: foundry. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 574.41 x 84.67 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 86.4px/84.672px 400 |
| Letter spacing | -2.592px |
| Colour | #06070a |
| Text node | span: Tobias 86.4px/84.672px 400, #06070a, ls -2.592px |
| Transition | none |
| How | at rest |

Crops: `foundry-title-default.png`.

#### foundry-card

Foundry product card. A Foundry product card (Aboard Sign, TinyLittleOffice).

Page: foundry. Selector: `foundry product card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1440 x 6600.69 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h2: Tobias 69.12px/67.7376px 400, #06070a, ls -2.0736px | = |
| Transition | none | = |
| Icon | 14 x 14, colour #ffffff | = |
| Painted layers | section.rd.rd-fd-proj 1440.0x1530.2 bg #ffffff border T:1px solid #06070a @ 0.1; a.btn.btn-rd 224.6x46.6 bg #06070a r 999px; ul.rd-fd-meta 770.8x53.6 border T:1px solid #06070a @ 0.1; details.rd-fd-tech 770.8x63.2 border T:1px solid #06070a @ 0.1 / B:1px solid #06070a @ 0.1; i::before 14pxx1.5px bg #06070a; i::after 14pxx1.5px bg #06070a | = |
| How | at rest | mouse hover |

Crops: `foundry-card-default.png`, `foundry-card-hover.png`.

### Feeds: perspectives, newsletter, events, media

#### perspectives-title

Page title.

Page: perspectives. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 541.52 x 73.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #06070a |
| Text node | span: Tobias 72px/73.44px 400, #06070a, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `perspectives-title-default.png`.

#### perspectives-row

Index row. A content row/card on the index (date, title, thumbnail).

Page: perspectives. Selector: `feed row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1344 x 242.39 | = |
| Padding | 24px 0px | = |
| Gap | 43.2px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Work Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #06070a | = |
| Text node | span.rd-meta.inline-flex: Work Sans 11.52px/17.28px 600, #06070a, ls 1.6128px | = |
| Transition | transform 0.6s cubic-bezier(0.32, 0.72, 0, 1) | = |
| Cursor | pointer | = |
| Icon | 13 x 13, colour #de4c00 | = |
| Painted layers | span.relative.aspect-[4/3] 259.2x194.4 bg #efe7db r 12px | = |
| How | at rest | mouse hover |
| Transform | - | matrix(1, 0, 0, 1, 7.9388, 0) |

Crops: `perspectives-row-default.png`, `perspectives-row-hover.png`.

#### perspectives-row-title

Row title.

Page: perspectives. Selector: `row title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 534.05 x 32.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 28.8px/32.256px 400 |
| Letter spacing | -0.576px |
| Colour | #06070a |
| Transition | color 0.3s ease |
| Cursor | pointer |
| How | at rest |

Crops: `perspectives-row-title-default.png`.

#### newsletter-title

Page title.

Page: newsletter. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656.16 x 146.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #fbf3ec |
| Text node | span: Tobias 72px/73.44px 400, #fbf3ec, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `newsletter-title-default.png`.

#### newsletter-row

Index row. A content row/card on the index (date, title, thumbnail).

Page: newsletter. Selector: `feed row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1344 x 267.52 | = |
| Padding | 28px 0px | = |
| Gap | 37.44px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Work Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #06070a | = |
| Text node | time.font-rd-sans.text-[0.74rem]: Work Sans 11.84px/17.76px 600, #6f6a63, ls 1.8944px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.aspect-[3/2].overflow-hidden 317.3x211.5 bg #f5f4f1 r 10px | = |
| How | at rest | mouse hover |

Crops: `newsletter-row-default.png`, `newsletter-row-hover.png`.

#### newsletter-row-title

Row title.

Page: newsletter. Selector: `row title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 740.31 x 34.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 31.68px/34.848px 300 |
| Letter spacing | -0.3168px |
| Colour | #06070a |
| Transition | color 0.4s ease |
| Cursor | pointer |
| How | at rest |

Crops: `newsletter-row-title-default.png`.

#### events-title

Page title.

Page: events. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000.08 x 73.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #06070a |
| Text node | span: Tobias 72px/73.44px 400, #06070a, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `events-title-default.png`.

#### events-row

Index row. A content row/card on the index (date, title, thumbnail).

Page: events. Selector: `feed row`. States: .

Not found on the page at capture time.

#### events-row-title

Row title.

Page: events. Selector: `row title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 543.22 x 39.67 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 37.44px/39.6864px 400 |
| Letter spacing | -0.5616px |
| Colour | #06070a |
| Transition | none |
| How | at rest |

Crops: `events-row-title-default.png`.

#### event-row

Event row. An office-hours/event row with its date.

Page: events. Selector: `event row`. States: .

Not found on the page at capture time.

#### media-title

Page title.

Page: media. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000.08 x 73.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #06070a |
| Text node | span: Tobias 72px/73.44px 400, #06070a, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `media-title-default.png`.

#### media-row

Index row. A content row/card on the index (date, title, thumbnail).

Page: media. Selector: `feed row`. States: .

Not found on the page at capture time.

#### media-row-title

Row title.

Page: media. Selector: `row title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 459.42 x 143.72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 46.08px/47.9232px 400 |
| Letter spacing | -0.9216px |
| Colour | #06070a |
| Transition | color 0.4s ease |
| Cursor | pointer |
| How | at rest |

Crops: `media-row-title-default.png`.

### Newsletter signup (resting only)

#### nl-form

Newsletter form. The "Email address + Subscribe" signup (dark variant on the newsletter page). Posts to /wp-json/aboard/v1/newsletter-signups — measured at rest, never submitted.

Page: newsletter. Selector: `form.rd-nl-form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 541.52 x 84.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #06070a |
| Text node | button: Work Sans 15.04px/15.04px 500, #fffefb |
| Transition | none |
| Icon | 14 x 14, colour #fffefb |
| Painted layers | input 379.3x50.0 bg #fbf2ea @ 0.08 border T:1px solid #e9decd @ 0.28 / R:1px solid #e9decd @ 0.28 / B:1px solid #e9decd @ 0.28 / L:1px solid #e9decd @ 0.28 r 999px; button 152.2x50.0 bg #de4c00 r 999px; span.rd-nl-form-ico 40.0x40.0 bg #ffffff @ 0.16 r 50%; input 0.0x0.0 bg #ffffff |
| How | at rest |

Crops: `nl-form-default.png`.

#### nl-field

Newsletter email field. The email input. Clicked into for the focus style; nothing typed.

Page: newsletter. Selector: `input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 379.33 x 50 | = |
| Padding | 0px 20px | = |
| Border | 1px solid #e9decd @ 0.28 | 1px solid #e67940 |
| Radius | 999px | = |
| Background | #fbf2ea @ 0.08 | = |
| Box shadow | none | #e67940 @ 0.25 0px 0px 0px 3px |
| Outline | none | = |
| Font | Work Sans 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #fbf3ec | = |
| Transition | border-color, box-shadow 0.3s, 0.3s ease, ease delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #e9decd @ 0.6, opacity 1 | = |
| Painted layers | input 379.3x50.0 bg #fbf2ea @ 0.08 border T:1px solid #e9decd @ 0.28 / R:1px solid #e9decd @ 0.28 / B:1px solid #e9decd @ 0.28 / L:1px solid #e9decd @ 0.28 r 999px | input 379.3x50.0 bg #fbf2ea @ 0.08 border T:1px solid #e67940 / R:1px solid #e67940 / B:1px solid #e67940 / L:1px solid #e67940 r 999px shadow #e67940 @ 0.25 0px 0px 0px 3px |
| How | at rest | clicked into the field |

Crops: `nl-field-default.png`, `nl-field-focused.png`.

#### nl-submit

Subscribe button. The Subscribe submit. Measured in every state — never pressed.

Page: newsletter. Selector: `newsletter submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152.19 x 50 | = | = | 149.14 x 49 |
| Padding | 5px 5px 5px 22px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #de4c00 | #c44300 | = | #c44300 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #e67940 offset 3px | = |
| Font | Work Sans 15.04px/15.04px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fffefb | = | = | = |
| Transition | background, transform 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #fffefb | = | = | 13.72 x 13.72, colour #fffefb |
| Painted layers | button 152.2x50.0 bg #de4c00 r 999px; span.rd-nl-form-ico 40.0x40.0 bg #ffffff @ 0.16 r 50% | button 152.2x50.0 bg #c44300 r 999px; span.rd-nl-form-ico 40.0x40.0 bg #ffffff @ 0.16 r 50% | button 152.2x50.0 bg #de4c00 r 999px outline 2px solid #e67940 offset 3px; span.rd-nl-form-ico 40.0x40.0 bg #ffffff @ 0.16 r 50% | button 149.1x49.0 bg #c44300 r 999px; span.rd-nl-form-ico 39.2x39.2 bg #ffffff @ 0.16 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `nl-submit-default.png`, `nl-submit-hover.png`, `nl-submit-focus-visible.png`, `nl-submit-pressed.png`.

#### nl-latest-title

Latest issue title. "Meet Aboard Sign" — the latest-issue headline.

Page: newsletter. Selector: `.rd-nl-latest-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 412.61 x 57.27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 56.16px/57.2832px 400 |
| Letter spacing | -1.1232px |
| Colour | #06070a |
| Transition | color 0.4s ease |
| Cursor | pointer |
| How | at rest |

Crops: `nl-latest-title-default.png`.

#### nl-form-card

Newsletter card form. The boxed variant of the signup (is-card) under the article.

Page: aboard-sign. Selector: `form.rd-nl-form.is-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 81.94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 17.28px/25.92px 400 |
| Letter spacing | normal |
| Colour | #06070a |
| Text node | button: Work Sans 15.04px/15.04px 500, #ffffff |
| Transition | none |
| Icon | 14 x 14, colour #ffffff |
| Painted layers | input 397.8x50.0 bg #fffefb border T:1px solid #06070a @ 0.1 / R:1px solid #06070a @ 0.1 / B:1px solid #06070a @ 0.1 / L:1px solid #06070a @ 0.1 r 999px; button 152.2x50.0 bg #06070a r 999px; span.rd-nl-form-ico 40.0x40.0 bg #ffffff @ 0.16 r 50%; input 0.0x0.0 bg #ffffff |
| How | at rest |

Crops: `nl-form-card-default.png`.

### Podcast

#### pod-title

Podcast title. The latest-episode headline in cream on the dark podcast section.

Page: podcast. Selector: `h1 / .rd-pd-latest-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 770.8 x 76.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #fbf3ec |
| Text node | span: Tobias 72px/73.44px 400, #fbf3ec, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `pod-title-default.png`.

#### pod-ep-title

Episode title. An episode row title ("Allison Fine: Making AI-Driven Change Less Scary").

Page: podcast. Selector: `h3.rd-pd-ep-title`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1084.91 x 32.25 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Tobias 28.8px/32.256px 300 | = |
| Letter spacing | -0.288px | = |
| Colour | #fbf3ec | = |
| Transition | color 0.3s ease | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `pod-ep-title-default.png`, `pod-ep-title-hover.png`.

#### pod-ep-row

Episode row. An episode row in the index.

Page: podcast. Selector: `episode row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1084.91 x 112.08 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Work Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #eadfcf | = |
| Text node | h3.rd-pd-ep-title: Tobias 28.8px/32.256px 300, #fbf3ec, ls -0.288px | h3.rd-pd-ep-title: Tobias 28.8px/32.256px 300, #e67940, ls -0.288px |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `pod-ep-row-default.png`, `pod-ep-row-hover.png`.

#### pod-seek

Player seek bar. The range input of the podcast dock player. Measured at rest, never dragged.

Page: podcast. Selector: `input.rd-pd-dock-seek`. States: .

Not found on the page at capture time.

#### pod-play

Player button. A dock-player transport button. Measured, never pressed (it would play).

Page: podcast. Selector: `dock player button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 340 x 340 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | #0b2050 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Work Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #eadfcf | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.rd-pd-art.max-[900px]:max-w-[420px] 340.0x340.0 bg #0b2050 r 10px | = |
| Ancestor paint | 1 up div.rd-pd-latest bg #00040f @ 0.42 shadow #e9decd @ 0.16 0px 0px 0px 1px inset | = |
| How | at rest | mouse hover |

Crops: `pod-play-default.png`, `pod-play-hover.png`.

#### pe-title

Episode page title.

Page: podcast-episode. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656.16 x 220.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #fbf3ec |
| Text node | span: Tobias 72px/73.44px 400, #fbf3ec, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `pe-title-default.png`.

#### pe-body

Episode body.

Page: podcast-episode. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 217.05 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 24px/36px 400 |
| Letter spacing | 0.48px |
| Colour | #fbf3ec |
| Transition | none |
| How | at rest |

Crops: `pe-body-default.png`.

### About, careers, security

#### about-title

About title.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000.08 x 220.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #06070a |
| Text node | span: Tobias 72px/73.44px 400, #06070a, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `about-title-default.png`.

#### about-body

about body text.

Page: about. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 770.8 x 263.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 63.36px/65.8944px 300 |
| Letter spacing | -1.39392px |
| Colour | #06070a |
| Text node | span.pq-word.is-lit: Tobias 63.36px/65.8944px 300, #07070a @ 0.875, ls -1.39392px |
| Transition | none |
| How | at rest |

Crops: `about-body-default.png`.

#### about-person

Team member. A person card/photo on the about page.

Page: about. Selector: `team member`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 770.8 x 347.72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #06070a |
| Text node | span.pq-word.is-lit: Tobias 63.36px/65.8944px 300, #06070a, ls -1.39392px |
| Transition | none |
| Painted layers | figcaption.mt-[clamp(24px,2.8vw,36px)].flex 770.8x48.2 border L:2px solid #de4c00 |
| How | at rest |

Crops: `about-person-default.png`.

#### faq-title

FAQ title.

Page: faq. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000.08 x 73.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #06070a |
| Text node | span: Tobias 72px/73.44px 400, #06070a, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `faq-title-default.png`.

#### faq-cat

FAQ category. A category heading inside the FAQ ("AI consulting, strategy & managed services").

Page: faq. Selector: `h2.text-rd-h2-sm`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 885.45 x 47.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 46.08px/47.9232px 400 |
| Letter spacing | -0.9216px |
| Colour | #06070a |
| Transition | none |
| How | at rest |

Crops: `faq-cat-default.png`.

#### faq-q

FAQ question. A question row of the FAQ accordion.

Page: faq. Selector: `h3.faq-q-heading`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 885.45 x 80 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Tobias 16px/16.64px 400 | = |
| Letter spacing | -0.32px | = |
| Colour | #06070a | = |
| Text node | span.faq-q-text.font-heading: Tobias 24px/28.8px 300, #06070a, ls -0.24px | span.faq-q-text.font-heading: Tobias 24px/28.8px 300, #de4c00, ls -0.24px |
| Transition | none | = |
| Painted layers | span.faq-toggle 36.0x36.0 border T:1px solid #06070a @ 0.1 / R:1px solid #06070a @ 0.1 / B:1px solid #06070a @ 0.1 / L:1px solid #06070a @ 0.1 r 50%; span::before.faq-toggle 12pxx1.5px bg #06070a r 1px; span::after.faq-toggle 12pxx1.5px bg #06070a r 1px | = |
| How | at rest | mouse hover |

Crops: `faq-q-default.png`, `faq-q-hover.png`.

#### faq-panel-open

FAQ panel (open). The answer panel after its question was pressed; a local disclosure, nothing sent.

Page: faq. Selector: `div.faq-panel`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 885.45 x 385.08 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #06070a |
| Text node | p: Work Sans 16px/26.4px 400, #3d3a36 |
| Transition | none |
| How | question pressed once to expand |

Crops: `faq-panel-open-open.png`.

#### faq-q-open

FAQ question (open). The question row after being pressed once.

Page: faq. Selector: `h3.faq-q-heading`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 885.45 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 16px/16.64px 400 |
| Letter spacing | -0.32px |
| Colour | #06070a |
| Text node | span.faq-q-text.font-heading: Tobias 24px/28.8px 300, #06070a, ls -0.24px |
| Transition | none |
| Painted layers | span.faq-toggle 50.9x50.9 bg #06070a border T:1px solid #06070a / R:1px solid #06070a / B:1px solid #06070a / L:1px solid #06070a r 50%; span::before.faq-toggle 12pxx1.5px bg #fffefb r 1px; span::after.faq-toggle 12pxx1.5px bg #fffefb r 1px |
| How | pressed once to expand |

Crops: `faq-q-open-open.png`.

#### careers-title

Careers title.

Page: careers. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000.08 x 293.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #06070a |
| Text node | span: Tobias 72px/73.44px 400, #06070a, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `careers-title-default.png`.

#### careers-body

careers body text.

Page: careers. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 312.25 x 51.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 17.28px/25.92px 400 |
| Letter spacing | normal |
| Colour | #3d3a36 |
| Transition | none |
| How | at rest |

Crops: `careers-body-default.png`.

#### job-row

Job row. An opening on the careers page.

Page: careers. Selector: `job row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 713.45 x 38.02 | 699.19 x 38.02 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Tobias 34.56px/38.016px 300 | = |
| Letter spacing | normal | = |
| Colour | #06070a | #de4c00 |
| Transition | color 0.4s ease | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `job-row-default.png`, `job-row-hover.png`.

#### security-title

Security title.

Page: security. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 770.8 x 73.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 72px/73.44px 400 |
| Letter spacing | -1.8px |
| Colour | #06070a |
| Text node | span: Tobias 72px/73.44px 400, #06070a, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `security-title-default.png`.

#### security-body

security body text.

Page: security. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 541.52 x 77.77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 17.28px/25.92px 400 |
| Letter spacing | normal |
| Colour | #3d3a36 |
| Transition | none |
| How | at rest |

Crops: `security-body-default.png`.

### Article page

#### art-title

Article title. "Meet Aboard Sign…" — a long-form piece in the article layout.

Page: aboard-sign. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000.08 x 77.77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 77.76px/77.76px 400 |
| Letter spacing | -1.944px |
| Colour | #fbf3ec |
| Text node | span: Tobias 77.76px/77.76px 400, #fbf3ec, ls -1.944px |
| Transition | none |
| How | at rest |

Crops: `art-title-default.png`.

#### art-body

Article body. A paragraph in the article column (rd-article, centred at columns 4-11).

Page: aboard-sign. Selector: `.rd-article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 312.25 x 52.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 17.6px/26.4px 400 |
| Letter spacing | normal |
| Colour | #e9decd @ 0.82 |
| Transition | none |
| How | at rest |

Crops: `art-body-default.png`.

#### art-share

Share rail. The SHARE rail beside the article (copy-link, never pressed).

Page: aboard-sign. Selector: `.rd-nl-rail`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 197.59 x 229.77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #06070a |
| Text node | span.rd-nl-meta.rd-nl-share-label: Work Sans 11.84px/17.76px 600, #6f6a63, ls 1.8944px |
| Transition | none |
| Icon | 18 x 18, colour #06070a |
| Painted layers | button.icon-copy-link.rd-icon-btn 42.0x42.0 border T:1px solid #06070a @ 0.1 / R:1px solid #06070a @ 0.1 / B:1px solid #06070a @ 0.1 / L:1px solid #06070a @ 0.1 r 50%; span.rd-nl-tip 62.2x28.7 bg #06070a r 999px; a.rd-icon-btn.rd-nl-share-btn 42.0x42.0 border T:1px solid #06070a @ 0.1 / R:1px solid #06070a @ 0.1 / B:1px solid #06070a @ 0.1 / L:1px solid #06070a @ 0.1 r 50%; a.rd-icon-btn.rd-nl-share-btn 42.0x42.0 border T:1px solid #06070a @ 0.1 / R:1px solid #06070a @ 0.1 / B:1px solid #06070a @ 0.1 / L:1px solid #06070a @ 0.1 r 50%; a.rd-icon-btn.rd-nl-share-btn 42.0x42.0 border T:1px solid #06070a @ 0.1 / R:1px solid #06070a @ 0.1 / B:1px solid #06070a @ 0.1 / L:1px solid #06070a @ 0.1 r 50% |
| How | at rest |

Crops: `art-share-default.png`.

#### art-nl-card

Newsletter card. A "More from the newsletter" card (date, title, thumbnail).

Page: aboard-sign. Selector: `a.rd-nl-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 426.88 x 422.58 | = |
| Padding | 0px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Work Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #06070a | = |
| Text node | time.rd-nl-meta: Work Sans 11.84px/17.76px 600, #6f6a63, ls 1.8944px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.mb-1.5.block 426.9x284.6 bg #f5f4f1 r 12px | = |
| How | at rest | mouse hover |

Crops: `art-nl-card-default.png`, `art-nl-card-hover.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile top bar. The mobile header: wordmark left, menu trigger right.

Page: home. Selector: `header.site-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 12px 12px 0px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #271503 |
| Text node | a.rd-nav-cta: Work Sans 14.08px/22.528px 400, #fffefb |
| Transition | none |
| Icon | 107.05 x 26, colour #271503 |
| Painted layers | nav::before.rd-nav.rd-focus-nav 350pxx60px bg #f0f1ef @ 0.84 r 28px; a::after 9pxx9px bg #271503; ul.sub-menu 0.0x0.0 bg #faf5ef @ 0.97 r 14px shadow #271503 @ 0.18 0px 14px 34px -22px; a::after 9pxx9px bg #271503; ul.sub-menu 0.0x0.0 bg #faf5ef @ 0.97 r 14px shadow #271503 @ 0.18 0px 14px 34px -22px; a.rd-nav-cta 0.0x0.0 bg #de4c00 r 999px |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-menu-trigger

Mobile menu trigger. The "Open menu" button. Pressed once below to open the menu; a local disclosure.

Page: home. Selector: `button.rd-nav-toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #271503 offset 2px | = |
| Font | Work Sans 16px/25.6px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #271503 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span 20.0x1.5 bg #271503; span 20.0x1.5 bg #271503; span 20.0x1.5 bg #271503 | = | button.rd-nav-toggle 44.0x44.0 r 2px outline 2px solid #271503 offset 2px; span 20.0x1.5 bg #271503; span 20.0x1.5 bg #271503; span 20.0x1.5 bg #271503 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-trigger-default.png`, `m-menu-trigger-hover.png`, `m-menu-trigger-focus-visible.png`, `m-menu-trigger-pressed.png`.

#### m-nav-panel

Mobile menu (open). The opened mobile menu panel; pressed once, nothing navigated.

Page: home. Selector: `nav.rd-nav open`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 350 x 643.41 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #271503 |
| Text node | a.rd-nav-cta: Work Sans 14.08px/22.528px 400, #fffefb |
| Transition | color, max-width, transform 0.5s, 0.7s, 0.7s cubic-bezier(0.65, 0, 0.35, 1), cubic-bezier(0.65, 0, 0.35, 1), cubic-bezier(0.65, 0, 0.35, 1) delay 0s, 0s, 0s |
| Icon | 107.05 x 26, colour #271503 |
| ::before | 350px x 643.406px, absolute, bg #f0f1ef @ 0.84, radius 28px |
| Painted layers | nav::before.rd-nav.rd-focus-nav 350pxx643.406px bg #f0f1ef @ 0.84 r 28px; a::after 9pxx9px bg #271503; ul.sub-menu 0.0x0.0 bg #faf5ef @ 0.97 r 14px shadow #271503 @ 0.18 0px 14px 34px -22px; a::after 9pxx9px bg #271503; ul.sub-menu 0.0x0.0 bg #faf5ef @ 0.97 r 14px shadow #271503 @ 0.18 0px 14px 34px -22px; a.rd-nav-cta 0.0x0.0 bg #de4c00 r 999px |
| How | menu trigger pressed once |

Crops: `m-nav-panel-open.png`.

#### m-hero-title

Mobile hero title.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 89.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Tobias 44.8px/44.8px 400 |
| Letter spacing | -0.896px |
| Colour | #271503 |
| Text node | span: Tobias 44.8px/44.8px 400, #271503, ls -0.896px |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

#### m-feed-row

Mobile feed row.

Page: home. Selector: `a.rd-feed-row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 232.81 |
| Padding | 24px 0px |
| Gap | 12px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Work Sans 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #271503 |
| Text node | span.rd-meta.inline-flex: Work Sans 11.52px/18.432px 600, #271503, ls 1.6128px |
| Transition | transform 0.6s cubic-bezier(0.32, 0.72, 0, 1) |
| Cursor | pointer |
| Icon | 13 x 13, colour #de4c00 |
| Painted layers | span.relative.aspect-[4/3] 120.0x120.0 bg #efe7db r 12px |
| How | at rest |

Crops: `m-feed-row-default.png`.

## Transitions declared in the readable stylesheets

aboard.com's WordPress theme stylesheets are same-origin readable and declare about 640 custom properties (the --wp--preset--* and --rd-* names; see css-vars.json). The values below are computed styles read off the running pages; the per-state Transition rows are computed values.

- aboard-sign: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`

- about: `color .5s var(--rd-ease-io)`, `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`

- careers: `color .5s var(--rd-ease-io)`, `padding .5s var(--rd-ease-io)`, `color 0.4s`, `background 0.4s`, `transform .5s var(--rd-ease)`, `none`, `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`

- case-studies: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`

- case-study: `box-shadow .9s var(--rd-ease-out)`, `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`

- events: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`

- faq: `color 0.3s`, `transform .5s var(--rd-ease-io)`, `transform .56s var(--rd-ease-io),background .4s,border-color .4s`, `none`, `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`

- foundry: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`

- home: `opacity .9s var(--rd-ease-io),visibility 0s linear .9s`, `opacity .9s var(--rd-ease-io),visibility 0s`, `opacity .5s var(--rd-ease-io)`, `opacity .8s var(--rd-ease-io) .25s`, `transform .6s var(--rd-ease)`, `unset`, `color 0.3s`, `opacity .4s var(--rd-ease-io),transform .6s var(--rd-ease-out)`, `none`, `flex-grow .9s var(--rd-ease)`, `background-color .5s var(--rd-ease-mode)`, `background 0.3s, transform 0.3s`

- how-we-work: `opacity .5s var(--rd-ease-io)`, `opacity .5s var(--rd-ease-io),transform .9s var(--rd-ease-out)`, `none`, `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`

- media: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`

- newsletter: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`

- perspectives: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`

- podcast: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`

- podcast-episode: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`

- security: `background 0.3s, transform 0.3s`, `background .4s var(--rd-ease),transform .4s var(--rd-ease)`, `transform .6s var(--rd-ease)`, `background 0.35s, box-shadow 0.35s`, `color 0.3s, text-decoration-color 0.3s`, `color .4s var(--rd-ease)`, `color 0.3s`, `background 0.3s, color 0.3s, border-color 0.3s`, `opacity var(--rd-reveal-fade),transform var(--rd-reveal-move)`, `opacity 1.4s var(--rd-ease-io) .1s`, `transform 2s var(--rd-ease-out) .1s`, `none`
