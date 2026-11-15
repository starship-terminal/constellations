# Component measurements

Computed styles read from foodnoms.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844, the Dark group at 1440 x 900 under emulated prefers-color-scheme: dark — the site's own media rule, the same theme a dark-system visitor gets), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### App shell and navigation

#### nav-bar

Marketing header row. The top bar: app icon + Foodnoms name, News/Foodnoms+/Help links and the "Get the App" primary pill.

Page: home. Selector: `[data-framer-name="Desktop"] (header)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 40 |
| Padding | 0px |
| Gap | 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.framer-text: Aquawax Pro Bold 24px/24px 700, color(display-p3 0.972549 0.384314 0.180392) |
| Transition | none |
| Painted layers | a.framer-5UbMV.framer-OHnkM 145.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-logo

Logo. The Foodnoms app-icon + wordmark in the header; links home.

Page: home. Selector: `a[aria-label="Foodnoms home"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 166 x 36 |
| Padding | 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | div.framer-text: Aquawax Pro Bold 24px/24px 700, color(display-p3 0.972549 0.384314 0.180392) |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-link

Nav link. A header link (News / Foodnoms+ / Help); measured, never followed.

Page: home. Selector: `header nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 38 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Aquawax Pro Medium 15px/15px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 0.4 0.4 0.4) | color(display-p3 0.984314 0.631373 0.509804) | = | color(display-p3 0.984314 0.631373 0.509804) |
| Transition | color 0.4s cubic-bezier(0.44, 0, 0.56, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-277bjg 38.0x18.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-cta

Get-the-App pill. The orange "Get the App ↗" primary pill in the header; an App-Store link, measured never followed.

Page: home. Selector: `a[data-framer-name="Primary"] "Get the App"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.972549 0.384 0.18) | color(display-p3 0.984314 0.631373 0.509804) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 1 1 1) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-5UbMV.framer-OHnkM 145.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px | a.framer-5UbMV.framer-OHnkM 145.0x40.0 bg color(display-p3 0.984314 0.631373 0.509804) r 20px | a.framer-5UbMV.framer-OHnkM 145.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-ticker

Hero headline ticker. The rotating benefit headline ("Track Nutrition", "Lose Weight", "Eat Healthy", …). The semantic h1 is visually hidden; this Title container is the painted display text.

Page: home. Selector: `[data-framer-name="Hero"] [data-framer-name="Title"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 411 x 133.59 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.framer-text.framer-styles-preset-17m3dyy: Aquawax Pro Bold 56px/61.6px 700, color(display-p3 0.972549 0.384314 0.180392) |
| Transition | none |
| Painted layers | button 0.0x0.0 bg #000000 @ 0.2 r 40px; button 0.0x0.0 bg #000000 @ 0.2 r 40px |
| How | at rest |

Crops: `hero-ticker-default.png`.

#### hero-lede

Hero lede. "A simple, clear nutrition tracker for building healthier habits." — the intro paragraph under the ticker.

Page: home. Selector: `hero [data-framer-name="Paragraph"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 28.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-uaxznt: Aquawax Pro Medium 18px/28.8px 500, color(display-p3 0.4 0.4 0.4) |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### hero-icon-btn

Hero icon button. The circular icon button beside the hero headline (a Framer "Button" component with an inline svg).

Page: home. Selector: `a[data-framer-name="Button"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 120 x 40, colour #0000ee, fill #000000 | = | = | 120 x 40, colour #ff0000, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-hseoqs.framer-lux5qc 120.0x40.0 outline 1px auto #101010 offset 1px | = |

Crops: `hero-icon-btn-default.png`, `hero-icon-btn-hover.png`, `hero-icon-btn-focus-visible.png`, `hero-icon-btn-pressed.png`.

#### goal-pill

Goal pill. A nutrition-goal chip in the benefits marquee (Weight, Healthy, Sugars, Water, Sodium, Muscle, Alcohol, Caffeine).

Page: home. Selector: `[data-framer-name="Weight"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 411 x 72 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Opacity | 0.6 |
| How | at rest |

Crops: `goal-pill-default.png`.

#### featured-title

As-Featured-By label. The "As Featured By" caption over the press-logo strip.

Page: home. Selector: `hero Trailing Title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 30.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.framer-text.framer-styles-preset-ishzqq: Aquawax Pro Bold 22px/30.8px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `featured-title-default.png`.

#### featured-logo

Press logo. One outlet logo in the "As Featured By" strip (MacStories, iMore, 9to5Mac, PopSugar, Good Housekeeping, Prevention).

Page: home. Selector: `[aria-label^="Featured in"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 128 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 128 x 32, colour #000000 |
| How | at rest |

Crops: `featured-logo-default.png`.

#### feature-card

Feature card. A feature section card ("Effortlessly Scan Food"): h3 title, paragraph and a product screenshot.

Page: home. Selector: `Features > Container`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 590 x 400 | = |
| Padding | 40px 40px 0px 40px | = |
| Gap | 32px | = |
| Border | none | = |
| Radius | 18.8px | = |
| Background | color(display-p3 0.94902 0.94902 0.94902) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h3.framer-text.framer-styles-preset-5gyp6i: Aquawax Pro Bold 28px/33.6px 700, color(display-p3 0.129412 0.588235 0.94902) | = |
| Transition | none | = |
| Painted layers | div.framer-15q1eiy 590.0x400.0 bg color(display-p3 0.94902 0.94902 0.94902) r 18.8px | = |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

#### feature-title

Feature heading. The h3 inside a feature card ("Effortlessly Scan Food").

Page: home. Selector: `Features h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 239 x 67.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 28px/33.6px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.129412 0.588235 0.94902) |
| Transition | none |
| How | at rest |

Crops: `feature-title-default.png`.

#### value-card

Value card. A values card ("Privacy First", "Your Data, Your Control", "No Ads, Ever"): glyph, h4 title and paragraph.

Page: home. Selector: `Values > Container`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 300 x 181.58 | = |
| Padding | 0px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h4.framer-text.framer-styles-preset-ishzqq: Aquawax Pro Bold 22px/30.8px 700, color(display-p3 0.05098 0.05098 0.05098) | = |
| Transition | none | = |
| Painted layers | div.framer-WLnLp.framer-i4k58q 40.0x40.0 bg color(display-p3 0.486275 0.631373 0.760784) | = |
| How | at rest | mouse hover |

Crops: `value-card-default.png`, `value-card-hover.png`.

#### value-icon

Value glyph. The svg glyph on a values card.

Page: home. Selector: `Values Symbol svg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | color(display-p3 0.486275 0.631373 0.760784) |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.framer-WLnLp.framer-i4k58q 40.0x40.0 bg color(display-p3 0.486275 0.631373 0.760784) |
| How | at rest |

Crops: `value-icon-default.png`.

#### reviews-h2

Reviews heading. "Trusted By Thousands of Users" — the reviews section h2.

Page: home. Selector: `Reviews Title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 43.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text.framer-styles-preset-hincdn: Aquawax Pro Bold 36px/43.2px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `reviews-h2-default.png`.

#### review-card

Review card. An App-Store review card in the scrolling marquee (quote, handle, star row).

Page: home. Selector: `Reviews li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 279 x 260 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-28rfuw: Aquawax Pro Bold 18px/25.2px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 10166, 0) |
| Painted layers | div.framer-1075njn 279.0x260.0 bg color(display-p3 0.94902 0.94902 0.94902) r 18.8px; div.framer-P8O4K.framer-hqvmb2 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1kv394 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1uk5w5j 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-194z1ba 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1yg8gv0 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392) |
| How | at rest |

Crops: none.

#### review-stars

Star rating. The five-star row on a review card.

Page: home. Selector: `Reviews Stars`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 138 x 18 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.framer-P8O4K.framer-hqvmb2 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1kv394 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1uk5w5j 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-194z1ba 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1yg8gv0 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392) |
| Ancestor paint | 1 up div.framer-1075njn bg color(display-p3 0.94902 0.94902 0.94902) |
| How | at rest |

