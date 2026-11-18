# Patterns

How the public Maze pages are built. Screenshots are in [screenshots/](screenshots).

## Marketing frame

[home-light-default](screenshots/home-light-default.png) is the signed-out home at 1440. A white header holds the wordmark, PLATFORM, SOLUTIONS, RESOURCES, CUSTOMERS, PRICING, Log in, a pill Try Maze for free, and a near-black Get a demo. The page ground is warm neutral. The hero is Phonic light, "Research at the pace of change", with the same two CTAs under the subcopy and a collage of product cards on the right.

The header is `position: relative`, not fixed. Lenis owns the scroll, so a viewport shot taken after a scroll can miss the header even when `window.scrollY` is 0. The committed viewport shot is the top of the full-page capture.

A black promo bar sits above the header: "Help shape Maze's Future of Research Report 2027 / Take the survey". That link opens a live study on `t.maze.co`. The bar is hidden in these shots. It was never clicked.

CookieYes ("We value your privacy") sits bottom-right on maze.co. OneTrust sits on auth.maze.co. Both are hidden. Neither was clicked.

A lime chat widget sits bottom-right. It was left alone.

## Platform menu

[home-light-platform-menu](screenshots/home-light-platform-menu.png). Hovering PLATFORM opens a panel: Maze Platform, Integrations, Panel, In-Product Prompts, AI Moderator, AI Study Builder, Prototype Testing, Moderated Interviews, Surveys, Live Website Testing, Mobile Testing, Maze MCP, Maze AI, Automated Reports. The labels are an icon font, so `innerText` is empty until the panel is open. No menu link was followed.

## Pricing

[pricing-light-default](screenshots/pricing-light-default.png). "Pricing & Packages" over Free, Starter and Enterprise. Starter is $99 per month and its CTA is "Sign up now" to `auth.maze.co/signup/?plan=starter&frequency=yearly`. That link was not clicked. No monthly/yearly switch was in the first viewport. The signup href already carries `frequency=yearly`.

## Auth login

[login-light-default](screenshots/login-light-default.png). Inter on a white column, lime collage on the right. Email and password are 440×48, radius 8. Log in is filled `rgb(5, 104, 253)`, white label, weight 600. Continue with Google, Continue with SSO, Reset password, and Sign up for a new account are on the same card. Nothing was submitted. The password field was never filled.

## Public report

[report-light-default](screenshots/report-light-default.png). Maze publishes a sample report that loads signed out: Banking App Usability Test, 104 responses, 7 blocks. Sign up for free is the same blue as Log in. Login is a white control. Neither was clicked. The phone width shows "Window size too small" and asks for 800px ([mobile-report-light-default](screenshots/mobile-report-light-default.png)).

## Demo form

[demo-light-default](screenshots/demo-light-default.png). "Turn any question into a confident decision" beside "Tell us about yourself": work email, role, company size, how the team can help, and a black Submit. The form was not submitted.

## Phone

[mobile-home-light-default](screenshots/mobile-home-light-default.png) is 390×844. The wordmark and a hamburger replace the desktop nav. [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png) is the local drawer: Platform, Solutions, Resources, Customers, Pricing, then Log in, Try Maze for free, and Get a demo. The drawer was opened with the button labelled Open navigation. No item was followed.
