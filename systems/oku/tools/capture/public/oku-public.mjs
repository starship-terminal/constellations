// Oku public capture. Headless Playwright only. Never types, never submits.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node oku-public.mjs
//
// Writes full-colour PNGs under RAW (default ~/.design-systems/oku/raw-shots)
// and a readings JSON the package builders consume.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'oku', 'raw-shots');
const OUT = process.env.OUT || path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1';

const BOOK = '/book/taipei-story-by-rebecca-f-kuang-16O8u';
const PROFILE = '/user/morgsdotorg';
const REVIEW = '/reviews/KLVMl/1nH4g';
const BLOG_POST = '/blog/oku-now-available-for-ios';

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function isWall(url) {
  try {
    const pathName = new URL(url).pathname;
    return pathName === '/signin' || pathName === '/join' || pathName === '/reset-password' || pathName === '/signup';
  } catch {
    return false;
  }
}

async function shot(page, file, requested) {
  await screenshotWithMetadata(page, { path: file }, requested);
  log('  shot', path.basename(file));
}

async function measure(page) {
  return page.evaluate(() => {
    const keys = ['color', 'backgroundColor', 'borderTopWidth', 'borderTopStyle', 'borderTopColor', 'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'textDecorationLine', 'outlineStyle', 'outlineWidth', 'outlineColor', 'outlineOffset', 'opacity', 'display'];
    const read = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) return null;
      const o = {
        tag: el.tagName,
        text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
        box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      };
      for (const k of keys) o[k] = s[k];
      return o;
    };
    const byText = (sel, text) => [...document.querySelectorAll(sel)].find((el) => (el.innerText || '').replace(/\s+/g, ' ').trim() === text);
    const header = [...document.querySelectorAll('div')].find((el) => {
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return s.position === 'fixed' && r.top <= 1 && r.height >= 60 && r.height <= 100 && r.width > 300;
    });
    return {
      url: location.href,
      title: document.title,
      viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
      htmlBg: getComputedStyle(document.documentElement).backgroundColor,
      bodyColor: getComputedStyle(document.body).color,
      bodyFont: getComputedStyle(document.body).fontFamily,
      bodySize: getComputedStyle(document.body).fontSize,
      h1: read(document.querySelector('h1')),
      h2: read(document.querySelector('h2')),
      navExplore: read(byText('a', 'Explore')),
      navSignIn: read([...document.querySelectorAll('a')].find((a) => (a.innerText || '').trim() === 'Sign in' && a.getBoundingClientRect().width > 2)),
      joinButton: read([...document.querySelectorAll('button')].find((b) => (b.innerText || '').trim() === 'Join' && b.getBoundingClientRect().width > 2)),
      header: read(header),
    };
  });
}

const readings = { capturedAt: new Date().toISOString(), themes: {} };

const browser = await chromium.launch({ headless: true });

async function contextFor(theme, mobile) {
  return browser.newContext({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mobile ? 2 : 1,
    isMobile: mobile,
    hasTouch: mobile,
    colorScheme: theme,
    locale: 'en-US',
    userAgent: mobile ? UA_MOBILE : UA,
  });
}

const desktopPages = [
  ['home', '/'],
  ['explore', '/explore'],
  ['blog', '/blog'],
  ['blog-post', BLOG_POST],
  ['pricing', '/pricing'],
  ['privacy', '/privacy'],
  ['terms', '/terms'],
  ['book', BOOK],
  ['profile', PROFILE],
  ['review', REVIEW],
  ['not-found', '/about'],
  ['login-missing', '/login'],
];

const mobilePages = [
  ['home', '/'],
  ['explore', '/explore'],
  ['blog', '/blog'],
  ['pricing', '/pricing'],
  ['book', BOOK],
  ['profile', PROFILE],
  ['review', REVIEW],
];

