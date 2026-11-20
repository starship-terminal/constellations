# Component measurements

Computed styles read from coinbase.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headed Chromium (Cloudflare gates headless) at 1440 x 900 (the Mobile group at 390 x 844) on the site's light surface (the OneTrust/consent overlays hidden, never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-banner

Promo banner. The announcement row at the top of the header (Banner__StyledLink → /partner/ai-signup-offer) — real chrome, kept.

Page: home. Selector: `header [class*=Banner] first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #0667d0 |
| Text node | span.inline-i1d5xt2g.fg-f1sorag4: CoinbaseSans 16px/24px 600, #11206b |
| Transition | background-color 0.2s ease-in-out |
| Cursor | pointer |
| Ancestor paint | 1 up div.flex-ff5rfy6.zIndex-z1q1xk3b bg #eef0f3 |
| How | at rest |

Crops: `promo-banner-default.png`.

#### header

Nav bar. The fixed site header (data-testid=main-nav): Coinbase logo, mega-menu links, search + language icons, Sign in ghost and the Sign up pill.

Page: home. Selector: `[data-testid=main-nav] [class*=StickyWrapper]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 117 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.inline-i1d5xt2g.fg-f1sorag4: CoinbaseSans 16px/24px 600, #11206b |
| Transition | none |
| Painted layers | div.flex-ff5rfy6.column-c1fk6aoh 1425.0x117.0 bg #ffffff; div.flex-ff5rfy6.zIndex-z1q1xk3b 1425.0x48.0 bg #eef0f3; div.flex-ff5rfy6.borderedBottom-b1oac3bo 1425.0x69.0 border B:1px solid #5b616e @ 0.2; div.flex-ff5rfy6.TrapdoorContentWrapper__Overlay-sc-599674da-1 1425.0x784.0 bg #32353d @ 0.33; section.TrapdoorContentWrapper__Wrapper-sc-599674da-0.jxswtl 1425.0x484.0 bg #ffffff; div.flex-ff5rfy6.SublinkIcon__IconWrapper-sc-b279167c-0 40.0x40.0 bg #eef0f3 r 12px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Coinbase logo home anchor in the nav.

Page: home. Selector: `[data-testid=header-home-link]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 44 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #0667d0 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. A mega-menu nav trigger ("Crypto", data-testid=main-nav-link-prices); its dropdown renders eager in the DOM.

Page: home. Selector: `[data-testid=main-nav-link-prices]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.33 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100000px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | CoinbaseSans 16px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0667d0 | = | = | = |
| Text node | span.inline-i1d5xt2g.fg-f1sorag4: CoinbaseSans 16px/20px 600, #0a0b0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.flex-ff5rfy6._1000-_tqhrr9 101.3x44.0 bg #f7f7f7 @ 0.88 r 100000px | a.GlobalNavLink__StyledLink-sc-1a5db85c-0.jJkJkH 101.3x44.0 r 100000px outline 1px auto #101010 offset 1px | = |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-signin

Nav sign-in. The "Sign in" ghost button linking to login.coinbase.com; measured never followed.

Page: home. Selector: `header a[href*=signin]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100.95 x 44 | = | = | 98.93 x 43.12 |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 56px | = | = | = |
| Background | #eef0f3 | #e5e7ea @ 0.88 | = | #f2f4f6 @ 0.82 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0052ff offset 2px | = |
| Font | CoinbaseSans 16px/18.4px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.inline-block-i1w8afo9.fg-f1sorag4: CoinbaseSans 16px/20px 600, #0a0b0d | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex-ff5rfy6.fgInverse-f1sdlwjn 101.0x44.0 bg #eef0f3 r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 101.0x44.0 bg #e5e7ea @ 0.88 r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 101.0x44.0 bg #eef0f3 r 56px outline 2px solid #0052ff offset 2px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 98.9x43.1 bg #f2f4f6 @ 0.82 r 56px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Nav CTA. The blue "Sign up" CDS pill (cds-Button, bgPrimary) in the nav; links to /signup, never followed.

Page: home. Selector: `header a[href*=signup]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.2 x 44 | = | = | 104.08 x 43.12 |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 56px | = | = | = |
| Background | #0052ff | #0048e0 @ 0.88 | = | #0043d1 @ 0.82 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0052ff offset 2px | = |
| Font | CoinbaseSans 16px/18.4px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.inline-block-i1w8afo9.bgLineInverse-b1qa1j3s: CoinbaseSans 16px/20px 600, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex-ff5rfy6.fgInverse-f1sdlwjn 106.2x44.0 bg #0052ff r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 106.2x44.0 bg #0048e0 @ 0.88 r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 106.2x44.0 bg #0052ff r 56px outline 2px solid #0052ff offset 2px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 104.1x43.1 bg #0043d1 @ 0.82 r 56px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title. "The most trusted crypto exchange" — the hero headline (CoinbaseDisplay scale).

