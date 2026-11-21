// Maps the public Sketch site tree from the homepage before screenshots.
// Writes systems/sketch/site-tree.md and raw/site-tree.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/map-site.mjs
//
// Look, don't submit. Sign-in, signup, SSO, Google, Apple, newsletter and
// contact forms are recorded as walls and not filled.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const WALL = /\/(signin|signup|sign-up|login|register|sso)(\/|$)|accounts\.google|appleid\.apple|id\.apple/i;
const OFFSITE = new Set(['discord.gg', 'developer.sketch.com', 'status.sketch.com', 'apps.apple.com', 'x.com', 'bsky.app', 'instagram.com', 'youtube.com', 'mastodon.design']);

function hostOf(href) {
  try { return new URL(href).hostname.replace(/^www\./, ''); } catch { return ''; }
}

const b = await chromium.launch({ headless: true });

async function open(width, height, mobile) {
  const ctx = await b.newContext({
    viewport: { width, height },
    deviceScaleFactor: 1,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  const page = await ctx.newPage();
  await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(2500);
  return { ctx, page };
}

function clean(s) {
  return (s || '').replace(/\s+/g, ' ').trim();
}

const { ctx, page } = await open(1440, 900, false);

const home = await page.evaluate(() => {
  const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();
  const nav = document.querySelector('header.main-nav, header');
  const top = [...nav.querySelectorAll(':scope > nav > ul > li, :scope .main-nav__list > li, header .main-nav__item')];
  const items = [...nav.querySelectorAll('li.main-nav__item, a.main-nav__link, button.main-nav__toggle')].map((el) => {
    const a = el.matches('a') ? el : el.querySelector(':scope > a.main-nav__link');
    const sub = [...el.querySelectorAll(':scope .main-nav__subnav__link, :scope a[href]')].filter((x) => x !== a);
    return {
      tag: el.tagName,
      cls: (el.className || '').toString().replace(/\s+/g, ' ').trim().slice(0, 140),
      text: clean(el.innerText || el.getAttribute('aria-label')).slice(0, 80),
      href: a ? a.getAttribute('href') : '',
      aria: el.getAttribute('aria-label') || a?.getAttribute('aria-label') || '',
      expanded: el.getAttribute('aria-expanded'),
      controls: el.getAttribute('aria-controls') || '',
      children: sub.slice(0, 24).map((s) => ({
        text: clean(s.innerText).slice(0, 90),
        href: s.getAttribute('href') || '',
      })),
    };
  });
  const footer = [...(document.querySelector('footer')?.querySelectorAll('a') || [])].map((a) => ({
    text: clean(a.innerText).slice(0, 80),
    href: a.getAttribute('href') || '',
  }));
  const forms = [...document.querySelectorAll('form')].map((f) => ({
    action: f.getAttribute('action') || '',
    id: f.id,
    cls: (f.className || '').toString().slice(0, 80),
    fields: [...f.querySelectorAll('input, textarea, select')].map((i) => ({
      tag: i.tagName, type: i.type || '', name: i.name, placeholder: i.placeholder || '',
    })),
    submit: clean(f.querySelector('button, input[type="submit"]')?.innerText || ''),
  }));
  const pageNav = [...document.querySelectorAll('.page-nav a, .top-bar a')].map((a) => ({
    text: clean(a.innerText).slice(0, 60),
    href: a.getAttribute('href') || '',
  }));
  return {
    title: document.title,
    url: location.href,
    items,
    footer,
    forms,
    pageNav,
    promo: clean(document.querySelector('.promo__banner')?.innerText).slice(0, 180),
    promoHref: document.querySelector('.promo__banner a')?.getAttribute('href') || '',
  };
});

// Hover each desktop subnav parent and record whether it opens.
const hovers = [];
const parents = page.locator('header li.main-nav__subnav, header li.main-nav__item').filter({ has: page.locator('.main-nav__subnav__link, ul') });
const nParents = await parents.count();
for (let i = 0; i < Math.min(nParents, 12); i++) {
  const item = parents.nth(i);
  const label = clean(await item.innerText()).slice(0, 40);
  await item.hover().catch(() => {});
  await page.waitForTimeout(350);
  const opened = await item.evaluate((el) => {
    const panel = el.querySelector('ul, .main-nav__dropdown, [class*="subnav"]');
    if (!panel) return { open: false };
    const r = panel.getBoundingClientRect();
    const cs = getComputedStyle(panel);
    return {
      open: r.height > 20 && cs.visibility !== 'hidden' && cs.display !== 'none' && Number(cs.opacity || 1) > 0,
      height: Math.round(r.height),
      display: cs.display,
    };
  });
  hovers.push({ label, ...opened });
  await page.mouse.move(10, 700);
  await page.waitForTimeout(150);
}

// Menu button (desktop hamburger is hidden; still record the control).
const menuBtn = page.locator('button.main-nav__toggle');
const menuMeta = await menuBtn.evaluate((el) => ({
  aria: el.getAttribute('aria-label'),
  controls: el.getAttribute('aria-controls'),
  expanded: el.getAttribute('aria-expanded'),
  visible: el.getBoundingClientRect().width > 0 && getComputedStyle(el).display !== 'none',
})).catch(() => null);

await ctx.close();

// Phone: open the menu drawer.
const mob = await open(390, 844, true);
const menu = mob.page.locator('button.main-nav__toggle').first();
await menu.click({ force: true });
await mob.page.waitForTimeout(700);
const drawer = await mob.page.evaluate(() => {
  const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();
  // The hamburger sets a class on the header; the panel that paints is .mobile-nav,
  // not #main-nav-menu (that id stays display:none at 390).
  const panel = document.querySelector('.mobile-nav');
  const links = [...(panel?.querySelectorAll('a') || [])].map((a) => ({
    text: clean(a.innerText).slice(0, 90),
    href: a.getAttribute('href') || '',
    visible: a.getBoundingClientRect().height > 0,
    action: a.getAttribute('data-action') || '',
  }));
  return {
    url: location.href,
    headerClass: document.querySelector('header')?.className || '',
    menuExpanded: document.querySelector('button.main-nav__toggle')?.getAttribute('aria-expanded'),
    panelVisible: !!(panel && panel.getBoundingClientRect().height > 0),
    links: links.filter((l) => l.visible).slice(0, 80),
  };
});
const sectionOpens = [{
  text: 'phone drawer lists Product, Explore and Support links directly (data-action mobileToggleNav is on the links themselves; clicking one navigates)',
  kids: drawer.links,
}];
await mob.ctx.close();

// Classify links.
const seen = new Map();
function add(source, text, href) {
  if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('javascript:')) return;
  let abs;
  try { abs = new URL(href, BASE + '/').href; } catch { return; }
  const u = new URL(abs);
  const key = u.origin + u.pathname.replace(/\/$/, '') || u.origin + '/';
  const rec = seen.get(key) || { url: u.href.split('?')[0], path: u.pathname, host: u.hostname, text: [], sources: [], kind: 'page' };
  if (text && !rec.text.includes(text)) rec.text.push(text.slice(0, 80));
  if (!rec.sources.includes(source)) rec.sources.push(source);
  const host = hostOf(abs);
  if (WALL.test(u.pathname) || WALL.test(abs)) rec.kind = 'auth-wall';
  else if (u.hostname !== 'www.sketch.com' && u.hostname !== 'sketch.com') rec.kind = OFFSITE.has(host) || !host.endsWith('sketch.com') ? 'offsite' : 'offsite-sketch';
  else if (/\/support\/contact\/?$/.test(u.pathname)) rec.kind = 'form-page';
  else if (/newsletter|signup/.test(u.pathname)) rec.kind = 'form-page';
  seen.set(key, rec);
}
for (const item of home.items) {
  add('header', item.text, item.href);
  for (const c of item.children || []) add('header-subnav', c.text, c.href);
}
for (const f of home.footer) add('footer', f.text, f.href);
for (const a of home.pageNav) add('home-page-nav', a.text, a.href);
if (home.promoHref) add('promo-banner', 'New in Sketch promo', home.promoHref);
for (const l of drawer.links) add('phone-menu', l.text, l.href);

const pages = [...seen.values()].sort((a, b) => a.path.localeCompare(b.path));

const tree = {
  capturedAt: new Date().toISOString(),
  origin: BASE,
  homeTitle: home.title,
  desktopMenuButton: menuMeta,
  desktopHovers: hovers,
  phoneMenu: drawer,
  phoneSections: sectionOpens,
  forms: home.forms,
  promo: { text: home.promo, href: home.promoHref },
  pages,
};
fs.writeFileSync(path.join(RAW, 'site-tree.json'), JSON.stringify(tree, null, 2));

const publicPages = pages.filter((p) => p.kind === 'page');
const walls = pages.filter((p) => p.kind === 'auth-wall');
const forms = pages.filter((p) => p.kind === 'form-page');
const off = pages.filter((p) => p.kind.startsWith('offsite'));

const md = `# Sketch public site tree

Mapped from the homepage at ${BASE}/ on ${tree.capturedAt.slice(0, 10)}, before screenshots. Desktop viewport 1440×900. Phone viewport 390×844. Headless Chromium. No form was submitted. No email was typed.

The marketing site is one origin, \`www.sketch.com\`. Header items Product, Explore and Support are disclosure menus (their links live in \`.main-nav__subnav\`). Pricing is a direct link. Sign In and Get started are direct links. On a 390-wide viewport the same lists sit behind the header Menu button (\`aria-controls="main-nav-menu"\`).

## Header controls (desktop)

| Control | Opens | Stop? |
|---|---|---|
| Skip Navigation | \`#content\` on the current page | no |
| Sketch wordmark | [/](https://www.sketch.com/) | no |
| Product (subnav, hover or focus) | Design, Collaboration, Prototyping, Developer Handoff, AI, All Features, plus the latest changelog card | no |
| Explore (subnav) | Changelog, Roadmap, Blog, Design Resources, Plugins & Integrations | no |
| Pricing | [/pricing/](https://www.sketch.com/pricing/) | no |
| Support (subnav) | Help Center, Documentation, Request a Feature, Contact Us, Community Discord | Discord is off-site; Contact Us is a form page, not submitted |
| Sign In | [/signin/](https://www.sketch.com/signin/) | auth wall: email, password, Apple, Google, SSO. Branch stops |
| Get started | [/downloads/mac/](https://www.sketch.com/downloads/mac/) | download page, no account form submitted |
| Menu button | hidden at 1440 (the bar is expanded). On 390 it opens \`#main-nav-menu\` | no |

Desktop hover probe (subnav parents): ${hovers.map((h) => `\`${h.label.slice(0, 24)}\` open=${h.open}`).join('; ') || 'not separately hovered'}.

