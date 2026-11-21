# FlowMapp components

Public marketing chrome and the sign-in wall, measured signed out on 2026-11-21. Values are computed styles from [raw/components-computed.json](raw/components-computed.json) and [raw/css-vars.json](raw/css-vars.json). Screenshots are the page, not a crop set: the icon extraction pass was not run.

## Button

**Log in** (`a.nav__btn`). Default: 76.9 by 38.5, padding 7.04px 16px, radius 12px, 1px solid rgba(0,0,0,0.1), text Inter 16/22.4 weight 600, color black, background transparent. Opens the sign-in wall. Not followed past the wall.

**Try for free** (`a.nav__btn.is-bg-black`). Default: 128.5 by 38.5, background rgb(0,0,0), text white, radius 12px, border 1px solid black. Opens sign-up. Stopped.

**Start planning** (`a.btn` plus `.btn__wrapper`). The anchor is 479.9 by 120.1, radius 1600px, fill rgba(0,128,255,0.2). The painted fill is the child `.btn__wrapper`: 455.9 by 96.1, background rgb(0,128,255), radius 1600px, shadow rgba(0,128,255,0.34) 0px 8px 10px 0px, text 30/42 weight 600 white. Hover and focus were applied to the anchor, not the painted child. The anchor focus outline was the browser default. A designed focus ring was Not captured.

**Pricing plan CTAs.** Sign up Free and Start Free Trial are blue pills on the pricing cards. They open `app.flowmapp.com/signup` with a plan query. Not followed. Hover, pressed, disabled, and loading were Not captured.

**Sign In / Sign Up submit.** On the auth wall the submit is present and disabled until the fields have values. It was not clicked. Loading and error states were Not captured.

## Icon button

The phone menu button is `.nav__burger.w-nav-button`, aria-label menu. It opens the nav sheet. The sheet close control is the X. Sizes were not measured as a separate crop. Shot: [phone-home-menu-open.png](screenshots/phone-home-menu-open.png).

## Link

Nav links are Inter 16/22.4 weight 600, radius 8px, padding 11.04px 14.08px, background transparent, transition background-color 0.3s ease. The current page paints the label blue (Pricing on the pricing shot). The computed color on the home link was black.

## Text field

Contact page fields (not filled): Your Name, Your FlowMapp account email, Organization Name, Subject, Message, Link to files. Placeholder text is the label. Computed field styles were Not captured.

Sign-in fields (not filled): Email (`name=email`), Password (`name=password`). Sign-up adds Username (`name=firstName`). Error and filled states were Not captured.

Help search: input name `s`, placeholder "Search for articles and documentation". Focused only. Shot: [desktop-help-search-focus.png](screenshots/desktop-help-search-focus.png).

## Text area, select, checkbox, radio, switch

Not present as a designed form control on the photographed marketing pages. The hero "Win more clients" control is a decorative graphic. The pricing Billed monthly / Billed annually control is a Webflow tab link, recorded under Tabs.

## Tabs

Pricing billing: `a.p-tabs__btn.w-tab-link`. Billed annually is the default (`w--current` on the annual pane). Billed monthly was clicked and stays on `/pricing`. Shot: [desktop-pricing-billed-monthly.png](screenshots/desktop-pricing-billed-monthly.png).

Blog filter tabs: All, Liked by readers, Team's choice, UX principles & guides, Sitemaps & Architecture, Trends. Same URL. Only All was the painted state.

Help Center: Knowledge base, FAQ, Release Notes are page links, not in-page tabs.

## Menu

Features and Use cases are hover menus on desktop (`.nav__pop`) and tap rows on the phone sheet. Contents are in [site-tree.md](site-tree.md).

## Tooltip, dialog, toast

No tooltip, dialog, or toast was opened on the marketing pages. The Help Center header keeps hidden sign-in, sign-up, and send forms in the DOM (`popup-miniform`). They were not opened and not submitted.

The help cookie bar is a fixed notice with Accept and a Privacy Policy link. Photographed, then hidden. Accept was not clicked.

## Card

Pricing plan cards: Free, Pro, Team (black), Agency. Demo share cards on `app.flowmapp.com/share/projects/215285`: light blue sitemap cards and light green user-flow cards. Card internals of the signed-in editor were Not captured.

## List row, table, avatar, badge

Not present as product components on the public marketing surface. The hero shows decorative avatar chips and a green "45% off" badge on pricing. Those are illustrations and a promo chip, not a component system that was measured.

## Gaps

- Signed-in app controls (project canvas, sitemap editor, user-flow editor, wireframe editor, comments, billing settings) were not captured. The walk stopped at the auth wall.
- Hover, pressed, disabled, loading, and error states for plan buttons and form fields were Not captured.
- No component crops were cut. Icons were not extracted.
