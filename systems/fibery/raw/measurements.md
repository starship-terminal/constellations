# Fibery component measurements

Computed styles read from fibery.com and fibery.io on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the light-only marketing pages (home, /pricing, /templates), the public workspace-creation wizard at fibery.io/sign-up and the public sign-in at fibery.io/login/ — with any consent layer and the Intercom widget hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The top bar: Fibery wordmark, Solutions/Platform/Support dropdowns, Pricing, Book a demo, Log in and the dark "Sign up for free" button.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 88 |
| Padding | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | span.HeaderMenuItem_menuLink__JgNSg: Suisse Intl 16px/34px 500, #251d1a |
| Transition | none |
| Icon | 127 x 36, colour #0000ee |
| Painted layers | nav::before.HeaderMainMenu_menuList__q0OJp 619pxx60px bg #fff5e8 r 10px; div.HeaderMainMenu_headerDivider__6tgCG 1.0x18.0 bg #000000 @ 0.25; div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C 113.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; span::after.HeaderMenuItem_menuLink__JgNSg 5pxx5px border R:2px solid #251d1a / B:2px solid #251d1a; div.HeaderMenuDropdown_root__uAFiX 0.0x0.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; div.MenuItemHeadline_root__BAYvv 0.0x0.0 border B:1px solid #251d1a @ 0.1 |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Fibery mark-and-wordmark in the header, linking home.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 127 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/0px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| Icon | 127 x 36, colour #0000ee |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-item

Nav link. The Pricing header link; measured, never followed.

Page: home. Selector: `.HeaderMenuItem_menuLink Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77 x 34 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16px/34px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #251d1a | = | = | = |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C bg #fdf7ef | = | = |
| Painted layers | - | = | a.HeaderMenuItem_menuLink__JgNSg 77.0x34.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-menu-btn

Dropdown trigger. The "Solutions" header item — opens the solutions dropdown panel on hover. The opened state was measured after hovering it.

Page: home. Selector: `.HeaderMenuItem_root Solutions`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 113 x 36 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #251d1a @ 0.1 | - | 1px solid #251d1a @ 0.1 | 1px solid #251d1a @ 0.1 |
| Radius | 6px | = | - | = | = |
| Background | transparent | #fdf7ef | - | #fdf7ef | #fdf7ef |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Suisse Intl 16px/34px 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #251d1a | = | - | = | = |
| Text node | span.HeaderMenuItem_menuLink__JgNSg: Suisse Intl 16px/34px 500, #251d1a | = | - | = | = |
| Transition | none | = | - | = | = |
| Icon | 0 x 0, colour #0000ee | 32 x 32, colour #0000ee | - | 32 x 32, colour #0000ee | 32 x 32, colour #0000ee |
| ::before | 8px x 34px, absolute, bg #000000 @ 0, radius 0px | = | - | = | = |
| ::after | 8px x 34px, absolute, bg #000000 @ 0, radius 0px | = | - | = | = |
| Painted layers | div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C 113.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; span::after.HeaderMenuItem_menuLink__JgNSg 5pxx5px border R:2px solid #251d1a / B:2px solid #251d1a; div.HeaderMenuDropdown_root__uAFiX 0.0x0.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; div.MenuItemHeadline_root__BAYvv 0.0x0.0 border B:1px solid #251d1a @ 0.1; div.MenuItemTile_iconWrap__6DuKw 0.0x0.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px; div.MenuItemTile_iconWrap__6DuKw 0.0x0.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px | div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C 113.0x36.0 bg #fdf7ef border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px; span::after.HeaderMenuItem_menuLink__JgNSg 5pxx5px border R:2px solid #251d1a / B:2px solid #251d1a; div.HeaderMenuDropdown_root__uAFiX 740.0x383.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; div.MenuItemHeadline_root__BAYvv 322.0x23.0 border B:1px solid #251d1a @ 0.1; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px | - | div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C 113.0x36.0 bg #fdf7ef border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px; span::after.HeaderMenuItem_menuLink__JgNSg 5pxx5px border R:2px solid #251d1a / B:2px solid #251d1a; div.HeaderMenuDropdown_root__uAFiX 740.0x383.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; div.MenuItemHeadline_root__BAYvv 322.0x23.0 border B:1px solid #251d1a @ 0.1; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px | div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C 113.0x36.0 bg #fdf7ef border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px; span::after.HeaderMenuItem_menuLink__JgNSg 5pxx5px border R:2px solid #251d1a / B:2px solid #251d1a; div.HeaderMenuDropdown_root__uAFiX 740.0x383.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; div.MenuItemHeadline_root__BAYvv 322.0x23.0 border B:1px solid #251d1a @ 0.1; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | held open by an earlier toggle |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `nav-menu-btn-default.png`, `nav-menu-btn-hover.png`, `nav-menu-btn-pressed.png`, `nav-menu-btn-opened.png`.

#### nav-panel

Dropdown panel. The solutions dropdown panel opened by hovering its trigger (menu tiles plus template links); its links were never followed.

Page: home. Selector: `.HeaderMenuDropdown_root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 740 x 383 |
| Padding | 28px 24px 24px 24px |
| Gap | 48px |
| Border | none |
| Radius | 12px |
| Background | #fff5e8 |
| Box shadow | #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px |
| Backdrop filter | blur(20px) |
| Outline | none |
| Font | Suisse Intl 16px/34px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | div.MenuItemHeadline_textWrap__f24OT: Suisse Intl 14px/14px 500, #5f5f5f |
| Transition | none |
| Icon | 32 x 32, colour #0000ee |
| Painted layers | div.HeaderMenuDropdown_root__uAFiX 740.0x383.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; div.MenuItemHeadline_root__BAYvv 322.0x23.0 border B:1px solid #251d1a @ 0.1; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-menu-item

Dropdown item. A tile inside the open dropdown panel; measured, never followed.

