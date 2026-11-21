# Pi public site tree

Mapped on 2026-11-21 from https://pi.ai, signed out, in headed Chrome at 1440×900. `https://pi.ai` redirects to `/talk/<id>`. The talk id is an anonymous session. It is not an account. The painted theme on a fresh load had no `dark` class. Adding `html.dark` switches the same shell to the dark token set. Nothing was typed. No identity provider was clicked. No form was submitted. No chat message was sent.

The public marketing site is a second host, https://hey.pi.ai/. It has one cream theme.

## Homepage shell

`https://pi.ai` opens a signed-out chat. A status banner sits above the shell. The left sidebar is 280px when open and 64px when collapsed. The header holds Log in and Sign up for free. The composer asks for a preferred name and was left empty.

| Control | Opens | Stop? |
|---|---|---|
| Pi — start new chat | A new anonymous `/talk/<id>` | public shell |
| Toggle sidebar | Collapses the sidebar on the same page (`--sidebar-width` 64px) | |
| Greetings from Pi | The current anonymous thread | public |
| Help & feedback | `/help-feedback` | public |
| Log in (sidebar) | `/onboarding/login` | yes, login wall |
| Chat options | Menu with one item, Auto-read | public; not toggled |
| Log in (header) | `/onboarding/login` | yes, login wall |
| Sign up for free | `/onboarding/signup` | yes, signup wall. Same wall as login |
| Preferred name field | Stays on the page | not typed |
| Submit name | Would send the name | not clicked |
| Terms | https://inflection.ai/terms-of-service | public legal |
| Privacy Policy | https://inflection.ai/privacy-policy | public legal |
| Home (phone tab bar) | The current thread | public |
| More (phone tab bar) | Chat options menu | public |
| Open chat history (phone) | Chat history drawer | public empty thread list |

`/discover` and `/voices` do not exist as pages. `/discover` returns the homepage. `/voices` and `/about` return the app 404 ("This page could not be found.").

## Chat options menu

One item: Auto-read. Escape closes the menu. It was not toggled.

## Phone drawer

At 390×844 the sidebar is closed. The top button is labelled Open chat history. It opens a drawer titled Chat history with the anonymous thread "Greetings from Pi" and a Log in pill. Close chat history dismisses it.

## Login and signup walls

Photographed empty. Continue with Google, Continue with Apple, Continue with Facebook, Email, and Phone were not clicked.

| Control | Opens | What it shows |
|---|---|---|
| Log in | `/onboarding/login` | "Sign up or log in". Google, Apple, Facebook, Email, Phone. |
| Sign up for free | `/onboarding/signup` | The same wall. |
| Email | Would open an email step | not opened |
| Phone | Would open a phone step | not opened |

## Help and feedback

`/help-feedback` is public.

| Control | Opens | Stop? |
|---|---|---|
| Visit the Help Center | https://help.pi.ai/en/ in a new tab | public help home |
| Request support | In-page form (email, summary, details, attach file) | yes. Photographed as a form. Not filled. Not submitted |
| Share your feedback | In-page survey | yes. Not filled. Not submitted |
| Go back | Returns to the help landing | |

The help center home has Find answers, Request help, Share your feedback, a search field left empty, and two collections (Using Pi, Issues and Requests). Collection articles were not opened.

## Privacy

`/privacy` renders the Inflection privacy policy inside the chat shell. Its nav links Try Pi, Labs, Blog, and About Us on https://inflection.ai/.

## Marketing site

https://hey.pi.ai/ is a Framer page. Nav: wordmark (home), Get the app (`#download`), Help (https://help.pi.ai/en/), Try Pi (https://pi.ai/, which landed on the login wall in this session).

| Control | Opens | Stop? |
|---|---|---|
| Get the app | `#download` on the same page: App Store badge, Google Play badge, QR code | badges not followed into the stores |
| Help | https://help.pi.ai/en/ | public |
| Try Pi | https://pi.ai/ | login wall in this session |
| Learn about Inflection AI | https://inflection.ai/ | public company site |
| Help Center | https://help.pi.ai/en/ | public |
| Terms of service | https://inflection.ai/terms-of-service | public legal |
| Privacy policy | https://inflection.ai/privacy-policy | public legal |
| Other notices | https://inflection.ai/legal | public legal |

`/labs`, `/blog`, and `/about` on hey.pi.ai return the marketing 404 ("The page you are looking for doesn't exist.") with Go back home.

`/download` on pi.ai redirects to a todesktop download URL ("Downloading…"). That file was not saved.

## Company site, linked, not the product

https://inflection.ai/ nav: Try Pi, Labs, Blog, About Us. About is https://inflection.ai/about. Those pages are Inflection's site, not the Pi app. They were opened to name the links and were not captured as Pi screens.
