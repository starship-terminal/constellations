// Measures Fourthwall public controls in the states a signed-out visitor can
// reach. Never types into a field, never submits, never clicks SSO.
//
//   PLAYWRIGHT=... node tools/capture/public/measure-states.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const PROPS = ['color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderRadius', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'boxShadow', 'textDecorationLine', 'opacity', 'outlineWidth', 'outlineColor', 'outlineOffset'];

function styleOf(s, rect) {
  const out = { rect: { w: Math.round(rect.width), h: Math.round(rect.height), x: Math.round(rect.x), y: Math.round(rect.y) } };
  for (const p of PROPS) out[p] = s[p];
  return out;
}

async function markVisible(page, selector, attr) {
  return page.evaluate(({ selector, attr }) => {
    const els = [...document.querySelectorAll(selector)].filter((el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 2 && r.height > 2 && s.visibility !== 'hidden' && s.display !== 'none';
    });
    if (!els.length) return 0;
    els[0].setAttribute(attr, '1');
    return els.length;
  }, { selector, attr });
}

async function read(page, selector) {
  return page.evaluate(({ selector, PROPS }) => {
    const el = document.querySelector(selector);
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const out = { text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80), rect: { w: Math.round(r.width), h: Math.round(r.height) } };
    for (const p of PROPS) out[p] = s[p];
    return out;
  }, { selector, PROPS });
}

async function crop(page, selector, file) {
  const loc = page.locator(selector).first();
  if (!await loc.count()) return false;
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return false;
  const pad = 8;
  await page.screenshot({
    path: file,
    clip: {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(box.width + pad * 2, 1440),
      height: Math.min(box.height + pad * 2, 700),
    },
  });
  return true;
}

