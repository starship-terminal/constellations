# Component measurements

Computed styles read from awwwards.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chrome at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme — no vote, submission or login was ever performed and any consent or promo layer was hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The top bar: wordmark, Explore/Directory/Academy/Jobs/Market nav, Log in / Sign Up / Be Pro / Submit Website.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 54 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/28px 300 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.nav-header-main__link: Inter Tight 14px/28px 500, #222222 |
| Transition | none |
| Icon | 0 x 0, colour #222222 |
| Painted layers | div.header-main__overlay 2880.0x1800.0 bg #000000 @ 0.7; div.header-main__container 1336.0x54.0 bg #e9e9e9 r 8px; div.nav-header-main__dropdown 1336.0x0.0 bg #ededed r 0px 0px 8px 8px; span.budget-tag.budget-tag--solid--black 0.0x0.0 bg #222222 r 4px; span.budget-tag.budget-tag--small--solid--black 28.2x16.0 bg #222222 r 4px; span::before.budget-tag.budget-tag--small--solid--black 4pxx8px bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The wordmark link back to /. 

Page: home. Selector: `a.header-main__logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 30 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/28px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| Icon | 30 x 16, colour #222222 |
| Ancestor paint | 1 up div.header-main__container bg #e9e9e9 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. A top-level nav link (Directory). Measured, never followed.

Page: home. Selector: `header a:has-text("Directory")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.67 x 54 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Tight 14px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |
| Painted layers | - | = | a.nav-header-main__link 56.7x54.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### login-link

Log in link. Log in in the site header. Measured, never followed — the click opens nothing headless and no login page exists signed-out.

Page: undefined. Selector: `:text("Log in")`. States: .

Not found on the page at capture time.

#### signup-link

Sign Up link. Sign Up in the site header. Measured, never followed.

Page: undefined. Selector: `:text("Sign Up")`. States: .

Not found on the page at capture time.

#### submit-cta

Submit Website button. The header CTA. Measured, never followed.