Crops: none.

#### cta-h2

CTA heading. "Start Tracking Macros for Free" — the closing call-to-action block.

Page: home. Selector: `CTA h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 43.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 36px/43.2px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `cta-h2-default.png`.

#### cta-secondary

Secondary CTA. The "Download the App ↗" secondary pill inside the closing CTA; an App-Store link, measured never followed.

Page: home. Selector: `a[data-framer-name="Secondary"] "Download"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 196 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.94902 0.94902 0.94902) | color(display-p3 0.901961 0.901961 0.901961) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 0.972549 0.384314 0.180392) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-5UbMV.framer-OHnkM 196.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px | a.framer-5UbMV.framer-OHnkM 196.0x40.0 bg color(display-p3 0.901961 0.901961 0.901961) r 20px | a.framer-5UbMV.framer-OHnkM 196.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-secondary-default.png`, `cta-secondary-hover.png`, `cta-secondary-focus-visible.png`, `cta-secondary-pressed.png`.

### Footer

#### footer

Footer. The site footer: logo, Explore / Comparisons / Company / Social link columns and the legal row.

Page: home. Selector: `[data-framer-name="Footer"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 288.8 |
| Padding | 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-s43twy: Aquawax Pro Bold 17px/23.8px 700, color(display-p3 1 1 1) |
| Transition | none |
| Painted layers | div.framer-13gyf4z 1376.0x243.8 bg color(display-p3 0.972549 0.384314 0.180392) r 18.8px; div.framer-cVfOO.framer-pqxif3 126.0x74.1 bg color(display-p3 1 1 1); div.framer-1g93id6 96.0x1.0 bg #bbddff |
| Ancestor paint | 1 up div.framer-HghBH.framer-pfRB1 bg color(display-p3 1 1 1) |
| How | at rest |

Crops: `footer-default.png`.

#### footer-col

Footer column label. A link-column heading in the footer ("Explore").

Page: home. Selector: `footer Explore Header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 61 x 23.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-s43twy: Aquawax Pro Bold 17px/23.8px 700, color(display-p3 1 1 1) |
| Transition | none |
| How | at rest |

Crops: `footer-col-default.png`.

#### footer-link

Footer link. A footer link ("Download ↗" under Explore); measured, never followed.

Page: home. Selector: `footer Explore Item a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Aquawax Pro Medium 15px/15px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 1 1 1) | color(display-p3 0.984314 0.631373 0.509804) | = | color(display-p3 0.984314 0.631373 0.509804) |
| Transition | color 0.4s cubic-bezier(0.44, 0, 0.56, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-277bjg 87.0x18.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-legal

Copyright line. The "(C) 2026. Algebraic Labs, LLC." line beside the Terms/Privacy links.

Page: home. Selector: `footer Copyright`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 199 x 15 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-rju16c: Aquawax Pro Medium 15px/15px 500, color(display-p3 0.2 0.2 0.2) |
| Transition | none |
| How | at rest |

Crops: `footer-legal-default.png`.

### Pricing (Foodnoms+)

#### plus-h1

Pricing headline. "Level Up Your Nutrition Tracking" — the Foodnoms+ page headline.

Page: plus. Selector: `h1 on /plus`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 123.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 56px/61.6px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `plus-h1-default.png`.

#### plus-tag

Tag chip. The "Find pricing info for your region in the app." note chip under the headline.

Page: plus. Selector: `[data-framer-name="Tag"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 310 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-1x6l9an: Aquawax Pro Medium 15px/21px 500, color(display-p3 1 1 1) |
| Transition | none |
| Ancestor paint | 1 up div.framer-15we10n bg color(display-p3 0.345098 0.337255 0.839216) |
| How | at rest |

Crops: `plus-tag-default.png`.

#### plus-cta

Try-for-free CTA. The "Try Foodnoms for Free ↗" primary pill; an App-Store link, measured never followed.

Page: plus. Selector: `a[data-framer-name="Primary"] "Try Foodnoms"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.972549 0.384 0.18) | color(display-p3 0.984314 0.631373 0.509804) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 1 1 1) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-5UbMV.framer-OHnkM 224.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px | a.framer-5UbMV.framer-OHnkM 224.0x40.0 bg color(display-p3 0.984314 0.631373 0.509804) r 20px | a.framer-5UbMV.framer-OHnkM 224.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plus-cta-default.png`, `plus-cta-hover.png`, `plus-cta-focus-visible.png`, `plus-cta-pressed.png`.

#### plus-cta-secondary

Secondary download pill. The "Download the App ↗" secondary pill on /plus; measured never followed.

Page: plus. Selector: `a[data-framer-name="Secondary"] on /plus`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 196 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.94902 0.94902 0.94902) | color(display-p3 0.901961 0.901961 0.901961) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 0.972549 0.384314 0.180392) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-5UbMV.framer-OHnkM 196.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px | a.framer-5UbMV.framer-OHnkM 196.0x40.0 bg color(display-p3 0.901961 0.901961 0.901961) r 20px | a.framer-5UbMV.framer-OHnkM 196.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plus-cta-secondary-default.png`, `plus-cta-secondary-hover.png`, `plus-cta-secondary-focus-visible.png`, `plus-cta-secondary-pressed.png`.

