// Public Fable capture. Headless Chromium, signed out. Hides the Osano consent
// banner (never clicks Accept / Save Preferences). Does not type, submit, or
// click Google, Apple, or any store checkout.
//
//   PLAYWRIGHT=... node systems/fable/tools/capture/public/shoot.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'fable', 'raw-shots');
const READ = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(READ, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const BASE = 'https://fable.co';
const log = (...a) => console.log(...a);

const HIDE = `
  .osano-cm-window, .osano-cm-dialog, .osano-cm-info-dialog, .osano-cm-widget,
  #hs-beacon, .BeaconContainer, .hsds-beacon, iframe[title*="Help"], iframe[id*="beacon"] {
    display: none !important; visibility: hidden !important; pointer-events: none !important;
  }
`;

async function prep(page) {
  await page.addStyleTag({ content: HIDE }).catch(() => {});
  await page.evaluate(() => {
    document.querySelectorAll('.osano-cm-window, .osano-cm-dialog, .osano-cm-info-dialog, .BeaconContainer, .hsds-beacon').forEach((el) => el.remove());
  }).catch(() => {});
}

async function open(page, url) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(2200);
  await prep(page);
  await page.waitForTimeout(300);
  return res && res.status();
}

async function shot(page, name, requested) {
  await screenshotWithMetadata(page, { path: path.join(RAW, name + '.png') }, { ...requested, sanitizedSourceUrl: null });
  log('  shot', name);
}

async function full(page, name, requested) {
  const dpr = requested.deviceScaleFactor;
  const vw = requested.viewport.width;
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y < h; y += 700) {
      scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 120));
    }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(400);
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const chunk = Math.floor(14000 / dpr);
  const MAXH = 8 * chunk;
  const hCap = Math.min(H, MAXH);
  if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
  const prefix = path.join(RAW, name);
  for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(name + '.part'))) fs.unlinkSync(path.join(RAW, old));
  if (hCap <= chunk) {
    await screenshotWithMetadata(page, { path: prefix + '.png', fullPage: true }, { ...requested, sanitizedSourceUrl: null });
  } else {
    for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(page, {
        path: `${prefix}.part${i}.png`,
        fullPage: true,
        clip: { x: 0, y, width: vw, height: Math.min(chunk, hCap - y) },
      }, { ...requested, sanitizedSourceUrl: null });
    }
  }
  log('  full', name, 'H=' + H);
  await page.evaluate(() => scrollTo(0, 0));
}

function rgb(c) {
  const m = String(c).match(/rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:[,\s/]+([\d.]+))?/);
  if (!m) return c;
  const a = m[4] == null ? 1 : +m[4];
  if (a >= 1) return '#' + [m[1], m[2], m[3]].map((n) => (+n).toString(16).padStart(2, '0')).join('');
  return `rgba(${m[1]}, ${m[2]}, ${m[3]}, ${a})`;
}

async function styleOf(locator) {
  return locator.evaluate((el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName.toLowerCase(),
      text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      cls: [...el.classList].slice(0, 4).join(' '),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      color: cs.color,
      backgroundColor: cs.backgroundColor,
      fontFamily: cs.fontFamily,
      fontSize: cs.fontSize,
      fontWeight: cs.fontWeight,
      lineHeight: cs.lineHeight,
      letterSpacing: cs.letterSpacing,
      borderRadius: cs.borderRadius,
      boxShadow: cs.boxShadow,
      borderTopWidth: cs.borderTopWidth,
      borderTopStyle: cs.borderTopStyle,
      borderTopColor: cs.borderTopColor,
      paddingTop: cs.paddingTop,
      paddingRight: cs.paddingRight,
      paddingBottom: cs.paddingBottom,
      paddingLeft: cs.paddingLeft,
      outlineWidth: cs.outlineWidth,
      outlineStyle: cs.outlineStyle,
      outlineColor: cs.outlineColor,
      textDecorationLine: cs.textDecorationLine,
    };
  });
}

const computed = [];
async function record(name, state, locator, pageUrl) {
  const n = await locator.count();
  if (!n) {
    computed.push({ name, state, miss: true, page: pageUrl });
    log('  miss', name, state);
    return null;
  }
  const loc = locator.first();
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await loc.page().waitForTimeout(150);
  const s = await styleOf(loc);
  computed.push({ name, state, page: pageUrl, ...s });
  log('  read', name, state, s.fontSize, rgb(s.color), rgb(s.backgroundColor));
  return loc;
}

async function crop(locator, file) {
  const dir = path.join(PKG, 'components', 'crops');
  fs.mkdirSync(dir, { recursive: true });
  await locator.screenshot({ path: path.join(dir, file) });
}

