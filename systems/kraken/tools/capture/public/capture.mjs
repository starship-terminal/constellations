// Public Kraken capture: site tree, screenshots, component styles.
// Hides the cookie banner. Never accepts consent, never types a credential,
// never clicks Google, Apple, passkey, or submits a form.
//
//   PLAYWRIGHT=<index.mjs> node tools/capture/public/capture.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'kraken', 'raw-shots');
const OUT = path.join(os.homedir(), '.design-systems', 'kraken', 'probe');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });
fs.mkdirSync(path.join(PKG, 'raw'), { recursive: true });

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

function absUrl(href) {
  try { return new URL(href, BASE); } catch { return null; }
}

const BLOCKED = (u) => {
  const h = u.hostname;
  const p = u.pathname;
  if (/accounts\.google|appleid\.apple|facebook\.com\/|login\.microsoft|id\.kraken\.com/.test(h + u.href)) return 'identity';
  if (/instagram|linkedin|youtube|tiktok|reddit|x\.com|twitter/.test(h)) return 'social';
  if (p.startsWith('/sign-in') || p.startsWith('/sign-up')) return 'auth-wall';
  return null;
};

async function shot(page, name) {
  const file = path.join(RAW, name + '.png');
  await page.screenshot({ path: file });
  const box = page.viewportSize();
  const meta = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    vv: window.visualViewport && {
      width: window.visualViewport.width,
      height: window.visualViewport.height,
      scale: window.visualViewport.scale,
    },
  }));
  fs.writeFileSync(file + '.capture.json', JSON.stringify({
    capturedAt: new Date().toISOString(),
    requested: box,
    ...meta,
    url: page.url().split('?')[0],
  }, null, 2));
  log('shot', name);
}

async function controls(page) {
  return page.evaluate(() => {
    const txt = (el) => (el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') || el.getAttribute('placeholder') || '')
      .replace(/\s+/g, ' ').trim().slice(0, 160);
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 2 && r.height > 2 && s.visibility !== 'hidden' && s.display !== 'none' && r.bottom > 0 && r.top < window.innerHeight;
    };
    return [...document.querySelectorAll('a, button, [role="button"], [role="tab"], summary, input, select')].filter(vis).map((el) => ({
      tag: el.tagName,
      role: el.getAttribute('role'),
      text: txt(el),
      href: el.getAttribute('href'),
      type: el.getAttribute('type'),
      expanded: el.getAttribute('aria-expanded'),
      haspopup: el.getAttribute('aria-haspopup'),
      placeholder: el.getAttribute('placeholder'),
    }));
  });
}

const tree = { start: BASE + '/', capturedAt: new Date().toISOString(), signed_in: false, pages: {}, homepageControls: [] };

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
page.setDefaultTimeout(20000);

await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);
await hideConsent(page);
await shot(page, 'home-light-default');
tree.homepageControls = await controls(page);

async function openNav(name) {
  const loc = page.locator('a, button, [role="button"], div').filter({ hasText: new RegExp('^' + name + '$') }).first();
  await loc.hover();
  await page.waitForTimeout(600);
  if (!(await page.locator('[aria-expanded="true"]').count())) {
    await loc.click({ force: true }).catch(() => {});
    await page.waitForTimeout(600);
  }
  const links = await page.evaluate(() => [...document.querySelectorAll('a[href]')].filter((a) => {
    const r = a.getBoundingClientRect();
    return r.width > 2 && r.height > 2 && r.top > 36 && r.top < 820;
  }).map((a) => ({
    text: (a.innerText || a.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 140),
    href: a.getAttribute('href'),
  })));
  await shot(page, 'home-light-menu-' + name.toLowerCase());
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.move(720, 700);
  await page.waitForTimeout(250);
  return links;
}

tree.menus = {};
for (const name of ['Kraken', 'Pro', 'Wallet', 'Prime', 'Markets', 'About']) {
  try { tree.menus[name] = await openNav(name); log('menu', name, tree.menus[name].length); }
  catch (e) { tree.menus[name] = [{ error: String(e.message).split('\n')[0] }]; log('menu fail', name); }
}

try {
  await page.getByRole('button', { name: 'Search', exact: true }).first().click();
  await page.waitForTimeout(700);
  await shot(page, 'home-light-search');
  tree.search = await page.evaluate(() => {
    const input = [...document.querySelectorAll('input')].find((el) => /trade|search/i.test(el.placeholder || ''));
    const items = [...document.querySelectorAll('a[href]')].filter((a) => {
      const r = a.getBoundingClientRect();
      return r.top > 40 && r.top < 800 && r.width > 2;
    }).slice(0, 20).map((a) => ({ text: (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80), href: a.getAttribute('href') }));
    return { placeholder: input ? input.placeholder : null, items };
  });
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);
} catch (e) { tree.search = { error: String(e.message).split('\n')[0] }; }

try {
  await page.getByRole('button', { name: 'EN', exact: true }).click();
  await page.waitForTimeout(700);
  await shot(page, 'home-light-language');
  tree.language = await page.evaluate(() => [...document.querySelectorAll('a, button, [role="option"], [role="menuitem"]')].filter((el) => {
    const r = el.getBoundingClientRect();
    return r.width > 2 && r.top > 40 && r.top < 800;
  }).slice(0, 40).map((el) => (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60)).filter(Boolean));
  await page.keyboard.press('Escape');
} catch (e) { tree.language = { error: String(e.message).split('\n')[0] }; }

