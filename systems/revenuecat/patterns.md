# Patterns

Public marketing and the signed-out app shell. The signed-in dashboard was
not opened.

## Marketing home

Header is 64px, background `#f9f9fb`, full width. Wordmark, then Why
RevenueCat?, Solutions, Developers, Resources, Pricing. Trailing cluster is
Log in, Contact sales, Sign up.

Hero sits on the same `#f9f9fb`. Inner column is 1280px with 32px side
padding and 88px top padding at 1440. H1 is objectSans 60px / 500,
line-height 67.5px, tracking -2.4px, max width about 579px: "Build and grow
your app business". Lede is helveticaNeue 20px / 400, `#3d3d5c`. Three stats
(166K+, 6B+, $19B+) are objectSans 24px / 500 in `#576ddb`.

Body sections alternate white. Feature articles are 384px cards, radius
16px, on `#f8f9fb`. A closing email field is a 480 by 64 pill with the
primary button inside the right edge.

At 390px the header stays 64px. The h1 drops to 30px / 33.75px, tracking
-1.2px. The hero button becomes full width (358px) at 44px tall. Menu opens
a fixed white sheet.

## Pricing

H1 is 64px / 500, line-height 72px, tracking -1.6px: "No plans, no gates.
Pay for what you track." Hero background `#f9f9fb`.

Two plan cards, 960px, radius 16px, padding 40px. PRO is a white card with
a `#d6dbf5` border. ENTERPRISE uses a gradient border from
`rgba(242, 84, 91, 0.5)` to `rgb(87, 108, 219)`. There is no monthly price
table. Copy says pay nothing up to $2,500 in monthly tracked revenue, then
1%.

Quote cards use a 1px gradient frame, 134deg, from `#d6dbf5` to `#ebedf5`.

## Signed-out login

`html` has class `dark`. Body text is Inter Variable 14px / 20px, `#f2f3f5`.
The form column is 480px inside 24px horizontal padding. H2 "Log in" is
ObjectSans 24px / 700. One email field, then a disabled Log in button.
Password is not on the page yet. Footer links sit at 12px in `#a2a4ab`.

An incident banner can sit above the form. On this capture it was yellow
`#f0d81b` with brown text `#643c00`.

## Signed-out signup

Same dark shell. Fields: name, email, password (with a 24px show control),
a "How did you hear about us?" combobox, a disabled full-width Sign up, a
Log in link, terms, and a marketing checkbox. Not submitted.

## What was not entered

No password, no name, no card, no phone, no company SSO. The marketing
email field was not submitted. Signup is not email-only, so AgentMail was
not used.
