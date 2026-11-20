# District component measurements

Computed styles read from district.in on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the home feed (/), the listing pages (/movies/, /events/, /events/comedy), an artist page, a ticket page and a forced html[data-theme=dark] pass — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### App chrome

#### nv-bar

Top nav. The fixed app bar — District mark, category tabs, search and location.

Page: home. Selector: `header w/ category links`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 75 |
| Padding | 8px 0px 12px 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.08; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | BeVietnamPro 16px/24px 400 |
| Letter spacing | normal |
| Colour | #131316 |
| Text node | span.dds-text-primary.dds-text-lg: BeVietnamPro 16px/24px 600, #131316 |
| Transition | none |
| Icon | 32 x 32, colour #6444e4 |
| Painted layers | div.dds-w-full.dds-bg-primary 1440.0x75.0 bg #ffffff border B:1px solid #000000 @ 0.08 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.dds-ml-3.5.dds-mr-2 1.4x30.0 bg #d1d5db; button.dds-flex.dds-items-center 200.0x52.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 84.0x36.0 bg #eae5ff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 84.0x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 84.0x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `nv-bar-default.png`.

#### nv-mark

District mark. The District logo link in the top nav; measured, never followed.

Page: home. Selector: `logo link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 108 x 43.63 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | BeVietnamPro 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #131316 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nv-mark-default.png`, `nv-mark-hover.png`, `nv-mark-focus-visible.png`, `nv-mark-pressed.png`.

#### nv-tab

Category tab. The Movies tab in the top category row — a real link; measured, never followed.

Page: home. Selector: `a[href=/movies/]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 36 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | BeVietnamPro 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #545459 | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #545459 | = | = | = |
| Painted layers | a.md:dds-px-2.dds-py-2 84.0x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nv-tab-default.png`, `nv-tab-hover.png`, `nv-tab-focus-visible.png`, `nv-tab-pressed.png`.

#### nv-tab-active

Category tab (For you). The "For you" home tab — the selected state of the category row.

Page: home. Selector: `For you tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 36 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #eae5ff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | BeVietnamPro 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #231268 | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #231268 | = | = | = |
| Painted layers | a.md:dds-px-2.dds-py-2 84.0x36.0 bg #eae5ff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nv-tab-active-default.png`, `nv-tab-active-hover.png`, `nv-tab-active-focus-visible.png`, `nv-tab-active-pressed.png`.

#### nv-search

Search field. The search affordance linking to /search; hover/focus measured, never followed.

Page: home. Selector: `search link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | BeVietnamPro 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #131316 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #6444e4 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nv-search-default.png`, `nv-search-hover.png`, `nv-search-focus-visible.png`, `nv-search-pressed.png`.

#### ft-bar

Site footer. The District sitemap footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 410.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #1e1e20 |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.dds-text-[14px].dds-font-semibold: BeVietnamPro 14px/21px 600, #eaeaeb |
| Transition | none |
| Icon | 79.56 x 32, colour #ffffff, fill #f2ebe3 |
| Painted layers | footer.dds-relative.dds-w-full 1440.0x410.5 bg #1e1e20; a.dds-hidden.dds-flex-row 231.1x122.5 bg #282828 border T:1px solid #3a3a3f / R:1px solid #3a3a3f / B:1px solid #3a3a3f / L:1px solid #3a3a3f r 12px; div.dds-border-t.dds-border-solid 1376.0x1.0 border T:1px solid #33333a |
| How | at rest |

Crops: `ft-bar-default.png`.

### Home feed

#### hm-h1

Page heading. The home feed heading.

Page: home. Selector: `feed heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 263 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 24px/20px 600 |
| Letter spacing | normal |
| Colour | #131316 |
| Transition | none |
| How | at rest |

Crops: `hm-h1-default.png`.

#### hm-section

Section heading. A feed section heading (artists / movies / events rail).

Page: home. Selector: `section heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 314 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 24px/20px 600 |
| Letter spacing | normal |
| Colour | #131316 |
| Transition | none |
| How | at rest |

Crops: `hm-section-default.png`.

### Content cards

#### mc-card

Movie card. A movie card — poster art, title, certificate and language; hover measured, never followed.

Page: home. Selector: `a[href*=movie-tickets-]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 197.33 x 348.45 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | BeVietnamPro 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #131316 | = |
| Text node | h5.dds-tracking-tight.dds-text-lg: BeVietnamPro 16px/22px 600, #131316, ls -0.4px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.sm:dds-mx-[0px].dds-min-h-[282px] 197.3x348.5 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 16px | = |
| How | at rest | mouse hover |

Crops: `mc-card-default.png`, `mc-card-hover.png`.

#### mc-title

Movie title. The title line inside a movie card.

Page: home. Selector: `card title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 77.81 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 16px/22px 600 |
| Letter spacing | -0.4px |
| Colour | #131316 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `mc-title-default.png`.

