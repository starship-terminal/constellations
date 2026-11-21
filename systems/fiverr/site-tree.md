# Fiverr public site tree

Captured 2026-11-21, signed out, in Playwright Chromium. Catalog name: Fiverr. Start URL: https://www.fiverr.com/.

The walk stopped. The first homepage load painted. Every later load of that URL, and a second load of the login URL, painted a human-check before the site. That check was not solved. No email, username, password, or code was typed. No SSO button was clicked. No form was submitted. No checkout, profile, birthday, plan, survey, onboarding, or newsletter field was filled.

Cookie banners were not shown on the pages that painted, so none were accepted and none were hidden.

## What painted

| URL | HTTP | What painted | Screenshot |
|---|---|---|---|
| https://www.fiverr.com/ | 200, once | Homepage. Title: Fiverr \| Freelance services marketplace \| Find top global talent | Not in the package. The file was overwritten by a later human-check shot of the same path before it was copied. It is not reconstructed. |
| https://www.fiverr.com/login | 200, once | Auth wall. Title: Login to Fiverr | [login-light-default.png](screenshots/login-light-default.png), 1440x900 |
| https://www.fiverr.com/ | 403, later loads | Human-check. Title: It needs a human touch | Not in the package. The page showed a client IP. |
| https://www.fiverr.com/login | 403, second load | Same human-check | Not in the package. |

Phone width 390x844 was not captured. The human-check blocked the session before a phone context loaded a painted page.

## Homepage controls (first load only)

Read from the DOM of the one homepage that painted. Destinations are the `href` values on that page. None of these controls were clicked, because the next navigation hit the human-check.

### Header

| Control | Kind | Opens |
|---|---|---|
| fiverr. wordmark | link | https://www.fiverr.com/?source=top_nav |
| Connect to your AI | button | In-page menu. Not opened. The chevron was visible. Destination of each item: not captured. |
| Freelance on Fiverr | link | https://www.fiverr.com/start_selling?source=top_nav |
| EN | button | In-page locale menu. Not opened. |
| Sign in | link | https://www.fiverr.com/login?source=top_nav. Auth wall. Branch stopped. |
| Join | link | https://www.fiverr.com/join?source=top_nav. Account creation. Branch stopped. Not clicked. |

### Category row

| Control | Kind | Opens |
|---|---|---|
| Trending | link | https://www.fiverr.com/categories/trending |
| Graphics & Design | link | https://www.fiverr.com/categories/graphics-design?source=category_tree |
| Programming & Tech | link | https://www.fiverr.com/categories/programming-tech?source=category_tree |
| Digital Marketing | link | https://www.fiverr.com/categories/online-marketing?source=category_tree |
| Video & Animation | link | https://www.fiverr.com/categories/video-animation?source=category_tree |
| Writing & Translation | link | https://www.fiverr.com/categories/writing-translation?source=category_tree |
| Music & Audio | link | https://www.fiverr.com/categories/music-audio?source=category_tree |
| Business | link | https://www.fiverr.com/categories/business?source=category_tree |
| Finance | link | https://www.fiverr.com/categories/finance?source=category_tree |
| AI Services | link | https://www.fiverr.com/categories/ai-services |
| Personal Growth | link | https://www.fiverr.com/categories/lifestyle?source=category_tree |
| Consulting | link | https://www.fiverr.com/categories/consulting-services |
| Data | link | https://www.fiverr.com/categories/data?source=category_tree |
| Photography | link | https://www.fiverr.com/categories/photography?source=category_tree |
| Browse categories | control, label only | Not opened. Whether it is a menu or a page was not captured. |

A second wordmark link pointed at https://www.fiverr.com/?source=side_navigation. The side navigation itself was not opened.

### Second row, read as buttons