Page: home. Selector: `dropdown menu tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 326 x 64 | = |
| Padding | 4px 24px 4px 4px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 10px | = |
| Background | transparent | #faebd6 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16px/34px 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | div.MenuItemTile_title__L5TcV: Suisse Intl 16px/16px 500, #251d1a | = |
| Transition | background-color 0.3s linear | = |
| Cursor | pointer | = |
| Icon | 32 x 32, colour #0000ee | = |
| Painted layers | div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 8px | a.MenuItemTile_root__ZxZoq 326.0x64.0 bg #faebd6 r 10px; div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 bg #fffdfa border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| Ancestor paint | 3 up div.HeaderMenuDropdown_root__uAFiX bg #fff5e8 shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px | = |
| How | at rest | mouse hover |

Crops: `nav-menu-item-default.png`, `nav-menu-item-hover.png`.

#### nav-login

Log in link. The "Log in" header link to fibery.io/login; measured, never followed.

Page: home. Selector: `header Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #fdf7ef | = | = | = |
| Box shadow | none | #251d1a @ 0.1 0px 0px 0px 1px | = | #251d1a @ 0.0969406 0px 0px 0px 0.969406px |
| Backdrop filter | blur(1px) | blur(10px) | = | blur(9.72465px) |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16px/40px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #251d1a | = | = | = |
| Text node | span.FiberyButton_content__4PHkJ: Suisse Intl 16px/40px 600, #251d1a | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.FiberyButton_root__0jBYr.HeaderMainMenu_loginButton__qHB_q 79.0x40.0 bg #fdf7ef r 6px | a.FiberyButton_root__0jBYr.HeaderMainMenu_loginButton__qHB_q 79.0x40.0 bg #fdf7ef r 6px shadow #251d1a @ 0.1 0px 0px 0px 1px | a.FiberyButton_root__0jBYr.HeaderMainMenu_loginButton__qHB_q 79.0x40.0 bg #fdf7ef r 6px outline 1px auto #101010 offset 1px | a.FiberyButton_root__0jBYr.HeaderMainMenu_loginButton__qHB_q 79.0x40.0 bg #fdf7ef r 6px shadow #251d1a @ 0.0969406 0px 0px 0px 0.969406px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-signup

Sign up button. The dark "Sign up for free" header button — the FiberyButton solid variant; links to /sign-up, measured never followed.

Page: home. Selector: `header Sign up for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 153 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #251d1a | = | = | = |
| Box shadow | none | #251d1a 0px 0px 0px 1px | = | #251d1a 0px 0px 0px 1px |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16px/40px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #faebd6 | = | = | = |
| Text node | span.FiberyButton_content__4PHkJ: Suisse Intl 16px/40px 600, #faebd6 | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.FiberyButton_root__0jBYr.ui-sign-up-btn 153.0x40.0 bg #251d1a r 6px | a.FiberyButton_root__0jBYr.ui-sign-up-btn 153.0x40.0 bg #251d1a r 6px shadow #251d1a 0px 0px 0px 1px | a.FiberyButton_root__0jBYr.ui-sign-up-btn 153.0x40.0 bg #251d1a r 6px outline 1px auto #101010 offset 1px | a.FiberyButton_root__0jBYr.ui-sign-up-btn 153.0x40.0 bg #251d1a r 6px shadow #251d1a 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

### Home

#### announce-bar

Announcement pill. The announcement pill at the top of the hero ("Are we turning Fibery into yet another AI app builder?") — a link to the blog post; measured, never followed.

Page: home. Selector: `a.SpillTheTea_root`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 874.38 x 32 | = |
| Padding | 5px 20px | = |
| Gap | 10px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #f6d3a0 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16px/19.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | div.SpillTheTea_contentWrap__yEVpR: Suisse Intl 16px/19.2px 600, #251d1a | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #0000ee | = |
| Painted layers | a.SpillTheTea_root__OaVqJ.SpillTheTea_compact__lQMBC 874.4x32.0 bg #f6d3a0 r 16px | = |
| How | at rest | mouse hover |

Crops: `announce-bar-default.png`, `announce-bar-hover.png`.

#### hero-h1

Hero headline. "Operating system for orgs run by nerds" — the display headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440.23 x 256 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 64px/64px 800 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | span: Suisse Intl 64px/64px 800, #251d1a |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-lede

Hero lede. The muted supporting paragraph under the hero headline.

Page: home. Selector: `hero .Subtitle_root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352.19 x 70.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 18px/23.4px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### hero-cta

Hero CTA. The dark "Sign up" hero button (FiberyButton solid); measured never followed.

Page: home. Selector: `hero Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #251d1a | = | = | = |
| Box shadow | none | #251d1a 0px 0px 0px 1px | = | #251d1a 0px 0px 0px 1px |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16px/40px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #faebd6 | = | = | = |
| Text node | span.FiberyButton_content__4PHkJ: Suisse Intl 16px/40px 600, #faebd6 | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.FiberyButton_root__0jBYr.FiberyButton_solid__ytpGo 150.0x40.0 bg #251d1a r 6px | a.FiberyButton_root__0jBYr.FiberyButton_solid__ytpGo 150.0x40.0 bg #251d1a r 6px shadow #251d1a 0px 0px 0px 1px | a.FiberyButton_root__0jBYr.FiberyButton_solid__ytpGo 150.0x40.0 bg #251d1a r 6px outline 1px auto #101010 offset 1px | a.FiberyButton_root__0jBYr.FiberyButton_solid__ytpGo 150.0x40.0 bg #251d1a r 6px shadow #251d1a 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-cta2

Hero secondary CTA. The outlined "Book a Demo" hero button (FiberyButton outline); measured never followed.

Page: home. Selector: `hero Book a Demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #faebd6 @ 0.1 | = | = | = |
| Box shadow | #251d1a 0px 0px 0px 1px inset | #251d1a 0px 0px 0px 1px inset, #251d1a 0px 0px 0px 0.5px | = | #251d1a 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Backdrop filter | blur(1px) | blur(10px) | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Suisse Intl 16px/40px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #251d1a | = | = | = |
| Text node | span.FiberyButton_content__4PHkJ: Suisse Intl 16px/40px 600, #251d1a | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.FiberyButton_root__0jBYr.FiberyButton_outline__BzDGM 136.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset | button.FiberyButton_root__0jBYr.FiberyButton_outline__BzDGM 136.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset, #251d1a 0px 0px 0px 0.5px | button.FiberyButton_root__0jBYr.FiberyButton_outline__BzDGM 136.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset outline 1px auto #101010 offset 0px | button.FiberyButton_root__0jBYr.FiberyButton_outline__BzDGM 136.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta2-default.png`, `hero-cta2-hover.png`, `hero-cta2-focus-visible.png`, `hero-cta2-pressed.png`.

#### product-frame

Product video frame. The hero product video (the looping app screencast in a framed panel beside the copy, with its pause control); a public product mock, not the signed-in app.