// In-page links, including those below the fold.
await page.evaluate(() => scrollTo(0, document.body.scrollHeight));
await page.waitForTimeout(600);
await page.evaluate(() => scrollTo(0, 0));
const homeLinks = await page.evaluate(() => [...document.querySelectorAll('a[href]')].map((a) => ({
  text: (a.innerText || a.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 100),
  href: a.getAttribute('href'),
})));
tree.homeLinks = homeLinks;

const seeds = new Map();
function addSeed(href, via) {
  const u = absUrl(href);
  if (!u) return;
  if (!/kraken\.com$/.test(u.hostname) && u.hostname !== 'www.kraken.com') {
    // record off-site destination but do not crawl it here
    return;
  }
  if (u.hostname !== 'www.kraken.com') return;
  const key = u.pathname.replace(/\/$/, '') || '/';
  if (!seeds.has(key)) seeds.set(key, { path: key, via });
}
addSeed('/', 'start');
for (const row of homeLinks) addSeed(row.href, 'home');
for (const rows of Object.values(tree.menus)) {
  if (Array.isArray(rows)) for (const row of rows) addSeed(row.href, 'menu');
}

const paths = [...seeds.keys()].filter((p) => !p.startsWith('/sign-in') && !p.startsWith('/sign-up')).slice(0, 48);
log('crawl', paths.length, 'paths');

for (const pth of paths) {
  try {
    const resp = await page.goto(BASE + pth, { waitUntil: 'domcontentloaded', timeout: 40000 });
    await page.waitForTimeout(1200);
    await hideConsent(page);
    const info = await page.evaluate(() => {
      const txt = (el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 100);
      const vis = [...document.querySelectorAll('a, button, [role="button"]')].filter((el) => {
        const r = el.getBoundingClientRect();
        return r.width > 2 && r.height > 2 && r.top >= 0 && r.top < window.innerHeight;
      }).slice(0, 40).map((el) => ({
        tag: el.tagName,
        text: txt(el),
        href: el.getAttribute('href'),
        popup: el.getAttribute('aria-haspopup'),
      }));
      return {
        title: document.title,
        h1: document.querySelector('h1')?.innerText?.replace(/\s+/g, ' ').trim().slice(0, 160) || null,
        visible: vis,
        linkCount: document.querySelectorAll('a[href]').length,
      };
    });
    tree.pages[pth] = { status: resp && resp.status(), url: page.url().split('?')[0], ...info };
    log('page', pth, info.h1 || info.title);
  } catch (e) {
    tree.pages[pth] = { error: String(e.message).split('\n')[0] };
    log('page fail', pth);
  }
}

// Auth walls: look only. No typing.
for (const [name, url] of [['sign-in', BASE + '/sign-in'], ['sign-up', BASE + '/sign-up']]) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 40000 });
  await page.waitForTimeout(2500);
  await hideConsent(page);
  await shot(page, name + '-light-wall');
  tree.pages['/' + name] = await page.evaluate(() => ({
    url: location.href.split('?')[0],
    title: document.title,
    h1: document.querySelector('h1')?.innerText || null,
    fields: [...document.querySelectorAll('input, button')].filter((el) => {
      const r = el.getBoundingClientRect();
      return r.width > 2 && r.top < 1000;
    }).map((el) => ({
      tag: el.tagName,
      type: el.getAttribute('type'),
      placeholder: el.getAttribute('placeholder'),
      autocomplete: el.getAttribute('autocomplete'),
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
    })),
    signed_in: false,
  }));
}

// A few full-page and mobile shots of the surfaces that carry the system.
const extra = ['/', '/prices', '/features', '/pro', '/learn', '/why-kraken'];
for (const pth of extra) {
  await page.goto(BASE + pth, { waitUntil: 'domcontentloaded', timeout: 40000 });
  await page.waitForTimeout(1500);
  await hideConsent(page);
  const slug = pth === '/' ? 'home' : pth.slice(1).replace(/\//g, '-');
  await shot(page, slug + '-light-default');
}

await browser.close();

// Mobile home.
const mctx = await chromium.launch({ headless: true }).then(async (b) => {
  const context = await b.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: UA_MOBILE,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
  });
  const p = await context.newPage();
  await p.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await p.waitForTimeout(2000);
  await hideConsent(p);
  await shot(p, 'mobile-home-light-default');
  tree.mobileHome = await controls(p);
  try {
    const menu = p.getByRole('button', { name: /menu|open/i }).first();
    if (await menu.count()) {
      await menu.click();
      await p.waitForTimeout(700);
      await shot(p, 'mobile-home-light-menu');
      tree.mobileMenu = await controls(p);
    }
  } catch (e) { tree.mobileMenu = { error: String(e.message).split('\n')[0] }; }
  await b.close();
});

fs.writeFileSync(path.join(OUT, 'site-tree.json'), JSON.stringify(tree, null, 2));
fs.writeFileSync(path.join(PKG, 'raw', 'site-tree.json'), JSON.stringify({
  capturedAt: tree.capturedAt,
  signed_in: false,
  pageCount: Object.keys(tree.pages).length,
  menuKeys: Object.keys(tree.menus),
}, null, 2));
log('done', Object.keys(tree.pages).length, 'pages');
