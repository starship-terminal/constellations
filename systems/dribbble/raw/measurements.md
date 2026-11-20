# Component measurements

Computed styles read from dribbble.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) — every captured surface paints light; the floating project-brief card, the Google One Tap prompt and any consent overlay were hidden, never answered — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The site nav bar (div.site-nav): the script Dribbble wordmark, the Explore/Hire-Talent/Get-Hired/Community dropdown triggers, the pink Start-Project-Brief link, Sign up and the dark Log-in pill.

Page: home. Selector: `.site-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #060318 |
| Text node | a.site-nav-main__link: Mona Sans 14px/30px 600, #060318 |
| Transition | opacity 0.4s ease-in-out delay 0.1s |
| Icon | 89 x 25, colour #060318 |
| Painted layers | div.site-nav__dark-overlay 1440.0x900.0 bg #000000 @ 0.5; div::before.site-nav__wrapper 1440pxx92px bg #ffffff; span 0.0x0.0 bg #060318 r 1e+07px; span 0.0x0.0 bg #060318 r 1e+07px; span 0.0x0.0 bg #060318 r 1e+07px; div.site-nav-search.site-nav-search--nav 0.0x0.0 bg #ffffff |
| Ancestor paint | 1 up body.logged-out.not-pro bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The script Dribbble wordmark anchor.

Page: home. Selector: `a.site-nav__logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 89 x 25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #060318 |
| Transition | color 0.1s ease |
| Cursor | pointer |
| Icon | 89 x 25, colour #060318 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Explore link that opens the header dropdown on hover; hovered, never followed.

Page: home. Selector: `a.site-nav-main__link "Explore"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.84 x 30 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/30px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #060318 | #7b7194 | = | #7b7194 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 9px x 8px, static, bg #000000 @ 0 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='9' viewBox='0 0 10 9' fill='none'%3, radius 0px | = | = | = |
| Painted layers | a::after.site-nav-main__link 9pxx8px image url(data:…) | = | a.site-nav-main__link 97.8x30.0 outline 2px solid #f3afe4 offset 1px; a::after.site-nav-main__link 9pxx8px image url(data:…) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav item. The Community dropdown trigger.

Page: home. Selector: `a.site-nav-main__link "Community"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126.97 x 30 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/30px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #060318 | #7b7194 | = | #7b7194 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 9px x 8px, static, bg #000000 @ 0 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='9' viewBox='0 0 10 9' fill='none'%3, radius 0px | = | = | = |
| Painted layers | a::after.site-nav-main__link 9pxx8px image url(data:…) | = | a.site-nav-main__link 127.0x30.0 outline 2px solid #f3afe4 offset 1px; a::after.site-nav-main__link 9pxx8px image url(data:…) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### signup-link

Sign-up link. The plain Sign-up header action; measured never followed.

Page: home. Selector: `.site-nav__signup`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.63 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/17px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #060318 | #7b7194 | = | #7b7194 |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.site-nav__signup.site-nav-hide-mobile 50.6x17.0 outline 2px solid #f3afe4 offset 1px | = |

Crops: `signup-link-default.png`, `signup-link-hover.png`, `signup-link-focus-visible.png`, `signup-link-pressed.png`.

#### login-btn

Log-in button. The dark Log-in pill (btn2--medium); measured never followed.

Page: home. Selector: `.site-nav__login.btn2`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 89.2 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #0d0c22 | 1px solid #3d3d4e | 1px solid #3d3d4e | 1px solid #3d3d4e |
| Radius | 1e+07px | = | = | = |
| Background | #0d0c22 | #3d3d4e | #3d3d4e | #3d3d4e |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/14px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 87.2031px x 46px, absolute, bg #0d0c22, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | a.site-nav__login.btn2 89.2x48.0 bg #0d0c22 border T:1px solid #0d0c22 / R:1px solid #0d0c22 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 1e+07px; a::before.site-nav__login.btn2 87.2031pxx46px bg #0d0c22; a::after.site-nav__login.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.site-nav__login.btn2 89.2x48.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.site-nav__login.btn2 87.2031pxx46px bg #0d0c22; a::after.site-nav__login.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.site-nav__login.btn2 89.2x48.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px outline 2px solid #f3afe4 offset 1px; a::before.site-nav__login.btn2 87.2031pxx46px bg #0d0c22; a::after.site-nav__login.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.site-nav__login.btn2 89.2x48.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.site-nav__login.btn2 87.2031pxx46px bg #0d0c22; a::after.site-nav__login.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-btn-default.png`, `login-btn-hover.png`, `login-btn-focus-visible.png`, `login-btn-pressed.png`.

#### nav-dropdown

Nav dropdown. The Explore dropdown panel (ul.site-nav-sub: Popular, New and Noteworthy, category links), opened by hovering its own trigger.

Page: home. Selector: `ul.site-nav-sub`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 230 x 479 |
| Padding | 24px |
| Border | 1px solid #e7e7e9 @ 0.5 |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #1b2032 @ 0.1 0px 15px 50px 0px |
| Outline | none |
| Font | Mona Sans 16px/16px 400 |
| Letter spacing | normal |
| Colour | #060318 |
| Text node | a.site-nav-sub__link.site-nav-sub__link--bold: Mona Sans 14px/17px 600, #060318 |
| Transition | opacity, visibility, transform, -webkit-transform 0.2s, 0.2s, 0.3s, 0.3s ease-in-out, ease-in-out, cubic-bezier(0.34, 1.56, 0.64, 1), cubic-bezier(0.34, 1.56, 0.64, 1) delay 0.05s, 0.05s, 0.05s, 0.05s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 20 x 20, colour #060318 |
| ::before | 228px x 18px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | ul.site-nav-sub 230.0x479.0 bg #ffffff border T:1px solid #e7e7e9 @ 0.5 / R:1px solid #e7e7e9 @ 0.5 / B:1px solid #e7e7e9 @ 0.5 / L:1px solid #e7e7e9 @ 0.5 r 8px shadow #1b2032 @ 0.1 0px 15px 50px 0px; li::after.site-nav-sub__divider 180pxx1px bg #d8d6d5 |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A link inside the opened Explore dropdown (each state re-hovers the Explore trigger first).

Page: home. Selector: `.site-nav-sub a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 32 | = | = | = |
| Padding | 0px 0px 12px 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | 2px solid #f3afe4 offset 1px |
| Font | Mona Sans 14px/17px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #060318 | #7b7194 | = | #7b7194 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #060318 | 20 x 20, colour #7b7194 | = | 20 x 20, colour #7b7194 |
| Ancestor paint | 2 up ul.site-nav-sub bg #ffffff shadow #1b2032 @ 0.1 0px 15px 50px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.site-nav-sub__link.site-nav-sub__link--bold 180.0x32.0 outline 2px solid #f3afe4 offset 1px | a.site-nav-sub__link.site-nav-sub__link--bold 180.0x32.0 outline 2px solid #f3afe4 offset 1px |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

#### search-input

Header search field. The "What are you looking for?" header field on inner pages; focused only, never submitted.

Page: shots. Selector: `.site-nav search input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 388.58 x 54 | = |
| Padding | 0px 0px 0px 24px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Mona Sans 14px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #060318 | = |
| Transition | background-color, outline, color, box-shadow, -webkit-box-shadow 0.2s, 0.2s, 0.2s, 0.2s, 0.2s ease, ease, ease, ease, ease delay 0s, 0s, 0s, 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #3a3546, opacity 1 | = |
| How | at rest | clicked into the field |

Crops: `search-input-default.png`, `search-input-focused.png`.

#### scope-select

Scope dropdown. The Shots scope selector beside the header search field (site-nav-search__dropdown-trigger); its list was never opened.

Page: shots. Selector: `.site-nav-search__dropdown-trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.42 x 40 | = | = | = |
| Padding | 0px 18.5px 0px 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Mona Sans 14px/14px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3a3546 | #7b7194 | = | #7b7194 |
| Text node | span: Mona Sans 14px/14px 600, #3a3546 | span: Mona Sans 14px/14px 600, #7b7194 | = | span: Mona Sans 14px/14px 600, #7b7194 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 14px x 14px, absolute, bg #000000 @ 0 url(…), radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 2 up div.site-nav-search__wrapper bg #ffffff outline 3px solid #faebf9 | = | = |

Crops: `scope-select-default.png`, `scope-select-hover.png`, `scope-select-focus-visible.png`, `scope-select-pressed.png`.

### Home

#### promo-banner

Promo banner. The WELCOME20 offer strip under the header — page content, measured where it sits; its Get-Started action was never pressed.

Page: home. Selector: `promo banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 62 |
| Padding | 0px 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Text node | p: Mona Sans 14px/19.6px 500, #0d0c22 |
| Transition | none |
| Icon | 31 x 31, colour #7b7194 |
| Painted layers | div.announcements__container 1360.0x62.0 bg #f4d7f3 @ 0.3 border T:1px solid #faebf9 / R:1px solid #faebf9 / B:1px solid #faebf9 / L:1px solid #faebf9 r 1e+07px; a.btn2.btn2--x-small 101.8x32.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; a::before.btn2.btn2--x-small 99.7656pxx30px bg #ffffff; a::after.btn2.btn2--x-small 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% |
| Ancestor paint | 1 up body.logged-out.not-pro bg #ffffff |
| How | at rest |

Crops: `promo-banner-default.png`.

#### hero-title

Hero headline. The "Work with the world's best" display headline; one word rotates and paints the Dribbble pink.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 618 x 124.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 52px/62.4px 600 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-accent

Hero accent word. The rotating accent word inside the headline.

Page: home. Selector: `h1 accent span`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 418.44 x 62.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 52px/62.4px 600 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Text node | span: Mona Sans 52px/62.4px 600, #ea4c89 |
| Transition | none |
| ::before | auto x auto, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `hero-accent-default.png`.

#### hero-check

Hero checklist item. A pink-check bullet under the hero (li.home-header__list-item).