#### pricing-table

Comparison table. The Free vs Foodnoms+ feature-comparison table — a Framer component of Row/Header/Title/Paragraph/Divider/Symbol cells, not a <table> element.

Page: plus. Selector: `[data-framer-name="Table"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000 x 1388.45 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-s43twy: Aquawax Pro Bold 17px/23.8px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| Painted layers | div.framer-g3o7pp 1000.0x1.0 bg color(display-p3 0.901961 0.901961 0.901961); div.framer-1ujdjyv 1000.0x1.0 bg color(display-p3 0.901961 0.901961 0.901961); div.framer-3cz472 1000.0x1.0 bg color(display-p3 0.901961 0.901961 0.901961); div.framer-10hz6qp 1000.0x1.0 bg color(display-p3 0.901961 0.901961 0.901961); div.framer-Mn18G.framer-1whp2gz 16.0x16.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-Mn18G.framer-dd4wrs 16.0x16.0 bg color(display-p3 0.345098 0.337255 0.839216) |
| Ancestor paint | 1 up div.framer-qjjbl.framer-ok3yK bg color(display-p3 1 1 1) |
| How | at rest |

Crops: `pricing-table-default.png`.

#### pricing-head

Table header cell. A column header cell in the comparison table ("Features" / "Free" / "Foodnoms+").

Page: plus. Selector: `Table Header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 23.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-s43twy: Aquawax Pro Bold 17px/23.8px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `pricing-head-default.png`.

#### pricing-row

Table row. A feature row ("Nutrient Tracking") with its Free and Foodnoms+ cells.

Page: plus. Selector: `Table Row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000 x 25.59 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-d601be: Aquawax Pro Medium 16px/25.6px 500, color(display-p3 0.2 0.2 0.2) |
| Transition | none |
| How | at rest |

Crops: `pricing-row-default.png`.

#### pricing-cell

Table cell text. A feature cell value ("Calories & Macros" under Free).

Page: plus. Selector: `Table Paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 218 x 25.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-d601be: Aquawax Pro Medium 16px/25.6px 500, color(display-p3 0.4 0.4 0.4) |
| Transition | none |
| How | at rest |

Crops: `pricing-cell-default.png`.

#### pricing-check

Table check glyph. The check-mark svg used for included features in the comparison table.

Page: plus. Selector: `Table Symbol svg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 16 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | color(display-p3 0.972549 0.384314 0.180392) |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.framer-Mn18G.framer-1whp2gz 16.0x16.0 bg color(display-p3 0.972549 0.384314 0.180392) |
| How | at rest |

Crops: `pricing-check-default.png`.

#### pricing-divider

Table divider. The hairline divider between comparison rows.

Page: plus. Selector: `Table Divider`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000 x 1 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | color(display-p3 0.901961 0.901961 0.901961) |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.framer-g3o7pp 1000.0x1.0 bg color(display-p3 0.901961 0.901961 0.901961) |
| How | at rest |

Crops: none.

### Help center

#### help-h1

Help headline. "Help Center".

Page: help. Selector: `h1 on /help`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 44px/48.4px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `help-h1-default.png`.

#### help-search

Search trigger. The "Search" control on the help landing — a Framer component that opens the search modal when clicked (a local UI toggle).

Page: help. Selector: `[data-framer-name="Variant 1"] "Search"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113 x 40 | = | = | = |
| Padding | 12px 18px 12px 16px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.972549 0.384 0.18) | color(display-p3 0.984314 0.631373 0.509804) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 1 1 1) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 32 x 32, colour color(display-p3 1 1 1 / 0), fill #000000 | = | = | = |
| Painted layers | div.framer-Ih1EH.framer-OHnkM 113.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px; div.framer-g3QhO.framer-1wgo293 16.0x16.0 bg color(display-p3 1 1 1) | div.framer-Ih1EH.framer-OHnkM 113.0x40.0 bg color(display-p3 0.984314 0.631373 0.509804) r 20px; div.framer-g3QhO.framer-1wgo293 16.0x16.0 bg color(display-p3 1 1 1) | div.framer-Ih1EH.framer-OHnkM 113.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px outline 1px auto #101010 offset 0px; div.framer-g3QhO.framer-1wgo293 16.0x16.0 bg color(display-p3 1 1 1) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `help-search-default.png`, `help-search-hover.png`, `help-search-focus-visible.png`, `help-search-pressed.png`.

#### help-search-modal

Search modal. The Framer search overlay opened by the Search trigger.

