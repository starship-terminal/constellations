# Krea patterns

How the measured components combine on each captured surface. Values are in [tokens.json](tokens.json). Components are in [components.md](components.md). Full-page evidence is in [screenshots/](screenshots).

## App shell (dark)

The signed-out home at https://www.krea.ai/ paints `html.dark`. The field is primary-950 `#101010` (`dark.color.page-950`). A 255px sidebar (`sidebar`, `dark.component.sidebar.width`) holds 36px rows: Home is selected, then Krea Agent, Train Lora, Node Editor, Assets, and the tool list (Image, Video, Enhancer, Audio, and the rest). Pricing carries a blue 40% off chip. A 48px white Sign in button (`nav-signin`, `dark.component.sign-in.height`) sits at the bottom of the sidebar. Toggle Sidebar folds the rail. Tools opens a local menu. See [home-dark-default](screenshots/home-dark-default.png), [home-dark-sidebar-folded](screenshots/home-dark-sidebar-folded.png) and [home-dark-tools-menu](screenshots/home-dark-tools-menu.png).

An offer strip sits above the feed ("Unlimited Nano Banana for 7 days", Claim offer). Claim offer was not followed. Below it, a prompt composer (`composer`, 822 x 48) reads "Describe an idea or upload an image to edit it..." with a Generate control. The field was filled and cleared. Generate was never clicked. The rest of the page is a public feed of generation cards (`feed-card`). See [home-dark-full](screenshots/home-dark-full.png).

## Image tool (signed out)

https://www.krea.ai/image uses the same dark shell and the same composer (`image-prompt`, 870 x 48) over a model gallery (`image-shell`). Generation is gated. The prompt was filled and cleared. See [image-dark-default](screenshots/image-dark-default.png).

## Marketing chrome

https://www.krea.ai/pricing, /enterprise, /plugins, /mcp and /blog share a marketing nav (`mkt-nav`, about 80px): App, Features, Plugins, Image, Video, Upscaler, API, MCP, Pricing, Enterprise, a white Sign up for free pill (`mkt-signup`) and a dark Log in pill (`mkt-login`). Both pills were measured and never followed.

Pricing opens on a Suisse Intl heading (`price-h1`) and four plans: Free $0, Basic, Pro (Most popular), Max. Yearly is selected, with a blue 40% off badge (`price-badge`, 55 x 21). The interval toggle (`price-interval`) is local UI. Get Pro (`price-cta`, 280 x 40, white pill) was measured and never followed. See [pricing-dark-default](screenshots/pricing-dark-default.png).

Enterprise is the same chrome with a Book a call control (`ent-cta`). The call form was not opened. See [enterprise-dark-default](screenshots/enterprise-dark-default.png).

Plugins and the image-generator feature page can paint a light hero while `html` stays dark. That light field is a marketing surface, not a second product theme. See [plugins-dark-default](screenshots/plugins-dark-default.png) and [features-dark-default](screenshots/features-dark-default.png).

MCP is a public connector page ("Krea MCP"). Add Krea connector was not followed. See [mcp-dark-default](screenshots/mcp-dark-default.png).

## Docs

https://www.krea.ai/docs is a separate docs surface. It was shot, and its sheets are not folded into the app tokens. Get API key was not followed. See [docs-dark-default](screenshots/docs-dark-default.png).

## Login boundary

https://www.krea.ai/login is "Welcome to Krea" (`login-h1`) with Continue with Google, Continue with Apple, Single Sign-On (SSO) (`login-google`, `login-apple`, `login-sso`, about 352 x 46) and an email field (`login-email`). Continue with Email (`login-email-btn`) is the blue button. Google, Apple and SSO were never followed. Continue with Email was submitted once on 2026-11-18; GET /api/auth/email-flow returned 400 captcha_failed (Cloudflare Turnstile, no visible widget) and the signed-in pass stopped. Terms and Privacy links were measured. See [login-dark-default](screenshots/login-dark-default.png).

## Phone (390 x 844)

The home collapses to Explore, Upgrade, filter chips (All, New, Images, Videos, Edit) and a tool grid (Image, Video, Agent, MCP, Enhancer, Audio). A menu control (`m-menu`, 52 x 64) opens the phone nav. See [mobile-home-dark-default](screenshots/mobile-home-dark-default.png) and [mobile-home-dark-nav](screenshots/mobile-home-dark-nav.png). Pricing at 390 keeps the plan stack. See [mobile-pricing-dark-default](screenshots/mobile-pricing-dark-default.png). Login at 390 is the same OAuth card. See [mobile-login-dark-default](screenshots/mobile-login-dark-default.png).

## Signed-in home (2026-11-20)

https://www.krea.ai/app, already signed in, paints the same `html.dark` field. The shell is two columns, not the 255px signed-out sidebar. A 52px black icon rail holds Krea, Bots, Agent, Node Editor, Train Lora, Files, API, More, and Account and usage. Beside it, a 288px section sidebar lists Home, Image, Video, Enhancer, Ad Studio, Edit, More, Sessions, Pricing (40% off yearly), Enterprise, MCP and Invite teammates. The canvas is a hero carousel and a prompt composer (Auto, Fast, a count, Generate). Generate was not clicked. See [app-dark-default](screenshots/app-dark-default.png).

Account and usage opens a menu: Buy plan, Usage (0% used), Workspace, Settings, Report a bug, Log out. Buy plan, Invite teammates, Report a bug and Log out were not followed. Settings navigated toward `/manage/profile` and the preview then stopped painting, so that page has no screenshot. See [app-dark-account-menu](screenshots/app-dark-account-menu.png) and [login-review.json](login-review.json).

The computed custom properties on that page match the public dark roles (`--background`, `--foreground`, `--card`, `--sidebar`, `--radius` at 0.625rem). They are recorded in [signed-in-2026-11-20.json](raw/signed-in-2026-11-20.json) and are not a second token set. Phone width was not captured on this walk.

## What does not paint signed out

There is no validation error, empty generation result, loading state, or destructive confirmation on the public pages. Search opens from a 20px sidebar button (`search-button`). The results panel was not captured as its own surface. Onboarding is the public home itself: the composer and the tool grid. Account, assets, train, nodes, billing, API keys and checkout stop at the login or plan buttons.