#### ar-card

Artist card. An artist card in the circular headshot rail (Samay Raina, ALAN WALKER…); hover measured, never followed.

Page: home. Selector: `a[href*=/artist]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 190 x 222 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | BeVietnamPro 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #131316 | = |
| Text node | h5.dds-tracking-tight.dds-text-lg: BeVietnamPro 16px/24px 600, #131316, ls -0.4px | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `ar-card-default.png`, `ar-card-hover.png`.

#### ev-card

Event card. An event card with date and venue; hover measured, never followed.

Page: home. Selector: `a[href$=/venue-guide]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 236 x 325 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | BeVietnamPro 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #131316 | = |
| Text node | span.dds-text-inverse.dds-text-lg: BeVietnamPro 18px/28px 600, #f7f7f7 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.dds-relative.dds-overflow-hidden 236.0x325.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 24px; div.dds-absolute.dds-inset-0 234.0x323.0 image linear-gradient(to top, #000000 @ 0.92 0%, #000000 @ 0.6 45%, #000000 @ 0 100%); div.dds-flex.dds-flex-col 210.0x89.0 border T:1px solid #f7f7f7 @ 0.2 | = |
| How | at rest | mouse hover |

Crops: `ev-card-default.png`, `ev-card-hover.png`.

#### mv-card

Listing movie card. A movie card on the listing grid; hover measured, never followed.

Page: movies. Selector: `a[href*=movie-tickets-MV]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 197.33 x 348.44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | BeVietnamPro 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #131316 | = |
| Text node | h5.dds-tracking-tight.dds-text-lg: BeVietnamPro 16px/22px 600, #131316, ls -0.4px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.sm:dds-mx-[0px].dds-min-h-[282px] 197.3x348.4 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 16px | = |
| How | at rest | mouse hover |

Crops: `mv-card-default.png`, `mv-card-hover.png`.

#### mv-cert

Certificate badge. The censor-certificate chip on a movie card (U / UA13+ / A).

Page: movies. Selector: `cert chip`. States: .

Not found on the page at capture time.

#### ev-listcard

Listing event card. An event card on the listing; hover measured, never followed.

Page: events. Selector: `a[href$=/venue-guide]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 236 x 325 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | BeVietnamPro 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #131316 | = |
| Text node | span.dds-text-inverse.dds-text-lg: BeVietnamPro 18px/28px 600, #f7f7f7 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.dds-relative.dds-overflow-hidden 236.0x325.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 24px; div.dds-absolute.dds-inset-0 234.0x323.0 image linear-gradient(to top, #000000 @ 0.92 0%, #000000 @ 0.6 45%, #000000 @ 0 100%); div.dds-flex.dds-flex-col 210.0x89.0 border T:1px solid #f7f7f7 @ 0.2 | = |
| How | at rest | mouse hover |

Crops: `ev-listcard-default.png`, `ev-listcard-hover.png`.

#### ev-price

Event price. A "₹1499 onwards" price line on an event card.

Page: events. Selector: `price text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 16px/24px 700 |
| Letter spacing | normal |
| Colour | #131316 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `ev-price-default.png`.

### Dark theme (data-theme=dark)

#### dk-body

Dark body. The page background with data-theme=dark applied — the real dark surface the DDS declares.

Page: homeDark. Selector: `body[data-theme=dark]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 4254.58 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #131316 |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f7f7f7 |
| Text node | span.dds-text-primary.dds-text-lg: BeVietnamPro 16px/24px 600, #f7f7f7 |
| Transition | none |
| Icon | 32 x 32, colour #6444e4 |
| Painted layers | body.hideScroll.body4 1440.0x4254.6 bg #131316; main.flex.w-screen 1440.0x4254.6 image linear-gradient(#eae5ff 0px, #ffffff 400px); div.dds-w-full.dds-bg-primary 1440.0x75.0 bg #131316 border B:1px solid #ffffff @ 0.08 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.dds-ml-3.5.dds-mr-2 1.4x30.0 bg #d1d5db; button.dds-flex.dds-items-center 200.0x52.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 84.0x36.0 bg #eae5ff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### dk-nav

Dark nav. The top nav under the dark theme.

