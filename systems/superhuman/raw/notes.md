# Capture notes

2026-11-22. Signed out. Headless Chromium via Playwright. Desktop viewport 1440 by 900, devicePixelRatio 1. Phone viewport 390 by 844 CSS. The script requested deviceScaleFactor 2, and the sidecar records devicePixelRatio 1. The PNG is 390 pixels wide.

The marketing site paints one light theme. `color-scheme` on the root was `light`. There is no theme control.

The cookie sheet is Transcend's consent manager (`#transcend-consent-manager`). It paints from a closed shadow, so page text and Playwright locators cannot see "We use cookies". The capture script sets that node to `display: none`. Accept and Reject were not clicked.

`https://superhuman.com/auth/signup` redirected to `https://id.superhuman.com/signup`. `https://go.superhuman.com/` and `https://docs.superhuman.com/` redirected to `https://id.superhuman.com/signin`. Both walls were photographed empty. Google, Microsoft, and Apple were not clicked. Continue with email was not clicked. The email field was empty.

`https://superhuman.com/mail/admin` stayed on that URL and showed "Please sign in to access your team's account." Continue with Google and Continue with Microsoft were not clicked.

`https://id.superhuman.com/login` returned an AccessDenied XML page. That shot was not kept.

`https://superhuman.com/auth/login` returned the marketing 404. The kept 404 is `https://superhuman.com/this-page-does-not-exist-capture-2026`.

The homepage hero button's fill is transparent in computed style. The dark pill is the hero video behind it. The measured action fill is the violet on pricing and on the identity wall.

Full-colour PNGs stayed in `~/.design-systems/superhuman/raw-shots/`. The package stores the 256-colour copies.
