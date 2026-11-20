# Mocha patterns

## Docs shell

docs.getmocha.com is a Mintlify site. At 1440 the top bar is 64px, the sidebar is 288px, and the article sits in a centre column with a table of contents on the right. The page colour is `--background-light` (`#f9f7ef`) or `--background-dark` (`#1a1a1a`). The wordmark is a raster logo, black in light and white in dark, 28px tall.

![Welcome, light, 1440](screenshots/docs-welcome-light.png)

![Welcome, dark, 1440](screenshots/docs-welcome-dark.png)

At 390 the sidebar collapses into a "Get Started" row with a menu icon. Search becomes an icon.

![Welcome, light, 390](screenshots/mobile-docs-welcome-light.png)

![Welcome, dark, 390](screenshots/mobile-docs-welcome-dark.png)

## FAQ

The FAQ page is the same shell with a stack of `details` rows under the shutdown callout.

![FAQ, light](screenshots/docs-faq-light.png)

![FAQ, accordion open](screenshots/docs-faq-light-accordion.png)

## Billing

The billing page is the same shell. It describes subscriptions. No payment form is on the page, and none was opened.

![Billing, light](screenshots/docs-billing-light.png)

## Shutdown

app.mocha.app, login.mocha.app, auth.mocha.app, dashboard.mocha.app, studio.mocha.app, build.mocha.app, and vidsync.mocha.app all return the same 410 page. Rechecked 2026-11-21. It is one column, centred, on `#f7f5f1`, with the black wordmark, a 68px heading, a muted sentence, and one pill link. The link points at `https://getmocha.com/blog/mocha-shutdown`, which does not resolve. login.mocha.app is the same page. It is not a sign-in form.

![login.mocha.app, 1440](screenshots/shutdown-login-light.png)

![Shutdown, 1440](screenshots/shutdown-light.png)

![Shutdown, 390](screenshots/mobile-shutdown-light.png)

## What was not entered

getmocha.com has no A record. Confirmed again on 2026-11-21: `/` and `/login` do not resolve. Sign-in, signup, the builder, and billing checkout are gone with the product. The search dialog was opened and closed with nothing typed. The theme menu was opened and closed. One FAQ row was opened. The phone nav sheet was opened. No form was submitted. The page list is [site-tree.md](site-tree.md).

![Phone nav, 390](screenshots/mobile-docs-welcome-light-menu.png)