Page: home. Selector: `.MainHero_screenSide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 854.58 x 480.69 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | transparent |
| Box shadow | #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px |
| Outline | none |
| Font | Suisse Intl 16px/0px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Transition | none |
| Icon | 24 x 24, colour #fffdfa |
| Painted layers | div.MainHero_screenSide__vs7Jo 854.6x480.7 r 20px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; button.VideoItem_control__lNTZU 40.0x40.0 bg #000000 @ 0.55 r 50% |
| How | at rest |

Crops: `product-frame-default.png`.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 592 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 48px/48px 800 |
| Letter spacing | normal |
| Colour | #faebd6 |
| Text node | span: Suisse Intl 48px/48px 800, #faebd6 |
| Transition | none |
| How | at rest |

Crops: none.

### Footer

#### footer

Footer. The page footer: sitemap columns, social icons, security/legal links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 489.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | p.FooterMain_statement__IvN_n: Suisse Intl 14px/21px 400, #251d1a |
| Transition | none |
| Icon | 86 x 36, colour #0000ee |
| Painted layers | div.FooterMain_mainPart__47yxl 1440.0x416.4 bg #fdf7ef; a.AskAiAboutFibery_urlItem__SKDx8.plausible-event-name=Ask+Chat+GPT+About+Fibery 25.0x25.0 bg #fffdfa border T:1px solid #eed0bf / R:1px solid #eed0bf / B:1px solid #eed0bf / L:1px solid #eed0bf r 6px; a.AskAiAboutFibery_urlItem__SKDx8.plausible-event-name=Ask+Claude+About+Fibery 25.0x25.0 bg #fffdfa border T:1px solid #eed0bf / R:1px solid #eed0bf / B:1px solid #eed0bf / L:1px solid #eed0bf r 6px; a.AskAiAboutFibery_urlItem__SKDx8.plausible-event-name=Ask+Gemini+About+Fibery 25.0x25.0 bg #fffdfa border T:1px solid #eed0bf / R:1px solid #eed0bf / B:1px solid #eed0bf / L:1px solid #eed0bf r 6px; a.AskAiAboutFibery_urlItem__SKDx8.plausible-event-name=Ask+Grok+About+Fibery 26.0x25.0 bg #fffdfa border T:1px solid #eed0bf / R:1px solid #eed0bf / B:1px solid #eed0bf / L:1px solid #eed0bf r 6px; a.AskAiAboutFibery_urlItem__SKDx8.plausible-event-name=Ask+Perplexity+About+Fibery 25.0x25.0 bg #fffdfa border T:1px solid #eed0bf / R:1px solid #eed0bf / B:1px solid #eed0bf / L:1px solid #eed0bf r 6px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 45 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #251d1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 45.0x24.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### price-h1

Pricing headline. "One platform for the whole company" — the /pricing masthead.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 52.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 48px/52.8px 800 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | div.TitleIconic_content__AKKki: Suisse Intl 48px/52.8px 800, #251d1a |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-switch

Billing switch. The Monthly/Yearly billing switch (a checkbox + label control); the toggled state flips the displayed prices — a local UI toggle, nothing sent.

Page: pricing. Selector: `.PriceSwitcher_root`. States: default, toggled.

| Property | default | toggled |
|---|---|---|
| Size (w x h) | 213 x 36 | = |
| Padding | 2px | = |
| Gap | 4px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #fdf7ef | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16px/19.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #251d1a | = |
| Text node | span.PriceSwitcher_monthlyText__ljgpl: Suisse Intl 14px/20px 500, #251d1a | span.PriceSwitcher_monthlyText__ljgpl: Suisse Intl 14px/20px 500, #fffdfa |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | label.PriceSwitcher_root__ixw3O 213.0x36.0 bg #fdf7ef r 8px; span.PriceSwitcher_yearlyText__lkp9F 127.0x32.0 bg #c17b58 r 6px shadow #000000 @ 0.15 0px 0px 3px 0px; span.PriceSwitcher_discount__RGNO5 62.0x22.0 bg #f0d7c8 r 4px | label.PriceSwitcher_root__ixw3O 213.0x36.0 bg #fdf7ef r 8px; span.PriceSwitcher_monthlyText__ljgpl 78.0x32.0 bg #c17b58 r 6px shadow #000000 @ 0.15 0px 0px 3px 0px; span.PriceSwitcher_yearlyText__lkp9F 127.0x32.0 bg #c17b58 @ 0.2 r 6px; span.PriceSwitcher_discount__RGNO5 62.0x22.0 bg #f6eae3 r 4px |
| How | at rest | clicked the label/switch — a local UI toggle; prices flip, nothing is sent |

Crops: `price-switch-default.png`, `price-switch-toggled.png`.

#### plan-card

Plan card. A pricing plan tile (the Free plan: name, icon, price, feature list, CTA).

Page: pricing. Selector: `.PricingPlans_planItem`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 282 x 559.27 |
| Padding | 40px 32px |
| Gap | 28px |
| Border | 1px solid #251d1a @ 0.1 |
| Radius | 12px |
| Background | #fdf7ef |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | span: Suisse Intl 24px/26.4px 800, #251d1a |
| Transition | all 0.3s ease |
| Icon | 18 x 18, colour #251d1a |
| ::before | 280px x 280px, absolute, bg #fbf0e1, radius 50% |
| Painted layers | div.PricingPlans_planItem__MmB8o 282.0x559.3 bg #fdf7ef border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 12px; div::before.PricingPlans_planItem__MmB8o 280pxx280px bg #fbf0e1 r 50%; a.FiberyButton_root__0jBYr.plausible-event-name=Signup+From+Pricing+Table 216.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset; span 119.0x19.2 image url(data:…); span 152.0x19.2 image url(data:…); span 162.0x19.2 image url(data:…) |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-card-paid

Paid plan card. A paid plan tile beside the Free plan.

Page: pricing. Selector: `.PricingPlans_planItem Pro`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 282 x 559.27 |
| Padding | 40px 32px |
| Gap | 28px |
| Border | 1px solid #251d1a @ 0.1 |
| Radius | 12px |
| Background | #fdf7ef |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | span: Suisse Intl 10px/12px 700, #fffdfa |
| Transition | all 0.3s ease |
| Icon | 14.14 x 14.14, colour #fffdfa |
| ::before | 280px x 280px, absolute, bg #f6eae3, radius 50% |
| Painted layers | div.PricingPlans_planItem__MmB8o 282.0x559.3 bg #fdf7ef border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 12px; div::before.PricingPlans_planItem__MmB8o 280pxx280px bg #f6eae3 r 50%; span.PricingPlans_aiBadge__78694 107.5x107.5 bg #2d6d7d; a.FiberyButton_root__0jBYr.plausible-event-name=Signup+From+Pricing+Table 216.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset; span 175.0x19.2 image url(data:…); span 35.0x19.2 image url(data:…) |
| How | at rest |

Crops: `plan-card-paid-default.png`.

#### plan-cta

Plan CTA. The call-to-action inside a plan tile; measured never followed.

Page: pricing. Selector: `plan CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 216 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #faebd6 @ 0.1 | = | = | = |
| Box shadow | #251d1a 0px 0px 0px 1px inset | #251d1a 0px 0px 0px 1px inset, #251d1a 0px 0px 0px 0.5px | = | #251d1a 0px 0px 0px 1px inset, #251d1a 0px 0px 0px 0.5px |
| Backdrop filter | blur(1px) | blur(10px) | = | blur(10px) |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Suisse Intl 16px/40px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #251d1a | = | = | = |
| Text node | span.FiberyButton_content__4PHkJ: Suisse Intl 16px/40px 600, #251d1a | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.FiberyButton_root__0jBYr.plausible-event-name=Signup+From+Pricing+Table 216.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset | a.FiberyButton_root__0jBYr.plausible-event-name=Signup+From+Pricing+Table 216.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset, #251d1a 0px 0px 0px 0.5px | a.FiberyButton_root__0jBYr.plausible-event-name=Signup+From+Pricing+Table 216.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset outline 1px auto #101010 offset 1px | a.FiberyButton_root__0jBYr.plausible-event-name=Signup+From+Pricing+Table 216.0x40.0 bg #faebd6 @ 0.1 r 6px shadow #251d1a 0px 0px 0px 1px inset, #251d1a 0px 0px 0px 0.5px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-item

