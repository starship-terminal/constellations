# Limitless patterns

Public pages plus the Sign Up Unavailable dialog, 2026-11-18. Lifelogs, settings and account were not reached. Recorded in [components.md](components.md) Gaps and in the catalog `capture.gaps`.

## Marketing frame

A white page, a sticky bar (wordmark, Home, Solutions, Privacy, Developers, About, Sign In), then a centered 60px headline. [Home](screenshots/home-light-default.png) leads with the acquisition letter in a 24px-radius card under a YouTube embed. [Phone](screenshots/mobile-home-light-default.png) collapses the bar to the wordmark and a hamburger; the menu is a full-height list ([open](screenshots/mobile-home-light-menu.png)).

## Solutions menu

Solutions is a local menu, not a page. It groups links by use case, role, job and condition ([open](screenshots/home-light-solutions.png)). A solution page is a headline, a short deck, and a card carousel ([voice recorder](screenshots/for-voice-light-default.png)).

## Developer docs

`/developers` is a long single column: a pale panel, a purple callout, a table of contents, then MCP URL, copy, and off-site links (GitHub, Slack). [Desktop](screenshots/developers-light-default.png). Anchors stay on the page. Copy writes to the clipboard and does not submit.

## FAQ

`/privacy` is a stack of native disclosures ([page](screenshots/privacy-light-default.png)). One was opened locally. The page does not post.

## Help center

`help.limitless.ai` is a separate Intercom-style surface: purple band, search, collection cards ([home](screenshots/help-light-default.png)). Search was focused and not queried. Article bodies were not opened.

## Sign-in wall

`app.limitless.ai` redirects to `/signin`: a centered card, Continue with Google, an email field, a Privacy Policy link ([desktop](screenshots/signin-light-default.png), [phone](screenshots/mobile-signin-light-default.png)). Google is OAuth and was not pressed.

## Sign Up Unavailable

Submitting the email field (never Google) opens a Radix dialog on a 30% black scrim: title "Sign Up Unavailable", body that Limitless is no longer accepting new users, a mailto to support@limitless.ai for Pendant owners, and an OK control ([desktop](screenshots/signin-light-signup-unavailable.png), [phone](screenshots/mobile-signin-light-signup-unavailable.png), [crop](components/crops/signup-unavailable-dialog-default.png)). OK was not pressed. No CAPTCHA, phone or payment appeared. A Google One Tap chip can appear on phone; it was not used.

## What is not on the captured surface

Lifelogs, settings, account, empty/loading/error of the app, form validation, destructive confirmation, and onboarding all sit behind an account this capture could not create. The 404 at `/pricing` is the marketing site's not-found page ([shot](screenshots/notfound-light-default.png)), not an app error state.

## Motion

Transitions on the public pages keep running under `prefers-reduced-motion: reduce`. The probe's verdict on all five pages is `ignores` ([raw/motion.json](raw/motion.json)). Durations are short (100ms on nav colour). That is a finding, not a gap to tidy.
