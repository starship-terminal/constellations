// Prime Video public capture. Signed-out pages only.
// Never types into a field, never submits a form, never follows an Amazon sign-in wall.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from './screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'primevideo', 'raw-shots');
const READINGS = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(READINGS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function safeUrl(url) {
  try {
    const u = new URL(url);
    for (const k of [...u.searchParams.keys()]) {
      if (/ref|return|token|sig|session|openid|email|phone/i.test(k)) u.searchParams.delete(k);
    }
    return u.origin + u.pathname + (u.search ? u.search : '');
  } catch {
    return null;
  }
}

function isWall(url) {
  return /amazon\./i.test(url) || /\/ap\/signin/i.test(url) || /\/auth-redirect/i.test(url) || /\/signup/i.test(url) || /\/contactus/i.test(url);
}

async function shot(page, name, requested, extra = {}) {
  const file = path.join(RAW, name + '.png');
  await screenshotWithMetadata(page, { path: file, ...extra }, {
    ...requested,
    sanitizedSourceUrl: safeUrl(page.url()),
  });
  log('  shot', name, page.url().split('?')[0]);
}

async function full(page, name, requested) {
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const vw = requested.viewport.width;
  const dpr = requested.deviceScaleFactor;
  const chunk = Math.floor(14000 / dpr);
  const MAXH = 8 * chunk;
  const hCap = Math.min(H, MAXH);
  if (H > MAXH) log('  ! truncated', name, H, 'to', hCap);
  const prefix = path.join(RAW, name);
  if (hCap <= chunk) {
    await screenshotWithMetadata(page, { path: prefix + '.png', fullPage: true }, { ...requested, sanitizedSourceUrl: safeUrl(page.url()) });
  } else {
    for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(page, {
        path: `${prefix}.part${i}.png`,
        fullPage: true,
        clip: { x: 0, y, width: vw, height: Math.min(chunk, hCap - y) },
      }, { ...requested, sanitizedSourceUrl: safeUrl(page.url()) });
    }
  }
  log('  full', name, 'H=' + H);
  await page.evaluate(() => scrollTo(0, 0));
}

async function readStyles(page) {
  return page.evaluate(() => {
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 40),
        w: Math.round(r.width),
        h: Math.round(r.height),
        color: s.color,
        bg: s.backgroundColor,
        font: s.fontFamily,
        size: s.fontSize,
        weight: s.fontWeight,
        lh: s.lineHeight,
        radius: s.borderRadius,
        bw: s.borderTopWidth,
        bc: s.borderTopColor,
        pad: s.padding,
        shadow: s.boxShadow,
        ls: s.letterSpacing,
      };
    };
    const one = (sel) => pick(document.querySelector(sel));
    const byText = (tag, text) => {
      const el = [...document.querySelectorAll(tag)].find((e) => (e.innerText || '').replace(/\s+/g, ' ').trim() === text && e.getBoundingClientRect().width > 8);
      return pick(el);
    };
    const body = getComputedStyle(document.body);
    const root = getComputedStyle(document.documentElement);
    const vars = {};
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        if (!list) return;
        for (const rule of list) {
          if (rule.style) for (const name of rule.style) if (name.startsWith('--')) vars[name] = (vars[name] || 0) + 1;
          if (rule.cssRules) walk(rule.cssRules);
        }
      };
      walk(rules);
    }
    const resolved = {};
    for (const name of Object.keys(vars)) {
      const v = root.getPropertyValue(name).trim();
      if (v) resolved[name] = v.slice(0, 80);
    }
    return {
      url: location.pathname,
      title: document.title,
      inner: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
      colorScheme: root.colorScheme,
      body: { bg: body.backgroundColor, color: body.color, font: body.fontFamily, size: body.fontSize },
      varCount: Object.keys(vars).length,
      resolved,
      h1: one('h1'),
      header: one('header') || one('nav'),
      join: byText('a', 'Join Prime'),
      signin: byText('a', 'Prime Member? Sign in'),
      trial: byText('a', 'Start your 30-day free trial'),
    };
  });
}

const browser = await chromium.launch({ headless: true });

async function contextFor(mobile) {
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: UA_MOBILE, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  return context;
}

const desktopReq = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
const mobileReq = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };
const readings = { pages: {}, components: {}, walls: [], capturedAt: new Date().toISOString() };

async function gotoPublic(page, url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(page, 2500);
  if (isWall(page.url())) {
    readings.walls.push({ from: url, landed: safeUrl(page.url()), title: await page.title() });
    log('  WALL', url, '->', page.url().split('?')[0]);
    return false;
  }
  log('  open', resp && resp.status(), page.url().split('?')[0], await page.title());
  return true;
}

const desk = await contextFor(false);
const page = await desk.newPage();

