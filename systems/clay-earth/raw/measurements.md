# Component measurements

Computed styles read from me.sh (clay.earth's redirect target — the Clay product rebranded to Mesh) on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's dark theme (the pricing route and app.me.sh sign-in card are warm light surfaces; no consent overlay mounts), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Nav pill. The floating top nav: wordmark, the Releases/Resources/Company dropdowns, Pricing link and Sign In.

Page: home. Selector: `div.y0DxmG_nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 388 x 48 |
| Padding | 0px 24px |
| Border | none |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.7 |
| Text node | button.y0DxmG_navigationLink: Verlag 12px/27px 700, #ffffff, ls 1px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -194, 0) |
| Icon | 40 x 40, colour #ffffff, fill #000000 |
| ::before | 388px x 48px, absolute, bg #ffffff @ 0.03 linear-gradient(#ffffff @ 0.12 10%, #ffffff @ 0 86%), radius 16px, shadow #000000 @ 0.06 0px 0px 0px 0.5px, #000000 @ 0.1 0px 2px 4px -2px, #000000 @ 0.06 0px 8px 16px -8px, #ffffff @ 0.03 0px 1px 0px 0px inset, #ffffff @ 0.03 0px -1px 0px 0px inset, #ffffff @ 0.03 0px -5px 6px 0px inset, #ffffff @ 0.03 0px -8px 24px 0px inset |
| ::after | 388px x 48px, absolute, bg #000000 @ 0 linear-gradient(#272727, #111111), radius 16px, shadow #000000 @ 0.08 0px 2px 4px -2px, #000000 @ 0.03 0px 8px 16px -8px, #ffffff @ 0.03 0px 1px 0px 0px inset, #ffffff @ 0.03 0px -1px 0px 0px inset, #ffffff @ 0.03 0px -5px 6px 0px inset, #ffffff @ 0.03 0px -8px 24px 0px inset |
| Painted layers | div::before.y0DxmG_nav 388pxx48px bg #ffffff @ 0.03 image linear-gradient(#ffffff @ 0.12 10%, #ffffff @ 0 86%) r 16px shadow #000000 @ 0.06 0px 0px 0px 0.5px, #000000 @ 0.1 0px 2px 4px -2px, #000000 @ 0.06 0px 8px 16px -8px, #ffffff @ 0.03 0px 1px 0px 0px inset, #ffffff @ 0.03 0px -1px 0px 0px inset, #ffffff @ 0.03 0px -5px 6px 0px inset, #ffffff @ 0.03 0px -8px 24px 0px inset; div::after.y0DxmG_nav 388pxx48px image linear-gradient(#272727, #111111) r 16px shadow #000000 @ 0.08 0px 2px 4px -2px, #000000 @ 0.03 0px 8px 16px -8px, #ffffff @ 0.03 0px 1px 0px 0px inset, #ffffff @ 0.03 0px -1px 0px 0px inset, #ffffff @ 0.03 0px -5px 6px 0px inset, #ffffff @ 0.03 0px -8px 24px 0px inset; a.hGEQua_imageLink 254.0x214.4 bg #ffffff @ 0.12 border T:1px solid #ffffff @ 0.06 / R:1px solid #ffffff @ 0.06 / B:1px solid #ffffff @ 0.06 / L:1px solid #ffffff @ 0.06 r 12px; a::after.hGEQua_imageLink 27pxx10px bg #ffffff border T:1px solid #1f1f1f @ 0.06 / R:1px solid #1f1f1f @ 0.06 / B:1px solid #1f1f1f @ 0.06 / L:1px solid #1f1f1f @ 0.06 r 6px shadow #000000 @ 0.06 0px 1px 3px 0px, #ffffff @ 0.5 0px 0px 1px 0px inset; div.img.Z2phqG_imgContainer 252.0x163.4 border B:1px solid #ffffff @ 0.06 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Mesh wordmark anchor.

Page: home. Selector: `a[href=me.sh/]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #f2b98b |
| Transition | color 0.15s ease-in-out |
| Cursor | pointer |
| Icon | 114 x 26, colour #f2b98b, fill #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. A plain nav link (Pricing).

Page: home. Selector: `nav a[href=/pricing]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57 x 27 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Verlag 12px/27px 700 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.y0DxmG_linkTitle: Verlag 12px/27px 700, #ffffff, ls 1px | = | = | = |
| Transition | opacity, color 0.1s, 0.24s ease-in-out, ease delay 0s, 0s | = | = | = |
| Opacity | 0.64 | - | = | - |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-dropdown

Nav dropdown. A nav dropdown trigger (the Releases/Resources/Company buttons); its own press opens the link menu (opened state).

Page: home. Selector: `button.y0DxmG_navigationLink`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 64 x 27 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Verlag 12px/27px 700 | = | = | = | = |
| Letter spacing | 1px | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Transition | opacity, color 0.1s, 0.24s ease-in-out, ease delay 0s, 0s | = | = | = | = |
| Opacity | 0.64 | - | = | - | - |
| Cursor | default | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `nav-dropdown-default.png`, `nav-dropdown-hover.png`, `nav-dropdown-focus-visible.png`, `nav-dropdown-pressed.png`, `nav-dropdown-opened.png`.

#### menu-panel

Nav menu. The opened nav dropdown panel, held open by the trigger toggle.

Page: home. Selector: `dropdown panel under the open trigger`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 556 x 154 |
| Padding | 0px 24px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.7 |
| Text node | a._4Zfkmq_newNavLink: Verlag 14px/14px 700, #ffffff, ls 1px |
| Transition | opacity 0.15s ease-in-out |
| Transform | matrix(1, 0, 0, 1, -278, 0) |
| Opacity | 0 |
| How | at rest |

Crops: `menu-panel-default.png`.

#### menu-card

Menu item. A link row inside the open nav menu.

Page: home. Selector: `first link inside the open dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 238 x 14 |
| Padding | 0px |
| Gap | 2px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Verlag 14px/14px 700 |
| Letter spacing | 1px |
| Colour | #ffffff |
| Transition | color 0.1s ease-in-out |
| Cursor | pointer |
| ::after | 13px x 12px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `menu-card-default.png`.

#### nav-cta

Nav CTA. The "Get Started" action inside the nav pill; links to /start, measured never followed.

Page: home. Selector: `.y0DxmG_ctaWrapper`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123 x 32.03 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Verlag 18px/27px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff @ 0.7 | = | - | = |
| Text node | div.eoWgla_ctaInner: Verlag 12px/12px 600, #ffffff, ls 1px | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.eoWgla_cta.y0DxmG_cta 123.0x32.0 r 8px shadow #ffffff @ 0.24 0px 0px 0px 1px inset; div::after.eoWgla_cta.y0DxmG_cta calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%) r 100%; div::before.eoWgla_ctaInner calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%); div::after.eoWgla_ctaInner 100%x100% image linear-gradient(135deg, #ffffff, #b6b6b6 150%) | div.eoWgla_cta.y0DxmG_cta 123.0x32.0 bg #ffffff @ 0.04 r 8px shadow #ffffff @ 0.24 0px 0px 0px 1px inset; div::after.eoWgla_cta.y0DxmG_cta calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%) r 100%; div::before.eoWgla_ctaInner calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%); div::after.eoWgla_ctaInner 100%x100% image linear-gradient(135deg, #ffffff, #b6b6b6 150%) | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-pressed.png`.

#### nav-signin

Sign-in link. The "Sign In" action in the nav pill; links to app.me.sh/login, measured never followed.

Page: home. Selector: `.y0DxmG_signInBtn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83 x 34 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Verlag 12px/0px 700 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #ffffff @ 0.64 | #ffffff | = | #ffffff @ 0.976 |
| Transition | background-color, color 0.2s, 0.24s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 83px x 34px, absolute, bg #000000 @ 0, radius 8px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.y0DxmG_signInBtn 83.0x34.0 bg #ffffff @ 0.08 r 8px | a.y0DxmG_signInBtn 83.0x34.0 r 8px outline 1px auto #101010 offset 1px | a.y0DxmG_signInBtn 83.0x34.0 bg #ffffff @ 0.08 r 8px |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

### Home

#### hero-title

Hero title. "Every relationship, organized." — the VerlagCondensed display headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1232 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | VerlagCondensed 64px/64px 700 |
| Letter spacing | 0.88px |
| Colour | #fefef7 |
| Text node | undefined: VerlagCondensed 64px/64px 700, #fefef7, ls 0.88px |
| Transition | none |
| Ancestor paint | 1 up section.IQmOHa_hero.btQYOq_dark bg #0f0f10 |
| How | at rest |

Crops: `hero-title-default.png`.

#### section-title

Section title. "Never miss what matters." — the first section heading (Verlag, 480x48); the hero carries no lede, only the display h1 and an animated stat counter.

Page: home. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | VerlagCondensed 48px/48px 900 |
| Letter spacing | 0.66px |
| Colour | #1d1d1f |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### stat-counter

Stat counter. One digit of the animated relationship-count ticker beside the hero (the digits cycle).

Page: home. Selector: `.IQmOHa_animatedDigit`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 8 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Verlag 18px/18px 700 |
| Letter spacing | 1px |
| Colour | #ffffff |
| Text node | span: Verlag 18px/18px 700, #ffffff, ls 1px |
| Transition | none |
| How | at rest |

Crops: `stat-counter-default.png`.

#### cta

Hero CTA. The "Get Mesh Free" pill — the painted 205x54 off-white inner of the hero CTA; the anchor links to /start, never followed.

Page: home. Selector: `.IQmOHa_mainCTA .eoWgla_ctaInner`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 205 x 54 | 202.95 x 53.46 | - | = |
| Padding | 0px 27px | = | - | = |
| Border | none | = | - | = |
| Radius | 14px | = | - | = |
| Background | #fdfcfa | = | - | = |
| Box shadow | #ffffff @ 0.98 0px 0px 4px 1px | = | - | = |
| Outline | none | = | - | = |
| Font | Verlag 18px/18px 600 | = | - | = |
| Letter spacing | 1px | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | transform 0.35s ease | = | - | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(0.99, 0, 0, 0.99, 0, 0) | - | = |
| Cursor | pointer | = | - | = |
| ::before | calc(100% + 54px) x calc(100% + 18px), absolute, bg #000000 @ 0 linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%), radius 0px | = | - | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0 linear-gradient(135deg, #ffffff, #b6b6b6 150%), radius 0px | = | - | = |
| Painted layers | div.eoWgla_ctaInner 205.0x54.0 bg #fdfcfa r 14px shadow #ffffff @ 0.98 0px 0px 4px 1px; div::before.eoWgla_ctaInner calc(100% + 54px)xcalc(100% + 18px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%); div::after.eoWgla_ctaInner 100%x100% image linear-gradient(135deg, #ffffff, #b6b6b6 150%) | div.eoWgla_ctaInner 202.9x53.5 bg #fdfcfa r 14px shadow #ffffff @ 0.98 0px 0px 4px 1px; div::before.eoWgla_ctaInner calc(100% + 54px)xcalc(100% + 18px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%); div::after.eoWgla_ctaInner 100%x100% image linear-gradient(135deg, #ffffff, #b6b6b6 150%) | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `cta-default.png`, `cta-hover.png`, `cta-pressed.png`.

#### cta-bottom

Bottom CTA. The "Get Mesh Free" pill closing the page — a white 185x52 button on the #0f0f10 bottom band; never followed.

Page: home. Selector: `.JzsFla_ctaButton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 185 x 52 | 181.3 x 50.96 | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 16px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Verlag 16px/27px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #f2b98b | #efab74 | - | = |
| Text node | div.eoWgla_ctaInner: Verlag 16px/16px 600, #000000, ls 1px | = | - | = |
| Transition | background-color 0.15s ease-in-out | = | - | = |
| Cursor | pointer | = | - | = |
| ::after | calc(100% + 48px) x calc(100% + 16px), absolute, bg #000000 @ 0 linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%), radius 100% | = | - | = |
| Painted layers | div.eoWgla_cta.JzsFla_ctaButton 185.0x52.0 bg #ffffff r 16px; div::after.eoWgla_cta.JzsFla_ctaButton calc(100% + 48px)xcalc(100% + 16px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%) r 100%; div::before.eoWgla_ctaInner calc(100% + 48px)xcalc(100% + 16px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%); div::after.eoWgla_ctaInner 100%x100% image linear-gradient(135deg, #ffffff, #b6b6b6 150%) | div.eoWgla_cta.JzsFla_ctaButton 181.3x51.0 bg #ffffff r 16px; div::after.eoWgla_cta.JzsFla_ctaButton calc(100% + 48px)xcalc(100% + 16px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%) r 100%; div::before.eoWgla_ctaInner calc(100% + 48px)xcalc(100% + 16px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%); div::after.eoWgla_ctaInner 100%x100% image linear-gradient(135deg, #ffffff, #b6b6b6 150%) | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `cta-bottom-default.png`, `cta-bottom-hover.png`, `cta-bottom-pressed.png`.

#### filter-button

Feature pill. A feature filter pill (Birthdays/Events/News/…); its press swaps the demo panel — a local toggle.

Page: home. Selector: `._9nEsHa_filterButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 480 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Verlag 20px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1d1d1f | = | = | = |
| Transition | opacity 0.15s ease-in-out | = | = | = |
| Opacity | 0.6 | - | = | - |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #1d1d1f | = | = | = |
| ::after | 492px x 48px, absolute, bg #000000 @ 0 linear-gradient(90deg, #1d1d1f @ 0.06 0%, #1d1d1f @ 0.03 100%), radius 16px | = | = | = |
| Painted layers | button::after._9nEsHa_filterButton_Birthdays 492pxx48px image linear-gradient(90deg, #1d1d1f @ 0.06 0%, #1d1d1f @ 0.03 100%) r 16px | = | button._9nEsHa_filterButton_Birthdays 480.0x48.0 outline 1px auto #101010 offset 0px; button::after._9nEsHa_filterButton_Birthdays 492pxx48px image linear-gradient(90deg, #1d1d1f @ 0.06 0%, #1d1d1f @ 0.03 100%) r 16px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-button-default.png`, `filter-button-hover.png`, `filter-button-focus-visible.png`, `filter-button-pressed.png`.

#### page-ground

Page ground. The html element's own painted fill — the black ground under every section (body itself is transparent).

Page: home. Selector: `document.documentElement`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 8016.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 18px/27px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.7 |
| Text node | button.y0DxmG_navigationLink: Verlag 12px/27px 700, #1f1f1f, ls 1px |
| Transition | none |
| Icon | 114 x 26, colour #f2b98b, fill #000000 |
| Painted layers | html 1440.0x8017.0 bg #000000; div::before.y0DxmG_nav 388pxx48px bg #ffffff @ 0.12 image linear-gradient(#ffffff @ 0.8 7%, #ffffff @ 0 86%) r 16px shadow #000000 @ 0.06 0px 0px 0px 0.5px, #000000 @ 0.08 0px 2px 4px -2px, #000000 @ 0.03 0px 8px 16px -8px, #ffffff 0px 1px 0px 0px inset, #ffffff @ 0.24 0px -1px 0px 0px inset, #ffffff @ 0.5 0px -5px 6px 0px inset, #ffffff @ 0.12 0px -8px 24px 0px inset; div::after.y0DxmG_nav 388pxx48px image linear-gradient(#ffffff, #f8f8f8) r 16px shadow #000000 @ 0.06 0px 0px 0px 0.5px, #000000 @ 0.08 0px 2px 4px -2px, #000000 @ 0.03 0px 8px 16px -8px, #ffffff @ 0.5 0px -5px 6px 0px inset, #ffffff @ 0.12 0px -8px 24px 0px inset; a.hGEQua_imageLink 254.0x214.4 bg #ffffff @ 0.12 border T:1px solid #1f1f1f @ 0.06 / R:1px solid #1f1f1f @ 0.06 / B:1px solid #1f1f1f @ 0.06 / L:1px solid #1f1f1f @ 0.06 r 12px; a::after.hGEQua_imageLink 27pxx10px bg #ffffff border T:1px solid #1f1f1f @ 0.06 / R:1px solid #1f1f1f @ 0.06 / B:1px solid #1f1f1f @ 0.06 / L:1px solid #1f1f1f @ 0.06 r 6px shadow #000000 @ 0.06 0px 1px 3px 0px, #ffffff @ 0.5 0px 0px 1px 0px inset; div.img.Z2phqG_imgContainer 252.0x163.4 border B:1px solid #1f1f1f @ 0.06 |
| How | at rest |

Crops: none.

#### hero-sub

Hero subcopy. "Mesh brings together everyone you've ever met…" — the serif lede under the display headline.

Page: home. Selector: `first p after h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Verlag 20px/28px 400 |
| Letter spacing | normal |
| Colour | #86868b |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

### Pricing

#### pricing-h1

Pricing title. "Invest in better relationships" — the pricing page display heading.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 590 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | VerlagCondensed 48px/56px 700 |
| Letter spacing | 0.66px |
| Colour | #1f1f1f |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### plan-card

Plan card. A plan card (the Personal column); translucent gray fill on black.

Page: pricing. Selector: `._3K18mq_card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 288 x 196 | = |
| Padding | 22px 24px 24px 24px | = |
| Gap | 12px | = |
| Border | 1px solid #eceae8 | = |
| Radius | 16px | = |
| Background | #959595 @ 0.06 | = |
| Background image | linear-gradient(#ffffff, #ffffff @ 0.5) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Verlag 18px/27px 400 | = |
| Letter spacing | normal | = |
| Colour | #1f1f1f | = |
| Text node | div._3K18mq_planLabel: Verlag 14px/14px 600, #fb7232, ls 1px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 286 x 194, colour #1f1f1f, fill #000000 | = |
| ::before | 286px x 194px, absolute, bg #000000 @ 0, radius 16px, shadow #a5a098 @ 0.16 0px 4px 8px -2px, #ffffff @ 0.5 0px -10px 6px 0px inset, #ffffff @ 0.24 0px -16px 24px 0px inset | = |
| ::after | 286px x 194px, absolute, bg #000000 @ 0, radius 16px, shadow #ed7239 @ 0.18 0px 16px 24px 0px, #000000 @ 0.08 0px 4px 8px -2px | = |
| Painted layers | div._3K18mq_card 288.0x196.0 bg #959595 @ 0.06 image linear-gradient(#ffffff, #ffffff @ 0.5) border T:1px solid #eceae8 / R:1px solid #eceae8 / B:1px solid #eceae8 / L:1px solid #eceae8 r 16px; div::before._3K18mq_card 286pxx194px r 16px shadow #a5a098 @ 0.16 0px 4px 8px -2px, #ffffff @ 0.5 0px -10px 6px 0px inset, #ffffff @ 0.24 0px -16px 24px 0px inset; div::after._3K18mq_card 286pxx194px r 16px shadow #ed7239 @ 0.18 0px 16px 24px 0px, #000000 @ 0.08 0px 4px 8px -2px; div.htJ5kW_button 238.0x44.0 border T:1px solid #1f1f1f @ 0.4 / R:1px solid #1f1f1f @ 0.4 / B:1px solid #1f1f1f @ 0.4 / L:1px solid #1f1f1f @ 0.4 r 10px | = |
| How | at rest | mouse hover |

Crops: `plan-card-default.png`, `plan-card-hover.png`.

#### plan-card-popular

Popular plan card. The Team plan card with the Popular tag.

Page: pricing. Selector: `._3K18mq_card._3K18mq_popular`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 196 |
| Padding | 22px 24px 24px 24px |
| Gap | 12px |
| Border | 1px solid #fb7232 |
| Radius | 16px |
| Background | #959595 @ 0.06 |
| Background image | linear-gradient(#ffffff, #ffffff @ 0.5) |
| Box shadow | #fb7232 @ 0.24 0px 0px 0px 3px |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | div._3K18mq_planLabel: Verlag 14px/14px 600, #fb7232, ls 1px |
| Transition | none |
| Cursor | pointer |
| Icon | 286 x 194, colour #1f1f1f, fill #000000 |
| ::before | 286px x 194px, absolute, bg #000000 @ 0, radius 16px, shadow #a5a098 @ 0.16 0px 4px 8px -2px, #ffffff @ 0.5 0px -10px 6px 0px inset, #ffffff @ 0.24 0px -16px 24px 0px inset |
| ::after | 286px x 194px, absolute, bg #000000 @ 0, radius 16px, shadow #ed7239 @ 0.18 0px 16px 24px 0px, #000000 @ 0.08 0px 4px 8px -2px |
| Painted layers | div._3K18mq_card._3K18mq_popular 288.0x196.0 bg #959595 @ 0.06 image linear-gradient(#ffffff, #ffffff @ 0.5) border T:1px solid #fb7232 / R:1px solid #fb7232 / B:1px solid #fb7232 / L:1px solid #fb7232 r 16px shadow #fb7232 @ 0.24 0px 0px 0px 3px; div::before._3K18mq_card._3K18mq_popular 286pxx194px r 16px shadow #a5a098 @ 0.16 0px 4px 8px -2px, #ffffff @ 0.5 0px -10px 6px 0px inset, #ffffff @ 0.24 0px -16px 24px 0px inset; div::after._3K18mq_card._3K18mq_popular 286pxx194px r 16px shadow #ed7239 @ 0.18 0px 16px 24px 0px, #000000 @ 0.08 0px 4px 8px -2px; span._3K18mq_annualSavings._3K18mq_shown 38.0x20.0 bg #fb7232 @ 0.12 r 4px; div.htJ5kW_button.htJ5kW_popular 238.0x44.0 bg #fb7232 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px; div::after.htJ5kW_button.htJ5kW_popular 238pxx44px bg #ffffff @ 0.08 r 10px |
| How | at rest |

Crops: `plan-card-popular-default.png`.

#### plan-price

Plan price. The "Free"/"$10/ month" price line inside a plan card.

Page: pricing. Selector: `.tnESpa_planPrice`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 238 x 56 |
| Padding | 0px 0px 0px 4px |
| Gap | 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | div.tnESpa_cost: ChronicleCondensed 56px/56px 400, #1f1f1f |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up div._3K18mq_card bg #959595 @ 0.06 |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. The "Get Started" outline action inside the Personal plan card (a button-styled div, 238x44); measured in all non-submitting states, never followed.

Page: pricing. Selector: `.htJ5kW_button inside a plan card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 238 x 44 | = | - | = |
| Padding | 0px | = | - | = |
| Border | 1px solid #1f1f1f @ 0.4 | 1px solid #000000 @ 0 | - | 1px solid #000000 @ 0 |
| Radius | 10px | = | - | = |
| Background | transparent | #fb7232 | - | #fb7232 |
| Box shadow | none | = | - | = |
| Backdrop filter | saturate(1.6) blur(12px) | = | - | = |
| Outline | none | = | - | = |
| Font | Verlag 14px/27px 600 | = | - | = |
| Letter spacing | 1px | = | - | = |
| Colour | #1f1f1f | #ffffff | - | #ffffff |
| Transition | background-color, color, border-color 0.15s, 0.15s, 0.15s ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | div.htJ5kW_button 238.0x44.0 border T:1px solid #1f1f1f @ 0.4 / R:1px solid #1f1f1f @ 0.4 / B:1px solid #1f1f1f @ 0.4 / L:1px solid #1f1f1f @ 0.4 r 10px | div.htJ5kW_button 238.0x44.0 bg #fb7232 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px | - | div.htJ5kW_button 238.0x44.0 bg #fb7232 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px |
| Ancestor paint | 1 up div._3K18mq_card bg #959595 @ 0.06 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-pressed.png`.

#### plan-cta-filled

Plan CTA, filled. The filled orange "Try it free" action inside the popular Team card; never pressed for real.

Page: pricing. Selector: `.htJ5kW_button inside _3K18mq_popular`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 238 x 44 | = | - | = |
| Padding | 0px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 10px | = | - | = |
| Background | #fb7232 | = | - | = |
| Box shadow | none | = | - | = |
| Backdrop filter | saturate(1.6) blur(12px) | = | - | = |
| Outline | none | = | - | = |
| Font | Verlag 14px/27px 600 | = | - | = |
| Letter spacing | 1px | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | background-color, color, border-color 0.15s, 0.15s, 0.15s ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s | = | - | = |
| Cursor | pointer | = | - | = |
| ::after | 238px x 44px, absolute, bg #ffffff @ 0.08, radius 10px | = | - | = |
| Painted layers | div.htJ5kW_button.htJ5kW_popular 238.0x44.0 bg #fb7232 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 10px; div::after.htJ5kW_button.htJ5kW_popular 238pxx44px bg #ffffff @ 0.08 r 10px | = | - | = |
| Ancestor paint | 1 up div._3K18mq_card._3K18mq_popular bg #959595 @ 0.06 shadow #fb7232 @ 0.24 0px 0px 0px 3px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `plan-cta-filled-default.png`, `plan-cta-filled-hover.png`, `plan-cta-filled-pressed.png`.

#### billing-toggle

Billing toggle. The "Pay monthly / Pay annually" switcher above the plan cards (226x40, gray-chip fill); a local toggle, never flipped.

Page: pricing. Selector: `.iVr8Iq_toggle`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 226 x 40 |
| Padding | 0px 6px |
| Border | none |
| Radius | 12px |
| Background | #1f1f1f @ 0.06 |
| Box shadow | none |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | div.EQVBJG_option.EQVBJG_monthlyOption: Verlag 10px/27px 600, #1f1f1f @ 0.5, ls 1px |
| Transition | none |
| Painted layers | div.iVr8Iq_toggle.EQVBJG_toggle 226.0x40.0 bg #1f1f1f @ 0.06 r 12px; div.EQVBJG_border 105.0x28.0 bg #ffffff border T:1px solid #1f1f1f @ 0.06 / R:1px solid #1f1f1f @ 0.06 / B:1px solid #1f1f1f @ 0.06 / L:1px solid #1f1f1f @ 0.06 r 8px shadow #000000 @ 0.06 0px 1px 3px 0px, #ffffff @ 0.5 0px 0px 1px 0px inset; div.EQVBJG_border 109.0x28.0 bg #ffffff border T:1px solid #1f1f1f @ 0.06 / R:1px solid #1f1f1f @ 0.06 / B:1px solid #1f1f1f @ 0.06 / L:1px solid #1f1f1f @ 0.06 r 8px shadow #000000 @ 0.06 0px 1px 3px 0px, #ffffff @ 0.5 0px 0px 1px 0px inset |
| How | at rest |

Crops: `billing-toggle-default.png`.

#### plan-name

Plan label. The PERSONAL/PRO/TEAM eyebrow label on a plan card.

Page: pricing. Selector: `._3K18mq_planLabel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 238 x 14 |
| Padding | 0px 0px 0px 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Verlag 14px/14px 600 |
| Letter spacing | 1px |
| Colour | #fb7232 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up div._3K18mq_card bg #959595 @ 0.06 |
| How | at rest |

Crops: `plan-name-default.png`.

#### pricing-ground

Pricing ground. The pricing page's warm-cream main surface (#f9f8f6) — pricing is a light route on the otherwise-dark site.

Page: pricing. Selector: `main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 2386 |
| Padding | 60px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #f9f8f6 |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #1f1f1f |
| Text node | button.y0DxmG_navigationLink: Verlag 12px/27px 700, #1f1f1f, ls 1px |
| Transition | none |
| Icon | 114 x 26, colour #f2b98b, fill #000000 |
| Painted layers | main.main.withAutomatticFooter 1440.0x2386.0 bg #f9f8f6; div::before.y0DxmG_nav 388pxx48px bg #ffffff @ 0.12 image linear-gradient(#ffffff @ 0.8 7%, #ffffff @ 0 86%) r 16px shadow #000000 @ 0.06 0px 0px 0px 0.5px, #000000 @ 0.08 0px 2px 4px -2px, #000000 @ 0.03 0px 8px 16px -8px, #ffffff 0px 1px 0px 0px inset, #ffffff @ 0.24 0px -1px 0px 0px inset, #ffffff @ 0.5 0px -5px 6px 0px inset, #ffffff @ 0.12 0px -8px 24px 0px inset; div::after.y0DxmG_nav 388pxx48px image linear-gradient(#ffffff, #f8f8f8) r 16px shadow #000000 @ 0.06 0px 0px 0px 0.5px, #000000 @ 0.08 0px 2px 4px -2px, #000000 @ 0.03 0px 8px 16px -8px, #ffffff @ 0.5 0px -5px 6px 0px inset, #ffffff @ 0.12 0px -8px 24px 0px inset; a.hGEQua_imageLink 254.0x214.4 bg #ffffff @ 0.12 border T:1px solid #1f1f1f @ 0.06 / R:1px solid #1f1f1f @ 0.06 / B:1px solid #1f1f1f @ 0.06 / L:1px solid #1f1f1f @ 0.06 r 12px; a::after.hGEQua_imageLink 27pxx10px bg #ffffff border T:1px solid #1f1f1f @ 0.06 / R:1px solid #1f1f1f @ 0.06 / B:1px solid #1f1f1f @ 0.06 / L:1px solid #1f1f1f @ 0.06 r 6px shadow #000000 @ 0.06 0px 1px 3px 0px, #ffffff @ 0.5 0px 0px 1px 0px inset; div.img.Z2phqG_imgContainer 252.0x163.4 border B:1px solid #1f1f1f @ 0.06 |
| How | at rest |

Crops: none.

### Sign-in page (boundary)

#### signin-title

Sign-in title. "Sign in to Mesh" — the 32px headline on the app.me.sh sign-in card, a LIGHT sibling surface (#fcfcfc), a different stack from the dark marketing site.

Page: signin. Selector: `span._headline_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 272 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ChronicleDisplayCondensed 32px/21px 400 |
| Letter spacing | -0.5px |
| Colour | #48494a |
| Transition | none |
| Ancestor paint | 3 up div._box_z86qt_27 bg #959595 @ 0.06 shadow #000000 @ 0.08 0px 2px 4px -2px, #000000 @ 0.03 0px 8px 16px -8px, #ffffff @ 0.5 0px -10px 24px 0px inset, #ffffff @ 0.24 0px -16px 48px 0px inset |
| How | at rest |

Crops: `signin-title-default.png`.

#### signin-input

E-mail field. The "Enter your email" field; filled with the documented test address then deleted, Sign in with email never pressed.

Page: signin. Selector: `input[type=text]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 272 x 40 | = | = |
| Padding | 0px 12px | = | = |
| Border | 1px solid #48494a @ 0.1 | 1px solid #2686be | 1px solid #2686be |
| Radius | 6px | = | = |
| Background | #48494a @ 0.04 | = | = |
| Box shadow | none | = | = |
| Backdrop filter | blur(40px) | = | = |
| Outline | none | = | = |
| Font | SFProText 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #48494a | = | = |
| Transition | border-color, background-color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #48494a, opacity 0.6 | = | = |
| Painted layers | input._textInput_5plfs_1 272.0x40.0 bg #48494a @ 0.04 border T:1px solid #48494a @ 0.1 / R:1px solid #48494a @ 0.1 / B:1px solid #48494a @ 0.1 / L:1px solid #48494a @ 0.1 r 6px | input._textInput_5plfs_1 272.0x40.0 bg #48494a @ 0.04 border T:1px solid #2686be / R:1px solid #2686be / B:1px solid #2686be / L:1px solid #2686be r 6px | input._textInput_5plfs_1 272.0x40.0 bg #48494a @ 0.04 border T:1px solid #2686be / R:1px solid #2686be / B:1px solid #2686be / L:1px solid #2686be r 6px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signin-input-default.png`, `signin-input-focused.png`, `signin-input-filled.png`.

#### signin-email-btn

E-mail sign-in. The orange "Sign in with email" button — the brand accent on this light surface; never pressed.

Page: signin. Selector: `._emailLoginBtn_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 272 x 40 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 12px | = | - | = |
| Background | #ff6821 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | SF Pro Text 14px/21px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff @ 0.6 | = | - | = |
| Transition | background-color, color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | - | = |
| Painted layers | button._loginBtn_1ii7i_42._emailLoginBtn_axxef_40 272.0x40.0 bg #ff6821 r 12px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `signin-email-btn-default.png`, `signin-email-btn-hover.png`, `signin-email-btn-pressed.png`.

#### signin-apple

Apple sign-in. The "Sign in with Apple" OAuth button; never followed.

Page: signin. Selector: `._appleBtn_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 272 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #1f1f1e | #1f1f1e @ 0.85 | = | #1f1f1e @ 0.85 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SF Pro Text 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 21, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | button._loginBtn_1ii7i_42._button_ykqwo_1 272.0x44.0 bg #1f1f1e r 12px | button._loginBtn_1ii7i_42._button_ykqwo_1 272.0x44.0 bg #1f1f1e @ 0.85 r 12px | = | button._loginBtn_1ii7i_42._button_ykqwo_1 272.0x44.0 bg #1f1f1e @ 0.85 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-apple-default.png`, `signin-apple-hover.png`, `signin-apple-focus-visible.png`, `signin-apple-pressed.png`.

#### signin-google

Google sign-in. The "Sign in with Google" OAuth button (Google blue); never followed.

Page: signin. Selector: `._googleBtn_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 272 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #5383ec | #5383ec @ 0.87 | = | #5383ec @ 0.87 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SF Pro Text 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | button._loginBtn_1ii7i_42._button_ykqwo_1 272.0x44.0 bg #5383ec r 12px | button._loginBtn_1ii7i_42._button_ykqwo_1 272.0x44.0 bg #5383ec @ 0.87 r 12px | = | button._loginBtn_1ii7i_42._button_ykqwo_1 272.0x44.0 bg #5383ec @ 0.87 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-google-default.png`, `signin-google-hover.png`, `signin-google-focus-visible.png`, `signin-google-pressed.png`.

#### signin-toggle

Create-account toggle. The "Create account" switcher on the sign-in card; a local toggle measured never pressed.

Page: signin. Selector: `._toggleBtn_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91 x 12 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | SFProText 12px/12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #48494a | = | = | = |
| Transition | filter 0.15s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-toggle-default.png`, `signin-toggle-hover.png`, `signin-toggle-focus-visible.png`, `signin-toggle-pressed.png`.

### Footer

#### footer

Footer. The #0f0f10 footer band: link columns, app links, the legal subfooter.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 335 |
| Padding | 150px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #0f0f10 |
| Box shadow | none |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.7 |
| Text node | h3.pNqdxq_footerNavSectionTitle: Verlag 12px/12px 600, #ffffff, ls 1px |
| Transition | none |
| Icon | 16 x 16, colour #f2b98b, fill #000000 |
| Painted layers | footer.pNqdxq_wrapper.pNqdxq_homePage 1440.0x335.0 bg #0f0f10; h3::after.pNqdxq_footerNavSectionTitle 472.875pxx2px image url(data:…)' /%3E%3C/svg%3E"); h3::after.pNqdxq_footerNavSectionTitle 754.438pxx2px image url(data:…)' /%3E%3C/svg%3E"); h3::after.pNqdxq_footerNavSectionTitle 626.25pxx2px image url(data:…)' /%3E%3C/svg%3E"); div.pNqdxq_container.container 1160.0x96.0 border T:1px solid #979797 @ 0.2; a.pNqdxq_socialLink.pNqdxq_linkedInLink 16.0x16.0 bg #ffffff @ 0.14 r 4px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a[href=/about]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88 x 12 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Verlag 12px/12px 700 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #ffffff @ 0.4 | #efab74 | = | #ed9d5d |
| Transition | color 0.15s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.pNqdxq_navigationLink 88.0x12.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link. A footer social icon link (X).

Page: home. Selector: `footer a[href*=x.com]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff @ 0.14 | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Verlag 18px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f2b98b | #efab74 | = | #ed9d5d |
| Transition | background-color 0.15s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #f2b98b, fill #000000 | 16 x 16, colour #efab74, fill #000000 | = | 16 x 16, colour #ed9d5d, fill #000000 |
| ::before | 16px x 16px, absolute, bg #000000 @ 0 linear-gradient(200deg, #ffffff @ 0.2, #b6b9b9 @ 0.2), radius 4px | = | = | = |
| Painted layers | a.pNqdxq_socialLink.pNqdxq_xLink 16.0x16.0 bg #ffffff @ 0.14 r 4px; a::before.pNqdxq_socialLink.pNqdxq_xLink 16pxx16px image linear-gradient(200deg, #ffffff @ 0.2, #b6b9b9 @ 0.2) r 4px | a::before.pNqdxq_socialLink.pNqdxq_xLink 16pxx16px image linear-gradient(200deg, #ffffff @ 0.2, #b6b9b9 @ 0.2) r 4px | a.pNqdxq_socialLink.pNqdxq_xLink 16.0x16.0 bg #ffffff @ 0.14 r 4px outline 1px auto #101010 offset 1px; a::before.pNqdxq_socialLink.pNqdxq_xLink 16pxx16px image linear-gradient(200deg, #ffffff @ 0.2, #b6b9b9 @ 0.2) r 4px | a::before.pNqdxq_socialLink.pNqdxq_xLink 16pxx16px image linear-gradient(200deg, #ffffff @ 0.2, #b6b9b9 @ 0.2) r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

### Mobile (390 wide)

#### m-menu-button

Menu button. The 44x32 hamburger at the bar edge (an icon div, no label); its own press slides the nav drawer in.

Page: home. Selector: `.y0DxmG_toggle`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 44 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #ffffff @ 0.06 |
| Background image | linear-gradient(179deg, #ffffff @ 0.1 7%, #ffffff @ 0 92%) |
| Box shadow | #000000 @ 0.08 0px 2px 4px -2px, #000000 @ 0.03 0px 8px 16px -8px, #ffffff @ 0.1 0px -2px 3px 0px inset, #ffffff @ 0.06 0px -4px 12px 0px inset |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.7 |
| Transition | none |
| Icon | 44 x 26, colour #ffffff @ 0.7, fill #000000 |
| ::before | 44px x 32px, absolute, bg #000000 @ 0, radius 8px |
| Painted layers | div.y0DxmG_toggle 44.0x32.0 bg #ffffff @ 0.06 image linear-gradient(179deg, #ffffff @ 0.1 7%, #ffffff @ 0 92%) r 8px shadow #000000 @ 0.08 0px 2px 4px -2px, #000000 @ 0.03 0px 8px 16px -8px, #ffffff @ 0.1 0px -2px 3px 0px inset, #ffffff @ 0.06 0px -4px 12px 0px inset |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The nav drawer after the hamburger press (fixed, 374x762; it is transparent and translated -187px off-canvas while closed).

Page: home. Selector: `.y0DxmG_mobileNav after toggle press`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 374 x 762 |
| Padding | 0px |
| Border | none |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Verlag 18px/27px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.7 |
| Text node | button.y0DxmG_navigationLink: Verlag 12px/12px 700, #ffffff, ls 1px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -187, 0) |
| Icon | 40 x 40, colour #ffffff, fill #000000 |
| Painted layers | ul.y0DxmG_mobileTopLevelNavList 374.0x549.9 bg #1f1f1e @ 0.06 image linear-gradient(#1f1f1e @ 0.8 2%, #1f1f1e @ 0 100%) r 12px; li.y0DxmG_mobileTopLevelNavBtn.y0DxmG_sectionOpen 342.0x282.9 border B:1px solid #ffffff @ 0.06; a.hGEQua_imageLink 171.0x174.9 bg #ffffff @ 0.12 border T:1px solid #ffffff @ 0.06 / R:1px solid #ffffff @ 0.06 / B:1px solid #ffffff @ 0.06 / L:1px solid #ffffff @ 0.06 r 12px; a::after.hGEQua_imageLink 27pxx10px bg #ffffff border T:1px solid #1f1f1f @ 0.06 / R:1px solid #1f1f1f @ 0.06 / B:1px solid #1f1f1f @ 0.06 / L:1px solid #1f1f1f @ 0.06 r 6px shadow #000000 @ 0.06 0px 1px 3px 0px, #ffffff @ 0.5 0px 0px 1px 0px inset; div.img.Z2phqG_imgContainer 169.0x109.9 border B:1px solid #ffffff @ 0.06; li.y0DxmG_mobileTopLevelNavBtn 342.0x57.0 border B:1px solid #ffffff @ 0.06 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-link

Menu link. A link row inside the open mobile drawer.

Page: home. Selector: `first link inside .y0DxmG_mobileNav`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Verlag 14px/14px 700 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #ffffff | #fb7232 | = | #fb7232 |
| Transition | color 0.1s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 13px x 12px, static, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile headline. The hero headline at 390 — the final word rotates (organized / searchable / up to date).

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | VerlagCondensed 48px/48px 700 |
| Letter spacing | 0.88px |
| Colour | #fefef7 |
| Text node | undefined: VerlagCondensed 48px/48px 700, #fefef7, ls 0.88px |
| Transition | none |
| Ancestor paint | 1 up section.IQmOHa_hero.btQYOq_dark bg #0f0f10 |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-cta

Mobile CTA. The fixed "Get Started" pill in the mobile bar; links to /start, never followed.

Page: home. Selector: `.y0DxmG_btns`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123 x 32.03 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 14px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Verlag 18px/27px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff @ 0.7 | = | - | = |
| Text node | div.eoWgla_ctaInner: Verlag 12px/12px 600, #1f1f1e, ls 1px | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.eoWgla_cta.y0DxmG_cta 123.0x32.0 bg #ffffff r 8px; div::after.eoWgla_cta.y0DxmG_cta calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%) r 100%; div::before.eoWgla_ctaInner calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%); div::after.eoWgla_ctaInner 100%x100% image linear-gradient(135deg, #ffffff, #b6b6b6 150%) | = | - | a.y0DxmG_signInBtn 0.0x0.0 bg #ffffff @ 0.08 r 8px; div.eoWgla_cta.y0DxmG_cta 123.0x32.0 bg #ffffff r 8px; div::after.eoWgla_cta.y0DxmG_cta calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%) r 100%; div::before.eoWgla_ctaInner calc(100% + 36px)xcalc(100% + 12px) image linear-gradient(225deg, #32c5ff 0%, #b620e0 51%, #f7b500 100%); div::after.eoWgla_ctaInner 100%x100% image linear-gradient(135deg, #ffffff, #b6b6b6 150%) |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-pressed.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `color 0.15s ease-in-out`, `none`, `y 0.4s ease-in-out, opacity 0.3s ease-in-out 0.1s`, `y 0.4s ease-in-out, opacity 0.3s ease-in-out`, `opacity 0.4s cubic-bezier(0.33, 1, 0.68, 1), transform 0.4s cubic-bezier(0.33, 1, 0.68, 1)`, `opacity 0.4s cubic-bezier(0.32, 0, 0.67, 0), transform 0.4s cubic-bezier(0.32, 0, 0.67, 0)`, `filter 0.2s`, `opacity 0.3s ease-in-out`, `transform 0.2s`, `opacity 0.2s`, `background-color 0.15s ease-in-out`, `transform 0.15s ease-in-out`
