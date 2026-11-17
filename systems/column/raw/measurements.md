# Component measurements

Computed styles read from column.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium (the site renders clean headless — no bot wall) at 1440 x 900 (the Mobile group at 390 x 844) on the site's light surface (the styled-components cookie banner hidden, never answered; dashboard.column.com/login measured at rest with nothing typed or submitted), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent — not driven on this capture, where nothing was typed at all; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-banner

Promo banner. The launch announcement row at the top of the header (Header__LaunchBanner) — real chrome, kept.

Page: home. Selector: `[class*=LaunchBanner]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 40 |
| Padding | 0px 20px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(90deg, #3e5199 0%, #5568ad 100%) |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.Typography__Text-sc-qr50ld-0.eGJccS: SuisseIntl 14px/15.4px 500, #ffffff |
| Transition | filter 0.2s ease |
| Cursor | pointer |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | a.Header__LaunchBanner-sc-i83ruj-8.dXGHmi 1440.0x40.0 image linear-gradient(90deg, #3e5199 0%, #5568ad 100%) |
| Ancestor paint | 1 up div.Layout__Body-sc-y46uw8-0.eBqw bg #f6f6f8 |
| How | at rest |

Crops: none.

#### header

Nav bar. The fixed site header (Header__SiteHeader): Column logo, nav triggers, Sign in, ghost CTAs and the navy Sign up button.

Page: home. Selector: `header[class*=SiteHeader]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 62 |
| Padding | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #12161e |
| Text node | button.Header__NavItemButton-sc-i83ruj-7.eAqYjN: SuisseIntl 14px/21px 500, #12161e |
| Transition | transform, box-shadow, background 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s |
| Icon | 86.48 x 19, colour #12161e, fill #000000 |
| Painted layers | button.Button__StyledButton-sc-fltzk0-1.dQTXBn 127.0x36.0 bg #ffffff @ 0.5 r 8px shadow #ffffff @ 0 0px 1px 1px 0px, #575a64 @ 0.12 0px 0px 0px 1px; div.GetStartedMenu__Panel-sc-1vb419z-3.frtiDs 400.0x153.4 bg #ffffff r 12px shadow #000000 @ 0.024 0px 0px 0px 1px, #000000 @ 0.05 0px 16px 32px 0px, #000000 @ 0.1 0px 4px 8px 0px; a.GetStartedMenu__Choice-sc-1vb419z-5.canNmk 188.0x137.4 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 1.5x1.5 bg #7ea7e9 r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 1.5x1.5 bg #7ea7e9 r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 1.5x1.5 bg #7ea7e9 r 50% |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Column logo home anchor in the nav (Header__HeaderLogo).

Page: home. Selector: `header [class*=HeaderLogo]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 86.48 x 19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #12161e |
| Transition | none |
| Cursor | pointer |
| Icon | 86.48 x 19, colour #12161e, fill #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. A nav trigger ("Products", Header__NavItemButton); its mega-menu renders eager in the DOM.

Page: home. Selector: `header [class*=NavItemButton] first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111 x 37 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.02 | = | #000000 @ 0.02 |
| Box shadow | none | #000000 @ 0.25 0px 0px 1px 0px | #a2c1ed 0px 0px 0px 2px | #000000 @ 0.25 0px 0px 1px 0px |
| Outline | none | = | = | = |
| Font | SuisseIntl 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #12161e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #12161e | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Backdrop filter | - | blur(8px) | = | blur(8px) |
| Painted layers | - | button.Header__NavItemButton-sc-i83ruj-7.eAqYjN 111.0x37.0 bg #000000 @ 0.02 r 8px shadow #000000 @ 0.25 0px 0px 1px 0px | button.Header__NavItemButton-sc-i83ruj-7.eAqYjN 111.0x37.0 r 8px shadow #a2c1ed 0px 0px 0px 2px | button.Header__NavItemButton-sc-i83ruj-7.eAqYjN 111.0x37.0 bg #000000 @ 0.02 r 8px shadow #000000 @ 0.25 0px 0px 1px 0px |