const browser = await chromium.launch({ headless: true });
const desktopReq = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
const mobileReq = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };

const desk = await browser.newContext({
  viewport: desktopReq.viewport,
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await desk.newPage();

const viewportMeta = await (async () => {
  await open(page, BASE + '/');
  return page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    devicePixelRatio: window.devicePixelRatio,
    visualViewport: window.visualViewport && {
      width: window.visualViewport.width,
      height: window.visualViewport.height,
      scale: window.visualViewport.scale,
    },
    themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
    mask: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
  }));
})();
log('viewport', JSON.stringify(viewportMeta));

await shot(page, 'home-light-default', desktopReq);
await full(page, 'home-light-full', desktopReq);

await record('nav-link', 'default', page.getByRole('link', { name: 'Clubs', exact: true }), BASE + '/');
await record('signup-nav', 'default', page.getByRole('button', { name: 'Sign up or log in' }), BASE + '/');
await record('cart-button', 'default', page.getByRole('button', { name: 'Shopping cart' }), BASE + '/');
await record('hero-title', 'default', page.locator('h1').first(), BASE + '/');
const cta = await record('cta', 'default', page.getByRole('button', { name: 'Get the app' }), BASE + '/');
if (cta) await crop(cta, 'cta-default.png');
{
  const loc = page.getByRole('button', { name: 'Get the app' }).first();
  await loc.hover();
  await page.waitForTimeout(200);
  await record('cta', 'hover', loc, BASE + '/');
  await crop(loc, 'cta-hover.png');
  await loc.focus();
  await page.waitForTimeout(150);
  await record('cta', 'focus-visible', loc, BASE + '/');
  await crop(loc, 'cta-focus-visible.png');
  await page.mouse.move(0, 0);
}
await record('section-title', 'default', page.locator('h2').nth(1), BASE + '/');

// signup dialog: look only
await page.getByRole('button', { name: 'Sign up or log in' }).first().click();
await page.waitForTimeout(700);
await shot(page, 'home-light-signup', desktopReq);
const dialog = page.getByRole('dialog').first();
await record('signup-dialog', 'default', dialog, BASE + '/');
await record('signup-title', 'default', dialog.locator('h1, h2').first(), BASE + '/');
const dialogControls = await dialog.locator('button, a, input').evaluateAll((els) => els.map((el) => {
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  return {
    tag: el.tagName.toLowerCase(),
    type: el.getAttribute('type'),
    text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    href: el.getAttribute('href'),
    color: cs.color,
    backgroundColor: cs.backgroundColor,
    fontSize: cs.fontSize,
    fontWeight: cs.fontWeight,
    fontFamily: cs.fontFamily.split(',')[0],
    borderRadius: cs.borderRadius,
    h: +r.height.toFixed(1),
    w: +r.width.toFixed(1),
    borderTopWidth: cs.borderTopWidth,
    borderTopColor: cs.borderTopColor,
  };
}));
computed.push({ name: 'signup-dialog-controls', controls: dialogControls });
await page.keyboard.press('Escape');
await page.waitForTimeout(300);

// get the app dialog
await page.getByRole('button', { name: 'Get the app' }).first().click();
await page.waitForTimeout(600);
await shot(page, 'home-light-get-app', desktopReq);
const appDialog = await page.getByRole('dialog').last().evaluate((el) => {
  const links = [...el.querySelectorAll('a')].map((a) => ({ text: (a.innerText || a.getAttribute('aria-label') || '').trim().slice(0, 80), href: a.href }));
  const buttons = [...el.querySelectorAll('button')].map((b) => (b.innerText || b.getAttribute('aria-label') || '').trim().slice(0, 80));
  return { text: el.innerText.replace(/\s+/g, ' ').slice(0, 400), links, buttons, bg: getComputedStyle(el).backgroundColor, radius: getComputedStyle(el).borderRadius };
}).catch((e) => ({ error: String(e.message).split('\n')[0] }));
computed.push({ name: 'get-app-dialog', ...appDialog });
await page.keyboard.press('Escape');

// clubs
await open(page, BASE + '/clubs');
await shot(page, 'clubs-light-default', desktopReq);
await page.getByRole('button', { name: 'Search thousands of book and TV clubs' }).first().click().catch((e) => log('  search fail', e.message.split('\n')[0]));
await page.waitForTimeout(600);
await shot(page, 'clubs-light-search', desktopReq);
await record('search-field', 'default', page.locator('input[type=search], input[placeholder*="Search"]').first(), BASE + '/clubs');
await page.keyboard.press('Escape');

// books
await open(page, BASE + '/books');
await shot(page, 'books-light-default', desktopReq);
await full(page, 'books-light-full', desktopReq);