Page: home. Selector: `.home-header__list li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 618 x 22 |
| Padding | 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/21px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| ::before | 23px x 21px, static, bg #ea4c89 @ 0.1, radius 50% |
| Painted layers | li::before.home-header__list-item 23pxx21px bg #ea4c89 @ 0.1 r 50% |
| How | at rest |

Crops: `hero-check-default.png`.

#### hero-cta

Hero CTA. The "Start Your Project Brief" dark pill; measured never followed.

Page: home. Selector: `"Start Your Project Brief"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 230.03 x 49 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #0d0c22 | 1px solid #3d3d4e | 1px solid #3d3d4e | 1px solid #3d3d4e |
| Radius | 1e+07px | = | = | = |
| Background | #0d0c22 | #3d3d4e | #3d3d4e | #3d3d4e |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/14px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17 x 17, colour #ffffff | = | = | = |
| ::before | 228.031px x 47px, absolute, bg #0d0c22, radius 0px | = | = | = |
| ::after | 17px x 17px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | a.btn2 230.0x49.0 bg #0d0c22 border T:1px solid #0d0c22 / R:1px solid #0d0c22 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 1e+07px; a::before.btn2 228.031pxx47px bg #0d0c22; a::after.btn2 17pxx17px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2 230.0x49.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.btn2 228.031pxx47px bg #0d0c22; a::after.btn2 17pxx17px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2 230.0x49.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px outline 2px solid #f3afe4 offset 1px; a::before.btn2 228.031pxx47px bg #0d0c22; a::after.btn2 17pxx17px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2 230.0x49.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.btn2 228.031pxx47px bg #0d0c22; a::after.btn2 17pxx17px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-media

Hero media card. The shot media panel beside the hero copy (figure.home-header-media, the animated designer-work card).

Page: home. Selector: `.home-header-media`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 614 x 430 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #f3f3f6 |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Text node | a.home-header-media__designer-badge: Mona Sans 12px/28px 500, #0d0c22 |
| Transition | none |
| Painted layers | div.home-header-right__media-container 614.0x430.0 bg #f3f3f6 r 24px; a.home-header-media__designer-badge 171.1x40.0 bg #ffffff r 1e+07px shadow #000000 @ 0.14 0px 3px 6px 0px; a.home-header-media__designer-badge 110.3x40.0 bg #ffffff r 1e+07px shadow #000000 @ 0.14 0px 3px 6px 0px; a.home-header-media__designer-badge 89.2x40.0 bg #ffffff r 1e+07px shadow #000000 @ 0.14 0px 3px 6px 0px; a.home-header-media__designer-badge 158.9x40.0 bg #ffffff r 1e+07px shadow #000000 @ 0.14 0px 3px 6px 0px; a.home-header-media__designer-badge 102.6x40.0 bg #ffffff r 1e+07px shadow #000000 @ 0.14 0px 3px 6px 0px |
| How | at rest |

Crops: `hero-media-default.png`.

#### view-tab

View tab. A Shots/Designers/Services tab (a segmented-control label) over the search strip.

Page: home. Selector: `segmented control label`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100.14 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Mona Sans 16px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | span: Mona Sans 13px/13px 600, #3a3546 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 18 x 18, colour #3a3546 | = | = | = |
| Painted layers | input 20.0x20.0 bg #b8509a border T:1px solid #783c6a / R:1px solid #783c6a / B:1px solid #783c6a / L:1px solid #783c6a r 50%; input::after 10pxx10px bg #ffffff r 50%; span 100.1x40.0 bg #faf9fb border T:1px solid #faf9fb / R:1px solid #faf9fb / B:1px solid #faf9fb / L:1px solid #faf9fb r 1e+07px | = | input 20.0x20.0 bg #b8509a border T:1px solid #783c6a / R:1px solid #783c6a / B:1px solid #783c6a / L:1px solid #783c6a r 50%; input::after 10pxx10px bg #ffffff r 50%; span 100.1x40.0 bg #faf9fb border T:1px solid #faf9fb / R:1px solid #faf9fb / B:1px solid #faf9fb / L:1px solid #faf9fb r 1e+07px outline 2px solid #0d0c22 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `view-tab-default.png`, `view-tab-hover.png`, `view-tab-focus-visible.png`, `view-tab-pressed.png`.

#### home-search

Search field. The "What type of design are you interested in?" pill field; focused only, never submitted.

Page: home. Selector: `home search input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 1234 x 54 | = |
| Padding | 0px 0px 0px 24px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Mona Sans 14px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #060318 | = |
| Transition | background-color, outline, color, box-shadow, -webkit-box-shadow 0.2s, 0.2s, 0.2s, 0.2s, 0.2s ease, ease, ease, ease, ease delay 0s, 0s, 0s, 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #3a3546, opacity 1 | = |
| How | at rest | clicked into the field |

Crops: `home-search-default.png`, `home-search-focused.png`.

#### search-go

Search button. The pink circle search button (btn2--circle); measured never pressed.

Page: home. Selector: `search submit button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #ea4c89 | 1px solid #ec5e95 | 1px solid #ec5e95 | 1px solid #ec5e95 |
| Radius | 50% | = | = | = |
| Background | #ea4c89 | #ec5e95 | #ec5e95 | #ec5e95 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 0px | = |
| Font | Mona Sans 13px/13px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| ::before | 38px x 38px, absolute, bg #ea4c89, radius 0px | = | = | = |
| ::after | 20px x 20px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | button.site-nav-search__btn.btn2 40.0x40.0 bg #ea4c89 border T:1px solid #ea4c89 / R:1px solid #ea4c89 / B:1px solid #ea4c89 / L:1px solid #ea4c89 r 50%; button::before.site-nav-search__btn.btn2 38pxx38px bg #ea4c89; button::after.site-nav-search__btn.btn2 20pxx20px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | button.site-nav-search__btn.btn2 40.0x40.0 bg #ec5e95 border T:1px solid #ec5e95 / R:1px solid #ec5e95 / B:1px solid #ec5e95 / L:1px solid #ec5e95 r 50%; button::before.site-nav-search__btn.btn2 38pxx38px bg #ea4c89; button::after.site-nav-search__btn.btn2 20pxx20px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | button.site-nav-search__btn.btn2 40.0x40.0 bg #ec5e95 border T:1px solid #ec5e95 / R:1px solid #ec5e95 / B:1px solid #ec5e95 / L:1px solid #ec5e95 r 50% outline 2px solid #f3afe4 offset 0px; button::before.site-nav-search__btn.btn2 38pxx38px bg #ea4c89; button::after.site-nav-search__btn.btn2 20pxx20px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | button.site-nav-search__btn.btn2 40.0x40.0 bg #ec5e95 border T:1px solid #ec5e95 / R:1px solid #ec5e95 / B:1px solid #ec5e95 / L:1px solid #ec5e95 r 50%; button::before.site-nav-search__btn.btn2 38pxx38px bg #ea4c89; button::after.site-nav-search__btn.btn2 20pxx20px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% |
| Ancestor paint | 1 up div.site-nav-search__wrapper bg #f3f3f6 outline 3px solid #000000 @ 0 | 1 up div.site-nav-search__wrapper bg #ffffff outline 3px solid #faebf9 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-go-default.png`, `search-go-hover.png`, `search-go-focus-visible.png`, `search-go-pressed.png`.

#### tag-chip

Tag chip. A Popular-search tag link under the field.

Page: home. Selector: `popular tag a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.53 x 31 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #e7e7e9 | = | = | = |
| Radius | 1e+07px | = | = | = |
| Background | #ffffff | #faf9fb | = | #faf9fb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 12px/12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pill2.pill2--white-dark 93.5x31.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px | a.pill2.pill2--white-dark 93.5x31.0 bg #faf9fb border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px | a.pill2.pill2--white-dark 93.5x31.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px outline 2px solid #f3afe4 offset 1px | a.pill2.pill2--white-dark 93.5x31.0 bg #faf9fb border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tag-chip-default.png`, `tag-chip-hover.png`, `tag-chip-focus-visible.png`, `tag-chip-pressed.png`.

#### sort-select

Sort control. The "Popular" sort dropdown; its list was never opened.

Page: home. Selector: `"Popular" control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94.45 x 35 | = | = | = |
| Padding | 0px 34px 0px 14px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #dbdade @ 0.9 | 1px solid #9e9ea7 @ 0.7 | 1px solid #9e9ea7 @ 0.7 | 1px solid #9e9ea7 @ 0.7 |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #060318 @ 0.01 0px 4px 4px 0px | #060318 @ 0.03 0px 4px 4px 0px | #060318 @ 0.03 0px 4px 4px 0px | #060318 @ 0.03 0px 4px 4px 0px |
| Outline | none | = | = | = |
| Font | Mona Sans 12px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | span: Mona Sans 12px/12px 500, #0d0c22 | = | = | = |
| Transition | color, box-shadow, border, background-color, -webkit-box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0 url(…), radius 0px | = | = | = |
| Painted layers | button.dropdown2 94.5x35.0 bg #ffffff border T:1px solid #dbdade @ 0.9 / R:1px solid #dbdade @ 0.9 / B:1px solid #dbdade @ 0.9 / L:1px solid #dbdade @ 0.9 r 8px shadow #060318 @ 0.01 0px 4px 4px 0px | button.dropdown2 94.5x35.0 bg #ffffff border T:1px solid #9e9ea7 @ 0.7 / R:1px solid #9e9ea7 @ 0.7 / B:1px solid #9e9ea7 @ 0.7 / L:1px solid #9e9ea7 @ 0.7 r 8px shadow #060318 @ 0.03 0px 4px 4px 0px | button.dropdown2 94.5x35.0 bg #ffffff border T:1px solid #9e9ea7 @ 0.7 / R:1px solid #9e9ea7 @ 0.7 / B:1px solid #9e9ea7 @ 0.7 / L:1px solid #9e9ea7 @ 0.7 r 8px shadow #060318 @ 0.03 0px 4px 4px 0px | button.dropdown2 94.5x35.0 bg #ffffff border T:1px solid #9e9ea7 @ 0.7 / R:1px solid #9e9ea7 @ 0.7 / B:1px solid #9e9ea7 @ 0.7 / L:1px solid #9e9ea7 @ 0.7 r 8px shadow #060318 @ 0.03 0px 4px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sort-select-default.png`, `sort-select-hover.png`, `sort-select-focus-visible.png`, `sort-select-pressed.png`.

