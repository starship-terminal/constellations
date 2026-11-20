# Elementor component measurements

Computed styles read from elementor.com on 2026-11-13 by `tools/capture/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The floating pill header: Elementor logo, the Products mega-menu trigger, Agency/Enterprise/Pricing/App-Builder links, the En language selector, Log in and the black Get-started pill.

Page: home. Selector: `painted bar inside header.elementor-location-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1248 x 72 |
| Padding | 0px 12px 0px 20px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.05 0px 0px 15.008px 3.008px |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.e-n-menu-title-text: Roobert 16px/22.4px 400, #212121 |
| Transition | none |
| Icon | 184 x 32, colour #0000ee |
| Painted layers | div.elementor-element.elementor-element-7559e775 1248.0x72.0 bg #ffffff r 24px shadow #000000 @ 0.05 0px 0px 15.008px 3.008px; div.elementor-element.elementor-element-921a16e 0.0x0.0 bg #ffffff r 24px shadow #000000 @ 0.05 0px 0px 15.008px 3.008px; div::before.elementor-element.elementor-element-921a16e 100%x1px bg #d1d1d1; div.elementor-element.elementor-element-46d7982 0.0x0.0 border R:1px solid #d1d1d1; a.elementor-element.elementor-element-425e4ad 0.0x0.0 image linear-gradient(297deg, #620856 9.99%, #1b0317 60.15%) r 8px; div.elementor-element.elementor-element-c576406 0.0x0.0 image linear-gradient(88deg, #ffffff 7.73%, #d67fc8 157.58%) |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Elementor wordmark anchor.

Page: home. Selector: `header a:first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 184 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | opacity 0.3s ease-in-out |
| Cursor | pointer |
| Icon | 184 x 32, colour #0000ee |
| Ancestor paint | 1 up div.elementor-element.elementor-element-7559e775 bg #ffffff shadow #000000 @ 0.05 0px 0px 15.008px 3.008px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Products menu trigger that opens the mega-menu; toggled, never followed.

Page: home. Selector: `.e-n-menu-title.e-click "Products"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.97 x 40.3 | = | - | = |
| Padding | 8.96px 16px | = | - | = |
| Gap | 1.92px | = | - | = |
| Border | none | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | #fae4fa | - | #fae4fa |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Roobert 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #212121 | #1f2124 | - | #1f2124 |
| Text node | span.e-n-menu-title-text: Roobert 16px/22.4px 400, #212121 | span.e-n-menu-title-text: Roobert 16px/22.4px 400, #1f2124 | - | span.e-n-menu-title-text: Roobert 16px/22.4px 400, #1f2124 |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 0 x 0, colour #212121, fill #000000 @ 0 | 0 x 0, colour #1f2124, fill #000000 @ 0 | - | 0 x 0, colour #1f2124, fill #000000 @ 0 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Painted layers | - | div.e-n-menu-title.e-click 98.0x40.3 bg #fae4fa r 8px | = | div.e-n-menu-title.e-click 98.0x40.3 bg #fae4fa r 8px |
| Error | - | = | keyboard focus could not be landed on the target | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. The plain Pricing header link.

Page: home. Selector: `e-n-menu "Pricing" link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.81 x 22.39 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | #1f2124 | = | #ff0000 |
| Text node | span.e-n-menu-title-text: Roobert 16px/22.4px 400, #212121 | span.e-n-menu-title-text: Roobert 16px/22.4px 400, #1f2124 | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.e-n-menu-title bg #fae4fa | = | = |
| Painted layers | - | = | a.e-n-menu-title-container.e-focus 50.8x22.4 outline 2px auto #005fcc offset 2px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Login link. The Log-in header action; measured never followed (it points at my.elementor.com).

Page: home. Selector: `header a "Log in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44.3 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | opacity 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 2 up div.elementor-element.elementor-element-7559e775 bg #ffffff shadow #000000 @ 0.05 0px 0px 15.008px 3.008px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.e-8ac6787-2a18a1c.dsm-link-wrapper-st 44.3x24.0 outline 2px auto #005fcc offset 2px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Nav CTA. The black Get-started pill (dsm-button-primary-st); measured never followed (points at my.elementor.com/signup).