FAQ item. A pricing FAQ row ("Is there a trial period?"); the opened state expands the answer — a local UI toggle.

Page: pricing. Selector: `.QandAItem_root`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 1200 x 73 | 1200 x 215.38 |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #251d1a @ 0.1; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16px/19.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #251d1a | = |
| Text node | div.QandAItem_questionHead__85Qr_: Suisse Intl 20px/32px 400, #132331 | div.QandAItem_questionHead__85Qr_.QandAItem_open__MKU7f: Suisse Intl 20px/32px 800, #132331 |
| Transition | none | = |
| Painted layers | div.QandAItem_root__Pe7di 1200.0x73.0 border B:1px solid #251d1a @ 0.1; div::after.QandAItem_questionHead__85Qr_ 9pxx9px border R:2px solid #242938 / B:2px solid #242938 | div.QandAItem_root__Pe7di 1200.0x215.4 border B:1px solid #251d1a @ 0.1; div::after.QandAItem_questionHead__85Qr_.QandAItem_open__MKU7f 9pxx9px border R:2px solid #242938 / B:2px solid #242938 |
| How | at rest | own toggle |

Crops: `faq-item-default.png`, `faq-item-opened.png`.

#### extend-table

Feature table. The plan-comparison feature table under the cards.

Page: pricing. Selector: `.PlansExtendTable_root, table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1270 x 6593.17 |
| Padding | 20px 35px |
| Border | none |
| Radius | 16px |
| Background | #fdf7ef |
| Box shadow | #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | span.PriceSwitcher_monthlyText__ljgpl: Suisse Intl 14px/20px 500, #fffdfa |
| Transition | none |
| Icon | 24 x 24, colour #251d1a |
| Painted layers | div.PlansExtendTable_root__rK6jB 1270.0x6593.2 bg #fdf7ef r 16px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; div.PlansExtendTable_tableHeader__GHAAU.PlansExtendTable_topTouch__HILBJ 1270.0x126.8 bg #fdf7ef; div::before.PlansExtendTable_tableHeader__GHAAU.PlansExtendTable_topTouch__HILBJ 1270pxx202.797px bg #fdf7ef shadow #14151a @ 0.08 0px 15px 10px -10px, #14151a @ 0.05 0px 1px 2px -2px; label.PriceSwitcher_root__ixw3O.PriceSwitcher_inTable__fYfC7 213.0x36.0 bg #faebd6 r 8px; span.PriceSwitcher_monthlyText__ljgpl 78.0x32.0 bg #c17b58 r 6px shadow #000000 @ 0.15 0px 0px 3px 0px; span.PriceSwitcher_discount__RGNO5 62.0x22.0 bg #f6eae3 r 4px |
| How | at rest |

Crops: none.

### Templates

#### tpl-h1

Templates headline. The /templates index headline.

Page: templates. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1144 x 52.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 48px/52.8px 800 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | div.TitleIconic_content__AKKki: Suisse Intl 48px/52.8px 800, #251d1a |
| Transition | none |
| How | at rest |

Crops: `tpl-h1-default.png`.

#### tpl-card

Template card. A template tile on the index (the square icon, name and description, tinted by --template-color); measured, never followed.

Page: templates. Selector: `a.CardTemplate_root`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 270.66 x 435.58 | = |
| Padding | 30px 30px 0px 30px | = |
| Gap | 10px | = |
| Border | 1px solid #f0b89b | = |
| Radius | 16px | = |
| Background | #fdf7ef | = |
| Box shadow | none | #c17b58 @ 0.25 4px 4px 20px 0px |
| Outline | none | = |
| Font | Suisse Intl 16px/19.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #251d1a | = |
| Text node | span: Suisse Intl 24px/28.8px 800, #251d1a | = |
| Transition | box-shadow 0.2s cubic-bezier(0.12, 0, 0.39, 0) | = |
| Cursor | pointer | = |
| Icon | 300 x 90, colour #251d1a, fill #000000 | = |
| Painted layers | a.CardTemplate_root__aGuJK 270.7x435.6 bg #fdf7ef border T:1px solid #f0b89b / R:1px solid #f0b89b / B:1px solid #f0b89b / L:1px solid #f0b89b r 16px; span.TemplateSingleItemIcon_templateItemSquare__2XQ_f.TemplateSingleItemIcon_customColor___wRor 36.0x36.0 bg #fdf7ef r 35%; span::before.TemplateSingleItemIcon_templateItemSquare__2XQ_f.TemplateSingleItemIcon_customColor___wRor 36pxx36px bg #9c2baf; span.TemplateSingleItemIcon_templateItemSquareIcon___dHZN.TemplateSingleItemIcon_customIcon___FjRb 36.0x36.0 bg #9c2baf r 12px; div::after.CardTemplate_pictureWrap__M6qs0 268.656pxx60px image linear-gradient(0deg, #fdf7ef 0px, #fdf6ed @ 0 100%); div.type-badge_badge__Zb4pJ 79.5x16.6 bg #9c2baf border T:1px solid #9c2baf / R:1px solid #9c2baf / B:1px solid #9c2baf / L:1px solid #9c2baf r 3px | a.CardTemplate_root__aGuJK 270.7x435.6 bg #fdf7ef border T:1px solid #f0b89b / R:1px solid #f0b89b / B:1px solid #f0b89b / L:1px solid #f0b89b r 16px shadow #c17b58 @ 0.25 4px 4px 20px 0px; span.TemplateSingleItemIcon_templateItemSquare__2XQ_f.TemplateSingleItemIcon_customColor___wRor 43.2x43.2 bg #fdf7ef r 35%; span::before.TemplateSingleItemIcon_templateItemSquare__2XQ_f.TemplateSingleItemIcon_customColor___wRor 36pxx36px bg #9c2baf; span.TemplateSingleItemIcon_templateItemSquareIcon___dHZN.TemplateSingleItemIcon_customIcon___FjRb 43.2x43.2 bg #9c2baf r 12px; div::after.CardTemplate_pictureWrap__M6qs0 268.656pxx60px image linear-gradient(0deg, #fdf7ef 0px, #fdf6ed @ 0 100%); div.type-badge_badge__Zb4pJ 79.5x16.6 bg #9c2baf border T:1px solid #9c2baf / R:1px solid #9c2baf / B:1px solid #9c2baf / L:1px solid #9c2baf r 3px |
| How | at rest | mouse hover |

Crops: `tpl-card-default.png`, `tpl-card-hover.png`.

#### tpl-icon

Template icon. A coloured template glyph (the square icon tile, tinted by --template-color).

Page: templates. Selector: `.TemplateSingleItemIcon_templateItemSquare`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 35% |
| Background | #fdf7ef |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Transition | none |
| Cursor | pointer |
| ::before | 36px x 36px, absolute, bg #9c2baf, radius 0px |
| Painted layers | span.TemplateSingleItemIcon_templateItemSquare__2XQ_f.TemplateSingleItemIcon_customColor___wRor 36.0x36.0 bg #fdf7ef r 35%; span::before.TemplateSingleItemIcon_templateItemSquare__2XQ_f.TemplateSingleItemIcon_customColor___wRor 36pxx36px bg #9c2baf |
| How | at rest |

Crops: `tpl-icon-default.png`.

### Sign-up wizard (fibery.io)

#### su-panel

Sign-up panel. The "Get a head start with AI" wizard step on fibery.io/sign-up: prompt field, premade solutions, the AI submit and "Start without AI".

Page: signup. Selector: `.FormWrap_root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 448.58 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | div.HeadlineGroup_headline__WlPI7.HeadlineGroup_large__MbV5W: Suisse Intl 24px/28.8px 700, #251d1a |
| Transition | none |
| Icon | 20 x 20, colour #000000 @ 0.7 |
| Painted layers | div.SpillTheTea_teaIconWrap__wOwL_ 32.0x32.0 bg #f6d3a0 r 8px; div.SpillTheTea_teaContent__tNd8n 0.0x0.0 bg #f6d3a0 r 8px 0px 8px 8px; textarea.AiPromptInput_textField__FYXHP 560.0x164.0 bg #ffffff r 20px shadow #000000 @ 0.1 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 6px 0px; div::before.AiPromptInput_controlsWrap__7AgKJ 540pxx52px bg #fffdfa r 0px 0px 10px 10px; button.FiberyButton_root__0jBYr.AiPromptInput_submitButton__VlAIj 162.0x32.0 bg #bd5f00 r 16px; button.AiPromptInput_premadeSolution__0TR7y.AiPromptInput_product__ZBk4O 164.0x28.0 bg #ffffff @ 0.5 r 16px shadow #000000 @ 0.05 0px 0px 0px 1px |
| How | at rest |