| Control | Opened |
|---|---|
| Business essentials | Not opened. Page, menu, or dialog: not captured. |
| All categories | Not opened. |
| Freelancer stories | Not opened. |
| AI experts | Not opened. |
| FAQ | Not opened. |
| English | Not opened. Locale control. |
| S$ SGD | Not opened. Currency control. |
| Join Fiverr | Not clicked. Same account-creation branch as Join. |
| Sign in | Not clicked. Same auth wall as the header Sign in link. |

### Hero and search

The hero headline was "Hire talent obsessed with getting it right". A search field was visible with placeholder text. It was not typed into and not submitted.

| Control | Kind | Opens |
|---|---|---|
| Quick search | tab or button | In-page list. Visible on first paint: Develop WordPress website for a real estate agency; WhatsApp AI chatbot for E-commerce; Minimal feel logo and brand kit for a new fitness studio. Each row's destination was not read. |
| Trending searches | tab or button | Not opened. |
| Explore marketplace | button | Not clicked. |
| Happening on Fiverr — see live projects | button | Not clicked. |
| Show talent / Show more talent | link, one instance | https://www.fiverr.com/categories/programming-tech/website-development |

Seller cards on the homepage linked to public profile paths. Those pages were not opened. The handles are what the site published. They are listed in [raw/observations.json](raw/observations.json) only as a boundary: the walk did not open them.

## Login wall

URL: https://www.fiverr.com/login. Screenshot: [login-light-default.png](screenshots/login-light-default.png).

This is the wall the walk reached. The branch stops here. Nothing below was clicked.

### Header on the login page

| Control | Seen as | Opens |
|---|---|---|
| fiverr. wordmark | link | Not followed. Expected home. |
| Search field, placeholder "What service are you looking for today?" | text field plus search icon button | Not typed. Not submitted. |
| Connect to your AI | button with chevron | Menu not opened. |
| EN | button | Locale menu not opened. |
| Become a Seller | link or button | Not followed. Seller start is an account branch. |
| Sign in | link or button | Already on the sign-in wall. |
| Join | button | Account creation. Not clicked. |

### Category strip on the login page

Visible and not followed: Trending, Graphics & Design, Programming & Tech, Digital Marketing, Video & Animation, Writing & Translation, Music & Audio, Business, Finance, AI Services (clipped at the viewport edge). Their destinations on this page were not read as `href`s. The human-check blocked the inventory pass.

### Sign-in card

| Control | Opens |
|---|---|
| Join here | Account creation. Not clicked. |
| Continue with Google | Google SSO. Not clicked. |
| Continue with email/username | Email or username step. Not clicked. The known probe note says that step asks for email or username and password. This capture did not open it. |
| Apple | Apple SSO. Not clicked. |
| Facebook | Facebook SSO. Not clicked. |
| Terms of Service | Public legal page. Not followed. The human-check blocked further navigation. |
| Privacy Policy | Public legal page. Not followed. Same reason. |

The card headline was "Sign in to your account". The left panel headline was "Success starts here", with the lines "Over 700 categories", "Quality work done faster", and "Access to talent and businesses across the globe".

### Footer on the login page

The viewport bottom shows the start of a footer. Column labels were clipped. Individual footer links, and which page each opens, were not captured. Scrolling to read them was not done before the session was blocked.

## Stopped branches

| Branch | Why it stopped |
|---|---|
| Homepage menus, search submit, category pages, footer, seller profiles, legal pages | Human-check painted on the next load of https://www.fiverr.com/ before those controls could be opened. |
| Sign in, Join, Become a Seller, Continue with email/username | Auth or account-creation wall. Recorded. Not entered. |
| Continue with Google, Apple, Facebook | SSO. Not clicked. |
| Phone 390x844 pass | Human-check painted before a phone page loaded. |
| Signed-in app, inbox, orders, checkout, onboarding | Not reached. signed_in is false. |

## Not captured

Unread token values are Not captured. No CSS custom properties were read, because the human-check blocked the measurement pass. The login screenshot is evidence of layout only. Colours in [tokens.json](tokens.json) that come from that PNG are labelled Sampled, and only where a flat fill was readable. Everything else is Not captured.
