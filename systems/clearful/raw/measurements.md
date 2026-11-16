# Component measurements

Computed styles read from clearful.com on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) on the site's light surface (the /library route is a Tailwind sibling build, the app.clearful.com sign-in a Flutter canvas read through its semantics overlay at devicePixelRatio 1; no consent overlay mounts), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Nav bar. The 1440x72 top nav (Webflow w-nav): logo, Guided Journals link, Log In and the blue Start-a-journal pill.

Page: home. Selector: `.navbar1_component`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px 72px |
| Border | T: none; R: none; B: 1px solid #e1e1e1; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | a.navbar1_link.w-nav-link: Manrope 16px/24px 600, #222222 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.navbar1_component.background-color-primary 1440.0x72.0 bg #ffffff border B:1px solid #e1e1e1; div.navbar-divider.margin-xxsmall 1.0x28.0 bg #e1e1e1; a.button.is-small 230.0x50.0 bg #1953ff border T:1px solid #1953ff / R:1px solid #1953ff / B:1px solid #1953ff / L:1px solid #1953ff r 999px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Clearful logo anchor (150x30).

Page: home. Selector: `.navbar1_logo-link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 150 x 29.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. The "Guided Journals" nav link (16px/600 ink); links to /library, never followed.

Page: home. Selector: `a.navbar1_link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 167 x 40 | = | = | = |
| Padding | 8px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | 8px | = | 8px |
| Background | transparent | #f7f7f7 | = | #f7f7f7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Manrope 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.navbar1_link.w-nav-link 167.0x40.0 bg #f7f7f7 r 8px | a.navbar1_link.w-nav-link 167.0x40.0 outline 1px auto #101010 offset 1px | a.navbar1_link.w-nav-link 167.0x40.0 bg #f7f7f7 r 8px |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-signin

Log-in link. The "Log In" nav action linking to app.clearful.com/#/sign-in; measured never followed.

Page: home. Selector: `nav a: Log In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86 x 40 | = | = | = |
| Padding | 8px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | 8px | = | 8px |
| Background | transparent | #f7f7f7 | = | #f7f7f7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Manrope 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.navbar1_link.w-nav-link 86.0x40.0 bg #f7f7f7 r 8px | a.navbar1_link.w-nav-link 86.0x40.0 outline 1px auto #101010 offset 1px | a.navbar1_link.w-nav-link 86.0x40.0 bg #f7f7f7 r 8px |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Nav CTA. The 999px blue "Start a journal — it's free" pill in the nav (225x50, #1953ff); the anchor points at #, measured never pressed.

Page: home. Selector: `a.button.is-small`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 230 x 50 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Border | 1px solid #1953ff | 1px solid #1b1bbc | = | 1px solid #1b1bbc |
| Radius | 999px | = | = | = |
| Background | #1953ff | #1b1bbc | = | #1b1bbc |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Manrope 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.is-small 230.0x50.0 bg #1953ff border T:1px solid #1953ff / R:1px solid #1953ff / B:1px solid #1953ff / L:1px solid #1953ff r 999px | a.button.is-small 230.0x50.0 bg #1b1bbc border T:1px solid #1b1bbc / R:1px solid #1b1bbc / B:1px solid #1b1bbc / L:1px solid #1b1bbc r 999px | a.button.is-small 230.0x50.0 bg #1953ff border T:1px solid #1953ff / R:1px solid #1953ff / B:1px solid #1953ff / L:1px solid #1953ff r 999px outline 1px auto #101010 offset 1px | a.button.is-small 230.0x50.0 bg #1b1bbc border T:1px solid #1b1bbc / R:1px solid #1b1bbc / B:1px solid #1b1bbc / L:1px solid #1b1bbc r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title. "Be a more thoughtful, resilient, and happier you with daily journaling" — the 72px/700 Literatatt display headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 259.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Literatatt 72px/86.4px 700 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### cta

Hero CTA. The 999px blue "Start journaling for free" pill under the hero (289x82, 20px/600); measured never pressed.

Page: home. Selector: `a.button.is-large`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 298 x 82 | = | = | = |
| Padding | 20px 28px | = | = | = |
| Border | 6px solid #adc2ff | = | = | = |
| Radius | 999px | = | = | = |
| Background | #1953ff | #1b1bbc | = | #1b1bbc |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Manrope 20px/30px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.is-large 298.0x82.0 bg #1953ff border T:6px solid #adc2ff / R:6px solid #adc2ff / B:6px solid #adc2ff / L:6px solid #adc2ff r 999px | a.button.is-large 298.0x82.0 bg #1b1bbc border T:6px solid #adc2ff / R:6px solid #adc2ff / B:6px solid #adc2ff / L:6px solid #adc2ff r 999px | a.button.is-large 298.0x82.0 bg #1953ff border T:6px solid #adc2ff / R:6px solid #adc2ff / B:6px solid #adc2ff / L:6px solid #adc2ff r 999px outline 1px auto #101010 offset 1px | a.button.is-large 298.0x82.0 bg #1b1bbc border T:6px solid #adc2ff / R:6px solid #adc2ff / B:6px solid #adc2ff / L:6px solid #adc2ff r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-default.png`, `cta-hover.png`, `cta-focus-visible.png`, `cta-pressed.png`.