### Shot feed

#### shot-card

Shot card. The one card the signed-out feed paints before the wall: image, designer avatar + name, PRO/PRO+ badge, like and view counts.

Page: shots. Selector: `shot card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 297 x 254.75 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Mona Sans 14px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | div.shot-title: Mona Sans 14px/20px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Icon | 16 x 16, colour #0d0c22 | = | = | = |
| Painted layers | div::after.js-thumbnail-base.shot-thumbnail-base 297pxx222.75px image linear-gradient(#000000 @ 0 0%, #000000 @ 0 8.1%, #000000 @ 0 15.5%, #000000 @ 0.004 22.5%; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 297.0x222.8 bg #e5e2c0; div.shot-thumbnail-overlay 297.0x222.8 image linear-gradient(#000000 @ 0 62%, #000000 @ 0.004 63.94%, #000000 @ 0.016 65.89%, #000000 @ r 8px; a.btn2.btn2--secondary-alt 34.0x34.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 50%; a::before.btn2.btn2--secondary-alt 32pxx32px bg #ffffff; a::after.btn2.btn2--secondary-alt 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | = | div::after.js-thumbnail-base.shot-thumbnail-base 297pxx222.75px image linear-gradient(#000000 @ 0 0%, #000000 @ 0 8.1%, #000000 @ 0 15.5%, #000000 @ 0.004 22.5%; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 297.0x222.8 bg #e5e2c0; a.shot-thumbnail-link.dribbble-link 297.0x222.8 outline 2px solid #f3afe4 offset 1px; div.shot-thumbnail-overlay 297.0x222.8 image linear-gradient(#000000 @ 0 62%, #000000 @ 0.004 63.94%, #000000 @ 0.016 65.89%, #000000 @ r 8px; a.btn2.btn2--secondary-alt 34.0x34.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 50%; a::before.btn2.btn2--secondary-alt 32pxx32px bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `shot-card-default.png`, `shot-card-hover.png`, `shot-card-focus-visible.png`, `shot-card-pressed.png`.

#### shot-title

Shot card link. The card's shot link (the image anchor carrying the title).

Page: shots. Selector: `shot card link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 297 x 222.75 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | #3d3d4e | = | #3d3d4e |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.shot-thumbnail-link.dribbble-link 297.0x222.8 outline 2px solid #f3afe4 offset 1px | = |

Crops: `shot-title-default.png`, `shot-title-hover.png`, `shot-title-focus-visible.png`, `shot-title-pressed.png`.

#### pro-badge

PRO badge. The small PRO/PRO+ membership chip on the card.

Page: shots. Selector: `PRO badge`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 20 | = | = | = |
| Padding | 0px 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ecebf0 | #d8d6d5 | = | #d8d6d5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 9px/20px 800 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #524b63 | = | = | = |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pro-badge.pro-badge--light 40.0x20.0 bg #ecebf0 r 4px | a.pro-badge.pro-badge--light 40.0x20.0 bg #d8d6d5 r 4px | a.pro-badge.pro-badge--light 40.0x20.0 bg #ecebf0 r 4px outline 2px solid #f3afe4 offset 1px | a.pro-badge.pro-badge--light 40.0x20.0 bg #d8d6d5 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pro-badge-default.png`, `pro-badge-hover.png`, `pro-badge-focus-visible.png`, `pro-badge-pressed.png`.

#### stat-count

Like/view count. A heart/eye count on the shot card.

Page: shots. Selector: `shot stat count`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 12.11 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 12px/16px 500 |
| Letter spacing | normal |
| Colour | #3d3d4e |
| Transition | none |
| How | at rest |

Crops: `stat-count-default.png`.

#### wall-cta

Sign-up wall. The "Sign up to continue" pill that ends the signed-out feed; measured never followed — the signed-in feed is the boundary.

Page: shots. Selector: `"Sign up to continue"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 159 x 40 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 1e+07px | = | = | = |
| Background | #0d0c22 | #565564 | #565564 | #565564 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #6e6d7a offset 1px | = |
| Font | Mona Sans 13px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.form-sub.sign-up-to-continue 159.0x40.0 bg #0d0c22 r 1e+07px | a.form-sub.sign-up-to-continue 159.0x40.0 bg #565564 r 1e+07px | a.form-sub.sign-up-to-continue 159.0x40.0 bg #565564 r 1e+07px outline 1px solid #6e6d7a offset 1px | a.form-sub.sign-up-to-continue 159.0x40.0 bg #565564 r 1e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `wall-cta-default.png`, `wall-cta-hover.png`, `wall-cta-focus-visible.png`, `wall-cta-pressed.png`.

#### category-tile

Category tile. A browse-category tile (Branding, Illustration…) under the wall.

Page: shots. Selector: `category tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.44 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 1e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | #6e6d7a | = | #6e6d7a |
| Transition | color 0.1s ease | all 0.2s ease | = | all 0.2s ease |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 101.4x36.0 r 1e+07px outline 2px solid #f3afe4 offset 1px | = |

Crops: `category-tile-default.png`, `category-tile-hover.png`, `category-tile-focus-visible.png`, `category-tile-pressed.png`.

### Shot detail

#### shot-detail-title

Shot title. The shot page headline.

Page: shot. Selector: `h1 on the shot page`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 29 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 24px/29px 600 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `shot-detail-title-default.png`.

#### shot-author

Shot author. The designer attribution row (avatar, name, Follow).

Page: shot. Selector: `shot author block`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | #3d3d4e | = | #3d3d4e |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.user-sticky-header__avatar.hoverable 48.0x48.0 outline 2px solid #f3afe4 offset 1px | = |

Crops: `shot-author-default.png`, `shot-author-hover.png`, `shot-author-focus-visible.png`, `shot-author-pressed.png`.

#### shot-follow

Follow button. The Follow action under the author; measured never pressed.

Page: shot. Selector: `"Follow"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32.39 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #6e6d7a offset 1px | = |
| Font | Mona Sans 11px/11px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6d7a | #0d0c22 | = | #0d0c22 |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.form-btn.follow 32.4x14.0 r 8px outline 1px solid #6e6d7a offset 1px | = |

Crops: `shot-follow-default.png`, `shot-follow-hover.png`, `shot-follow-focus-visible.png`, `shot-follow-pressed.png`.

#### shot-cta

Get-in-touch button. The dark hire pill on the shot page; measured never followed.

Page: shot. Selector: `"Get in touch"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.88 x 40 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #0d0c22 | 1px solid #3d3d4e | 1px solid #3d3d4e | 1px solid #3d3d4e |
| Radius | 1e+07px | = | = | = |
| Background | #0d0c22 | #3d3d4e | #3d3d4e | #3d3d4e |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 13px/13px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Mona Sans 13px/13px 600, #ffffff | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 115.875px x 38px, absolute, bg #0d0c22, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | a.btn2.user-sticky-header__msg-button 117.9x40.0 bg #0d0c22 border T:1px solid #0d0c22 / R:1px solid #0d0c22 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 1e+07px; a::before.btn2.user-sticky-header__msg-button 115.875pxx38px bg #0d0c22; a::after.btn2.user-sticky-header__msg-button 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2.user-sticky-header__msg-button 117.9x40.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.btn2.user-sticky-header__msg-button 115.875pxx38px bg #0d0c22; a::after.btn2.user-sticky-header__msg-button 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2.user-sticky-header__msg-button 117.9x40.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px outline 2px solid #f3afe4 offset 1px; a::before.btn2.user-sticky-header__msg-button 115.875pxx38px bg #0d0c22; a::after.btn2.user-sticky-header__msg-button 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2.user-sticky-header__msg-button 117.9x40.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.btn2.user-sticky-header__msg-button 115.875pxx38px bg #0d0c22; a::after.btn2.user-sticky-header__msg-button 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `shot-cta-default.png`, `shot-cta-hover.png`, `shot-cta-focus-visible.png`, `shot-cta-pressed.png`.

#### shot-icon-btn

Like/save icon button. A heart/bookmark round button beside the CTA; measured never pressed.

Page: shot. Selector: `like or save icon button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e7e7e9 | 1px solid #dbdbde | 1px solid #dbdbde | 1px solid #dbdbde |
| Radius | 50% | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 0px | = |
| Font | Mona Sans 13px/13px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0d0c22 | = | = | = |
| ::before | 38px x 38px, absolute, bg #ffffff, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50% outline 2px solid #f3afe4 offset 0px; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `shot-icon-btn-default.png`, `shot-icon-btn-hover.png`, `shot-icon-btn-focus-visible.png`, `shot-icon-btn-pressed.png`.

#### shot-media

Shot media. The big shot image frame (largest image in main).

Page: shot. Selector: `largest main img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1023.98 x 1281.03 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 14px/28px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `shot-media-default.png`.

#### rail-btn

Action rail button. A button on the right-hand action rail (like/share/info).

Page: shot. Selector: `right rail button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e7e7e9 | 1px solid #dbdbde | 1px solid #dbdbde | 1px solid #dbdbde |
| Radius | 50% | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 0px | = |
| Font | Mona Sans 13px/13px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | span.count-indicator: Mona Sans 11px/18px 600, #6e6d7a | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0d0c22 | = | = | = |
| ::before | 38px x 38px, absolute, bg #ffffff, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50%; span.count-indicator 20.0x20.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50% shadow #000000 @ 0.03 0px 2px 6px 0px | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50%; span.count-indicator 20.0x20.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50% shadow #000000 @ 0.03 0px 2px 6px 0px | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50% outline 2px solid #f3afe4 offset 0px; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50%; span.count-indicator 20.0x20.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50% shadow #000000 @ 0.03 0px 2px 6px 0px | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50%; span.count-indicator 20.0x20.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50% shadow #000000 @ 0.03 0px 2px 6px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `rail-btn-default.png`, `rail-btn-hover.png`, `rail-btn-focus-visible.png`, `rail-btn-pressed.png`.

### Designer profile

#### profile-avatar

Profile avatar. The designer's round avatar.

Page: designer. Selector: `profile avatar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 80 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 50% |
| Background | #fdfcfb |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `profile-avatar-default.png`.

