# Faire component measurements

Computed styles read from faire.com on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's public surfaces — the home page, category teaser grids, a public brand storefront, the SEO /suppliers/ listings, the marketing pages, the /apply brand application form, the /support help center and the sign-in/sign-up dialogs mounted by ?signIn=1 and ?signUp=1 — with the OneTrust consent layer hidden (never answered) and the intermittent Cloudflare edge challenge waited out (never solved), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The white top bar: Faire wordmark, "All categories" dropdown, search field, locale button, Blog, "Sign up to sell", "Sign in" and the dark "Sign up to buy" button.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 108 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #dadada; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.sc-a94a1c8b-1.cleewM: graphik 14px/20px 200, #333333, ls 0.15px |
| Transition | background 0.1s linear |
| Icon | 8 x 8, colour #333333 |
| Painted layers | header.border-b-fs-border-muted.bg-fs-surface-primary 1440.0x108.0 bg #ffffff border B:1px solid #dadada; div.flex.flex-row 597.9x40.0 bg #ffffff; div.fs-form-field.flex 597.9x40.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 999px; button.interactive.focusable 132.1x40.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div.bg-fs-surface-primary.flex 1440.0x47.0 bg #ffffff; div.bg-fs-surface-primary.relative 1064.7x47.0 bg #ffffff |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Faire wordmark in the header, linking home.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 136 x 29 |
| Padding | 8px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### search-field

Header search field. The "Search wholesale products or brands" field; focused and typed into then cleared — nothing searched.

Page: home. Selector: `input[type=search]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 579.11 x 20 | = | = |
| Padding | 0px 0px 0px 40px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Graphik_fix 14px/20px 400 | = | = |
| Letter spacing | 0.15px | = | = |
| Colour | #333333 | #000000 | #000000 |
| Transition | width, opacity 0.252s, 0.252s, 0.2s cubic-bezier(0.33, 1, 0.68, 1), cubic-bezier(0.33, 1, 0.68, 1), ease-in-out delay 0s, 0s, 0.07s | = | = |
| Cursor | text | = | = |
| Placeholder | #333333 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field | typed "candles", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`.

#### all-categories-btn

All categories button. The rounded header dropdown trigger (rounded-[32px]); the opened state was measured after activating it — a local UI toggle, its links never followed.

Page: home. Selector: `header button "All categories"`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 141.11 x 40 | 133 x 40 | = | = | 133 x 40 |
| Padding | 10px 16px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 32px | = | = | = | = |
| Background | transparent | #f1f1f1 | #f1f1f1 | #f1f1f1 | #f1f1f1 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = | = |
| Font | graphik 14px/20px 200 | GT Standard 14px/20px 400 | = | = | GT Standard 14px/20px 400 |
| Letter spacing | 0.15px | normal | = | = | normal |
| Colour | #333333 | #000000 | = | #000000 | #000000 |
| Transition | background-color 0.3s ease-out | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 8 x 8, colour #333333 | 8 x 8, colour #000000 | = | 8 x 8, colour #000000 | 8 x 8, colour #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | button.sc-a94a1c8b-1.cleewM 133.0x40.0 bg #f1f1f1 r 32px | button.sc-a94a1c8b-1.cleewM 141.1x40.0 bg #f1f1f1 r 32px outline 2px solid #101010 offset 2px | button.sc-a94a1c8b-1.cleewM 141.1x40.0 bg #f1f1f1 r 32px | button.sc-da430d62-1.llTVOz 133.0x40.0 bg #f1f1f1 r 32px |

Crops: `all-categories-btn-default.png`, `all-categories-btn-hover.png`, `all-categories-btn-focus-visible.png`, `all-categories-btn-pressed.png`, `all-categories-btn-opened.png`.

#### categories-panel

Categories menu panel. The panel opened by "All categories"; its links were never followed.

Page: home. Selector: `categories menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 712 |
| Padding | 48px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.f_t_base.f_t_color: graphik 12px/16px 200, #6c6a6a, ls 0.15px |
| Transition | none |
| Painted layers | div.bg-fs-surface-primary.mx-auto 1440.0x712.0 bg #ffffff |
| Ancestor paint | 1 up div.bg-fs-surface-primary.absolute bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.25 0px 12px 12px -8px |
| How | at rest |

Crops: `categories-panel-default.png`.

#### nav-sell

Sign up to sell link. The header link to the brand application; measured, never followed.

Page: home. Selector: `header "Sign up to sell"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.25 x 60 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #101010 offset 1px | = |
| Font | graphik 14px/20px 200 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | #000000 | = | #000000 |
| Transition | color 0.1s linear | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.focus-visible:outline.text-fs-text-primary 121.3x60.0 outline 1px solid #101010 offset 1px | = |

Crops: `nav-sell-default.png`, `nav-sell-hover.png`, `nav-sell-focus-visible.png`, `nav-sell-pressed.png`.

#### nav-signup-buy

Sign up to buy button. The dark "Sign up to buy" fs-button--primary in the header; measured, never pressed.

Page: home. Selector: `header .fs-button--primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132.11 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #333333 | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #ffffff, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.interactive.focusable 132.1x40.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 132.1x40.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 132.1x40.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #275ec5 offset 1px | button.interactive.focusable 132.1x40.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-buy-default.png`, `nav-signup-buy-hover.png`, `nav-signup-buy-focus-visible.png`, `nav-signup-buy-pressed.png`.

#### nav-link

Nav link. The header Blog link; measured, never followed.

Page: home. Selector: `header a "Blog"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 54.61 x 60 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | graphik 14px/20px 200 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | #000000 | = | #000000 |
| Transition | color 0.1s linear | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-fs-text-primary.hover:text-fs-action-text-hover 54.6x60.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### locale-btn

Locale button. The EN-US locale selector (globe + "EN-US") in the header — a div control, not a button; measured, never opened.

Page: home. Selector: `header locale control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.75 x 60 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Graphik 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | p.f_t_base.f_t_color: graphik 14px/20px 200, #333333, ls 0.15px | = | - | = |
| Transition | none | = | - | = |
| Icon | 16 x 16, colour #000000 | = | - | = |
| Painted layers | div.[&&]:border-fs-border-muted.[&&]:absolute 0.0x0.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada shadow #f7f7f7 0px 1px 1px 0px | div.[&&]:border-fs-border-muted.[&&]:absolute 170.0x506.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada shadow #f7f7f7 0px 1px 1px 0px | - | div.[&&]:border-fs-border-muted.[&&]:absolute 170.0x506.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada shadow #f7f7f7 0px 1px 1px 0px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `locale-btn-default.png`, `locale-btn-hover.png`, `locale-btn-pressed.png`.

