# Patterns

Public pages only. Signed-in charts, settings, and checkout were not entered.

## Marketing home

[home-light-default.png](screenshots/home-light-default.png) at 1440, [home-light-phone.png](screenshots/home-light-phone.png) at 390.

A 64px header holds the wordmark, Platform and Enrich menus, Pricing, Log in, and a blue Sign up pill. The hero is a left column (uppercase display, grey subcopy, dark and white pills) beside a sample org chart. Below that, a three-column grid of company cards, then an articles row on a grey band, then a near-black footer.

At 390 the nav links collapse into a 32px menu button. Opening it shows a fixed white drawer with Platform, Enrich, Pricing, then Sign up and Log in stacked at the bottom. [The drawer was measured in the preview tab. The phone screenshot is the closed state.]

## Pricing

[pricing-light-default.png](screenshots/pricing-light-default.png).

A 66px page title, a Yearly/Monthly pill, then four plan cards. Get started links to `/signup` and was not followed. Contact sales was not opened. A comparison table sits under the cards. Plan prices are product content, not tokens.

## Org chart

[org-google-light-default.png](screenshots/org-google-light-default.png).

A public company page shows the name, a short description, industry and office links, Org chart / Teams / Offices tabs (a 2px rgb(13, 13, 13) underline on the selected tab), one visible position card, a blurred chart behind a "Log in or sign up to view org chart" gate, then team cards and office rows. The gate's Sign up was not followed.

## Auth

Login is a centred column: email, password, a dark Log in button, then Google, Microsoft, passkey, and SSO. Signup is email plus Google and Microsoft. Those identity buttons were not pressed. No account was created.

## Contact and missing page

Contact lists support, sales, and press links, then an FAQ. One question was opened and closed in the DOM. A made-up path returns the site's own 404, "Whoops!", with a blue "home" link. [missing-light-default.png](screenshots/missing-light-default.png).

## Gaps

- No empty, loading, or error page beyond the 404.
- No destructive confirmation, toast, or onboarding. Signup stops at the email form.
- Search was not used. The org page has a search icon that was not opened.