Page: help. Selector: `.__framer-search-modal-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 17.84 x 17.84, colour color(display-p3 0.972549 0.384314 0.180392), fill #000000 |
| Painted layers | div 1440.0x900.0 bg #2e2e2e @ 0.6; div 594.7x56.5 bg color(display-p3 1 1 1) r 26px shadow #2e2e2e @ 0.26 0px 0px 20px 0px |
| Ancestor paint | 1 up body.__framer-overflow-hidden bg color(display-p3 1 1 1) |
| How | at rest |

Crops: `help-search-modal-default.png`.

#### help-search-input

Search field. The real input inside the Framer search modal; focused and typed into then cleared — never submitted.

Page: help. Selector: `search modal input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 530 x 34 | = | 500 x 34 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Aquawax Pro Medium 17px/34px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | color(display-p3 0.184314 0.184314 0.184314) | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | color(display-p3 0.184314 0.184314 0.184314 / 0.64), opacity 1 | = | = |
| Ancestor paint | 2 up div bg color(display-p3 1 1 1) shadow #2e2e2e @ 0.26 0px 0px 20px 0px | = | = |
| How | at rest | clicked into the field | typed "barcode", then deleted; nothing sent |

Crops: `help-search-input-default.png`, `help-search-input-focused.png`, `help-search-input-filled.png`.

#### help-accordion

Accordion section (closed). A collapsed topic group ("About Foodnoms"): header row with title and rotating + chevron; the question links sit inside.

Page: help. Selector: `[data-framer-name="Closed"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 25.2 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h5.framer-text.framer-styles-preset-28rfuw: Aquawax Pro Bold 18px/25.2px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| Icon | 22.63 x 22.63, colour #000000 |
| How | at rest |

Crops: `help-accordion-default.png`.

#### help-accordion-open

Accordion section (open). The same topic group expanded — measured after clicking its own Header (a local UI toggle; Closed -> Open).

Page: help. Selector: `[data-framer-name="Open"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 112.39 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h5.framer-text.framer-styles-preset-28rfuw: Aquawax Pro Bold 18px/25.2px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| How | at rest |

Crops: `help-accordion-open-default.png`.

#### help-accordion-header

Accordion header. The clickable header row of a topic group (tabindex=0, data-highlight): title + chevron.

Page: help. Selector: `accordion Header`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 800 x 25.2 | = | = |
| Padding | 0px | = | = |
| Gap | 32px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | sans-serif 12px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | h5.framer-text.framer-styles-preset-28rfuw: Aquawax Pro Bold 18px/25.2px 700, color(display-p3 0.05098 0.05098 0.05098) | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #000000 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | div.framer-3e3bb0 800.0x25.2 outline 1px auto #101010 offset 0px |

Crops: `help-accordion-header-default.png`, `help-accordion-header-hover.png`, `help-accordion-header-focus-visible.png`.

#### help-accordion-link

Accordion question link. A question link inside an open accordion ("What is Foodnoms?"); measured, never followed.

Page: help. Selector: `accordion a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Aquawax Pro Medium 16px/25.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 0.972549 0.384 0.18) | = | = | = |
| Transition | color 0.4s cubic-bezier(0.44, 0, 0.56, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-ksvyhk 149.0x18.0 outline 1px auto #101010 offset 1px | = |

Crops: `help-accordion-link-default.png`, `help-accordion-link-hover.png`, `help-accordion-link-focus-visible.png`, `help-accordion-link-pressed.png`.

#### help-contact

Contact block. The "Contact Us" block under the accordion sections.

Page: help. Selector: `[data-framer-name="Contact"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 146 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text.framer-styles-preset-hincdn: Aquawax Pro Bold 36px/43.2px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| Painted layers | a.framer-5UbMV.framer-OHnkM 116.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px |
| Ancestor paint | 1 up div.framer-ViJnN.framer-PT6di bg color(display-p3 1 1 1) |
| How | at rest |

Crops: `help-contact-default.png`.

#### help-contact-cta

Contact CTA. The mailto CTA in the Contact block (support@foodnoms.com, a published contact address); measured, never activated.

Page: help. Selector: `Contact Primary mailto`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.972549 0.384 0.18) | color(display-p3 0.984314 0.631373 0.509804) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 1 1 1) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-5UbMV.framer-OHnkM 116.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px | a.framer-5UbMV.framer-OHnkM 116.0x40.0 bg color(display-p3 0.984314 0.631373 0.509804) r 20px | a.framer-5UbMV.framer-OHnkM 116.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `help-contact-cta-default.png`, `help-contact-cta-hover.png`, `help-contact-cta-focus-visible.png`, `help-contact-cta-pressed.png`.

### News

#### news-h1

News headline. "News & Updates".

Page: news. Selector: `h1 on /news`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 44px/48.4px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `news-h1-default.png`.

#### news-card