Page: homeDark. Selector: `dark header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 75 |
| Padding | 8px 0px 12px 0px |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.08; L: none |
| Radius | 0px |
| Background | #131316 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | BeVietnamPro 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f7f7f7 |
| Text node | span.dds-text-primary.dds-text-lg: BeVietnamPro 16px/24px 600, #f7f7f7 |
| Transition | none |
| Icon | 32 x 32, colour #6444e4 |
| Painted layers | div.dds-w-full.dds-bg-primary 1440.0x75.0 bg #131316 border B:1px solid #ffffff @ 0.08 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.dds-ml-3.5.dds-mr-2 1.4x30.0 bg #d1d5db; button.dds-flex.dds-items-center 200.0x52.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 84.0x36.0 bg #eae5ff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 84.0x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 84.0x36.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `dk-nav-default.png`.

#### dk-card

Dark card. A content card under the dark theme.

Page: homeDark. Selector: `dark card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 197.33 x 348.45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f7f7f7 |
| Text node | h5.dds-tracking-tight.dds-text-lg: BeVietnamPro 16px/22px 600, #f7f7f7, ls -0.4px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.sm:dds-mx-[0px].dds-min-h-[282px] 197.3x348.5 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 16px |
| How | at rest |

Crops: `dk-card-default.png`.

### Listing page

#### mv-h1

Movies heading. The "Movies in <city>" listing heading.

Page: movies. Selector: `movies h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 40px/60px 700 |
| Letter spacing | -1px |
| Colour | #131316 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `mv-h1-default.png`.

#### mv-chip

Filter chip. A language/format filter chip on the listing; measured, never toggled.

Page: movies. Selector: `filter chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 32 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #000000 @ 0.24 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | BeVietnamPro 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #131316 | = | = | = |
| Text node | span.dds-text-primary.dds-text-sm: BeVietnamPro 12px/16px 500, #131316 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.dds-flex.dds-items-center 56.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.24 / R:1px solid #000000 @ 0.24 / B:1px solid #000000 @ 0.24 / L:1px solid #000000 @ 0.24 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | button.dds-flex.dds-items-center 56.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.24 / R:1px solid #000000 @ 0.24 / B:1px solid #000000 @ 0.24 / L:1px solid #000000 @ 0.24 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mv-chip-default.png`, `mv-chip-hover.png`, `mv-chip-focus-visible.png`, `mv-chip-pressed.png`.

#### ev-h1

Events heading. The events listing heading.

Page: events. Selector: `events h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 40px/60px 700 |
| Letter spacing | -1px |
| Colour | #131316 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `ev-h1-default.png`.

#### cm-h1

Comedy heading. The comedy events listing heading.

Page: comedy. Selector: `comedy h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 626.94 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 40px/60px 700 |
| Letter spacing | -1px |
| Colour | #131316 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `cm-h1-default.png`.

#### cm-filter

Filter control. A listing filter control; measured, never opened.

Page: comedy. Selector: `filter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 632 x 500 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ui-sans-serif 14px/21px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.dds-text-sm.dds-font-semibold: ui-sans-serif 12px/20px 600, #131316 | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.dds-flex.dds-flex-col 132.0x52.0 bg #f1f1f2; div::after.dds-flex.dds-flex-col 132pxx52px image linear-gradient(to right, #d5ccff -70%, #000000 @ 0); div.dds-bg-surface-secondary.dds-flex 500.0x500.0 bg #f1f1f2 r 0px 20px 20px 0px; input 0.0x0.0 bg #ffffff border T:1px solid #000000 @ 0.24 / R:1px solid #000000 @ 0.24 / B:1px solid #000000 @ 0.24 / L:1px solid #000000 @ 0.24 r 100%; label::before 20pxx20px border T:2px solid #2c2c2e / R:2px solid #2c2c2e / B:2px solid #2c2c2e / L:2px solid #2c2c2e r 50%; label::after 10pxx10px bg #ffffff r 50% | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `cm-filter-default.png`, `cm-filter-hover.png`, `cm-filter-focus-visible.png`, `cm-filter-pressed.png`.

### Event / artist detail

#### at-h1

Artist name. The artist page display name.

Page: artist. Selector: `artist h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350.58 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 32px/40px 700 |
| Letter spacing | normal |
| Colour | #131316 |
| Transition | none |
| How | at rest |

Crops: `at-h1-default.png`.

#### at-show

Show card. An upcoming-show card on the artist page; hover measured, never followed.