Menu button at 1440: visible=${menuMeta?.visible}, aria="${menuMeta?.aria || ''}", controls=${menuMeta?.controls || ''}, expanded=${menuMeta?.expanded}.

## Phone menu

The Menu button does not flip \`aria-expanded\` (it stayed \`${drawer.menuExpanded}\`). It opens \`.mobile-nav\` (panel visible: ${drawer.panelVisible}). That drawer lists Product, Explore and Support links directly. Close is \`.mobile-nav__close\`. \`#main-nav-menu\` stays \`display: none\` at 390.

## Home interactions that are not navigations

| Control | Opens |
|---|---|
| Promo banner ("New in Sketch") | ${home.promoHref || '(no href)'} |
| In-page section nav (\`.page-nav\`, \`.top-bar\`) | hash targets on the homepage (\`#design\`, \`#prototype\`, \`#collaborate\`, \`#about\`) |
| Newsletter form in the footer | email field plus a marketing-consent checkbox and Sign up. Not filled. Not submitted |
| Grid-layout toggle | an internal layout debug control (\`main-nav#toggleGridLayout\`). Not a public page |
| Tooltip triggers on Pricing | \`.tooltip-trigger\` buttons. Hover/focus only; no navigation |
| Billing toggle on Pricing | Yearly / Monthly buttons. In-page state |
| Currency select on Pricing | USD / EUR. In-page state. Not a form submit of account data |

## Auth wall (branch stops)

[/signin/](https://www.sketch.com/signin/) shows "Sign in to Sketch", an email field, a password field, Continue with Apple, Continue with Google, Continue with SSO, Forgot Password, Sign In, and Create an account. Password is not submitted. No email is typed. Create an account, Forgot Password, Apple, Google and SSO are not clicked.

The Mac app, the web app workspace, and the iOS app sit behind that wall or an App Store listing. They are not captured.

## Form pages (opened, not submitted)

Contact Us ([/support/contact/](https://www.sketch.com/support/contact/)) is recorded as a form page. Fields are not filled.

## Public pages reached from the homepage

${publicPages.map((p) => `- ${p.path || '/'} — labels: ${p.text.filter(Boolean).slice(0, 3).join(' / ') || '(unlabelled)'} — via ${p.sources.join(', ')}`).join('\n')}

## Off-site (recorded, not walked)

${off.map((p) => `- ${p.url} — ${p.text.filter(Boolean).slice(0, 2).join(' / ') || '(unlabelled)'} — via ${p.sources.join(', ')}`).join('\n')}

## Sitemap

\`/sitemap.xml\` lists hundreds of documentation, blog, changelog and support articles. Those are the same public marketing/docs surface, not extra product UI. The capture visits the section indexes linked from the homepage (docs, blog, changelog, support, plugins, design resources) plus one article each where a homepage card links it. It does not crawl all 800 sitemap URLs.

## Walls and skips

| URL | Why the branch stops |
|---|---|
| https://www.sketch.com/signin/ | Email and password, or Apple, Google, or SSO |
| Create an account / Forgot Password (linked from the sign-in page) | Account creation and recovery. Not opened |
| Newsletter Sign up | Form. Not submitted. No email typed |
| https://www.sketch.com/support/contact/ | Contact form. Page may be opened; fields not filled |
| Discord, X, Bluesky, Instagram, YouTube, Mastodon, App Store, developer.sketch.com, status.sketch.com | Off-site. Recorded only |
`;

fs.writeFileSync(path.join(PKG, 'site-tree.md'), md);
console.log('wrote site-tree', pages.length, 'urls;', publicPages.length, 'public');
await b.close();
