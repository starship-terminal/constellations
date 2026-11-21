# Patterns

Public marketing and the signed-out login. No screenshots: the preview browser did not produce frames. Layout numbers are computed element sizes.

## Marketing shell

At 1440 CSS px the page is a purple news bar (54px, #5727e7, white 16px link) stuck above a white header (`.header-4`, 92px). The sticky wrapper is 146px and has no shadow. Nav links are black Satoshi 18px weight 700. The right side is three 12px-radius buttons: Login and Book a Demo are outlined, Start for Free is #5727e7. Content sits in `.page-container` at max-width 1230px with 15px side padding. The nav container is 90% and measured 1296px wide.

At 390 CSS px the header is 72px. The desktop Login button's box height was 0. The pricing card narrowed to 350px. The menu button exists (`.header-menu-button`) but its box height was 0 in that read, so the open phone menu was not captured.

## Hero

`.home-banner-section` has 100px vertical padding and a computed background of white. Its stylesheet also sets a radial and linear gradient (stops #6a4cff, #3d9cff, #6feaff, #3fa6ff, #3e6dff). The h1 is white Satoshi 60px / 78px weight 700, 1080px wide. Two actions sit under the summary: Book a Demo (purple, 48px) and Try it Free (white, black border, 48px).

## Pricing

`/pricing` leads with product tabs (Virtual Events selected). Plan cards are white 12px-radius panels. The plan name is 40px at 1440 and 24px at 390. The price is #5727e7 at 32px. Buy Now matches the primary button and was not followed. A Monthly / Yearly control is in the DOM. Its save tag had height 0 at rest, so the selected billing state was not isolated.

## Login

`https://app.spatial.chat/login` is a white shell. The form column is 360px on the left (954px region). A 486px rail on the right is #f9f9fc and holds a quote. The stack is Google, Apple, an "or" divider, an email field, and a Continue button in #5b5bf5. Legal copy sits under the button. Nothing was submitted.

## Not captured

Signed-in app shell, empty and loading states inside the product, destructive confirmation, search, tables, and onboarding. Those sit behind login. The email form was not submitted, so there is no validation pattern.

## Public site

[site-tree.md](site-tree.md) maps the homepage header, footer, and the pages those controls open. Shots from 2026-11-22 live in [screenshots/public/](screenshots/public/). The marketing pages are white with a purple news bar and a purple primary button. Login and signup are the same empty wall at https://app.spatial.chat/login: Google, Apple, an email field, and Continue. None of those were used.