Page: home. Selector: `header a.dsm-btn-wrapper-st "Get started"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 144 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | #ed01ee | #ed01ee | #ed01ee |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 18px/25.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dsm-btn-wrapper-st.e-8149469-75e5fd5 144.0x48.0 bg #000000 r 8px | a.dsm-btn-wrapper-st.e-8149469-75e5fd5 144.0x48.0 bg #ed01ee r 8px | a.dsm-btn-wrapper-st.e-8149469-75e5fd5 144.0x48.0 bg #ed01ee r 8px outline 2px auto #005fcc offset 2px | a.dsm-btn-wrapper-st.e-8149469-75e5fd5 144.0x48.0 bg #ed01ee r 8px |
| Ancestor paint | 2 up div.elementor-element.elementor-element-7559e775 bg #ffffff shadow #000000 @ 0.05 0px 0px 15.008px 3.008px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Nav dropdown. The Products mega-menu panel, opened by its own trigger.

Page: home. Selector: `#e-n-menu-content-9381 (open)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 693.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.elementor-heading-title.elementor-size-default: Roobert 14px/22.4px 400, #ffffff, ls 0.7px |
| Transition | none |
| Icon | 84.3 x 30.39, colour #6ec1e4 @ 0 |
| Painted layers | div.elementor-element.elementor-element-921a16e 1248.0x693.2 bg #ffffff r 24px shadow #000000 @ 0.05 0px 0px 15.008px 3.008px; div::before.elementor-element.elementor-element-921a16e 1248pxx1px bg #d1d1d1; div.elementor-element.elementor-element-46d7982 368.0x557.2 border R:1px solid #d1d1d1; a.elementor-element.elementor-element-425e4ad 343.0x204.2 image linear-gradient(297deg, #620856 9.99%, #1b0317 60.15%) r 8px; div.elementor-element.elementor-element-c576406 295.0x57.0 image linear-gradient(88deg, #ffffff 7.73%, #d67fc8 157.58%); hr.e-17c71e6-282d567.e-divider-base 343.0x1.0 bg #d1d1d1 |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A product link inside the opened mega-menu columns.