const pages = [
  ['home', 'https://www.primevideo.com/'],
  ['movies', 'https://www.primevideo.com/movie'],
  ['tv', 'https://www.primevideo.com/tv'],
  ['sports', 'https://www.primevideo.com/sports'],
  ['categories', 'https://www.primevideo.com/categories'],
  ['genre-action', 'https://www.primevideo.com/genre/action'],
  ['kids', 'https://www.primevideo.com/kids'],
  ['collection', 'https://www.primevideo.com/collection/newandupcoming'],
  ['watch-anywhere', 'https://www.primevideo.com/splash/watchAnywhere'],
  ['help', 'https://www.primevideo.com/help'],
  ['legal', 'https://www.primevideo.com/help?nodeId=202064890'],
];

for (const [name, url] of pages) {
  if (!(await gotoPublic(page, url))) continue;
  readings.pages[name] = await readStyles(page);
  await shot(page, name + '-dark-default', desktopReq);
  if (['home', 'movies', 'categories', 'help', 'genre-action'].includes(name)) {
    await full(page, name + '-dark-full', desktopReq);
  }
}

// Search panel. Do not type.
if (await gotoPublic(page, 'https://www.primevideo.com/')) {
  await page.getByRole('button', { name: 'Search Prime Video' }).first().click();
  await wait(page, 700);
  const search = await page.evaluate(() => {
    const el = document.querySelector('#pv-search-nav');
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return { w: Math.round(r.width), h: Math.round(r.height), bg: s.backgroundColor, color: s.color, radius: s.borderRadius, size: s.fontSize, font: s.fontFamily, bw: s.borderTopWidth, bc: s.borderTopColor, pad: s.padding };
  });
  readings.components.searchField = search;
  await shot(page, 'home-dark-search', desktopReq);
  await page.keyboard.press('Escape');
  await wait(page, 300);
  await page.getByRole('button', { name: 'EN', exact: true }).click();
  await wait(page, 600);
  await shot(page, 'home-dark-language', desktopReq);
  await page.keyboard.press('Escape');
  await page.mouse.click(20, 500);
  await wait(page, 300);
  await page.getByRole('button', { name: 'Profile, Settings, and Account' }).click();
  await wait(page, 600);
  await shot(page, 'home-dark-account-menu', desktopReq);
  await page.keyboard.press('Escape');
}

// Title page + trailer unavailable + share dialog + details tab.
const DETAIL = 'https://www.primevideo.com/detail/0GOXEUMNGKVV4AQ0HEBYT02TD5';
if (await gotoPublic(page, DETAIL)) {
  readings.pages.detail = await readStyles(page);
  readings.components.detailActions = await page.evaluate(() => {
    return [...document.querySelectorAll('button, a')].filter((el) => {
      const r = el.getBoundingClientRect();
      return r.top > 280 && r.top < 760 && r.left < 640 && r.width > 20;
    }).slice(0, 12).map((el) => {
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.getAttribute('aria-label') || el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
        w: Math.round(r.width), h: Math.round(r.height),
        bg: s.backgroundColor, color: s.color, radius: s.borderRadius, bw: s.borderTopWidth, bc: s.borderTopColor,
        size: s.fontSize, weight: s.fontWeight, font: s.fontFamily,
      };
    });
  });
  await shot(page, 'detail-dark-default', desktopReq);
  await page.evaluate(() => scrollTo(0, 700));
  await wait(page, 600);
  await shot(page, 'detail-dark-related', desktopReq);
  await page.evaluate(() => scrollTo(0, 0));
  const details = page.getByText('Details', { exact: true }).first();
  if (await details.count()) {
    await details.click();
    await wait(page, 800);
    await shot(page, 'detail-dark-details', desktopReq);
  }
  await page.locator('button[aria-label="Share"]').click({ force: true });
  await wait(page, 800);
  readings.components.share = await page.evaluate(() => {
    const d = document.querySelector('[role="dialog"]');
    if (!d) return null;
    const s = getComputedStyle(d);
    return { text: (d.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 120), bg: s.backgroundColor, color: s.color, radius: s.borderRadius };
  });
  await shot(page, 'detail-dark-share', desktopReq);
  await page.keyboard.press('Escape');
  await wait(page, 400);
  const trailer = page.getByRole('link', { name: 'Watch trailer' });
  if (await trailer.count()) {
    await trailer.first().click();
    await wait(page, 2500);
    await shot(page, 'detail-dark-trailer-unavailable', desktopReq);
    const ok = page.getByRole('button', { name: 'OK' });
    if (await ok.count()) await ok.first().click();
    await wait(page, 500);
  }
}

// Genre chip selected.
if (await gotoPublic(page, 'https://www.primevideo.com/genre/action')) {
  const movies = page.getByRole('link', { name: 'Movies', exact: true }).or(page.getByRole('button', { name: 'Movies', exact: true }));
  // The filter chip, not the header nav. Pick the one below the title.
  const chip = page.locator('a, button').filter({ hasText: /^Movies$/ });
  const n = await chip.count();
  log('  movie chips', n);
  if (n > 1) {
    await chip.nth(1).click();
    await wait(page, 1200);
    readings.pages['genre-movies'] = { url: safeUrl(page.url()) };
    await shot(page, 'genre-action-dark-movies', desktopReq);
  }
}