Page: home. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656.5 x 240 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseDisplay 80px/80px 400 |
| Letter spacing | normal |
| Colour | #0a0b0d |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The "Sign up with Singpass" dark pill (cds-Button, bgInverse) under the hero copy; links to /signup, never followed.

Page: home. Selector: `main a[href*=signup]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 256.73 x 56 | = | = | 251.6 x 54.88 |
| Padding | 16px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 56px | = | = | = |
| Background | #0a0b0d | #111214 @ 0.88 | = | #151618 @ 0.82 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0052ff offset 2px | = |
| Font | CoinbaseSans 16px/18.4px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.inline-block-i1w8afo9.fgInverse-f1sdlwjn: CoinbaseSans 18px/24px 600, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex-ff5rfy6.fgInverse-f1sdlwjn 256.7x56.0 bg #0a0b0d r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 256.7x56.0 bg #111214 @ 0.88 r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 256.7x56.0 bg #0a0b0d r 56px outline 2px solid #0052ff offset 2px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 251.6x54.9 bg #151618 @ 0.82 r 56px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### carousel-card

Promo card. A promo-carousel card in the home flow (promo-carousel-item-*, autoplay rotating offers).

Page: home. Selector: `[data-testid^=promo-carousel] first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 724.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #141519 |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.richTextElements__InheritedElement-sc-d7d13d1e-2.richTextElements__StyledH2-sc-d7d13d1e-5: CoinbaseDisplay 52px/52px 400, #ffffff |
| Transition | none |
| Painted layers | div.flex-ff5rfy6.hidden-h147juno 1425.0x724.4 bg #141519; section.flex-ff5rfy6.center-cc1bafw 1425.0x724.4 bg #141519; div.flex-ff5rfy6.relative-rmdk4io 1425.0x724.4 bg #141519; div.flex-ff5rfy6._3-_1d2qff5 1265.0x496.4 bg #0a0b0d r 56px; div.flex-ff5rfy6.bgAlternate-btxvtgs 576.5x432.4 bg #141519 r 56px; a.flex-ff5rfy6.fgInverse-f1sdlwjn 187.6x56.0 bg #ffffff r 56px |
| How | at rest |

Crops: `carousel-card-default.png`.

#### chip

Filter chip. A filter chip inside the dark asset panel on home ("Tradable"/"Top gainers"/"New on Coinbase", data-testid=chip, dark themed).

Page: home. Selector: `[data-testid=chip] first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.03 x 44 | = | = | 114.69 x 43.12 |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 56px | = | = | = |
| Background | #282b31 | #2f3237 @ 0.88 | = | #32353b @ 0.82 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #578bfa offset 2px | = |
| Font | CoinbaseSans 16px/18.4px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0b0d | = | = | = |
| Text node | span.inline-block-i1w8afo9.fg-f1sorag4: CoinbaseSans 16px/20px 600, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Cursor | pointer | = | = | = |
| Painted layers | button.flex-ff5rfy6.fgInverse-f1sdlwjn 117.0x44.0 bg #282b31 r 56px | button.flex-ff5rfy6.fgInverse-f1sdlwjn 117.0x44.0 bg #2f3237 @ 0.88 r 56px | button.flex-ff5rfy6.fgInverse-f1sdlwjn 117.0x44.0 bg #282b31 r 56px outline 2px solid #578bfa offset 2px | button.flex-ff5rfy6.fgInverse-f1sdlwjn 114.7x43.1 bg #32353b @ 0.82 r 56px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `chip-default.png`, `chip-hover.png`, `chip-focus-visible.png`, `chip-pressed.png`.

#### dark-band

Dark panel. The .coinbase.dark themed asset panel on home (the dark Tradable/Top-gainers card) — its paint lands on children; the theme element itself reads transparent.

Page: home. Selector: `.coinbase.dark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656.5 x 640 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.inline-block-i1w8afo9.fg-f1sorag4: CoinbaseSans 16px/20px 600, #ffffff |
| Transition | none |
| Painted layers | div.flex-ff5rfy6.bg-bp7gg31 656.5x640.0 bg #0a0b0d r 40px; div.flex-ff5rfy6.relative-rmdk4io 452.7x44.0 bg #0a0b0d; button.flex-ff5rfy6.fgInverse-f1sdlwjn 117.0x44.0 bg #282b31 r 56px; button.flex-ff5rfy6.fgInverse-f1sdlwjn 138.3x44.0 bg #0a0b0d r 56px; button.flex-ff5rfy6.fgInverse-f1sdlwjn 181.4x44.0 bg #0a0b0d r 56px; a.inline-i1d5xt2g.fgPrimary-f1viahif 592.5x80.0 bg #0a0b0d @ 0 |
| How | at rest |