#### nav-signin

Sign in button. The header "Sign in" — it mounts the sign-in dialog; measured, never pressed.

Page: home. Selector: `header "Sign in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.06 x 60 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | #000000 | = | #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.type-fs-paragraph.whitespace-nowrap 79.1x60.0 outline 1px auto #101010 offset 0px | = |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### promo-banner

Promo banner. The top strip above the header ("Shop wholesale online from over 100,000 brands. Sign up").

Page: home. Selector: `promo strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 394.27 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik_fix 14px/20px 400 |
| Letter spacing | 0.15px |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `promo-banner-default.png`.

#### cat-nav-link

Category nav link. A link in the sub-header category strip ("New products", "Home decor"…); measured, never followed.

Page: home. Selector: `header category a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.5 x 30 | = | = | = |
| Padding | 4px 0px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = |
| Font | graphik 14px/20px 200 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | #000000 | = | #000000 |
| Text node | h5.f_t_base.f_t_color: graphik 18px/26px 200, #333333, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.sc-da430d62-1.llTVOz 105.5x30.0 r 4px outline 2px solid #101010 offset 2px | = |

Crops: `cat-nav-link-default.png`, `cat-nav-link-hover.png`, `cat-nav-link-focus-visible.png`, `cat-nav-link-pressed.png`.

### Home

#### hero-h1

Hero headline. "Find your next bestseller" — the type-fs-display display heading in inverse ink over the hero media.

Page: home. Selector: `h1.type-fs-display`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 546 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nantes_fix 52px/64px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-panel

Hero panel. The hero block behind the display heading.

Page: home. Selector: `hero section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 224 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.type-fs-display-s.text-fs-text-primary-inverse: GT Canon 52px/64px 400, #ffffff |
| Transition | none |
| Painted layers | button.interactive.focusable 131.0x48.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px; a.interactive.focusable 87.0x20.0 bg #333333 @ 0 r 4px |
| How | at rest |

Crops: `hero-panel-default.png`.

#### cta-secondary

Secondary button. An outlined "Sign up to buy" fs-button--secondary; measured, never pressed.

Page: home. Selector: `.fs-button--secondary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.11 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #dadada | = | = | 1px solid #000000 |
| Radius | 4px | = | = | = |
| Background | #ffffff | = | = | #f1f1f1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | = | = | #000000 |
| Text node | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #333333, ls 0.15px | = | = | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #000000, ls 0.15px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.interactive.focusable 140.1x48.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px | = | button.interactive.focusable 140.1x48.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px outline 2px solid #275ec5 offset 1px | button.interactive.focusable 140.1x48.0 bg #f1f1f1 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-secondary-default.png`, `cta-secondary-hover.png`, `cta-secondary-focus-visible.png`, `cta-secondary-pressed.png`.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 627 x 128 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | nantes 52px/64px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.w-full.text-center: nantes 52px/64px 400, #333333 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### brand-card

Brand card. A brand tile on the home page (image, name); measured, never followed.

Page: home. Selector: `a[href*=/brand/]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 217.33 x 273.34 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.f_t_base.f_t_maxLines: graphik 14px/20px 500, #333333, ls 0.15px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | p.f_t_base.f_t_maxLines 127.7x20.0 image linear-gradient(to right in oklab, #333333 0px, #333333 100%) | p.f_t_base.f_t_maxLines 104.0x20.0 image linear-gradient(to right in oklab, #333333 0px, #333333 100%) |
| How | at rest | mouse hover |

Crops: `brand-card-default.png`, `brand-card-hover.png`.

#### cta-plain

Plain button. A "Sign up for free" fs-button--plain text button; measured, never pressed.

Page: home. Selector: `.fs-button--plain`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.41 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #333333 @ 0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | = | = | #000000 |
| Text node | span.items-start.inline: Graphik_fix 14px/20px 400, #333333, ls 0.15px | = | = | span.items-start.inline: Graphik_fix 14px/20px 400, #000000, ls 0.15px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.interactive.focusable 105.4x20.0 bg #333333 @ 0 r 4px | = | button.interactive.focusable 105.4x20.0 bg #333333 @ 0 r 4px outline 2px solid #275ec5 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-plain-default.png`, `cta-plain-hover.png`, `cta-plain-focus-visible.png`, `cta-plain-pressed.png`.

#### cta-primary

Primary button. A dark "Sign up to buy" fs-button--primary (medium); measured, never pressed.

Page: home. Selector: `main .fs-button--primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 131 x 48 | 140.11 x 48 | 140.11 x 48 | 140.11 x 48 |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | = | = | #f7f7f7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard 14px/20px 400 | Graphik_fix 14px/20px 400 | Graphik_fix 14px/20px 400 | Graphik_fix 14px/20px 400 |
| Letter spacing | normal | 0.15px | 0.15px | 0.15px |
| Colour | #161616 | #333333 | #333333 | #333333 |
| Text node | span.text-center.fs-button__label--clamped: GT Standard 14px/20px 400, #161616 | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #333333, ls 0.15px | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #333333, ls 0.15px | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #333333, ls 0.15px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.interactive.focusable 131.0x48.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 140.1x48.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 140.1x48.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #275ec5 offset 1px | button.interactive.focusable 140.1x48.0 bg #f7f7f7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-primary-default.png`, `cta-primary-hover.png`, `cta-primary-focus-visible.png`, `cta-primary-pressed.png`.

#### pill-tab

Featured-brands pill tab. A rounded pill filter tab under "Featured brands" (the selected one paints dark); measured, never toggled.

Page: home. Selector: `featured-brands pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116.5 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Graphik 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.f_t_base.f_t_color: graphik 14px/20px 200, #333333, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | p.f_t_base.f_t_color 116.5x40.0 border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 40px | = | p.f_t_base.f_t_color 116.5x40.0 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 r 40px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pill-tab-default.png`, `pill-tab-hover.png`, `pill-tab-focus-visible.png`, `pill-tab-pressed.png`.

#### category-card

Category card. A category tile (image, label); measured, never followed.

