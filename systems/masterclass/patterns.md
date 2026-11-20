# Patterns

Public MasterClass, signed out, 2026-11-21. The site tree is [site-tree.md](site-tree.md).

## App shell and navigation

A black bar. The wordmark sits left, then Browse (a menu of categories) and a search field. Gifts, View Plans and Log In are quiet text links. Get MasterClass is the only filled pink button. A thinner row above links to Certificates, On Call, Executive and At Work. Phone width keeps the same controls. There is no hamburger.

Browse opens a dark menu on the same page. View All Categories goes to `/categories`. Category buttons filter the homepage carousel and stay on `/`.

## Form with a validation error

The homepage intent list shows "Please select at least one option to continue" before a choice is made. The find-my-classes quiz uses checkboxes and Next. Those forms were not submitted. Newsletter and contact fields were not filled, so their error states are not captured.

## Empty, loading and error

A request for a path that does not exist is captured as `notfound-dark-default`. Search with no query shows popular searches, not an empty state. Loading is the trailer dialog's "Loading video..." line. A dedicated empty library does not exist on the public site.

## Destructive confirmation

Not present on the public site. Account deletion and refund requests sit behind login or the help centre article, which is an explanation, not a confirm dialog.

## Feedback after an action

The promo strip and the pink Get MasterClass button are the feedback for the offer. Closing the strip is a dismiss, not a toast. No toast was observed.

## Search and filtering

The header field opens a menu of popular searches. Typing shows class links. Enter was not pressed. Category chips on the homepage, the gift page and the promotion page filter cards in place. The categories page is the full filter index.

## List or table

Class cards are the list. A category page is a grid of the same cards. The sitemap is a link list. No data table was on the public pages.

## Onboarding

The homepage "What brings you to MasterClass today?" and `/find-my-classes` are the public onboarding quiz. The quiz was not completed, because the next steps ask for goals and then a signup wall.