Crops: `su-panel-default.png`.

#### su-field

Prompt field. The AI workspace prompt textarea; focused and typed into then cleared — never submitted.

Page: signup. Selector: `textarea#promptField`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 560 x 164 | = | = |
| Padding | 16px 32px 50px 18px | = | = |
| Border | none | = | = |
| Radius | 20px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0.1 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 6px 0px | = | = |
| Outline | none | = | = |
| Font | Suisse Intl 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | all 0.3s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #251d1a, opacity 0.3 | = | = |
| Painted layers | textarea.AiPromptInput_textField__FYXHP 560.0x164.0 bg #ffffff r 20px shadow #000000 @ 0.1 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 6px 0px | = | = |
| How | at rest | clicked into the field | typed "Create a workspace for a bakery that includes suppliers and orders", then deleted; nothing sent |

Crops: `su-field-default.png`, `su-field-focused.png`, `su-field-filled.png`.

#### su-submit

Create workspace button. The AI wizard submit — disabled until the prompt holds text; the enabled state was measured after typing (the text was then cleared, never submitted).

Page: signup. Selector: `Create workspace`. States: default, hover, focus-visible, pressed, enabled.

| Property | default | hover | focus-visible | pressed | enabled |
|---|---|---|---|---|---|
| Size (w x h) | 162 x 32 | = | - | = | = |
| Padding | 6px 12px | = | - | = | = |
| Gap | 10px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 16px | = | - | = | = |
| Background | #bd5f00 | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Suisse Intl 14px/20px 500 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #fffdfa | = | - | = | = |
| Text node | span.FiberyButton_content__4PHkJ: Suisse Intl 14px/20px 500, #fffdfa | = | - | = | = |
| Transition | all 0.3s ease | = | - | = | = |
| Opacity | 0.5 | = | - | = | - |
| Cursor | not-allowed | = | - | = | pointer |
| Icon | 12 x 10, colour #fffdfa | = | - | = | = |
| Painted layers | button.FiberyButton_root__0jBYr.AiPromptInput_submitButton__VlAIj 162.0x32.0 bg #bd5f00 r 16px | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | typed into the prompt to enable the submit (cleared afterwards, never pressed) |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `su-submit-default.png`, `su-submit-hover.png`, `su-submit-pressed.png`, `su-submit-enabled.png`.