async function states(page, name, selector, { hover = true, focus = true, press = true } = {}) {
  const out = {};
  const loc = page.locator(selector).first();
  if (!await loc.count()) { log('miss', name, selector); return out; }
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(150);
  out.default = await read(page, selector);
  if (out.default) await crop(page, selector, path.join(CROPS, `${name}-default.png`));
  if (hover) {
    await loc.hover().catch(() => {});
    await page.waitForTimeout(180);
    out.hover = await read(page, selector);
    await crop(page, selector, path.join(CROPS, `${name}-hover.png`));
    await page.mouse.move(8, 8);
  }
  if (focus) {
    await loc.focus().catch(() => {});
    await page.waitForTimeout(120);
    out['focus-visible'] = await read(page, selector);
    await crop(page, selector, path.join(CROPS, `${name}-focus-visible.png`));
  }
  if (press) {
    await page.evaluate((selector) => {
      const el = document.querySelector(selector);
      if (!el) return;
      el.classList.add('is-pressed');
    }, selector);
    const box = await loc.boundingBox();
    if (box) {
      await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
      await page.mouse.down();
      await page.waitForTimeout(80);
      out.pressed = await read(page, selector);
      await crop(page, selector, path.join(CROPS, `${name}-pressed.png`));
      await page.mouse.up();
    }
  }
  log('measured', name, Object.keys(out).join(','));
  return out;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
await context.route(/onetrust|cookielaw|cookiebot/i, (route) => route.abort());
const page = await context.newPage();
const components = {};

await page.goto('https://fourthwall.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1600);
await page.mouse.move(8, 860);
await page.waitForTimeout(300);
const nBtn = await markVisible(page, 'a.btn-primary', 'data-fw-btn');
const nLogin = await markVisible(page, 'a.nav-login', 'data-fw-login');
const nNav = await markVisible(page, 'a.nav-link', 'data-fw-nav');
const nFoot = await markVisible(page, 'footer a', 'data-fw-foot');
log('visible', { nBtn, nLogin, nNav, nFoot });
components.button = await states(page, 'button', '[data-fw-btn="1"]', { press: false });
components.loginLink = await states(page, 'login-link', '[data-fw-login="1"]', { press: false });
components.navLink = await states(page, 'nav-link', '[data-fw-nav="1"]', { press: false });
components.footerLink = await states(page, 'footer-link', '[data-fw-foot="1"]', { press: false });
components.heading = { default: await read(page, 'h1') };
if (components.heading.default) await crop(page, 'h1', path.join(CROPS, 'heading-default.png'));
components.body = { default: await read(page, 'p') };
components.nav = { default: await read(page, '.nav-bar') };
if (components.nav.default) await crop(page, '.nav-bar', path.join(CROPS, 'nav-default.png'));
components.footer = { default: await read(page, 'footer') };

await page.mouse.move(8, 860);
await page.locator('[data-fw-nav="1"]').hover({ timeout: 8000 });
await page.waitForTimeout(400);
components.menu = { default: await read(page, '.nav-dropdown') };
components.menuLink = await states(page, 'menu-link', '.mega-link', { press: false });
await page.screenshot({ path: path.join(CROPS, 'menu-default.png'), clip: { x: 0, y: 0, width: 1440, height: 640 } });

await page.goto('https://fourthwall.com/contact', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(1400);
const fieldSel = await page.evaluate(() => {
  const el = document.querySelector('input[type="text"], input[type="email"], input:not([type="hidden"]), textarea');
  if (!el) return null;
  if (el.id) return `#${CSS.escape(el.id)}`;
  if (el.name) return `${el.tagName.toLowerCase()}[name="${el.name}"]`;
  return el.tagName.toLowerCase();
});
log('contact field', fieldSel);
if (fieldSel) {
  components.textField = await states(page, 'text-field', fieldSel, { hover: true, focus: true, press: false });
}
const faqBtn = await page.evaluate(() => document.querySelector('button, summary') ? true : false);

await page.goto('https://fourthwall.com/faq', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(1200);
const acc = await page.evaluate(() => {
  const el = document.querySelector('summary, button[aria-expanded], .faq-question, [class*="accordion"]');
  if (!el) return null;
  el.setAttribute('data-fw-acc', '1');
  return true;
});
if (acc) {
  components.accordion = await states(page, 'accordion', '[data-fw-acc="1"]', { press: false });
  await page.locator('[data-fw-acc="1"]').click().catch(() => {});
  await page.waitForTimeout(400);
  components.accordion.open = await read(page, '[data-fw-acc="1"]');
  await crop(page, '[data-fw-acc="1"]', path.join(CROPS, 'accordion-open.png'));
}

await page.goto('https://fourthwall.com/search', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(1200);
const searchSel = await page.evaluate(() => {
  const el = document.querySelector('input[type="search"], input[placeholder], input[type="text"]');
  if (!el) return null;
  el.setAttribute('data-fw-search', '1');
  return '[data-fw-search="1"]';
});
if (searchSel) components.searchField = await states(page, 'search-field', searchSel, { press: false });

// Auth wall: open, photograph empty form, do not type or click SSO.
await page.goto('https://fourthwall.com/get-started', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(1800);
const auth = {
  finalHost: new URL(page.url()).hostname,
  finalPath: new URL(page.url()).pathname,
  title: await page.title(),
  fields: await page.evaluate(() => [...document.querySelectorAll('input, button, a')].slice(0, 30).map((el) => ({
    tag: el.tagName,
    type: el.getAttribute('type'),
    name: el.getAttribute('name'),
    id: el.id,
    text: (el.getAttribute('aria-label') || el.innerText || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
  }))),
};
components.authWall = { default: { text: auth.title, fields: auth.fields.map((f) => f.text).filter(Boolean).slice(0, 12) } };
await page.screenshot({ path: path.join(CROPS, 'auth-wall-default.png') });
log('auth', auth.finalHost, auth.finalPath, auth.fields.length);

const out = {
  _meta: {
    product: 'Fourthwall',
    signed_in: false,
    capturedAt: new Date().toISOString(),
    source: 'live fourthwall.com, signed out, desktop 1440, deviceScaleFactor 2',
    note: 'No field was typed into. No form was submitted. No SSO control was clicked.',
  },
  components,
  auth,
};
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2) + '\n');
log('wrote', Object.keys(components).length, 'components');
await browser.close();