Page: artist. Selector: `show card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 296 x 544 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ui-sans-serif 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.dds-text-primary.dds-text-lg: ui-sans-serif 16px/24px 400, #131316 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.dds-min-w-[268px].md:dds-min-w-[296px] 296.0x544.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 16px; div.dds-absolute.dds-px-3 88.3x36.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 7px shadow #000000 @ 0.25 0px 4px 4px 0px | = |
| How | at rest | mouse hover |

Crops: `at-show-default.png`, `at-show-hover.png`.

#### at-book

Book CTA. The booking link on the artist page — the show card itself navigates to the ticket page; measured at every paintable state, never followed — booking gates on the Zomato account.

Page: artist. Selector: `booking card-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 296 x 544 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.dds-text-primary.dds-text-lg: ui-sans-serif 16px/24px 400, #131316 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.dds-min-w-[268px].md:dds-min-w-[296px] 296.0x544.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 16px; div.dds-absolute.dds-px-3 88.3x36.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 7px shadow #000000 @ 0.25 0px 4px 4px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `at-book-default.png`, `at-book-hover.png`, `at-book-focus-visible.png`, `at-book-pressed.png`.

#### tk-h1

Event title. The event detail title on the ticket page.

Page: tickets. Selector: `ticket h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 169.13 x 38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 28px/normal 700 |
| Letter spacing | -0.7px |
| Colour | #131316 |
| Transition | none |
| How | at rest |

Crops: `tk-h1-default.png`.

#### tk-date

Date pill. A date/time selector pill; measured, never confirmed.

Page: tickets. Selector: `date pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 162.13 x 20 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ui-sans-serif 16px/20px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #6d49fd | = | - | = |
| Transition | none | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `tk-date-default.png`, `tk-date-hover.png`, `tk-date-focus-visible.png`, `tk-date-pressed.png`.

#### tk-price

Ticket price. The ticket price line.

Page: tickets. Selector: `price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 41.19 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 18px/20px 700 |
| Letter spacing | normal |
| Colour | #131316 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `tk-price-default.png`.

#### tk-book

Book button. The primary Book/Proceed CTA; hover/focus measured, never pressed — payment gates on the Zomato account.

Page: tickets. Selector: `Book CTA`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 162.97 x 52 | = | = |
| Padding | 4px 32px | = | = |
| Gap | 0px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | #131316 | #1e1e20 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | ui-sans-serif 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | span.dds-text-inverse.dds-text-lg: ui-sans-serif 16px/24px 600, #ffffff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.dds-flex.dds-items-center 163.0x52.0 bg #131316 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.dds-flex.dds-items-center 163.0x52.0 bg #1e1e20 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.dds-flex.dds-items-center 163.0x52.0 bg #131316 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #101010 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `tk-book-default.png`, `tk-book-hover.png`, `tk-book-focus-visible.png`.

### Mobile (390 wide)

#### m-bar

Mobile nav. The phone app bar at 390px.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 8px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | BeVietnamPro 14px/21px 400 |
| Letter spacing | normal |
| Colour | #131316 |
| Text node | span.dds-text-primary.dds-text-lg: BeVietnamPro 16px/24px 600, #131316 |
| Transition | none |
| Icon | 32 x 32, colour #6444e4 |
| Painted layers | div.dds-w-full.dds-bg-primary 390.0x60.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.dds-ml-3.5.dds-mr-2 0.0x0.0 bg #d1d5db; button.dds-flex.dds-items-center 200.0x52.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 0.0x0.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 0.0x0.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.md:dds-px-2.dds-py-2 0.0x0.0 bg #e2f1fe r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `m-bar-default.png`.

#### m-tab

Mobile tab. A category tab at 390px.

Page: mobile. Selector: `mobile tab`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 84 x 60 |
| Padding | 8px |
| Gap | 4px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | BeVietnamPro 14px/20px 600 |
| Letter spacing | normal |
| Colour | #545459 |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 20 x 20, colour #545459 |
| Painted layers | a.md:dds-px-2.dds-py-2 84.0x60.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 3 up div.dds-sticky.dds-left-0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `m-tab-default.png`.

#### m-card

Mobile card. A content card at 390px.

Page: mobile. Selector: `mobile card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 364 x 271.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BeVietnamPro 14px/21px 400 |
| Letter spacing | normal |
| Colour | #131316 |
| Text node | span.dds-text-lg.dds-font-semibold: BeVietnamPro 16px/24px 600, #131316 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-card-default.png`.

## Transitions declared in the readable stylesheets

district.in serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- artist: none

- comedy: none

- events: none

- home: none

- homeDark: none

- movies: none

- tickets: none
