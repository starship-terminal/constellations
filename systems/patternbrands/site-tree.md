# Pattern Brands site tree

Mapped on 2026-11-21 from `https://www.patternbrands.com/` in headless Chromium at 1440×900. The crawl followed every same-host link the home page exposes, then checked `/sitemap.xml`, `/robots.txt`, and the usual account paths. `sitemap.xml` returned the Webflow 404. `robots.txt` was empty.

There is no sign-in control and no sign-in form. `/login`, `/signin`, `/sign-in`, `/account` and `/auth` all return the same Webflow "Page Not Found" page.

## Home (`/`)

The page is one product section and a footer. It has no header nav, no menu button, and no form.

| Control | What it does |
|---|---|
| Contact Us (`a.btn`, `mailto:the published contact address`) | Opens the visitor's mail client. Not followed. Hover scales a green circle over the fill. Tab draws a browser focus outline. |
| Onsen card (`a.product_item` → `https://onsentowel.com/`) | Leaves the site. Hover scales the photo to 1.1 and shifts the arrow 4px right. Not followed. |
| Miracle Made card (`a.product_item` → `https://www.miraclebrand.co/`) | Leaves the site. Same hover as the Onsen card. Not followed. |
| GIR card (`a.product_item` → `https://www.gir.co/`) | Leaves the site. Same hover. Not followed. |
| Footer Contact Us (`a.footer_link`, mailto) | Opens mail. Not followed. |
| Footer Careers | Leaves the site for `https://www.linkedin.com/company/pattern-brands/jobs/`. Not followed. |
| Footer Onsen, Miracle Made, GIR | Same brand sites as the cards. Not followed. |
| Footer Terms of Service | Opens `/terms-of-service` on this host. |
| Footer Privacy Policy | The href is `/pattern-privacy-policy`. The server redirects to `/privacy-policy`. |
| Footer `the published contact address` | The visible text is the address. The href is `/#`, so it does not open mail. |
| Footer logo | `a.footer_logo-link` points at `/#`. It stays on the home page. |
| Made in Webflow badge | Webflow's own badge, `https://webflow.com/?utm_campaign=brandjs`. Not part of the product. Not followed. |

The heading rotates the words thoughtful, innovative and beautiful. That is a script on the page, not a navigation control.

## Pages reached

| URL | Status | What is on it |
|---|---|---|
| `https://www.patternbrands.com/` | 200 | Home. Logo, rotating heading, Contact Us, three brand cards, green footer. |
| `https://www.patternbrands.com/terms-of-service` | 200 | Long legal page. Title, Overview, body copy, underlined external legal links. Same footer as home. |
| `https://www.patternbrands.com/privacy-policy` | 200 | Privacy policy. Reached from the redirect of `/pattern-privacy-policy`. |
| `https://www.patternbrands.com/pattern-privacy-policy` | 200, redirects | Lands on `/privacy-policy`. |
| `https://www.patternbrands.com/login` | 404 | Webflow Page Not Found, with a Go Home link to `/`. |
| `https://www.patternbrands.com/signin` | 404 | Same Page Not Found. |
| `https://www.patternbrands.com/sign-in` | 404 | Same Page Not Found. |
| `https://www.patternbrands.com/account` | 404 | Same Page Not Found. |
| `https://www.patternbrands.com/auth` | 404 | Same Page Not Found. |
| `https://www.patternbrands.com/terms-and-conditions` | 404 | Linked from the terms body as a relative path that does not exist. Same Page Not Found. |
| `https://www.patternbrands.com/sitemap.xml` | 404 | Webflow 404, not a sitemap. |

## Not on this site

Brand stores (Onsen, Miracle Made, GIR), the LinkedIn careers page, and mailto links sit on other hosts. They were recorded as exits and not captured.