#### su-premade

Premade solution. A premade-solution chip ("Product development"); measured, never pressed — it fills the prompt.

Page: signup. Selector: `.AiPromptInput_premadeSolution`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 164 x 28 | = | = | = |
| Padding | 0px 12px 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff @ 0.5 | #ffffff @ 0.9 | = | #ffffff @ 0.9 |
| Box shadow | #000000 @ 0.05 0px 0px 0px 1px | #f0d7c8 0px 0px 0px 1px | = | #f0d7c8 0px 0px 0px 1px |
| Backdrop filter | blur(12px) | = | = | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 12px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.6 | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 @ 0.6 | = | = | = |
| Painted layers | button.AiPromptInput_premadeSolution__0TR7y.AiPromptInput_product__ZBk4O 164.0x28.0 bg #ffffff @ 0.5 r 16px shadow #000000 @ 0.05 0px 0px 0px 1px | button.AiPromptInput_premadeSolution__0TR7y.AiPromptInput_product__ZBk4O 164.0x28.0 bg #ffffff @ 0.9 r 16px shadow #f0d7c8 0px 0px 0px 1px | = | button.AiPromptInput_premadeSolution__0TR7y.AiPromptInput_product__ZBk4O 164.0x28.0 bg #ffffff @ 0.9 r 16px shadow #f0d7c8 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `su-premade-default.png`, `su-premade-hover.png`, `su-premade-focus-visible.png`, `su-premade-pressed.png`.

#### su-skip

Start without AI. The "Start without AI" skip action; measured, never followed — it advances the wizard.

Page: signup. Selector: `Start without AI`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 163 x 34 | = | = | = |
| Padding | 0px 8px 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #fffdfa | #251d1a | = | #251d1a |
| Box shadow | #251d1a 0px 0px 0px 1px | = | = | = |
| Backdrop filter | blur(12px) | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.SkipAiButton_textWrap__J7FK7: Suisse Intl 16px/34px 500, #251d1a | span.SkipAiButton_textWrap__J7FK7: Suisse Intl 16px/34px 500, #fffdfa | = | span.SkipAiButton_textWrap__J7FK7: Suisse Intl 16px/34px 500, #fffdfa |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.SkipAiButton_skipButton__ahFUu 163.0x34.0 bg #fffdfa r 6px shadow #251d1a 0px 0px 0px 1px; span::after.SkipAiButton_textWrap__J7FK7 18pxx18px bg #251d1a | button.SkipAiButton_skipButton__ahFUu 163.0x34.0 bg #251d1a r 6px shadow #251d1a 0px 0px 0px 1px; span::after.SkipAiButton_textWrap__J7FK7 18pxx18px bg #fffdfa | button.SkipAiButton_skipButton__ahFUu 163.0x34.0 bg #fffdfa r 6px shadow #251d1a 0px 0px 0px 1px outline 1px auto #101010 offset 0px; span::after.SkipAiButton_textWrap__J7FK7 18pxx18px bg #251d1a | button.SkipAiButton_skipButton__ahFUu 163.0x34.0 bg #251d1a r 6px shadow #251d1a 0px 0px 0px 1px; span::after.SkipAiButton_textWrap__J7FK7 18pxx18px bg #fffdfa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `su-skip-default.png`, `su-skip-hover.png`, `su-skip-focus-visible.png`, `su-skip-pressed.png`.

#### su-steps

Step pagination. The wizard step dots at the bottom (step 1 of the workspace-creation flow).

Page: signup. Selector: `.SignupStepPagination_step`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 198 x 11 |
| Padding | 0px 14px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Transition | none |
| Painted layers | button::before.SignupStepPagination_step__oPEqw.SignupStepPagination_active__EpG_s 50pxx3px bg #c17b58; button::before.SignupStepPagination_step__oPEqw.SignupStepPagination_disabled__KMDWj 50pxx3px bg #dedede; button::before.SignupStepPagination_step__oPEqw.SignupStepPagination_disabled__KMDWj 50pxx3px bg #dedede |
| How | at rest |

Crops: `su-steps-default.png`.

### Login (fibery.io)

#### login-panel

Login panel. The "Login to Fibery" form column on fibery.io/login: OAuth buttons, Continue with Email, Workspace SSO and the sign-up switch link.

Page: login. Selector: `.FormWrap_root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 276.8 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | div.HeadlineGroup_headline__WlPI7.HeadlineGroup_large__MbV5W: Suisse Intl 24px/28.8px 700, #251d1a |
| Transition | none |
| Icon | 16 x 16, colour #251d1a |
| Painted layers | div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset; div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset; button.FiberyButton_root__0jBYr.LoginMethodsForm_emailButton__SrJ_9 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset; button.FiberyButton_root__0jBYr.LoginMethodsForm_workspaceSsoButton__2Xc1J 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-google

Google OAuth. The "Continue with Google" OAuth submit — its form POSTs to /login/google/start; measured, never pressed.

Page: login. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.OAuthButtonLogin_text__Mhgx1: Suisse Intl 16px/20px 400, #251d1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #251d1a | = | = | = |
| Painted layers | div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.25 / R:1px solid #251d1a @ 0.25 / B:1px solid #251d1a @ 0.25 / L:1px solid #251d1a @ 0.25 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | button.OAuthButtonLogin_formButton__BcoL2 360.0x36.0 outline 1px auto #101010 offset 0px; div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-ms

Microsoft OAuth. The "Continue with Microsoft" OAuth submit; measured, never pressed.

Page: login. Selector: `Continue with Microsoft`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.OAuthButtonLogin_text__Mhgx1: Suisse Intl 16px/20px 400, #251d1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #251d1a | = | = | = |
| Painted layers | div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.25 / R:1px solid #251d1a @ 0.25 / B:1px solid #251d1a @ 0.25 / L:1px solid #251d1a @ 0.25 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | button.OAuthButtonLogin_formButton__BcoL2 360.0x36.0 outline 1px auto #101010 offset 0px; div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-ms-default.png`, `login-ms-hover.png`, `login-ms-focus-visible.png`, `login-ms-pressed.png`.

