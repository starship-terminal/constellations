# Patterns

Public signed-out pages only. No screenshots: the preview browser returned no frames. Layout numbers are from `getBoundingClientRect` at innerWidth 1169, devicePixelRatio 2.

## Marketing home

https://www.netflix.com/sg/ redirected from https://www.netflix.com/. English. Signed out.

The page is black. A 760px hero sits under an 80px header. The header holds the wordmark (148 by 40), a language select, and a red Sign In link. The hero copy is centred in a 508px column: a 40px bold headline, a 16px price line, then a prompt and a row of email field plus Get Started. A scrim gradient covers the hero image. The image URL is an nflxext asset. The full scrim stop list was truncated in the reader.

Below the hero, in a column that starts 80px from the left:

1. Trending now. A horizontal row of 140 by 196 tiles, 44px apart.
2. More reasons to join. Four gradient cards, 499 by 198 at this width, radius 16px.
3. Frequently asked questions. Six square rows on `#2d2d2d`.
4. A second email prompt, then the footer.

The footer is `text.secondary`, 16px for the contact line and 14px underlined links. Padding-bottom is 96px.

## Login

https://www.netflix.com/sg/login. The form was not submitted.

Black page, no hero image. The wordmark sits at the top left, 148 by 40. The form column is 440px wide, starting 365px from the left at 1169. The title is 32px bold. The subhead is 18px at 70% white. Two fields (email or mobile number, password) then a 48px Continue button. "Get help" is a blue underlined button. The footer repeats a shorter link list and the language select.

At innerWidth 390 the Continue button was 350px wide and 48px tall. The email chrome stayed 56px. The title stayed 32px bold.

## Signup wall

Get Started and "Or get started with a new account." lead into account creation. That flow was not entered. Plan choice, card entry, and playback are gaps.

## What these pages do not show

No app shell, no search, no table, no empty browse state, no loading playback, no destructive confirm, no onboarding beyond the email prompt.
