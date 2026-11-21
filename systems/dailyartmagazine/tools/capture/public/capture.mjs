// Public capture for DailyArt Magazine.
//
//   RAW=~/.design-systems/dailyartmagazine/raw-shots \
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//   node capture.mjs
//
// Photographs the public magazine, records every visible control and the page
// it opens, and writes computed styles. Shop and Courses are external stores:
// their links are recorded and never followed. Newsletter and contact fields
// are never filled. No form is submitted. No identity provider is clicked.
import fs from 'node:fs';
import path from 'node:path';
import { chromium } from '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs';
import { screenshotWithMetadata } from '../screenshot.mjs';

const BASE = 'https://www.dailyartmagazine.com';
const RAW = process.env.RAW || path.join(process.env.HOME, '.design-systems/dailyartmagazine/raw-shots');
const PKG = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..', '..');
const OUT = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });
fs.mkdirSync(path.join(PKG, 'screenshots'), { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const EXTERNAL = /shop\.dailyartmagazine\.com|courses\.dailyartmagazine\.com|paypal\.com|facebook\.com|twitter\.com|instagram\.com|x\.com|utm\.guru|ads\.freestar|linkedin\.com|google\.com|apple\.com/i;

function sameSite(href) {
  try {
    const u = new URL(href, BASE);
    return u.hostname === 'www.dailyartmagazine.com' || u.hostname === 'dailyartmagazine.com';
  } catch { return false; }
}

async function hideAds(page) {
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('.fs-close-button, [id*="freestar"], [class*="freestar"], iframe')) {
      if (el.tagName === 'IFRAME' || /ad|freestar/i.test(el.id + ' ' + el.className)) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}

async function shot(page, name, requested) {
  const file = path.join(RAW, name + '.png');
  await hideAds(page);
  await screenshotWithMetadata(page, { path: file }, { ...requested, sanitizedSourceUrl: new URL(page.url()).origin + new URL(page.url()).pathname });
  log('shot', name);
}

function pageEval() {
  const clip = (s, n = 160) => (s || '').replace(/\s+/g, ' ').trim().slice(0, n);
  const controls = [...document.querySelectorAll('a, button, input, select, textarea, summary, [role="button"]')].map((el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    const visible = r.width > 1 && r.height > 1 && cs.visibility !== 'hidden' && cs.display !== 'none' && Number(cs.opacity) > 0;
    return {
      tag: el.tagName.toLowerCase(),
      type: el.getAttribute('type') || '',
      text: clip(el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || el.getAttribute('title') || '', 100),
      href: el.href || el.getAttribute('href') || '',
      id: el.id || '',
      cls: (typeof el.className === 'string' ? el.className : '').slice(0, 90),
      name: el.getAttribute('name') || '',
      visible,
      inHeader: !!el.closest('#top-header, .fixed-nav, header'),
      inFooter: !!el.closest('footer, #colophon, .site-footer'),
    };
  });
  const h1 = clip([...document.querySelectorAll('h1')].map((h) => h.innerText).join(' | '), 180);
  const forms = [...document.querySelectorAll('form')].map((f) => ({
    id: f.id,
    cls: (typeof f.className === 'string' ? f.className : '').slice(0, 80),
    action: f.getAttribute('action') || '',
    fields: [...f.querySelectorAll('input, textarea, select, button')].map((i) => ({
      tag: i.tagName.toLowerCase(),
      type: i.type || '',
      name: i.name || '',
      placeholder: i.placeholder || '',
    })),
  }));
  return {
    title: document.title,
    h1,
    bodyClass: document.body.className.slice(0, 240),
    passwordFields: document.querySelectorAll('input[type="password"]').length,
    controls,
    forms,
    themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
  };
}

const PAGES = [
  ['home', '/'],
  ['latest', '/latest/'],
  ['category-movements', '/category/art-movements/'],
  ['category-painting', '/category/art-forms/painting/'],
  ['article', '/siena-art-of-bronze-frick/'],
  ['author', '/author/zstanska/'],
  ['about', '/about-dailyart-magazine/'],
  ['team', '/dailyart-team/'],
  ['contribute', '/send-an-article/'],
  ['advertise', '/advertisement/'],
  ['contact', '/contact/'],
  ['quizzes', '/quizzes/'],
  ['search', '/?s=monet'],
  ['login', '/login'],
  ['cookie', '/cookie-policy/'],
  ['privacy', '/privacy-policy/'],
  ['terms', '/terms-of-service/'],
  ['newsletter-terms', '/newsletter-terms-and-conditions/'],
  ['trending', '/trending/'],
  ['long-reads', '/long-reads/'],
];

const browser = await chromium.launch({ headless: true });
const tree = { capturedAt: new Date().toISOString(), base: BASE, pages: {}, externalNotFollowed: [], interactions: [] };
const readings = { capturedAt: tree.capturedAt, pages: {} };

async function visit(context, key, urlPath, { mobile = false, prefix = '' } = {}) {
  const page = await context.newPage();
  page.setDefaultTimeout(12000);
  const full = urlPath.startsWith('http') ? urlPath : BASE + urlPath;
  log('open', key, full);
  const resp = await page.goto(full, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch((e) => {
    log('FAIL goto', key, e.message.split('\n')[0]);
    return null;
  });
  await page.waitForTimeout(2200);
  await hideAds(page);
  const info = await page.evaluate(pageEval).catch(() => null);
  const name = `${prefix}${key}-light-default`;
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  await shot(page, name, { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr });
  if (info) {
    tree.pages[prefix + key] = {
      url: new URL(page.url()).origin + new URL(page.url()).pathname + (new URL(page.url()).search ? new URL(page.url()).search.replace(/[?&](utm_[^=&]+|fbclid|gclid)=[^&]*/g, '') : ''),
      status: resp ? resp.status() : null,
      title: info.title,
      h1: info.h1,
      passwordFields: info.passwordFields,
      forms: info.forms.map((f) => ({ id: f.id, cls: f.cls, fieldTypes: f.fields.map((x) => x.type || x.tag) })),
      controls: info.controls.filter((c) => c.visible).map((c) => ({
        tag: c.tag, type: c.type, text: c.text, href: c.href, id: c.id, cls: c.cls, inHeader: c.inHeader, inFooter: c.inFooter,
      })),
    };
  }
  return page;
}

// Desktop walk
{
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    userAgent: UA,
    locale: 'en-US',
  });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });

  const home = await visit(context, 'home', '/');
  // hamburger opens the category drawer
  await home.locator('#hamburger').click({ timeout: 5000 }).catch((e) => log('hamburger', e.message.split('\n')[0]));
  await home.waitForTimeout(700);
  await shot(home, 'home-light-menu-open', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  const menuText = await home.evaluate(() => {
    const nav = document.querySelector('.fixed-nav.navigation.open, .fixed-nav.open, nav.fixed-nav');
    if (!nav) return { open: false };
    const items = [...nav.querySelectorAll('a')].map((a) => ({
      text: (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      href: a.href,
    }));
    return { open: /open/.test(nav.className), cls: nav.className, count: items.length, items };
  });
  tree.interactions.push({ control: '#hamburger', opens: 'nav.fixed-nav.navigation (class open)', itemCount: menuText.count, items: menuText.items });
  // close menu by clicking hamburger again if it toggles
  await home.locator('#hamburger').click({ timeout: 3000 }).catch(() => {});
  await home.waitForTimeout(400);

  // donate modal: open, photograph, close. Do not follow PayPal.
  await home.locator('.donate.open-modal, .open-modal').first().click({ timeout: 5000 }).catch((e) => log('donate', e.message.split('\n')[0]));
  await home.waitForTimeout(600);
  const donate = await home.evaluate(() => {
    const m = document.querySelector('.modal-r');
    if (!m) return null;
    return {
      cls: m.className,
      shown: /show/.test(m.className) || getComputedStyle(m).display !== 'none',
      text: (m.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 400),
      links: [...m.querySelectorAll('a')].map((a) => ({ text: (a.innerText || '').trim(), href: a.href })),
    };
  });
  if (donate && donate.shown) {
    await shot(home, 'home-light-donate-modal', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    tree.interactions.push({
      control: 'button.donate.open-modal',
      opens: 'div.modal-r.modal-r--show',
      text: donate.text,
      linksRecordedNotFollowed: donate.links.map((l) => l.href),
    });
    for (const l of donate.links) tree.externalNotFollowed.push({ from: 'donate modal', text: l.text, href: l.href, reason: 'PayPal donation checkout; not followed' });
  }
  await home.locator('.modal-close-r').first().click({ timeout: 3000 }).catch(() => {});
  await home.keyboard.press('Escape').catch(() => {});

  // search: the visible Search control. Record the field; type a query via URL only (already a planned page), do not submit a filled form from a click that might post.
  const searchPage = await visit(context, 'search', '/?s=monet');

  // load more on home is an in-page control; click once and record, it fetches more cards, not a form submit.
  await home.bringToFront();
  await home.evaluate(() => window.scrollTo(0, document.body.scrollHeight * 0.35));
  const loadMore = home.locator('button.load-more-arts').first();
  if (await loadMore.count()) {
    await loadMore.scrollIntoViewIfNeeded().catch(() => {});
    const before = await home.locator('article, .art-item, .post').count().catch(() => 0);
    await loadMore.click({ timeout: 5000 }).catch((e) => log('load more', e.message.split('\n')[0]));
    await home.waitForTimeout(1500);
    const after = await home.locator('article, .art-item, .post').count().catch(() => 0);
    tree.interactions.push({ control: 'button.load-more-arts', opens: 'more cards on the same page', before, after });
    await shot(home, 'home-light-load-more', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  }

  await home.close();
  await searchPage.close().catch(() => {});

  for (const [key, urlPath] of PAGES) {
    if (key === 'home' || key === 'search') continue;
    const p = await visit(context, key, urlPath);
    await p.close();
  }

  // hover a primary button and a nav link for state readings
  const statePage = await context.newPage();
  await statePage.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await statePage.waitForTimeout(1500);
  await hideAds(statePage);
  const btn = statePage.locator('a.primary, button.primary, .primary.btn').filter({ hasText: /browse more|search|subscribe/i }).first();
  // measure via evaluate after hover of a visible primary link
  const hoverTarget = statePage.locator('#top-header a').filter({ hasText: 'Stories' }).first();
  await hoverTarget.hover().catch(() => {});
  await statePage.waitForTimeout(400);
  await shot(statePage, 'home-light-nav-hover', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  tree.interactions.push({ control: 'header link Stories (hover)', opens: 'https://www.dailyartmagazine.com/latest/ on click; hover is a colour state only' });
  await statePage.close();

  await context.close();
}

// Phone width: home, menu, article, login
{
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: UA_MOBILE,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
  });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  for (const [key, urlPath] of [['home', '/'], ['article', '/siena-art-of-bronze-frick/'], ['login', '/login'], ['contact', '/contact/']]) {
    const p = await visit(context, key, urlPath, { mobile: true, prefix: 'mobile-' });
    if (key === 'home') {
      await p.locator('#hamburger').click({ timeout: 5000 }).catch(() => {});
      await p.waitForTimeout(700);
      await shot(p, 'mobile-home-light-menu-open', { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
      tree.interactions.push({ control: '#hamburger at 390', opens: 'nav.fixed-nav.navigation.open (same drawer as desktop)' });
    }
    await p.close();
  }
  await context.close();
}

// Computed styles of named components on home + article + contact + login
{
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    userAgent: UA,
    locale: 'en-US',
  });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const page = await context.newPage();
  const measure = async (label, url, extra) => {
    await page.goto(BASE + url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await page.waitForTimeout(1800);
    await hideAds(page);
    if (extra) await extra(page);
    const data = await page.evaluate(() => {
      const pick = (sel) => {
        const el = document.querySelector(sel);
        if (!el) return null;
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        if (r.width < 1 && r.height < 1) return { missing: 'zero box', sel };
        return {
          sel,
          text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60),
          rect: { w: Math.round(r.width), h: Math.round(r.height) },
          color: cs.color,
          backgroundColor: cs.backgroundColor,
          borderTopColor: cs.borderTopColor,
          borderTopWidth: cs.borderTopWidth,
          borderRadius: cs.borderRadius,
          fontFamily: cs.fontFamily,
          fontSize: cs.fontSize,
          fontWeight: cs.fontWeight,
          lineHeight: cs.lineHeight,
          letterSpacing: cs.letterSpacing,
          textTransform: cs.textTransform,
          padding: `${cs.paddingTop} ${cs.paddingRight} ${cs.paddingBottom} ${cs.paddingLeft}`,
          boxShadow: cs.boxShadow,
          textDecorationLine: cs.textDecorationLine,
        };
      };
      const sels = {
        page: 'body',
        header: '#top-header',
        logo: 'a.logo',
        navLink: '#primary-top-menu a',
        hamburger: '#hamburger',
        searchButton: 'button.primary.btn',
        primaryButton: 'button.primary.btn.long, a.btn, .primary.btn.long',
        cardTitle: 'h2 a, h3 a, .post-title a, article h2',
        h1: 'h1',
        bodyLink: '.entry-content a, article a, .post-content a',
        footer: 'footer',
        footerLink: 'footer a',
        newsletterField: 'input.email-newsletter',
        newsletterButton: 'button.newsletter-send',
        donateButton: 'button.donate, .donate.btn',
        checkbox: 'input[type="checkbox"]',
      };
      const out = {};
      for (const [k, sel] of Object.entries(sels)) out[k] = pick(sel);
      const root = getComputedStyle(document.documentElement);
      const vars = {};
      for (const sheet of document.styleSheets) {
        let rules;
        try { rules = sheet.cssRules; } catch { continue; }
        const walk = (rs) => {
          for (const rule of rs) {
            if (rule.style) {
              for (const name of rule.style) {
                if (name.startsWith('--') && !name.startsWith('--wp--')) vars[name] = rule.style.getPropertyValue(name).trim();
              }
            }
            if (rule.cssRules) walk(rule.cssRules);
          }
        };
        if (rules) walk(rules);
      }
      return {
        out,
        themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
        vars,
        fonts: [...document.fonts].slice(0, 20).map((f) => f.family + ' ' + f.weight + ' ' + f.status),
      };
    });
    readings.pages[label] = data;
    log('measured', label);
  };
  await measure('home', '/');
  await measure('home-menu', '/', async (p) => {
    await p.locator('#hamburger').click().catch(() => {});
    await p.waitForTimeout(500);
  });
  await measure('article', '/siena-art-of-bronze-frick/');
  await measure('contact', '/contact/');
  await measure('login', '/login');
  await measure('search', '/?s=monet');
  await page.close();
  await context.close();
}

// brand evidence
{
  const context = await browser.newContext({ userAgent: UA });
  const page = await context.newPage();
  await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  readings.brand = await page.evaluate(() => ({
    themeColor: [...document.querySelectorAll('meta[name="theme-color"]')].map((m) => ({ content: m.content, media: m.media || null })),
    maskIcon: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
    icons: [...document.querySelectorAll('link[rel*="icon"]')].map((l) => ({ rel: l.rel, href: l.href, sizes: l.sizes?.toString?.() || '' })),
    manifest: document.querySelector('link[rel="manifest"]')?.href || null,
  }));
  await context.close();
}

await browser.close();

fs.writeFileSync(path.join(OUT, 'site-tree.json'), JSON.stringify(tree, null, 2));
fs.writeFileSync(path.join(OUT, 'readings.json'), JSON.stringify(readings, null, 2));
log('wrote', path.join(OUT, 'site-tree.json'));
log('pages', Object.keys(tree.pages).length, 'interactions', tree.interactions.length);
