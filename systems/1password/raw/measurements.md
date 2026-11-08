# Component measurements

Computed styles read from 1password.com on 2026-11-08 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-strip

Announcement strip. The tan strip above the header: "1Password for Agents" copy with a Learn more link and a Sign in link at the far right.

Page: home. Selector: `top strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 587.69 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.box-decoration-clone.pb-0.5: agileSans 16px/24px 350, #303136 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.box-decoration-clone.pb-0.5 587.7x23.0 image linear-gradient(#303136, #303136); span::after 12pxx12px bg #303136 |
| How | at rest |

Crops: `promo-strip-default.png`.

#### promo-link

Announcement link.

Page: home. Selector: `strip Learn more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 587.69 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px | = |
| Font | agileSans 16px/24px 350 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.box-decoration-clone.pb-0.5: agileSans 16px/24px 350, #303136 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.box-decoration-clone.pb-0.5 587.7x23.0 image linear-gradient(#303136, #303136); span::after 12pxx12px bg #303136 | = | a.header-navigation__nav-banner-link.[&>span]:text-wrap 587.7x24.0 outline 1px auto #005fcc offset 4px; span.box-decoration-clone.pb-0.5 587.7x23.0 image linear-gradient(#303136, #303136); span::after 12pxx12px bg #303136 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `promo-link-default.png`, `promo-link-hover.png`, `promo-link-focus-visible.png`, `promo-link-pressed.png`.

#### signin-link

Sign in link. The sign-in link at the strip's far right; points at my.1password.com.

Page: home. Selector: `a Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 49.2 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px | = |
| Font | agileSans 16px/24px 350 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.box-decoration-clone.pb-0.5: agileSans 16px/24px 350, #303136 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.box-decoration-clone.pb-0.5 49.2x23.0 image linear-gradient(#303136, #303136) | = | a.group/nav-item.focus-visible:outline-offset-[4px] 49.2x24.0 outline 1px auto #005fcc offset 4px; span.box-decoration-clone.pb-0.5 49.2x23.0 image linear-gradient(#303136, #303136) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-link-default.png`, `signin-link-hover.png`, `signin-link-focus-visible.png`, `signin-link-pressed.png`.

#### header

Header. The white sticky bar (header-navigation): wordmark, Business/Personal/Developers/Partners/Resources flyout buttons, Pricing link, then Talk to sales and the blue Get started free pill.

Page: home. Selector: `header.header-navigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.box-decoration-clone.pb-0.5: agileSans 16px/24px 350, #303136 |
| Transition | none |
| Icon | 12 x 12, colour #303136 |
| Painted layers | nav.header-navigation.relative 1440.0x132.0 bg #ffffff; div.flex.w-full 1440.0x56.0 bg #cbb88e; span.box-decoration-clone.pb-0.5 587.7x23.0 image linear-gradient(#303136, #303136); span::after 12pxx12px bg #303136; span.box-decoration-clone.pb-0.5 49.2x23.0 image linear-gradient(#303136, #303136); button.group/nav-item.inline-flex 78.1x28.0 image linear-gradient(#000000, #000000) |
| How | at rest |

Crops: `header-default.png`.

#### logo

Wordmark.

Page: home. Selector: `header logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 143 x 27.33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| How | at rest |

Crops: `logo-default.png`.

#### nav-flyout-button

Nav flyout button. A group/nav-item button (Business, Personal, Developers, Partners, Resources); opens the mega flyout on hover.

Page: home. Selector: `button.group/nav-item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.09 x 28 | = | = | = |
| Padding | 2px 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#000000, #000000) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 3px | = |
| Font | agileSans 16px/24px 350 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-iron-ore-new-800.text-opacity-100: agileSans 16px/24px 400, #303136, ls -0.32px | = | = | = |
| Transition | background-size 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #303136 | = | = | = |
| Painted layers | button.group/nav-item.inline-flex 78.1x28.0 image linear-gradient(#000000, #000000) | = | button.group/nav-item.inline-flex 78.1x28.0 image linear-gradient(#000000, #000000) outline 1px auto #005fcc offset 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-flyout-button-default.png`, `nav-flyout-button-hover.png`, `nav-flyout-button-focus-visible.png`, `nav-flyout-button-pressed.png`.

#### nav-flyout

Nav flyout. The mega panel a nav group opens on click (Business, Personal, ...): product and feature links in columns.

