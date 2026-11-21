# MonoDesk patterns

Public marketing site, signed out, 2026-11-21.

## App shell

The marketing header is a floating pill (`.menu`): 66px tall, 16px radius, fill `rgba(33, 33, 33, 0.25)`, 1px border `rgba(255, 255, 255, 0.08)`, backdrop blur 20px. Logo, Envato "by" mark, four nav items with chevrons (Creative Pros, Features, More open mega menus; Pricing and About are links), Log in, and a highlighter pill "Get started free".

Phone: the same pill collapses to logo, hamburger (`button.hamburger-btn`, aria-label "Toggle menu"), and a round highlighter button. The menu is a fixed full-viewport sheet (`nav.mobile-nav.is-open`). Its list scrolls inside `.mobile-nav-content`. More sits below Pricing and About and expands Help, Blog, and Playground. A sheet titled "On your phone right now?" asks for an email. That field was not filled. A Google One Tap bar can cover the bottom of the phone page. It was hidden for the menu shots and was not clicked.

Screenshots: [home-dark-default.png](screenshots/home-dark-default.png), [mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png), [mobile-home-dark-prompt.png](screenshots/mobile-home-dark-prompt.png).

## Hero

Blue grid (`#1c64f5`) with a white Geist headline at 72px / 82.8px on desktop. Two pills: highlighter "Get started free" and a quieter "Log in". Under them, a product demo frame labelled `app.monodesk.com`. That frame is a marketing render, not the signed-in app.

## Pricing

Three plan cards (Free, Core, Pro) on a light panel. Pro is outlined in highlighter and badged "Most popular". "Get started" on a plan goes to `https://app.monodesk.com/create`, which was not entered. "See full feature set" expands a comparison table on the same page.

Screenshot: [pricing-dark-default.png](screenshots/pricing-dark-default.png).

## Help

Blue hero, white pill search, then white category cards on a light band. Search filters in place. Nothing was submitted.

Screenshot: [help-dark-default.png](screenshots/help-dark-default.png).

## Playground

A separate dark layout with a blue wordmark and square tool tiles. "Have a play. Free, no sign-up." Tool pages that ask for a name, a location, or client details were not filled.

Screenshot: [playground-dark-default.png](screenshots/playground-dark-default.png).

## Not on the public site

Empty, loading, and error states of the workspace, destructive confirmations, and onboarding live in the app. Not captured.
