# Components

Public marketing site and the account-entry walls, measured on 2026-11-21. The signed-in app was not entered. Crops are cut from the full-colour captures before quantising.

| Component | States captured | Crop | Notes |
|---|---|---|---|
| Banner | default | [banner-default.png](components/crops/banner-default.png) | Yellow `#ffc233` strip, Inter 18/28.8, ink `#121217`. "Learn more" opens the shutdown post. |
| Navigation | default | [nav-default.png](components/crops/nav-default.png) | Purple bar, logo, Docs, Help, Sign in, white pill button. Height 88px from the nav link box. |
| Button, primary | default | [button-primary-default.png](components/crops/button-primary-default.png) | White fill, ink text, 40px radius, 40px height, Inter 15/24 weight 500. Hover and focus computed styles did not change. The stylesheet's `.button:hover` blue is a Webflow default and did not apply to this pill. |
| Hero title | default | [hero-title-default.png](components/crops/hero-title-default.png) | Circular Pro Book 80/80, white on purple. |
| Link | default | [nav-default.png](components/crops/nav-default.png) | Nav links are white at 60% opacity, 15/24. Hover rule sets them to solid white. Footer links match the dim white. |
| Switch | default | [pricing-light-default.png](screenshots/pricing-light-default.png) | Annual discount checkbox on the pricing email card. Off by default. The native control computed a 13px height. The painted pill is larger than that box. |
| Slider | default | [pricing-light-default.png](screenshots/pricing-light-default.png) | Subscriber range, min 0, max 52, value 0, labelled 500 subscribers. Not dragged. |
| Accordion | open, closed | [faq-open-default.png](components/crops/faq-open-default.png) | Twelve FAQ rows. Row 01 is open on load. Question ink is pink `#db0bb9` (`--pink-700`). Radius 8px. |
| Dialog | default | [dialog-default.png](components/crops/dialog-default.png) | Help "Message us" opens Contact support. Name, Email, Additional details, Cancel, Submit. Not submitted. Dialog radius was not read from CSS (the node is outside the page's style root). |
| Text field | default | [login-card-default.png](components/crops/login-card-default.png) | Login email and password, 40px height, 8px radius, 8px 16px padding. Empty. Not typed. |
| Button, auth | default | [login-submit-default.png](components/crops/login-submit-default.png) | Violet `#7047eb`, 48px height, 8px radius, white label. Not clicked. |
| OAuth button | default | [login-card-default.png](components/crops/login-card-default.png) | Google and Twitter, 50px height, 8px radius. Not clicked. |
| Checkbox | default | [login-card-default.png](components/crops/login-card-default.png) | Remember me. Left unchecked. |
| Menu | open | [menu-mobile-default.png](components/crops/menu-mobile-default.png) | Phone hamburger opens Docs, Help, Sign in. |
| Card | default | [pricing-light-default.png](screenshots/pricing-light-default.png) | Fee card on green-100, email card on pink-100. |

## Not present

Select, radio, tabs, tooltip, toast, table, avatar, badge, icon button, and text area were not on the public pages that were opened. The help dialog has a text area. Its computed style was not read, because the dialog node sits outside the page style root. That size is Not captured.

## Not captured

- Pressed and disabled states. No disabled control was shown. Pressed was not held.
- Loading and error states. No form was submitted, so validation never ran.
- Dark theme. The public site does not offer one.
- Focus ring on the marketing pill. Keyboard focus did not change the computed outline.
- Icon sizes. Icons are the logo and share glyphs. Their pixel size was not measured.
- Signed-in components. Stopped at the login wall.