Page: home. Selector: `header a[href*="/submit"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.66 x 42 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #222222 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #383838 | = | #383838 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter Tight 14px/42px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | #ffffff | = | #ffffff |
| Transition | color, background, border 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.button--small--outline--rounded 138.7x42.0 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 8px | a.button.button--small--outline--rounded 138.7x42.0 bg #383838 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 8px | = | a.button.button--small--outline--rounded 138.7x42.0 bg #383838 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `submit-cta-default.png`, `submit-cta-hover.png`, `submit-cta-focus-visible.png`, `submit-cta-pressed.png`.

#### bepro-link

Be Pro link. The Be Pro upsell button in the header. Measured, never followed.

Page: home. Selector: `a[href="/pro"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.02 x 42 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #222222 | #383838 | = | #383838 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter Tight 14px/42px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background, border 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.button--small--rounded 80.0x42.0 bg #222222 r 8px | a.button.button--small--rounded 80.0x42.0 bg #383838 r 8px | = | a.button.button--small--rounded 80.0x42.0 bg #383838 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `bepro-link-default.png`, `bepro-link-hover.png`, `bepro-link-focus-visible.png`, `bepro-link-pressed.png`.

### Home

#### sotd-heading

Section heading. "Site of the Day" heading over the first card.

Page: home. Selector: `:has-text("Site of the Day")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1336 x 359.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/28px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span: Inter Tight 14px/28px 400, #222222 |
| Transition | none |
| Painted layers | strong.budget-tag.budget-tag--medium 98.7x23.0 border T:1px solid #222222 @ 0.3 / R:1px solid #222222 @ 0.3 / B:1px solid #222222 @ 0.3 / L:1px solid #222222 @ 0.3 r 4px; strong::before.link-underlined 70.2188pxx2px image linear-gradient(to right, #222222 45%, #222222 @ 0.3 55%); strong::before.link-underlined 110.359pxx2px image linear-gradient(to right, #222222 45%, #222222 @ 0.3 55%) |
| How | at rest |

Crops: `sotd-heading-default.png`.

#### site-card

Site card. A winning-site card: screenshot, title, author and rollover actions.

Page: home. Selector: `ancestor of a.figure-rollover__link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 658 x 493.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 14px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Tight 20.6479px/28px 300 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Transition | all 0.3s ease | = |
| Icon | 14 x 11.89, colour #222222 | = |
| Painted layers | div.figure-rollover__hover 658.0x493.5 image linear-gradient(0deg, #000000 @ 0.5 0%, #000000 @ 0 100%); a.button.button--white--rounded 120.3x47.6 bg #ffffff r 8px | = |
| How | at rest | mouse hover |

Crops: `site-card-default.png`, `site-card-hover.png`.

#### card-cta

Card action. The "Vote Now" button revealed by hovering a site card. Measured, never clicked — voting records a score.

Page: home. Selector: `.figure-rollover__hover a.button`. States: .

Not found on the page at capture time.

### Winners grid

#### grid-title

Grid title. "Winning websites. Web Design Inspiration".

Page: websites. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 305.89 x 18.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/18.2px 600 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| ::after | auto x auto, static, bg #000000 @ 0, radius 2px |
| Painted layers | h1::after.breadcrumb-filters__title autoxauto border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 2px |
| How | at rest |

Crops: `grid-title-default.png`.

#### filter-item

Filter tab. An Awards/Category/Tag/Technology filter tab on the winners grid.

Page: websites. Selector: `.nav-filters__item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 105.78 x 42 | = |
| Padding | 0px 24px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #f8f8f8 | #ffffff |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Tight 13.3px/28px 500 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | span: Inter Tight 13.3px/28px 500, #222222 | = |
| Transition | all 0.3s ease | = |
| Cursor | pointer | = |
| Icon | 8 x 8, colour #222222 | = |
| Painted layers | span.nav-filters__item.js-nav-filters-item 105.8x42.0 bg #f8f8f8 r 8px | span.nav-filters__item.js-nav-filters-item 105.8x42.0 bg #ffffff r 8px |
| How | at rest | mouse hover |

Crops: `filter-item-default.png`, `filter-item-hover.png`.

#### filter-dropdown

Filter dropdown. The open sublist under a filter tab.

Page: websites. Selector: `.nav-filters__dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 280 x 346 |
| Padding | 8px 8px 0px 8px |
| Border | none |
| Radius | 8px |
| Background | #f8f8f8 |
| Box shadow | #000000 @ 0.2 0px 0px 6px 0px |
| Outline | none |
| Font | Inter Tight 13.3px/28px 500 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.js-filter-item-name: Inter Tight 13.3px/28px 500, #222222 |
| Transition | all 0.6s ease |
| Painted layers | div.nav-filters__dropdown 280.0x346.0 bg #f8f8f8 r 8px shadow #000000 @ 0.2 0px 0px 6px 0px; a::before.nav-filters__subitem 12pxx12px border T:1px solid #a7a7a7 / R:1px solid #a7a7a7 / B:1px solid #a7a7a7 / L:1px solid #a7a7a7 r 50%; a::after.nav-filters__subitem 8pxx8px bg #222222 r 50%; a::before.nav-filters__subitem 12pxx12px border T:1px solid #a7a7a7 / R:1px solid #a7a7a7 / B:1px solid #a7a7a7 / L:1px solid #a7a7a7 r 50%; a::after.nav-filters__subitem 8pxx8px bg #222222 r 50%; a::before.nav-filters__subitem 12pxx12px border T:1px solid #a7a7a7 / R:1px solid #a7a7a7 / B:1px solid #a7a7a7 / L:1px solid #a7a7a7 r 50% |
| How | at rest |

Crops: `filter-dropdown-default.png`.

#### filter-option

Filter option. An option row inside the open filter dropdown. Measured, never followed.

Page: websites. Selector: `.nav-filters__subitem`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 264 x 40 | = |
| Padding | 0px 8px 0px 30px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | #ededed |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Tight 13.3px/28px 500 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | span.js-filter-item-name: Inter Tight 13.3px/28px 500, #222222 | = |
| Transition | all 0.3s ease | = |
| Cursor | pointer | = |
| ::before | 12px x 12px, absolute, bg #000000 @ 0, radius 50% | = |
| ::after | 8px x 8px, absolute, bg #222222, radius 50% | = |
| Painted layers | a::before.nav-filters__subitem 12pxx12px border T:1px solid #a7a7a7 / R:1px solid #a7a7a7 / B:1px solid #a7a7a7 / L:1px solid #a7a7a7 r 50%; a::after.nav-filters__subitem 8pxx8px bg #222222 r 50% | a.nav-filters__subitem 264.0x40.0 bg #ededed r 8px; a::before.nav-filters__subitem 12pxx12px border T:1px solid #a7a7a7 / R:1px solid #a7a7a7 / B:1px solid #a7a7a7 / L:1px solid #a7a7a7 r 50%; a::after.nav-filters__subitem 8pxx8px bg #222222 r 50% |
| How | at rest | mouse hover |

Crops: `filter-option-default.png`, `filter-option-hover.png`.

#### grid-card

Grid card. A winning-site card on the winners grid.

Page: websites. Selector: `ancestor of a.figure-rollover__link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 432 x 324 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Tight 15px/28px 300 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Transition | all 0.3s ease | = |
| Icon | 15 x 15, colour #222222, fill #000000 | = |
| Painted layers | div.figure-rollover__hover 432.0x324.0 image linear-gradient(0deg, #000000 @ 0.5 0%, #000000 @ 0 100%) | = |
| How | at rest | mouse hover |

Crops: `grid-card-default.png`, `grid-card-hover.png`.

#### grid-card-link

Grid card link. The card anchor to /sites/<slug>. Measured, never followed.

Page: websites. Selector: `a.figure-rollover__link`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 432 x 324 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 1px |
| Font | Inter Tight 15px/28px 300 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | Shift+Tab, Tab |
| Painted layers | - | a.figure-rollover__link 432.0x324.0 outline 1px auto #005fcc offset 1px |

Crops: `grid-card-link-default.png`, `grid-card-link-focus-visible.png`.

### undefined

#### site_url

Site-detail URL.

Page: site. Selector: ``. States: default.

| Property | default |
|---|---|
| Note | /sites/creative-reference-library |

Crops: none.

### Site detail

#### site-title

Site title.

Page: site. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1336 x 253.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 126.732px/126.732px 600 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | a: Inter Tight 126.732px/126.732px 600, #222222 |
| Transition | none |
| How | at rest |

Crops: `site-title-default.png`.

#### score-box

Score box. The jury score panel (Design/Usability/Creativity/Content).

Page: site. Selector: `.box-score`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 69.38 x 83.72 |
| Padding | 0px |
| Border | 1px solid #222222 |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 13.9718px/13.9718px 300 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | strong: Inter Tight 13.9718px/13.9718px 500, #222222 |
| Transition | none |
| Painted layers | div.box-score 69.4x83.7 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 8px; div.box-score__bottom 67.4x53.8 border T:1px solid #222222 |
| How | at rest |

Crops: `score-box-default.png`.

#### score-note

Score note.

Page: site. Selector: `.box-score__note`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 45.03 x 30.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 13.9718px/13.9718px 300 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | strong: Inter Tight 23.0535px/13.9718px 600, #222222 |
| Transition | none |
| How | at rest |

Crops: `score-note-default.png`.

#### vote-button

Vote button. The vote CTA; measured except a real press — voting records a score and is never clicked.

Page: site. Selector: `.button:has-text("Vote")`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 190.52 x 60 | = | = |
| Padding | 0px 15.6px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #e3c352 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Tight 13px/60px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #222222 | = | = |
| Text node | strong: Inter Tight 13px/60px 600, #222222 | = | = |
| Transition | all 0.3s ease | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.button.button--medium--rounded--awwward 190.5x60.0 bg #e3c352 r 8px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Opacity | - | 0.8 | = |

Crops: `vote-button-default.png`, `vote-button-hover.png`, `vote-button-focus-visible.png`.

#### visit-link

Visit link. The external visit-site toolbar icon; the hover pass found it outside the viewport, so only the at-rest reading stands.

Page: site. Selector: `a.toolbar-bts__item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 20 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/28px 300 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | all 0.3s ease |
| Cursor | pointer |
| Icon | 20 x 20, colour #222222 |
| How | at rest |

Crops: `visit-link-default.png`.

#### tag-chip

Tag chip. A category tag (Art & Illustration…) on the site detail page. Measured, never followed.

Page: site. Selector: `.button--tag`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 179.08 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | 1px solid #a7a7a7 | 1px solid #222222 | = | 1px solid #222222 |
| Radius | 72px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter Tight 18px/28px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | color, background, border 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.button--tag 179.1x48.0 border T:1px solid #a7a7a7 / R:1px solid #a7a7a7 / B:1px solid #a7a7a7 / L:1px solid #a7a7a7 r 72px | a.button.button--tag 179.1x48.0 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 72px | = | a.button.button--tag 179.1x48.0 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 72px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tag-chip-default.png`, `tag-chip-hover.png`, `tag-chip-focus-visible.png`, `tag-chip-pressed.png`.

#### card-action

Card action. A rollover action icon on a related-site card. Measured, never clicked.

Page: undefined. Selector: `.figure-rollover__bt`. States: .

Not found on the page at capture time.

### Collections

#### coll-title

Collections title.

Page: collections. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 99 x 18.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/18.2px 600 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| ::after | auto x auto, static, bg #000000 @ 0, radius 2px |
| Painted layers | h1::after.breadcrumb-filters__title autoxauto border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 2px |
| How | at rest |

Crops: `coll-title-default.png`.

#### coll-card

Collection card. A curated-collection card. Measured, never followed.

Page: collections. Selector: `a[href*="/collections/"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 139.8 x 42 | = |
| Padding | 0px 24px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #f8f8f8 | #ffffff |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Tight 13.3px/28px 500 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | span: Inter Tight 13.3px/28px 500, #222222 | = |
| Transition | all 0.3s ease | = |
| Cursor | pointer | = |
| Icon | 17 x 17, colour #222222 | = |
| Painted layers | a.nav-filters__item 139.8x42.0 bg #f8f8f8 r 8px | a.nav-filters__item 139.8x42.0 bg #ffffff r 8px |
| How | at rest | mouse hover |

Crops: `coll-card-default.png`, `coll-card-hover.png`.

### Submit gate

#### submit-title

Submit title.

Page: submit. Selector: `h1, .heading-5`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 505.11 x 100.53 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 41.8873px/50.2648px 600 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `submit-title-default.png`.

#### submit-cta-2

Submit CTA. The first call-to-action on /submit/. Measured, never followed.

Page: undefined. Selector: `main .button`. States: .

Not found on the page at capture time.

#### plan-card

Plan/pricing card. A submission plan card where the page offers one.

Page: submit. Selector: `[class*="plan"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1336 x 550.91 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/28px 300 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div.plan__title: Inter Tight 29.2958px/38.0845px 600, #222222 |
| Transition | none |
| Icon | 20 x 20, colour #222222 |
| Painted layers | div.plan.plan--standard 432.0x550.9 bg #ffffff r 14px; a.button.button--large--outline--rounded 230.0x72.0 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 r 8px; div.plan.plan--pro 884.0x550.9 bg #222222 r 14px; a.button.button--medium--outline--white--rounded 230.0x60.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 8px; span::before.link-underlined 76.4375pxx2px image linear-gradient(to right, #ffffff 45%, #ffffff @ 0.3 55%); div.plan__right 512.7x550.9 bg #2c2c2c |
| How | at rest |

Crops: `plan-card-default.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 432 x 145 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 15px/28px 300 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | strong: Inter Tight 15px/18px 600, #222222 |
| Transition | none |
| Icon | 20 x 20, colour #222222 |
| Painted layers | div.card-course__row 432.0x60.0 border T:1px solid #f8f8f8 / B:1px solid #f8f8f8; div.box-score__wrap 100.0x4.0 bg #ededed r 4px; div.box-score__bar 98.0x4.0 bg #fff083 |
| Ancestor paint | 1 up div.card-course.card-academy bg #ffffff @ 0.9 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 432 x 90 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Tight 15px/28px 300 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | strong: Inter Tight 13.9718px/13.9718px 600, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222222 | = | = | = |
| Painted layers | div.card-academy__row 432.0x90.0 border T:1px solid #ededed | = | a 432.0x90.0 outline 1px auto #005fcc offset 1px; div.card-academy__row 432.0x90.0 border T:1px solid #ededed | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 54 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f8f8f8 |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/28px 300 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Icon | 16 x 16, colour #222222 |
| Painted layers | header 390.0x54.0 bg #f8f8f8; div.header-main__overlay 0.0x0.0 bg #000000 @ 0.7; div.header-main__container 390.0x54.0 bg #e9e9e9; nav.nav-header-main 390.0x790.0 bg #f8f8f8; li.nav-header-main__item.has-dropdown 390.0x330.0 border B:1px solid #000000 @ 0.3; span.nav-header-main__link 390.0x54.0 bg #000000 @ 0.13 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `header menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 54 x 54 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter Tight 14px/28px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222222 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 16 x 16, colour #222222 | = | - | = |
| ::before | 48px x 54px, absolute, bg #000000 @ 0, radius 0px | = | - | = |
| Ancestor paint | 1 up div.header-main__container bg #e9e9e9 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Error | - | = | keyboard focus did not land on the element | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The menu button after its own toggle; the crop is the open menu layer.

Page: home. Selector: `header menu button`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 54 x 54 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/28px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #222222 |
| ::before | 48px x 54px, absolute, bg #000000 @ 0, radius 0px |
| Ancestor paint | 1 up div.header-main__container bg #f8f8f8 |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. A row inside the opened menu.

Page: home. Selector: `nav a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 54 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 14px/28px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | all 0.3s ease |
| Cursor | pointer |
| Icon | 0 x 0, colour #222222 |
| How | at rest |

Crops: `m-nav-link-default.png`.

#### m-site-card

Mobile site card. A winning-site card on mobile.

Page: home. Selector: `a.figure-rollover__link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 268.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 18px/28px 300 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-site-card-default.png`.

## Transitions declared in the readable stylesheets

awwwards.com serves its stylesheets from www.awwwards.com itself, so the CSSOM could read nearly every rule on each page. The per-state Transition rows above are computed values and cover those rules too.

- home: `0.3s`, `0.6s`, `none`, `opacity 0.3s`, `background 0.3s`, `0.3s ease-in-out`, `color 0.3s, background 0.3s, border 0.3s`, `border 0.3s`, `fill 0.3s`, `0.5s`, `0.3s ease-out`, `0.6s cubic-bezier(0, 1, 0.5, 1)`
