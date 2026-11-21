# GitHub public patterns

How the signed-out pages combine the components in [components.md](components.md). Mapped 2026-11-22.

## Marketing chrome

A white header sits on a white page. The left cluster is the octocat and four menus plus Pricing. The right cluster is Search, Sign in, and a black Sign up pill. Opening a menu replaces the page under the header with a white panel of columns. Opening Search replaces that with a dialog. Only one of those is open at a time in the shots.

On a 390px screen the menus collapse into one drawer. The drawer lists the same four groups, then Pricing, then a full-width black Sign up button, then a Search field. The person icon in the phone header goes to the login wall.

## Homepage

A black display heading, an empty email field, a green signup button, and a quiet download button. Below that, a product walkthrough (Review changes, Direct the fix, Check the results, Approve and merge, See it shipped) is a public demo, not a signed-in pull request. An activity ticker lists public repositories. Those links were not followed. A Universe recap banner sits above the header content. It was not followed.

## Pricing

Three plan cards: Free, Team, Enterprise, with USD prices. The page is long. The full shot stops at 12000 CSS px of 15997. Trial and sales buttons were not clicked, so the next screen is the signup or sales wall, not a checkout.

## Feature and company pages

`/features`, Copilot, Actions, Codespaces, `/platform`, `/enterprise`, `/team`, `/resources`, `/about`, customer stories, trust center, security, marketplace, trending, explore, sponsors, why GitHub, education, GitHub Mobile, and the sitemap use the same logged-out header. They were opened as pages. Their inner menus were not re-opened.

## Public repository

`https://github.com/github/docs` loads signed out. The file list and the public README are visible. Star and Fork were not clicked. Other people's public names on that page are part of the public repository.

## Empty states

A missing path paints a 404 with an octocat and a search field. A search URL with no matching repositories paints "Your search did not match any repositories". Neither field was typed.

## Auth walls

Sign in opens `/login` with empty fields. The card lists Google, Apple, passkey, forgot password, and create account. None of those were used. Sign up opens `/signup` and stops on a captcha. The homepage email field was left empty, so it never became a signup submission.

## Footer

Four link columns, a newsletter field, Terms, Privacy, cookie controls, and a language select. The newsletter was not submitted. The language was not changed. Cookie controls were not used.
