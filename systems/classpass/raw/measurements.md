# Component measurements

Computed styles read from classpass.com on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme (the TrustArc consent overlay was hidden, never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The 64px top bar: wordmark, Search/Plans links, the "How it works" dropdown, Gifts/List-my-business/Corporate-wellness links, Log in and the promo CTA.

Page: home. Selector: `div[data-testid=app-header]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.08 0px 2px 10px 0px |
| Outline | none |
| Font | norms 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: norms 36px/40px 500, #000000 |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | header.AppHeader_base__tOTMe 1440.0x64.0 bg #ffffff shadow #000000 @ 0.08 0px 2px 10px 0px; nav.AppHeader_navigation___N_V_ 1440.0x64.0 bg #ffffff; span.Button_button__8B4nB.Button_buttonColor-primary__SYZoa 149.0x40.0 bg #0055ff border T:1px solid #0055ff / R:1px solid #0055ff / B:1px solid #0055ff / L:1px solid #0055ff r 9999px; ul.Menu_menu__Ci1Yt.Menu_mobilePanel__3oCNR 0.0x0.0 bg #ffffff; li.Menu_menuItem__tIh_1 0.0x0.0 border B:1px solid #e7e7e7; li.Menu_menuItem__tIh_1 0.0x0.0 border B:1px solid #e7e7e7 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The ClassPass wordmark anchor.

Page: home. Selector: `a[aria-label=home]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 124 x 64 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | norms 36px/40px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. A plain header link (Plans).

Page: home. Selector: `header a[href=/plans]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66 x 64 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #f7f7f7 | #f7f7f7 | #f7f7f7 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | norms 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a 66.0x64.0 bg #f7f7f7 | a 66.0x64.0 bg #f7f7f7 | a 66.0x64.0 bg #f7f7f7 |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-dropdown

Nav dropdown. The "How it works" menu trigger (aria-haspopup=menu); its own press opens the link menu (opened state).

Page: home. Selector: `button.NavDesktopDropdown_Button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 138 x 64 | = | = | = | = |
| Padding | 0px 16px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | #f7f7f7 | #f7f7f7 | #f7f7f7 | #f7f7f7 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | norms 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | button.NavDesktopDropdown_Button__R5NHb 138.0x64.0 bg #f7f7f7 | button.NavDesktopDropdown_Button__R5NHb 138.0x64.0 bg #f7f7f7 | button.NavDesktopDropdown_Button__R5NHb 138.0x64.0 bg #f7f7f7 | button.NavDesktopDropdown_Button__R5NHb 138.0x64.0 bg #f7f7f7 |

Crops: `nav-dropdown-default.png`, `nav-dropdown-hover.png`, `nav-dropdown-focus-visible.png`, `nav-dropdown-pressed.png`, `nav-dropdown-opened.png`.

#### menu-panel

Nav menu. The "How it works" dropdown panel (Walkthrough / How ClassPass works / Features links), held open by the trigger toggle.

Page: home. Selector: `[role=menu] under the open trigger`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 200 x 121 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.08 0px 2px 10px 0px |
| Outline | none |
| Font | norms 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.NavDesktopDropdown_Item__Ps8sT: norms 14px/20px 500, #000000 |
| Transition | none |
| Painted layers | div.NavDesktopDropdown_Items__MGAQs 200.0x121.0 bg #ffffff shadow #000000 @ 0.08 0px 2px 10px 0px; a.NavDesktopDropdown_Item__Ps8sT 200.0x61.0 border T:1px solid #e7e7e7 |
| How | at rest |

Crops: `menu-panel-default.png`.

#### menu-card

Menu item. A link row inside the open nav menu.

Page: home. Selector: `first link inside [role=menu]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 200 x 60 |
| Padding | 20px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 14px/20px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s |
| Cursor | pointer |
| Ancestor paint | 1 up div.NavDesktopDropdown_Items__MGAQs bg #ffffff shadow #000000 @ 0.08 0px 2px 10px 0px |
| How | at rest |

Crops: `menu-card-default.png`.

#### nav-login

Log-in link. The header "Log in" link; measured never followed.

Page: home. Selector: `header a[href=/login]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71 x 64 | = | - | = |
| Padding | 0px 16px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | #f7f7f7 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | norms 14px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Painted layers | - | = | = | a 71.0x64.0 bg #f7f7f7 |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-pressed.png`.

#### nav-cta

Nav CTA. The "💥 Get 14 days free 💥" promo button; links to /walkthrough, measured never followed.

Page: home. Selector: `[data-testid=NavCta]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149 x 53 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | norms 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.Button_button__8B4nB.Button_buttonColor-primary__SYZoa: norms 16px/16px 500, #ffffff | = | - | = |
| Transition | none | = | - | = |
| Painted layers | span.Button_button__8B4nB.Button_buttonColor-primary__SYZoa 149.0x40.0 bg #0055ff border T:1px solid #0055ff / R:1px solid #0055ff / B:1px solid #0055ff / L:1px solid #0055ff r 9999px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title. "One app for <rotating word>" — the circuit display headline (the activity word cycles).

Page: home. Selector: `h1.HomepageHeroC_heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 408 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | circuit 36px/40px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.HomepageHeroC_staticLine__F1UTo: circuit 40px/53px 500, #000000 |
| Transition | none |
| Ancestor paint | 1 up div.HomepageHeroC_hero__moA8J bg #ffffff |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subcopy. The norms lede under the display headline.

Page: home. Selector: `.HomepageHeroC_subtitle`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 514 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 20px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-card

Hero activity card. One of the rotating activity photo cards beside the headline (the deck cycles).

Page: home. Selector: `.HeroAnimationBlock_card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 185 x 225 |
| Padding | 0px |
| Border | none |
| Radius | 25px |
| Background | #000000 @ 0.08 |
| Box shadow | none |
| Outline | none |
| Font | norms 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.HeroAnimationBlock_card__ry20G 185.0x225.0 bg #000000 @ 0.08 r 25px |
| How | at rest |

Crops: `hero-card-default.png`.

#### page-ground

Page ground. The html element's own painted fill — the white ground under every section (body itself is transparent).

Page: home. Selector: `document.documentElement`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | norms 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: norms 36px/40px 500, #000000 |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | html 1440.0x900.0 bg #ffffff; header.AppHeader_base__tOTMe 1440.0x64.0 bg #ffffff shadow #000000 @ 0.08 0px 2px 10px 0px; nav.AppHeader_navigation___N_V_ 1440.0x64.0 bg #ffffff; span.Button_button__8B4nB.Button_buttonColor-primary__SYZoa 149.0x40.0 bg #0055ff border T:1px solid #0055ff / R:1px solid #0055ff / B:1px solid #0055ff / L:1px solid #0055ff r 9999px; ul.Menu_menu__Ci1Yt.Menu_mobilePanel__3oCNR 0.0x0.0 bg #ffffff; li.Menu_menuItem__tIh_1 0.0x0.0 border B:1px solid #e7e7e7 |
| How | at rest |

Crops: none.

### Plans and pricing

#### section-title

Section title. The first section heading on the plans page (norms 24px).

Page: plans. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 654 x 57.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 24px/28.8px 400 |
| Letter spacing | -0.3px |
| Colour | #000000 |
| Text node | span: norms 24px/28.8px 400, #000000, ls -0.3px |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### plans-h1

Plans title. "Pick a plan that works for you" in 60px circuit.

Page: plans. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 728 x 124.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | circuit 60px/62.4px 400 |
| Letter spacing | 1px |
| Colour | #000000 |
| Text node | span: circuit 60px/62.4px 400, #000000, ls 1px |
| Transition | none |
| How | at rest |

Crops: `plans-h1-default.png`.

#### plan-slide

Plan slide (default). The recommended "45 credits" plan slide (the DEFAULT pill); prices render in the detected locale (SGD here).

Page: plans. Selector: `.AvailablePlansCarousel_slide:has-text(DEFAULT)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 266.66 x 148 | = |
| Padding | 24px | = |
| Border | none | = |
| Radius | 18px | = |
| Background | #ffffff | = |
| Box shadow | #0155fe @ 0.1 0px 5px 16px 0px | = |
| Outline | none | = |
| Font | norms 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h6.AvailablePlansCarousel_credits__z7Ebr: norms 16px/24px 700, #000000, ls -0.2px | = |
| Transition | none | = |
| Painted layers | div.AvailablePlansCarousel_slide__mKeZE 266.7x148.0 bg #ffffff r 18px shadow #0155fe @ 0.1 0px 5px 16px 0px; div::after.Pill_pill__K98vi.Pill_size-md__BDV_3 79pxx28px bg #c0e0ff r 14px | = |
| How | at rest | mouse hover |

Crops: `plan-slide-default.png`, `plan-slide-hover.png`.

#### plan-price

Plan price. The "SGD 99 /mo" price row inside a slide.

Page: plans. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 117.41 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 36px/40px 700 |
| Letter spacing | -0.6px |
| Colour | #000000 |
| Transition | none |
| Ancestor paint | 3 up div.AvailablePlansCarousel_slide__mKeZE bg #ffffff shadow #0155fe @ 0.1 0px 5px 16px 0px |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-pill

Plan pill. The DEFAULT tag on the recommended slide.

Page: plans. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 79 x 20 |
| Padding | 2px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 12px/16px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| ::after | 79px x 28px, absolute, bg #c0e0ff, radius 14px |
| Painted layers | div::after.Pill_pill__K98vi.Pill_size-md__BDV_3 79pxx28px bg #c0e0ff r 14px |
| Ancestor paint | 2 up div.AvailablePlansCarousel_slide__mKeZE bg #ffffff shadow #0155fe @ 0.1 0px 5px 16px 0px |
| How | at rest |

Crops: `plan-pill-default.png`.

#### loc-selector

Location selector. The detected-market pill pricing is quoted in; a locale control, never toggled.

Page: plans. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 992 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | undefined: norms 16px/24px 400, #0055ff |
| Transition | none |
| How | at rest |

Crops: `loc-selector-default.png`.

#### faq-question

FAQ question. An FAQ accordion trigger; its own press opens the answer (opened state).

Page: plans. Selector: ``. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 952 x 34 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | norms 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Text node | h3: norms 18px/18px 400, #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 18 x 18, colour #000000 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | div 952.0x34.0 outline 1px auto #101010 offset 0px | = | = |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-focus-visible.png`, `faq-question-pressed.png`, `faq-question-opened.png`.

#### cms-cta

Page CTA. A CMS call-to-action in the plans body; never followed.

Page: plans. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 327 x 50 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | norms 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: norms 16px/24px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Painted layers | span.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_ 327.0x50.0 bg #111111 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 9999px | span.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_ 327.0x50.0 bg #040404 border T:1px solid #040404 / R:1px solid #040404 / B:1px solid #040404 / L:1px solid #040404 r 9999px | a 327.0x16.0 outline 1px auto #101010 offset 1px; span.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_ 327.0x50.0 bg #111111 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 9999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cms-cta-default.png`, `cms-cta-hover.png`, `cms-cta-focus-visible.png`, `cms-cta-pressed.png`.

### Footer

#### footer

Footer. The footer band: link columns, the app-store badges, social icons, the legal subfooter.

Page: home. Selector: `footer.Footer_footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 581 |
| Padding | 64px 100px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | norms 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h5.Footer_header__uVM6a: norms 18px/24px 500, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | footer.Footer_footer__OYoYH 1440.0x581.0 bg #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a[href=/about]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | norms 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 64.0x16.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link. A footer social icon link (Facebook).

Page: home. Selector: `footer a[href*=facebook]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 12 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | norms 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 28 x 28, colour #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 28.0x12.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### app-badge

App-store badge. An app-store badge link in the footer; never followed.

Page: home. Selector: `footer .AppDownloadIcons a > *`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 117 x 12 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | norms 12px/12px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 117 x 38, colour #ffffff, fill #000000 | = |
| How | at rest | mouse hover |

Crops: `app-badge-default.png`, `app-badge-hover.png`.

### Public search

#### search-box

Search box. The activity + location combobox pair on the public results page.

Page: search. Selector: `[data-testid=SearchBox]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 549 x 64 |
| Padding | 12px 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | norms 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | section.JVGKHB897QCEb9iSC_AW 549.0x64.0 bg #ffffff; div.wRburMR2MwVNDUQf_lbg 517.0x40.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 20px shadow #000000 @ 0.05 0px 1px 2px 0px; div::before.C6HbY8wxzxZCoECg_vTw 1pxx24px bg #d6d6d6 |
| How | at rest |

Crops: `search-box-default.png`.

#### search-field

Activity field. The "Yoga, pilates, massage…" combobox field; filled with sample text then deleted, never searched.

Page: search. Selector: `SearchBoxField input[placeholder~=pilates]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 217.5 x 20 | = | = |
| Padding | 0px 0px 0px 8px | = | = |
| Border | none | = | = |
| Radius | 3px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | norms 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

#### search-loc

Location field. The "City, neighborhood" combobox, prefilled with the detected area — focused only so the prefilled value survives.

Page: search. Selector: `input[placeholder~=neighborhood]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 217.5 x 20 | = |
| Padding | 0px 0px 0px 8px | = |
| Border | none | = |
| Radius | 3px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | norms 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 1 | = |
| How | at rest | clicked into the field |

Crops: `search-loc-default.png`, `search-loc-focused.png`.

#### filter-pill

Vertical pill. The "Fitness" vertical pill in the filter bar; its press opens the verticals switcher.

Page: search. Selector: `[data-testid=VerticalsFilter] button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128 x 38 | = | = | = |
| Padding | 0px 16px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | norms 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: norms 14px/20px 500, #0055ff | = | = | = |
| Transition | none | = | = | = |
| Icon | 24 x 24, colour #0055ff | = | = | = |
| Painted layers | button.NdbE21qLuZOtwHTH6gip.TqHQqCBFnxwMo5dWH9VJ 112.0x32.0 bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 16px | button.NdbE21qLuZOtwHTH6gip.TqHQqCBFnxwMo5dWH9VJ 112.0x32.0 bg #f7f7f7 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 16px | button.NdbE21qLuZOtwHTH6gip.TqHQqCBFnxwMo5dWH9VJ 112.0x32.0 bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 16px outline 2px solid #0055ff offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-pill-default.png`, `filter-pill-hover.png`, `filter-pill-focus-visible.png`, `filter-pill-pressed.png`.

#### filter-multi

Filter dropdown. The "Activities" multi-select trigger; its own press opens the option panel (opened state).

Page: search. Selector: `[data-testid=MultiSelectFilter] button:has-text("Activities")`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 142 x 38 | = | = | = | = |
| Padding | 0px 16px 0px 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | norms 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Text node | span: norms 14px/20px 500, #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = | = |
| Painted layers | button.NdbE21qLuZOtwHTH6gip 126.0x32.0 bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 16px | button.NdbE21qLuZOtwHTH6gip 126.0x32.0 bg #f7f7f7 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 16px | button.NdbE21qLuZOtwHTH6gip 126.0x32.0 bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 16px outline 2px solid #0055ff offset 0px | = | button.NdbE21qLuZOtwHTH6gip 126.0x32.0 bg #f7f7f7 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 16px outline 2px solid #0055ff offset 0px; div.efln90Mt5oP0x_l3_09w 380.0x349.0 bg #ffffff r 8px shadow #000000 @ 0.24 0px 4px 12px 0px; span.xt0rRErSJCGHBs8HoZFQ 18.0x18.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 3px; span.xt0rRErSJCGHBs8HoZFQ 18.0x18.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 3px; span.xt0rRErSJCGHBs8HoZFQ 18.0x18.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 3px; span.xt0rRErSJCGHBs8HoZFQ 18.0x18.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `filter-multi-default.png`, `filter-multi-hover.png`, `filter-multi-focus-visible.png`, `filter-multi-pressed.png`, `filter-multi-opened.png`.

#### filter-panel

Filter panel. The opened Activities option panel.

Page: search. Selector: `opened dropdown under Activities`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 349 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: norms 14px/20px 400, #000000 |
| Transition | none |
| Painted layers | div.efln90Mt5oP0x_l3_09w 380.0x349.0 bg #ffffff r 8px shadow #000000 @ 0.24 0px 4px 12px 0px; span.xt0rRErSJCGHBs8HoZFQ 18.0x18.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 3px; span.xt0rRErSJCGHBs8HoZFQ 18.0x18.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 3px; span.xt0rRErSJCGHBs8HoZFQ 18.0x18.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 3px; span.xt0rRErSJCGHBs8HoZFQ 18.0x18.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 3px; span.xt0rRErSJCGHBs8HoZFQ 18.0x18.0 border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 3px |
| How | at rest |

Crops: `filter-panel-default.png`.

#### venue-card

Venue card. A studio result card (photo, name, rating, distance); links to the public venue page, hovered never followed.

Page: search. Selector: ``. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 790 x 112 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | norms 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | div.hqhUxYCIcaKkl9Ush0cZ.text--ellipsis: norms 12px/16px 700, #999999 | = |
| Transition | none | = |
| Icon | 24 x 24, colour #999999 | = |
| Painted layers | div.XrDNDtaXHW1_uWXNwVwl 168.0x112.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 5px; div.Y_21MOMThkep3uDkWzoB 0.0x0.0 bg #ffffff r 5px shadow #000000 @ 0.32 0px 8px 24px 0px; div::after.Y_21MOMThkep3uDkWzoB autoxauto border R:8px solid #000000 @ 0 / B:8px solid #ffffff / L:8px solid #000000 @ 0; div.tekap2kBylKtaCtYqVIg.x_pSRKfGsnjIlMIdn0rz 350.0x112.0 border L:1px solid #e7e7e7; div.sFZ7vPkstVNxYbvxqyxk 0.0x0.0 border B:1px solid #e7e7e7 | = |
| How | at rest | mouse hover |

Crops: `venue-card-default.png`, `venue-card-hover.png`.

#### venue-rating

Star rating. The "4.8 (27500+)" star-rating row inside a venue card.

Page: search. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 103.08 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0055ff |
| Text node | span: norms 14px/20px 500, #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 12.08 x 11.06, colour #0055ff, fill #555555 |
| How | at rest |

Crops: `venue-rating-default.png`.

#### universal-cta

Universal CTA. The "Get 14 days free" pill rendered with the bt--primary classes; links to /walkthrough, never followed.

Page: search. Selector: `[data-testid=UniversalCta] / a.bt--primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149 x 40 | = | = | = |
| Padding | 12px 16px 10px 16px | = | = | = |
| Border | 1px solid #0055ff | 1px solid #004de6 | = | 1px solid #0044cc |
| Radius | 999px | = | = | = |
| Background | #0055ff | #004de6 | = | #0044cc |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0055ff offset 1px | = |
| Font | norms 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.bt.bt--primary 149.0x40.0 bg #0055ff border T:1px solid #0055ff / R:1px solid #0055ff / B:1px solid #0055ff / L:1px solid #0055ff r 999px | a.bt.bt--primary 149.0x40.0 bg #004de6 border T:1px solid #004de6 / R:1px solid #004de6 / B:1px solid #004de6 / L:1px solid #004de6 r 999px | a.bt.bt--primary 149.0x40.0 bg #0055ff border T:1px solid #0055ff / R:1px solid #0055ff / B:1px solid #0055ff / L:1px solid #0055ff r 999px outline 2px solid #0055ff offset 1px | a.bt.bt--primary 149.0x40.0 bg #0044cc border T:1px solid #0044cc / R:1px solid #0044cc / B:1px solid #0044cc / L:1px solid #0044cc r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `universal-cta-default.png`, `universal-cta-hover.png`, `universal-cta-focus-visible.png`, `universal-cta-pressed.png`.

### Sign-in page (boundary)

#### signin-title

Sign-in title. "Welcome back" on the public sign-in card.

Page: signin. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 28px/32px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Ancestor paint | 1 up div.Login_loginForm__wb_4M bg #ffffff shadow #000000 @ 0.24 0px 4px 12px 0px |
| How | at rest |

Crops: `signin-title-default.png`.

#### signin-email

E-mail field. The e-mail input; filled with the documented test address then deleted, Log in never pressed.

Page: signin. Selector: `input[name=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 400 x 42 | = | = |
| Padding | 8px 16px | = | = |
| Border | 1px solid #e7e7e7 | 1px solid #1a5ee5 | 1px solid #1a5ee5 |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | norms 18px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.Login_input__jJDhI 400.0x42.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 4px | input.Login_input__jJDhI 400.0x42.0 bg #ffffff border T:1px solid #1a5ee5 / R:1px solid #1a5ee5 / B:1px solid #1a5ee5 / L:1px solid #1a5ee5 r 4px | input.Login_input__jJDhI 400.0x42.0 bg #ffffff border T:1px solid #1a5ee5 / R:1px solid #1a5ee5 / B:1px solid #1a5ee5 / L:1px solid #1a5ee5 r 4px |
| Ancestor paint | 3 up div.Login_loginForm__wb_4M bg #ffffff shadow #000000 @ 0.24 0px 4px 12px 0px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signin-email-default.png`, `signin-email-focused.png`, `signin-email-filled.png`.

#### signin-pass

Password field. The password input; focused only, never filled.

Page: signin. Selector: `input[name=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 400 x 42 | = |
| Padding | 8px 16px | = |
| Border | 1px solid #e7e7e7 | 1px solid #1a5ee5 |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | norms 18px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input.Login_input__jJDhI 400.0x42.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 4px | input.Login_input__jJDhI 400.0x42.0 bg #ffffff border T:1px solid #1a5ee5 / R:1px solid #1a5ee5 / B:1px solid #1a5ee5 / L:1px solid #1a5ee5 r 4px |
| Ancestor paint | 3 up div.Login_loginForm__wb_4M bg #ffffff shadow #000000 @ 0.24 0px 4px 12px 0px | = |
| How | at rest | clicked into the field |

Crops: `signin-pass-default.png`, `signin-pass-focused.png`.

#### signin-submit

Log-in button. The primary "Log in" submit; measured in all non-submitting states, never pressed for real.

Page: signin. Selector: `[data-testid=LoginSubmitButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 48 | = | = | = |
| Padding | 16px 0px 14px 0px | = | = | = |
| Border | 1px solid #0055ff | 1px solid #004de6 | = | 1px solid #0044cc |
| Radius | 9999px | = | = | = |
| Background | #0055ff | #004de6 | = | #0044cc |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0055ff offset 0px | = |
| Font | norms 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_button__8B4nB.Button_buttonColor-primary__SYZoa 400.0x48.0 bg #0055ff border T:1px solid #0055ff / R:1px solid #0055ff / B:1px solid #0055ff / L:1px solid #0055ff r 9999px | button.Button_button__8B4nB.Button_buttonColor-primary__SYZoa 400.0x48.0 bg #004de6 border T:1px solid #004de6 / R:1px solid #004de6 / B:1px solid #004de6 / L:1px solid #004de6 r 9999px | button.Button_button__8B4nB.Button_buttonColor-primary__SYZoa 400.0x48.0 bg #0055ff border T:1px solid #0055ff / R:1px solid #0055ff / B:1px solid #0055ff / L:1px solid #0055ff r 9999px outline 2px solid #0055ff offset 0px | button.Button_button__8B4nB.Button_buttonColor-primary__SYZoa 400.0x48.0 bg #0044cc border T:1px solid #0044cc / R:1px solid #0044cc / B:1px solid #0044cc / L:1px solid #0044cc r 9999px |
| Ancestor paint | 3 up div.Login_loginForm__wb_4M bg #ffffff shadow #000000 @ 0.24 0px 4px 12px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-submit-default.png`, `signin-submit-hover.png`, `signin-submit-focus-visible.png`, `signin-submit-pressed.png`.

#### signin-apple

Apple sign-in. The "Sign in with Apple" OAuth button; never followed.

Page: signin. Selector: `[data-testid=SignInWithApple]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 48 | = | = | = |
| Padding | 16px 0px 14px 0px | = | = | = |
| Border | 1px solid #d6d6d6 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0055ff offset 0px | = |
| Font | norms 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.SignInWithApple_text__qBOAl: norms 16px/16px 500, #000000 | = | = | = |
| Transition | color, background-color, border-color 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| Painted layers | button.Button_button__8B4nB.Button_buttonRounded__o8JOm 400.0x48.0 bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 9999px | = | button.Button_button__8B4nB.Button_buttonRounded__o8JOm 400.0x48.0 bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 9999px outline 2px solid #0055ff offset 0px | = |
| Ancestor paint | 2 up div.Login_loginForm__wb_4M bg #ffffff shadow #000000 @ 0.24 0px 4px 12px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-apple-default.png`, `signin-apple-hover.png`, `signin-apple-focus-visible.png`, `signin-apple-pressed.png`.

#### signin-google

Google sign-in. The "Sign in with Google" OAuth button; never followed.

Page: signin. Selector: `[data-testid=SignInWithGoogle]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 48 | = | = | = |
| Padding | 16px 0px 14px 0px | = | = | = |
| Border | 1px solid #d6d6d6 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0055ff offset 0px | = |
| Font | norms 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.SignInWithGoogle_text__OoGEq: norms 16px/16px 500, #000000 | = | = | = |
| Transition | color, background-color, border-color 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | button.Button_button__8B4nB.Button_buttonRounded__o8JOm 400.0x48.0 bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 9999px | = | button.Button_button__8B4nB.Button_buttonRounded__o8JOm 400.0x48.0 bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / B:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 9999px outline 2px solid #0055ff offset 0px | = |
| Ancestor paint | 2 up div.Login_loginForm__wb_4M bg #ffffff shadow #000000 @ 0.24 0px 4px 12px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-google-default.png`, `signin-google-hover.png`, `signin-google-focus-visible.png`, `signin-google-pressed.png`.

#### signin-forgot

Forgot-password link. The "Forgot your password?" link; never followed.

Page: signin. Selector: `a.Login_forgotPassword`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | norms 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a5ee5 | = | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.Login_loginForm__wb_4M bg #ffffff shadow #000000 @ 0.24 0px 4px 12px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Login_forgotPassword__W9SlG 400.0x24.0 outline 1px auto #101010 offset 1px | = |

Crops: `signin-forgot-default.png`, `signin-forgot-hover.png`, `signin-forgot-focus-visible.png`, `signin-forgot-pressed.png`.

### Trial onboarding (boundary)

#### walk-title

Trial title. "What your trial includes" — the first onboarding card, the entry the promo CTAs link to.

Page: walk. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 547.98 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 20px/28px 500 |
| Letter spacing | -0.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `walk-title-default.png`.

#### walk-cta

Step CTA. The black "Next" step button; measured in all non-submitting states, never pressed — pressing advances account creation.

Page: walk. Selector: `button.Button_buttonColor-mkt-black`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 208 x 48 | = | = | = |
| Padding | 12px 16px 10px 16px | = | = | = |
| Border | 1px solid #111111 | 1px solid #040404 | = | 1px solid #000000 |
| Radius | 9999px | = | = | = |
| Background | #111111 | #040404 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0055ff offset 0px | = |
| Font | norms 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.TextTransition_text__TULNQ.TextTransition_current__LoZin: norms 16px/24px 500, #ffffff | = | = | = |
| Transition | color, background-color, border-color 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_ 208.0x48.0 bg #111111 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 9999px | button.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_ 208.0x48.0 bg #040404 border T:1px solid #040404 / R:1px solid #040404 / B:1px solid #040404 / L:1px solid #040404 r 9999px | button.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_ 208.0x48.0 bg #111111 border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 r 9999px outline 2px solid #0055ff offset 0px | button.Button_button__8B4nB.Button_buttonColor-mkt-black__RenB_ 208.0x48.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `walk-cta-default.png`, `walk-cta-hover.png`, `walk-cta-focus-visible.png`, `walk-cta-pressed.png`.

#### walk-slide

Benefit slide. A "What your trial includes" benefit slide (icon + heading + body).

Page: walk. Selector: `.WalkThrough_slide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 595.98 x 676 |
| Padding | 0px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.WalkThrough_heading__jlJpU: norms 20px/28px 500, #000000, ls -0.2px |
| Transition | none |
| How | at rest |

Crops: `walk-slide-default.png`.

#### walk-dots

Step dots. The onboarding progress dots (the first is active).

Page: walk. Selector: `.WalkThrough_dots`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | button.MultiCarousel_dot__gYPcR.MultiCarousel_dotActive___T3Mv 8.0x8.0 bg #000000 r 100%; button.MultiCarousel_dot__gYPcR 8.0x8.0 bg #d6d6d6 r 100%; button.MultiCarousel_dot__gYPcR 8.0x8.0 bg #d6d6d6 r 100% |
| How | at rest |

Crops: `walk-dots-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `div[data-testid=app-header] at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.08 0px 2px 10px 0px |
| Outline | none |
| Font | norms 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: norms 36px/40px 500, #000000 |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | header.AppHeader_base__tOTMe 390.0x64.0 bg #ffffff shadow #000000 @ 0.08 0px 2px 10px 0px; nav.AppHeader_navigation___N_V_ 390.0x64.0 bg #ffffff; span.Button_button__8B4nB.Button_buttonColor-primary__SYZoa 0.0x0.0 bg #0055ff border T:1px solid #0055ff / R:1px solid #0055ff / B:1px solid #0055ff / L:1px solid #0055ff r 9999px; ul.Menu_menu__Ci1Yt.Menu_mobilePanel__3oCNR 390.0x844.0 bg #ffffff; li.Menu_menuItem__tIh_1 358.0x61.6 border B:1px solid #e7e7e7; li.Menu_menuItem__tIh_1 358.0x61.6 border B:1px solid #e7e7e7 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-banner

Promo banner. The yellow "Get 14 days free" promo bar at this width; captured as UI, its Close never pressed.

Page: home. Selector: `div.Banner_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 48 |
| Padding | 8px 40px |
| Border | none |
| Radius | 0px |
| Background | #fce172 |
| Box shadow | none |
| Outline | none |
| Font | norms 16px/24px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | pointer |
| Icon | 24 x 24, colour #000000 |
| Painted layers | div.Banner_base__JGFU7.Banner_anim__o2Oze 390.0x48.0 bg #fce172 |
| How | at rest |

Crops: `m-banner-default.png`.

#### m-menu-button

Menu button. The hamburger at the bar's right edge; its own press opens the menu overlay.

Page: home. Selector: `button.Menu_toggler`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 56 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | norms 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | undefined: norms 14px/20px 400, #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The menu overlay after the toggler's own press.

Page: home. Selector: `fixed/absolute menu container after Menu_toggler press`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | norms 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: norms 20px/28.5714px 400, #000000 |
| Transition | none |
| Painted layers | ul.Menu_menu__Ci1Yt.Menu_mobilePanel__3oCNR 390.0x844.0 bg #ffffff; li.Menu_menuItem__tIh_1 358.0x61.6 border B:1px solid #e7e7e7; li.Menu_menuItem__tIh_1 358.0x61.6 border B:1px solid #e7e7e7; li.Menu_menuItem__tIh_1 358.0x61.6 border B:1px solid #e7e7e7; li.Menu_menuItem__tIh_1 358.0x61.6 border B:1px solid #e7e7e7; li.Menu_menuItem__tIh_1 358.0x61.6 border B:1px solid #e7e7e7 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-link

Menu link. A link row inside the open mobile menu.

Page: home. Selector: `first link in the open menu`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 60.56 | = | = | = |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #f7f7f7 | #f7f7f7 | #f7f7f7 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | norms 20px/28.5714px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color 0.3s, 0.3s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a 358.0x60.6 bg #f7f7f7 | a 358.0x60.6 bg #f7f7f7 | a 358.0x60.6 bg #f7f7f7 |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile headline.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 119 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | circuit 36px/40px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.HomepageHeroC_staticLine__F1UTo: circuit 30px/26px 500, #000000 |
| Transition | none |
| Ancestor paint | 1 up div.HomepageHeroC_hero__moA8J bg #ffffff |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `color 0.3s, background-color 0.3s, border-color 0.3s`, `background-color 0.3s, color 0.3s`, `background-color 0.5s ease-in-out`, `transform 0.3s`, `opacity 0.5s ease-in-out`, `transform 0.2s`, `left 0.25s, width 0.25s, opacity 0.15s`, `color 0.5s cubic-bezier(0.333, 0, 0.667, 1)`, `opacity 300ms ease-in, visibility ease-in 300ms`
