# Leonardo.Ai patterns

How the public pieces combine. Signed out, 2026-11-18. Account, generation, checkout and OAuth were not entered.

## Marketing canvas

When to use it: the public site. A black full-bleed wordmark field, a short white line, one filled pill and one outline pill.

Components: nav (Create, Industry, Business, Learn, Pricing, Contact, Tutorial, Log in), display wordmark, Start now, Developer API, footer.

Layout: fixed nav over a black canvas. The violet wordmark is the page, not a heading inside a card. The white line sits in the optical centre. Start now is a white pill. Developer API is an outline pill. The footer is a black band of links.

Example: [home-dark-default](screenshots/home-dark-default.png), [home-dark-full](screenshots/home-dark-full.png).

## Pricing plans

When to use it: plan comparison before an account exists.

Components: marketing nav, plan cards, Pay Yearly / Pay Monthly, Subscribe.

Layout: the same black marketing chrome. Subscribe leaves the page for the app. That handoff was not followed.

Example: [pricing-dark-default](screenshots/pricing-dark-default.png).

## Signed-out app shell

When to use it: the product frame before an account.

Components: icon rail (Create, Library, Agent, Upscaler, Blueprints, Flow State, Plans, API), display heading, prompt field, Generate, mode chips, featured cards, Sign up, Sign in.

Layout: a 77px rail on the left. The heading sits over a full-bleed image. The prompt is a dark rounded bar. Generate sits inside the bar, muted until an account exists. Mode chips are pills under the bar. Featured cards are a horizontal row. Sign up and Sign in sit at the bottom of the rail.

Example: [app-dark-default](screenshots/app-dark-default.png), [app-dark-full](screenshots/app-dark-full.png).

Library, Plans and account routes redirect to login. They are recorded in the catalog gaps, not captured.

## Blueprints browse

When to use it: a public catalog inside the app shell.

Components: search field, category chips, cards.

Layout: the same rail. Search is a text field. Chips filter the grid. Search was filled and cleared. No blueprint was opened into a generation flow.

Example: [blueprints-dark-default](screenshots/blueprints-dark-default.png).

## Login card

When to use it: the account boundary.

Components: wordmark, Canva / Apple / Google / Microsoft / Continue with Email, Need help, store badges.

Layout: a dark card on the left, a full-bleed image on the right with a caption. The OAuth rows are equal-width ghost pills. Email continues into a form that was not submitted. Turnstile is present and was not solved.

Example: [login-dark-default](screenshots/login-dark-default.png), [mobile-login-dark-default](screenshots/mobile-login-dark-default.png).

## Docs

When to use it: the public API reference.

Components: docs heading, search, nav link.

Layout: a ReadMe page painted dark. Search is a dark field. The light color mode is declared in the stylesheets and is not the live public paint.

Example: [docs-dark-default](screenshots/docs-dark-default.png).

## Phone

When to use it: 390px.

Components: marketing nav (drawer), app prompt.

Layout: the marketing home stacks. The drawer opens over the canvas. The app prompt is full width under the heading. Generation was not submitted.

Example: [mobile-home-dark-default](screenshots/mobile-home-dark-default.png), [mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png), [mobile-app-dark-default](screenshots/mobile-app-dark-default.png).

## What does not paint signed out

Forms and validation, empty and error states, destructive confirm, toasts, and onboarding sit behind the account. The login card is the stop. Do not invent those states from this package.