Page: home. Selector: `mega-menu content a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 250.66 x 84.81 | = | = | = |
| Padding | 16px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #fae4fa | #fae4fa | #fae4fa |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | div.elementor-heading-title.elementor-size-default: Roobert 14px/22.4px 600, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up div.elementor-element.elementor-element-921a16e bg #ffffff shadow #000000 @ 0.05 0px 0px 15.008px 3.008px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.elementor-element.elementor-element-30424c5 250.7x84.8 bg #fae4fa r 8px | a.elementor-element.elementor-element-30424c5 250.7x84.8 bg #fae4fa r 8px outline 2px auto #005fcc offset 2px | a.elementor-element.elementor-element-30424c5 250.7x84.8 bg #fae4fa r 8px |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

#### menu-feature

Menu feature tile. The large featured tile inside the mega-menu (the Agent Ready Scanner promo).

Page: home. Selector: `mega-menu featured tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 343 x 204.22 | = | = | = |
| Padding | 40px 24px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(297deg, #620856 9.99%, #1b0317 60.15%) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.elementor-heading-title.elementor-size-default: Roobert 14px/22.4px 400, #ffffff, ls 0.7px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.elementor-element.elementor-element-425e4ad 343.0x204.2 image linear-gradient(297deg, #620856 9.99%, #1b0317 60.15%) r 8px; div.elementor-element.elementor-element-c576406 295.0x57.0 image linear-gradient(88deg, #ffffff 7.73%, #d67fc8 157.58%) | = | a.elementor-element.elementor-element-425e4ad 343.0x204.2 image linear-gradient(297deg, #620856 9.99%, #1b0317 60.15%) r 8px outline 2px auto #005fcc offset 2px; div.elementor-element.elementor-element-c576406 295.0x57.0 image linear-gradient(88deg, #ffffff 7.73%, #d67fc8 157.58%) | = |
| Ancestor paint | 2 up div.elementor-element.elementor-element-921a16e bg #ffffff shadow #000000 @ 0.05 0px 0px 15.008px 3.008px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-feature-default.png`, `menu-feature-hover.png`, `menu-feature-focus-visible.png`, `menu-feature-pressed.png`.

### Home hero

#### hero-title

Hero headline. The 88px Roobert white display headline over the photo hero (a .dark-mode island).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 880 x 193.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 88px/96.8px 600 |
| Letter spacing | -0.88px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-lede

Hero copy. The lede under the hero headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 20px/28px 400 |
| Letter spacing | normal |
| Colour | #f6f6f6 |
| Transition | none |
| Ancestor paint | 1 up div.elementor-element.elementor-element-5i423sx8e bg #000000 |
| How | at rest |

Crops: `hero-lede-default.png`.

#### hero-cta

Hero CTA. The white Get-started pill in the dark hero (dsm-button-primary inverted by the .dark-mode scope); measured never followed.

Page: home. Selector: `section.dark-mode a "Get started"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.36 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #ed01ee | #ed01ee | #ed01ee |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 18px/25.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | #ffffff | #ffffff |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dsm-btn-wrapper.e-23010b6-4d410a3 140.4x48.0 bg #ffffff r 8px | a.dsm-btn-wrapper.e-23010b6-4d410a3 140.4x48.0 bg #ed01ee r 8px | a.dsm-btn-wrapper.e-23010b6-4d410a3 140.4x48.0 bg #ed01ee r 8px outline 2px auto #005fcc offset 2px | a.dsm-btn-wrapper.e-23010b6-4d410a3 140.4x48.0 bg #ed01ee r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-stage

Hero stage. The full-viewport video hero (the first .dark-mode island) behind the headline; its paint is the hosted <video> plus the swap overlay, not a background.

Page: home. Selector: `section.dark-mode (first)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 88px 96px |
| Gap | 48px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.g-0f57b66.g-0c75c4e: Roobert 56px/61.6px 600, #ffffff @ 0.3, ls -0.56px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 2700) |
| Icon | 48 x 48, colour #000000 |
| Painted layers | section.elementor-element.elementor-element-e7079fd 1440.0x900.0 bg #000000 |
| How | at rest |

Crops: none.

### Home

#### h2-section

Section heading. A Roobert section heading in the page body.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 576 x 62.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 24px/31.2px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `h2-section-default.png`.

#### card

Card. A dsm card tile (1rem radius, white fill).

Page: home. Selector: `.dsm-card-wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 183.67 |
| Padding | 24px |
| Border | none |
| Radius | 16px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.dsm-title-md.e-heading-base: Roobert 32px/35.2px 600, #f6f6f6 |
| Transition | none |
| Painted layers | div.elementor-element.elementor-element-5i423sx8e 400.0x183.7 bg #000000 r 16px |
| How | at rest |

Crops: `card-default.png`.

#### icon-item

Icon list item. A dsm icon-list row (glyph + label).

Page: home. Selector: `.dsm-icon-list-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 228.8 x 27.59 |
| Padding | 0px 0px 8px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.elementor-icon-list-text: Roobert 14px/19.6px 400, #f6f6f6 |
| Transition | none |
| How | at rest |

Crops: `icon-item-default.png`.

#### cta-dark

Dark CTA. A black dsm-button-primary pill on a light section; measured never followed.

Page: home. Selector: `light-section a.dsm-btn-wrapper`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 141.72 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | #ed01ee | #ed01ee | #ed01ee |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 18px/25.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dsm-btn-wrapper.dsm-button-primary 141.7x48.0 bg #000000 r 8px | a.dsm-btn-wrapper.dsm-button-primary 141.7x48.0 bg #ed01ee r 8px | a.dsm-btn-wrapper.dsm-button-primary 141.7x48.0 bg #ed01ee r 8px outline 2px auto #005fcc offset 2px | a.dsm-btn-wrapper.dsm-button-primary 141.7x48.0 bg #ed01ee r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-dark-default.png`, `cta-dark-hover.png`, `cta-dark-focus-visible.png`, `cta-dark-pressed.png`.

### Pricing

#### pricing-h1

Pricing title. The pricing page heading.

Page: pricing. Selector: `h1/h2 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 306.75 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 20px/26px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### plan-name

Plan name. A plan card name (Essential/Advanced Solo/Advanced).

Page: pricing. Selector: `plan name heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 247 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 20px/32px 600 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. A plan card price figure.

Page: pricing. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 73.08 x 40 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 14px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Roobert 40px/40px 600, #000000 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card Buy-now action; measured never followed (it would open checkout).

Page: pricing. Selector: `"Buy now"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 247 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #000000 | 2px solid #ed01ee | 2px solid #ed01ee | 2px solid #ed01ee |
| Radius | 8px | = | = | = |
| Background | transparent | #ed01ee | #ed01ee | #ed01ee |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 18px/52px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | #ffffff | #ffffff |
| Text node | span.elementor-button-text: Roobert 18px/52px 500, #000000 | span.elementor-button-text: Roobert 18px/52px 500, #ffffff | span.elementor-button-text: Roobert 18px/52px 500, #ffffff | span.elementor-button-text: Roobert 18px/52px 500, #ffffff |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.elementor-button.elementor-button-link 247.0x56.0 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 8px | a.elementor-button.elementor-button-link 247.0x56.0 bg #ed01ee border T:2px solid #ed01ee / R:2px solid #ed01ee / B:2px solid #ed01ee / L:2px solid #ed01ee r 8px | a.elementor-button.elementor-button-link 247.0x56.0 bg #ed01ee border T:2px solid #ed01ee / R:2px solid #ed01ee / B:2px solid #ed01ee / L:2px solid #ed01ee r 8px outline 2px auto #005fcc offset 2px | a.elementor-button.elementor-button-link 247.0x56.0 bg #ed01ee border T:2px solid #ed01ee / R:2px solid #ed01ee / B:2px solid #ed01ee / L:2px solid #ed01ee r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-card

Plan card. A pricing plan card: white 8px-radius tile holding the plan name, price, Buy-now action, the variant toggle and the feature list.

Page: pricing. Selector: `.e-loop-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 297 x 1024.33 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Roobert 14px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.elementor-heading-title.elementor-size-default: Roobert 20px/32px 600, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.elementor.elementor-8299265 297.0x1024.3 bg #ffffff r 8px; section.elementor-element.elementor-element-ac2d3b5 297.0x1024.3 bg #ffffff border T:1px solid #d1d1d1 / R:1px solid #d1d1d1 / B:1px solid #d1d1d1 / L:1px solid #d1d1d1 r 8px; strong 0.0x0.0 bg #69d784 r 16px; strong 0.0x0.0 bg #69d784 r 16px; a.elementor-button.elementor-button-link 247.0x56.0 border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 8px; li::before.plan__features__item.sites 16pxx21px image url(data:…) |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-toggle

Billing toggle. A plan variant toggle inside a plan card (Advanced/Expert, One/One Agency); measured, never switched into a purchase.

Page: pricing. Selector: `button.plan-toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.5 x 34 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 16px/34px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #212121 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | pointer | pointer | pointer |
| Painted layers | button.plan-toggle.active 119.5x34.0 bg #ffffff r 8px | = | button.plan-toggle.active 119.5x34.0 bg #ffffff r 8px outline 2px auto #005fcc offset 2px | = |
| Ancestor paint | 1 up div.plan-toggle-wrap bg #ebebeb | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-toggle-default.png`, `plan-toggle-hover.png`, `plan-toggle-focus-visible.png`, `plan-toggle-pressed.png`.

#### feature-row

Feature row. A plan feature row with its included/not-included marker.

Page: pricing. Selector: `li.plan__features__item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 247 x 19.59 |
| Padding | 0px 0px 0px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 14px/19.6px 400 |
| Letter spacing | normal |
| Colour | #212121 |
| Text node | b: Roobert 14px/19.6px 700, #212121 |
| Transition | none |
| ::before | 16px x 21px, absolute, bg #000000 @ 0 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='none'%3E%3Cpath d='M19 17.36, radius 0px |
| Painted layers | li::before.plan__features__item.sites 16pxx21px image url(data:…) |
| How | at rest |

Crops: `feature-row-default.png`.

### Contact form

#### contact-h1

Contact title. The Contact-us page heading.

Page: contact. Selector: `h1/h2 on /contact`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 100.69 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 20px/26px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### contact-card

Contact card. A contact-option card (Legal department inquiries form): its own toggle opens the Elementor popup holding the form.

Page: contact. Selector: `[data-action-link*=popup:open]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 280.02 | = | = | = |
| Padding | 32px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #f6f6f6 | transparent | transparent | transparent |
| Box shadow | none | #000000 0px 0px 0px 1px | #000000 0px 0px 0px 1px | #000000 0px 0px 0px 1px |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 18px/25.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3.dsm-title-sm.e-heading-base: Roobert 24px/31.2px 600, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 32 x 32, colour #000000 | = | = | = |
| Painted layers | button.elementor-element.elementor-element-b206526 400.0x280.0 bg #f6f6f6 r 16px | button.elementor-element.elementor-element-b206526 400.0x280.0 r 16px shadow #000000 0px 0px 0px 1px | button.elementor-element.elementor-element-b206526 400.0x280.0 r 16px shadow #000000 0px 0px 0px 1px outline 2px auto #005fcc offset 2px | button.elementor-element.elementor-element-b206526 400.0x280.0 r 16px shadow #000000 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `contact-card-default.png`, `contact-card-hover.png`, `contact-card-focus-visible.png`, `contact-card-pressed.png`.

#### form-popup

Form popup. The Elementor popup dialog holding the contact form, opened by its card.

Page: contact. Selector: `[data-elementor-type=popup] (open)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 602 x 720.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong: Roobert 40px/52px 900, #000000 |
| Transition | none |
| Icon | 48 x 48, colour #000000 |
| Painted layers | a.elementor-icon 48.0x48.0 bg #f6f6f6 r 50%; input.elementor-field.elementor-size-sm 249.0x40.4 bg #ffffff border T:1px solid #d1d1d1 / R:1px solid #d1d1d1 / B:1px solid #d1d1d1 / L:1px solid #d1d1d1 r 4px; input.elementor-field.elementor-size-sm 249.0x40.4 bg #ffffff border T:1px solid #d1d1d1 / R:1px solid #d1d1d1 / B:1px solid #d1d1d1 / L:1px solid #d1d1d1 r 4px; input.elementor-field.elementor-size-sm 522.0x40.4 bg #ffffff border T:1px solid #d1d1d1 / R:1px solid #d1d1d1 / B:1px solid #d1d1d1 / L:1px solid #d1d1d1 r 4px; textarea.elementor-field-textual.elementor-field 522.0x107.6 bg #ffffff border T:1px solid #d1d1d1 / R:1px solid #d1d1d1 / B:1px solid #d1d1d1 / L:1px solid #d1d1d1 r 4px; input.elementor-field.elementor-size-sm 16.0x16.0 bg #ffffff |
| How | at rest |

Crops: `form-popup-default.png`.

#### field-name

Name field. The full-name text input; sample text typed and deleted, nothing sent.

Page: contact. Selector: `input#form-field-full_name`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 249 x 40.41 | = | = |
| Padding | 8px | = | = |
| Border | 1px solid #d1d1d1 | 1px solid #000000 | 1px solid #000000 |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #e2e2e2 0px 0px 6px 0px | #e2e2e2 0px 0px 6px 0px |
| Outline | none | = | = |
| Font | Roobert 16px/22.4px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000, opacity 1 | = | = |
| Painted layers | input.elementor-field.elementor-size-sm 249.0x40.4 bg #ffffff border T:1px solid #d1d1d1 / R:1px solid #d1d1d1 / B:1px solid #d1d1d1 / L:1px solid #d1d1d1 r 4px | input.elementor-field.elementor-size-sm 249.0x40.4 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px shadow #e2e2e2 0px 0px 6px 0px | input.elementor-field.elementor-size-sm 249.0x40.4 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px shadow #e2e2e2 0px 0px 6px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `field-name-default.png`, `field-name-focused.png`, `field-name-filled.png`.

#### field-email

Email field. The email input; focused only, never filled or sent.

Page: contact. Selector: `input#form-field-email`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 249 x 40.41 | = |
| Padding | 8px | = |
| Border | 1px solid #d1d1d1 | 1px solid #000000 |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | none | #e2e2e2 0px 0px 6px 0px |
| Outline | none | = |
| Font | Roobert 16px/22.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input.elementor-field.elementor-size-sm 249.0x40.4 bg #ffffff border T:1px solid #d1d1d1 / R:1px solid #d1d1d1 / B:1px solid #d1d1d1 / L:1px solid #d1d1d1 r 4px | input.elementor-field.elementor-size-sm 249.0x40.4 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px shadow #e2e2e2 0px 0px 6px 0px |
| How | at rest | clicked into the field |

Crops: `field-email-default.png`, `field-email-focused.png`.

#### field-message

Message area. The message textarea; focused only.

Page: contact. Selector: `textarea.elementor-field`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 522 x 107.63 | = |
| Padding | 8px | = |
| Border | 1px solid #d1d1d1 | 1px solid #000000 |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | none | #e2e2e2 0px 0px 6px 0px |
| Outline | none | = |
| Font | Roobert 16px/22.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | textarea.elementor-field-textual.elementor-field 522.0x107.6 bg #ffffff border T:1px solid #d1d1d1 / R:1px solid #d1d1d1 / B:1px solid #d1d1d1 / L:1px solid #d1d1d1 r 4px | textarea.elementor-field-textual.elementor-field 522.0x107.6 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px shadow #e2e2e2 0px 0px 6px 0px |
| How | at rest | clicked into the field |

Crops: `field-message-default.png`, `field-message-focused.png`.

#### field-select

Department select. The department select; measured, never changed.

Page: contact. Selector: `select.elementor-field`. States: .

Not found on the page at capture time.

#### checkbox

Acceptance checkbox. The acceptance checkbox; checked and unchecked as local UI state — the form was never submitted.

Page: contact. Selector: `input#form-field-acceptance`. States: default, hover, focus-visible, pressed, selected.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | #ffffff | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 2px | = | = |
| Font | Roobert 16px/22.4px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Opacity | 0 | = | = | = | = |
| Cursor | default | = | = | = | = |
| Placeholder | #000000, opacity 1 | = | = | = | = |
| Painted layers | input.elementor-field.elementor-size-sm 16.0x16.0 bg #ffffff | = | input.elementor-field.elementor-size-sm 16.0x16.0 bg #ffffff outline 1px auto #005fcc offset 2px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `checkbox-default.png`, `checkbox-hover.png`, `checkbox-focus-visible.png`, `checkbox-pressed.png`, `checkbox-selected.png`.

#### submit-btn

Submit button. The form submit; measured, never pressed (a real press would send the form).

Page: contact. Selector: `button[type=submit]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.22 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #000000 | #ed01ee | = | #ed01ee |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 18px/48px 500 | = | = | = |
| Letter spacing | -0.36px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.elementor-button-text: Roobert 18px/48px 500, #ffffff, ls -0.36px | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.elementor-button.elementor-size-sm 105.2x48.0 bg #000000 r 8px | button.elementor-button.elementor-size-sm 105.2x48.0 bg #ed01ee r 8px | button.elementor-button.elementor-size-sm 105.2x48.0 bg #000000 r 8px outline 2px auto #005fcc offset 2px | button.elementor-button.elementor-size-sm 105.2x48.0 bg #ed01ee r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `submit-btn-default.png`, `submit-btn-hover.png`, `submit-btn-focus-visible.png`, `submit-btn-pressed.png`.

### FAQ

#### faq-h1

FAQ title. The Frequently-Asked-Questions heading.

Page: faq. Selector: `FAQ heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 901.38 x 79.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 72px/79.2px 600 |
| Letter spacing | -0.72px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `faq-h1-default.png`.

#### faq-item

FAQ item (closed). A question row of the FAQ accordion (aria-expanded toggle).

Page: faq. Selector: `.dsm-faq--title`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1024 x 28 | = | = | = |
| Padding | 0px 80px 0px 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.elementor-heading-title.elementor-size-default: Roobert 20px/28px 700, #212121 | = | = | = |
| Transition | background, border, box-shadow, transform 0.3s, 0.3s, 0.3s, 0.4s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 16px x 16px, absolute, bg #000000 @ 0 linear-gradient(#000000, #000000), linear-gradient(#000000, #000000), radius 0px | = | = | = |
| Painted layers | div::after.elementor-element.elementor-element-52f3298d 16pxx16px image linear-gradient(#000000, #000000), linear-gradient(#000000, #000000) | = | div.elementor-element.elementor-element-52f3298d 1024.0x28.0 outline 1px auto #005fcc offset 0px; div::after.elementor-element.elementor-element-52f3298d 16pxx16px image linear-gradient(#000000, #000000), linear-gradient(#000000, #000000) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`.

#### faq-item-open

FAQ item (open). The same question row after its own toggle opened it.

Page: faq. Selector: `.dsm-faq--title[aria-expanded=true]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 28 |
| Padding | 0px 80px 0px 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.elementor-heading-title.elementor-size-default: Roobert 20px/28px 700, #212121 |
| Transition | background, border, box-shadow, transform 0.3s, 0.3s, 0.3s, 0.4s ease, ease, ease, ease delay 0s, 0s, 0s, 0s |
| Cursor | pointer |
| ::after | 16px x 16px, absolute, bg #000000 @ 0 linear-gradient(#000000, #000000), linear-gradient(#000000, #000000), radius 0px |
| Painted layers | div::after.elementor-element.elementor-element-52f3298d 16pxx16px image linear-gradient(#000000, #000000), linear-gradient(#000000, #000000) |
| How | at rest |

Crops: `faq-item-open-default.png`.

#### faq-answer

FAQ answer. The revealed answer panel.

Page: faq. Selector: `.dsm-faq--faq-content[aria-hidden=false]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 160.03 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.wp-block-paragraph: Roobert 16px/22.4px 400, #212121 |
| Transition | grid-template-rows 0.5s ease |
| How | at rest |

Crops: `faq-answer-default.png`.

### Footer

#### footer

Footer. The dsm-footer (a .dark-mode island): link columns, social icons and legal on black.

Page: home. Selector: `.dsm-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 671.53 |
| Padding | 0px 96px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | b: Roobert 14px/19.6px 700, #ffffff |
| Transition | none |
| Icon | 138.39 x 24, colour #000000 |
| Painted layers | div.elementor-element.elementor-element-471e6fac 1440.0x671.5 bg #000000; a 124.4x17.0 image linear-gradient(#ffffff 0px, #ffffff 0px); a 86.6x17.0 image linear-gradient(#ffffff 0px, #ffffff 0px) |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.36 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #ed01ee | #ed01ee | #ed01ee |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Roobert 18px/25.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | #ffffff | #ffffff |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dsm-btn-wrapper-st.e-69010ca4-c5c945f 140.4x48.0 bg #ffffff r 8px | a.dsm-btn-wrapper-st.e-69010ca4-c5c945f 140.4x48.0 bg #ed01ee r 8px | a.dsm-btn-wrapper-st.e-69010ca4-c5c945f 140.4x48.0 bg #ed01ee r 8px outline 2px auto #005fcc offset 2px | a.dsm-btn-wrapper-st.e-69010ca4-c5c945f 140.4x48.0 bg #ed01ee r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social icon. A footer social-icon link (icon button).

Page: home. Selector: `footer .elementor-social-icon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10% | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #005fcc offset 2px | = |
| Font | Times 24px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #69727d | #ffffff | = | #ffffff |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #69727d, fill #000000 | 24 x 24, colour #ffffff, fill #212121 | = | 24 x 24, colour #ffffff, fill #212121 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |
| Painted layers | - | = | a.elementor-icon.elementor-social-icon 24.0x24.0 r 10% outline 2px auto #005fcc offset 2px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `painted bar inside header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 64 |
| Padding | 0px 16px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.05 0px 0px 15.008px 3.008px |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 144 x 27.83, colour #0000ee |
| Painted layers | div.elementor-element.elementor-element-7559e775 358.0x64.0 bg #ffffff r 24px shadow #000000 @ 0.05 0px 0px 15.008px 3.008px; div.e-n-menu-wrapper 0.0x0.0 bg #ffffff; div.e-n-menu-title.e-click 0.0x0.0 bg #ffffff border B:1px solid #d1d1d1; div.elementor-element.elementor-element-921a16e 0.0x0.0 bg #ffffff; div::before.elementor-element.elementor-element-921a16e 100%x1px bg #d1d1d1; div.elementor-element.elementor-element-46d7982 0.0x0.0 border B:1px solid #d1d1d1 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header hamburger toggle (e-n-menu-toggle).

Page: mobile. Selector: `button.e-n-menu-toggle`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/25.2px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| Icon | 32 x 32, colour #000000, fill #1f2124 |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The header menu panel opened by its own toggle.

Page: mobile. Selector: `#menubar-938 open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 88px 0px 128px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.e-n-menu-title-text: Roobert 14px/19.6px 400, #212121 |
| Transition | max-height 0.3s ease |
| Icon | 20 x 20, colour #212121, fill #000000 @ 0 |
| Painted layers | div.e-n-menu-wrapper 390.0x844.0 bg #ffffff; div.e-n-menu-title.e-click 390.0x52.6 bg #ffffff border B:1px solid #d1d1d1; div.elementor-element.elementor-element-921a16e 0.0x0.0 bg #ffffff; div::before.elementor-element.elementor-element-921a16e 100%x1px bg #d1d1d1; div.elementor-element.elementor-element-46d7982 0.0x0.0 border B:1px solid #d1d1d1; a.elementor-element.elementor-element-425e4ad 0.0x0.0 image linear-gradient(297deg, #620856 9.99%, #1b0317 60.15%) r 8px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. An item inside the opened header menu.

Page: mobile. Selector: `mobile menu item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 52.59 | = | = | = |
| Padding | 16px 32px 16px 36px | = | = | = |
| Gap | 1.92px | = | = | = |
| Border | T: none; R: none; B: 1px solid #d1d1d1; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Roobert 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #212121 | #1f2124 | = | #1f2124 |
| Text node | span.e-n-menu-title-text: Roobert 14px/19.6px 400, #212121 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #212121, fill #000000 @ 0 | 20 x 20, colour #1f2124, fill #000000 @ 0 | = | 20 x 20, colour #1f2124, fill #000000 @ 0 |
| Painted layers | div.e-n-menu-title.e-click 390.0x52.6 bg #ffffff border B:1px solid #d1d1d1 | = | div.e-n-menu-title.e-click 390.0x52.6 bg #ffffff border B:1px solid #d1d1d1; button.e-n-menu-dropdown-icon.e-focus 20.0x19.6 outline 2px auto #005fcc offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326 x 116.16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 35.2px/38.72px 600 |
| Letter spacing | -0.4px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

Elementor's sheets are same-origin uploads/plugins CSS plus inline <style> blocks, so this list holds the transitions the CSSOM could read on each captured page; the per-state Transition rows above are computed values and cover the dsm-* and e-n-menu rules.

- contact: `200ms`, `none`, `opacity 1s`, `0.5s`, `background var(--background-transition,.3s),border var(--border-transition,.3s),box-shadow var(--border-transition,.3s),transform var(--e-con-transform-transition-duration,.4s)`, `var(--overlay-transition,.3s)`, `background var(--overlay-transition,.3s),border-radius var(--border-transition,.3s),opacity var(--overlay-transition,.3s)`, `background .3s,border .3s,border-radius .3s,box-shadow .3s,transform var(--e-transform-transition-duration,.4s)`, `0.3s`, `unset`, `block-size 0.3s, content-visibility 0.3s allow-discrete`, `transform 0.3s`

- faq: `200ms`, `none`, `opacity 1s`, `0.5s`, `background var(--background-transition,.3s),border var(--border-transition,.3s),box-shadow var(--border-transition,.3s),transform var(--e-con-transform-transition-duration,.4s)`, `var(--overlay-transition,.3s)`, `background var(--overlay-transition,.3s),border-radius var(--border-transition,.3s),opacity var(--overlay-transition,.3s)`, `background .3s,border .3s,border-radius .3s,box-shadow .3s,transform var(--e-transform-transition-duration,.4s)`, `0.3s`, `unset`, `block-size 0.3s, content-visibility 0.3s allow-discrete`, `transform 0.3s`

- home: `200ms`, `none`, `opacity 1s`, `0.5s`, `background var(--background-transition,.3s),border var(--border-transition,.3s),box-shadow var(--border-transition,.3s),transform var(--e-con-transform-transition-duration,.4s)`, `var(--overlay-transition,.3s)`, `background var(--overlay-transition,.3s),border-radius var(--border-transition,.3s),opacity var(--overlay-transition,.3s)`, `background .3s,border .3s,border-radius .3s,box-shadow .3s,transform var(--e-transform-transition-duration,.4s)`, `0.3s`, `unset`, `block-size 0.3s, content-visibility 0.3s allow-discrete`, `transform 0.3s`

- pricing: `200ms`, `none`, `opacity 1s`, `0.5s`, `background var(--background-transition,.3s),border var(--border-transition,.3s),box-shadow var(--border-transition,.3s),transform var(--e-con-transform-transition-duration,.4s)`, `var(--overlay-transition,.3s)`, `background var(--overlay-transition,.3s),border-radius var(--border-transition,.3s),opacity var(--overlay-transition,.3s)`, `background .3s,border .3s,border-radius .3s,box-shadow .3s,transform var(--e-transform-transition-duration,.4s)`, `0.3s`, `unset`, `block-size 0.3s, content-visibility 0.3s allow-discrete`, `transform 0.3s`
