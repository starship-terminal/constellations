# Fable patterns

Public marketing site. The signed-in app is behind `/signin` and was not entered. Control destinations are in [site-tree.md](site-tree.md).

## Shell

A 60px header (`core.size.header`) with the mark, Clubs, Books, Library, then Blog, a person icon, and a cart. On a 390px phone the word nav collapses to a hamburger. The footer is an inverse band (`light.background.inverse`) with Clubs, Explore, About, Learn more, and social links.

## Home

A forest hero (`light.background.hero`) with Heldane Display at 72px and a cream quiet pill, then a cover carousel into Discover, then club cards, then feature blocks. [screenshots/home-light-default.png](screenshots/home-light-default.png).

## Catalogs

Clubs is a title plus genre chips and horizontal club rows. Books is the same shape with book rows. A club page and a book page are a title, a primary pill, and related rows. [screenshots/clubs-light-default.png](screenshots/clubs-light-default.png), [screenshots/book-light-default.png](screenshots/book-light-default.png).

## Overlays

Sign up is a centered dialog, not a page. Get the app is a QR dialog. Club search and book shop are search dialogs with an empty result line. Discover's "What is this?" is a short explainer. [screenshots/home-light-signup.png](screenshots/home-light-signup.png), [screenshots/home-light-get-app.png](screenshots/home-light-get-app.png).

## Login wall

`/library` redirects to `/signin?next=%2Flibrary`. `/login` is a 404. [screenshots/signin-light-default.png](screenshots/signin-light-default.png), [screenshots/notfound-light-default.png](screenshots/notfound-light-default.png).

## Empty and error

Club search with no query says "Clubs will appear here". Book search says books will appear. The 404 is an illustrated "Oops!" with Go back. No toast, no destructive confirm, and no onboarding were reached. Forms were not submitted, so validation errors were not captured.