Article card. A news article card (CMS image, title, date) linking to a /news/* article; measured, never followed.

Page: news. Selector: `a[href*="/news/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 442.66 x 396.52 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | h5.framer-text.framer-styles-preset-28rfuw: Aquawax Pro Bold 18px/25.2px 700, color(display-p3 0.2 0.2 0.2) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-EwUIO.framer-hjQD7 442.7x396.5 outline 1px auto #101010 offset 1px | = |

Crops: `news-card-default.png`, `news-card-hover.png`, `news-card-focus-visible.png`, `news-card-pressed.png`.

#### news-date

Card date. The publish-date label on a news card.

Page: news. Selector: `[data-framer-name="Date"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 398.39 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | time: Aquawax Pro Medium 15px/21px 500, color(display-p3 0.4 0.4 0.4) |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `news-date-default.png`.

#### nl-h2

Newsletter heading. "Become a Foodnoms Insider" — the newsletter block heading.

Page: news. Selector: `Newsletter h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 43.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 36px/43.2px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `nl-h2-default.png`.

#### nl-email

Newsletter email field. The pill-shaped email field in the newsletter block; focused and typed into then cleared — never submitted.

Page: news. Selector: `input[type="email"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 294 x 42 | = | = |
| Padding | 12px 18px | = | = |
| Border | none | = | = |
| Radius | 40px | = | = |
| Background | color(display-p3 0.94902 0.94902 0.94902) | = | = |
| Box shadow | color(display-p3 0.976471 0.505882 0.345098) 0px 0px 0px 0px inset, color(display-p3 0.901961 0.901961 0.901961) 0px 0px 0px 1px inset | color(display-p3 0.976471 0.505882 0.345098) 0px 0px 0px 2px inset, color(display-p3 0.901961 0.901961 0.901961) 0px 0px 0px 1px inset | color(display-p3 0.976471 0.505882 0.345098) 0px 0px 0px 2px inset, color(display-p3 0.901961 0.901961 0.901961) 0px 0px 0px 1px inset |
| Outline | none | = | = |
| Font | Aquawax Pro Medium 16px/16px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | color(display-p3 0.2 0.2 0.2) | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | color(display-p3 0.8 0.8 0.800001), opacity 1 | = | = |
| Painted layers | input.v1.framer-custom-input 294.0x42.0 bg color(display-p3 0.94902 0.94902 0.94902) r 40px shadow color(display-p3 0.976471 0.505882 0.345098) 0px 0px 0px 0px inset, color(display-p3 0.901961 0.901961 0.901961) 0px 0px 0px 1px inset | input.v1.framer-custom-input 294.0x42.0 bg color(display-p3 0.94902 0.94902 0.94902) r 40px shadow color(display-p3 0.976471 0.505882 0.345098) 0px 0px 0px 2px inset, color(display-p3 0.901961 0.901961 0.901961) 0px 0px 0px 1px inset | input.v1.framer-custom-input 294.0x42.0 bg color(display-p3 0.94902 0.94902 0.94902) r 40px shadow color(display-p3 0.976471 0.505882 0.345098) 0px 0px 0px 2px inset, color(display-p3 0.901961 0.901961 0.901961) 0px 0px 0px 1px inset |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `nl-email-default.png`, `nl-email-focused.png`, `nl-email-filled.png`.

#### nl-submit

Newsletter submit. The subscribe submit control; hovered and focused only — never pressed (it posts the form).

Page: news. Selector: `input[type="submit"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 96 x 42 | = | = |
| Padding | 12px 18px | = | = |
| Border | none | = | = |
| Radius | 40px | = | = |
| Background | color(display-p3 0.972549 0.384 0.18) | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Aquawax Pro DemiBold 16px/16px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | color(display-p3 1 1 1) | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Placeholder | color(display-p3 1 1 1), opacity 1 | = | = |
| Painted layers | input 96.0x42.0 bg color(display-p3 0.972549 0.384 0.18) r 40px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `nl-submit-default.png`, `nl-submit-hover.png`, `nl-submit-focus-visible.png`.

### Press

#### press-h1

Press headline. "Press Hub".

Page: press. Selector: `h1 on /press`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 44px/48.4px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `press-h1-default.png`.

#### press-tag

Section tag. A tag label on the press page sections.

Page: press. Selector: `[data-framer-name="Tag"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 25.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h5.framer-text.framer-styles-preset-28rfuw: Aquawax Pro Bold 18px/25.2px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `press-tag-default.png`.

#### press-details

App details block. The "App Details" fact block on the press hub.

Page: press. Selector: `[data-framer-name="Details"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 212.8 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text.framer-styles-preset-hincdn: Aquawax Pro Bold 36px/43.2px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| Ancestor paint | 1 up div.framer-cf2zC.framer-PT6di bg color(display-p3 1 1 1) |
| How | at rest |

Crops: `press-details-default.png`.

#### press-asset

Asset download link. The "Download Screenshots" asset link (a framerusercontent .zip); measured, never downloaded.

Page: press. Selector: `press "Download Screenshots"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 241 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | color(display-p3 0.94902 0.94902 0.94902) | color(display-p3 0.901961 0.901961 0.901961) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Aquawax Pro DemiBold 16px/16px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 0.972549 0.384314 0.180392) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 241.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 50px | a 241.0x40.0 bg color(display-p3 0.901961 0.901961 0.901961) r 50px | a 241.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 50px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `press-asset-default.png`, `press-asset-hover.png`, `press-asset-focus-visible.png`, `press-asset-pressed.png`.

#### press-contact-cta

Press contact CTA. The "Email Ryan />" secondary pill (a published press-contact mailto); measured, never activated.

Page: press. Selector: `press Secondary mailto`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 137 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.94902 0.94902 0.94902) | color(display-p3 0.901961 0.901961 0.901961) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 0.972549 0.384314 0.180392) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-5UbMV.framer-OHnkM 137.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px | a.framer-5UbMV.framer-OHnkM 137.0x40.0 bg color(display-p3 0.901961 0.901961 0.901961) r 20px | a.framer-5UbMV.framer-OHnkM 137.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `press-contact-cta-default.png`, `press-contact-cta-hover.png`, `press-contact-cta-focus-visible.png`, `press-contact-cta-pressed.png`.

### Article pages

#### fp-h1

Article headline. "A calorie tracker with a family plan" — the /family-plan article headline.

Page: family-plan. Selector: `h1 on /family-plan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 44px/48.4px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `fp-h1-default.png`.

#### fp-intro

Intro paragraph. The article intro block under the headline.

Page: family-plan. Selector: `[data-framer-name="Intro Body"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 167.97 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-d601be: Aquawax Pro Medium 16px/25.6px 500, color(display-p3 0.2 0.2 0.2) |
| Transition | none |
| How | at rest |

Crops: `fp-intro-default.png`.

#### fp-faq

FAQ block. The "Frequently asked questions" block — static question + Answer rows, not an accordion.

Page: family-plan. Selector: `[data-framer-name="FAQ"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 726.3 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text.framer-styles-preset-hincdn: Aquawax Pro Bold 36px/43.2px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `fp-faq-default.png`.

#### fp-faq-answer

FAQ answer. An answer paragraph inside the FAQ block.

Page: family-plan. Selector: `[data-framer-name="Answer"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 51.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-d601be: Aquawax Pro Medium 16px/25.6px 500, color(display-p3 0.2 0.2 0.2) |
| Transition | none |
| How | at rest |

Crops: `fp-faq-answer-default.png`.

#### vs-h1

Comparison headline. The /vs/myfitnesspal article headline.

Page: vs-mfp. Selector: `h1 on /vs/myfitnesspal`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 145.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 44px/48.4px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `vs-h1-default.png`.

#### vs-body

Article body. A body paragraph in the comparison article.

Page: vs-mfp. Selector: `Article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 102.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Medium 16px/25.6px 500 |
| Letter spacing | normal |
| Colour | color(display-p3 0.2 0.2 0.2) |
| Transition | none |
| How | at rest |

Crops: `vs-body-default.png`.

#### vs-table

Comparison table. The "Quick Comparison" feature table inside the article body.

Page: vs-mfp. Selector: `article table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 811.28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-d601be: Aquawax Pro Medium 16px/25.6px 500, color(display-p3 0.2 0.2 0.2) |
| Transition | none |
| Painted layers | th.framer-text 172.2x51.6 bg color(display-p3 0.94902 0.94902 0.94902) border B:2px solid; th.framer-text 328.0x51.6 bg color(display-p3 0.94902 0.94902 0.94902) border B:2px solid; th.framer-text 299.8x51.6 bg color(display-p3 0.94902 0.94902 0.94902) border B:2px solid; td.framer-text 172.2x50.6 border B:1px solid; td.framer-text 328.0x50.6 border B:1px solid; td.framer-text 299.8x50.6 border B:1px solid |
| How | at rest |

Crops: `vs-table-default.png`.

#### vs-faq-h2

FAQ heading. The "Frequently Asked Questions" h2 in the article.

Page: vs-mfp. Selector: `article h2 FAQ`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 43.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 36px/43.2px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `vs-faq-h2-default.png`.

#### ha-back

Back link. The "← Back" pill at the top of a help article (links to /help); measured, never followed.

Page: help-article. Selector: `article Secondary "← Back"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.94902 0.94902 0.94902) | color(display-p3 0.901961 0.901961 0.901961) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 0.972549 0.384314 0.180392) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-5UbMV.framer-OHnkM 95.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px | a.framer-5UbMV.framer-OHnkM 95.0x40.0 bg color(display-p3 0.901961 0.901961 0.901961) r 20px | a.framer-5UbMV.framer-OHnkM 95.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ha-back-default.png`, `ha-back-hover.png`, `ha-back-focus-visible.png`, `ha-back-pressed.png`.

#### ha-tag

Article tag. The category tag chip on a help article.

Page: help-article. Selector: `article Tag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 23.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-s43twy: Aquawax Pro Bold 17px/23.8px 700, color(display-p3 0.4 0.4 0.4) |
| Transition | none |
| How | at rest |

Crops: `ha-tag-default.png`.

#### ha-h1

Article headline. "How do I scan barcodes?" — a help article title.

Page: help-article. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 44px/48.4px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `ha-h1-default.png`.

#### ha-body

Article body. A body paragraph inside the help article.

Page: help-article. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 780 x 25.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Medium 16px/25.6px 500 |
| Letter spacing | normal |
| Colour | color(display-p3 0.2 0.2 0.2) |
| Transition | none |
| How | at rest |

Crops: `ha-body-default.png`.

#### ha-h2

Article section heading. A section heading inside the article ("Scanning a Barcode").

Page: help-article. Selector: `article h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 43.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 36px/43.2px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `ha-h2-default.png`.

#### ha-link

Inline link. A link inside a help article's prose (the /help/mcp article; the barcode article has none); measured, never followed.

Page: help-mcp. Selector: `article p a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Aquawax Pro Medium 16px/25.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 0.972549 0.384 0.18) | = | = | = |
| Transition | color 0.4s cubic-bezier(0.44, 0, 0.56, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-ksvyhk 184.0x18.0 outline 1px auto #101010 offset 1px | = |

Crops: `ha-link-default.png`, `ha-link-hover.png`, `ha-link-focus-visible.png`, `ha-link-pressed.png`.

#### na-date

Article date. The publish-date label above the article title.

Page: news-article. Selector: `[data-framer-name="Date"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 23.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | time: Aquawax Pro Bold 17px/23.8px 700, color(display-p3 0.4 0.4 0.4) |
| Transition | none |
| How | at rest |

Crops: `na-date-default.png`.

#### na-h1

Article headline. "FoodNoms 2: Feature Overview" — a news article title.

Page: news-article. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 44px/48.4px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `na-h1-default.png`.

#### na-toc

Table of contents label. The "Table of Contents" heading beside the anchor list.

Page: news-article. Selector: `TOC heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 43.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 36px/43.2px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `na-toc-default.png`.

#### na-h2

Article section heading. A section heading inside the news article.

Page: news-article. Selector: `article h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 43.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 36px/43.2px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `na-h2-default.png`.

#### na-body

Article body. A body paragraph in the news article.

Page: news-article. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 51.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Medium 16px/25.6px 500 |
| Letter spacing | normal |
| Colour | color(display-p3 0.2 0.2 0.2) |
| Transition | none |
| How | at rest |

Crops: `na-body-default.png`.

#### na-inline-link

Inline link. An inline link inside the article prose ("HidrateSpark"); measured, never followed.

Page: news-article. Selector: `article a "HidrateSpark"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Aquawax Pro Medium 16px/25.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 0.972549 0.384 0.18) | = | = | = |
| Transition | color 0.4s cubic-bezier(0.44, 0, 0.56, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-ksvyhk 102.0x18.0 outline 1px auto #101010 offset 1px | = |

Crops: `na-inline-link-default.png`, `na-inline-link-hover.png`, `na-inline-link-focus-visible.png`, `na-inline-link-pressed.png`.

### Legal

#### terms-h1

Terms headline. "Terms of Use".

Page: terms. Selector: `h1 on /terms`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 44px/48.4px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `terms-h1-default.png`.

#### terms-item

Legal section heading. A numbered section heading inside the legal body ("1. Agreement to these Terms" style; the single Legal Item component holds the whole document).

Page: terms. Selector: `Legal Item h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 33.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 28px/33.6px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `terms-item-default.png`.

### Open-in-app interstitial

#### os-h1

Interstitial headline. "Open in Foodnoms" — the deep-link interstitial shown when an app link is opened on the web.

Page: open-signup. Selector: `h1 on /open/settings/sign-up`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Bold 44px/48.4px 700 |
| Letter spacing | normal |
| Colour | color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| How | at rest |

Crops: `os-h1-default.png`.

#### os-primary

Interstitial action. The "Open in Foodnoms" pill on the interstitial — the page's own action (a deep link back into the app); measured, never followed.

Page: open-signup. Selector: `interstitial Secondary "Open in Foodnoms"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 181 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.94902 0.94902 0.94902) | color(display-p3 0.901961 0.901961 0.901961) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 0.972549 0.384314 0.180392) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-5UbMV.framer-OHnkM 181.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px | a.framer-5UbMV.framer-OHnkM 181.0x40.0 bg color(display-p3 0.901961 0.901961 0.901961) r 20px | a.framer-5UbMV.framer-OHnkM 181.0x40.0 bg color(display-p3 0.94902 0.94902 0.94902) r 20px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `os-primary-default.png`, `os-primary-hover.png`, `os-primary-focus-visible.png`, `os-primary-pressed.png`.

### Dark theme (emulated prefers-color-scheme)

#### d-body

Page canvas (dark). The top-level frame under the dark media rule.

Page: dark. Selector: `page root (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 4462.67 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.framer-text: Aquawax Pro Bold 24px/24px 700, color(display-p3 0.972549 0.384314 0.180392) |
| Transition | none |
| Icon | 120 x 40, colour #0000ee, fill #000000 |
| Painted layers | div.framer-HghBH.framer-pfRB1 1440.0x4462.7 bg color(display-p3 0 0 0); a.framer-5UbMV.framer-OHnkM 145.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px; div.framer-yY4Sd.framer-wYouK 0.0x0.0 bg color(display-p3 0 0 0); button 0.0x0.0 bg #000000 @ 0.2 r 40px; button 0.0x0.0 bg #000000 @ 0.2 r 40px; div.framer-15q1eiy 590.0x400.0 bg color(display-p3 0.101 0.101 0.101) r 18.8px |
| Ancestor paint | 1 up body bg color(display-p3 0 0 0) |
| How | at rest |

Crops: none.

#### d-nav-cta

Get-the-App pill (dark). The header primary pill under the dark media rule.

Page: dark. Selector: `nav Primary (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 145 x 40 |
| Padding | 12px 18px |
| Gap | 10px |
| Border | none |
| Radius | 20px |
| Background | color(display-p3 0.972549 0.384 0.18) |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 1 1 1) |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.framer-5UbMV.framer-OHnkM 145.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px |
| How | at rest |

Crops: `d-nav-cta-default.png`.

#### d-nav-link

Nav link (dark). A header link under the dark media rule.

Page: dark. Selector: `nav a (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 38 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Medium 15px/15px 500 |
| Letter spacing | normal |
| Colour | color(display-p3 0.6 0.6 0.6) |
| Transition | color 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| Cursor | pointer |
| How | at rest |

Crops: `d-nav-link-default.png`.

#### d-hero-lede

Hero lede (dark). The hero paragraph under the dark media rule.

Page: dark. Selector: `hero Paragraph (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 28.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-uaxznt: Aquawax Pro Medium 18px/28.8px 500, color(display-p3 0.6 0.6 0.6) |
| Transition | none |
| How | at rest |

Crops: `d-hero-lede-default.png`.

#### d-feature-card

Feature card (dark). A feature card under the dark media rule.

Page: dark. Selector: `Features Container (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 590 x 400 |
| Padding | 40px 40px 0px 40px |
| Gap | 32px |
| Border | none |
| Radius | 18.8px |
| Background | color(display-p3 0.101 0.101 0.101) |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.framer-text.framer-styles-preset-5gyp6i: Aquawax Pro Bold 28px/33.6px 700, color(display-p3 0.129412 0.588235 0.94902) |
| Transition | none |
| Painted layers | div.framer-15q1eiy 590.0x400.0 bg color(display-p3 0.101 0.101 0.101) r 18.8px |
| How | at rest |

Crops: `d-feature-card-default.png`.

#### d-value-card

Value card (dark). A values card under the dark media rule.

Page: dark. Selector: `Values Container (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 181.58 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.framer-text.framer-styles-preset-ishzqq: Aquawax Pro Bold 22px/30.8px 700, color(display-p3 0.94902 0.94902 0.94902) |
| Transition | none |
| Painted layers | div.framer-WLnLp.framer-i4k58q 40.0x40.0 bg color(display-p3 0.486275 0.631373 0.760784) |
| How | at rest |

Crops: `d-value-card-default.png`.

#### d-review-card

Review card (dark). A review card under the dark media rule.

Page: dark. Selector: `Reviews li (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 279 x 260 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-28rfuw: Aquawax Pro Bold 18px/25.2px 700, color(display-p3 0.94902 0.94902 0.94902) |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 10166, 0) |
| Painted layers | div.framer-1075njn 279.0x260.0 bg color(display-p3 0.101 0.101 0.101) r 18.8px; div.framer-P8O4K.framer-hqvmb2 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1kv394 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1uk5w5j 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-194z1ba 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1yg8gv0 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392) |
| How | at rest |

Crops: none.

#### d-footer

Footer (dark). The footer under the dark media rule.

Page: dark. Selector: `Footer (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 288.8 |
| Padding | 0px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-s43twy: Aquawax Pro Bold 17px/23.8px 700, color(display-p3 1 1 1) |
| Transition | none |
| Painted layers | div.framer-13gyf4z 1376.0x243.8 bg color(display-p3 0.972549 0.384314 0.180392) r 18.8px; div.framer-cVfOO.framer-pqxif3 126.0x74.1 bg color(display-p3 1 1 1); div.framer-1g93id6 96.0x1.0 bg #bbddff |
| Ancestor paint | 1 up div.framer-HghBH.framer-pfRB1 bg color(display-p3 0 0 0) |
| How | at rest |

Crops: `d-footer-default.png`.

#### d-footer-link

Footer link (dark). A footer link under the dark media rule.

Page: dark. Selector: `footer a (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 87 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aquawax Pro Medium 15px/15px 500 |
| Letter spacing | normal |
| Colour | color(display-p3 1 1 1) |
| Transition | color 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| Cursor | pointer |
| How | at rest |

Crops: `d-footer-link-default.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone top bar: app icon, Foodnoms name and the hamburger.

Page: mobile. Selector: `mobile Leading (header)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.framer-text: Aquawax Pro Bold 24px/24px 700, color(display-p3 0.972549 0.384314 0.180392) |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-hamburger

Mobile hamburger. The "Open navigation menu" button that opens the phone nav overlay (its aria-label flips to "Close navigation menu" once open, so the opened overlay is evidenced by the mobile-home-light-drawer screenshot and the m-drawer-link reading taken inside it).

Page: mobile. Selector: `button[aria-label="Open navigation menu"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.framer-x03zsu 40.0x40.0 outline 1px auto #e59700 offset 0px | = |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-focus-visible.png`, `m-hamburger-pressed.png`.

#### m-hero-ticker

Mobile hero ticker. The rotating headline at 390 wide.

Page: mobile. Selector: `mobile hero Title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 266 x 85.59 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.framer-text.framer-styles-preset-17m3dyy: Aquawax Pro Bold 36px/39.6px 700, color(display-p3 0.972549 0.384314 0.180392) |
| Transition | none |
| Painted layers | button 0.0x0.0 bg #000000 @ 0.2 r 40px; button 0.0x0.0 bg #000000 @ 0.2 r 40px |
| How | at rest |

Crops: `m-hero-ticker-default.png`.

#### m-hero-cta

Mobile hero CTA. The primary App-Store pill on the phone layout; measured never followed.

Page: mobile. Selector: `mobile Primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145 x 40 | = | = | = |
| Padding | 12px 18px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | color(display-p3 0.972549 0.384 0.18) | color(display-p3 0.984314 0.631373 0.509804) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-uhlqxi: Aquawax Pro DemiBold 16px/16px 600, color(display-p3 1 1 1) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-5UbMV.framer-OHnkM 145.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px | a.framer-5UbMV.framer-OHnkM 145.0x40.0 bg color(display-p3 0.984314 0.631373 0.509804) r 20px | a.framer-5UbMV.framer-OHnkM 145.0x40.0 bg color(display-p3 0.972549 0.384 0.18) r 20px outline 1px auto #e59700 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

#### m-feature-card

Mobile feature card. A feature card at 390 wide.

Page: mobile. Selector: `mobile Features Container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 542.81 |
| Padding | 40px 40px 0px 40px |
| Border | none |
| Radius | 18.8px |
| Background | color(display-p3 0.94902 0.94902 0.94902) |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.framer-text.framer-styles-preset-5gyp6i: Aquawax Pro Bold 22px/26.4px 700, color(display-p3 0.129412 0.588235 0.94902) |
| Transition | none |
| Painted layers | div.framer-15q1eiy 358.0x542.8 bg color(display-p3 0.94902 0.94902 0.94902) r 18.8px |
| How | at rest |

Crops: `m-feature-card-default.png`.

#### m-review-card

Mobile review card. A review card at 390 wide.

Page: mobile. Selector: `mobile Reviews li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 279 x 260 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-28rfuw: Aquawax Pro Bold 16px/22.4px 700, color(display-p3 0.05098 0.05098 0.05098) |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 10166, 0) |
| Painted layers | div.framer-1075njn 279.0x260.0 bg color(display-p3 0.94902 0.94902 0.94902) r 18.8px; div.framer-P8O4K.framer-hqvmb2 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1kv394 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1uk5w5j 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-194z1ba 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1yg8gv0 18.0x18.0 bg color(display-p3 0.972549 0.384314 0.180392) |
| How | at rest |

Crops: none.

#### m-footer-link

Mobile footer link. A footer link at 390 wide; measured, never followed.

Page: mobile. Selector: `mobile footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Aquawax Pro Medium 15px/15px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 1 1 1) | color(display-p3 0.984314 0.631373 0.509804) | = | color(display-p3 0.984314 0.631373 0.509804) |
| Transition | color 0.4s cubic-bezier(0.44, 0, 0.56, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-277bjg 87.0x18.0 outline 1px auto #e59700 offset 1px | = |

Crops: `m-footer-link-default.png`, `m-footer-link-hover.png`, `m-footer-link-focus-visible.png`, `m-footer-link-pressed.png`.

## Transitions declared in the readable stylesheets

foodnoms.com's own CSS is served in inline <style> blocks, so this list holds every rule declaring transition or animation that the CSSOM could read on each page; the per-state Transition rows above are the computed values.

- family-plan: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- help: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- help-article: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- home: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- news: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- news-article: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- open-signup: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- plus: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- press: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- terms: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`

- vs-mfp: `color 0.4s cubic-bezier(0.44, 0, 0.56, 1)`, `opacity 0.4s ease-out`, `unset`
