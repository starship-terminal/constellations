# Preply patterns

Signed-out marketing and login chrome. First read 2026-11-19. Site tree and extra screens refreshed 2026-11-21. The control map is [site-tree.md](site-tree.md).

## Home

A 64px near-black bar ("Preply stands with Ukraine") sits above a pink header and a pink hero. The header class computes to the same pink as the hero (#ff7aac). The hero is a large Platform headline, a black "Find your tutor" button, and a lesson-progress illustration. Below that the page goes white: stat row, language tiles, step cards with a 1px black border and 4px radius.

[home](screenshots/home-light-default.png)

## Login

Centered column on white. "Log in", underlined signup links, three outlined social buttons (Google, Facebook, Apple), a ghost corporate-SSO link, then email and password fields and a pink "Log in" submit. The form was not submitted. Signup is not email-only.

[login](screenshots/login-light-default.png)

## Find tutors

Public search and tutor list. The hero is a subject field and a pink "Find your tutor" button. Below that, filter chips (goal, focus, price, language, country, category, availability, sort) sit over tutor cards. Goal opens a dialog. Price opens a range. The search icon expands "Search by name or keyword". Book trial lesson was not followed.

[tutors](screenshots/tutors-light-default.png), [list](screenshots/tutors-light-list.png), [goal](screenshots/tutors-light-filter.png)

## Other public pages

Teach, business, proven progress, stand-with-Ukraine, and a 404. Same header. Business has a lead form (name, email, job). It was not filled in.

## Mobile

390x844 at 2x. The hero headline wraps to four lines. A hamburger opens a right-hand drawer (Log In, Home, Find tutors, For business, Proven Progress, Become a tutor, Messages, Help, then language and currency).

[mobile home](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-menu.png), [mobile tutors](screenshots/mobile-tutors-light-list.png)

## Theme

One theme. prefers-color-scheme: dark did not change the pink or the ink.
