# Hims UK site tree

Mapped 2026-11-21 from the public homepage at https://www.forhims.co.uk/ before screenshots. Signed out. `html.brand-hims.variant-care-sans`. One light theme (`color-scheme: normal`). No dark-theme control.

A Ketch dialog ("About cookies on our site", Accept all, Customise) covers the page. It was hidden, not clicked. No password, email, phone, or code was typed. No form was submitted. No identity provider was clicked. No consultation or purchase was started.

forhims.co.uk does not redirect to forhims.com. forhers.com is a different product. The US host www.hims.com is a different domain.

## Shell (desktop)

| Control | Opens |
|---|---|
| Migration strip ("We're moving to a new platform… Click here for details") | page https://www.forhims.co.uk/migration-privacy |
| Logo (`a[aria-label="Link to homepage"]`) | page https://www.forhims.co.uk/ |
| Weight | page https://www.forhims.co.uk/weight-loss |
| Hair | page https://www.forhims.co.uk/hair-loss |
| Sex (`button[aria-label="Sex"]`) | flyout on the same page (`.floating-menustyles__MenuItemsContainer`). Erectile Dysfunction opens https://www.forhims.co.uk/erectile-dysfunction. Premature Ejaculation opens https://www.forhims.co.uk/premature-ejaculation |
| Learn (`button[aria-label="Learn"]`) | flyout on the same page. Blog opens https://www.forhims.co.uk/blog. Condition Guides opens https://www.forhims.co.uk/conditions |
| Treatments | page https://www.forhims.co.uk/customer/treatments. Signed-out care portal. Login wall. Branch stopped. |
| Messaging | page https://www.forhims.co.uk/customer/support. Login wall. Branch stopped. |
| Profile | page https://www.forhims.co.uk/customer/profile. Login wall. Branch stopped. |
| LOGIN (`button[data-testid="global-navigation-login"]`) | On `/customer/login` it opens a login drawer on the same page (email, password, Create an account, Forgot your password). On `/` the same button left the marketing page for a full-page "Log into Hims" form in this session. Login wall. Not typed, not submitted. No Google, Apple, or other identity provider was on either form. |
| Menu (`button[data-testid="global-navigation-open-menu"]`) | drawer on the same page (`.drawerstyles__Frame`). Close (`[data-testid="global-navigation-close-menu"]` / "Close the drawer") returns to the same page. |

The menu drawer lists ACCOUNT and EXPLORE. The explore rows are buttons that navigate, not in-drawer expansions.

| Drawer control | Opens |
|---|---|
| Get started (`button[data-testid="drawer-action-get-started"]`) | register / create-account drawer. Signup wall. Not submitted. |
| Log in (`button[data-testid="drawer-action-login"]`) | login drawer. Login wall. Not submitted. |
| Forgot password (`button[data-testid="drawer-action-forgot-password"]`) | forgot-password drawer. Not submitted. |
| Weight | page https://www.forhims.co.uk/weight-loss |
| Hair | page https://www.forhims.co.uk/hair-loss |
| ED | page https://www.forhims.co.uk/erectile-dysfunction |
| Early Climax | page https://www.forhims.co.uk/premature-ejaculation |

## Home https://www.forhims.co.uk/

| Control | Opens |
|---|---|
| Explore treatments (hero, a button) | in-page treatment cards, same page |
| Lose weight | page https://www.forhims.co.uk/c/wl. Consultation start. Not entered. |
| Have great sex | page https://www.forhims.co.uk/c/e. Consultation start. Not entered. |
| Regrow hair | page https://www.forhims.co.uk/c/hl. Consultation start. Not entered. |
| Have longer sex | page https://www.forhims.co.uk/c/p. Consultation start. Not entered. |
| Explore treatments (weight section) | page https://www.forhims.co.uk/weight-loss |
| Explore ED treatments | page https://www.forhims.co.uk/erectile-dysfunction |
| Explore hair loss treatments | page https://www.forhims.co.uk/hair-loss |
| Explore early climax treatments | page https://www.forhims.co.uk/premature-ejaculation |
| Get started (product cards) | consultation pages `/c/wl`, `/c/hl`, `/c/e`, `/c/p`. Not entered. |
| Learn more (product cards) | category pages `/weight-loss`, `/hair-loss`, `/erectile-dysfunction`, `/premature-ejaculation` |
| What is Hims? / How does Hims work? | in-page FAQ disclosure, same page |
| Get started (lower page) | page https://www.forhims.co.uk/c. Treatments index. A Get started there can start a consultation. Not entered past the public index. |

## Footer (every page)

Treatments: Weight Management `/weight-loss`, Hair Loss `/hair-loss`, Erectile Dysfunction `/erectile-dysfunction`, Premature Ejaculation `/premature-ejaculation`.

Learn: About Us `/about`, How It Works `/how-it-works`, Good Health `/blog`, Condition Guides `/conditions`, Purpose `/purpose`, Reviews `/hims-reviews`.

Connect: Investors leaves for https://investors.hims.com. Careers leaves for https://www.hims.com/careers-professionals. Help Centre leaves for https://ukhims.zendesk.com/hc/en-gb. Contact Us leaves for a Zendesk article. Press is `mailto:press@forhims.co.uk`. None of those was opened as a product surface.

Legal: Terms & Conditions `/terms-and-conditions`, Privacy Policy `/privacy-policy`, Pharmacy Terms `/pharmacy-terms`, Sitemap `https://www.forhims.co.uk/sitemap.html`, Complaints `/complaints`. LegitScript and CQC badges leave the site.

## Phone (390)

The same header collapses. Weight, Hair, Sex and Learn stay reachable from the menu drawer. LOGIN and the menu button stay in the header. Category tiles and footer links are the same pages.

## Login walls (recorded, not entered)

| Control or URL | What loaded |
|---|---|
| LOGIN, drawer Log in | Login drawer on the current page. Email and password. Branch stopped. |
| Get started, Create an account | Register drawer. Branch stopped. |
| Forgot password | Reset drawer. Branch stopped. |
| `/customer/treatments`, `/customer/support`, `/customer/profile` | Signed-out care portal. Account wall. Branch stopped. |
| `/c/wl`, `/c/e`, `/c/hl`, `/c/p` | Consultation start. Not entered. |
