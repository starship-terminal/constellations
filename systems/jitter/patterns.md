# Patterns

How the public pages and the signed-in product combine. Screenshots are 256-colour PNGs. Read colours from [tokens.json](tokens.json).

## Marketing shell

A fixed header on `#f2f1f3`: wordmark, Product, Customers, Templates, Pricing, Log in, and a black Sign up pill. The hero is a large Euclid/Inter headline on white, a violet pill, then a logo row. See [home-light-default.png](screenshots/home-light-default.png).

At 390 the nav collapses to Log in and a round menu button. See [mobile-home-light-default.png](screenshots/mobile-home-light-default.png) and [mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png).

## Pricing

A monthly/annual toggle, then a row of coloured plan CTAs (blue, yellow, violet). An accordion answers common questions. See [pricing-light-default.png](screenshots/pricing-light-default.png) and the toggle crop [plan-toggle-default.png](components/crops/plan-toggle-default.png). The annual prices were not isolated as their own full-page shot. Checkout was not entered.

## Templates

A search field and category links over a grid of public previews. See [templates-light-default.png](screenshots/templates-light-default.png). Opening a file would enter the editor, which is gated.

## Sign-in boundary

`/login/` and `/join/` render the same card: Google, an email field, and Continue with email. See [login-light-default.png](screenshots/login-light-default.png). Email Continue sends a magic link. Google and SSO were never clicked. The check-email screen is [join-light-check-email.png](screenshots/join-light-check-email.png).

## Onboarding

A blue motion sequence then: name, role, matching teams, invite teammates, start. Name and role were filled. Team join and invites were skipped. See [onboarding-light-name.png](screenshots/onboarding-light-name.png), [onboarding-light-role.png](screenshots/onboarding-light-role.png), [onboarding-light-start.png](screenshots/onboarding-light-start.png).

## Files

A light files shell: Drafts, Templates, workspace, Brand Kit, Trash, Create new file, Import from Figma. The header holds My files and a round avatar. See [files-light-default.png](screenshots/files-light-default.png). Account menu: My account, Logout. [files-light-account-menu.png](screenshots/files-light-account-menu.png). Empty team files: [team-light-default.png](screenshots/team-light-default.png).

## Account

`/account/` is My account: picture, name field, on the same files shell. [account-light-default.png](screenshots/account-light-default.png). Workspace settings show the Free Plan and an Upgrade your plan pill that was not pressed. [workspace-light-default.png](screenshots/workspace-light-default.png).

## Editor

A dark 48px header (back, title, Offline, Share, 100%, Export) over a light canvas. Design / Animate sit on the right. A Superagents promo card can sit on the canvas. Export and Upgrade now were measured at rest. [editor-light-default.png](screenshots/editor-light-default.png). Phone width shows a dark share/view of the file. [mobile-editor-light-default.png](screenshots/mobile-editor-light-default.png).

## Contact sales boundary

A form with name, email, phone and a message, plus Send message. See [contact-light-default.png](screenshots/contact-light-default.png). The form was not filled and not submitted. The phone field's placeholder is a sample number the site publishes, not a person's number.

## Not found

An unknown path renders the site's own not-found page. See [notfound-light-default.png](screenshots/notfound-light-default.png).