#### login-email

Email button. The "Continue with Email" button — reveals the e-mail step of the sign-in (a local step change, not a submission); the opened state was measured after pressing it.

Page: login. Selector: `Continue with Email`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 360 x 36 | = | = | = | = |
| Padding | 8px 12px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | 1px solid #251d1a @ 0.1 | 1px solid #251d1a @ 0.25 | = | 1px solid #251d1a @ 0.25 | = |
| Radius | 6px | = | = | = | = |
| Background | #fffdfa | = | = | = | = |
| Box shadow | #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Suisse Intl 16px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #251d1a | = | = | = | = |
| Text node | span: Suisse Intl 16px/20px 500, #251d1a | = | = | = | = |
| Transition | border-color 0.3s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 16, colour #251d1a | = | = | = | = |
| Painted layers | button.FiberyButton_root__0jBYr.LoginMethodsForm_emailButton__SrJ_9 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | button.FiberyButton_root__0jBYr.LoginMethodsForm_emailButton__SrJ_9 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.25 / R:1px solid #251d1a @ 0.25 / B:1px solid #251d1a @ 0.25 / L:1px solid #251d1a @ 0.25 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | button.FiberyButton_root__0jBYr.LoginMethodsForm_emailButton__SrJ_9 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset outline 1px auto #101010 offset 0px | button.FiberyButton_root__0jBYr.LoginMethodsForm_emailButton__SrJ_9 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.25 / R:1px solid #251d1a @ 0.25 / B:1px solid #251d1a @ 0.25 / L:1px solid #251d1a @ 0.25 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | held open by an earlier toggle |

Crops: `login-email-default.png`, `login-email-hover.png`, `login-email-pressed.png`, `login-email-opened.png`.

#### login-email-field

Email field (login). The e-mail input revealed by the "Continue with Email" step; focused and typed into then cleared — never submitted.

Page: login. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 360 x 36 | = | = |
| Padding | 4px 12px | = | = |
| Border | 1px solid #251d1a @ 0.1 | 1px solid #251d1a @ 0.25 | 1px solid #251d1a @ 0.25 |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Suisse Intl 16px/28px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | all 0.3s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #251d1a, opacity 0.3 | = | = |
| Painted layers | input.LoginMethodsForm_input__d0tXF.LoginMethodsForm_email__Xbrrf 360.0x36.0 bg #ffffff border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px | input.LoginMethodsForm_input__d0tXF.LoginMethodsForm_email__Xbrrf 360.0x36.0 bg #ffffff border T:1px solid #251d1a @ 0.25 / R:1px solid #251d1a @ 0.25 / B:1px solid #251d1a @ 0.25 / L:1px solid #251d1a @ 0.25 r 6px | input.LoginMethodsForm_input__d0tXF.LoginMethodsForm_email__Xbrrf 360.0x36.0 bg #ffffff border T:1px solid #251d1a @ 0.25 / R:1px solid #251d1a @ 0.25 / B:1px solid #251d1a @ 0.25 / L:1px solid #251d1a @ 0.25 r 6px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-field-default.png`, `login-email-field-focused.png`, `login-email-field-filled.png`.

#### login-sso

Workspace SSO. The "Workspace SSO" button; measured, never followed.

Page: login. Selector: `Workspace SSO`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #251d1a @ 0.1 | 1px solid #251d1a @ 0.25 | = | 1px solid #251d1a @ 0.25 |
| Radius | 6px | = | = | = |
| Background | #fffdfa | = | = | = |
| Box shadow | #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Suisse Intl 16px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #251d1a | = | = | = |
| Text node | span: Suisse Intl 16px/20px 500, #251d1a | = | = | = |
| Transition | border-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 18, colour #251d1a | = | = | = |
| Painted layers | button.FiberyButton_root__0jBYr.LoginMethodsForm_workspaceSsoButton__2Xc1J 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | button.FiberyButton_root__0jBYr.LoginMethodsForm_workspaceSsoButton__2Xc1J 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.25 / R:1px solid #251d1a @ 0.25 / B:1px solid #251d1a @ 0.25 / L:1px solid #251d1a @ 0.25 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset | button.FiberyButton_root__0jBYr.LoginMethodsForm_workspaceSsoButton__2Xc1J 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.1 / R:1px solid #251d1a @ 0.1 / B:1px solid #251d1a @ 0.1 / L:1px solid #251d1a @ 0.1 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset outline 1px auto #101010 offset 0px | button.FiberyButton_root__0jBYr.LoginMethodsForm_workspaceSsoButton__2Xc1J 360.0x36.0 bg #fffdfa border T:1px solid #251d1a @ 0.25 / R:1px solid #251d1a @ 0.25 / B:1px solid #251d1a @ 0.25 / L:1px solid #251d1a @ 0.25 r 6px shadow #d6d6d6 @ 0.01 0px 9px 2px 0px, #d6d6d6 @ 0.05 0px 6px 2px 0px, #d6d6d6 @ 0.18 0px 3px 2px 0px, #d6d6d6 @ 0.3 0px 1px 1px 0px, #d6d6d6 @ 0.35 0px 0px 1px 0px, #ffffff @ 0.2 0px 1px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-sso-default.png`, `login-sso-hover.png`, `login-sso-focus-visible.png`, `login-sso-pressed.png`.

#### login-hint

Hint card. The "Did you know?" tip card beside the sign-in (the dark/system theme tip).

Page: login. Selector: `.HintSideSection_root, .HintItem_root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560.8 x 850 |
| Padding | 40px |
| Border | none |
| Radius | 20px |
| Background | #d5d8ca |
| Background image | url(…) |
| Box shadow | #000000 @ 0.05 0px 0px 0px 1px inset |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | div.HintSideSection_headline__RzAMO: Suisse Intl 20px/20px 700, #251d1a |
| Transition | none |
| Icon | 18 x 18, colour #000000 |
| Painted layers | div.HintSideSection_root__Fr0sI 560.8x850.0 bg #d5d8ca r 20px shadow #000000 @ 0.05 0px 0px 0px 1px inset; div.HintSideSection_hintItem__vOZla 446.0x162.0 bg #fffdfa r 16px |
| How | at rest |

Crops: `login-hint-default.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header: Fibery mark, the sandwich button and the sign-up CTA.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 77 |
| Padding | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Transition | none |
| Icon | 127 x 36, colour #0000ee |
| Painted layers | div.HeaderMainMenu_root__idMKp 366.0x53.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; nav::before.HeaderMainMenu_menuList__q0OJp 100%x100% bg #fff5e8 r 10px; div.HeaderMainMenu_headerDivider__6tgCG 0.0x0.0 bg #000000 @ 0.25; div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; span::after.HeaderMenuItem_menuLink__JgNSg 5pxx5px border R:2px solid #251d1a / B:2px solid #251d1a; div.HeaderMenuDropdown_root__uAFiX 0.0x0.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-menu-btn