Page: home. Selector: `header-navigation__dropdown`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 1248 x 675 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.text-iron-ore-new-500.text-opacity-100: agileSans 16px/20px 300, #6c6e7a |
| Transition | all 0.3s cubic-bezier(0, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | div.header-navigation__dropdown-container.bg-pure-white 1248.0x675.0 bg #ffffff border T:1px solid #e7e7e9 / R:1px solid #e7e7e9 / B:1px solid #e7e7e9 / L:1px solid #e7e7e9 r 12px shadow #000000 @ 0.1 0px 6px 14px 0px, #000000 @ 0.09 0px 26px 26px 0px, #000000 @ 0.05 0px 58px 35px 0px, #000000 @ 0.01 0px 104px 41px 0px, #000000 @ 0 0px 162px 45px 0px; div.m-0.h-[26px] 20.0x26.0 bg #303136; span.box-decoration-clone.pb-0.5 62.1x23.0 image linear-gradient(#303136, #303136); div.m-0.h-[26px] 20.0x26.0 bg #303136; span.box-decoration-clone.pb-0.5 72.8x23.0 image linear-gradient(#303136, #303136); div.m-0.h-[26px] 20.0x26.0 bg #303136 |
| How | at rest |

Crops: `nav-flyout-open.png`.

#### nav-link

Nav link. A plain text nav item (Pricing).

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 155.98 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px | = |
| Font | agileSans 16px/24px 350 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.box-decoration-clone.pb-0.5: agileSans 16px/24px 400, #303136, ls -0.32px | span.box-decoration-clone.pb-0.5: agileSans 16px/24px 400, #145fe4, ls -0.32px | = | span.box-decoration-clone.pb-0.5: agileSans 16px/24px 400, #145fe4, ls -0.32px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.m-0.h-[26px] 20.0x26.0 bg #303136; span.box-decoration-clone.pb-0.5 48.2x23.0 image linear-gradient(#303136, #303136) | div.m-0.h-[26px] 20.0x26.0 bg #145fe3; span.box-decoration-clone.pb-0.5 48.2x23.0 image linear-gradient(#145fe4, #145fe4) | a.group/nav-item.focus-visible:outline-offset-[4px] 156.0x21.0 outline 1px auto #005fcc offset 4px; div.m-0.h-[26px] 20.0x26.0 bg #145fe3; span.box-decoration-clone.pb-0.5 48.2x23.0 image linear-gradient(#303136, #303136) | div.m-0.h-[26px] 20.0x26.0 bg #145fe4; span.box-decoration-clone.pb-0.5 48.2x23.0 image linear-gradient(#145fe4, #145fe4) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### cta-header-primary

Header primary CTA. The blue cta-btn pill at the header's far right ("Get started free").

Page: home. Selector: `header .cta-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 168.53 x 46 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #145fe4 | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #145fe4 offset 3px | = |
| Font | agileSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #145fe4 | #145fe4 | #145fe4 |
| Text node | span: agileSans 16px/24px 400, #ffffff | span: agileSans 16px/24px 400, #145fe4 | span: agileSans 16px/24px 400, #145fe4 | span: agileSans 16px/24px 400, #145fe4 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = | = | = |
| ::before | 166.531px x 44px, absolute, bg #145fe4, radius 9999px | 174.531px x 52px, absolute, bg #145fe4, radius 9999px | = | 174.531px x 52px, absolute, bg #145fe4, radius 9999px |
| ::after | 166.531px x 44px, absolute, bg #000000 @ 0, radius 9999px | 174.531px x 52px, absolute, bg #000000 @ 0, radius 9999px | = | 174.531px x 52px, absolute, bg #000000 @ 0, radius 9999px |
| Painted layers | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 166.531pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 166.531pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 174.531pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 174.531pxx52px border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px outline 1px solid #145fe4 offset 3px; a::before.cta-btn.flex-1 166.531pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 166.531pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 174.531pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 174.531pxx52px border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-header-primary-default.png`, `cta-header-primary-hover.png`, `cta-header-primary-focus-visible.png`, `cta-header-primary-pressed.png`.

#### cta-header-sales

Header sales link.

Page: home. Selector: `header a Talk to sales`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.83 x 28 | = | = | = |
| Padding | 2px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 4px | = |
| Font | agileSans 16px/24px 350 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.box-decoration-clone.pb-0.5: agileSans 16px/24px 400, #303136, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.box-decoration-clone.pb-0.5 86.8x23.0 image linear-gradient(#303136, #303136) | = | a.py-0.5.group/nav-item 86.8x28.0 outline 1px auto #005fcc offset 4px; span.box-decoration-clone.pb-0.5 86.8x23.0 image linear-gradient(#303136, #303136) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-header-sales-default.png`, `cta-header-sales-hover.png`, `cta-header-sales-focus-visible.png`, `cta-header-sales-pressed.png`.

#### footer

Footer. The footer: link columns, legal row, social icons.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1276.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #1d1d21 |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/25.6px 350 |
| Letter spacing | -0.32px |
| Colour | #ffffff @ 0.8 |
| Text node | p.text-base.!leading-[150%]: agileSans 16px/24px 300, #ffffff, ls -0.32px |
| Transition | none |
| Icon | 16 x 16, colour #ffffff @ 0.8 |
| Painted layers | footer.text-base.leading-[160%] 1440.0x1276.7 bg #1d1d21; div.absolute.left-0 0.0x0.0 bg #ffffff border T:1px solid #f2f2f3 / R:1px solid #f2f2f3 / B:1px solid #f2f2f3 / L:1px solid #f2f2f3 r 4px; div.flex.items-center 0.0x0.0 bg #f6f8fc r 4px outline 2px solid #3b66bc offset 0px; div.flex.items-center 0.0x0.0 bg #ffffff; div.flex.items-center 0.0x0.0 bg #ffffff; div.flex.items-center 0.0x0.0 bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

### Home

#### hero

Hero. The opening band on bg-hero-gradient-blue: oversized display headline, sub copy and the CTA row on a dark field above the product collage.

Page: home. Selector: `section.bg-hero-gradient-blue`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 1222.39 |
| Padding | 0px 24px |
| Border | none |
| Radius | 0px 0px 48px 48px |
| Background | transparent |
| Background image | linear-gradient(#1d1d21 0px, #1d1d21 25%, #145fe4 70%, #99beff 100%) |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.text-5xl.xs:text-[64px]: agileSans 88px/96.8px 300, #ffffff, ls -1.76px |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | div.h-full.w-full 1392.0x1222.4 image linear-gradient(#1d1d21 0px, #1d1d21 25%, #145fe4 70%, #99beff 100%) r 0px 0px 48px 48px; a.cta-btn.flex-1 204.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 202pxx44px bg #ffffff r 9999px; a::after.cta-btn.flex-1 202pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.cta-btn.flex-1 204.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 202pxx44px bg #ffffff r 9999px |
| Ancestor paint | 1 up header.flex.flex-col bg #1d1d21 |
| How | at rest |

Crops: `hero-default.png`.

#### hero-title

Hero title. Display copy in agileSans, ~88px light.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 822 x 290.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 88px/96.8px 300 |
| Letter spacing | -1.76px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### cta-hero-primary

Hero primary CTA. The white cta-btn pill in the hero ("Talk to sales").

Page: home. Selector: `hero .cta-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 204 x 46 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ffffff | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 3px | = |
| Font | agileSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #145fe4 | #ffffff | #ffffff | #ffffff |
| Text node | span: agileSans 16px/24px 400, #145fe4 | span: agileSans 16px/24px 400, #ffffff | span: agileSans 16px/24px 400, #ffffff | span: agileSans 16px/24px 400, #ffffff |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = | = | = |
| ::before | 202px x 44px, absolute, bg #ffffff, radius 9999px | 210px x 52px, absolute, bg #ffffff, radius 9999px | = | 210px x 52px, absolute, bg #ffffff, radius 9999px |
| ::after | 202px x 44px, absolute, bg #000000 @ 0, radius 9999px | 210px x 52px, absolute, bg #000000 @ 0, radius 9999px | = | 210px x 52px, absolute, bg #000000 @ 0, radius 9999px |
| Painted layers | a.cta-btn.flex-1 204.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 202pxx44px bg #ffffff r 9999px; a::after.cta-btn.flex-1 202pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 204.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 210pxx52px bg #ffffff r 9999px; a::after.cta-btn.flex-1 210pxx52px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px | a.cta-btn.flex-1 204.0x46.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px outline 1px solid #ffffff offset 3px; a::before.cta-btn.flex-1 202pxx44px bg #ffffff r 9999px; a::after.cta-btn.flex-1 202pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 204.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 210pxx52px bg #ffffff r 9999px; a::after.cta-btn.flex-1 210pxx52px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-hero-primary-default.png`, `cta-hero-primary-hover.png`, `cta-hero-primary-focus-visible.png`, `cta-hero-primary-pressed.png`.

#### cta-hero-secondary

Hero secondary CTA. The bordered outline pill beside the primary ("View plans").

Page: home. Selector: `hero secondary cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 204 x 46 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 3px | = |
| Font | agileSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #1d1d21 | #1d1d21 | #1d1d21 |
| Text node | span: agileSans 16px/24px 400, #ffffff | span: agileSans 16px/24px 400, #1d1d21 | span: agileSans 16px/24px 400, #1d1d21 | span: agileSans 16px/24px 400, #1d1d21 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = | = | = |
| ::before | 202px x 44px, absolute, bg #ffffff, radius 9999px | 210px x 52px, absolute, bg #ffffff, radius 9999px | = | 210px x 52px, absolute, bg #ffffff, radius 9999px |
| ::after | 202px x 44px, absolute, bg #000000 @ 0, radius 9999px | 210px x 52px, absolute, bg #000000 @ 0, radius 9999px | = | 210px x 52px, absolute, bg #000000 @ 0, radius 9999px |
| Painted layers | a.cta-btn.flex-1 204.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 202pxx44px bg #ffffff r 9999px; a::after.cta-btn.flex-1 202pxx44px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px | a.cta-btn.flex-1 204.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 210pxx52px bg #ffffff r 9999px; a::after.cta-btn.flex-1 210pxx52px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px | a.cta-btn.flex-1 204.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #ffffff offset 3px; a::before.cta-btn.flex-1 202pxx44px bg #ffffff r 9999px; a::after.cta-btn.flex-1 202pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 204.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 210pxx52px bg #ffffff r 9999px; a::after.cta-btn.flex-1 210pxx52px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-hero-secondary-default.png`, `cta-hero-secondary-hover.png`, `cta-hero-secondary-focus-visible.png`, `cta-hero-secondary-pressed.png`.

#### video-embed

Video embed. The hero product video: a cross-origin Vimeo iframe. The element's box and style were measured; its contents are unreachable (cross-origin), so nothing inside is claimed.

Page: home. Selector: `iframe[src*=vimeo]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1248 x 702 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `video-embed-default.png`.

#### section-title

Section title.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 822 x 211.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 64px/70.4px 300 |
| Letter spacing | -1.28px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 571.03 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 64px/70.4px 300 |
| Letter spacing | -1.28px |
| Colour | #303136 |
| Text node | span: agileSans 64px/70.4px 300, #303136, ls -1.28px |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-selector

Plan selector. The large bordered pill beside the h1 that switches the grid between Enterprise / Business / Individual & Family.

Page: pricing. Selector: `plan pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 378.53 x 98.41 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | agileSans 16px/24px 350 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.whitespace-nowrap: agileSans 64px/70.4px 300, #145fe4, ls -1.28px | = | = | = |
| Transition | none | = | = | = |
| Icon | 48 x 48, colour #145fe4 | = | = | = |
| Painted layers | div.border-2.border-secure-blue 378.5x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.rounded-b-20.border-2 378.5x309.2 border R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 0px 0px 20px 20px; div.inline-block.w-max 378.5x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.inline-block.w-max 338.0x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.inline-block.w-max 332.2x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.inline-flex.w-full 378.5x98.4 bg #ffffff border T:2px solid #d7d7db / R:2px solid #d7d7db / B:2px solid #d7d7db / L:2px solid #d7d7db r 20px | div.border-2.border-secure-blue 378.5x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.rounded-b-20.border-2 378.5x309.2 border R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 0px 0px 20px 20px; div.inline-block.w-max 378.5x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.inline-block.w-max 338.0x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.inline-block.w-max 332.2x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.inline-flex.w-full 378.5x98.4 bg #ffffff border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px | div.group/segment-selector.relative 378.5x98.4 outline 2px solid #000000 @ 0 offset 2px; div.border-2.border-secure-blue 378.5x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.rounded-b-20.border-2 378.5x309.2 border R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 0px 0px 20px 20px; div.inline-block.w-max 378.5x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.inline-block.w-max 338.0x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px; div.inline-block.w-max 332.2x98.4 border T:2px solid #145fe4 / R:2px solid #145fe4 / B:2px solid #145fe4 / L:2px solid #145fe4 r 20px 20px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-selector-default.png`, `plan-selector-hover.png`, `plan-selector-focus-visible.png`, `plan-selector-pressed.png`.

#### product-column

Product column. One column of the platform/product pricing grid: kicker, product name, blurb, CTA pill and a feature list.

Page: pricing. Selector: `pricing grid column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 248.8 x 563.59 |
| Padding | 24px 0px 0px 0px |
| Border | T: none; R: 2px solid #e7e7e9; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.text-base.!leading-[125%]: agileSans 16px/20px 300, #303136 |
| Transition | none |
| Painted layers | div.grid-rows.relative 248.8x563.6 border R:2px solid #e7e7e9; a.cta-btn.flex-1 217.2x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 215.172pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 215.172pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| Ancestor paint | 1 up div.p-0.md:grid bg #ffffff |
| How | at rest |

Crops: `product-column-default.png`.

#### product-name

Product name.

Page: pricing. Selector: `column product name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 217.17 x 57.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 24px/28.8px 400 |
| Letter spacing | -0.48px |
| Colour | #303136 |
| Transition | none |
| How | at rest |

Crops: `product-name-default.png`.

#### cta-quote

Request a quote CTA.

Page: pricing. Selector: `Request a quote`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 217.17 x 46 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #145fe4 | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #145fe4 offset 3px | = |
| Font | agileSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #145fe4 | #145fe4 | #145fe4 |
| Text node | span: agileSans 16px/24px 400, #ffffff | span: agileSans 16px/24px 400, #145fe4 | span: agileSans 16px/24px 400, #145fe4 | span: agileSans 16px/24px 400, #145fe4 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = | = | = |
| ::before | 215.172px x 44px, absolute, bg #145fe4, radius 9999px | 223.172px x 52px, absolute, bg #145fe4, radius 9999px | = | 223.172px x 52px, absolute, bg #145fe4, radius 9999px |
| ::after | 215.172px x 44px, absolute, bg #000000 @ 0, radius 9999px | 223.172px x 52px, absolute, bg #000000 @ 0, radius 9999px | = | 223.172px x 52px, absolute, bg #000000 @ 0, radius 9999px |
| Painted layers | a.cta-btn.flex-1 217.2x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 215.172pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 215.172pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 217.2x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 223.172pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 223.172pxx52px border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px | a.cta-btn.flex-1 217.2x46.0 border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px outline 1px solid #145fe4 offset 3px; a::before.cta-btn.flex-1 215.172pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 215.172pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 217.2x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 223.172pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 223.172pxx52px border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-quote-default.png`, `cta-quote-hover.png`, `cta-quote-focus-visible.png`, `cta-quote-pressed.png`.

#### faq-row

FAQ row. A collapsible question row in the FAQ block.

Page: pricing. Selector: `faq button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.09 x 28 | = | = | = |
| Padding | 2px 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#000000, #000000) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 3px | = |
| Font | agileSans 16px/24px 350 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-iron-ore-new-800.text-opacity-100: agileSans 16px/24px 400, #303136, ls -0.32px | = | = | = |
| Transition | background-size 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #303136 | = | = | = |
| Painted layers | button.group/nav-item.inline-flex 78.1x28.0 image linear-gradient(#000000, #000000) | = | button.group/nav-item.inline-flex 78.1x28.0 image linear-gradient(#000000, #000000) outline 1px auto #005fcc offset 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-row-default.png`, `faq-row-hover.png`, `faq-row-focus-visible.png`, `faq-row-pressed.png`.

#### faq-answer

FAQ answer. The expanded answer body under a FAQ row.

Page: pricing. Selector: `faq panel`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 604 x 104 |
| Padding | 0px 48px 32px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p: agileSans 16px/24px 300, #ffffff, ls -0.32px |
| Transition | all 0.5s cubic-bezier(0.4, 0, 0.2, 1) |
| How | at rest |

Crops: `faq-answer-open.png`.

### Product page

#### product-title

Product title.

Page: product. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 140.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 64px/70.4px 300 |
| Letter spacing | -1.28px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `product-title-default.png`.

#### cta-product-primary

Product primary CTA.

Page: product. Selector: `Get started free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 168.53 x 46 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #145fe4 | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #145fe4 offset 3px | = |
| Font | agileSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #145fe4 | #145fe4 | #145fe4 |
| Text node | span: agileSans 16px/24px 400, #ffffff | span: agileSans 16px/24px 400, #145fe4 | span: agileSans 16px/24px 400, #145fe4 | span: agileSans 16px/24px 400, #145fe4 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = | = | = |
| ::before | 166.531px x 44px, absolute, bg #145fe4, radius 9999px | 174.531px x 52px, absolute, bg #145fe4, radius 9999px | = | 174.531px x 52px, absolute, bg #145fe4, radius 9999px |
| ::after | 166.531px x 44px, absolute, bg #000000 @ 0, radius 9999px | 174.531px x 52px, absolute, bg #000000 @ 0, radius 9999px | = | 174.531px x 52px, absolute, bg #000000 @ 0, radius 9999px |
| Painted layers | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 166.531pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 166.531pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 174.531pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 174.531pxx52px border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px outline 1px solid #145fe4 offset 3px; a::before.cta-btn.flex-1 166.531pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 166.531pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 174.531pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 174.531pxx52px border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-product-primary-default.png`, `cta-product-primary-hover.png`, `cta-product-primary-focus-visible.png`, `cta-product-primary-pressed.png`.

#### feature-card

Feature card. A product-feature card on the marketing page.

Page: product. Selector: `feature card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1392 x 726.41 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 25px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | agileSans 16px/24px 350 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h2.text-[40px].xlRedesign:text-[64px]: agileSans 64px/70.4px 300, #303136, ls -1.28px | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

#### cta-marketplace

Marketplace link. The link to the 1Password Marketplace (marketplace.1password.com) on the product page.

Page: product. Selector: `a Marketplace`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 163.83 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | agileSans 16px/25.6px 350 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #ffffff @ 0.8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.mr-2.hover:underline 163.8x21.0 outline 1px auto #005fcc offset 1px | = |

Crops: `cta-marketplace-default.png`, `cta-marketplace-hover.png`, `cta-marketplace-focus-visible.png`, `cta-marketplace-pressed.png`.

### Downloads

#### download-title

Download title. The display heading "Download 1Password for macOS": the h1 itself is sr-only, so the styled text block was measured instead.

Page: download. Selector: `download heading block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 678.52 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 64px/70.4px 300 |
| Letter spacing | -1.28px |
| Colour | #303136 |
| Transition | none |
| How | at rest |

Crops: `download-title-default.png`.

#### download-button

Download button.

Page: download. Selector: `Download`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 266.52 x 46 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #145fe4 | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #145fe4 offset 3px | = |
| Font | agileSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #145fe4 | #145fe4 | #145fe4 |
| Text node | span: agileSans 16px/24px 400, #ffffff | span: agileSans 16px/24px 400, #145fe4 | span: agileSans 16px/24px 400, #145fe4 | span: agileSans 16px/24px 400, #145fe4 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = | = | = |
| ::before | 264.516px x 44px, absolute, bg #145fe4, radius 9999px | 272.516px x 52px, absolute, bg #145fe4, radius 9999px | = | 272.516px x 52px, absolute, bg #145fe4, radius 9999px |
| ::after | 264.516px x 44px, absolute, bg #000000 @ 0, radius 9999px | 272.516px x 52px, absolute, bg #000000 @ 0, radius 9999px | = | 272.516px x 52px, absolute, bg #000000 @ 0, radius 9999px |
| Painted layers | a.cta-btn.flex-1 266.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 264.516pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 264.516pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 266.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 272.516pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 272.516pxx52px border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px | a.cta-btn.flex-1 266.5x46.0 border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px outline 1px solid #145fe4 offset 3px; a::before.cta-btn.flex-1 264.516pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 264.516pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 266.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 272.516pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 272.516pxx52px border T:1px solid #145fe4 / R:1px solid #145fe4 / B:1px solid #145fe4 / L:1px solid #145fe4 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `download-button-default.png`, `download-button-hover.png`, `download-button-focus-visible.png`, `download-button-pressed.png`.

#### platform-link

Platform link. A link to another platform's download page.

Page: download. Selector: `platform link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96 x 130.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3b66bc offset 2px | = |
| Font | agileSans 16px/24px 350 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.mx-[7px].mt-1: agileSans 15px/22.5px 350, #303136 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.flex.h-[76px] 96.0x96.0 bg #f6f8fc r 12px | div.flex.h-[76px] 96.0x96.0 bg #ffffff r 12px | a.group.flex 96.0x130.5 r 12px outline 2px solid #3b66bc offset 2px; div.flex.h-[76px] 96.0x96.0 bg #f6f8fc r 12px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `platform-link-default.png`, `platform-link-hover.png`, `platform-link-focus-visible.png`, `platform-link-pressed.png`.

#### platform-pill

Platform pill. The macOS platform selector under the title, same segment-selector control as the pricing plan pill.

Page: download. Selector: `macOS pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 377.19 x 121.41 | = | = | = |
| Padding | 8px 8px 0px 8px | = | = | = |
| Border | 4px solid #000000 @ 0 | = | 4px solid #3b66bc | = |
| Radius | 0px | = | 12px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | agileSans 16px/24px 350 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.text-[40px].xs:text-5xl: agileSans 64px/70.4px 350, #3b66bc, ls -1.28px | = | = | = |
| Transition | none | = | = | = |
| Icon | 0 x 0, colour #000000 | = | = | = |
| Painted layers | div.relative.border-[3px] 377.2x121.4 border T:4px solid #000000 @ 0 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0; div.hidden.cursor-pointer 0.0x0.0 border B:1px solid #f2f2f3; div.border-iron-ore-new-50.[&:not(:last-child)]:border-b 0.0x0.0 border B:1px solid #f2f2f3; div.text-sm.!leading-[150%] 0.0x0.0 r 4px outline 2px solid #3b66bc offset 0px; div.border-iron-ore-new-50.[&:not(:last-child)]:border-b 0.0x0.0 border B:1px solid #f2f2f3; div.border-iron-ore-new-50.[&:not(:last-child)]:border-b 0.0x0.0 border B:1px solid #f2f2f3 | = | div.relative.border-[3px] 377.2x121.4 border T:4px solid #3b66bc / R:4px solid #3b66bc / B:4px solid #3b66bc / L:4px solid #3b66bc r 12px outline 2px solid #000000 @ 0 offset 2px; div.hidden.cursor-pointer 0.0x0.0 border B:1px solid #f2f2f3; div.border-iron-ore-new-50.[&:not(:last-child)]:border-b 0.0x0.0 border B:1px solid #f2f2f3; div.text-sm.!leading-[150%] 0.0x0.0 r 4px outline 2px solid #3b66bc offset 0px; div.border-iron-ore-new-50.[&:not(:last-child)]:border-b 0.0x0.0 border B:1px solid #f2f2f3; div.border-iron-ore-new-50.[&:not(:last-child)]:border-b 0.0x0.0 border B:1px solid #f2f2f3 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `platform-pill-default.png`, `platform-pill-hover.png`, `platform-pill-focus-visible.png`, `platform-pill-pressed.png`.

### Developer

#### dev-title

Developer title.

Page: developer. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 140.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 64px/70.4px 300 |
| Letter spacing | -1.28px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `dev-title-default.png`.

#### dev-cta

Developer CTA.

Page: developer. Selector: `developer cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 168.53 x 46 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ffffff | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 3px | = |
| Font | agileSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: agileSans 16px/24px 400, #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = | = | = |
| ::before | 166.531px x 44px, absolute, bg #145fe4, radius 9999px | 174.531px x 52px, absolute, bg #145fe4, radius 9999px | = | 174.531px x 52px, absolute, bg #145fe4, radius 9999px |
| ::after | 166.531px x 44px, absolute, bg #000000 @ 0, radius 9999px | 174.531px x 52px, absolute, bg #000000 @ 0, radius 9999px | = | 174.531px x 52px, absolute, bg #000000 @ 0, radius 9999px |
| Painted layers | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 166.531pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 166.531pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 174.531pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 174.531pxx52px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px outline 1px solid #ffffff offset 3px; a::before.cta-btn.flex-1 166.531pxx44px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 166.531pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | a.cta-btn.flex-1 168.5x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 174.531pxx52px bg #145fe4 r 9999px; a::after.cta-btn.flex-1 174.531pxx52px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dev-cta-default.png`, `dev-cta-hover.png`, `dev-cta-focus-visible.png`, `dev-cta-pressed.png`.

#### dev-card

Developer card. A feature/link card on the developer page.

Page: developer. Selector: `developer card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 405.33 x 384.81 |
| Padding | 0px |
| Border | 1px solid #d7d7db |
| Radius | 25px |
| Background | #f2f2f3 |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.text-2xl.xs:text-[24px]: agileSans 32px/38.4px 300, #303136, ls -0.64px |
| Transition | none |
| Painted layers | div.overflow-hidden.xlRedesign:row-span-2 405.3x384.8 bg #f2f2f3 border T:1px solid #d7d7db / R:1px solid #d7d7db / B:1px solid #d7d7db / L:1px solid #d7d7db r 25px |
| How | at rest |

Crops: `dev-card-default.png`.

### Forms

#### contact-title

Contact title.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 584 x 140.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 64px/70.4px 300 |
| Letter spacing | -1.28px |
| Colour | #303136 |
| Transition | none |
| How | at rest |

Crops: `contact-title-default.png`.

#### field-select

Select field.

Page: contact. Selector: `select`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 128 x 50 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/25.6px 350 |
| Letter spacing | -0.32px |
| Colour | #ffffff @ 0.8 |
| Text node | p.text-base.!leading-[150%]: agileSans 16px/24px 300, #ffffff, ls -0.32px |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #6c6e7a |
| Painted layers | div.absolute.left-0 0.0x0.0 bg #ffffff border T:1px solid #f2f2f3 / R:1px solid #f2f2f3 / B:1px solid #f2f2f3 / L:1px solid #f2f2f3 r 4px; div.flex.items-center 0.0x0.0 bg #f6f8fc r 4px outline 2px solid #3b66bc offset 0px; div.flex.items-center 0.0x0.0 bg #ffffff; div.flex.items-center 0.0x0.0 bg #ffffff; div.flex.items-center 0.0x0.0 bg #ffffff; div.flex.items-center 0.0x0.0 bg #ffffff |
| How | at rest |

Crops: none.

#### form-embed

Sales form embed. The contact form is a Marketo iframe hosted on integrations.1passwordservices.com. The element box was measured; the fields inside are cross-origin and were neither introspected nor submitted.

Page: contact. Selector: `iframe[src*=marketo]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 504 x 915 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `form-embed-default.png`.

### Sign-in boundary

#### unsupported-card

Unsupported-browser page. start.1password.com gates headless/unsupported browsers here instead of the sign-in form. Measured as the honest edge of the public surface; the vault itself is credential-gated and out of scope.

Page: signin. Selector: `unsupported main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter V 15px/18px 400 |
| Letter spacing | -0.45px |
| Colour | #000000 @ 0.82 |
| Text node | h1.default--typography_IPc9L.text06--typography_oBNUp: Inter V 18.75px/21px 600, #000000 @ 0.82, ls -0.5625px |
| Transition | none |
| Icon | 16 x 16, colour #000000 @ 0.82 |
| Painted layers | div 1440.0x900.0 bg #f6f7f8; div::before 32pxx965.094px bg #ffffff shadow #ffffff -1px 0px 0px 0px, #000000 @ 0.13 1px 0px 0px 0px inset, #000000 @ 0.13 -1px 0px 0px 0px inset, #ffffff -2px 0px 0px 0px inset; div::after 32pxx965.094px bg #ffffff shadow #ffffff 1px 0px 0px 0px, #000000 @ 0.13 1px 0px 0px 0px inset, #000000 @ 0.13 -1px 0px 0px 0px inset, #ffffff 2px 0px 0px 0px inset; div.reset_base__1e6d9s10.sprinkles_borderRadius_medium_xs__omrdfn2u 420.0x253.1 bg #fafafa border T:1px solid #000000 @ 0.13 / R:1px solid #000000 @ 0.13 / B:1px solid #000000 @ 0.13 / L:1px solid #000000 @ 0.13 r 8px; div.reset_base__1e6d9s10.sprinkles_alignItems_center_xs__omrdfn7o 18.0x18.0 bg #ebf3ff r 99999px; div.reset_base__1e6d9s10.sprinkles_alignItems_center_xs__omrdfn7o 18.0x18.0 bg #ebf3ff r 99999px |
| Ancestor paint | 1 up body.knox-provider_ltr__kddqqu0.knox-light-mode bg #fafafa |
| How | at rest |

Crops: `unsupported-card-default.png`.

#### unsupported-title

Unsupported title.

Page: signin. Selector: `unsupported heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter V 18.75px/21px 600 |
| Letter spacing | -0.5625px |
| Colour | #000000 @ 0.82 |
| Transition | none |
| How | at rest |

Crops: `unsupported-title-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The 390-wide header bar.

Page: home. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 825.56 |
| Padding | 128px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #1d1d21 |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.text-5xl.xs:text-[64px]: agileSans 48px/52.8px 300, #ffffff, ls -0.96px |
| Transition | none |
| Painted layers | header.flex.flex-col 390.0x825.6 bg #1d1d21; div.h-full.w-full 390.0x697.6 image linear-gradient(#1d1d21 0px, #1d1d21 25%, #145fe4 70%, #99beff 100%); a.cta-btn.flex-1 342.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a::before.cta-btn.flex-1 340pxx44px bg #ffffff r 9999px; a::after.cta-btn.flex-1 340pxx44px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a.cta-btn.flex-1 342.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button. Opens the mobile nav drawer.

Page: home. Selector: `mobile menu button`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 20 x 20 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | agileSans 16px/24px 350 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.group.relative 20.0x20.0 outline 2px solid #000000 @ 0 offset 2px; span.bg-iron-ore-new-800.before:bg-iron-ore-new-800 20.0x2.0 bg #303136 r 2px; span::before.bg-iron-ore-new-800.before:bg-iron-ore-new-800 20pxx2px bg #303136 r 2px; span::after.bg-iron-ore-new-800.before:bg-iron-ore-new-800 20pxx2px bg #303136 r 2px | button.group.relative 20.0x20.0 outline 2px solid #000000 @ 0 offset 2px; span.bg-iron-ore-new-800.before:bg-iron-ore-new-800 20.0x2.0 bg #868893 r 2px; span::before.bg-iron-ore-new-800.before:bg-iron-ore-new-800 20pxx2px bg #868893 r 2px; span::after.bg-iron-ore-new-800.before:bg-iron-ore-new-800 20pxx2px bg #868893 r 2px |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-pressed.png`.

#### m-nav-drawer

Mobile nav drawer. The sheet the menu button opens.

Page: home. Selector: `mobile nav drawer`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 390 x 615 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.box-decoration-clone.pb-0.5: agileSans 24px/28.8px 350, #303136, ls -0.48px |
| Transition | transform 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #303136 |
| Painted layers | div.inline-flex.gap-3 92.7x31.0 image linear-gradient(#000000, #000000); span.box-decoration-clone.pb-0.5 92.7x33.0 image linear-gradient(#303136, #303136); div.inline-flex.gap-3 90.6x31.0 image linear-gradient(#000000, #000000); span.box-decoration-clone.pb-0.5 90.6x33.0 image linear-gradient(#303136, #303136); span.box-decoration-clone.pb-0.5 118.0x33.0 image linear-gradient(#303136, #303136); div.inline-flex.gap-3 89.8x31.0 image linear-gradient(#000000, #000000) |
| How | at rest |

Crops: `m-nav-drawer-open.png`.

#### m-hero-title

Mobile hero title.

Page: home. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 211.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | agileSans 48px/52.8px 300 |
| Letter spacing | -0.96px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

## Transitions declared in the readable stylesheets

1Password's Next.js build serves its CSS same-origin, so this list covers the rules the CSSOM could read on each page (Tailwind utilities and the Knox --knox-* design tokens); the per-state Transition rows above are computed values.

- home: `width 0.3s ease-in-out, background-color 0.3s ease-in-out`, `mask-position 0.3s ease-in-out, background-color 0.3s ease-in-out, -webkit-mask-position 0.3s ease-in-out`, `width 0.5s ease-in-out, background-color 0.5s ease-in-out`, `transform 0.2s ease-out 0.1s, opacity 0.2s ease-out 0.1s`, `transform 0.2s ease-out, opacity 0.2s ease-out`, `inset 0.3s, opacity 0.3s`, `inset 0.3s, border-color 0.3s`, `background-size 0.3s linear`, `width 0.3s ease-in-out`, `opacity 0.3s ease-in-out, transform 0.3s ease-in-out, margin-right 0.3s ease-in-out, width 0.3s ease-in-out`, `opacity 0.3s ease-in-out, width 0.3s ease-in-out, margin-right 0.3s ease-in-out, transform 0.3s ease-in-out`, `none`

- pricing: `width 0.3s ease-in-out, background-color 0.3s ease-in-out`, `mask-position 0.3s ease-in-out, background-color 0.3s ease-in-out, -webkit-mask-position 0.3s ease-in-out`, `width 0.5s ease-in-out, background-color 0.5s ease-in-out`, `transform 0.2s ease-out 0.1s, opacity 0.2s ease-out 0.1s`, `transform 0.2s ease-out, opacity 0.2s ease-out`, `inset 0.3s, opacity 0.3s`, `inset 0.3s, border-color 0.3s`, `background-size 0.3s linear`, `width 0.3s ease-in-out`, `opacity 0.3s ease-in-out, transform 0.3s ease-in-out, margin-right 0.3s ease-in-out, width 0.3s ease-in-out`, `opacity 0.3s ease-in-out, width 0.3s ease-in-out, margin-right 0.3s ease-in-out, transform 0.3s ease-in-out`, `none`

- product: `width 0.3s ease-in-out, background-color 0.3s ease-in-out`, `mask-position 0.3s ease-in-out, background-color 0.3s ease-in-out, -webkit-mask-position 0.3s ease-in-out`, `width 0.5s ease-in-out, background-color 0.5s ease-in-out`, `transform 0.2s ease-out 0.1s, opacity 0.2s ease-out 0.1s`, `transform 0.2s ease-out, opacity 0.2s ease-out`, `inset 0.3s, opacity 0.3s`, `inset 0.3s, border-color 0.3s`, `background-size 0.3s linear`, `width 0.3s ease-in-out`, `opacity 0.3s ease-in-out, transform 0.3s ease-in-out, margin-right 0.3s ease-in-out, width 0.3s ease-in-out`, `opacity 0.3s ease-in-out, width 0.3s ease-in-out, margin-right 0.3s ease-in-out, transform 0.3s ease-in-out`, `none`
