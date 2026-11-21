# Avnier public site tree

Mapped from [https://avnier.com/](https://avnier.com/) on 2026-11-21 in headless Chrome (Playwright, `channel: chrome`), signed out, French locale. Desktop viewport 1440×900. Phone checks used 390×844. Nothing was typed, submitted, or added to the cart. Login, register, recover, newsletter, contact, loyalty, and the first-order code dialog were not filled. Google, Apple, Facebook, Microsoft, and SSO were not clicked. The Axeptio consent layer, the shipping-country popup, and the Klaviyo first-order dialog were hidden after the arrival shot, never answered.

Each control is one of: **page** (navigation), **menu** (stays on the page), **overlay** (drawer or modal that stays on the page), **dialog**, or **login wall** (branch stopped).

## Header (every public page)

| Control | Opens | Where |
|---|---|---|
| Wordmark | page | `/` |
| SHOP | menu | Mega-menu panel on the same URL. Hover opens a full-width dropdown (measured 1440×767). Links below. |
| MARQUE | menu | Same dropdown, second panel (measured 619px tall). Links below. |
| SECONDE MAIN | page | `https://secondemain.avnier.com` (leaves avnier.com; not walked) |
| ARCHIVE SALE | page | `/collections/archive-sale` |
| Recherche | overlay | `details-modal` search dialog on the same URL (`aria-haspopup="dialog"`). Placeholder "Recherche". Not submitted. |
| CONNEXION | login wall | `/account/login`. Branch stopped. |
| PANIER | overlay | `side-cart` drawer on the same URL (JS intercepts `/cart`). Empty state: "MON PANIER - 0 ARTICLE / LE PANIER EST VIDE". Close control stays on the page. |
| Skip link "IGNORER ET PASSER AU CONTENU" | menu | `#MainContent` on the same page |

Phone header (390): the wordmark, Recherche, CONNEXION, and PANIER stay. SHOP and MARQUE are not in the bar. A Menu summary (`aria-label="Menu"`, visible text "E-SHOP") opens the **menu drawer** (overlay) on `/`.

## SHOP menu

Stays on the page until a child link is chosen. Each child is a page.

| Link | Opens |
|---|---|
| Tous les produits | page `/collections/tous-les-produits` |
| Cartes cadeaux | page `/products/ecarte-cadeau` |
| Bonnets et casquettes | page `/collections/casquettes-et-bonnets` |
| Crewnecks et pulls | page `/collections/crewnecks-et-pulls` |
| Hoodies | page `/collections/hoodies` |
| T-shirts | page `/collections/t-shirts` |
| Vestes | page `/collections/vestes` |
| Pantalons et shorts | page `/collections/pantalons-et-shorts` |
| Chaussures | page `/collections/chaussures` |
| Accessoires | page `/collections/accessoires` |
| Patch velcro | page `/collections/patch-velcro` |
| Gamme pro | page `/pages/gamme-pro` |
| STUNT MÉCANIQUE | page `/pages/stunt-mecanique-capsule-vetements-cascade-avnier` |
| AVNIER+SAINT JAMES | page `/pages/avnier-saint-james-intervalle-iii` |
| AVNIER + PALÉO 2026 | page `/pages/avnier-x-paleo-2026` |
| AVNIER + EVIL DEAD | page `/pages/avnier-evil-dead` |
| AVNIER + CUPRA | page `/pages/avnier-cupra` |
| Essentiels | page `/collections/les-essentiels` |
| Nouveautés | page `/collections/les-nouveautes` |
| Archive sale | page `/collections/archive-sale` |

The desktop header also keeps a hidden inline list (`display: none` at 1440) with a shorter shop list plus Doudoune Symphony (`/products/doudoune-symphony`), Chaussures AV-1 (`/products/av-1`), and Carte cadeau. Those targets are public pages. They are not a second visible menu.

## MARQUE menu

| Link | Opens |
|---|---|
| AUDIO VISUAL WORK WEAR | page `/pages/avww` |
| MÉTHODE | page `/pages/methode` |
| HISTOIRE | page `/pages/histoire` |
| QUE SIGNIFIE AVNIER | page `/pages/que-signifie-avnier` |
| Programme Professionnel All Access | page `/pages/pro` |
| SECONDE MAIN | page `https://secondemain.avnier.com` (not walked) |
| HISTOIRE / Découvrir les backstages | page `/pages/histoire` (image tile, same URL) |
| AVNIER / La signification | page `/pages/que-signifie-avnier` (image tile, same URL) |

## Phone menu drawer

Opened by Menu on `/` at 390. Stays on the page. FERMER closes it. Child links match the SHOP and MARQUE lists above, plus:

| Control | Opens |
|---|---|
| Recherche | overlay (search dialog) |
| CONNEXION | login wall `/account/login` |
| PANIER | overlay (side-cart; `/cart` itself is a 404 page) |
| LIVRAISON | page `/pages/livraison` |
| RETOURS | page `/pages/retour` |
| AIDE & CONTACT | page `/pages/contact` |
| COMPTE | login wall `/account/login` |
| PROGRAMME FIDÉLITÉ | overlay `#loloyal/home` (Loloyal iframe on the same URL). Not signed in. |
| Facebook, Instagram, YouTube | page, off-site. Not walked. |
| Shipping country `<select>` | menu (native select). Not changed. |

## Collection pages (product grids)

Reached from SHOP, the footer, or a product card. Each is a page. Confirmed 200: archive sale, tous les produits, crewnecks et pulls, hoodies, casquettes et bonnets, t-shirts, vestes, pantalons et shorts, chaussures, accessoires, patch velcro, les essentiels, les nouveautés, intervalle-iii, stunt-mecanique.

| Control | Opens |
|---|---|
| Product card | page `/products/<handle>` (grid sample, not a fixed catalogue) |
| FILTRER / PRIX + | menu (disclosure on the same URL). Options: Moins de 50€, Moins de 100€, Moins de 150€, Plus de 150€. Not applied. |
| COULEUR + | menu. Colour checkboxes (Argile rouge, Blanc, Bleu, and further swatches). Not applied. |
| TAILLE + | menu. Size checkboxes (XS through XXXL, and numeric sizes). Not applied. |
| TYPE DE PRODUIT + | menu. Type checkboxes (Accessoire, Bonnets, Cartes-cadeaux, and further types). Not applied. |
| TRIER PAR | menu (`select[name="sort_by"]`). Options: Recommandés, Le plus pertinent, Meilleures ventes, Moins chers, Plus chers. Not changed. |

## Product page

Sample used for controls: `/products/doudoune-symphony` (200, "Doudoune SYMPHONY"). Other public product URLs confirmed 200 and not treated as a second system: veste-layout-cobra, t-shirt-source-black-stunt-association, velcro-stunt-mecanique, bonnet-fujames-avnier-x-saint-james, jeans-roadie-cobra, pull-tokyeux-avnier-x-saint-james, jogging-avrapp-avnier-x-saint-james, crewneck-accelerator, av-1, ecarte-cadeau.

| Control | Opens |
|---|---|
| SIZE radio (XS, S, M, L, XL, XXL on this product) | menu (stays on the page; selects a variant). XL and XXL were marked unavailable on this product. Not used to add to cart. |
| COULEUR radio (Fuchsia nebuleux, Noir, Vert Citron on this product) | menu (stays on the page). |
| CHOISIR LA BONNE TAILLE | dialog (panel titled "COMMENT CHOISIR LA BONNE TAILLE ?", with mannequin measurements and a size chart). The no-JS fallback is a page: `/pages/doudoune-symphony-guide-des-tailles` (200). |
| Media toggle "OUVRIR LE MÉDIA … DANS UNE FENÊTRE MODALE" | dialog (`.product-media-modal__dialog`). |
| AJOUTER AU PANIER | not pressed. Would be a cart action. |
| Quantity | not present on this product. |

## Content pages

Confirmed 200 from the home page, SHOP, MARQUE, or the footer.

| URL | Title |
|---|---|
| `/pages/gamme-pro` | GAMME PRO |
| `/pages/avww` | AVWW |
| `/pages/methode` | MÉTHODE |
| `/pages/histoire` | HISTOIRE |
| `/pages/que-signifie-avnier` | QUE SIGNIFIE AVNIER |
| `/pages/pro` | Pro |
| `/pages/stunt-mecanique-capsule-vetements-cascade-avnier` | STUNT MÉCANIQUE |
| `/pages/avnier-saint-james-intervalle-iii` | AVNIER + SAINT JAMES |
| `/pages/avnier-x-paleo-2026` | AVNIER x PALÉO 2026 |
| `/pages/avnier-evil-dead` | AVNIER + EVIL DEAD |
| `/pages/avnier-cupra` | AVNIER + CUPRA |
| `/pages/livraison` | LIVRAISON |
| `/pages/retour` | Retours |
| `/pages/contact` | Contact |
| `/pages/vie-privee` | Vie privée |
| `/pages/cgv` | CGV |
| `/pages/mentions-legales` | Mentions légales |

Home hero tiles also link to collaboration and capsule pages already listed above. They are pages.

Contact (`/pages/contact`) shows a form (name, email, phone, comment, file). Not filled. Not submitted.

## Footer

Same link set on the pages that render `#shopify-section-v2-footer`.

| Control | Opens |
|---|---|
| E-shop column (Tous les produits through Carte cadeau) | page, same targets as the SHOP menu plus `/products/doudoune-symphony` and `/products/av-1` |
| LIVRAISON, RETOURS, AIDE & CONTACT | page `/pages/livraison`, `/pages/retour`, `/pages/contact` |
| COMPTE | login wall `/account/login` |
| PROGRAMME FIDÉLITÉ | overlay `#loloyal/home` |
| MARQUE column | page, same targets as the MARQUE menu |
| Facebook, Instagram, YouTube | page, off-site. Not walked. |
| VIE PRIVÉE, CGV, MENTIONS LÉGALES | page `/pages/vie-privee`, `/pages/cgv`, `/pages/mentions-legales` |
| Newsletter email ("Votre adresse e-mail") | not filled. Not submitted. |

A block above the footer links "MARQUE MÉTHODE" and "MARQUE AUDIO VISUAL WORK WEAR" to `/pages/methode` and `/pages/avww`.

## Login wall (branch stopped)

| URL | What is on the gate | What was not done |
|---|---|---|
| `/account/login` | Email ("E-mail"), password ("Mot de passe"), CONNEXION, "MOT DE PASSE OUBLIÉ ?" (`#recover`), "CRÉER UN COMPTE" | No email typed. No password typed. No submit. No SSO. |
| `/account/register` | First name, last name, email, password, "CRÉER MON COMPTE" (200, title "Créer un compte") | Not filled. Not submitted. Account not created. |
| `#recover` on the login page | Recover email field, Envoyer, Annuler | Not filled. Not submitted. |

`/cart` is a 404 page ("404 Page introuvable") for a signed-out visit. The working cart is the PANIER drawer.

## Arrival overlays

| Overlay | Opens | Notes |
|---|---|---|
| Axeptio cookie bar | dialog | "AVNIER UTILISE DES COOKIES…". Buttons: Non merci, Je choisis, OK pour moi. Not clicked. |
| Shipping country popup | dialog | `#section-v2-shipping-country-popup`. Not answered. |
| First-order code | dialog | Klaviyo form, "-10% SUR TA PREMIÈRE COMMANDE", fields "Ton prénom" and "Ton e-mail", button "RECEVOIR LE CODE". Not filled. Not submitted. |

## Off-site and not walked

- `https://secondemain.avnier.com`
- `https://www.avnier.nopli.eu` (a SECONDE MAIN target inside a hidden dropdown slot)
- Facebook, Instagram, YouTube profile links
- Checkout, account home, orders: behind the login wall
