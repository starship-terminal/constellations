# Limitless patterns

Public pages, refreshed 2026-11-21. The control map is [site-tree.md](site-tree.md). Lifelogs, settings and account were not reached. Nothing was typed or submitted.

## Marketing frame

A white page, a sticky bar (wordmark, Home, Solutions, Privacy, Developers, About, Sign In), then a centered 60px headline. [Home](screenshots/home-light-default.png) leads with the acquisition letter in a 24px-radius card under a YouTube embed. [Phone](screenshots/mobile-home-light-default.png) collapses the bar to the wordmark and a hamburger; the menu is a full-height list ([open](screenshots/mobile-home-light-menu.png)).

## Solutions menu

Solutions is a local menu, not a page. It groups links by use case, role, job and condition ([open](screenshots/home-light-solutions.png)). A solution page is a headline, a short deck, and a card carousel ([voice recorder](screenshots/for-voice-light-default.png), [students](screenshots/for-students-light-default.png), [parents](screenshots/for-parents-light-default.png)). `/for/dementia` is the same shape ([shot](screenshots/for-dementia-light-default.png)).

## Developer docs

`/developers` is a long single column: a pale panel, a purple callout, a table of contents, then MCP URL, copy, and off-site links (GitHub, Slack). [Desktop](screenshots/developers-light-default.png). Anchors stay on the page. Copy writes to the clipboard and does not submit.

## FAQ

`/privacy` is a stack of native disclosures ([page](screenshots/privacy-light-default.png)). One was opened locally. The page does not post.

## Help center

`help.limitless.ai` is a separate Intercom-style surface: purple band, search, collection cards ([home](screenshots/help-light-default.png)). Search was focused and not queried. Article bodies were not opened.

## Sign-in wall

`app.limitless.ai` redirects to `/signin`: a centered card, Continue with Google, an empty email field, a Privacy Policy link ([desktop](screenshots/signin-light-default.png), [focused, still empty](screenshots/signin-light-email-focused.png), [phone](screenshots/mobile-signin-light-default.png)). Google was not pressed. The field was not filled. The form was not submitted.

## Signup path

`https://app.limitless.ai/signup` is a public "Page not found" card with a Home button ([shot](screenshots/signup-light-default.png)). There is no separate signup form. `/signup` on the marketing host is the same 404 as `/pricing`.

## What is not on the captured surface

Lifelogs, settings, account, form validation, destructive confirmation, and onboarding sit behind the empty wall. `login-extracted` stays `not-started`. The 404 at `/pricing` is the marketing site's not-found page ([shot](screenshots/notfound-light-default.png)). Phone width for an inner page is [privacy](screenshots/mobile-privacy-light-default.png).

## Motion

Transitions on the public pages keep running under `prefers-reduced-motion: reduce`. The probe's verdict on all five pages is `ignores` ([raw/motion.json](raw/motion.json)). Durations are short (100ms on nav colour). That is a finding, not a gap to tidy.
