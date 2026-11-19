# Patterns

Pages measured on 19 November 2026. No full-page screenshots: the preview browser did not produce frames. Layout numbers are computed boxes.

## Signed-out chat

`https://pi.ai/` redirects to `/talk/<id>`. The id in this session was a generated greeting thread, not an account. The shell is a 280px sidebar plus a main column.

| Region | Light, 1440×900 | Dark, 1169×731 |
|---|---|---|
| Page | `#FAF3EA` | `#131212` |
| Sidebar | 280×900, `#F7EFE4` | 280×731, `#1A1918`, 1px right border `#504A42` |
| Greeting | Grenette 22px, `#1A4631`, column 576px at x=572 | Grenette 22px, `#D8D4CE`, column 576px at x=437 |
| Header actions | Log in at x=1120, Sign up for free at x=1256 | Log in at x=849, Sign up for free at x=985 |
| Name field | 528×40 at y=805 | 528×40 at y=636 |

The greeting copy is fixed: "Hey, I'm Pi — your personal AI." Then a short introduction, then "But first, what should I call you?" A label under the field says the name is also what other users see. The footer links Terms and Privacy Policy. Nothing was typed.

The sidebar holds the greeting thread title, Help and feedback, a note that login saves history past 60 days, and a Log in pill.

## Login

`/onboarding/login` replaces the main column. The heading is an h3, "Sign up or log in", Grenette Condensed 32px, line-height 35.2px, letter-spacing -0.48px. It is `#FCFAF7` in dark and `#131212` in light.

Under it, three OAuth buttons stack with 16px gaps: Continue with Google, Continue with Apple, Continue with Facebook. Each is 353×56, radius 48px, 1.5px border. Dark fill `#242322`, border `#504A42`, label `#D8D4CE` at 18px weight 500. Light fill `#FCFAF7`, border `#E1D3C0`, label `#131212`.

An "or" divider sits under the stack. Email and Phone are 56px circles with labels in DM Sans 14px. The legal line is DM Sans 16px weight 500, `#B4AFA7` in dark and `#655E55` in light.

Email and Phone were not opened. Google, Apple and Facebook were not clicked. The page also offers a phone path, which this capture does not enter.

## Marketing home

`https://pi.ai/` does not render a marketing page. It redirects into the chat. The public marketing site is `https://hey.pi.ai/`, linked from the chat's privacy document as "Try Pi". It is a Framer site.

At 1440×900 the page is 4812px tall. The nav is a 64px bar: wordmark, Get the app, Help, and a 96×40 Try Pi pill. The hero is 1200×800 with 64px top padding and 80px inline padding. The h1 is 379px wide. Feature 1, 3 and the hero sit on the page cream `#FAF3EA`. Feature 2 and Feature 4 are bands of `#F7EFE4`, 720px tall, padding 128px 80px. A closing line, "Created by Inflection AI", is Grenette 52px.

At 390×844 the page is 6096px tall. The hero band is 378×640. The h1 is 40px on 38px line-height, 342px wide. Feature bands stack full width. The only dark control still on screen is the "Learn about Inflection AI" link, 271×54, fill `#131212`.

The marketing chat bubbles are a public demo, not a signed-in thread. Their text colour is `#131212` and the type is Grenette 18px.

## Widths

| Width | What was measured |
|---|---|
| 1440×900 | Light chat, light and dark login, marketing home. `devicePixelRatio` 2, visual viewport scale 1. |
| 390×844 | Marketing home only. The chat was not remeasured at 390. |
| 1169×731 | Dark chat, the preview fill size before the freeform resize. |

## Not captured

Discover (`/discover`) redirected back to the greeting thread. `/privacy` on pi.ai rendered an Inflection privacy document inside the chat shell, with its own Framer classes, and the sidebar still overlaid it. Labs, blog, about, pricing and download on pi.ai returned 404 to a same-origin fetch. Account settings, saved chats, voice, reminders and the signed-in composer were not reached.
