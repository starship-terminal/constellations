# Component measurements

Computed styles read from kitchen.co on 2026-11-18 by tools/capture/measure.mjs, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844).

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Chrome

#### promo-bar

Promo bar. The black campaign strip above the header.

Page: home. Selector: ``. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1440 x 56 | = |
| Padding | 0px 16px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #1d1c1d | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/23.2px 700 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | rest | pointer hover |

Crops: `promo-bar-default.png`, `promo-bar-hover.png`.

#### logo

Wordmark. The Kitchen.co wordmark in the header.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 141 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 18px/26.1px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| How | rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A primary nav link.

Page: home. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.55 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Graphik 16px/23.2px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1d1c1d | = | = | = |
| Text node | text: Graphik 16px/23.2px 700, #1d1c1d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | rest | pointer hover | Shift+Tab, Tab | CDP :hover:active |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### footer

Footer. The site footer.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 795.14 |
| Padding | 100px 0px 70px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.8 |
| Transition | none |
| How | rest |

Crops: `footer-default.png`.

### Buttons

#### nav-login

Log in button. The outline Log in control in the header.

Page: home. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.08 x 44 | = | = | = |
| Padding | 10px 15px | = | = | = |
| Border | 2px solid #1d1c1d | = | = | = |
| Radius | 5px | = | = | = |
| Background | transparent | #1d1c1d | = | #1d1c1d |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Graphik 16px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1d1c1d | #ffffff | = | #ffffff |
| Text node | text: Graphik 16px/20px 700, #1d1c1d | text: Graphik 16px/20px 700, #ffffff | = | text: Graphik 16px/20px 700, #ffffff |
| Transition | background, border-color, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | rest | pointer hover | Shift+Tab, Tab | CDP :hover:active |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-try

Try it free button. The filled ink button in the header.

Page: home. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.02 x 44 | = | = | = |
| Padding | 10px 15px | = | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #1d1c1d | = | 2px solid #1d1c1d |
| Radius | 5px | = | = | = |
| Background | #1d1c1d | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Graphik 16px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #1d1c1d | = | #1d1c1d |
| Text node | text: Graphik 16px/20px 700, #ffffff | text: Graphik 16px/20px 700, #1d1c1d | = | text: Graphik 16px/20px 700, #1d1c1d |
| Transition | background, border-color, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | rest | pointer hover | Shift+Tab, Tab | CDP :hover:active |

Crops: `nav-try-default.png`, `nav-try-hover.png`, `nav-try-focus-visible.png`, `nav-try-pressed.png`.

#### cta-coral

Coral call to action. The coral Get Started link on the home hero.

Page: home. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 270 x 52 | = | = | = |
| Padding | 14px 24px | = | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #ed553b | = | 2px solid #ed553b |
| Radius | 5px | = | = | = |
| Background | #ed553b | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Graphik 18px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #ed553b | = | #ed553b |
| Text node | text: Graphik 18px/20px 700, #ffffff | text: Graphik 18px/20px 700, #ed553b | = | text: Graphik 18px/20px 700, #ed553b |
| Transition | background, border-color, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | rest | pointer hover | Shift+Tab, Tab | CDP :hover:active |

Crops: `cta-coral-default.png`, `cta-coral-hover.png`, `cta-coral-focus-visible.png`, `cta-coral-pressed.png`.

#### plan-cta

Plan call to action. The action on a plan card. The href was not followed.

Page: pricing. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 331.28 x 52 | = | = | = |
| Padding | 14px 24px | = | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #1d1c1d | = | 2px solid #1d1c1d |
| Radius | 5px | = | = | = |
| Background | #1d1c1d | transparent | = | transparent |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Graphik 18px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #1d1c1d | = | #1d1c1d |
| Text node | text: Graphik 18px/20px 700, #ffffff | text: Graphik 18px/20px 700, #1d1c1d | = | text: Graphik 18px/20px 700, #1d1c1d |
| Transition | background, border-color, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | rest | pointer hover | Shift+Tab, Tab | CDP :hover:active |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

### Type

#### hero-kicker

Hero kicker. The small label above the home headline.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 23.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/23.2px 700 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Text node | text: Graphik 16px/23.2px 700, #1d1c1d |
| Transition | none |
| How | rest |

Crops: `hero-kicker-default.png`.

#### hero-title

Hero title. The home page headline.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 72px/72px 700 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Text node | text: Graphik 72px/72px 700, #1d1c1d |
| Transition | none |
| How | rest |

Crops: `hero-title-default.png`.

#### hero-body

Hero body. The paragraph under the home headline.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 69.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 24px/34.8px 400 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Text node | text: Graphik 24px/34.8px 400, #1d1c1d |
| Transition | none |
| How | rest |

Crops: `hero-body-default.png`.

#### plan-price

Plan price. The price figure on a plan card.

Page: pricing. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 331.28 x 86.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Transition | none |
| How | rest |

Crops: `plan-price-default.png`.

### Cards

#### feature-card

Feature card. A feature card on the home page.

Page: home. Selector: ``. States: .

Not found on the page at capture time.

#### plan-card

Plan card. A pricing plan card.

Page: pricing. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 433.28 x 713.45 |
| Padding | 0px 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Transition | none |
| How | rest |

