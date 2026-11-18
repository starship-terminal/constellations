# Kitchen.co patterns

How the public pages are put together. Screenshots are the evidence. Values live in [tokens.json](tokens.json).

## Marketing chrome

A black promo bar sits above a white header. The wordmark is a chef-hat mark plus "Kitchen.co". Desktop nav is Features, Solutions (a hover menu), Pricing, Tutorials, Affiliate Program, then an outline Log in and a filled ink Try it FREE. Phone width replaces the nav with a Menu control that opens a full-width list and stacks the two actions.

See [home-light-default](screenshots/home-light-default.png) and [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png).

## Hero

Centered Graphik. A small bold kicker, a 72px headline, an 18px paragraph, then one coral button. The home page follows with a before/after illustration, not a product screenshot of the signed-in app.

See [home-light-default](screenshots/home-light-default.png).

## Pricing

Three plan columns on white: Free (ink button), Agency White-label on a sand field (coral button), Lifetime (ink button, with a coral text link for the one-time price). FAQ rows sit below as an accordion. Pay Now links leave the site for Stripe and were not followed.

See [pricing-light-default](screenshots/pricing-light-default.png) and [pricing-light-faq-open](screenshots/pricing-light-faq-open.png).

## Login and signup

`/login` redirects to `/login/workspace` and asks for a workspace slug. `/get-started` takes an email, then a six-digit confirmation code, then a create-workspace form (title, name, password). Marketing and the workspace are different systems: Graphik and coral on the public site, system UI and blue `#0165e1` inside the app.

See [login-light-default](screenshots/login-light-default.png), [get-started-light-default](screenshots/get-started-light-default.png) and [app-onboard-create-light-default](screenshots/app-onboard-create-light-default.png).

## Workspace shell

A 64px pale rail of `nav__button` icons (Home, Inbox, Proposals, Clients, Tasks, More, Settings) sits left of a rounded white stage. A search field is centred in the top bar. An orange initials avatar sits top-right. Empty Home is a heading, a short line, and five jumbo cards. Phone width is a separate client portal with a bottom tab bar (Home, Inbox, Clients, Profile), not the desktop shell squeezed.

See [app-home-light-default](screenshots/app-home-light-default.png) and [mobile-app-home-light-default](screenshots/mobile-app-home-light-default.png).

## Empty lists and dialogs

Inbox chats, Clients, My Tasks and the tasks table all show empty copy. Proposals opens a DocuMocu connect dialog; Connect and Buy were not pressed. Settings > Billing shows the free plan (2 seats, 2 GB) with Upgrade and Buy Lifetime Access, which were not pressed.

See [app-inbox-light-default](screenshots/app-inbox-light-default.png), [app-clients-light-default](screenshots/app-clients-light-default.png), [app-proposals-light-default](screenshots/app-proposals-light-default.png) and [app-settings-billing-light-default](screenshots/app-settings-billing-light-default.png).