Page: home. Selector: `a[href*=/category/]:has(img)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 437.33 x 312.38 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h4.f_t_base.f_t_color: nantes 22px/32px 400, #ffffff | = |
| Transition | transform, translate, scale, rotate 1s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | div.absolute.inset-0 437.3x312.4 image linear-gradient(22.18deg, #000000 @ 0.5 1.86%, #000000 @ 0 31.23%) | = |
| How | at rest | mouse hover |

Crops: `category-card-default.png`, `category-card-hover.png`.

### Footer

#### footer

Footer. The page footer: brand promise line, sitemap columns, locale and social links, legal row.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 448 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.f_t_base.f_t_color: nantes 38px/50px 400, #333333 |
| Transition | none |
| Icon | 16 x 16, colour #333333 |
| Painted layers | button.interactive.focusable 140.1x48.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px; a.interactive.focusable 139.3x48.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px |
| Ancestor paint | 1 up div.bg-fs-surface-primary.w-full bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 59.2 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Brand storefront

#### brand-h1

Brand headline. "54 Celsius wholesale" — the brand storefront masthead.

Page: brand. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 215 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Standard 22px/32px 500 |
| Letter spacing | normal |
| Colour | #161616 |
| Transition | none |
| How | at rest |

Crops: `brand-h1-default.png`.

#### min-order-badge

Minimum order badge. The "US$100 min" order-minimum label on brand tiles.

Page: brand. Selector: `"US$X min" badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 75 x 20 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.type-fs-paragraph: GT Standard 14px/20px 400, #161616 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `min-order-badge-default.png`.

#### brand-tab

Section tab. A storefront section nav item ("All products"/"New"); measured, never followed.

Page: brand. Selector: `brand section tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78 x 51 | = | = | = |
| Padding | 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid #95948f; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #101010 offset 0px | = |
| Font | Graphik 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h2.f_t_base.f_t_color: GT Standard 14px/20px 500, #161616 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.flex.h-full 78.0x51.0 border B:1px solid #95948f | = | button.flex.h-full 78.0x51.0 border B:1px solid #95948f outline 5px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `brand-tab-default.png`, `brand-tab-hover.png`, `brand-tab-focus-visible.png`, `brand-tab-pressed.png`.

#### brand-product-tile

Brand product tile. A product card on the brand page (photo, name, price, order minimum); it links to the sign-up dialog — measured, never followed.

Page: brand. Selector: `brand product tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 259.19 x 259.19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `brand-product-tile-default.png`, `brand-product-tile-hover.png`.

#### about-h2

About heading. The "About <brand>" section heading.

Page: brand. Selector: `h2 About`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 616 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Standard 14px/20px 500 |
| Letter spacing | normal |
| Colour | #161616 |
| Transition | none |
| Ancestor paint | 1 up div.flex.h-full shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2px 8px 0px |
| How | at rest |

Crops: `about-h2-default.png`.

#### wall-email

Wall email field. The "Business email address" field in the brand page's sign-up wall; focused and typed into then cleared — never submitted.

Page: brand. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 322 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GT Standard 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #161616 | #000000 | #000000 |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #161616 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `wall-email-default.png`, `wall-email-focused.png`.

#### brand-avatar

Brand avatar. The brand's circular fs-avatar logo by the masthead.

Page: brand. Selector: `span.fs-avatar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 96 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 999px |
| Background | #ffffff |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | GT Standard 30px/38px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | span.fs-avatar.fs-avatar__placeholder 96.0x96.0 bg #ffffff r 999px outline 2px solid #000000 @ 0 offset 2px; span.pointer-events-none.absolute 96.0x96.0 bg #000000 @ 0.02 r 999px |
| How | at rest |

Crops: `brand-avatar-default.png`.

### Suppliers listings

#### supplier-row

Supplier row. A brand row/card in the suppliers listing; measured, never followed.

Page: suppliers. Selector: `suppliers a[href*=/brand/]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 220 x 220 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.bg-fs-surface-secondary.relative 220.0x220.0 bg #f7f7f7; div.bg-fs-action-surface-active/2.rounded-fs-component-default 220.0x220.0 bg #000000 @ 0.02 r 4px | = |
| How | at rest | mouse hover |

Crops: `supplier-row-default.png`, `supplier-row-hover.png`.

#### supall-h1

All brands headline. The /suppliers/All Brands masthead.

Page: suppliersAll. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Canon 30px/38px 400 |
| Letter spacing | normal |
| Colour | #161616 |
| Transition | none |
| How | at rest |

Crops: `supall-h1-default.png`.

#### supall-row

All brands row. A brand row in the A-Z listing; measured, never followed.

Page: suppliersAll. Selector: `suppliers/All a[href*=/brand/]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 220 x 220 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.bg-fs-surface-secondary.relative 220.0x220.0 bg #f7f7f7; div.bg-fs-action-surface-active/2.rounded-fs-component-default 220.0x220.0 bg #000000 @ 0.02 r 4px | = |
| How | at rest | mouse hover |

Crops: `supall-row-default.png`, `supall-row-hover.png`.

#### sup-h1

Suppliers headline. The SEO suppliers listing masthead.

Page: suppliers. Selector: `h1`. States: .

Not found on the page at capture time.

#### sup-filter-link

Subcategory link. A related-subcategory link; measured, never followed.

Page: suppliers. Selector: `suppliers subcategory a`. States: .

Not found on the page at capture time.

### Brand application (/apply)

#### back-btn

Back button. The "Go back" chevron icon button in the top bar; measured, never pressed.

Page: apply. Selector: `apply back button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Graphik 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.absolute.left-4 40.0x40.0 r 3.35544e+07px outline 1px auto #101010 offset 0px | = |

Crops: `back-btn-default.png`, `back-btn-hover.png`, `back-btn-focus-visible.png`, `back-btn-pressed.png`.

#### field-firstname

First name field. The firstName input; focused and typed into then cleared — never submitted.

Page: apply. Selector: `input[name=firstName]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 186 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Graphik_fix 14px/20px 400 | = | = |
| Letter spacing | 0.15px | = | = |
| Colour | #333333 | #000000 | #000000 |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #333333, opacity 1 | #000000, opacity 1 | #000000, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field | typed "Ada", then deleted; nothing sent |

Crops: `field-firstname-default.png`, `field-firstname-focused.png`, `field-firstname-filled.png`.

#### field-lastname

Last name field. The lastName input; focused and typed into then cleared — never submitted.

Page: apply. Selector: `input[name=lastName]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 186 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Graphik_fix 14px/20px 400 | = | = |
| Letter spacing | 0.15px | = | = |
| Colour | #333333 | #000000 | #000000 |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #333333, opacity 1 | #000000, opacity 1 | #000000, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field | typed "Lovelace", then deleted; nothing sent |

Crops: `field-lastname-default.png`, `field-lastname-focused.png`, `field-lastname-filled.png`.