#### profile-name

Profile name. The designer/agency display name heading.

Page: designer. Selector: `profile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 305.3 x 38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 32px/38px 700 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `profile-name-default.png`.

#### profile-headline

Profile headline. The designer's tagline block (masthead-intro h2) under the name.

Page: designer. Selector: `.masthead-intro h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 168 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 48px/56px 700 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `profile-headline-default.png`.

#### profile-stat

Profile stat. A followers/following/likes stat (.masthead-stats .stat) under the headline.

Page: designer. Selector: `.masthead-stats .stat`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 93.56 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #6e6d7a |
| Transition | none |
| How | at rest |

Crops: `profile-stat-default.png`.

#### profile-cta

Get-in-touch button. The dark hire pill on the profile; measured never followed.

Page: designer. Selector: `"Get in touch"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 131.72 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #0d0c22 | 1px solid #3d3d4e | 1px solid #3d3d4e | 1px solid #3d3d4e |
| Radius | 1e+07px | = | = | = |
| Background | #0d0c22 | #3d3d4e | #3d3d4e | #3d3d4e |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/14px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Mona Sans 14px/14px 600, #ffffff | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 129.719px x 46px, absolute, bg #0d0c22, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | a.btn2 131.7x48.0 bg #0d0c22 border T:1px solid #0d0c22 / R:1px solid #0d0c22 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 1e+07px; a::before.btn2 129.719pxx46px bg #0d0c22; a::after.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2 131.7x48.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.btn2 129.719pxx46px bg #0d0c22; a::after.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2 131.7x48.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px outline 2px solid #f3afe4 offset 1px; a::before.btn2 129.719pxx46px bg #0d0c22; a::after.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2 131.7x48.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.btn2 129.719pxx46px bg #0d0c22; a::after.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `profile-cta-default.png`, `profile-cta-hover.png`, `profile-cta-focus-visible.png`, `profile-cta-pressed.png`.

#### profile-follow

Follow button. The white Follow pill; measured never pressed.

Page: designer. Selector: `"Follow"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.14 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e7e7e9 | 1px solid #dbdbde | 1px solid #dbdbde | 1px solid #dbdbde |
| Radius | 1e+07px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/14px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | span: Mona Sans 14px/14px 600, #0d0c22 | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 91.1406px x 46px, absolute, bg #ffffff, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | a.btn2.btn2--tertiary 93.1x48.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; a::before.btn2.btn2--tertiary 91.1406pxx46px bg #ffffff; a::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | a.btn2.btn2--tertiary 93.1x48.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 1e+07px; a::before.btn2.btn2--tertiary 91.1406pxx46px bg #ffffff; a::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | a.btn2.btn2--tertiary 93.1x48.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 1e+07px outline 2px solid #f3afe4 offset 1px; a::before.btn2.btn2--tertiary 91.1406pxx46px bg #ffffff; a::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | a.btn2.btn2--tertiary 93.1x48.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 1e+07px; a::before.btn2.btn2--tertiary 91.1406pxx46px bg #ffffff; a::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `profile-follow-default.png`, `profile-follow-hover.png`, `profile-follow-focus-visible.png`, `profile-follow-pressed.png`.

#### profile-icon-btn

Icon button. The icon-only action beside Follow (save/message); measured never pressed.

Page: designer. Selector: `profile icon button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e7e7e9 | 1px solid #dbdbde | 1px solid #dbdbde | 1px solid #dbdbde |
| Radius | 50% | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 0px | = |
| Font | Mona Sans 14px/14px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0d0c22 | = | = | = |
| ::before | 46px x 46px, absolute, bg #ffffff, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | button.btn2.btn2--tertiary 48.0x48.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50%; button::before.btn2.btn2--tertiary 46pxx46px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 48.0x48.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50%; button::before.btn2.btn2--tertiary 46pxx46px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 48.0x48.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50% outline 2px solid #f3afe4 offset 0px; button::before.btn2.btn2--tertiary 46pxx46px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 48.0x48.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50%; button::before.btn2.btn2--tertiary 46pxx46px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `profile-icon-btn-default.png`, `profile-icon-btn-hover.png`, `profile-icon-btn-focus-visible.png`, `profile-icon-btn-pressed.png`.

#### profile-tab

Profile tab. A tab in the Work/Services/Reviews/Collections bar.

Page: designer. Selector: `profile tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67.45 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 1e+07px | = | = | = |
| Background | #f8f7f4 | #f5f3f0 | = | #f5f3f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/15px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | span.label: Mona Sans 14px/15px 600, #0d0c22 | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 67.5x36.0 bg #f8f7f4 r 1e+07px | a 67.5x36.0 bg #f5f3f0 r 1e+07px | a 67.5x36.0 bg #f8f7f4 r 1e+07px outline 2px solid #f3afe4 offset 1px | a 67.5x36.0 bg #f5f3f0 r 1e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `profile-tab-default.png`, `profile-tab-hover.png`, `profile-tab-focus-visible.png`, `profile-tab-pressed.png`.

#### profile-sort

Work sort control. The "Recent Shots" dropdown over the work grid; its list was never opened.