for (const theme of ['light', 'dark']) {
  readings.themes[theme] = { pages: {}, interactions: [] };
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const ctx = await contextFor(theme, false);
  for (const [name, pathName] of desktopPages) {
    const page = await ctx.newPage();
    log(theme, name);
    try {
      const resp = await page.goto('https://oku.club' + pathName, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await wait(page, 1800);
      const finalUrl = page.url();
      if (isWall(finalUrl)) {
        readings.themes[theme].interactions.push({ name, stopped: 'auth wall', url: finalUrl });
        log('  WALL', finalUrl);
        await page.close();
        continue;
      }
      await shot(page, path.join(RAW, `${name}-${theme}-default.png`), requested);
      const m = await measure(page);
      m.status = resp?.status() ?? null;
      readings.themes[theme].pages[name] = m;
    } catch (e) {
      log('  FAILED', name, String(e.message).split('\n')[0]);
      readings.themes[theme].interactions.push({ name, failed: String(e.message).split('\n')[0] });
    }
    await page.close();
  }

  // Long pages: viewport tiles, stitched later. The kit helper rejects fullPage
  // when the PNG height does not match the CSS document height at device scale.
  for (const name of ['home', 'pricing', 'book']) {
    const spec = desktopPages.find((p) => p[0] === name);
    if (!spec) continue;
    const page = await ctx.newPage();
    try {
      await page.goto('https://oku.club' + spec[1], { waitUntil: 'domcontentloaded', timeout: 45000 });
      await wait(page, 1200);
      const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
      const chunk = 900;
      const max = Math.min(H, 8 * chunk);
      log(theme, name, 'tiles H', H);
      const tiles = [];
      for (let y = 0, i = 0; y < max; y += chunk, i++) {
        await page.evaluate((yy) => window.scrollTo(0, yy), y);
        await wait(page, 250);
        const file = path.join(RAW, `${name}-${theme}-tile${i}.png`);
        await shot(page, file, requested);
        tiles.push(file);
      }
      readings.themes[theme].interactions.push({ name: name + '-tiles', height: H, captured: max, tiles: tiles.length, truncated: H > max });
      await page.evaluate(() => window.scrollTo(0, 0));
    } catch (e) {
      log('  TILE FAILED', name, String(e.message).split('\n')[0]);
    }
    await page.close();
  }

  // Join dialog, then close. Do not type.
  {
    const page = await ctx.newPage();
    await page.goto('https://oku.club/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1200);
    const join = page.locator('button').filter({ hasText: /^Join$/ });
    const count = await join.count();
    for (let i = 0; i < count; i++) {
      const box = await join.nth(i).boundingBox();
      if (box && box.width > 20) {
        await join.nth(i).click();
        break;
      }
    }
    await wait(page, 700);
    const wall = await page.evaluate(() => ({
      url: location.href,
      email: !!document.querySelector('input[type="email"]'),
      password: !!document.querySelector('input[type="password"]'),
    }));
    readings.themes[theme].interactions.push({ name: 'join-dialog', ...wall, typed: false, submitted: false });
    if (wall.email && !isWall(wall.url)) {
      await shot(page, path.join(RAW, `home-${theme}-join-dialog.png`), requested);
    }
    await page.keyboard.press('Escape');
    await page.close();
  }

  // Nav link hover + focus, and Join button hover. No navigation into a wall.
  {
    const page = await ctx.newPage();
    await page.goto('https://oku.club/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1000);
    const link = page.locator('a', { hasText: /^Explore$/ }).first();
    await link.hover();
    await wait(page, 250);
    const hover = await link.evaluate((el) => {
      const s = getComputedStyle(el);
      return { color: s.color, textDecoration: s.textDecorationLine, bg: s.backgroundColor };
    });
    await link.focus();
    await wait(page, 150);
    const focus = await link.evaluate((el) => {
      const s = getComputedStyle(el);
      return { outline: s.outline, outlineColor: s.outlineColor, outlineWidth: s.outlineWidth, outlineOffset: s.outlineOffset, boxShadow: s.boxShadow };
    });
    const join = page.locator('button').filter({ hasText: /^Join$/ }).first();
    const joinDefault = await join.evaluate((el) => {
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return { bg: s.backgroundColor, color: s.color, radius: s.borderRadius, h: Math.round(r.height), w: Math.round(r.width), size: s.fontSize, weight: s.fontWeight, pad: s.paddingTop + ' ' + s.paddingRight };
    });
    await join.hover();
    await wait(page, 200);
    const joinHover = await join.evaluate((el) => ({ bg: getComputedStyle(el).backgroundColor, color: getComputedStyle(el).color }));
    await join.focus();
    const joinFocus = await join.evaluate((el) => {
      const s = getComputedStyle(el);
      return { outline: s.outline, outlineColor: s.outlineColor, outlineWidth: s.outlineWidth, boxShadow: s.boxShadow };
    });
    readings.themes[theme].interactions.push({ name: 'nav-link-states', hover, focus, joinDefault, joinHover, joinFocus });
    await page.close();
  }

  // Pricing label click: record that prices do not change. Do not follow Subscribe.
  {
    const page = await ctx.newPage();
    await page.goto('https://oku.club/pricing', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1200);
    const prices = () => page.evaluate(() => (document.body.innerText.match(/\$\d+[^\\n]{0,24}/g) || []).slice(0, 4));
    const before = await prices();
    const yearly = page.getByText('Pay yearly', { exact: true });
    if (await yearly.count()) {
      await yearly.click();
      await wait(page, 400);
    }
    const after = await prices();
    readings.themes[theme].interactions.push({ name: 'pricing-labels', before, afterYearlyClick: after, url: page.url(), changed: JSON.stringify(before) !== JSON.stringify(after) });
    await page.close();
  }

  // Review spoiler toggle. Public, no form.
  {
    const page = await ctx.newPage();
    await page.goto('https://oku.club' + REVIEW, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1200);
    const btn = page.getByRole('button', { name: /spoilers/i });
    if (await btn.count()) {
      await btn.first().click();
      await wait(page, 400);
      if (!isWall(page.url())) await shot(page, path.join(RAW, `review-${theme}-spoiler.png`), requested);
      readings.themes[theme].interactions.push({ name: 'review-spoiler', url: page.url(), wall: isWall(page.url()) });
    }
    await page.close();
  }

  // Book status button opens the signup dialog. Do not type. Close it.
  {
    const page = await ctx.newPage();
    await page.goto('https://oku.club' + BOOK, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1200);
    const status = page.locator('button').nth(2);
    const box = await status.boundingBox();
    if (box && box.width > 20) {
      await status.click();
      await wait(page, 600);
      const wall = await page.evaluate(() => ({
        url: location.href,
        email: !!document.querySelector('input[type="email"]'),
        password: !!document.querySelector('input[type="password"]'),
      }));
      readings.themes[theme].interactions.push({ name: 'book-status', ...wall, stopped: wall.email || wall.password });
      if (wall.email && !isWall(page.url())) {
        await shot(page, path.join(RAW, `book-${theme}-signup-dialog.png`), requested);
      }
      await page.keyboard.press('Escape');
    }
    await page.close();
  }

  await ctx.close();

  // Phone width.
  const mctx = await contextFor(theme, true);
  const mreq = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };
  for (const [name, pathName] of mobilePages) {
    const page = await mctx.newPage();
    log(theme, 'mobile', name);
    try {
      await page.goto('https://oku.club' + pathName, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await wait(page, 1600);
      if (isWall(page.url())) {
        readings.themes[theme].interactions.push({ name: 'mobile-' + name, stopped: 'auth wall', url: page.url() });
        await page.close();
        continue;
      }
      await shot(page, path.join(RAW, `mobile-${name}-${theme}-default.png`), mreq);
    } catch (e) {
      log('  FAILED mobile', name, String(e.message).split('\n')[0]);
    }
    await page.close();
  }
  // Mobile menu.
  {
    const page = await mctx.newPage();
    await page.goto('https://oku.club/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1200);
    const buttons = await page.locator('button').all();
    for (const b of buttons) {
      const box = await b.boundingBox();
      if (box && box.x > 280 && box.y < 80 && box.width < 80) {
        await b.click({ force: true });
        break;
      }
    }
    await wait(page, 600);
    if (!isWall(page.url())) {
      await shot(page, path.join(RAW, `mobile-home-${theme}-menu.png`), mreq);
      readings.themes[theme].interactions.push({ name: 'mobile-menu', url: page.url() });
    }
    await page.close();
  }
  await mctx.close();
}

// Sign-in wall: record the URL and a screenshot of the wall itself, type nothing.
{
  const ctx = await contextFor('light', false);
  const page = await ctx.newPage();
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  await page.goto('https://oku.club/signin', { waitUntil: 'domcontentloaded', timeout: 40000 });
  await wait(page, 1200);
  const wall = await page.evaluate(() => ({
    url: location.href,
    title: document.title,
    email: !!document.querySelector('input[type="email"], input[type="text"]'),
    password: !!document.querySelector('input[type="password"]'),
    labels: [...document.querySelectorAll('label, button, a, h1, h2, p')].map((el) => (el.innerText || '').replace(/\s+/g, ' ').trim()).filter((t) => t && t.length < 40).slice(0, 16),
  }));
  readings.signinWall = { ...wall, typed: false, submitted: false, stopped: true };
  // Screenshot the wall so the boundary is visible. Do not include field values (fields are empty).
  await shot(page, path.join(RAW, 'signin-light-wall.png'), requested);
  await page.close();
  await ctx.close();
}

fs.writeFileSync(path.join(OUT, 'capture-readings.json'), JSON.stringify(readings, null, 2));
log('readings', path.join(OUT, 'capture-readings.json'));
log('shots', RAW);
await browser.close();