#### section-title

Section title. The first 60px/700 section heading ("We're Clearful, the award-winning, modern jour…", navy #001452).

Page: home. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 432 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Literatatt 60px/72px 700 |
| Letter spacing | normal |
| Colour | #001452 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### feature-card

Feature card. A 1280x720 feature card (layout409): copy column + app screenshot.

Page: home. Selector: `.layout409_card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 720 |
| Padding | 0px |
| Gap | 0px |
| Border | 1px solid #ffffff |
| Radius | 24px |
| Background | #f7f7f7 |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div.text-style-tagline: Manrope 18px/31.5px 700, #1953ff |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 20 x 20, colour #1953ff |
| Painted layers | div.layout409_card.card-1 1280.0x720.0 bg #f7f7f7 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 24px |
| How | at rest |

Crops: `feature-card-default.png`.

#### tab-link

Cadence tab. A cadence tab (Weekly/Monthly/Quarterly/Bi-Yearly/Yearly) in the timeline14 w-tabs widget; the held tab carries w--current, tabs switch panes locally.

Page: home. Selector: `a.timeline14_tab-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 256 x 73.59 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | T: none; R: none; B: 1px solid #000000 @ 0; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Manrope 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div.heading-style-timeline: Manrope 24px/33.6px 700, #222222 | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 15 x 15, colour #222222 | = | = | = |
| Painted layers | a.timeline14_tab-link.w-inline-block 256.0x73.6 border B:1px solid #000000 @ 0; div.timeline14_fade-overlay-left 64.0x6.0 image linear-gradient(270deg, #000000 @ 0, #ffffff); div.timeline14_tab-progress 120.5x3.0 bg #e1e1e1; div.timeline14_circle.w-embed 15.0x15.0 shadow #f7f7f7 0px 0px 0px 8px; div.timeline14_tab-progress 120.5x3.0 bg #e1e1e1 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tab-link-default.png`, `tab-link-hover.png`, `tab-link-focus-visible.png`, `tab-link-pressed.png`.

#### section-accent

Brand-light band. The #d6e0ff brand-light section fill (background-color-brand-light) — the site's one tinted band.

Page: home. Selector: `.background-color-brand-light`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1200 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #d6e0ff |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #001452 |
| Text node | h2: Literatatt 60px/72px 700, #001452 |
| Transition | none |
| Painted layers | header.section_header64.background-color-brand-light 1440.0x1200.0 bg #d6e0ff |
| How | at rest |

Crops: `section-accent-default.png`.

#### app-badge

Store badge. The App Store badge artwork (153x80); the anchor links to apps.apple.com, never followed.

Page: home. Selector: `img[alt*=App Store]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 153.42 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `app-badge-default.png`.

#### page-ground

Page ground. The body element's painted fill — the white ground (html itself is transparent).

Page: home. Selector: `document.body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 32520.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div.qr-code-title: Manrope 20px/30px 800, #222222 |
| Transition | none |
| Icon | 0 x 0, colour #1953ff |
| Painted layers | body 1440.0x32520.8 bg #ffffff; div.qr-code 115.0x196.0 bg #ffffff r 8px shadow #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.06 0px 4px 6px -2px; div.modal_get-app_content-wrapper.text-color-brand-dark 0.0x0.0 bg #d6e0ff; a.button.is-secondary 0.0x0.0 border T:1px solid #001452 / R:1px solid #001452 / B:1px solid #001452 / L:1px solid #001452 r 999px; a.button.is-secondary 0.0x0.0 border T:1px solid #001452 / R:1px solid #001452 / B:1px solid #001452 / L:1px solid #001452 r 999px; a.button.is-secondary 0.0x0.0 border T:1px solid #001452 / R:1px solid #001452 / B:1px solid #001452 / L:1px solid #001452 r 999px |
| How | at rest |

Crops: none.

### Pricing

#### pricing-title

Pricing title. "Pricing Plans" — the 60px/700 heading over the Free/Premium comparison table.

Page: pricing. Selector: `h2 Pricing Plans`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Literatatt 60px/72px 700 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-tab

Billing tab. The Monthly/Yearly billing tab (w-tab-menu, 108x40); the held period carries w--current. A local pane switch, measured never flipped.

Page: pricing. Selector: `a.pricing27_tab-link.w--current`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106 x 40 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Manrope 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div: Manrope 16px/24px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-tab-default.png`, `billing-tab-hover.png`, `billing-tab-focus-visible.png`, `billing-tab-pressed.png`.

#### plan-column

Plan column. A plan column top (347x247): price, cadence and the Get-started button.

Page: pricing. Selector: `.pricing27_top-row-content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 347.42 x 246.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div.heading-style-h6: Manrope 24px/33.6px 700, #222222 |
| Transition | none |
| Painted layers | a.button-4.max-width-full 347.4x58.0 bg #1953ff border T:1px solid #1953ff / R:1px solid #1953ff / B:1px solid #1953ff / L:1px solid #1953ff r 999px |
| How | at rest |

Crops: `plan-column-default.png`.

#### plan-price

Plan price. The "$0/mo"/"$9.99/mo" price line (56px/700).

Page: pricing. Selector: `.pricing27_top-row-price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 347.42 x 67.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Manrope 56px/67.2px 700 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | undefined: Manrope 24px/33.6px 700, #222222 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. The blue "Get started" pill under each price (347x58, #1953ff); never pressed.

Page: pricing. Selector: `a.is-pricing27-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 347.42 x 58 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #1953ff | 1px solid #1b1bbc | = | 1px solid #1b1bbc |
| Radius | 999px | = | = | = |
| Background | #1953ff | #1b1bbc | = | #1b1bbc |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Manrope 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button-4.max-width-full 347.4x58.0 bg #1953ff border T:1px solid #1953ff / R:1px solid #1953ff / B:1px solid #1953ff / L:1px solid #1953ff r 999px | a.button-4.max-width-full 347.4x58.0 bg #1b1bbc border T:1px solid #1b1bbc / R:1px solid #1b1bbc / B:1px solid #1b1bbc / L:1px solid #1b1bbc r 999px | a.button-4.max-width-full 347.4x58.0 bg #1953ff border T:1px solid #1953ff / R:1px solid #1953ff / B:1px solid #1953ff / L:1px solid #1953ff r 999px outline 1px auto #101010 offset 1px | a.button-4.max-width-full 347.4x58.0 bg #1b1bbc border T:1px solid #1b1bbc / R:1px solid #1b1bbc / B:1px solid #1b1bbc / L:1px solid #1b1bbc r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### feature-row

Feature row. A feature row in the Free/Premium comparison table (1280x56 on the #f7f7f7 alternate band).

Page: pricing. Selector: `.pricing27_row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 56 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 8px |
| Background | #f7f7f7 |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div: Manrope 16px/24px 600, #222222 |
| Transition | none |
| Painted layers | div.w-layout-grid.pricing27_row 1280.0x56.0 bg #f7f7f7 r 8px |
| How | at rest |

Crops: `feature-row-default.png`.

### Footer

#### footer

Footer. The #f7f7f7 footer band (1440x535): resource links, store badges, social icons and the legal subfooter.

Page: home. Selector: `footer.footer1_component`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 548.05 |
| Padding | 0px |
| Border | T: 1px solid #e1e1e1; R: none; B: none; L: none |
| Radius | 0px |
| Background | #f7f7f7 |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | div.text-size-medium.text-weight-semibold: Manrope 18px/31.5px 600, #222222 |
| Transition | none |
| Icon | 20 x 20, colour #626262 |
| Painted layers | footer.footer1_component 1440.0x548.0 bg #f7f7f7 border T:1px solid #e1e1e1; div.line-divider 1280.0x1.0 bg #e1e1e1 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a.footer1_link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85 x 40 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Manrope 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #515151 | #1953ff | = | #1953ff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.footer1_link 85.0x40.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link. A footer social icon link (Instagram).

Page: home. Selector: `footer a[href*=instagram]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106 x 40 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Manrope 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #626262 | #1953ff | = | #1953ff |
| Text node | div: Manrope 16px/24px 400, #626262 | div: Manrope 16px/24px 400, #1953ff | = | div: Manrope 16px/24px 400, #1953ff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #626262 | 20 x 20, colour #1953ff | = | 20 x 20, colour #1953ff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.footer1_social-link.w-inline-block 106.0x40.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

### Guided-journals library (Tailwind surface)

#### library-h1

Library title. "Guided Journaling Library" — 60px/800 Mulish in Tailwind gray-900 (#111827); /library is a Tailwind sibling stack, not the Webflow marketing sheet.

Page: library. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 832 x 76 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Mulish 60px/76px 800 |
| Letter spacing | normal |
| Colour | #111827 |
| Transition | none |
| How | at rest |

Crops: `library-h1-default.png`.

#### prompt-card

Journal card. A guided-journal link card (white, 395x160, radius 16, Tailwind utilities); links into the library, never followed.

Page: library. Selector: `a.flex h-40 card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 394.66 x 160 | = | = | = |
| Padding | 32px | = | = | = |
| Border | 1px solid #e1e1e1 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff | #f7f7f7 | = | #f7f7f7 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Mulish 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3.text-2xl.font-bold: Mulish 24px/32px 700, #111827 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter, -webkit-backdrop-filter 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.flex-col 394.7x160.0 bg #ffffff border T:1px solid #e1e1e1 / R:1px solid #e1e1e1 / B:1px solid #e1e1e1 / L:1px solid #e1e1e1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | a.flex.flex-col 394.7x160.0 bg #f7f7f7 border T:1px solid #e1e1e1 / R:1px solid #e1e1e1 / B:1px solid #e1e1e1 / L:1px solid #e1e1e1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | a.flex.flex-col 394.7x160.0 bg #ffffff border T:1px solid #e1e1e1 / R:1px solid #e1e1e1 / B:1px solid #e1e1e1 / L:1px solid #e1e1e1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px outline 1px auto #101010 offset 1px | a.flex.flex-col 394.7x160.0 bg #f7f7f7 border T:1px solid #e1e1e1 / R:1px solid #e1e1e1 / B:1px solid #e1e1e1 / L:1px solid #e1e1e1 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -4) | = | matrix(1, 0, 0, 1, 0, -4) |

Crops: `prompt-card-default.png`, `prompt-card-hover.png`, `prompt-card-focus-visible.png`, `prompt-card-pressed.png`.

### App sign-in (Flutter boundary)

#### signin-image

Welcome illustration. The "Welcome Back Image" artwork on the sign-in card (264x176) — read through Flutter's flt-semantics overlay; the card paints on canvas so only geometry/roles are DOM-readable.

Page: signin. Selector: `flt-semantics[role=img]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 264 x 176 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 588, 56) |
| How | at rest |

Crops: `signin-image-default.png`.

#### signin-button

Sign-in button. A "Continue with email/Apple/Google" button on the sign-in card (400x56); canvas-painted, measured via the semantics overlay — never pressed.

Page: signin. Selector: `flt-semantics[role=button]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 520, 384.5) |
| How | at rest |

Crops: `signin-button-default.png`.

### Mobile (390 wide)

#### m-header

Mobile bar. The 390x64 mobile nav bar: logo + hamburger.

Page: home. Selector: `.navbar1_component at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px 19.5px |
| Border | T: none; R: none; B: 1px solid #e1e1e1; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.navbar1_component.background-color-primary 390.0x64.0 bg #ffffff border B:1px solid #e1e1e1; nav.navbar1_menu.is-page-height-tablet 0.0x0.0 bg #ffffff; div.navbar-divider.margin-xxsmall 0.0x0.0 bg #e1e1e1; a.button.is-small 0.0x0.0 bg #1953ff border T:1px solid #1953ff / R:1px solid #1953ff / B:1px solid #1953ff / L:1px solid #1953ff r 999px; div.menu-icon1_line-top 24.0x2.0 bg #222222; div.menu-icon1_line-middle 24.0x2.0 bg #222222 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The 40x48 hamburger (w-nav-button, the menu-icon1 lines); its own press opens the nav menu.

Page: home. Selector: `.navbar1_menu-button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Manrope 24px/36px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.menu-icon1_line-top 24.0x2.0 bg #222222; div.menu-icon1_line-middle 24.0x2.0 bg #222222; div.menu-icon1_line-bottom 24.0x2.0 bg #222222 |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The nav menu after the hamburger press (Webflow w-nav-menu).

Page: home. Selector: `nav.w-nav-menu after toggle press`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 16px 19.5px 96px 19.5px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Manrope 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | a.navbar1_link.w-nav-link: Manrope 18px/27px 600, #222222 |
| Transition | height, transform 0.5s, 0.4s ease, ease delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | nav.navbar1_menu.is-page-height-tablet 390.0x844.0 bg #ffffff; div.navbar-divider.margin-xxsmall 0.0x0.0 bg #e1e1e1; a.button.is-small 351.0x50.0 bg #1953ff border T:1px solid #1953ff / R:1px solid #1953ff / B:1px solid #1953ff / L:1px solid #1953ff r 999px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-link

Menu link. A link row inside the open mobile menu.

Page: home. Selector: `first link inside the open w-nav-menu`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 351 x 51 | = | = | = |
| Padding | 12px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | 8px | = | 8px |
| Background | transparent | #f7f7f7 | = | #f7f7f7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Manrope 18px/27px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up nav.navbar1_menu.is-page-height-tablet bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.navbar1_link.w-nav-link 351.0x51.0 bg #f7f7f7 r 8px | a.navbar1_link.w-nav-link 351.0x51.0 outline 1px auto #101010 offset 1px | a.navbar1_link.w-nav-link 351.0x51.0 bg #f7f7f7 r 8px |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile headline. The hero headline at 390.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 351 x 470.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Literatatt 56px/67.2px 700 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: none