Page: designer. Selector: `"Recent Shots" control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 143.22 x 40 | = | = | = |
| Padding | 18px 35px 18px 18px | = | = | = |
| Border | 1px solid #e7e7e9 @ 0.9 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.01 0px 2px 2px 0px | #000000 @ 0.03 0px 4px 4px 0px | = | #000000 @ 0.03 0px 4px 4px 0px |
| Outline | none | = | 1px solid #6e6d7a offset 1px | = |
| Font | Mona Sans 14px/19px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | span.js-current-filter: Mona Sans 14px/19px 500, #0d0c22 | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #0d0c22, fill #3d3d4e | = | = | = |
| Painted layers | a.form-btn.outlined 143.2x40.0 bg #ffffff border T:1px solid #e7e7e9 @ 0.9 / R:1px solid #e7e7e9 @ 0.9 / B:1px solid #e7e7e9 @ 0.9 / L:1px solid #e7e7e9 @ 0.9 r 8px shadow #000000 @ 0.01 0px 2px 2px 0px | a.form-btn.outlined 143.2x40.0 bg #ffffff border T:1px solid #e7e7e9 @ 0.9 / R:1px solid #e7e7e9 @ 0.9 / B:1px solid #e7e7e9 @ 0.9 / L:1px solid #e7e7e9 @ 0.9 r 8px shadow #000000 @ 0.03 0px 4px 4px 0px | a.form-btn.outlined 143.2x40.0 bg #ffffff border T:1px solid #e7e7e9 @ 0.9 / R:1px solid #e7e7e9 @ 0.9 / B:1px solid #e7e7e9 @ 0.9 / L:1px solid #e7e7e9 @ 0.9 r 8px shadow #000000 @ 0.01 0px 2px 2px 0px outline 1px solid #6e6d7a offset 1px | a.form-btn.outlined 143.2x40.0 bg #ffffff border T:1px solid #e7e7e9 @ 0.9 / R:1px solid #e7e7e9 @ 0.9 / B:1px solid #e7e7e9 @ 0.9 / L:1px solid #e7e7e9 @ 0.9 r 8px shadow #000000 @ 0.03 0px 4px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `profile-sort-default.png`, `profile-sort-hover.png`, `profile-sort-focus-visible.png`, `profile-sort-pressed.png`.

#### profile-shot-card

Work grid card. A shot card in the designer's work grid.

Page: designer. Selector: `work grid card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 300 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Mona Sans 14px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | div.shot-title: Mona Sans 14px/20px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Icon | 11 x 9, colour #ffffff | = | = | = |
| Painted layers | div::after.js-thumbnail-base.shot-thumbnail-base 400pxx300px image linear-gradient(#000000 @ 0 0%, #000000 @ 0 8.1%, #000000 @ 0 15.5%, #000000 @ 0.004 22.5%; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 400.0x300.0 bg #f2f1f2; div.is-motion.shot-thumbnail-extras-icon 21.0x21.0 bg #000000 @ 0.2 r 50%; div.shot-thumbnail-overlay 400.0x300.0 image linear-gradient(#000000 @ 0 62%, #000000 @ 0.004 63.94%, #000000 @ 0.016 65.89%, #000000 @ r 8px; a.btn2.btn2--secondary-alt 34.0x34.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 50%; a::before.btn2.btn2--secondary-alt 32pxx32px bg #ffffff | = | div::after.js-thumbnail-base.shot-thumbnail-base 400pxx300px image linear-gradient(#000000 @ 0 0%, #000000 @ 0 8.1%, #000000 @ 0 15.5%, #000000 @ 0.004 22.5%; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 400.0x300.0 bg #f2f1f2; div.is-motion.shot-thumbnail-extras-icon 21.0x21.0 bg #000000 @ 0.2 r 50%; a.animated-target 0.0x0.0 outline 2px solid #f3afe4 offset 1px; div.shot-thumbnail-overlay 400.0x300.0 image linear-gradient(#000000 @ 0 62%, #000000 @ 0.004 63.94%, #000000 @ 0.016 65.89%, #000000 @ r 8px; a.btn2.btn2--secondary-alt 34.0x34.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `profile-shot-card-default.png`, `profile-shot-card-hover.png`, `profile-shot-card-focus-visible.png`, `profile-shot-card-pressed.png`.

### Designers directory

#### dir-h1

Directory title. The "Hire Top Freelance Designers" heading.

Page: designers. Selector: `h1 on /designers`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1296 x 29 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 24px/29px 700 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `dir-h1-default.png`.

#### topic-chip

Topic chip. A Popular topic link under the directory heading.

Page: designers. Selector: `popular topic a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.16 x 31 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #e7e7e9 | = | = | = |
| Radius | 1e+07px | = | = | = |
| Background | #ffffff | #faf9fb | = | #faf9fb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 12px/12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pill2.pill2--white-dark 96.2x31.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px | a.pill2.pill2--white-dark 96.2x31.0 bg #faf9fb border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px | a.pill2.pill2--white-dark 96.2x31.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px outline 2px solid #f3afe4 offset 1px | a.pill2.pill2--white-dark 96.2x31.0 bg #faf9fb border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topic-chip-default.png`, `topic-chip-hover.png`, `topic-chip-focus-visible.png`, `topic-chip-pressed.png`.

#### filter-select

Filter control. A filter dropdown over the directory (Categories/Budget/Location/Rating/More); its list was never opened.

Page: designers. Selector: `filter dropdown`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115.89 x 35 | = | = | = |
| Padding | 0px 34px 0px 14px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #dbdade @ 0.9 | 1px solid #9e9ea7 @ 0.7 | 1px solid #9e9ea7 @ 0.7 | 1px solid #9e9ea7 @ 0.7 |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #060318 @ 0.01 0px 4px 4px 0px | #060318 @ 0.03 0px 4px 4px 0px | #060318 @ 0.03 0px 4px 4px 0px | #060318 @ 0.03 0px 4px 4px 0px |
| Outline | none | = | = | = |
| Font | Mona Sans 12px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color, box-shadow, border, background-color, -webkit-box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0 url(…), radius 0px | = | = | = |
| Painted layers | button.dropdown2 115.9x35.0 bg #ffffff border T:1px solid #dbdade @ 0.9 / R:1px solid #dbdade @ 0.9 / B:1px solid #dbdade @ 0.9 / L:1px solid #dbdade @ 0.9 r 8px shadow #060318 @ 0.01 0px 4px 4px 0px | button.dropdown2 115.9x35.0 bg #ffffff border T:1px solid #9e9ea7 @ 0.7 / R:1px solid #9e9ea7 @ 0.7 / B:1px solid #9e9ea7 @ 0.7 / L:1px solid #9e9ea7 @ 0.7 r 8px shadow #060318 @ 0.03 0px 4px 4px 0px | button.dropdown2 115.9x35.0 bg #ffffff border T:1px solid #9e9ea7 @ 0.7 / R:1px solid #9e9ea7 @ 0.7 / B:1px solid #9e9ea7 @ 0.7 / L:1px solid #9e9ea7 @ 0.7 r 8px shadow #060318 @ 0.03 0px 4px 4px 0px | button.dropdown2 115.9x35.0 bg #ffffff border T:1px solid #9e9ea7 @ 0.7 / R:1px solid #9e9ea7 @ 0.7 / B:1px solid #9e9ea7 @ 0.7 / L:1px solid #9e9ea7 @ 0.7 r 8px shadow #060318 @ 0.03 0px 4px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-select-default.png`, `filter-select-hover.png`, `filter-select-focus-visible.png`, `filter-select-pressed.png`.

#### designer-card

Designer card. A freelancer card (resume-user-card): avatar, name, PRO+/SELECT badges, star rating, projects count, rate, location, response time, work strip and skill chips.

Page: designers. Selector: `.resume-user-card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1296 x 416.13 | = | = | = |
| Padding | 28px | = | = | = |
| Gap | 24px | = | = | = |
| Border | 1px solid #f3f3f4 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #121619 @ 0.02 0px 1px 10px 0px | #000000 @ 0.1 0px 8px 25px 0px | = | #000000 @ 0.1 0px 8px 25px 0px |
| Outline | none | = | = | = |
| Font | Mona Sans 14px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | span.user-card-profile__heading-name: Mona Sans 18px/28px 600, #0d0c22 | = | = | = |
| Transition | box-shadow, -webkit-box-shadow 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 11 x 11, colour #0d0c22 | = | = | = |
| Painted layers | div.resume-user-card.card 1296.0x416.1 bg #ffffff border T:1px solid #f3f3f4 / R:1px solid #f3f3f4 / B:1px solid #f3f3f4 / L:1px solid #f3f3f4 r 8px shadow #121619 @ 0.02 0px 1px 10px 0px; a.pro-badge.pro-badge--dark 40.0x20.0 bg #3a3546 r 4px; span.pro-badge.pro-badge--select 47.5x20.0 image linear-gradient(172deg, #4a6071 14.52%, #000000 108.51%) r 4px; button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | div.resume-user-card.card 1296.0x416.1 bg #ffffff border T:1px solid #f3f3f4 / R:1px solid #f3f3f4 / B:1px solid #f3f3f4 / L:1px solid #f3f3f4 r 8px shadow #000000 @ 0.1 0px 8px 25px 0px; a.pro-badge.pro-badge--dark 40.0x20.0 bg #3a3546 r 4px; span.pro-badge.pro-badge--select 47.5x20.0 image linear-gradient(172deg, #4a6071 14.52%, #000000 108.51%) r 4px; button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | div.resume-user-card.card 1296.0x416.1 bg #ffffff border T:1px solid #f3f3f4 / R:1px solid #f3f3f4 / B:1px solid #f3f3f4 / L:1px solid #f3f3f4 r 8px shadow #121619 @ 0.02 0px 1px 10px 0px; a.pro-badge.pro-badge--dark 40.0x20.0 bg #3a3546 r 4px outline 2px solid #f3afe4 offset 1px; span.pro-badge.pro-badge--select 47.5x20.0 image linear-gradient(172deg, #4a6071 14.52%, #000000 108.51%) r 4px; button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | div.resume-user-card.card 1296.0x416.1 bg #ffffff border T:1px solid #f3f3f4 / R:1px solid #f3f3f4 / B:1px solid #f3f3f4 / L:1px solid #f3f3f4 r 8px shadow #000000 @ 0.1 0px 8px 25px 0px; a.pro-badge.pro-badge--dark 40.0x20.0 bg #3a3546 r 4px; span.pro-badge.pro-badge--select 47.5x20.0 image linear-gradient(172deg, #4a6071 14.52%, #000000 108.51%) r 4px; button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `designer-card-default.png`, `designer-card-hover.png`, `designer-card-focus-visible.png`, `designer-card-pressed.png`.

#### designer-name

Designer name. The freelancer's display name on the card.

Page: designers. Selector: `designer card name`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 153.55 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3a3546 | #3d3d4e | = | #3d3d4e |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17 x 17, colour #3a3546 | 17 x 17, colour #3d3d4e | = | 17 x 17, colour #3d3d4e |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.user-card-profile__subheading-item.user-card-profile__subheading-link 153.5x28.0 outline 2px solid #f3afe4 offset 1px | = |

Crops: `designer-name-default.png`, `designer-name-hover.png`, `designer-name-focus-visible.png`, `designer-name-pressed.png`.

#### badge-select

SELECT badge. The SELECT/PRO+ membership chip on the card.

Page: designers. Selector: `SELECT badge`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 20 | = | = | = |
| Padding | 0px 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ecebf0 | #d8d6d5 | = | #d8d6d5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 9px/20px 800 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #524b63 | = | = | = |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pro-badge.pro-badge--light 40.0x20.0 bg #ecebf0 r 4px | a.pro-badge.pro-badge--light 40.0x20.0 bg #d8d6d5 r 4px | a.pro-badge.pro-badge--light 40.0x20.0 bg #ecebf0 r 4px outline 2px solid #f3afe4 offset 1px | a.pro-badge.pro-badge--light 40.0x20.0 bg #d8d6d5 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `badge-select-default.png`, `badge-select-hover.png`, `badge-select-focus-visible.png`, `badge-select-pressed.png`.

#### rating

Star rating. The 4.9 (158) star-rating figure.

Page: designers. Selector: `star rating`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 71.45 x 28 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 14px/28px 600 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Text node | span.designer-ratings-score__ratings-count: Mona Sans 14px/28px 600, #0d0c22 |
| Transition | none |
| Cursor | pointer |
| Icon | 11 x 11, colour #0d0c22 |
| How | at rest |

Crops: `rating-default.png`.

#### designer-meta

Designer meta. A projects-completed / response-time / services meta item.

Page: designers. Selector: `designer meta`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 157.59 x 28 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 14px/28px 500 |
| Letter spacing | normal |
| Colour | #3a3546 |
| Transition | none |
| Cursor | pointer |
| Icon | 17 x 17, colour #3a3546 |
| How | at rest |

Crops: `designer-meta-default.png`.

#### promoted-tag

Promoted tag. The small "Promoted" disclosure label.

Page: designers. Selector: `"Promoted"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 57.91 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 12px/28px 700 |
| Letter spacing | normal |
| Colour | #98959f |
| Transition | color 0.1s ease-in-out |
| Cursor | pointer |
| How | at rest |

Crops: `promoted-tag-default.png`.

#### designer-cta

Get-in-touch button. The dark hire pill on the card; measured never followed.

Page: designers. Selector: `"Get in touch"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.88 x 40 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #0d0c22 | 1px solid #3d3d4e | 1px solid #3d3d4e | 1px solid #3d3d4e |
| Radius | 1e+07px | = | = | = |
| Background | #0d0c22 | #3d3d4e | #3d3d4e | #3d3d4e |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 13px/13px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Mona Sans 13px/13px 600, #ffffff | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 115.875px x 38px, absolute, bg #0d0c22, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | a.btn2 117.9x40.0 bg #0d0c22 border T:1px solid #0d0c22 / R:1px solid #0d0c22 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 1e+07px; a::before.btn2 115.875pxx38px bg #0d0c22; a::after.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2 117.9x40.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.btn2 115.875pxx38px bg #0d0c22; a::after.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2 117.9x40.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px outline 2px solid #f3afe4 offset 1px; a::before.btn2 115.875pxx38px bg #0d0c22; a::after.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | a.btn2 117.9x40.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; a::before.btn2 115.875pxx38px bg #0d0c22; a::after.btn2 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% |
| Ancestor paint | 3 up div.resume-user-card.card bg #ffffff shadow #121619 @ 0.02 0px 1px 10px 0px | 3 up div.resume-user-card.card bg #ffffff shadow #000000 @ 0.1 0px 8px 25px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `designer-cta-default.png`, `designer-cta-hover.png`, `designer-cta-focus-visible.png`, `designer-cta-pressed.png`.

#### bookmark-btn

Bookmark icon button. The icon-only save/bookmark button on the card; measured never pressed.

Page: designers. Selector: `.resume-user-card icon-only control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #e7e7e9 | 1px solid #dbdbde | 1px solid #dbdbde | 1px solid #dbdbde |
| Radius | 50% | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 0px | = |
| Font | Mona Sans 13px/13px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0d0c22 | = | = | = |
| ::before | 38px x 38px, absolute, bg #ffffff, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50% outline 2px solid #f3afe4 offset 0px; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 40.0x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 50%; button::before.btn2.btn2--tertiary 38pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bookmark-btn-default.png`, `bookmark-btn-hover.png`, `bookmark-btn-focus-visible.png`, `bookmark-btn-pressed.png`.

#### skill-chip-dark

Skill chip, dark. The dark certified chip ("Webflow Expert").

Page: designers. Selector: `dark skill chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136.42 x 27 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #3a3546 | = | = | = |
| Radius | 1e+07px | = | = | = |
| Background | #3a3546 | #655c7a | = | #655c7a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 11px/14px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Mona Sans 11px/14px 700, #ffffff | = | = | = |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #ffffff | = | = | = |
| Painted layers | a.pill2.pill2--grey-950 136.4x27.0 bg #3a3546 border T:1px solid #3a3546 / R:1px solid #3a3546 / B:1px solid #3a3546 / L:1px solid #3a3546 r 1e+07px | a.pill2.pill2--grey-950 136.4x27.0 bg #655c7a border T:1px solid #3a3546 / R:1px solid #3a3546 / B:1px solid #3a3546 / L:1px solid #3a3546 r 1e+07px | a.pill2.pill2--grey-950 136.4x27.0 bg #3a3546 border T:1px solid #3a3546 / R:1px solid #3a3546 / B:1px solid #3a3546 / L:1px solid #3a3546 r 1e+07px outline 2px solid #f3afe4 offset 1px | a.pill2.pill2--grey-950 136.4x27.0 bg #655c7a border T:1px solid #3a3546 / R:1px solid #3a3546 / B:1px solid #3a3546 / L:1px solid #3a3546 r 1e+07px |
| Ancestor paint | 2 up div.resume-user-card.card bg #ffffff shadow #121619 @ 0.02 0px 1px 10px 0px | 2 up div.resume-user-card.card bg #ffffff shadow #000000 @ 0.1 0px 8px 25px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `skill-chip-dark-default.png`, `skill-chip-dark-hover.png`, `skill-chip-dark-focus-visible.png`, `skill-chip-dark-pressed.png`.

#### skill-chip

Skill chip. A light skill tag on the card.

Page: designers. Selector: `skill chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95.78 x 31 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #e7e7e9 | = | = | = |
| Radius | 1e+07px | = | = | = |
| Background | #ffffff | #faf9fb | = | #faf9fb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 12px/12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pill2.pill2--white-dark 95.8x31.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px | a.pill2.pill2--white-dark 95.8x31.0 bg #faf9fb border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px | a.pill2.pill2--white-dark 95.8x31.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px outline 2px solid #f3afe4 offset 1px | a.pill2.pill2--white-dark 95.8x31.0 bg #faf9fb border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `skill-chip-default.png`, `skill-chip-hover.png`, `skill-chip-focus-visible.png`, `skill-chip-pressed.png`.

### Jobs board

#### jobs-h1

Jobs title. The jobs-board heading.

Page: jobs. Selector: `h1 on /jobs`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 732 x 152 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Source Serif Pro 72px/76px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `jobs-h1-default.png`.

#### job-card

Job card. A posting card: logo, role, company, location/type tags.

Page: jobs. Selector: `job card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 912 x 104 | = | - | = |
| Padding | 24px | = | - | = |
| Border | 1px solid #f1f1f1 | = | - | = |
| Radius | 8px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | none | #f3f3f4 @ 0.65 0px 8px 15px 0px | - | #f3f3f4 @ 0.65 0px 8px 15px 0px |
| Outline | none | = | - | = |
| Font | Mona Sans 14px/28px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #0d0c22 | = | - | = |
| Text node | span.job-board-job-company: Mona Sans 15px/15px 500, #0d0c22 | = | - | = |
| Transition | background-color 0.2s ease | = | - | = |
| Icon | 14 x 22, colour #0d0c22 | = | - | = |
| Painted layers | li.job-list-item 912.0x104.0 bg #ffffff border T:1px solid #f1f1f1 / R:1px solid #f1f1f1 / B:1px solid #f1f1f1 / L:1px solid #f1f1f1 r 8px; a.form-btn.outlined 93.5x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; button.btn2.btn2--tertiary 105.8x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; button::before.btn2.btn2--tertiary 103.812pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | li.job-list-item 912.0x104.0 bg #ffffff border T:1px solid #f1f1f1 / R:1px solid #f1f1f1 / B:1px solid #f1f1f1 / L:1px solid #f1f1f1 r 8px shadow #f3f3f4 @ 0.65 0px 8px 15px 0px; a.form-btn.outlined 93.5x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; button.btn2.btn2--tertiary 105.8x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; button::before.btn2.btn2--tertiary 103.812pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | - | li.job-list-item 912.0x104.0 bg #ffffff border T:1px solid #f1f1f1 / R:1px solid #f1f1f1 / B:1px solid #f1f1f1 / L:1px solid #f1f1f1 r 8px shadow #f3f3f4 @ 0.65 0px 8px 15px 0px; a.form-btn.outlined 93.5x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; button.btn2.btn2--tertiary 105.8x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; button::before.btn2.btn2--tertiary 103.812pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `job-card-default.png`, `job-card-hover.png`, `job-card-pressed.png`.

#### job-title

Job title. A role title on a posting (h4.job-board-job-title inside li.job-list-item).

Page: jobs. Selector: `job title inside a job card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 250.09 x 36 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Mona Sans 22px/36px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #0d0c22 | = | - | = |
| Transition | none | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `job-title-default.png`, `job-title-hover.png`, `job-title-pressed.png`.

#### job-tag

Job tag. A remote/contract/location tag on the posting (span.location inside li.job-list-item).

Page: jobs. Selector: `job tag inside a job card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67.78 x 28 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Mona Sans 14px/28px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #3d3d4e | = | - | = |
| Text node | span.location: Mona Sans 12px/28px 700, #3d3d4e | = | - | = |
| Transition | none | = | - | = |
| Icon | 14 x 22, colour #0d0c22 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `job-tag-default.png`, `job-tag-hover.png`, `job-tag-pressed.png`.

#### job-apply

Apply button. The apply action; measured never followed.

Page: jobs. Selector: `"Apply"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.81 x 40 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e7e7e9 | 1px solid #dbdbde | 1px solid #dbdbde | 1px solid #dbdbde |
| Radius | 1e+07px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 0px | = |
| Font | Mona Sans 13px/13px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 103.812px x 38px, absolute, bg #ffffff, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | button.btn2.btn2--tertiary 105.8x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; button::before.btn2.btn2--tertiary 103.812pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 105.8x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 1e+07px; button::before.btn2.btn2--tertiary 103.812pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 105.8x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 1e+07px outline 2px solid #f3afe4 offset 0px; button::before.btn2.btn2--tertiary 103.812pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | button.btn2.btn2--tertiary 105.8x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 1e+07px; button::before.btn2.btn2--tertiary 103.812pxx38px bg #ffffff; button::after.btn2.btn2--tertiary 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 3 up li.job-list-item bg #ffffff shadow #f3f3f4 @ 0.65 0px 8px 15px 0px | = | = |

Crops: `job-apply-default.png`, `job-apply-hover.png`, `job-apply-focus-visible.png`, `job-apply-pressed.png`.

### Search

#### search-h1

Search title. The query heading ("Logo").

Page: search. Selector: `h1 on /search`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1408 x 38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 32px/38px 700 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `search-h1-default.png`.

#### search-desc

Search description. The dictionary-style definition line under the query.

Page: search. Selector: `search definition`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 732 x 56 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #655c7a |
| Transition | none |
| How | at rest |

Crops: `search-desc-default.png`.

#### related-link

Related link. A Related: tag link under the definition.

Page: search. Selector: `related link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.52 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | #3d3d4e | = | #3d3d4e |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 57.5x17.0 outline 2px solid #f3afe4 offset 1px | = |

Crops: `related-link-default.png`, `related-link-hover.png`, `related-link-focus-visible.png`, `related-link-pressed.png`.

#### filter-tab

Filter tab. A category tab over the results grid.

Page: search. Selector: `filter tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 1e+07px | = | = | = |
| Background | #f8f7f4 | #f5f3f0 | = | #f5f3f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color 0.1s ease | all 0.2s ease | = | all 0.2s ease |
| Cursor | pointer | = | = | = |
| Painted layers | a 90.0x36.0 bg #f8f7f4 r 1e+07px | a 90.0x36.0 bg #f5f3f0 r 1e+07px | a 90.0x36.0 bg #f8f7f4 r 1e+07px outline 2px solid #f3afe4 offset 1px | a 90.0x36.0 bg #f5f3f0 r 1e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-tab-default.png`, `filter-tab-hover.png`, `filter-tab-focus-visible.png`, `filter-tab-pressed.png`.

#### filter-sort

Sort control. The "Popular" sort dropdown; its list was never opened.

Page: search. Selector: `"Popular" control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115 x 40 | = | = | = |
| Padding | 18px 35px 18px 18px | = | = | = |
| Border | 1px solid #e7e7e9 @ 0.9 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.01 0px 2px 2px 0px | #000000 @ 0.03 0px 4px 4px 0px | = | #000000 @ 0.03 0px 4px 4px 0px |
| Outline | none | = | 1px solid #6e6d7a offset 1px | = |
| Font | Mona Sans 14px/19px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | span: Mona Sans 14px/19px 500, #0d0c22 | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #0d0c22, fill #3d3d4e | = | = | = |
| Painted layers | a.form-btn.outlined 115.0x40.0 bg #ffffff border T:1px solid #e7e7e9 @ 0.9 / R:1px solid #e7e7e9 @ 0.9 / B:1px solid #e7e7e9 @ 0.9 / L:1px solid #e7e7e9 @ 0.9 r 8px shadow #000000 @ 0.01 0px 2px 2px 0px | a.form-btn.outlined 115.0x40.0 bg #ffffff border T:1px solid #e7e7e9 @ 0.9 / R:1px solid #e7e7e9 @ 0.9 / B:1px solid #e7e7e9 @ 0.9 / L:1px solid #e7e7e9 @ 0.9 r 8px shadow #000000 @ 0.03 0px 4px 4px 0px | a.form-btn.outlined 115.0x40.0 bg #ffffff border T:1px solid #e7e7e9 @ 0.9 / R:1px solid #e7e7e9 @ 0.9 / B:1px solid #e7e7e9 @ 0.9 / L:1px solid #e7e7e9 @ 0.9 r 8px shadow #000000 @ 0.01 0px 2px 2px 0px outline 1px solid #6e6d7a offset 1px | a.form-btn.outlined 115.0x40.0 bg #ffffff border T:1px solid #e7e7e9 @ 0.9 / R:1px solid #e7e7e9 @ 0.9 / B:1px solid #e7e7e9 @ 0.9 / L:1px solid #e7e7e9 @ 0.9 r 8px shadow #000000 @ 0.03 0px 4px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-sort-default.png`, `filter-sort-hover.png`, `filter-sort-focus-visible.png`, `filter-sort-pressed.png`.

#### filters-btn

Filters button. The Filters toggle at the end of the tab row; measured, its panel was never opened.

Page: search. Selector: `"Filters" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 98.45 x 40 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Border | 1px solid #e7e7e9 | 1px solid #dbdbde | 1px solid #dbdbde | 1px solid #dbdbde |
| Radius | 1e+07px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #6e6d7a offset 1px | = |
| Font | Mona Sans 13px/16px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | span.label: Mona Sans 13px/16px 600, #0d0c22 | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13 x 13, colour #0d0c22 | = | = | = |
| Painted layers | a.form-btn.outlined 98.5x40.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px; span.meatball 0.0x0.0 bg #ea64d9 r 50% | a.form-btn.outlined 98.5x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 1e+07px; span.meatball 0.0x0.0 bg #ea64d9 r 50% | a.form-btn.outlined 98.5x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 1e+07px outline 1px solid #6e6d7a offset 1px; span.meatball 0.0x0.0 bg #ea64d9 r 50% | a.form-btn.outlined 98.5x40.0 bg #ffffff border T:1px solid #dbdbde / R:1px solid #dbdbde / B:1px solid #dbdbde / L:1px solid #dbdbde r 1e+07px; span.meatball 0.0x0.0 bg #ea64d9 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filters-btn-default.png`, `filters-btn-hover.png`, `filters-btn-focus-visible.png`, `filters-btn-pressed.png`.

#### grid-shot-card

Grid shot card. A shot card in the results grid: image, avatar + name, PRO+ chip, like and view counts.

Page: search. Selector: `results shot card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 297 x 254.75 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Mona Sans 14px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Text node | div.shot-title: Mona Sans 14px/20px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Icon | 16 x 16, colour #0d0c22 | = | = | = |
| Painted layers | div::after.js-thumbnail-base.shot-thumbnail-base 297pxx222.75px image linear-gradient(#000000 @ 0 0%, #000000 @ 0 8.1%, #000000 @ 0 15.5%, #000000 @ 0.004 22.5%; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 297.0x222.8 bg #ffffff; div.shot-thumbnail-overlay 297.0x222.8 image linear-gradient(#000000 @ 0 62%, #000000 @ 0.004 63.94%, #000000 @ 0.016 65.89%, #000000 @ r 8px; a.btn2.btn2--secondary-alt 34.0x34.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 50%; a::before.btn2.btn2--secondary-alt 32pxx32px bg #ffffff; a::after.btn2.btn2--secondary-alt 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 50% | = | div::after.js-thumbnail-base.shot-thumbnail-base 297pxx222.75px image linear-gradient(#000000 @ 0 0%, #000000 @ 0 8.1%, #000000 @ 0 15.5%, #000000 @ 0.004 22.5%; figure.js-thumbnail-placeholder.shot-thumbnail-placeholder 297.0x222.8 bg #ffffff; a.shot-thumbnail-link.dribbble-link 297.0x222.8 outline 2px solid #f3afe4 offset 1px; div.shot-thumbnail-overlay 297.0x222.8 image linear-gradient(#000000 @ 0 62%, #000000 @ 0.004 63.94%, #000000 @ 0.016 65.89%, #000000 @ r 8px; a.btn2.btn2--secondary-alt 34.0x34.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 50%; a::before.btn2.btn2--secondary-alt 32pxx32px bg #ffffff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `grid-shot-card-default.png`, `grid-shot-card-hover.png`, `grid-shot-card-focus-visible.png`, `grid-shot-card-pressed.png`.

### Stories (blog)

#### stories-h1

Stories title. The blog's heading or featured story title.

Page: stories. Selector: `h1/h2 on /stories`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 843.19 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 48px/56px 700 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `stories-h1-default.png`.

#### story-card

Story card. An article card in the blog index.

Page: stories. Selector: `story card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 808.61 x 86.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 36px/43.2px 500 | = | = | = |
| Letter spacing | -1.08px | = | = | = |
| Colour | #0d0c22 | #ea64d9 | = | #ea64d9 |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 808.6x86.2 outline 2px solid #f3afe4 offset 1px | = |

Crops: `story-card-default.png`, `story-card-hover.png`, `story-card-focus-visible.png`, `story-card-pressed.png`.

#### story-tag

Story tag. A category link on the stories index (ul.blog-cat: Interviews, Inspiration, Process, Community).

Page: stories. Selector: `ul.blog-cat a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 281.81 x 25 | = | = | = |
| Padding | 2px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | #3d3d4e | = | #3d3d4e |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 281.8x25.0 outline 2px solid #f3afe4 offset 1px | = |

Crops: `story-tag-default.png`, `story-tag-hover.png`, `story-tag-focus-visible.png`, `story-tag-pressed.png`.

### Log in and sign up

#### login-card

Login card. The "Welcome back" form card (auth-layout__content) on the split layout; never filled or submitted. The Continue-with-Google action is a Google-rendered GSI element — hidden as a third-party prompt like every other overlay, never answered, so it is documented as a gap rather than measured.

Page: login. Selector: `.auth-layout__content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 804 |
| Padding | 0px 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Text node | h1.auth-screen-header__heading: Mona Sans 24px/29px 700, #0d0c22 |
| Transition | none |
| Icon | 76 x 30, colour #0d0c22 |
| Painted layers | div 0.0x0.0 image linear-gradient(-90deg, #f3f3f4 8%, #faf9fb 28%, #f3f3f4 70%) r 1e+07px; div.nsm7Bb-HzV7m-LgbsSe.TzA9Ye-LgbsSe 0.0x0.0 bg #ffffff border T:1px solid #dadce0 / R:1px solid #dadce0 / B:1px solid #dadce0 / L:1px solid #dadce0 r 20px; input.input2.input2--large 0.0x0.0 bg #ffffff border T:1px solid #dbdade @ 0.9 / R:1px solid #dbdade @ 0.9 / B:1px solid #dbdade @ 0.9 / L:1px solid #dbdade @ 0.9 r 8px; button.btn2.btn2--medium 0.0x0.0 bg #0d0c22 border T:1px solid #0d0c22 / R:1px solid #0d0c22 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 1e+07px; button::before.btn2.btn2--medium 100%x100% bg #0d0c22; button::after.btn2.btn2--medium 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% |
| How | at rest |

Crops: `login-card-default.png`.

#### email-field

Email field. The "Enter email or username" input; sample text was typed and deleted, nothing sent.

Page: login. Selector: `auth email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 310 x 47 | = | = |
| Padding | 0px 16px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #dbdade @ 0.9 | 1px solid #9e9ea7 @ 0.7 | 1px solid #9e9ea7 @ 0.7 |
| Radius | 8px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #060318 @ 0.03 0px 4px 4px 0px | #060318 @ 0.03 0px 4px 4px 0px |
| Outline | none | = | = |
| Font | Mona Sans 16px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0d0c22 | = | = |
| Transition | color, box-shadow, border, background-color, -webkit-box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #98959f, opacity 1 | = | = |
| Painted layers | input.input2.input2--large 310.0x47.0 bg #ffffff border T:1px solid #dbdade @ 0.9 / R:1px solid #dbdade @ 0.9 / B:1px solid #dbdade @ 0.9 / L:1px solid #dbdade @ 0.9 r 8px | input.input2.input2--large 310.0x47.0 bg #ffffff border T:1px solid #9e9ea7 @ 0.7 / R:1px solid #9e9ea7 @ 0.7 / B:1px solid #9e9ea7 @ 0.7 / L:1px solid #9e9ea7 @ 0.7 r 8px shadow #060318 @ 0.03 0px 4px 4px 0px | input.input2.input2--large 310.0x47.0 bg #ffffff border T:1px solid #9e9ea7 @ 0.7 / R:1px solid #9e9ea7 @ 0.7 / B:1px solid #9e9ea7 @ 0.7 / L:1px solid #9e9ea7 @ 0.7 r 8px shadow #060318 @ 0.03 0px 4px 4px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### continue-btn

Continue button. The dark Continue submit; measured, never pressed (a press would submit).

Page: login. Selector: `"Continue"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 310 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #0d0c22 | 1px solid #3d3d4e | 1px solid #3d3d4e | 1px solid #3d3d4e |
| Radius | 1e+07px | = | = | = |
| Background | #0d0c22 | #3d3d4e | #3d3d4e | #3d3d4e |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 0px | = |
| Font | Mona Sans 14px/14px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border, border-radius, padding 0.05s cubic-bezier(0.32, 0, 0.59, 0.03) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 308px x 46px, absolute, bg #0d0c22, radius 0px | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0, radius 50% | = | = | = |
| Painted layers | button.btn2.btn2--medium 310.0x48.0 bg #0d0c22 border T:1px solid #0d0c22 / R:1px solid #0d0c22 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 1e+07px; button::before.btn2.btn2--medium 308pxx46px bg #0d0c22; button::after.btn2.btn2--medium 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | button.btn2.btn2--medium 310.0x48.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; button::before.btn2.btn2--medium 308pxx46px bg #0d0c22; button::after.btn2.btn2--medium 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | button.btn2.btn2--medium 310.0x48.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px outline 2px solid #f3afe4 offset 0px; button::before.btn2.btn2--medium 308pxx46px bg #0d0c22; button::after.btn2.btn2--medium 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% | button.btn2.btn2--medium 310.0x48.0 bg #3d3d4e border T:1px solid #3d3d4e / R:1px solid #3d3d4e / B:1px solid #3d3d4e / L:1px solid #3d3d4e r 1e+07px; button::before.btn2.btn2--medium 308pxx46px bg #0d0c22; button::after.btn2.btn2--medium 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `continue-btn-default.png`, `continue-btn-hover.png`, `continue-btn-focus-visible.png`, `continue-btn-pressed.png`.

#### auth-link

Auth link. A Terms / Privacy / Sign-up link under the card actions.

Page: login. Selector: `auth link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 34.22 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 12px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #7b7194 | #524b63 | = | #524b63 |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 34.2x15.0 outline 2px solid #f3afe4 offset 1px | = |

Crops: `auth-link-default.png`, `auth-link-hover.png`, `auth-link-focus-visible.png`, `auth-link-pressed.png`.

#### auth-art

Auth illustration panel. The painted half of the split layout (a shot fills it, credited bottom-right).

Page: login. Selector: `auth side panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Text node | a.auth-sidebar__credit: Mona Sans 14px/17px 400, #ffffff |
| Transition | none |
| How | at rest |

Crops: `auth-art-default.png`.

#### signup-card

Signup card. The "Welcome to Dribbble" form card; never filled or submitted.

Page: signup. Selector: `.auth-layout__content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 804 |
| Padding | 0px 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Text node | h1.auth-screen-header__heading: Mona Sans 24px/29px 700, #0d0c22 |
| Transition | none |
| Icon | 76 x 30, colour #0d0c22 |
| Painted layers | div 310.0x40.0 image linear-gradient(-90deg, #f3f3f4 8%, #faf9fb 28%, #f3f3f4 70%) r 1e+07px; input.input2.input2--large 310.0x47.0 bg #ffffff border T:1px solid #dbdade @ 0.9 / R:1px solid #dbdade @ 0.9 / B:1px solid #dbdade @ 0.9 / L:1px solid #dbdade @ 0.9 r 8px; button.btn2.btn2--medium 310.0x48.0 bg #0d0c22 border T:1px solid #0d0c22 / R:1px solid #0d0c22 / B:1px solid #0d0c22 / L:1px solid #0d0c22 r 1e+07px; button::before.btn2.btn2--medium 308pxx46px bg #0d0c22; button::after.btn2.btn2--medium 16pxx16px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #ffffff / L:1px solid #ffffff r 50%; div 0.0x0.0 image linear-gradient(-90deg, #f3f3f4 8%, #faf9fb 28%, #f3f3f4 70%) r 1e+07px |
| How | at rest |

Crops: `signup-card-default.png`.

#### signup-field

Signup email field. The "Enter email address" input; focused only, never filled or submitted.

Page: signup. Selector: `signup input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 310 x 47 | = |
| Padding | 0px 16px | = |
| Gap | 8px | = |
| Border | 1px solid #dbdade @ 0.9 | 1px solid #9e9ea7 @ 0.7 |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | none | #060318 @ 0.03 0px 4px 4px 0px |
| Outline | none | = |
| Font | Mona Sans 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d0c22 | = |
| Transition | color, box-shadow, border, background-color, -webkit-box-shadow 0.2s cubic-bezier(0.34, 1.56, 0.64, 1) | = |
| Cursor | text | = |
| Placeholder | #98959f, opacity 1 | = |
| Painted layers | input.input2.input2--large 310.0x47.0 bg #ffffff border T:1px solid #dbdade @ 0.9 / R:1px solid #dbdade @ 0.9 / B:1px solid #dbdade @ 0.9 / L:1px solid #dbdade @ 0.9 r 8px | input.input2.input2--large 310.0x47.0 bg #ffffff border T:1px solid #9e9ea7 @ 0.7 / R:1px solid #9e9ea7 @ 0.7 / B:1px solid #9e9ea7 @ 0.7 / L:1px solid #9e9ea7 @ 0.7 r 8px shadow #060318 @ 0.03 0px 4px 4px 0px |
| How | at rest | clicked into the field |

Crops: `signup-field-default.png`, `signup-field-focused.png`.

### Footer

#### footer

Footer. The footer: script wordmark, link columns (For designers/Hire designers/Company), social icons and the legal row.

Page: home. Selector: `footer / .site-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 508 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Text node | div.site-footer-marquee-item__title: Mona Sans 14px/28px 500, #0d0c22 |
| Transition | opacity 0.4s ease-in-out delay 0.1s |
| Icon | 104 x 30, colour #0d0c22 |
| Painted layers | div.site-footer.js-site-footer 1440.0x508.0 bg #ffffff; div::before.site-footer-marquee-item__stack 192pxx144px bg #edf3d8 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px; div::after.site-footer-marquee-item__stack 196pxx147px bg #e6fbfe border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 10px; div.site-footer-marquee-item__media 204.0x154.0 bg #9e9ea7 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 8px; div::before.site-footer-marquee-item__stack 192pxx144px bg #e3ebfd border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px; div::after.site-footer-marquee-item__stack 196pxx147px bg #f6d9fb border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 10px |
| Ancestor paint | 1 up body.logged-out.not-pro bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A text link in the footer bottom bar (For designers / Hire talent / …); the category cards above it are measured separately.

Page: home. Selector: `footer bottom-bar a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.09 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.site-footer__link 90.1x17.0 outline 2px solid #f3afe4 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social icon. A social-icon link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 18 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f3afe4 offset 1px | = |
| Font | Mona Sans 16px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0c22 | = | = | = |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #0d0c22 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.site-footer__social-link 18.0x18.0 outline 2px solid #f3afe4 offset 1px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `.site-nav at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 58 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #060318 |
| Text node | a.site-nav__login.btn2: Mona Sans 14px/14px 600, #ffffff |
| Transition | opacity 0.4s ease-in-out delay 0.1s |
| Icon | 89 x 25, colour #060318 |
| Painted layers | div.site-nav__dark-overlay 390.0x844.0 bg #000000 @ 0.5; div::before.site-nav__wrapper 390pxx58px bg #ffffff; span 24.0x3.0 bg #060318 r 1e+07px; span 17.8x3.0 bg #060318 r 1e+07px; span 12.0x3.0 bg #060318 r 1e+07px; div.site-nav-search.site-nav-search--nav 0.0x0.0 bg #ffffff |
| Ancestor paint | 1 up body.logged-out.not-pro bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header menu toggle.

Page: mobile. Selector: `header menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36 x 29 |
| Padding | 6px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span 24.0x3.0 bg #060318 r 1e+07px; span 17.8x3.0 bg #060318 r 1e+07px; span 12.0x3.0 bg #060318 r 1e+07px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The header menu panel opened by its own toggle.

Page: mobile. Selector: `mobile menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 319 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 16px/28px 400 |
| Letter spacing | normal |
| Colour | #060318 |
| Text node | a.site-nav-main__link: Mona Sans 18px/22px 700, #060318 |
| Transition | opacity, visibility 0.25s, 0.25s ease-out, ease-out delay 0s, 0s |
| Icon | 20 x 20, colour #060318 |
| Painted layers | div.site-nav-main__wrapper 390.0x319.0 bg #ffffff border T:1px solid #e7e7e9; a::after.site-nav-main__link 9pxx8px image url(data:…); ul.site-nav-sub 326.0x0.0 bg #ffffff; li::after.site-nav-sub__divider 326pxx1px bg #d8d6d5; a::after.site-nav-main__link 9pxx8px image url(data:…); ul.site-nav-sub.site-nav-sub--wide-format 326.0x0.0 bg #ffffff |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 333 x 64.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 27px/32.4px 600 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-search

Mobile search field.

Page: mobile. Selector: `search input/link at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 98.48 x 31 |
| Padding | 0px 16px |
| Gap | 0px |
| Border | 1px solid #e7e7e9 |
| Radius | 1e+07px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Mona Sans 13px/13px 400 |
| Letter spacing | normal |
| Colour | #0d0c22 |
| Transition | color 0.1s ease |
| Cursor | pointer |
| Painted layers | a.pill2.pill2--white-dark 98.5x31.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 1e+07px |
| How | at rest |

Crops: `m-search-default.png`.

## Transitions declared in the readable stylesheets

dribbble.com serves its Rails/Vite CSS bundles from cdn.dribbble.com (read from the network responses as well as the CSSOM), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- designer: `cubic-bezier(0.46, 0.1, 0.52, 0.98)`, `width 300ms ease-out, opacity 150ms ease-in 150ms`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color 0.15s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- designers: `width 300ms ease-out, opacity 150ms ease-in 150ms`, `color 0.1s ease-in-out`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color 0.15s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `width 200ms, height 200ms, max-height 200ms, transform 300ms cubic-bezier(0, 1.2, 1, 1), opacity 83ms ease-out`

- home: `width 300ms ease-out, opacity 150ms ease-in 150ms`, `color 0.1s ease-in-out`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color 0.15s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- jobs: `width 300ms ease-out, opacity 150ms ease-in 150ms`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color 0.15s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- login: `width 300ms ease-out, opacity 150ms ease-in 150ms`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color 0.15s`

- search: `width 300ms ease-out, opacity 150ms ease-in 150ms`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color 0.15s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- shot: `cubic-bezier(0.46, 0.1, 0.52, 0.98)`, `width 300ms ease-out, opacity 150ms ease-in 150ms`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color 0.15s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.2s`, `transform 0.2s`, `0.4s`

- shots: `width 300ms ease-out, opacity 150ms ease-in 150ms`, `color 0.1s ease-in-out`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color 0.15s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- stories: `width 300ms ease-out, opacity 150ms ease-in 150ms`, `opacity 0.2s ease-in, filter 0.2s ease-in`, `none`, `background-color 0.15s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`