Mobile menu button. The icon-only sandwich button that opens the phone nav — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `.HeaderMainMenu_sandwichBtn`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Suisse Intl 16px/19.2px 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #251d1a | = | - | = | = |
| Transition | none | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| ::before | 20px x 2px, static, bg #251d1a, radius 2px | = | - | = | = |
| ::after | 20px x 2px, static, bg #251d1a, radius 2px | = | - | = | = |
| Painted layers | div::before.HeaderMainMenu_sandwichBtn__VTPQ2 20pxx2px bg #251d1a r 2px; div::after.HeaderMainMenu_sandwichBtn__VTPQ2 20pxx2px bg #251d1a r 2px | = | - | = | = |
| Ancestor paint | 2 up div.HeaderMainMenu_root__idMKp bg #fff5e8 shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px | = | - | = | 2 up div.HeaderMainMenu_root__idMKp.HeaderMainMenu_mobileMenuOpen__Q6P7N bg #fff5e8 shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | held open by an earlier toggle |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav. The nav drawer opened by the sandwich button — the menu list plus the Book a demo / Log in / Sign up buttons; its links were never followed.

Page: mobile. Selector: `.HeaderMainMenu_mobileMenu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366 x 749.97 |
| Padding | 12px |
| Border | none |
| Radius | 12px |
| Background | #fff5e8 |
| Box shadow | #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px |
| Backdrop filter | blur(20px) |
| Outline | none |
| Font | Suisse Intl 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | span.HeaderMenuItem_menuLink__JgNSg.HeaderMenuItem_buttonLink__G_7l2: Suisse Intl 16px/34px 500, #251d1a |
| Transition | none |
| Icon | 127 x 36, colour #0000ee |
| Painted layers | div.HeaderMainMenu_root__idMKp.HeaderMainMenu_mobileMenuOpen__Q6P7N 366.0x750.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px; nav::before.HeaderMainMenu_menuList__q0OJp.HeaderMainMenu_bgVisible__fOEfU 100%x100% bg #fff5e8 r 10px; div.HeaderMainMenu_headerDivider__6tgCG 0.0x0.0 bg #000000 @ 0.25; div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; span::after.HeaderMenuItem_menuLink__JgNSg 5pxx5px border R:2px solid #251d1a / B:2px solid #251d1a; div.HeaderMenuDropdown_root__uAFiX 0.0x0.0 bg #fff5e8 r 12px shadow #14151a @ 0.08 0px 10px 16px -3px, #14151a @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The display headline at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358.81 x 184 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 46px/46px 800 |
| Letter spacing | normal |
| Colour | #251d1a |
| Text node | span: Suisse Intl 46px/46px 800, #251d1a |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The "Sign up" hero button at 390 wide; measured never followed.

Page: mobile. Selector: `mobile Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358.81 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #251d1a | = | = | = |
| Box shadow | none | = | = | #251d1a 0px 0px 0px 1px |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Suisse Intl 16px/40px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #faebd6 | = | = | = |
| Text node | span.FiberyButton_content__4PHkJ: Suisse Intl 16px/40px 600, #faebd6 | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.FiberyButton_root__0jBYr.FiberyButton_solid__ytpGo 358.8x40.0 bg #251d1a r 6px | = | a.FiberyButton_root__0jBYr.FiberyButton_solid__ytpGo 358.8x40.0 bg #251d1a r 6px outline 1px auto #e59700 offset 1px | a.FiberyButton_root__0jBYr.FiberyButton_solid__ytpGo 358.8x40.0 bg #251d1a r 6px shadow #251d1a 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

fibery.com and fibery.io serve their CSS same-origin as Next.js `/_next/static/css/` chunks, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- home: `0.3s`, `0.2s ease-in-out`, `border-color 0.3s`, `opacity 0.3s`, `transform 0.3s`, `background-color 0.3s`, `transform 0.3s, opacity 0.3s linear`, `opacity 0.1s linear, transform 0.1s linear`, `transform 0.1s ease-out`, `color 0.3s`, `transform 0.3s ease-in-out`, `height 0.3s ease-in-out`

- login: `0.3s`, `0.2s ease-in-out`, `border-color 0.3s`, `opacity 0.3s`, `transform 0.3s`, `background-color 0.3s`, `transform 0.3s, opacity 0.3s linear`, `opacity 0.1s linear, transform 0.1s linear`, `transform 0.1s ease-out`, `color 0.3s`, `transform 0.3s ease-in-out`, `height 0.3s ease-in-out`

- pricing: `0.3s`, `0.2s ease-in-out`, `border-color 0.3s`, `opacity 0.3s`, `transform 0.3s`, `background-color 0.3s`, `transform 0.3s, opacity 0.3s linear`, `opacity 0.1s linear, transform 0.1s linear`, `transform 0.1s ease-out`, `color 0.3s`, `transform 0.3s ease-in-out`, `height 0.3s ease-in-out`

- signup: `0.3s`, `0.2s ease-in-out`, `border-color 0.3s`, `opacity 0.3s`, `transform 0.3s`, `background-color 0.3s`, `transform 0.3s, opacity 0.3s linear`, `opacity 0.1s linear, transform 0.1s linear`, `transform 0.1s ease-out`, `color 0.3s`, `transform 0.3s ease-in-out`, `height 0.3s ease-in-out`

- templates: `0.3s`, `0.2s ease-in-out`, `border-color 0.3s`, `opacity 0.3s`, `transform 0.3s`, `background-color 0.3s`, `transform 0.3s, opacity 0.3s linear`, `opacity 0.1s linear, transform 0.1s linear`, `transform 0.1s ease-out`, `color 0.3s`, `transform 0.3s ease-in-out`, `height 0.3s ease-in-out`

## Reduced motion

- home (`header a[class*="FiberyButton"], header [class*="FiberyButton"]` under prefers-reduced-motion): transition `0.3s`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