// book
await open(page, BASE + '/book/fourth-wing-by-rebecca-yarros-9781649374080');
await shot(page, 'book-light-default', desktopReq);
await record('book-title', 'default', page.locator('h1').first(), page.url());
await record('want-to-read', 'default', page.getByRole('button', { name: 'Want to read' }), page.url());
{
  const loc = page.getByRole('button', { name: 'Want to read' });
  if (await loc.count()) {
    await loc.hover();
    await page.waitForTimeout(200);
    await record('want-to-read', 'hover', loc, page.url());
  }
}

// club
await open(page, BASE + '/club/romantasy-with-sophia-altman-599083839156');
await shot(page, 'club-light-default', desktopReq);

// genre
await open(page, BASE + '/club/fantasy');
await shot(page, 'genre-light-default', desktopReq);

// blog + post
await open(page, BASE + '/blog');
await shot(page, 'blog-light-default', desktopReq);
await open(page, BASE + '/blog/how-to-start-a-book-club');
await shot(page, 'post-light-default', desktopReq);

// discover
await open(page, BASE + '/discover');
await shot(page, 'discover-light-default', desktopReq);
await page.getByRole('button', { name: 'What is this?' }).click().catch(() => {});
await page.waitForTimeout(400);
await shot(page, 'discover-light-about', desktopReq);
await page.keyboard.press('Escape');

// legal + missing login
await open(page, BASE + '/privacy');
await shot(page, 'privacy-light-default', desktopReq);
await open(page, BASE + '/login');
await shot(page, 'notfound-light-default', desktopReq);

// signin wall: photograph, do not type, do not click Google/Apple
await open(page, BASE + '/signin?next=%2Flibrary');
await shot(page, 'signin-light-default', desktopReq);
const wall = await page.evaluate(() => {
  const inputs = [...document.querySelectorAll('input')].map((i) => ({
    type: i.type, name: i.name, placeholder: i.placeholder, aria: i.getAttribute('aria-label'),
  }));
  const buttons = [...document.querySelectorAll('button, a')].map((el) => ({
    tag: el.tagName.toLowerCase(),
    text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    href: el.getAttribute('href'),
    type: el.getAttribute('type'),
  })).filter((x) => x.text);
  return { url: location.href, title: document.title, h1: document.querySelector('h1')?.innerText || '', inputs, buttons: buttons.slice(0, 20) };
});
computed.push({ name: 'signin-wall', ...wall });
await record('login-submit', 'default', page.getByRole('button', { name: 'Login with email' }), page.url());
await record('email-field', 'default', page.locator('input[type=email]'), page.url());

// help center (public)
await open(page, 'https://help.fable.co/');
await shot(page, 'help-light-default', desktopReq);

await page.close();
await desk.close();

// phone
const mob = await browser.newContext({
  viewport: mobileReq.viewport,
  deviceScaleFactor: 2,
  userAgent: UA_MOBILE,
  isMobile: true,
  hasTouch: true,
  locale: 'en-US',
});
const mp = await mob.newPage();
await open(mp, BASE + '/');
const mobileMeta = await mp.evaluate(() => ({
  innerWidth: window.innerWidth,
  innerHeight: window.innerHeight,
  devicePixelRatio: window.devicePixelRatio,
}));
log('mobile viewport', JSON.stringify(mobileMeta));
await shot(mp, 'mobile-home-light-default', mobileReq);
await full(mp, 'mobile-home-light-full', mobileReq);
// burger if present
const burger = mp.getByRole('button', { name: /menu|open/i });
if (await burger.count()) {
  await burger.first().click().catch(() => {});
  await mp.waitForTimeout(500);
  await shot(mp, 'mobile-home-light-menu', mobileReq);
}
await open(mp, BASE + '/clubs');
await shot(mp, 'mobile-clubs-light-default', mobileReq);
await open(mp, BASE + '/book/fourth-wing-by-rebecca-yarros-9781649374080');
await shot(mp, 'mobile-book-light-default', mobileReq);
await mp.close();
await mob.close();
await browser.close();

const brand = {
  capturedAt: new Date().toISOString().slice(0, 10),
  themeColor: viewportMeta.themeColor,
  maskIcon: viewportMeta.mask,
  desktop: viewportMeta,
  mobile: mobileMeta,
  consent: 'Osano banner hidden with CSS. Accept All, Reject Non-Essential, and Save Preferences were not clicked.',
};
fs.writeFileSync(path.join(READ, 'components-computed.json'), JSON.stringify({ brand, computed }, null, 2) + '\n');
fs.writeFileSync(path.join(READ, 'brand.json'), JSON.stringify(brand, null, 2) + '\n');
log('wrote readings', computed.length);