// Hover and focus on Join Prime, without navigating.
if (await gotoPublic(page, 'https://www.primevideo.com/')) {
  const join = page.getByRole('link', { name: 'Join Prime' }).first();
  const box = await join.boundingBox();
  if (box) {
    await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
    await wait(page, 400);
    readings.components.joinHover = await page.evaluate(() => {
      const el = [...document.querySelectorAll('a')].find((a) => a.innerText.trim() === 'Join Prime');
      if (!el) return null;
      const s = getComputedStyle(el);
      return { bg: s.backgroundColor, color: s.color, radius: s.borderRadius, shadow: s.boxShadow };
    });
    await shot(page, 'home-dark-join-hover', desktopReq);
    await page.mouse.move(0, 0);
  }
  await join.focus();
  await wait(page, 300);
  readings.components.joinFocus = await page.evaluate(() => {
    const el = document.activeElement;
    if (!el) return null;
    const s = getComputedStyle(el);
    return { tag: el.tagName, text: (el.innerText || '').trim().slice(0, 30), outline: s.outline, shadow: s.boxShadow, bg: s.backgroundColor };
  });
  await shot(page, 'home-dark-join-focus', desktopReq);
  // Pressed via CDP, no navigation.
  const pressed = await page.evaluate(() => {
    const el = [...document.querySelectorAll('a')].find((a) => a.innerText.trim() === 'Join Prime');
    if (!el) return null;
    el.addEventListener('click', (e) => e.preventDefault(), { capture: true });
    return true;
  });
  if (pressed && box) {
    await page.mouse.move(box.x + 8, box.y + 8);
    await page.mouse.down();
    await wait(page, 150);
    readings.components.joinPressed = await page.evaluate(() => {
      const el = [...document.querySelectorAll('a')].find((a) => a.innerText.trim() === 'Join Prime');
      const s = getComputedStyle(el);
      return { bg: s.backgroundColor, color: s.color };
    });
    await shot(page, 'home-dark-join-pressed', desktopReq);
    await page.mouse.up();
  }
}

// Help article, public.
if (await gotoPublic(page, 'https://www.primevideo.com/help')) {
  const href = await page.evaluate(() => {
    const a = [...document.querySelectorAll('a')].find((el) => /nodeId=/.test(el.href) && (el.innerText || '').trim().length > 12 && !/contact/i.test(el.innerText));
    return a ? a.href : null;
  });
  if (href && !isWall(href)) {
    if (await gotoPublic(page, href)) {
      readings.pages.helpArticle = { url: safeUrl(page.url()), title: await page.title() };
      await shot(page, 'help-dark-article', desktopReq);
    }
  }
}

await desk.close();

// Phone.
const mob = await contextFor(true);
const mp = await mob.newPage();
const mobilePages = [
  ['mobile-home', 'https://www.primevideo.com/'],
  ['mobile-movies', 'https://www.primevideo.com/movie'],
  ['mobile-categories', 'https://www.primevideo.com/categories'],
  ['mobile-genre-action', 'https://www.primevideo.com/genre/action'],
  ['mobile-detail', DETAIL],
  ['mobile-help', 'https://www.primevideo.com/help'],
];
for (const [name, url] of mobilePages) {
  if (!(await gotoPublic(mp, url))) continue;
  readings.pages[name] = await readStyles(mp);
  await shot(mp, name + '-dark-default', mobileReq);
  if (name === 'mobile-home' || name === 'mobile-movies') await full(mp, name + '-dark-full', mobileReq);
}
if (await gotoPublic(mp, 'https://www.primevideo.com/')) {
  const menu = mp.locator('button').filter({ hasText: /^$/ }).first();
  const opener = mp.getByRole('button', { name: /menu|navigation|browse/i }).first();
  let opened = false;
  if (await opener.count()) {
    await opener.click();
    opened = true;
  } else {
    const buttons = mp.locator('header button, nav button');
    const count = await buttons.count();
    log('  mobile header buttons', count);
    if (count) {
      await buttons.first().click();
      opened = true;
    }
  }
  if (opened) {
    await wait(mp, 800);
    readings.components.mobileMenu = await mp.evaluate(() => {
      return [...document.querySelectorAll('a, button')].filter((el) => {
        const r = el.getBoundingClientRect();
        return r.width > 20 && r.top > 40 && r.top < 700 && getComputedStyle(el).visibility !== 'hidden';
      }).slice(0, 16).map((el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 40));
    });
    await shot(mp, 'mobile-home-dark-menu', mobileReq);
  }
}
await mob.close();
await browser.close();

fs.writeFileSync(path.join(READINGS, 'capture.json'), JSON.stringify(readings, null, 2));
log('wrote readings', Object.keys(readings.pages).length, 'pages');