Crops: `plan-card-default.png`.

#### review-card

Review card. A customer review card.

Page: reviews. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 588.8 x 606 |
| Padding | 40px |
| Border | 1px solid #d8d7d7 |
| Radius | 10px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 18px/26.1px 400 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Transition | none |
| How | rest |

Crops: `review-card-default.png`.

### Links

#### footer-link

Footer link. A link in the footer.

Page: home. Selector: ``. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 33.73 x 23.19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/23.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0.8 | #000000 |
| Text node | text: Graphik 16px/23.2px 400, #000000 @ 0.8 | text: Graphik 16px/23.2px 400, #000000 |
| Transition | none | = |
| Cursor | pointer | = |
| How | rest | pointer hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

### Menus

#### solutions-menu

Solutions menu. The Solutions dropdown, opened by hover.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 250.19 |
| Padding | 17px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/23.2px 700 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Transition | opacity, visibility 0.2s, 0.2s ease, ease delay 0s, 0s |
| Opacity | 0.00386886 |
| Cursor | pointer |
| How | rest |

Crops: `solutions-menu-default.png`.

#### solutions-item

Solutions menu item. One row in the Solutions dropdown.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 370 x 55.05 |
| Padding | 6px 24px |
| Border | none |
| Radius | 5px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 14px/20.3px 400 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Transition | padding 0.2s ease |
| Cursor | pointer |
| How | rest |

Crops: `solutions-item-default.png`.

### Tabs

#### plans-tab

Plans tab. A billing-period tab on pricing.

Page: pricing. Selector: ``. States: .

Not found on the page at capture time.

### Lists

#### faq-row

FAQ row. A closed pricing FAQ accordion row.

Page: pricing. Selector: ``. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 1120 x 58 | = | = |
| Padding | 16px 16px 16px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Graphik 22px/normal 700 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1d1c1d | = | = |
| Text node | text: Graphik 22px/normal 700, #1d1c1d | = | = |
| Transition | padding 0.2s ease | = | = |
| Cursor | pointer | = | = |
| How | rest | pointer hover | Shift+Tab, Tab |

Crops: `faq-row-default.png`, `faq-row-hover.png`, `faq-row-focus-visible.png`.

#### faq-row-open

FAQ row open. A pricing FAQ row after its head was clicked. No form was submitted.

Page: pricing. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1120 x 167.28 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #707070 @ 0.2; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 18px/26.1px 400 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Transition | none |
| How | rest |

Crops: `faq-row-open-default.png`.

### Badges

#### badge

Badge. A badge on the pricing page, when one paints.

Page: pricing. Selector: ``. States: .

Not found on the page at capture time.

### Fields

#### login-field

Workspace field. The login workspace field. Sample text was typed and cleared. Nothing was submitted.

Page: login. Selector: ``. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 274.39 x 50 | = |
| Padding | 0px 19px | = |
| Border | 2px solid #333333 | = |
| Radius | 5px 0px 0px 5px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/19.2px 500 | = |
| Letter spacing | normal | = |
| Colour | #1d1c1d | = |
| Transition | border-color 0.3s ease | = |
| Cursor | text | = |
| How | rest | click, nothing submitted |

Crops: `login-field-default.png`, `login-field-focused.png`.

#### signup-field

Get started field. The first field on Get started. Nothing was submitted.

Page: get-started. Selector: ``. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 570 x 50 | = |
| Padding | 0px 20px | 0px 19px |
| Border | 1px solid #cbcbcb | 2px solid #3e3e3e |
| Radius | 5px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Graphik 16px/19.2px 500 | = |
| Letter spacing | normal | = |
| Colour | #1d1c1d | = |
| Transition | border-color 0.3s ease | = |
| Cursor | text | = |
| How | rest | click, nothing submitted |

Crops: `signup-field-default.png`, `signup-field-focused.png`.

#### search-field

Blog search field. The blog search field. Nothing was submitted.

Page: blog. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 40 |
| Padding | 0px 30px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Transition | none |
| Cursor | text |
| How | rest |

Crops: `search-field-default.png`.

### Media

#### avatar

Review avatar. The avatar on a review.

Page: reviews. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 56 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/23.2px 500 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Transition | none |
| How | rest |

Crops: `avatar-default.png`.

### Mobile

#### menu-button

Menu button. The phone Menu control.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 34 x 34 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 0px/0px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | text: Graphik 0px/0px 400, #0000ee |
| Transition | none |
| Cursor | pointer |
| How | rest |

Crops: `menu-button-default.png`.

#### mobile-drawer

Mobile drawer. The phone nav after Menu is pressed. No destination was followed.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 754 |
| Padding | 20px 20px 50px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Transition | none |
| How | rest |

Crops: `mobile-drawer-default.png`.

#### mobile-nav-link

Mobile nav link. A link inside the opened phone nav.

Page: home. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 34.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Graphik 24px/34.8px 700 |
| Letter spacing | normal |
| Colour | #1d1c1d |
| Text node | text: Graphik 24px/34.8px 700, #1d1c1d |
| Transition | none |
| Cursor | pointer |
| How | rest |

Crops: `mobile-nav-link-default.png`.

## Transitions declared in the readable stylesheets

Kitchen.co serves main.css same-origin. The per-state Transition rows above are the computed values.
