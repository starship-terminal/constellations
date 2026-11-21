// Maps calendly.com's public tree from the homepage. Records every visible control
// and the page or overlay it opens. Never types, never submits, never clicks an
// identity provider. Cookie banners are hidden, never accepted or declined.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node map-site.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const OUT = process.env.MAP_OUT || path.join(os.homedir(), '.design-systems', 'calendly', 'map.json');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const MARKETING_PREFIXES = [
  '/', '/pricing', '/scheduling', '/ai-assistant', '/notetaker', '/contacts', '/payments',
  '/integration', '/security', '/features', '/solutions', '/learn', '/demo', '/blog',
  '/resources', '/about', '/release-notes', '/customers', '/newsroom', '/help',
  '/contact', '/contact-us', '/careers', '/legal', '/partners', '/signup', '/login',
  '/app/signup', '/app/login',
];

function hostOf(href) {
  try { return new URL(href).hostname.replace(/^www\./, ''); } catch { return ''; }
}

function pathOf(href) {
  try {
    const u = new URL(href, 'https://calendly.com');
    return u.pathname.replace(/\/$/, '') || '/';
  } catch { return ''; }
}

function sameSite(href) {
  const h = hostOf(href);
  return h === 'calendly.com' || h.endsWith('.calendly.com') || h === '';
}

function isAuthWall(href) {
  const p = pathOf(href);
  return p === '/login' || p === '/signup' || p === '/app/login' || p === '/app/signup'
    || p.startsWith('/login/') || p.startsWith('/signup/');
}

function isIdp(text, href) {
  const blob = `${text} ${href}`.toLowerCase();
  return /google|apple|facebook|microsoft|canva|linkedin|github|sso|okta|saml/.test(blob)
    && /sign|log|continue|auth|oauth|sso/.test(blob);
}

function marketingPath(href) {
  if (!sameSite(href)) return false;
  const p = pathOf(href);
  if (isAuthWall(href)) return false;
  if (p.startsWith('/event_types') || p.startsWith('/app/')) return false;
  return MARKETING_PREFIXES.some((pre) => p === pre || p.startsWith(pre + '/'));
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  userAgent: UA,
  locale: 'en-US',
});

async function hideCookies(page) {
  await page.addStyleTag({
    content: '#onetrust-consent-sdk,#onetrust-banner-sdk{display:none!important;visibility:hidden!important;}',
  }).catch(() => {});
}

function clean(s) {
  return (s || '').replace(/\s+/g, ' ').trim().slice(0, 180);
}

async function readControls(page) {
  return page.evaluate(() => {
    const clean = (s) => (s || '').replace(/\s+/g, ' ').trim().slice(0, 180);
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 2 && r.height > 2 && s.visibility !== 'hidden' && s.display !== 'none' && Number(s.opacity) > 0.05;
    };
    const region = (el) => {
      if (el.closest('#onetrust-consent-sdk')) return 'cookie-banner';
      if (el.closest('header, #site-header')) return 'header';
      if (el.closest('footer')) return 'footer';
      if (el.closest('[role="dialog"], [role="menu"], [aria-modal="true"]')) return 'overlay';
      return 'page';
    };
    const out = [];
    const seen = new Set();
    for (const el of document.querySelectorAll('a[href], button, [role="button"], summary')) {
      if (!vis(el)) continue;
      if (el.closest('#onetrust-consent-sdk')) continue;
      const text = clean(el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') || '');
      const href = el.getAttribute('href') || '';
      const key = el.tagName + '|' + text + '|' + href + '|' + region(el);
      if (seen.has(key)) continue;
      seen.add(key);
      out.push({
        tag: el.tagName,
        role: el.getAttribute('role'),
        text,
        href,
        expanded: el.getAttribute('aria-expanded'),
        haspopup: el.getAttribute('aria-haspopup'),
        region: region(el),
      });
    }
    return {
      title: document.title,
      h1: document.querySelector('h1')?.innerText?.replace(/\s+/g, ' ').trim().slice(0, 200) || '',
      url: location.href,
      controls: out,
    };
  });
}

const pages = [];
const queue = ['https://calendly.com/'];
const seen = new Set();
const authStops = [];
const external = [];
const idp = [];

while (queue.length && pages.length < 48) {
  const url = queue.shift();
  const key = pathOf(url);
  if (seen.has(key)) continue;
  seen.add(key);
  const page = await context.newPage();
  let status = 0;
  try {
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    status = resp ? resp.status() : 0;
    await page.waitForTimeout(1600);
    await hideCookies(page);
    const info = await readControls(page);
    const record = { requested: url, final: page.url(), status, title: info.title, h1: info.h1, controls: info.controls };
    pages.push(record);
    console.log(status, key, info.controls.length, 'controls');

    if (!isAuthWall(url)) {
      for (const c of info.controls) {
        if (!c.href || c.href.startsWith('#') || c.href.startsWith('mailto:') || c.href.startsWith('tel:')) continue;
        const abs = new URL(c.href, page.url()).href;
        if (isIdp(c.text, abs)) { idp.push({ from: key, text: c.text, href: abs.split('?')[0] }); continue; }
        if (isAuthWall(abs)) { authStops.push({ from: key, text: c.text, href: pathOf(abs) }); continue; }
        if (!sameSite(abs)) { external.push({ from: key, text: c.text, href: abs.split('?')[0] }); continue; }
        if (marketingPath(abs) && !seen.has(pathOf(abs)) && !queue.includes(abs.split('?')[0])) {
          queue.push(abs.split('?')[0]);
        }
      }
    }
  } catch (e) {
    pages.push({ requested: url, status: 0, error: String(e.message).split('\n')[0] });
    console.log('FAIL', key, String(e.message).split('\n')[0]);
  }
  await page.close();
}

// Header mega menus, recorded as overlays opened from the homepage.
const home = await context.newPage();
await home.goto('https://calendly.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await home.waitForTimeout(1500);
await hideCookies(home);
const menus = {};
for (const name of ['Product', 'Solutions', 'Resources']) {
  const loc = home.locator('#site-header nav').getByRole('button', { name, exact: true }).first();
  await loc.hover();
  await home.waitForTimeout(500);
  menus[name] = await home.evaluate(() => {
    const clean = (s) => (s || '').replace(/\s+/g, ' ').trim().slice(0, 160);
    return [...document.querySelectorAll('a[href]')].filter((a) => {
      const r = a.getBoundingClientRect();
      return r.top > 70 && r.top < 560 && r.width > 20 && r.height > 8;
    }).map((a) => ({ text: clean(a.innerText || a.getAttribute('aria-label')), href: a.getAttribute('href') }));
  });
  await home.keyboard.press('Escape');
  await home.mouse.move(700, 800);
  await home.waitForTimeout(200);
}
await home.close();

const tree = {
  capturedAt: new Date().toISOString(),
  origin: 'https://calendly.com/',
  note: 'Public marketing tree plus login and signup walls. Identity providers were recorded and not opened. Forms were not submitted. Cookie banner was hidden, not clicked.',
  pages,
  menus,
  authStops,
  idp: idp.filter((x, i, a) => a.findIndex((y) => y.href === x.href && y.text === x.text) === i),
  external: external.filter((x, i, a) => a.findIndex((y) => y.href === x.href) === i).slice(0, 80),
  queueLeft: queue.map(pathOf),
};
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(tree, null, 2));
console.log('wrote', OUT, 'pages', pages.length);
await browser.close();
