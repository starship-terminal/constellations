# Component measurements

Computed styles read from untitled.stream on 2026-11-08 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Dialogs and overlays

#### consent-card

Cookie consent card. The "We value privacy" card, fixed bottom-left on first load (frosted surface). Its Customize / Reject all / Accept all buttons were measured but never pressed: the consent form posts a Remix action to /settings/cookies, which Cloudflare 403s headless, replacing the page with the router error boundary.

Page: home. Selector: `consent card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 224 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #262626 @ 0.9 |
| Background image | linear-gradient(0deg, #808080 0%, #808080 100%), none |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.2 0px 4px 10px 0px |
| Backdrop filter | blur(10px) |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #ffffff |
| Text node | h1.body-semibold: Untitled Sans 15px/20px 500, #ffffff, ls -0.45px |
| Transition | none |
| Painted layers | div.frost-background.animate-fade-in 500.0x224.0 bg #262626 @ 0.9 image linear-gradient(0deg, #808080 0%, #808080 100%), none r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.2 0px 4px 10px 0px; button.clean-btn.footnote-semibold 81.2x40.0 bg #ffffff @ 0.05 r 3.35544e+07px; button.clean-btn.footnote-semibold 85.6x40.0 bg #ffffff r 3.35544e+07px |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `consent-card-default.png`.

#### consent-accept

Accept all button. The solid white pill in the consent card. Not pressed.

Page: home. Selector: `button Accept all`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 85.63 x 40 | = |
| Padding | 12px 16px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Untitled Sans 12px/16px 500 | = |
| Letter spacing | -0.41px | = |
| Colour | #000000 | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.clean-btn.footnote-semibold 85.6x40.0 bg #ffffff r 3.35544e+07px | = |
| How | at rest | mouse hover |
| Opacity | - | 0.8 |

Crops: `consent-accept-default.png`, `consent-accept-hover.png`.

#### consent-reject

Reject all button. The bg-white/5 ghost pill beside Accept all. Not pressed.

Page: home. Selector: `button Reject all`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 81.2 x 40 | = |
| Padding | 12px 16px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | #ffffff @ 0.05 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Untitled Sans 12px/16px 500 | = |
| Letter spacing | -0.41px | = |
| Colour | #ffffff | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.clean-btn.footnote-semibold 81.2x40.0 bg #ffffff @ 0.05 r 3.35544e+07px | = |
| How | at rest | mouse hover |
| Opacity | - | 0.8 |

Crops: `consent-reject-default.png`, `consent-reject-hover.png`.

#### consent-customize

Customize link. The text-only option in the consent card. Not pressed.

Page: home. Selector: `button Customize`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 58.45 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Untitled Sans 12px/16px 500 | = |
| Letter spacing | -0.41px | = |
| Colour | #ffffff | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Ancestor paint | 3 up div.frost-background.animate-fade-in bg #262626 @ 0.9 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.2 0px 4px 10px 0px | = |
| How | at rest | mouse hover |
| Opacity | - | 0.8 |

Crops: `consent-customize-default.png`, `consent-customize-hover.png`.

### Shell and navigation

#### header

Header. The transparent top band: [untitled] wordmark and the super-title tagline on the left, [membership] text link and the black Enter App pill on the right.

Page: home. Selector: `header column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1312 x 88 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | p.super-title.max-w-[360px]: Untitled Sans 26px/32px 500, #191919, ls -0.78px |
| Transition | none |
| Icon | 0 x 0, colour #191919 |
| Painted layers | a.clean-btn.inline-flex 150.0x44.0 image linear-gradient(#242424 0%, #101010 100%) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 4px 15px 0px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Wordmark. The [untitled] mark, a text link rendered with bracket styling; only rendered on the sub-pages, not on home.

Page: pricing. Selector: `wordmark link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112.28 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 15px/20px 400 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #191919 | = | = | = |
| Text node | span.inline-block: Untitled Sans 26px/32px 500, #191919, ls -0.78px | = | = | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `logo-default.png`, `logo-hover.png`, `logo-focus-visible.png`, `logo-pressed.png`.

#### nav-membership

Membership nav link. The [membership] text link in the header; scrolls to the membership pitch.

Page: home. Selector: `a [membership]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99.3 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 15px/20px 500 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #191919 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `nav-membership-default.png`, `nav-membership-hover.png`, `nav-membership-focus-visible.png`, `nav-membership-pressed.png`.

#### cta-enter-app

Enter App CTA. The black pill at the header's far right; links to /login.

Page: home. Selector: `a.clean-btn Enter App`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#242424 0%, #101010 100%) | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 4px 15px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 13px/16px 500 | = | = | = |
| Letter spacing | -0.39px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.clean-btn.inline-flex 150.0x44.0 image linear-gradient(#242424 0%, #101010 100%) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 4px 15px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `cta-enter-app-default.png`, `cta-enter-app-hover.png`, `cta-enter-app-focus-visible.png`, `cta-enter-app-pressed.png`.

#### footer

Footer. The legal row at the foot: Terms, Privacy, Cookie Policy, Contact Us and a Cookie Settings button, plus the Made in Brooklyn, NY mark.

Page: home. Selector: `footer row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 436.64 x 16 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | a.subhead.text-secondary-label: Untitled Sans 13px/16px 400, #7e7e7e, ls -0.39px |
| Transition | none |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer legal link.

Page: home. Selector: `a.subhead Terms`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36.58 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 13px/16px 400 | = | = | = |
| Letter spacing | -0.39px | = | = | = |
| Colour | #7e7e7e | = | = | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### cookie-settings

Cookie settings button. The footer control that re-opens the consent card. Focused and hovered only — pressing it reposts the gated consent flow.

Page: home. Selector: `button Cookie Settings`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 90.13 x 16 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Untitled Sans 13px/16px 400 | = | = |
| Letter spacing | -0.39px | = | = |
| Colour | #7e7e7e | = | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Opacity | - | 0.8 | = |

Crops: `cookie-settings-default.png`, `cookie-settings-hover.png`, `cookie-settings-focus-visible.png`.

#### pricing-header

Pricing header. Same top band as home, here with the [untitled] wordmark link at the left and Enter app (ghost) + Subscribe (black) pills on the right.

Page: pricing. Selector: `header column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 108 |
| Padding | 32px 64px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | span.inline-block: Untitled Sans 26px/32px 500, #191919, ls -0.78px |
| Transition | none |
| Painted layers | div.absolute.blur-sm 2592.0x108.0 image linear-gradient(in oklab, #ffffff 0%, #ffffff 80%, #000000 @ 0 100%); a.clean-btn.inline-flex 150.0x44.0 bg #1a1a1a @ 0.05 r 3.35544e+07px; a.clean-btn.inline-flex 150.0x44.0 image linear-gradient(#242424 0%, #101010 100%) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 4px 15px 0px |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `pricing-header-default.png`.

#### cta-subscribe

Subscribe CTA. The black Subscribe pill in the header.

Page: pricing. Selector: `a.clean-btn Subscribe`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#242424 0%, #101010 100%) | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 4px 15px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 13px/16px 500 | = | = | = |
| Letter spacing | -0.39px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.clean-btn.inline-flex 150.0x44.0 image linear-gradient(#242424 0%, #101010 100%) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.15 0px 4px 15px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `cta-subscribe-default.png`, `cta-subscribe-hover.png`, `cta-subscribe-focus-visible.png`, `cta-subscribe-pressed.png`.

### Home

#### hero-title

Hero title. The visible display copy "A sacred place for your work-in-progress music" (p.super-title); the actual h1 is sr-only.

Page: home. Selector: `p.super-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 26px/32px 500 |
| Letter spacing | -0.78px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### disc-carousel

Disc carousel. The signature element: a strip of oversized iridescent CD renders (div.rounded-full with webp background-image art) filling the hero.

Page: home. Selector: `disc strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Gap | 28px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Transition | none |
| Painted layers | div.bg-shading.rounded-full 842.0x842.0 bg #1a1a1a @ 0.05 r 3.35544e+07px; div.bg-shading.rounded-full 690.6x690.6 bg #1a1a1a @ 0.05 r 3.35544e+07px; div.bg-shading.rounded-full 820.8x820.8 bg #1a1a1a @ 0.05 r 3.35544e+07px; div.bg-shading.rounded-full 647.5x647.5 bg #1a1a1a @ 0.05 r 3.35544e+07px; div.bg-shading.rounded-full 0.0x0.0 bg #1a1a1a @ 0.05 r 3.35544e+07px; div.absolute.blur-sm 0.0x0.0 image linear-gradient(to top in oklab, #ffffff 0%, #ffffff 80%, #000000 @ 0 100%) |
| How | at rest |

Crops: `disc-carousel-default.png`.

#### disc

Disc. One iridescent CD render: a rounded-full div whose background-image is a webp disc artwork.

Page: home. Selector: `div.rounded-full disc`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 695.03 x 695.03 |
| Padding | 0px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #1a1a1a @ 0.05 |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Transition | none |
| Transform | matrix(0.173569, 0.984822, -0.984822, 0.173569, 0, 0) |
| Painted layers | div.bg-shading.rounded-full 695.0x695.0 bg #1a1a1a @ 0.05 r 3.35544e+07px |
| How | at rest |

Crops: none.

#### pill-bar

Bottom pill bar. The floating bar pinned to the viewport bottom: social pills (Texting Interviews, IG, X), the black We're hiring pill, Learn more, and the iOS / Android / MacOS platform pills.

Page: home. Selector: `floating pill bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 92 |
| Padding | 24px 64px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | a.body-semibold.pointer-events-auto: Untitled Sans 15px/20px 500, #191919, ls -0.45px |
| Transition | none |
| Icon | 20 x 20, colour #191919 |
| Painted layers | div.sm:bg-shading.flex 272.4x44.0 bg #1a1a1a @ 0.05 r 3.35544e+07px; a.body-semibold.bg-primary-label 130.7x44.0 bg #191919 r 3.35544e+07px; button.sm:bg-shading.pointer-events-auto 148.7x44.0 bg #1a1a1a @ 0.05 r 3.35544e+07px; a.body-semibold.bg-shading 96.4x44.0 bg #1a1a1a @ 0.05 r 3.35544e+07px; a.body-semibold.bg-shading 127.9x44.0 bg #1a1a1a @ 0.05 r 3.35544e+07px; a.body-semibold.bg-shading 127.0x44.0 bg #1a1a1a @ 0.05 r 3.35544e+07px |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `pill-bar-default.png`.

#### pill-social

Social pill. A frosted pill in the bottom bar holding the social links (Texting Interviews, IG, X).

Page: home. Selector: `social pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150.94 x 20 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 15px/20px 500 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #191919 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.sm:bg-shading.flex bg #1a1a1a @ 0.05 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `pill-social-default.png`, `pill-social-hover.png`, `pill-social-focus-visible.png`, `pill-social-pressed.png`.

#### cta-hiring

Hiring pill. The inverted (black) "We're hiring" pill in the bottom bar; links to jobs.untitled.stream.

Page: home. Selector: `a We're hiring`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130.72 x 44 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #191919 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 15px/20px 500 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.body-semibold.bg-primary-label 130.7x44.0 bg #191919 r 3.35544e+07px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `cta-hiring-default.png`, `cta-hiring-hover.png`, `cta-hiring-focus-visible.png`, `cta-hiring-pressed.png`.

#### pill-learn-more

Learn more pill. The frosted pill that scrolls the page to the product sections.

Page: home. Selector: `button Learn more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148.67 x 44 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #1a1a1a @ 0.05 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 15px/20px 400 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #191919 | = | = | = |
| Text node | span.body-semibold.flex: Untitled Sans 15px/20px 500, #191919, ls -0.45px | = | = | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Opacity | 0 | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #191919 | = | = | = |
| Painted layers | button.sm:bg-shading.pointer-events-auto 148.7x44.0 bg #1a1a1a @ 0.05 r 3.35544e+07px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pill-learn-more-default.png`, `pill-learn-more-hover.png`, `pill-learn-more-focus-visible.png`, `pill-learn-more-pressed.png`.

#### pill-platform

Platform pill. One of the iOS / Android / MacOS download pills in the bottom bar, each with a platform icon.

Page: home. Selector: `a.bg-shading platform`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.39 x 44 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #1a1a1a @ 0.05 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 15px/20px 500 | = | = | = |
| Letter spacing | -0.45px | = | = | = |
| Colour | #191919 | = | = | = |
| Text node | span: Untitled Sans 15px/20px 500, #191919, ls -0.45px | = | = | = |
| Transition | opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #191919 | = | = | = |
| Painted layers | a.body-semibold.bg-shading 96.4x44.0 bg #1a1a1a @ 0.05 r 3.35544e+07px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `pill-platform-default.png`, `pill-platform-hover.png`, `pill-platform-focus-visible.png`, `pill-platform-pressed.png`.

#### feature-title

Feature title. An h3.body-semibold heading a product section down the page ("Organize your music the way you want").

Page: home. Selector: `h3 feature`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 319 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 500 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `feature-title-default.png`.

#### feature-section

Feature section. A product-feature block down the landing page: heading, copy and media.

Page: home. Selector: `feature block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 319 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | h3.body-semibold.mb-4: Untitled Sans 15px/20px 500, #191919, ls -0.45px |
| Transition | none |
| How | at rest |

Crops: `feature-section-default.png`.

#### read-more

Read more link. A text link expanding a product story section.

Page: home. Selector: `a Read more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.88 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 13px/16px 400 | = | = | = |
| Letter spacing | -0.39px | = | = | = |
| Colour | #191919 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `read-more-default.png`, `read-more-hover.png`, `read-more-focus-visible.png`, `read-more-pressed.png`.

#### feature-video

Feature video. A product-demo video embedded in a feature section; measured as the element, its stream is not introspected.

Page: home. Selector: `video`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 450 x 345.94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #1a1a1a @ 0.05 |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Transition | none |
| Opacity | 0 |
| Painted layers | video.opacity-0.shadow-device 450.0x345.9 bg #1a1a1a @ 0.05 |
| Ancestor paint | 1 up div.sm:border-border.bg-shading bg #1a1a1a @ 0.05 |
| How | at rest |

Crops: `feature-video-default.png`.

### Mobile (390 wide)

#### m-hero-title

Mobile hero title.

Page: home. Selector: `mobile super-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 294 x 88 |
| Padding | 0px 0px 20px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 28px/34px 500 |
| Letter spacing | -1.64px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

#### m-appstore

App Store badge. The Download on the App Store badge under the mobile hero title.

Page: home. Selector: `app store badge`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 150 x 50 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Untitled Sans 17px/22px 500 | = |
| Letter spacing | -0.43px | = |
| Colour | #191919 | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 150 x 50, colour #191919 | = |
| How | at rest | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 |

Crops: `m-appstore-default.png`, `m-appstore-pressed.png`.

#### m-disc

Mobile disc. The oversized iridescent disc filling the lower half of the mobile hero.

Page: home. Selector: `mobile disc div`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 772.52 x 772.52 |
| Padding | 0px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #1a1a1a @ 0.05 |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 17px/22px 400 |
| Letter spacing | -0.43px |
| Colour | #191919 |
| Transition | none |
| Transform | matrix(-0.35126, 0.936278, -0.936278, -0.35126, 0, 0) |
| Painted layers | div.bg-shading.rounded-full 772.5x772.5 bg #1a1a1a @ 0.05 r 3.35544e+07px |
| How | at rest |

Crops: none.

#### m-membership

Mobile nav link.

Page: home. Selector: `mobile header link`. States: .

Not found on the page at capture time.

### Pricing

#### pricing-title

Pricing title. "Take your creative process to the next level" — a .super-title block, same display style as the home hero.

Page: pricing. Selector: `.super-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1312 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 26px/32px 500 |
| Letter spacing | -0.78px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-toggle

Billing toggle. The Yearly / Monthly segment rail at the left of the plan grid: the buttons are its direct children, and the column stretches to the plan cards' full height.

Page: pricing. Selector: `billing segment`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 121.95 x 536 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | button.body-semibold.relative: Untitled Sans 15px/20px 500, #191919, ls -0.45px |
| Transition | none |
| Painted layers | span.bg-shading.rounded-20 91.1x44.0 bg #1a1a1a @ 0.05 r 20px |
| How | at rest |

Crops: `billing-toggle-default.png`.

#### billing-yearly

Yearly option. The selected segment (default plan is yearly).

Page: pricing. Selector: `button Yearly`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 91.08 x 44 | = | = |
| Padding | 12px 24px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Untitled Sans 15px/20px 500 | = | = |
| Letter spacing | -0.45px | = | = |
| Colour | #191919 | = | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | span.bg-shading.rounded-20 91.1x44.0 bg #1a1a1a @ 0.05 r 20px | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | 0.8 |

Crops: `billing-yearly-default.png`, `billing-yearly-hover.png`, `billing-yearly-pressed.png`.

#### billing-monthly

Monthly option.

Page: pricing. Selector: `button Monthly`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 105 x 44 | = |
| Padding | 12px 24px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Untitled Sans 15px/20px 500 | = |
| Letter spacing | -0.45px | = |
| Colour | #191919 | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Opacity | - | 0.8 |

Crops: `billing-monthly-default.png`, `billing-monthly-hover.png`.

#### billing-monthly-on

Monthly option (selected). The Monthly segment after pressing it: client-side state switch, no data posted.

Page: pricing. Selector: `button Monthly on`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 105 x 44 |
| Padding | 12px 24px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 500 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Opacity | 0.996676 |
| Cursor | pointer |
| Painted layers | span.bg-shading.rounded-20 105.0x44.0 bg #1a1a1a @ 0.05 r 20px |
| How | at rest |

Crops: `billing-monthly-on-open.png`.

#### plan-price-monthly

Monthly price. The membership price after switching to Monthly.

Page: pricing. Selector: `price monthly`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 278 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 500 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `plan-price-monthly-open.png`.

#### plan-card

Plan card (starter). The [starter] free tier card: plan name, price, feature list with icons.

Page: pricing. Selector: `starter card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 536 |
| Padding | 32px 24px |
| Border | none |
| Radius | 20px |
| Background | #eeeeee |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | div.super-title.pb-20: Untitled Sans 26px/32px 500, #191919, ls -0.78px |
| Transition | none |
| Icon | 32 x 32, colour #191919 |
| Painted layers | div.bg-secondary-background-dark.rounded-20 350.0x536.0 bg #eeeeee r 20px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-card-paid

Plan card (membership). The [membership] card: $49.99 / year, feature list with icons.

Page: pricing. Selector: `membership card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 536 |
| Padding | 32px 24px 32px 0px |
| Border | none |
| Radius | 0px |
| Background | #eeeeee |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | div.super-title.pb-20: Untitled Sans 26px/32px 500, #191919, ls -0.78px |
| Transition | none |
| Icon | 32 x 32, colour #191919 |
| Painted layers | div.bg-secondary-background-dark.relative 350.0x536.0 bg #eeeeee; div.from-secondary-background.absolute 0.0x0.0 image linear-gradient(to top in oklab, #f2f2f2 0%, #000000 @ 0 100%); div.from-secondary-background.top-0 150.0x536.0 image linear-gradient(to left in oklab, #f2f2f2 0%, #000000 @ 0 100%) |
| Ancestor paint | 1 up div.bg-secondary-background-dark.rounded-20 bg #eeeeee |
| How | at rest |

Crops: `plan-card-paid-default.png`.

#### plan-name

Plan name. A bracketed plan name ([starter], [membership]).

Page: pricing. Selector: `plan name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 254 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 26px/32px 500 |
| Letter spacing | -0.78px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price.

Page: pricing. Selector: `price text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 254 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 500 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### feature-row

Feature row. A plan feature line: icon + h3.body-semibold name + sub copy ("Unlimited listening").

Page: pricing. Selector: `feature li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 254 x 52 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | h3.body-semibold: Untitled Sans 15px/20px 500, #191919, ls -0.45px |
| Transition | none |
| Icon | 32 x 32, colour #191919 |
| How | at rest |

Crops: `feature-row-default.png`.

### Trust and security

#### trust-title

Trust title. "Trust & Security" — the page is a single long-text column.

Page: trust. Selector: `trust h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 536 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 26px/32px 500 |
| Letter spacing | -0.78px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `trust-title-default.png`.

#### trust-section-title

Trust section title. A numbered practice heading ("[1] Passwordless sign-in").

Page: trust. Selector: `trust heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 536 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 18px/22px 500 |
| Letter spacing | -0.54px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `trust-section-title-default.png`.

#### trust-list

Trust bullet list. The encryption-standards bullet list (TLS in transit, AES-256 at rest).

Page: trust. Selector: `trust ul`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 528 x 86 |
| Padding | 0px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | strong: Untitled Sans 15px/20px 500, #191919, ls -0.45px |
| Transition | none |
| How | at rest |

Crops: `trust-list-default.png`.

#### trust-link

Trust link.

Page: trust. Selector: `trust a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112.25 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 26px/32px 500 | = | = | = |
| Letter spacing | -0.78px | = | = | = |
| Colour | #191919 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `trust-link-default.png`, `trust-link-hover.png`, `trust-link-focus-visible.png`, `trust-link-pressed.png`.

### Sign-in boundary

#### login-card

Sign-in card. The centred sign-in column: app icon, the tagline, and three choices — Continue with Google, Continue with Apple, Sign in with phone. OAuth and phone sign-in were measured at rest only; nothing was pressed or sent.

Page: login. Selector: `login column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 762 |
| Padding | 32px 0px 128px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Text node | h1: Untitled Sans 26px/32px 500, #191919, ls -0.78px |
| Transition | none |
| Icon | 21 x 20, colour #191919 |
| Painted layers | div.amulet-clip-mask.bg-amulet 220.0x220.0 image linear-gradient(#eeeeee, #d0d0d0); div.absolute.inset-[7%] 189.2x189.2 bg oklab(0 none none / 0.1) r 3.35544e+07px; div.absolute.inset-[12%] 167.2x167.2 bg oklab(0 none none / 0.1) r 3.35544e+07px; div.absolute.inset-[47%] 13.2x13.2 bg oklab(0 none none / 0.1) r 3.35544e+07px; button.text-primary.bg-primary-label 342.0x52.0 bg #1a1a1a @ 0.05 r 3.35544e+07px; button.text-primary.bg-primary-label 342.0x54.0 bg #1a1a1a @ 0.05 r 3.35544e+07px |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `login-card-default.png`.

#### login-icon

App icon. The iridescent-disc app icon at the top of the sign-in card.

Page: login. Selector: `login icon`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 189.22 x 189.22 |
| Padding | 0px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | oklab(0 none none / 0.1) |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 15px/20px 400 |
| Letter spacing | -0.45px |
| Colour | #191919 |
| Transition | none |
| Painted layers | div.absolute.inset-[7%] 189.2x189.2 bg oklab(0 none none / 0.1) r 3.35544e+07px |
| How | at rest |

Crops: `login-icon-default.png`.

#### login-title

Sign-in title.

Page: login. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Untitled Sans 26px/32px 500 |
| Letter spacing | -0.78px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### oauth-google

Continue with Google. The frosted OAuth pill. Hovered and focused only — pressing it leaves for accounts.google.com.

Page: login. Selector: `Google oauth pill`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 342 x 52 | = | = |
| Padding | 16px 20px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #1a1a1a @ 0.05 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Untitled Sans 15px/20px 400 | = | = |
| Letter spacing | -0.45px | = | = |
| Colour | #191919 | = | = |
| Text node | label.body-semibold.cursor-pointer: Untitled Sans 15px/20px 500, #191919, ls -0.45px | = | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 21 x 20, colour #191919 | = | = |
| Painted layers | button.text-primary.bg-primary-label 342.0x52.0 bg #1a1a1a @ 0.05 r 3.35544e+07px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Opacity | - | 0.8 | = |

Crops: `oauth-google-default.png`, `oauth-google-hover.png`, `oauth-google-focus-visible.png`.

#### oauth-apple

Continue with Apple. The matching Apple OAuth pill. Hovered and focused only.

Page: login. Selector: `Apple oauth pill`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 342 x 54 | = | = |
| Padding | 16px 20px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #1a1a1a @ 0.05 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Untitled Sans 15px/20px 400 | = | = |
| Letter spacing | -0.45px | = | = |
| Colour | #191919 | = | = |
| Text node | label.body-semibold.cursor-pointer: Untitled Sans 15px/20px 500, #191919, ls -0.45px | = | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 18 x 22, colour #191919 | = | = |
| Painted layers | button.text-primary.bg-primary-label 342.0x54.0 bg #1a1a1a @ 0.05 r 3.35544e+07px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Opacity | - | 0.8 | = |

Crops: `oauth-apple-default.png`, `oauth-apple-hover.png`, `oauth-apple-focus-visible.png`.

#### phone-signin

Phone sign-in link. The text option under the OAuth pills; leads to the passwordless SMS flow.

Page: login. Selector: `phone sign-in`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 342 x 52 | = | = |
| Padding | 16px 0px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Untitled Sans 15px/20px 500 | = | = |
| Letter spacing | -0.45px | = | = |
| Colour | #191919 | = | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Opacity | - | 0.8 | = |

Crops: `phone-signin-default.png`, `phone-signin-hover.png`, `phone-signin-focus-visible.png`.

#### legal-link

Legal link. The Terms / Privacy Policy links under the sign-in choices.

Page: login. Selector: `login legal a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 33.81 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Untitled Sans 12px/16px 400 | = | = | = |
| Letter spacing | -0.35px | = | = | = |
| Colour | #7e7e7e | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `legal-link-default.png`, `legal-link-hover.png`, `legal-link-focus-visible.png`, `legal-link-pressed.png`.

## Transitions declared in the readable stylesheets

untitled.stream's Vite build serves its CSS same-origin, so this list covers the rules the CSSOM could read on each page (Tailwind utilities and the site's own semantic --color-*/type-scale tokens); the per-state Transition rows above are computed values.

- home: `opacity 0.15s, transform 0.1s`, `transform var(--peek-duration) ease-in-out`

- login: `opacity 0.15s, transform 0.1s`, `transform var(--peek-duration) ease-in-out`

- pricing: `opacity 0.15s, transform 0.1s`, `transform var(--peek-duration) ease-in-out`

- trust: `opacity 0.15s, transform 0.1s`, `transform var(--peek-duration) ease-in-out`
