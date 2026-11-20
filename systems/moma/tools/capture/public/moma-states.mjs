// Second pass: membership marketing URL, menu, search, login button states,
// element crops. Headed Chrome. Stops on a Cloudflare challenge. Writes raw/login-states.json
// (raw/states.json is moma-membership.mjs's). Presses nothing that submits.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'moma', 'raw-shots');
const CROPS = path.join(PKG, 'components', 'crops');
const READ = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const browser = await chromium.launch({ channel: 'chrome', headless: false });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  locale: 'en-US',
});
const page = await context.newPage();
const log = (...a) => console.log(...a);

async function guard() {
  const title = await page.title();
  const text = await page.evaluate(() => (document.body.innerText || '').slice(0, 300));
  if (/just a moment|attention required|checking your browser/i.test(title)) {
    console.error('STOP Cloudflare', title);
    await browser.close();
    process.exit(3);   // nothing is written before the first guard passes, and the write is last
  }
  return { title, text: text.slice(0, 180) };
}

async function shot(name, source) {
  await screenshotWithMetadata(page, { path: `${RAW}/${name}.png` }, {
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 2,
    sanitizedSourceUrl: source,
  });
  log('shot', name);
}

async function hideCookie() {
  await page.addStyleTag({
    content: '[class*="cookie" i], [id*="cookie" i], [class*="consent" i], [class*="klaviyo"], div[class*="needsclick"] { display:none !important; }',
  }).catch(() => {});
}

await page.goto('https://www.moma.org/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2000);
await guard();
await hideCookie();

// Open the header's Membership menu only: a <button> that declares a popup or an expanded state.
// The old lookup clicked the first button or link whose text matched /membership/, which could
// be a link that navigates away.
const memberHref = await page.evaluate(() => {
  const btn = [...document.querySelectorAll('button[aria-expanded], button[aria-haspopup]')]
    .find((el) => /membership/i.test((el.innerText || el.getAttribute('aria-label') || '').trim()) && el.getBoundingClientRect().width > 40);
  if (btn) btn.click();
  return btn ? 'menu-button' : null;
});
log('membership control', memberHref);
await page.waitForTimeout(700);
const menuLinks = await page.evaluate(() => {
  return [...document.querySelectorAll('a')].filter((a) => {
    const r = a.getBoundingClientRect();
    return r.width > 40 && r.top > 40 && r.top < 500 && /member|join|support|benefit/i.test(a.textContent || '');
  }).map((a) => ({ href: a.getAttribute('href'), text: (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60) }));
});
log('menu links', JSON.stringify(menuLinks));
await shot('home-light-membership-menu', 'https://www.moma.org/');

const membershipPath = (menuLinks.find((l) => /member/i.test(l.href || '') && !/donate/i.test(l.href || '')) || {}).href;
log('chosen membership', membershipPath);

// search
// Close the menu with Escape. A blind click at (10, 700) used to land on whatever sat there.
await page.keyboard.press('Escape').catch(() => {});
await page.waitForTimeout(300);
const searchBtn = page.locator('button[aria-label*="Search" i], a[aria-label*="Search" i], button:has(svg)').filter({ hasText: '' });
const opened = await page.evaluate(() => {
  const btns = [...document.querySelectorAll('button, a')];
  const s = btns.find((b) => /search/i.test(b.getAttribute('aria-label') || '') && b.getBoundingClientRect().width > 8);
  if (s) { s.click(); return s.getAttribute('aria-label'); }
  return null;
});
log('search click', opened);
await page.waitForTimeout(600);
await shot('home-light-search', 'https://www.moma.org/');
const searchField = await page.evaluate(() => {
  const el = document.querySelector('input[type="search"], input[name*="search" i], input[placeholder*="Search" i], [role="search"] input');
  if (!el) return null;
  const s = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  return { placeholder: el.placeholder, w: Math.round(r.width), h: Math.round(r.height), fontSize: s.fontSize, border: s.borderBottom, color: s.color, bg: s.backgroundColor };
});
log('search field', JSON.stringify(searchField));

// login states
await page.goto('https://www.moma.org/auth/login', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1800);
await guard();
const loginStyles = await page.evaluate(() => {
  function read(el) {
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      text: (el.innerText || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 40),
      fontSize: s.fontSize, fontWeight: s.fontWeight, fontFamily: s.fontFamily,
      color: s.color, bg: s.backgroundColor, border: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
      radius: s.borderRadius, pad: s.padding, shadow: s.boxShadow,
      box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      cls: (el.className || '').toString().slice(0, 80),
    };
  }
  const cont = [...document.querySelectorAll('button')].find((b) => /continue/i.test(b.textContent || ''));
  const email = document.querySelector('input[type="email"], input.moma-input-field, input');
  const card = document.querySelector('form, .moma-card, [class*="card"]') || document.querySelector('main');
  return { continue: read(cont), email: read(email), card: read(card) };
});
log('login styles', JSON.stringify(loginStyles));

async function crop(name, box) {
  if (!box || box.w < 4) { log('skip crop', name); return; }
  const pad = 8;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(1440 - Math.max(0, box.x - pad), box.w + pad * 2),
    height: Math.min(900 - Math.max(0, box.y - pad), box.h + pad * 2),
  };
  await screenshotWithMetadata(page, {
    path: `${CROPS}/${name}.png`,
    clip,
    scale: 'css',
  }, {
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 2,
    sanitizedSourceUrl: 'https://www.moma.org/auth/login',
  });
  log('crop', name, clip.width, clip.height);
}

await crop('login-email-default', loginStyles.email && loginStyles.email.box);
await crop('login-continue-default', loginStyles.continue && loginStyles.continue.box);
const cont = page.getByRole('button', { name: 'Continue' });
if (await cont.count()) {
  await cont.hover();
  await page.waitForTimeout(250);
  const hover = await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((el) => /continue/i.test(el.textContent || ''));
    const s = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    return { bg: s.backgroundColor, color: s.color, box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
  });
  log('continue hover', JSON.stringify(hover));
  await crop('login-continue-hover', hover.box);
  await cont.focus();
  await page.waitForTimeout(200);
  const focus = await page.evaluate(() => {
    const b = document.activeElement;
    const s = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    return { outline: s.outline, boxShadow: s.boxShadow, bg: s.backgroundColor, box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
  });
  log('continue focus', JSON.stringify(focus));
  await crop('login-continue-focus-visible', focus.box);
}

// The empty Continue submit is gone: pressing Continue submits the login form, which the
// capture rules forbid even when empty. The validation state is not captured.

// raw/states.json belongs to moma-membership.mjs; this pass writes its own file.
fs.writeFileSync(path.join(READ, 'login-states.json'), JSON.stringify({
  membershipPath, menuLinks, searchField, loginStyles, capturedAt: new Date().toISOString(),
}, null, 2));

if (membershipPath && membershipPath.startsWith('/')) {
  await page.goto('https://www.moma.org' + membershipPath, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(2200);
  const g = await guard();
  log('membership page', page.url(), g.title);
  await hideCookie();
  await shot('membership-light-default', 'https://www.moma.org' + membershipPath);
  const h1 = await page.evaluate(() => {
    const el = document.querySelector('h1');
    if (!el) return null;
    const s = getComputedStyle(el);
    return { text: el.innerText.slice(0, 80), fontSize: s.fontSize, fontWeight: s.fontWeight, color: s.color };
  });
  log('membership h1', JSON.stringify(h1));
}

await browser.close();
log('states done');