#### field-email

Email field. The work-email input; focused and typed into then cleared — never submitted.

Page: apply. Selector: `input[name=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 430 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Graphik_fix 14px/20px 400 | = | = |
| Letter spacing | 0.15px | = | = |
| Colour | #333333 | #000000 | #000000 |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #333333, opacity 1 | #000000, opacity 1 | #000000, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `field-email-default.png`, `field-email-focused.png`, `field-email-filled.png`.

#### field-phone

Phone field. The phoneNumber input with its +1 country-code prefix button; focused and typed into then cleared — never submitted.

Page: apply. Selector: `input[name=phoneNumber]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 406 x 40 | = | = |
| Padding | 0px 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | graphik 14px/20px 200 | = | = |
| Letter spacing | 0.15px | = | = |
| Colour | #333333 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #333333, opacity 1 | = | = |
| Ancestor paint | 1 up div.rounded-fs-component-default.bg-fs-surface-primary bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "555 000 0000", then deleted; nothing sent |

Crops: `field-phone-default.png`, `field-phone-focused.png`, `field-phone-filled.png`.

#### phone-code-btn

Country code button. The +1 country-code prefix button inside the phone field; measured, never opened.

Page: apply. Selector: `phone +1 button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64 x 40 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | T: none; R: 1px solid #dadada; B: none; L: none | = | T: none; R: 1px solid #8e8c8c; B: none; L: none | = |
| Radius | 4px 0px 0px 4px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 0px | = |
| Font | Graphik 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.f_t_base.f_t_truncate: graphik 14px/20px 200, #333333, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 8 x 8, colour #333333 | = | = | = |
| Painted layers | button.rounded-l-fs-component-default.border-r-fs-border-muted 64.0x40.0 bg #ffffff border R:1px solid #dadada r 4px 0px 0px 4px | = | button.rounded-l-fs-component-default.border-r-fs-border-muted 64.0x40.0 bg #ffffff border R:1px solid #8e8c8c r 4px 0px 0px 4px outline 2px solid #101010 offset 0px | = |
| Ancestor paint | 1 up div.rounded-fs-component-default.bg-fs-surface-primary bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `phone-code-btn-default.png`, `phone-code-btn-hover.png`, `phone-code-btn-focus-visible.png`, `phone-code-btn-pressed.png`.

#### field-password

Password field. The password input (with a show-password icon); focused only — nothing was typed or submitted.

Page: apply. Selector: `input[name=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 414 x 20 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik_fix 14px/20px 400 | = |
| Letter spacing | 0.15px | = |
| Colour | #333333 | #000000 |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #333333, opacity 1 | #000000, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field |

Crops: `field-password-default.png`, `field-password-focused.png`.

#### show-password

Show password icon button. The fs-icon-button--plain show/hide toggle inside the password field; measured, never pressed.

Page: apply. Selector: `show password button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #333333 @ 0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 8px | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | #000000 | = | #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #333333 | 16 x 16, colour #000000 | = | 16 x 16, colour #000000 |
| Painted layers | button.interactive.focusable 16.0x16.0 bg #333333 @ 0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | = | button.interactive.focusable 16.0x16.0 bg #333333 @ 0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #275ec5 offset 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `show-password-default.png`, `show-password-hover.png`, `show-password-focus-visible.png`, `show-password-pressed.png`.

#### checkbox-terms

Terms checkbox. The fs-checkbox for the terms consent; measured, never toggled.

Page: apply. Selector: `.fs-checkbox__input`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 14 x 14 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 2px solid #275ec5 offset 2px |
| Font | Graphik_fix 14px/20px 400 | = |
| Letter spacing | 0.15px | = |
| Colour | #333333 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Placeholder | #333333, opacity 1 | = |
| Ancestor paint | 1 up div.fs-checkbox__box.type-aligned-elem bg #333333 @ 0 | = |
| How | at rest | Shift+Tab, Tab |
| Painted layers | - | input.fs-checkbox__input.focusable 14.0x14.0 outline 2px solid #275ec5 offset 2px |

Crops: `checkbox-terms-default.png`, `checkbox-terms-focus-visible.png`.

#### checkbox-marketing

Marketing checkbox. The opt-in fs-checkbox; measured, never toggled.

Page: apply. Selector: `.fs-checkbox__input marketing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 14 x 14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik_fix 14px/20px 400 |
| Letter spacing | 0.15px |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| Placeholder | #333333, opacity 1 |
| Ancestor paint | 1 up div.fs-checkbox__box.type-aligned-elem bg #333333 @ 0 |
| How | at rest |

Crops: `checkbox-marketing-default.png`.

#### next-btn

Next button. The form's dark fs-button--primary "Next" submit; its states were measured but the button was never clicked — nothing was submitted.

Page: apply. Selector: `apply Next`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 472 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #333333 | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #ffffff, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.interactive.focusable 472.0x48.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 472.0x48.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 472.0x48.0 bg #333333 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #275ec5 offset 1px | button.interactive.focusable 472.0x48.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| Ancestor paint | 2 up div.w-full.bg-white bg #ffffff shadow #000000 @ 0 0px -2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `next-btn-default.png`, `next-btn-hover.png`, `next-btn-focus-visible.png`, `next-btn-pressed.png`.

#### apply-heading

Application heading. The /apply step heading ("Welcome! Sign up to sell on Faire." — an h4 in the f_t_displaySSerifRegular serif role).

Page: apply. Selector: `apply h4 heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472 x 38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | nantes 30px/38px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `apply-heading-default.png`.

### Sign-in dialog

#### signin-dialog

Sign-in dialog. The "Sign in to Faire" fs-modal mounted by ?signIn=1 over the home page: email + password fields, dark submit, Google and Apple SSO, a sign-up link and the close icon.

Page: signin. Selector: `.fs-modal sign-in`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 649 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | GT Standard 14px/20px 400 |
| Letter spacing | normal |
| Colour | #161616 |
| Text node | h4.f_t_base.f_t_color: GT Canon 30px/38px 400, #161616 |
| Transition | none |
| Icon | 16 x 16, colour #161616 |
| Painted layers | div.fs-modal.fs-modal--canvas 420.0x649.0 bg #ffffff; button.fs-modal__close-btn.interactive 24.0x24.0 bg #333333 @ 0 r 4px; div.border-fs-border-muted.flex 0.0x0.0 border B:1px solid #e4e1de; div.fs-form-field.flex 340.0x40.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px; div.fs-form-field.flex 340.0x40.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px; button.interactive.focusable 16.0x16.0 bg #333333 @ 0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest |

Crops: `signin-dialog-default.png`.

#### signin-submit

Sign in submit. The dialog's Sign in submit button; its states were measured but the button was never clicked — nothing was submitted.

Page: signin. Selector: `sign-in submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 340 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #161616 | #474747 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-center.fs-button__label--clamped: GT Standard 14px/20px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.interactive.focusable 340.0x48.0 bg #161616 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 340.0x48.0 bg #474747 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 340.0x48.0 bg #161616 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #275ec5 offset 1px | button.interactive.focusable 340.0x48.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-submit-default.png`, `signin-submit-hover.png`, `signin-submit-focus-visible.png`, `signin-submit-pressed.png`.

#### signin-email

Email field (sign-in). The email input in the sign-in dialog; focused and typed into then cleared — never submitted.

Page: signin. Selector: `sign-in input[name=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 298 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GT Standard 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #161616 | #000000 | #000000 |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #161616 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signin-email-default.png`, `signin-email-focused.png`, `signin-email-filled.png`.

#### signin-password

Password field (sign-in). The password input in the sign-in dialog; focused only — nothing was typed or submitted.

Page: signin. Selector: `sign-in input[type=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 282 x 20 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT Standard 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #161616 | #000000 |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #161616 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field |

Crops: `signin-password-default.png`, `signin-password-focused.png`.

#### signin-google

Google SSO button. "Sign in with Google"; measured, never followed.

Page: signin. Selector: `sign-in Google button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 340 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | 1px solid #e4e1de | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | #474747 | = | #474747 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = |
| Font | GT Standard 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #161616 | 20 x 20, colour #ffffff | = | 20 x 20, colour #ffffff |
| Painted layers | button.sc-da430d62-1.dmAPYn 340.0x48.0 bg #ffffff border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px | button.sc-da430d62-1.dmAPYn 340.0x48.0 bg #474747 border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px | button.sc-da430d62-1.dmAPYn 340.0x48.0 bg #ffffff border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px outline 2px solid #101010 offset 2px | button.sc-da430d62-1.dmAPYn 340.0x48.0 bg #474747 border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-google-default.png`, `signin-google-hover.png`, `signin-google-focus-visible.png`, `signin-google-pressed.png`.

#### signin-apple

Apple SSO button. "Sign in with Apple"; measured, never followed.

Page: signin. Selector: `sign-in Apple button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 340 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | 1px solid #e4e1de | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | #474747 | = | #474747 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = |
| Font | GT Standard 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #161616 | 20 x 20, colour #ffffff | = | 20 x 20, colour #ffffff |
| Painted layers | button.sc-da430d62-1.dmAPYn 340.0x48.0 bg #ffffff border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px | button.sc-da430d62-1.dmAPYn 340.0x48.0 bg #474747 border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px | button.sc-da430d62-1.dmAPYn 340.0x48.0 bg #ffffff border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px outline 2px solid #101010 offset 2px | button.sc-da430d62-1.dmAPYn 340.0x48.0 bg #474747 border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-apple-default.png`, `signin-apple-hover.png`, `signin-apple-focus-visible.png`, `signin-apple-pressed.png`.

#### signin-signup-link

Sign up link (sign-in). The "Sign up" action inside the sign-in dialog; measured, never followed.

Page: signin. Selector: `sign-in Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 340 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #dadada | 1px solid #000000 | = | 1px solid #000000 |
| Radius | 4px | = | = | = |
| Background | #ffffff | #f1f1f1 | = | #f1f1f1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | #000000 | = | #000000 |
| Text node | span.text-center.fs-button__label--clamped: GT Standard 14px/20px 400, #161616 | span.text-center.fs-button__label--clamped: GT Standard 14px/20px 400, #000000 | = | span.text-center.fs-button__label--clamped: GT Standard 14px/20px 400, #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.interactive.focusable 340.0x48.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px | a.interactive.focusable 340.0x48.0 bg #f1f1f1 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px | a.interactive.focusable 340.0x48.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px outline 2px solid #275ec5 offset 1px | a.interactive.focusable 340.0x48.0 bg #f1f1f1 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-signup-link-default.png`, `signin-signup-link-hover.png`, `signin-signup-link-focus-visible.png`, `signin-signup-link-pressed.png`.

#### signin-close

Dialog close button. The dialog's "Close modal" icon button; measured, never pressed.

Page: signin. Selector: `sign-in close`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #333333 @ 0 | #f1f1f1 | = | #f1f1f1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | #000000 | = | #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #161616 | = | = | = |
| Painted layers | button.fs-modal__close-btn.interactive 24.0x24.0 bg #333333 @ 0 r 4px | button.fs-modal__close-btn.interactive 24.0x24.0 bg #f1f1f1 r 4px | button.fs-modal__close-btn.interactive 24.0x24.0 bg #333333 @ 0 r 4px outline 2px solid #275ec5 offset 1px | button.fs-modal__close-btn.interactive 24.0x24.0 bg #f1f1f1 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-close-default.png`, `signin-close-hover.png`, `signin-close-focus-visible.png`, `signin-close-pressed.png`.

#### signin-show-password

Show password icon (sign-in). The eye icon inside the password field; measured, never pressed.

Page: signin. Selector: `sign-in show password`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #333333 @ 0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 8px | = |
| Font | GT Standard 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | #000000 | = | #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #161616 | 16 x 16, colour #000000 | = | 16 x 16, colour #000000 |
| Painted layers | button.interactive.focusable 16.0x16.0 bg #333333 @ 0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | = | button.interactive.focusable 16.0x16.0 bg #333333 @ 0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #275ec5 offset 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-show-password-default.png`, `signin-show-password-hover.png`, `signin-show-password-focus-visible.png`, `signin-show-password-pressed.png`.

### Sign-up dialog

#### signup-dialog

Sign-up dialog. The "Unlock wholesale pricing" fs-modal mounted by ?signUp=1: business-email field, "Sign up for free" submit, Google and Apple SSO and a sign-in link.

Page: signup. Selector: `.fs-modal sign-up`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 523 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | GT Standard 14px/20px 400 |
| Letter spacing | normal |
| Colour | #161616 |
| Text node | h4.f_t_base.f_t_color: GT Canon 30px/38px 400, #161616 |
| Transition | none |
| Icon | 16 x 16, colour #161616 |
| Painted layers | div.fs-modal.fs-modal--canvas 500.0x523.0 bg #ffffff; button.fs-modal__close-btn.interactive 24.0x24.0 bg #333333 @ 0 r 4px; div.fs-form-field.flex 436.0x40.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px; button.interactive.focusable 436.0x48.0 bg #161616 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; button.sc-da430d62-1.dmAPYn 436.0x48.0 bg #ffffff border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px; div.bg-fs-surface-secondary.p-8 500.0x108.0 bg #f7f7f7 |
| How | at rest |

Crops: `signup-dialog-default.png`.

#### signup-email

Business email field. The business-email input in the sign-up dialog; focused and typed into then cleared — never submitted.

Page: signup. Selector: `sign-up email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 394 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GT Standard 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #161616 | #000000 | #000000 |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #161616, opacity 1 | #000000, opacity 1 | #000000, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signup-email-default.png`, `signup-email-focused.png`, `signup-email-filled.png`.

#### signup-submit

Sign up submit. The dialog's "Sign up for free" submit button; its states were measured but the button was never clicked — nothing was submitted.

Page: signup. Selector: `sign-up submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 436 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #161616 | #474747 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-center.fs-button__label--clamped: GT Standard 14px/20px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.interactive.focusable 436.0x48.0 bg #161616 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 436.0x48.0 bg #474747 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.interactive.focusable 436.0x48.0 bg #161616 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #275ec5 offset 1px | button.interactive.focusable 436.0x48.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-submit-default.png`, `signup-submit-hover.png`, `signup-submit-focus-visible.png`, `signup-submit-pressed.png`.

#### signup-google

Google SSO button (sign-up). "Sign up with Google"; measured, never followed.

Page: signup. Selector: `sign-up Google button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 436 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | 1px solid #e4e1de | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | #474747 | = | #474747 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 2px | = |
| Font | GT Standard 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #161616 | 20 x 20, colour #ffffff | = | 20 x 20, colour #ffffff |
| Painted layers | button.sc-da430d62-1.dmAPYn 436.0x48.0 bg #ffffff border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px | button.sc-da430d62-1.dmAPYn 436.0x48.0 bg #474747 border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px | button.sc-da430d62-1.dmAPYn 436.0x48.0 bg #ffffff border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px outline 2px solid #101010 offset 2px | button.sc-da430d62-1.dmAPYn 436.0x48.0 bg #474747 border T:1px solid #e4e1de / R:1px solid #e4e1de / B:1px solid #e4e1de / L:1px solid #e4e1de r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-google-default.png`, `signup-google-hover.png`, `signup-google-focus-visible.png`, `signup-google-pressed.png`.

#### signup-apple

Apple SSO button (sign-up). "Sign up with Apple"; measured, never followed.

Page: signup. Selector: `sign-up Apple button`. States: .

Not found on the page at capture time.

#### signup-signin-link

Sign in link (sign-up). The "Sign in" action inside the sign-up dialog; measured, never followed.

Page: signup. Selector: `sign-up Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard M 12px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.focusable.interactive 36.0x14.0 outline 2px solid #275ec5 offset 1px | = |

Crops: `signup-signin-link-default.png`, `signup-signin-link-hover.png`, `signup-signin-link-focus-visible.png`, `signup-signin-link-pressed.png`.

#### signup-close

Dialog close button (sign-up). The dialog's "Close modal" icon button; measured, never pressed.

Page: signup. Selector: `sign-up close`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #333333 @ 0 | #f1f1f1 | = | #f1f1f1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | #000000 | = | #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #161616 | = | = | = |
| Painted layers | button.fs-modal__close-btn.interactive 24.0x24.0 bg #333333 @ 0 r 4px | button.fs-modal__close-btn.interactive 24.0x24.0 bg #f1f1f1 r 4px | button.fs-modal__close-btn.interactive 24.0x24.0 bg #333333 @ 0 r 4px outline 2px solid #275ec5 offset 1px | button.fs-modal__close-btn.interactive 24.0x24.0 bg #f1f1f1 r 4px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `signup-close-default.png`, `signup-close-hover.png`, `signup-close-focus-visible.png`, `signup-close-pressed.png`.

### Help center

#### help-search

Help search field. The "Search retailer guides" field; focused and typed into then cleared — nothing searched.

Page: support. Selector: `support search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 564 x 40 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | graphik 14px/20px 200 | = | = |
| Letter spacing | 0.15px | = | = |
| Colour | #333333 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #333333 @ 0.5, opacity 1 | = | = |
| Ancestor paint | 1 up div.RoundSearchInputField__RoundSearchWrapper-sc-3a76fb54-0.cSSARQ bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "shipping", then deleted; nothing sent |

Crops: `help-search-default.png`, `help-search-focused.png`, `help-search-filled.png`.

#### help-link

Help topic link. A help topic link; measured, never followed.

Page: support. Selector: `support topic a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 471.98 x 162 | = | = | = |
| Padding | 0px 0px 40px 56px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.fs-tag__content: Graphik_fix 12px/16px 400, #333333, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.fs-tag.fs-component 120.6x24.0 bg #f1f1f1 r 2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `help-link-default.png`, `help-link-hover.png`, `help-link-focus-visible.png`, `help-link-pressed.png`.

#### help-h1

Help center headline. The /support help-center masthead.

Page: support. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 398 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | nantes 52px/64px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `help-h1-default.png`.

### Marketing pages

#### hw-h1

How Faire works headline. The /how-faire-works masthead.

Page: howItWorks. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 647 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | graphik 18px/26px 500 |
| Letter spacing | 0.15px |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `hw-h1-default.png`.

#### hw-cta

How Faire works headline CTA. The page's main call to action; measured, never followed or pressed.

Page: howItWorks. Selector: `howItWorks CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52.06 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik_fix 14px/normal 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.focusable.interactive 52.1x17.0 outline 2px solid #275ec5 offset 1px | = |

Crops: `hw-cta-default.png`, `hw-cta-hover.png`, `hw-cta-focus-visible.png`, `hw-cta-pressed.png`.

#### about-h1

About headline. The /about masthead.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 74 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Standard 18px/26px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `about-h1-default.png`.

#### about-cta

About headline CTA. The page's main call to action; measured, never followed or pressed.

Page: about. Selector: `about CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 47 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.focusable.interactive 47.0x16.0 outline 2px solid #275ec5 offset 1px | = |

Crops: `about-cta-default.png`, `about-cta-hover.png`, `about-cta-focus-visible.png`, `about-cta-pressed.png`.

#### news-cta

Newsroom headline CTA. The page's main call to action; measured, never followed or pressed.

Page: news. Selector: `news CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123.36 x 50 | = | = | = |
| Padding | 15px 25px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #333333 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | graphik 14px/20px 200 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.builder-block.builder-f9e595bb8f6d42458b03fd5d96ef844d 123.4x50.0 bg #333333 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `news-cta-default.png`, `news-cta-hover.png`, `news-cta-focus-visible.png`, `news-cta-pressed.png`.

#### news-card

Newsroom headline card. A content card on the page; measured, never followed.

Page: news. Selector: `news card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 86.81 x 38 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | graphik 14px/20px 200 | = |
| Letter spacing | 0.15px | = |
| Colour | #333333 | #000000 |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `news-card-default.png`, `news-card-hover.png`.

#### careers-cta

Careers headline CTA. The page's main call to action; measured, never followed or pressed.

Page: careers. Selector: `careers CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.25 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `careers-cta-default.png`, `careers-cta-hover.png`, `careers-cta-focus-visible.png`, `careers-cta-pressed.png`.

#### lr-h1

Large retailers headline. The /large-retailers masthead.

Page: largeRetailers. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 137.75 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | graphik 12px/16px 200 |
| Letter spacing | 0.15px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `lr-h1-default.png`.

#### lr-cta

Large retailers headline CTA. The page's main call to action; measured, never followed or pressed.

Page: largeRetailers. Selector: `largeRetailers CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.11 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #dadada | 1px solid #000000 | = | 1px solid #000000 |
| Radius | 4px | = | = | = |
| Background | #ffffff | #f1f1f1 | = | #f1f1f1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | #000000 | = | #000000 |
| Text node | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #333333, ls 0.15px | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #000000, ls 0.15px | = | span.text-center.fs-button__label--clamped: Graphik_fix 14px/20px 400, #000000, ls 0.15px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.interactive.focusable 140.1x48.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px | button.interactive.focusable 140.1x48.0 bg #f1f1f1 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px | button.interactive.focusable 140.1x48.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 4px outline 2px solid #275ec5 offset 1px | button.interactive.focusable 140.1x48.0 bg #f1f1f1 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `lr-cta-default.png`, `lr-cta-hover.png`, `lr-cta-focus-visible.png`, `lr-cta-pressed.png`.

#### pos-cta

Point of sale headline CTA. The page's main call to action; measured, never followed or pressed.

Page: pos. Selector: `pos CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52.06 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik_fix 14px/normal 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.focusable.interactive 52.1x17.0 outline 2px solid #275ec5 offset 1px | = |

Crops: `pos-cta-default.png`, `pos-cta-hover.png`, `pos-cta-focus-visible.png`, `pos-cta-pressed.png`.

#### markets-h1

Faire Markets headline. The /markets masthead.

Page: markets. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Canon 52px/64px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `markets-h1-default.png`.

#### markets-cta

Faire Markets headline CTA. The page's main call to action; measured, never followed or pressed.

Page: markets. Selector: `markets CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 47 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.focusable.interactive 47.0x16.0 outline 2px solid #275ec5 offset 1px | = |

Crops: `markets-cta-default.png`, `markets-cta-hover.png`, `markets-cta-focus-visible.png`, `markets-cta-pressed.png`.

#### aff-h1

Affiliates headline. The /affiliates masthead.

Page: affiliates. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 553 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Canon 52px/64px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `aff-h1-default.png`.

#### aff-cta

Affiliates headline CTA. The page's main call to action; measured, never followed or pressed.

Page: affiliates. Selector: `affiliates CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 47 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | GT Standard 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.focusable.interactive 47.0x16.0 outline 2px solid #275ec5 offset 1px | = |

Crops: `aff-cta-default.png`, `aff-cta-hover.png`, `aff-cta-focus-visible.png`, `aff-cta-pressed.png`.

#### news-h1

Newsroom headline. The /news masthead.

Page: news. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 670 x 100 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | nantes 38px/50px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `news-h1-default.png`.

#### careers-h1

Careers headline. The /careers masthead.

Page: careers. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 450 x 150 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | nantes 38px/50px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `careers-h1-default.png`.

#### pos-h1

Point of sale headline. The /point-of-sale/about masthead.

Page: pos. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 456 x 128 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | nantes 52px/64px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `pos-h1-default.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header: Faire mark, Menu button, Sign in.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 51 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #dadada; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.type-fs-paragraph.whitespace-nowrap: Graphik_fix 14px/20px 400, #333333, ls 0.15px |
| Transition | background 0.1s linear |
| Icon | 20 x 20, colour #333333 |
| Painted layers | header.bg-fs-surface-primary.relative 390.0x51.0 bg #ffffff border B:1px solid #dadada; div.bg-fs-surface-primary.relative 390.0x50.0 bg #ffffff; button.interactive.focusable 40.0x21.3 bg #333333 @ 0 r 4px; button.interactive.focusable 40.0x21.3 bg #333333 @ 0 r 4px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-menu-btn

Mobile menu button. The header Menu button that opens the nav drawer — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `mobile Menu button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 52 x 50 | = | = | = | = |
| Padding | 0px 16px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = | = |
| Font | Graphik 16px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #333333 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #333333 | = | = | = | = |
| Ancestor paint | 1 up div.bg-fs-surface-primary.relative bg #ffffff | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.relative.flex 52.0x50.0 outline 1px auto #e59700 offset 0px | = | = |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 317 x 38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nantes_fix 30px/38px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-drawer

Mobile nav drawer. The nav drawer opened by the Menu button; its links were never followed.

Page: mobile. Selector: `mobile nav drawer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 312 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px 4px 4px 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.f_t_base.f_t_color: graphik 14px/20px 200, #ffffff, ls 0.15px |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | div.ReactModal__Content.ReactModal__Content--after-open 312.0x844.0 bg #ffffff r 0px 4px 4px 0px; div.bg-fs-surface-primary-inverse.flex 312.0x157.0 bg #333333; div.h-9.cursor-pointer 272.0x36.0 bg #333333; div.h-9.cursor-pointer 272.0x36.0 bg #333333; div.h-9.cursor-pointer 272.0x36.0 bg #333333 |
| Ancestor paint | 1 up div.ReactModal__Overlay.ReactModal__Overlay--after-open bg #000000 @ 0.5 |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-search-btn

Mobile search button. The unlabelled magnifier icon button in the phone header; measured at rest (opening the search overlay is covered by m-search).

Page: mobile. Selector: `mobile search icon button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 21.34 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #333333 @ 0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik_fix 14px/20px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #333333 | = | = | #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #333333 | = | = | = |
| Painted layers | button.interactive.focusable 40.0x21.3 bg #333333 @ 0 r 4px | = | button.interactive.focusable 40.0x21.3 bg #333333 @ 0 r 4px outline 2px solid #275ec5 offset 1px | = |
| Ancestor paint | 1 up div.bg-fs-surface-primary.relative bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-search-btn-default.png`, `m-search-btn-hover.png`, `m-search-btn-focus-visible.png`, `m-search-btn-pressed.png`.

#### m-search

Mobile search field. The search field inside the overlay the magnifier button opens (a local UI toggle); focused and typed into then cleared — nothing searched.

Page: mobile. Selector: `mobile search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 285.09 x 20 | = | = |
| Padding | 0px 0px 0px 40px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Graphik_fix 14px/20px 400 | = | = |
| Letter spacing | 0.15px | = | = |
| Colour | #333333 | #000000 | #000000 |
| Transition | width, opacity 0.252s, 0.252s, 0.2s cubic-bezier(0.33, 1, 0.68, 1), cubic-bezier(0.33, 1, 0.68, 1), ease-in-out delay 0s, 0s, 0.07s | = | = |
| Cursor | text | = | = |
| Placeholder | #333333 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field | typed "candles", then deleted; nothing sent |

Crops: `m-search-default.png`, `m-search-focused.png`, `m-search-filled.png`.

### Category teaser

#### cat-h1

Category headline. The category page masthead ("Wholesale home decor for your store").

Page: category. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1248 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Canon 38px/50px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `cat-h1-default.png`.

#### cat-filter-btn

All filters button. The filters trigger on the category teaser grid; measured, never opened.

Page: category. Selector: `category "All filters" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #dadada | = | = | 1px solid #000000 |
| Radius | 999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.fs-filter__label: GT Standard 14px/20px 400, #161616 | = | = | span.fs-filter__label: GT Standard 14px/20px 400, #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #161616 | = | = | 16 x 16, colour #000000 |
| Painted layers | button.fs-filter.focusable 112.0x40.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 999px | = | button.fs-filter.focusable 112.0x40.0 bg #ffffff border T:1px solid #dadada / R:1px solid #dadada / B:1px solid #dadada / L:1px solid #dadada r 999px outline 2px solid #275ec5 offset 1px | button.fs-filter.focusable 112.0x40.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cat-filter-btn-default.png`, `cat-filter-btn-hover.png`, `cat-filter-btn-focus-visible.png`, `cat-filter-btn-pressed.png`.

#### product-tile

Product tile. A product card in the teaser grid (photo, name, price); clicking it mounts the sign-up dialog, so it was measured, never followed.

Page: category. Selector: `product tile a:has(img)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 217.33 x 217.33 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `product-tile-default.png`, `product-tile-hover.png`.

#### subcat-card

Subcategory card. A card in the "Explore diverse styles" subcategory grid (thumbnail + label); measured, never followed.

Page: category. Selector: `subcategory card a:has(img)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 324 x 96 | = | = | = |
| Padding | 16px | = | = | = |
| Gap | 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #fbf8f6 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #275ec5 offset 1px | = |
| Font | Graphik 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.type-fs-paragraph-medium.line-clamp-2: GT Standard 14px/20px 500, #161616 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.f_c_visualNavTile.border-fs-border-muted 324.0x96.0 bg #fbf8f6 r 4px; div.firstImageContainer 64.0x64.0 r 4px shadow #000000 @ 0.08 2px 2px 6px 0px; div.imageUnderlay 64.0x64.0 bg #000000 @ 0.02; div.secondImageContainer 58.2x58.2 r 4px shadow #000000 @ 0.08 2px 2px 6px 0px; div.imageUnderlay 58.2x58.2 bg #000000 @ 0.05 | = | a.f_c_visualNavTile.border-fs-border-muted 324.0x96.0 bg #fbf8f6 r 4px outline 2px solid #275ec5 offset 1px; div.firstImageContainer 64.0x64.0 r 4px shadow #000000 @ 0.08 2px 2px 6px 0px; div.imageUnderlay 64.0x64.0 bg #000000 @ 0.02; div.secondImageContainer 58.2x58.2 r 4px shadow #000000 @ 0.08 2px 2px 6px 0px; div.imageUnderlay 58.2x58.2 bg #000000 @ 0.05 | a.f_c_visualNavTile.border-fs-border-muted 324.0x96.0 bg #fbf8f6 r 4px; div.firstImageContainer 67.3x67.3 r 4px shadow #000000 @ 0.08 2px 2px 6px 0px; div.imageUnderlay 67.3x67.3 bg #000000 @ 0.02; div.secondImageContainer 62.5x62.5 r 4px shadow #000000 @ 0.08 2px 2px 6px 0px; div.imageUnderlay 62.5x62.5 bg #000000 @ 0.05 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `subcat-card-default.png`, `subcat-card-hover.png`, `subcat-card-focus-visible.png`, `subcat-card-pressed.png`.

#### wall-field

Sign-up wall email field. The "Business email address" field in the page's sign-up section; focused and typed into then cleared — never submitted.

Page: category. Selector: `email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 322 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GT Standard 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #161616 | #000000 | #000000 |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #161616 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 | #000000 @ 0.5, opacity 1 |
| Ancestor paint | 1 up div.fs-form-field.flex bg #ffffff | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 | 1 up div.fs-form-field.flex bg #ffffff outline 1px solid #000000 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `wall-field-default.png`, `wall-field-focused.png`, `wall-field-filled.png`.

#### brand-tile

Brand link on card. A brand name link inside a product card on the category page; measured, never followed.

Page: category. Selector: `main a[href*=/brand/]`. States: .

Not found on the page at capture time.

## Transitions declared in the readable stylesheets

faire.com serves its CSS cross-origin from cdn.faire.com, so the CSSOM sees only the same-origin inline sheets (toastify, OneTrust, any inline styles); this list holds whatever transitions those readable sheets declare on each page. The per-state Transition rows above are computed values and cover every rule the page paints, including the unreadable cdn.faire.com bundles.

- about: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- affiliates: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- apply: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- brand: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- careers: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- category: none

- home: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- howItWorks: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `opacity 0.2s ease-in-out`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`

- largeRetailers: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- markets: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- news: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- pos: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- signin: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- signup: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- suppliers: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- support: `left 0.3s, width 0.3s`, `color 0.3s`, `0.3s`, `background-image 0.5s linear`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

## Reduced motion

- home (`header .fs-button--primary, button.fs-button--primary` under prefers-reduced-motion): transition `all`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