Crops: `nav-item-default.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-ghost

Nav sign-in link. The "Sign in" NavItem anchor (Header__NavItem) linking to dashboard.column.com/login; measured never followed.

Page: home. Selector: `header a[class*=NavItem]:has-text("Sign in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77 x 38 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.02 | = | #000000 @ 0.02 |
| Box shadow | none | #000000 @ 0.25 0px 0px 1px 0px | #a2c1ed 0px 0px 0px 2px | #000000 @ 0.25 0px 0px 1px 0px |
| Outline | none | = | = | = |
| Font | SuisseIntl 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #12161e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Backdrop filter | - | blur(8px) | = | blur(8px) |
| Painted layers | - | a.Header__NavItem-sc-i83ruj-6.kkIoGS 77.0x38.0 bg #000000 @ 0.02 r 8px shadow #000000 @ 0.25 0px 0px 1px 0px | a.Header__NavItem-sc-i83ruj-6.kkIoGS 77.0x38.0 r 8px shadow #a2c1ed 0px 0px 0px 2px | a.Header__NavItem-sc-i83ruj-6.kkIoGS 77.0x38.0 bg #000000 @ 0.02 r 8px shadow #000000 @ 0.25 0px 0px 1px 0px |

Crops: `nav-ghost-default.png`, `nav-ghost-hover.png`, `nav-ghost-focus-visible.png`, `nav-ghost-pressed.png`.

#### nav-cta

Nav CTA. The "Get started" pill (Button__StyledButton / GetStartedMenu__Trigger, white-50% fill + border) — the nav's painted CTA; it opens the GetStartedMenu dropdown whose navy "Sign up" choice renders eager but hidden, so it is not measured at rest.

Page: home. Selector: `header [class*=GetStartedMenu__Trigger]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff @ 0.5 | #ffffff | #ffffff | #ffffff |
| Box shadow | #ffffff @ 0 0px 1px 1px 0px, #575a64 @ 0.12 0px 0px 0px 1px | #000000 @ 0.15 0px 1px 1px 0px, #575a64 @ 0.2 0px 0px 0px 1px | #000000 @ 0.2 0px 1px 1px 0px, #575a64 @ 0.2 0px 0px 0px 1px, #f6f6f8 0px 0px 0px 4px | #000000 @ 0.2 0px 0px 0px 0px, #575a64 @ 0.2 0px 0px 0px 1px |
| Backdrop filter | blur(2px) | = | = | = |
| Outline | none | = | = | = |
| Font | SuisseIntl 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232730 | = | = | = |
| Text node | span.Button__ButtonText-sc-fltzk0-0.UqLjF: SuisseIntl 14px/14px 500, #232730 | = | = | = |
| Transition | box-shadow, background-color, border-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #232730 | = | = | = |
| Painted layers | button.Button__StyledButton-sc-fltzk0-1.dQTXBn 127.0x36.0 bg #ffffff @ 0.5 r 8px shadow #ffffff @ 0 0px 1px 1px 0px, #575a64 @ 0.12 0px 0px 0px 1px | button.Button__StyledButton-sc-fltzk0-1.dQTXBn 127.0x36.0 bg #ffffff r 8px shadow #000000 @ 0.15 0px 1px 1px 0px, #575a64 @ 0.2 0px 0px 0px 1px | button.Button__StyledButton-sc-fltzk0-1.dQTXBn 127.0x36.0 bg #ffffff r 8px shadow #000000 @ 0.2 0px 1px 1px 0px, #575a64 @ 0.2 0px 0px 0px 1px, #f6f6f8 0px 0px 0px 4px | button.Button__StyledButton-sc-fltzk0-1.dQTXBn 127.0x36.0 bg #ffffff r 8px shadow #000000 @ 0.2 0px 0px 0px 0px, #575a64 @ 0.2 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title. "Move, hold, and lend the dollar at scale" — the hero headline (SuisseIntl 52px, deep navy).

Page: home. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 486 x 114.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 52px/57.2px 600 |
| Letter spacing | -1.56px |
| Colour | #111a4a |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The first button under the hero copy (the "Get started"/contact pair); links onward, never followed.

Page: home. Selector: `main [class*=StyledButton] first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 98 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #111a4a | = | = | = |
| Box shadow | #111a4a 0px 0px 0px 1px, #000000 @ 0.25 0px 2px 4px 0px, #000000 @ 0.25 0px 1px 2px 0px | #111a4a 0px 0px 0px 1px, #000000 @ 0.25 0px 2px 4px 0px | #111a4a 0px 0px 0px 1px, #000000 @ 0.15 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 4px | #111a4a 0px 0px 0px 1px, #000000 @ 0.15 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | SuisseIntl 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Button__ButtonText-sc-fltzk0-0.UqLjF: SuisseIntl 14px/14px 500, #ffffff | = | = | = |
| Transition | box-shadow, background-color, border-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| ::after | 98px x 36px, absolute, bg #000000 @ 0 linear-gradient(#ffffff, #ffffff @ 0 100%), radius 8px | = | = | = |
| Painted layers | a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 98.0x36.0 bg #111a4a r 8px shadow #111a4a 0px 0px 0px 1px, #000000 @ 0.25 0px 2px 4px 0px, #000000 @ 0.25 0px 1px 2px 0px; a::after.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 98pxx36px image linear-gradient(#ffffff, #ffffff @ 0 100%) r 8px | a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 98.0x36.0 bg #111a4a r 8px shadow #111a4a 0px 0px 0px 1px, #000000 @ 0.25 0px 2px 4px 0px; a::after.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 98pxx36px image linear-gradient(#ffffff, #ffffff @ 0 100%) r 8px | a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 98.0x36.0 bg #111a4a r 8px shadow #111a4a 0px 0px 0px 1px, #000000 @ 0.15 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 4px; a::after.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 98pxx36px image linear-gradient(#ffffff, #ffffff @ 0 100%) r 8px | a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 98.0x36.0 bg #111a4a r 8px shadow #111a4a 0px 0px 0px 1px, #000000 @ 0.15 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 0px; a::after.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 98pxx36px image linear-gradient(#ffffff, #ffffff @ 0 100%) r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### stat-figure

Stat tile. A stat tile in the home stats row (_scale__StatsWrapper > Column — "$4.5T+ Annual transaction volume").

Page: home. Selector: `[class*=StatsWrapper] [class*=Column] first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 253 x 56.77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Typography__Text-sc-qr50ld-0.dTKSBX: SuisseIntl 24px/26.4px 500, #167e6c, ls -0.24px |
| Transition | none |
| How | at rest |

Crops: `stat-figure-default.png`.

#### dark-band

Dark band. The near-black navy infrastructure section ("The only bank built from the ground up for developers", #011821 ground).

Page: home. Selector: `[class*=_infrastructure__Wrapper]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1416 x 3242 |
| Padding | 0px |
| Border | none |
| Radius | 12px |
| Background | #011821 |
| Background image | radial-gradient(circle, #ffffff @ 0.075 0px, #ffffff @ 0.075 1px, #000000 @ 0 1px) |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Eyebrow__TypingText-sc-1eei7jk-2.dnBPUN: SuisseIntlMono 12px/18px 400, #88deeb |
| Transition | border-radius 0.5s ease |
| Icon | 300 x 130, colour #000000 |
| Painted layers | section._infrastructure__Wrapper-sc-1vpshqz-0.kSiwGN 1416.0x3242.0 bg #011821 image radial-gradient(circle, #ffffff @ 0.075 0px, #ffffff @ 0.075 1px, #000000 @ 0 1px) r 12px; div::after.Eyebrow__Wrapper-sc-1eei7jk-0.gncDFq 138pxx24px bg #88deeb @ 0.05 r 4px shadow #88deeb @ 0.1 0px 0px 0px 1px; span.Eyebrow__Cursor-sc-1eei7jk-3.jRxMyJ 6.0x12.0 bg #88deeb r 2px; div::after._stack__StackContainer-sc-asnsum-16.iGPgwy 1000pxx500px image radial-gradient(#011821 0px, #011821 15%, #011821 @ 0.9 25%, #011821 @ 0.7 35%, #011821 @ ; div::after._stack__StackCompany-sc-asnsum-0.kyIcqi 300pxx130px bg #011821 @ 0.01; div._stack__Key-sc-asnsum-1.dHJjms 236.0x25.0 border T:1px solid #ffffff @ 0.1 |
| How | at rest |

Crops: none.

#### dark-title

Dark band title. "Flexible building blocks built on USD" — the 48px heading inside the dark infrastructure band (white on #011821).

Page: home. Selector: `[class*=_infrastructure] h3 first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 426.66 x 105.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 48px/52.8px 500 |
| Letter spacing | -0.96px |
| Colour | #c1e8ef |
| Transition | none |
| How | at rest |

Crops: `dark-title-default.png`.

#### section-title

Section title. "Start building today" — the display section heading (SuisseIntl 60px).

Page: home. Selector: `main h2:has-text("Start building")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1072 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 60px/60px 600 |
| Letter spacing | -0.6px |
| Colour | #111a4a |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `section-title-default.png`.

#### page-ground

Page ground. The body element painted fill — the page ground.

Page: home. Selector: `document.body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 9980.73 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Typography__Text-sc-qr50ld-0.eGJccS: SuisseIntl 14px/15.4px 500, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | body.fouc-ready 1440.0x9980.7 bg #ffffff; div.Layout__Body-sc-y46uw8-0.eBqw 1440.0x9980.7 bg #f6f6f8; a.Header__LaunchBanner-sc-i83ruj-8.dXGHmi 1440.0x40.0 image linear-gradient(90deg, #3e5199 0%, #5568ad 100%); button.Button__StyledButton-sc-fltzk0-1.dQTXBn 127.0x36.0 bg #ffffff @ 0.5 r 8px shadow #ffffff @ 0 0px 1px 1px 0px, #575a64 @ 0.12 0px 0px 0px 1px; div.GetStartedMenu__Panel-sc-1vb419z-3.frtiDs 400.0x153.4 bg #ffffff r 12px shadow #000000 @ 0.024 0px 0px 0px 1px, #000000 @ 0.05 0px 16px 32px 0px, #000000 @ 0.1 0px 4px 8px 0px; a.GetStartedMenu__Choice-sc-1vb419z-5.canNmk 188.0x137.4 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| Ancestor paint | 1 up html.fouc-ready bg #ffffff |
| How | at rest |

Crops: none.

### ACH page

#### ach-title

ACH title. "Ultimate control and simplicity" — the ACH product page headline.

Page: ach. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 536 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 56px/60px 600 |
| Letter spacing | -1.12px |
| Colour | #12161e |
| Transition | none |
| How | at rest |

Crops: none.

#### section-box

Section box. A SectionBox content card on the ACH page.

Page: ach. Selector: `[class*=SectionBox__Wrapper] first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 443 |
| Padding | 72px 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff @ 0.6 |
| Box shadow | #000000 @ 0.04 0px 0px 0px 1px |
| Backdrop filter | blur(4px) |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.Heading-sc-85myk6-0.etWoiF: SuisseIntl 36px/40px 600, #12161e, ls -0.36px |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | section.SectionBox__Wrapper-sc-1yhrdnb-0.eaCpzR 1280.0x443.0 bg #ffffff @ 0.6 r 16px shadow #000000 @ 0.04 0px 0px 0px 1px; div.Code__CodeWrapper-sc-1os4h85-1.cMNxFu 524.0x231.0 bg #111a4a border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0.02 0px 40px 32px 0px, #000000 @ 0.03 0px 22px 18px 0px, #000000 @ 0.03 0px 12px 10px 0px, #000000 @ 0.04 0px 7px 5px 0px, #000000 @ 0.07 0px 3px 2px 0px; div::before.Code__CodeWrapper-sc-1os4h85-1.cMNxFu 522pxx229px image linear-gradient(#ffffff @ 0.1 0%, #ffffff @ 0.024 100%) r 8px; div.Code__CodeTitle-sc-1os4h85-0.cVCJHz 522.0x49.0 border B:1px solid #ffffff @ 0.2; button.Code__CopyButton-sc-1os4h85-7.xOBoZ 24.0x24.0 bg #111a4a @ 0.75 shadow #111a4a @ 0.75 0px 0px 8px 8px |
| How | at rest |

Crops: none.

#### product-screen

Product screen. The product-UI mock on the ACH page (ProductScreen__Wrapper — a rendered app frame inside the marketing page).

Page: ach. Selector: `[class*=ProductScreen__Wrapper] first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 430 x 530.77 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| ::before | 438.594px x 541.359px, absolute, bg #000000 @ 0 linear-gradient(132deg, #f7d8da 12%, #7ea7e9 97%), linear-gradient(132deg, #d4e3f7 12%, #c5f2d4 97%), radius 0% |
| ::after | 688px x 849.203px, absolute, bg #fbfcfd, radius 0% |
| Painted layers | div::before.ProductScreen__Wrapper-sc-1cencb3-0.blaCph 438.594pxx541.359px image linear-gradient(132deg, #f7d8da 12%, #7ea7e9 97%), linear-gradient(132deg, #d4e3f7 12%, #c r 0%; div::after.ProductScreen__Wrapper-sc-1cencb3-0.blaCph 688pxx849.203px bg #fbfcfd r 0%; div.ProductScreen__ScreenWrapper-sc-1cencb3-1.dMlVCy 430.0x530.8 bg #ffffff r 8px shadow #000000 @ 0.05 0px 0px 0px 1px, #000000 @ 0.02 0px 40px 32px 0px, #000000 @ 0.03 0px 22px 18px 0px, #000000 @ 0.03 0px 12px 10px 0px, #000000 @ 0.04 0px 7px 5px 0px, #000000 @ 0.07 0px 3px 2px 0px |
| How | at rest |

Crops: `product-screen-default.png`.

### Card programs page

#### cards-title

Cards title. The Card programs product page headline.

Page: cardprograms. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 625.33 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 56px/60px 600 |
| Letter spacing | -1.12px |
| Colour | #12161e |
| Transition | none |
| How | at rest |

Crops: `cards-title-default.png`.

#### cards-cta

Cards CTA. The first button CTA on the Card programs page; links onward, never followed.

Page: cardprograms. Selector: `main [class*=Styled*Link/Button] first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #111a4a | = | = | = |
| Box shadow | #111a4a 0px 0px 0px 1px, #000000 @ 0.25 0px 2px 4px 0px, #000000 @ 0.25 0px 1px 2px 0px | #111a4a 0px 0px 0px 1px, #000000 @ 0.25 0px 2px 4px 0px | #111a4a 0px 0px 0px 1px, #000000 @ 0.15 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 4px | #111a4a 0px 0px 0px 1px, #000000 @ 0.15 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | SuisseIntl 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Button__ButtonText-sc-fltzk0-0.UqLjF: SuisseIntl 14px/14px 500, #ffffff | = | = | = |
| Transition | box-shadow, background-color, border-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| ::after | 139px x 36px, absolute, bg #000000 @ 0 linear-gradient(#ffffff, #ffffff @ 0 100%), radius 8px | = | = | = |
| Painted layers | a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 139.0x36.0 bg #111a4a r 8px shadow #111a4a 0px 0px 0px 1px, #000000 @ 0.25 0px 2px 4px 0px, #000000 @ 0.25 0px 1px 2px 0px; a::after.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 139pxx36px image linear-gradient(#ffffff, #ffffff @ 0 100%) r 8px | a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 139.0x36.0 bg #111a4a r 8px shadow #111a4a 0px 0px 0px 1px, #000000 @ 0.25 0px 2px 4px 0px; a::after.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 139pxx36px image linear-gradient(#ffffff, #ffffff @ 0 100%) r 8px | a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 139.0x36.0 bg #111a4a r 8px shadow #111a4a 0px 0px 0px 1px, #000000 @ 0.15 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 4px; a::after.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 139pxx36px image linear-gradient(#ffffff, #ffffff @ 0 100%) r 8px | a.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 139.0x36.0 bg #111a4a r 8px shadow #111a4a 0px 0px 0px 1px, #000000 @ 0.15 0px 1px 3px 0px, #d4e3f7 0px 0px 0px 0px; a::after.Button__StyledOutboundLink-sc-fltzk0-2.bHvuWn 139pxx36px image linear-gradient(#ffffff, #ffffff @ 0 100%) r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cards-cta-default.png`, `cards-cta-hover.png`, `cards-cta-focus-visible.png`, `cards-cta-pressed.png`.

### App sign-in (boundary)

#### signin-card

Sign-in card. The dashboard.column.com login form — email field plus the Sign-in and passkey rows. Measured at rest, never submitted.

Page: signin. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 280 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #232730 |
| Text node | span.sc-2aaa72-5.krBPdO: Inter 14px/16px 400, #575a64 |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | label.sc-2aaa72-0.kRmqPU 280.0x40.0 bg #575a64 @ 0.04 r 8px shadow #2b3143 @ 0.075 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.075 0px 1px 1px 0px inset, #000000 @ 0.024 0px 2px 4px 0px inset; button::after.sc-a08sz3-0.jswqKE 280pxx32px bg #4575cd r 8px shadow #2b3143 @ 0.075 0px 0px 0px 1px inset, #4575cd @ 0.15 0px 0px 0px 0px, #000000 @ 0.25 0px -1px 0px 0px inset, #000000 @ 0.25 0px 1px 1px 0px, #000000 @ 0.1 0px 2px 4px 0px |
| How | at rest |

Crops: none.

#### signin-field

Email field. The sign-in email input — a focus reading only; nothing typed, nothing sent.

Page: signin. Selector: `input[name=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 248 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #575a64 | = |
| Transition | opacity 0.2s ease | = |
| Cursor | text | = |
| Placeholder | #afb0b3, opacity 1 | = |
| Ancestor paint | 2 up label.sc-2aaa72-0.kRmqPU bg #575a64 @ 0.04 shadow #2b3143 @ 0.075 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.075 0px 1px 1px 0px inset, #000000 @ 0.024 0px 2px 4px 0px inset | 2 up label.sc-2aaa72-0.hFoKE bg #575a64 @ 0.04 shadow #2b3143 @ 0.075 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.075 0px 1px 1px 0px inset, #000000 @ 0.024 0px 2px 4px 0px inset |
| How | at rest | clicked into the field |

Crops: none.

#### signin-submit

Sign-in button. The "Sign in"/"Continue" submit on the login form; measured never pressed — it would submit the form.

Page: signin. Selector: `form button:has-text("Sign in/Continue")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 280 x 32 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/16px 500 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.inline-flex.items-center: Inter 14px/16px 500, #ffffff, ls -0.14px | = | = | = |
| Transition | color, transform 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| ::after | 280px x 32px, absolute, bg #4575cd, radius 8px, shadow #2b3143 @ 0.075 0px 0px 0px 1px inset, #4575cd @ 0.15 0px 0px 0px 0px, #000000 @ 0.25 0px -1px 0px 0px inset, #000000 @ 0.25 0px 1px 1px 0px, #000000 @ 0.1 0px 2px 4px 0px | = | 280px x 32px, absolute, bg #4575cd, radius 8px, shadow #2b3143 @ 0.075 0px 0px 0px 1px inset, #4575cd @ 0.15 0px 0px 0px 3px, #000000 @ 0.25 0px -1px 0px 0px inset, #000000 @ 0.25 0px 1px 1px 0px, #000000 @ 0.1 0px 2px 4px 0px | = |
| Painted layers | button::after.sc-a08sz3-0.jswqKE 280pxx32px bg #4575cd r 8px shadow #2b3143 @ 0.075 0px 0px 0px 1px inset, #4575cd @ 0.15 0px 0px 0px 0px, #000000 @ 0.25 0px -1px 0px 0px inset, #000000 @ 0.25 0px 1px 1px 0px, #000000 @ 0.1 0px 2px 4px 0px | = | button::after.sc-a08sz3-0.dsdCvr 280pxx32px bg #4575cd r 8px shadow #2b3143 @ 0.075 0px 0px 0px 1px inset, #4575cd @ 0.15 0px 0px 0px 3px, #000000 @ 0.25 0px -1px 0px 0px inset, #000000 @ 0.25 0px 1px 1px 0px, #000000 @ 0.1 0px 2px 4px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-submit-hover.png`, `signin-submit-focus-visible.png`, `signin-submit-pressed.png`.

#### signin-passkey

Passkey button. The "Sign in with a passkey" row on the login form; measured never pressed.

Page: signin. Selector: `button:has-text("passkey")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 280 x 32 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/16px 500 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #575a64 | = | = | = |
| Text node | div.sc-a08sz3-3.bfVxcd: Inter 14px/16px 500, #575a64, ls -0.14px | = | = | = |
| Transition | color, transform 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #575a64 | = | = | = |
| ::after | 278px x 30px, absolute, bg #ffffff, radius 8px, shadow #2b3143 @ 0.075 0px 0px 0px 1px, #4575cd @ 0.15 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 1px 0px, #000000 @ 0.075 0px 2px 4px 0px | = | = | = |
| Painted layers | button::after.sc-a08sz3-0.cNPJAo 278pxx30px bg #ffffff r 8px shadow #2b3143 @ 0.075 0px 0px 0px 1px, #4575cd @ 0.15 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 1px 0px, #000000 @ 0.075 0px 2px 4px 0px | = | button::after.sc-a08sz3-0.bEKcVr 278pxx30px bg #ffffff r 8px shadow #2b3143 @ 0.075 0px 0px 0px 1px, #4575cd @ 0.15 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 1px 0px, #000000 @ 0.075 0px 2px 4px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-passkey-default.png`.

### Footer

#### footer

Footer. The closer band at the page bottom (light grey, #eeeff2): link columns, the Column logo and legal copy.

Page: home. Selector: `[class*=_closer__Wrapper]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1416 x 1074.38 |
| Padding | 0px |
| Border | 1px solid #e3e4e8 |
| Radius | 12px |
| Background | #eeeff2 |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.Typography__Text-sc-qr50ld-0.fTFZBq: SuisseIntl 60px/60px 600, #111a4a, ls -0.6px |
| Transition | border-radius 0.5s ease |
| Cursor | default |
| Icon | 125 x 28.63, colour #000000 |
| ::after | 1414px x 1072.38px, absolute, bg #000000 @ 0 linear-gradient(#eeeff2 0%, #eeeff2 55%, #000000 @ 0 100%), radius 0px |
| Painted layers | div._closer__Wrapper-sc-jov7sq-0.lkfxlE 1416.0x1074.4 bg #eeeff2 border T:1px solid #e3e4e8 / R:1px solid #e3e4e8 / B:1px solid #e3e4e8 / L:1px solid #e3e4e8 r 12px; div::after._closer__Wrapper-sc-jov7sq-0.lkfxlE 1414pxx1072.38px image linear-gradient(#eeeff2 0%, #eeeff2 55%, #000000 @ 0 100%); div._closer__PatternOverlay-sc-jov7sq-2.iXTVbv 1414.0x1072.4 image linear-gradient(125deg, #d65620 -3.16%, #9f7aee 14.55%, #4575cd 32.26%, #71d2f0 49.97%, #4; a._closer__CardLink-sc-jov7sq-4.czbWQZ 344.0x209.0 bg #ffffff @ 0.25 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 8px shadow #000000 @ 0.1 0px 1px 2px 0px; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50% |
| How | at rest |

Crops: none.

#### footer-link

Footer card link. The closer band’s card link (_closer__CardLink — "Documentation / Get started" tiles, white-25% fill + 1px white ring).

Page: home. Selector: `footer closer CardLink first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344 x 208.98 | = | = | = |
| Padding | 24px 32px 32px 32px | = | = | = |
| Gap | 48px | = | = | = |
| Border | 1px solid #ffffff | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff @ 0.25 | = | = | = |
| Box shadow | #000000 @ 0.1 0px 1px 2px 0px | = | = | = |
| Backdrop filter | blur(12px) | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | SuisseIntl 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h4.Typography__Text-sc-qr50ld-0.hEcRJK: SuisseIntl 16px/17.6px 600, #111a4a | = | = | = |
| Transition | background 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a._closer__CardLink-sc-jov7sq-4.czbWQZ 344.0x209.0 bg #ffffff @ 0.25 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 8px shadow #000000 @ 0.1 0px 1px 2px 0px; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50% | = | a._closer__CardLink-sc-jov7sq-4.czbWQZ 344.0x209.0 bg #ffffff @ 0.25 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 8px shadow #000000 @ 0.1 0px 1px 2px 0px outline 1px auto #101010 offset 1px; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 2.0x2.0 bg #4575cd r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`.

#### footer-logo

Footer logo. The Column logo block inside the footer band (_footer__FooterLogoContainer).

Page: home. Selector: `[class*=_footer__FooterLogoContainer]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 125 x 28.63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/0px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 125 x 28.63, colour #000000 |
| Painted layers | div._footer__HolographicOverlay-sc-3qrn5b-4.ezcnIC 125.0x28.6 image linear-gradient(90deg, #000000 @ 0 0%, #94efb7 @ 0.2 25%, #71d2f0 @ 0.4 45%, #4575cd @ 0.3 |
| How | at rest |

Crops: none.

### Mobile (390 wide)

#### m-header

Mobile bar. The 390 mobile nav bar (Header__SiteHeader): logo and the menu toggle, under the launch banner row.

Page: home. Selector: `header[class*=SiteHeader]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 45 |
| Padding | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #12161e |
| Transition | transform, box-shadow, background 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s |
| Icon | 72.83 x 16, colour #12161e, fill #000000 |
| Painted layers | button.Button__StyledButton-sc-fltzk0-1.dQTXBn 0.0x0.0 bg #ffffff @ 0.5 r 8px shadow #ffffff @ 0 0px 1px 1px 0px, #575a64 @ 0.12 0px 0px 0px 1px; div.GetStartedMenu__Panel-sc-1vb419z-3.frtiDs 0.0x0.0 bg #ffffff r 12px shadow #000000 @ 0.024 0px 0px 0px 1px, #000000 @ 0.05 0px 16px 32px 0px, #000000 @ 0.1 0px 4px 8px 0px; a.GetStartedMenu__Choice-sc-1vb419z-5.canNmk 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 0.0x0.0 bg #7ea7e9 r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 0.0x0.0 bg #7ea7e9 r 50%; div.DotGridIcon__Dot-sc-ws0s75-1.lktAvq 0.0x0.0 bg #7ea7e9 r 50% |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger (Header__MobileNavToggle, aria-label "Open menu"); its own press opens the menu.

Page: home. Selector: `[class*=MobileNavToggle]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 16 x 18.42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 12px/18px 500 |
| Letter spacing | normal |
| Colour | #12161e |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #12161e |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The menu overlay after the hamburger press.

Page: home. Selector: `opened mobile menu overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 799 |
| Padding | 4px 4px 0px 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #12161e |
| Text node | h3.MobileMenu__Section-sc-1ksm2t0-2.jHXbkc: SuisseIntl 14px/20px 500, #12161e |
| Transition | none |
| Icon | 16 x 16, colour #12161e |
| Painted layers | div.MobileMenu__Panel-sc-1ksm2t0-0.hwMZyc 382.0x759.0 bg #ffffff r 12px shadow #000000 @ 0.024 0px 0px 0px 1px, #000000 @ 0.05 0px 16px 32px 0px, #000000 @ 0.1 0px 4px 8px 0px; hr.MobileMenu__Rule-sc-1ksm2t0-5.fzhOVg 342.0x1.0 border T:1px solid #eeeff2; hr.MobileMenu__Rule-sc-1ksm2t0-5.fzhOVg 342.0x1.0 border T:1px solid #eeeff2; div.MobileMenu__Footer-sc-1ksm2t0-6.gqEOjj 382.0x77.0 bg #ffffff border T:1px solid #eeeff2; a.MobileMenu__Btn-sc-1ksm2t0-7.ejIHAe 167.0x44.0 r 8px shadow #e3e4e8 0px 0px 0px 1px inset; button.MobileMenu__Btn-sc-1ksm2t0-7.fSwosC 167.0x44.0 bg #12161e r 8px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-link

Menu link. A link/accordion row inside the open mobile menu.

Page: home. Selector: `first row inside the open menu`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 342 x 42 | = | = | = |
| Padding | 10px 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | SuisseIntl 16px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #12161e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #12161e | = | = | = |
| Ancestor paint | 3 up div.MobileMenu__Panel-sc-1ksm2t0-0.hwMZyc bg #ffffff shadow #000000 @ 0.024 0px 0px 0px 1px, #000000 @ 0.05 0px 16px 32px 0px, #000000 @ 0.1 0px 4px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.MobileMenu__Row-sc-1ksm2t0-4.jAtTwx 342.0x42.0 outline 1px auto #e59700 offset 1px | = |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile headline. The hero headline at 390.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 70.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SuisseIntl 32px/35.2px 600 |
| Letter spacing | -0.32px |
| Colour | #111a4a |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `box-shadow 0.2s, background-color 0.2s, border-color 0.2s`, `opacity 0.5s`, `opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.2s`, `background-color 0.1s ease-out`, `transform 0.3s, box-shadow 0.3s, background 0.3s`, `none`, `filter 0.2s`, `colors 0.2s`, `transform 0.15s`, `stroke-dashoffset 0.15s, transform 0.15s`, `box-shadow 0.2s, border-color 0.2s`, `box-shadow 0.2s, border-color 0.2s, background-color 0.2s`