Crops: `dark-band-default.png`.

#### cta-dark

Dark CTA. The "See more assets" dark pill under the crypto band (fgInverse on bgInverse #0a0b0d, pill radius); links to /explore, never followed.

Page: home. Selector: `main a:has-text("See more assets")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 207.88 x 56 | = | = | 203.72 x 54.88 |
| Padding | 16px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 56px | = | = | = |
| Background | #0a0b0d | #111214 @ 0.88 | = | #151618 @ 0.82 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0052ff offset 2px | = |
| Font | CoinbaseSans 16px/18.4px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.inline-block-i1w8afo9.fgInverse-f1sdlwjn: CoinbaseSans 18px/24px 600, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex-ff5rfy6.fgInverse-f1sdlwjn 207.9x56.0 bg #0a0b0d r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 207.9x56.0 bg #111214 @ 0.88 r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 207.9x56.0 bg #0a0b0d r 56px outline 2px solid #0052ff offset 2px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 203.7x54.9 bg #151618 @ 0.82 r 56px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-dark-default.png`, `cta-dark-hover.png`, `cta-dark-focus-visible.png`, `cta-dark-pressed.png`.

#### section-title

Section title. A display section heading in page content ("Unlock zero trading fees…" style, CoinbaseDisplay scale).

Page: home. Selector: `h2:has-text("Unlock/Explore crypto")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 544 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseDisplay 44px/48px 400 |
| Letter spacing | normal |
| Colour | #0a0b0d |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### page-ground

Page ground. The body element painted fill — the page ground.

Page: home. Selector: `document.body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.inline-i1d5xt2g.fg-f1sorag4: CoinbaseSans 13px/16px 600, #0a0b0d |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.flex-ff5rfy6.column-c1fk6aoh 1425.0x0.0 bg #ffffff; a.inline-i1d5xt2g.fgPrimary-f1viahif 1425.0x36.0 bg #eef0f3; a.inline-i1d5xt2g.fgPrimary-f1viahif 1425.0x36.0 bg #eef0f3; div.flex-ff5rfy6.column-c1fk6aoh 1425.0x117.0 bg #ffffff; div.flex-ff5rfy6.zIndex-z1q1xk3b 1425.0x48.0 bg #eef0f3; div.flex-ff5rfy6.borderedBottom-b1oac3bo 1425.0x69.0 border B:1px solid #5b616e @ 0.2 |
| How | at rest |

Crops: none.

### Explore (prices)

#### explore-title

Explore title. "Explore Crypto" — the prices page headline.

Page: explore. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 194.53 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseDisplay 28px/36px 600 |
| Letter spacing | normal |
| Colour | #0a0b0d |
| Transition | none |
| How | at rest |

Crops: `explore-title-default.png`.

#### explore-search

Asset search field. The asset search input on /explore (input-interactable-area) — a focus reading only; nothing typed.

Page: explore. Selector: `[data-testid=input-interactable-area]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 309 x 42 | = |
| Padding | 0px | = |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 100000px | = |
| Background | #eef0f3 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | CoinbaseSans 16px/18.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | box-shadow 0.2s ease-in-out | = |
| Cursor | pointer | = |
| Painted layers | span.flex-ff5rfy6._100-_x44gs4 309.0x42.0 bg #eef0f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100000px | = |
| How | at rest | clicked into the field |

Crops: `explore-search-default.png`, `explore-search-focused.png`.

#### price-table

Price table. The live crypto price table (data-testid=prices-table-v2) with sortable columns.

Page: explore. Selector: `[data-testid=prices-table-v2]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1002 x 816 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #0a0b0d |
| Text node | div.block-bvmbflj.fgMuted-fqraqpo: CoinbaseSans 16px/24px 600, #5b616e |
| Transition | none |
| Icon | 64 x 32, colour #0a0b0d, fill #000000 |
| Painted layers | table.tableCss-tcfnqih 1002.0x816.0 bg #ffffff; tr.tableRowCss-t1cncu43 1002.0x56.0 bg #ffffff; th.tableCellCss-t1tm00n7.tableHeaderCellCss-tuqbsed 264.0x56.0 bg #ffffff; button.flex-ff5rfy6._100-_x44gs4 264.0x40.0 bg #ffffff @ 0 r 8px; th.tableCellCss-t1tm00n7.tableHeaderCellCss-tuqbsed 142.7x56.0 bg #ffffff; button.flex-ff5rfy6._100-_x44gs4 142.7x40.0 bg #ffffff @ 0 r 8px |
| How | at rest |

Crops: `price-table-default.png`.

#### price-row

Price row. An asset row in the price table (icon, name, price, sparkline, change).

Page: explore. Selector: `[data-testid^=prices-table-v2-row-] first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1002 x 76 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | #f7f8f9 @ 0.35 | #f7f8f9 @ 0.35 | #f7f8f9 @ 0.35 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | CoinbaseSans 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0b0d | = | = | = |
| Text node | span.iconCss-i1t3cbh7.s-s1qkbjwr: CoinbaseIcons 16px/16px 400, #0a0b0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 64 x 32, colour #0a0b0d, fill #000000 | = | = | = |
| Painted layers | tr.tableRowCss-t1cncu43.tableRowHoverCss-tg1utdg 1002.0x76.0 bg #ffffff; a.flex-ff5rfy6.center-cjpujcd 40.0x40.0 bg #ffffff @ 0 r 100000px; a.inline-i1d5xt2g.fgPrimary-f1viahif 96.3x44.0 bg #ffffff @ 0; div.flex-ff5rfy6.relative-rmdk4io 32.0x32.0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 r 100%; a.flex-ff5rfy6.fgInverse-f1sdlwjn 77.0x40.0 bg #0052ff r 40px | tr.tableRowCss-t1cncu43.tableRowHoverCss-tg1utdg 1002.0x76.0 bg #f7f8f9 @ 0.35; a.flex-ff5rfy6.center-cjpujcd 40.0x40.0 bg #ffffff @ 0 r 100000px; a.inline-i1d5xt2g.fgPrimary-f1viahif 96.3x44.0 bg #ffffff @ 0; div.flex-ff5rfy6.relative-rmdk4io 32.0x32.0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 r 100%; a.flex-ff5rfy6.fgInverse-f1sdlwjn 77.0x40.0 bg #0052ff r 40px | tr.tableRowCss-t1cncu43.tableRowHoverCss-tg1utdg 1002.0x76.0 bg #f7f8f9 @ 0.35 outline 1px auto #101010 offset 0px; a.flex-ff5rfy6.center-cjpujcd 40.0x40.0 bg #ffffff @ 0 r 100000px; a.inline-i1d5xt2g.fgPrimary-f1viahif 96.3x44.0 bg #ffffff @ 0; div.flex-ff5rfy6.relative-rmdk4io 32.0x32.0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 r 100%; a.flex-ff5rfy6.fgInverse-f1sdlwjn 77.0x40.0 bg #0052ff r 40px | tr.tableRowCss-t1cncu43.tableRowHoverCss-tg1utdg 1002.0x76.0 bg #f7f8f9 @ 0.35; a.flex-ff5rfy6.center-cjpujcd 40.0x40.0 bg #ffffff @ 0 r 100000px; a.inline-i1d5xt2g.fgPrimary-f1viahif 96.3x44.0 bg #ffffff @ 0; div.flex-ff5rfy6.relative-rmdk4io 32.0x32.0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 r 100%; a.flex-ff5rfy6.fgInverse-f1sdlwjn 77.0x40.0 bg #0052ff r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-row-default.png`, `price-row-hover.png`, `price-row-focus-visible.png`, `price-row-pressed.png`.

#### price-figure

Price figure. A price figure cell in the price table (the "S$132,809.31"-style value).

Page: explore. Selector: `first S$ cell in first price row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 93.3 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0b0d |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `price-figure-default.png`.

#### sort-icon

Sort icon. A sort arrow on a sortable price-table column; measured at rest, never toggled.

Page: explore. Selector: `[data-testid=table-sort-icon-*]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 12 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 700 |
| Letter spacing | normal |
| Colour | #5b616e |
| Text node | span.iconCss-i1t3cbh7.xs-xffinnj: CoinbaseIcons 12px/12px 400, #5b616e |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `sort-icon-default.png`.

### Coinbase One page

#### one-title

Coinbase One title. The Coinbase One subscription page headline.

Page: one. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656.5 x 240 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseDisplay 80px/80px 400 |
| Letter spacing | normal |
| Colour | #0a0b0d |
| Transition | none |
| How | at rest |

Crops: `one-title-default.png`.

#### one-cta

Coinbase One CTA. The first CDS pill CTA on the Coinbase One page; links onward, never followed.

Page: one. Selector: `main cds-Button first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 235.45 x 56 | = | = | 230.74 x 54.88 |
| Padding | 16px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 56px | = | = | = |
| Background | #0052ff | #0048e0 @ 0.88 | = | #0043d1 @ 0.82 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0052ff offset 2px | = |
| Font | CoinbaseSans 16px/18.4px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.inline-block-i1w8afo9.bgLineInverse-b1qa1j3s: CoinbaseSans 18px/24px 600, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex-ff5rfy6.fgInverse-f1sdlwjn 235.5x56.0 bg #0052ff r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 235.5x56.0 bg #0048e0 @ 0.88 r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 235.5x56.0 bg #0052ff r 56px outline 2px solid #0052ff offset 2px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 230.7x54.9 bg #0043d1 @ 0.82 r 56px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `one-cta-default.png`, `one-cta-hover.png`, `one-cta-focus-visible.png`, `one-cta-pressed.png`.

### Prime page

#### prime-title

Prime title. The Coinbase Prime institutional page headline.

Page: prime. Selector: `first visible h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1361 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseDisplay 96px/96px 400 |
| Letter spacing | normal |
| Colour | #0a0b0d |
| Transition | none |
| How | at rest |

Crops: `prime-title-default.png`.

#### prime-cta

Prime CTA. The first CDS pill CTA on the Prime page; links onward, never followed.

Page: prime. Selector: `main cds-Button first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 165.52 x 56 | = | = | 162.21 x 54.88 |
| Padding | 16px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 56px | = | = | = |
| Background | #0a0b0d | #111214 @ 0.88 | = | #151618 @ 0.82 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0052ff offset 2px | = |
| Font | CoinbaseSans 16px/18.4px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.inline-block-i1w8afo9.fgInverse-f1sdlwjn: CoinbaseSans 18px/24px 600, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex-ff5rfy6.fgInverse-f1sdlwjn 165.5x56.0 bg #0a0b0d r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 165.5x56.0 bg #111214 @ 0.88 r 56px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 165.5x56.0 bg #0a0b0d r 56px outline 2px solid #0052ff offset 2px | a.flex-ff5rfy6.fgInverse-f1sdlwjn 162.2x54.9 bg #151618 @ 0.82 r 56px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `prime-cta-default.png`, `prime-cta-hover.png`, `prime-cta-focus-visible.png`, `prime-cta-pressed.png`.

### App sign-in (boundary)

#### signin-card

Sign-in card. The login.coinbase.com sign-in surface the app paints. Measured at rest, never submitted.

Page: signin. Selector: `main/first visible sign-in container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 146 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: CoinbaseSans 16px/24px 600, #ffffff |
| Transition | none |
| Painted layers | span.flex-ff5rfy6._100-_x44gs4 400.0x58.0 bg #ffffff border T:1px solid #5b616e @ 0.66 / R:1px solid #5b616e @ 0.66 / B:1px solid #5b616e @ 0.66 / L:1px solid #5b616e @ 0.66 r 8px; button.flex-ff5rfy6.fgInverse-f1sdlwjn 400.0x56.0 bg #1460ff r 56px |
| How | at rest |

Crops: `signin-card-default.png`.

#### signin-field

Email field. The sign-in email input (data-testid=email-input) — a focus reading only; nothing typed, nothing sent.

Page: signin. Selector: `[data-testid=email-input]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 398 x 56 | = |
| Padding | 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | CoinbaseSans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0b0d | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #5b616e, opacity 1 | = |
| Ancestor paint | 1 up span.flex-ff5rfy6._100-_x44gs4 bg #ffffff | 1 up span.flex-ff5rfy6._100-_x44gs4 bg #f7f7f7 shadow #0052ff 0px 0px 0px 1px |
| How | at rest | clicked into the field |
| Opacity | - | 0.88 |

Crops: `signin-field-default.png`, `signin-field-focused.png`.

#### signin-submit

Continue button. The "Continue" submit on the sign-in card; measured never pressed — it would submit the form.

Page: signin. Selector: `[data-testid=email-submit-button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 56 | = | - | 392 x 54.88 |
| Padding | 16px 32px | = | - | = |
| Border | none | = | - | = |
| Radius | 56px | = | - | = |
| Background | #1460ff | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Times New Roman 16px/normal 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span: CoinbaseSans 16px/24px 600, #ffffff | = | - | = |
| Transition | none | = | - | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | - | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Opacity | 0.5 | = | - | = |
| Cursor | default | = | - | = |
| Painted layers | button.flex-ff5rfy6.fgInverse-f1sdlwjn 400.0x56.0 bg #1460ff r 56px | = | - | button.flex-ff5rfy6.fgInverse-f1sdlwjn 392.0x54.9 bg #1460ff r 56px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `signin-submit-default.png`, `signin-submit-hover.png`, `signin-submit-pressed.png`.

#### signin-oauth

OAuth button. A "Sign in with Google" OAuth row on the sign-in card; measured never pressed.

Page: signin. Selector: `[data-testid=sign-in-with-google]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 58 | = | = | 392 x 56.84 |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #5b616e @ 0.2 | 1px solid #505561 @ 0.2 | = | 1px solid #4b505a @ 0.2 |
| Radius | 56px | = | = | = |
| Background | #ffffff @ 0 | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0052ff offset 2px | = |
| Font | Times New Roman 16px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0b0d | = | = | = |
| Text node | span.inline-i1d5xt2g.fg-f1sorag4: CoinbaseSans 16px/24px 600, #0a0b0d | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0a0b0d | = | = | 19.6 x 19.6, colour #0a0b0d |
| Painted layers | button.flex-ff5rfy6.fg-f1sorag4 400.0x58.0 bg #ffffff @ 0 border T:1px solid #5b616e @ 0.2 / R:1px solid #5b616e @ 0.2 / B:1px solid #5b616e @ 0.2 / L:1px solid #5b616e @ 0.2 r 56px | button.flex-ff5rfy6.fg-f1sorag4 400.0x58.0 border T:1px solid #505561 @ 0.2 / R:1px solid #505561 @ 0.2 / B:1px solid #505561 @ 0.2 / L:1px solid #505561 @ 0.2 r 56px | button.flex-ff5rfy6.fg-f1sorag4 400.0x58.0 bg #ffffff @ 0 border T:1px solid #5b616e @ 0.2 / R:1px solid #5b616e @ 0.2 / B:1px solid #5b616e @ 0.2 / L:1px solid #5b616e @ 0.2 r 56px outline 2px solid #0052ff offset 2px | button.flex-ff5rfy6.fg-f1sorag4 392.0x56.8 border T:1px solid #4b505a @ 0.2 / R:1px solid #4b505a @ 0.2 / B:1px solid #4b505a @ 0.2 / L:1px solid #4b505a @ 0.2 r 56px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-oauth-default.png`, `signin-oauth-hover.png`, `signin-oauth-focus-visible.png`, `signin-oauth-pressed.png`.

#### signin-passkey

Passkey button. The "Sign in with passkey" row on the sign-in card; measured never pressed.

Page: signin. Selector: `[data-testid=sign-in-with-passkey]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 58 | = | = | 392 x 56.84 |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #5b616e @ 0.2 | 1px solid #505561 @ 0.2 | = | 1px solid #4b505a @ 0.2 |
| Radius | 56px | = | = | = |
| Background | #ffffff @ 0 | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0052ff offset 2px | = |
| Font | Times New Roman 16px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0b0d | = | = | = |
| Text node | span.iconCss-i1t3cbh7.m-mvegnts: CoinbaseIcons 20px/20px 400, #0a0b0d | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |
| Cursor | pointer | = | = | = |
| Painted layers | button.flex-ff5rfy6.fg-f1sorag4 400.0x58.0 bg #ffffff @ 0 border T:1px solid #5b616e @ 0.2 / R:1px solid #5b616e @ 0.2 / B:1px solid #5b616e @ 0.2 / L:1px solid #5b616e @ 0.2 r 56px | button.flex-ff5rfy6.fg-f1sorag4 400.0x58.0 border T:1px solid #505561 @ 0.2 / R:1px solid #505561 @ 0.2 / B:1px solid #505561 @ 0.2 / L:1px solid #505561 @ 0.2 r 56px | button.flex-ff5rfy6.fg-f1sorag4 400.0x58.0 bg #ffffff @ 0 border T:1px solid #5b616e @ 0.2 / R:1px solid #5b616e @ 0.2 / B:1px solid #5b616e @ 0.2 / L:1px solid #5b616e @ 0.2 r 56px outline 2px solid #0052ff offset 2px | button.flex-ff5rfy6.fg-f1sorag4 392.0x56.8 border T:1px solid #4b505a @ 0.2 / R:1px solid #4b505a @ 0.2 / B:1px solid #4b505a @ 0.2 / L:1px solid #4b505a @ 0.2 r 56px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-passkey-default.png`, `signin-passkey-hover.png`, `signin-passkey-focus-visible.png`, `signin-passkey-pressed.png`.

### Footer

#### footer

Footer. The site footer: link columns (Company/Individuals/Businesses/Institutions/Developers/Support), social icons, region selector and the legal row.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 1230 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.iconCss-i1t3cbh7.l-lc7jme9: CoinbaseIcons 64px/64px 400, #0052ff |
| Transition | none |
| Painted layers | section.flex-ff5rfy6.center-cc1bafw 1425.0x1230.0 bg #eef0f3; div.flex-ff5rfy6.relative-rmdk4io 1425.0x1230.0 bg #eef0f3; hr.flex-ff5rfy6.bgLine-b1adt9t6 1361.0x1.0 bg #5b616e @ 0.2; a.inline-i1d5xt2g.fgMuted-fqraqpo 58.4x20.0 bg #ffffff @ 0; a.inline-i1d5xt2g.fgMuted-fqraqpo 155.7x20.0 bg #ffffff @ 0; button.flex-ff5rfy6.center-cjpujcd 26.0x26.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| Ancestor paint | 1 up div.block-bvmbflj.zIndex-z1q1xk3b bg #eef0f3 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A link in a footer link column.

Page: home. Selector: `footer a first visible`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48.52 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | CoinbaseText 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5b616e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.CDSFooterLink__Link-sc-9ac24f85-0.jAlaFt 48.5x24.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link. A footer social icon anchor (X/LinkedIn/Instagram).

Page: home. Selector: `footer a[href*=x/linkedin/instagram]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 27 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | CoinbaseText 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0b0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.CDSFooterLink__Link-sc-9ac24f85-0.jAlaFt 16.0x27.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-region

Region selector. The "Language and region" pair in the footer (Singapore / English selectors) — the enclosing control cluster.

Page: home. Selector: `parent of footer button:has-text("Singapore")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 201.75 x 26 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.iconCss-i1t3cbh7.m-mvegnts: CoinbaseIcons 24px/24px 400, #5b616e |
| Transition | none |
| Painted layers | button.flex-ff5rfy6.center-cjpujcd 26.0x26.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0; button.flex-ff5rfy6.center-cjpujcd 83.1x26.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0; button.flex-ff5rfy6.center-cjpujcd 61.4x26.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest |

Crops: `footer-region-default.png`.

### Mobile (390 wide)

#### m-header

Mobile bar. The 390 mobile nav bar (data-testid=mobile-nav): logo, search, language and menu toggle.

Page: home. Selector: `[data-testid=mobile-nav] inner bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 129 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #ffffff 0px -1px 0px 1px |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.richTextElements__InheritedElement-sc-d7d13d1e-2.richTextElements__StyledP-sc-d7d13d1e-3: CoinbaseSans 13px/16px 600, #0a0b0d |
| Transition | none |
| Painted layers | div.flex-ff5rfy6.MobileNav__StickyWrapper-sc-113ae5f-1 390.0x129.0 shadow #ffffff 0px -1px 0px 1px; div.flex-ff5rfy6.zIndex-z1q1xk3b 390.0x57.0 bg #ffffff border B:1px solid #5b616e @ 0.2; a.GlobalNavLink__StyledLink-sc-1a5db85c-0.jJkJkH 390.0x56.0 bg #f7f7f7 @ 0.88; div.flex-ff5rfy6._1-_4wf66 390.0x72.0 bg #ffffff border B:1px solid #5b616e @ 0.2; button.flex-ff5rfy6.fgInverse-f1sdlwjn 44.0x47.0 bg #eef0f3 r 56px; button.flex-ff5rfy6.fgInverse-f1sdlwjn 0.0x0.0 bg #eef0f3 r 56px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger (data-testid=mobile-menu-toggle, aria-label "open navigation menu"); its own press opens the menu.

Page: home. Selector: `[data-testid=mobile-menu-toggle]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 44 x 47 |
| Padding | 0px |
| Border | none |
| Radius | 56px |
| Background | #eef0f3 |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.iconCss-i1t3cbh7.m-mvegnts: CoinbaseIcons 20px/20px 400, #0a0b0d |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | pointer |
| Painted layers | button.flex-ff5rfy6.fgInverse-f1sdlwjn 44.0x47.0 bg #eef0f3 r 56px |
| Ancestor paint | 3 up div.flex-ff5rfy6.MobileNav__StickyWrapper-sc-113ae5f-1 shadow #ffffff 0px -1px 0px 1px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The menu overlay after the hamburger press.

Page: home. Selector: `opened mobile menu overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 715 |
| Padding | 32px 4px 0px 4px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseSans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.inline-i1d5xt2g.fg-f1sorag4: CoinbaseSans 24px/28px 400, #0a0b0d |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | div.flex-ff5rfy6._0_5-_14pg5wn 390.0x715.0 bg #ffffff; button.flex-ff5rfy6.fgInverse-f1sdlwjn 44.0x44.0 bg #eef0f3 r 56px; a.flex-ff5rfy6.fgInverse-f1sdlwjn 101.0x44.0 bg #eef0f3 r 56px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-link

Menu link. A link/accordion row inside the open mobile menu.

Page: home. Selector: `first row inside the open menu`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 382 x 56 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | #f7f7f7 @ 0.88 | #f7f7f7 @ 0.88 | #f7f7f7 @ 0.88 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | CoinbaseSans 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0667d0 | = | = | = |
| Text node | span.inline-i1d5xt2g.fg-f1sorag4: CoinbaseSans 24px/28px 400, #0a0b0d | = | = | = |
| Transition | background-color 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.GlobalNavLink__StyledLink-sc-1a5db85c-0.jJkJkH 382.0x56.0 bg #f7f7f7 @ 0.88 r 16px | a.GlobalNavLink__StyledLink-sc-1a5db85c-0.jJkJkH 382.0x56.0 bg #f7f7f7 @ 0.88 r 16px outline 1px auto #e59700 offset 1px | a.GlobalNavLink__StyledLink-sc-1a5db85c-0.jJkJkH 382.0x56.0 bg #f7f7f7 @ 0.88 r 16px |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile headline. The hero headline at 390.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 156 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CoinbaseDisplay 52px/52px 400 |
| Letter spacing | normal |
| Colour | #0a0b0d |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `fill 0.15s ease-in-out`, `box-shadow 0.2s ease-in-out`, `background-color ease-in-out 5000s`, `background 0.15s cubic-bezier(0.6, 0, 0.15, 1)`, `border-color, background-color 0.2s linear`, `text-decoration-color 200ms ease-in-out`, `background-color 200ms ease-in-out`, `background-color 0.2s ease-in-out`, `opacity 200ms ease-in-out`, `opacity 0.2s ease-in, visibility`, `0.2s cubic-bezier(0.33, 0, 0, 1)`, `transform 0.3s ease-in-out`
