# Patterns

## Marketing home

A fixed 52px white bar. The wordmark sits at the left, 53 by 20. Products, Mission and Careers sit in the centre, 14px / 400. Sign in sits at the right as an ink pill.

The headline is Sana Sans 400, 61.52px at innerWidth 1169, ink, letter-spacing -1.8456px. The subheading is 16px / 400, letter-spacing -0.16px. Under that, two product cards sit side by side, each 544 by 583, radius 24px, with a 20px title and an Explore pill. [screenshots/home-light-default.png](screenshots/home-light-default.png)

The footer is four columns of 14px links, padding 46px 0 16px, then "Sana Labs © 2026" in ink at 50% opacity. The home page is short: scrollHeight was 1243 at the 1169 viewport.

At 390 the nav collapses to the wordmark, Sign in and a 38px menu button. The headline is 44px, letter-spacing -1.32px. The cards stack at 342px wide. [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png)

## Sign-in

`https://sana.ai/sign-in-to-sana` sets `html.dark`. The page background is `#131314`. A 44px bar holds a mark and a 302px pill: Overview, Privacy and terms, FAQ, on `#1e1f20`.

The form column is 352px wide. The title is 34px / 500, two lines. Under it, a Google Identity Services button (not clicked), the word "or", the work-email field, and a disabled submit. Agreement copy is 13px at 40% fog. A 653 by 605 panel, `#17181a`, radius 18px, sits to the right. Its image had no painted source in the reading.

There is no screenshot of this page. The preview tab could not produce frames.

## Code step

Submitting the email form replaces the field with "We sent you a code", a 400px pill of six digits, Resend code, Back and a disabled Continue. Back is the only filled button on that step: fog face, night label. The code was not entered. A native form submit left the page for an API URL that showed "Invalid code", and that URL was not used as a surface.

## FAQ

The same sign-in page holds an FAQ accordion below the form. Items are 40px buttons, radius 14px. The open answer is 14px at 40% fog. One item was opened and measured.
