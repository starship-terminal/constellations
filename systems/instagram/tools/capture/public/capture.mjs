// Captures Instagram's public pages. Signed out. No form is submitted.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node capture.mjs
//
// Writes full-colour PNGs to ~/.design-systems/instagram/raw-shots and CSS
// readings to systems/instagram/raw/. Login, signup, Facebook, Google, Apple,
// password reset, and Meta Verified are recorded as walls and not entered.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW_SHOTS = process.env.RAW || path.join(os.homedir(), '.design-systems', 'instagram', 'raw-shots');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW_SHOTS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const BASE = 'https://www.instagram.com';

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function safeUrl(url) {
  try {
    const u = new URL(url);
    if (u.hostname !== 'www.instagram.com' && u.hostname !== 'instagram.com') return u.origin + u.pathname;
    u.search = '';
    return u.origin + u.pathname;
  } catch {
    return null;
  }
}

async function dismissSignup(page) {
  await page.keyboard.press('Escape').catch(() => {});
  await wait(page, 300);
  const left = await page.evaluate(() => {
    let n = 0;
    for (const d of document.querySelectorAll('[role="dialog"]')) {
      const t = d.innerText || '';
      if (/Sign up|Log in|never miss a post|See photos|See their followers/i.test(t)) {
        let node = d;
        while (node.parentElement && node.parentElement !== document.body) node = node.parentElement;
        node.style.setProperty('display', 'none', 'important');
        n++;
      }
    }
    return n;
  });
  return left;
}

async function lazyScroll(page) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await page.evaluate((yy) => scrollTo(0, yy), y);
    await wait(page, 180);
  }
  await page.evaluate(() => scrollTo(0, 0));
  await wait(page, 400);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.page = page;
    this.prefix = prefix;
    this.vw = vw;
    this.vh = vh;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    const file = `${RAW_SHOTS}/${this.prefix}-${name}.png`;
    this.requested.sanitizedSourceUrl = safeUrl(this.page.url());
    await screenshotWithMetadata(this.page, { path: file }, this.requested);
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    await lazyScroll(this.page);
    const H = await this.page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = `${RAW_SHOTS}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW_SHOTS).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW_SHOTS}/${old}`);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    this.requested.sanitizedSourceUrl = safeUrl(this.page.url());
    if (hCap <= chunk) await screenshotWithMetadata(this.page, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(this.page, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await this.page.evaluate(() => scrollTo(0, 0));
  }
}

async function open(page, url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await wait(page, 2200);
  return { status: resp && resp.status(), url: safeUrl(page.url()) };
}

const pages = [
  { id: 'login', url: BASE + '/' },
  { id: 'login-named', url: BASE + '/accounts/login/' },
  { id: 'locations', url: BASE + '/explore/locations/' },
  { id: 'locations-country', url: BASE + '/explore/locations/US/united-states/' },
  { id: 'popular', url: BASE + '/popular/' },
  { id: 'lite', url: BASE + '/web/lite/' },
  { id: 'profile', url: BASE + '/instagram/' },
  { id: 'missing', url: BASE + '/directory/profiles/' },
];

async function readVars(page) {
  return page.evaluate(() => {
    const names = new Set();
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        for (const r of list) {
          if (r.style) for (const name of r.style) if (name.startsWith('--')) names.add(name);
          if (r.cssRules) walk(r.cssRules);
        }
      };
      if (rules) walk(rules);
    }
    const cs = getComputedStyle(document.documentElement);
    const out = {};
    for (const n of [...names].sort()) {
      if (n.startsWith('--ig-') || n.startsWith('--igds-') || n.startsWith('--fds-duration') || n.startsWith('--font-') || n.startsWith('--glimmer') || n.startsWith('--story-swap')) {
        const v = cs.getPropertyValue(n).trim();
        if (v) out[n] = v;
      }
    }
    return {
      className: document.documentElement.className,
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      bodyBg: getComputedStyle(document.body).backgroundColor,
      bodyColor: getComputedStyle(document.body).color,
      vars: out,
    };
  });
}

async function measure(page) {
  return page.evaluate(() => {
    function pick(sel) {
      const el = document.querySelector(sel);
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        selector: sel,
        text: (el.getAttribute('aria-label') || el.innerText || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 60),
        box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
        backgroundColor: s.backgroundColor,
        color: s.color,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        borderRadius: s.borderRadius,
        border: s.borderTopWidth + ' ' + s.borderTopStyle + ' ' + s.borderTopColor,
        padding: s.padding,
        height: s.height,
      };
    }
    return {
      username: pick('input[name="email"], input[aria-label*="Mobile"]'),
      loginButton: pick('[role="button"]'),
      forgot: pick('a[href*="password/reset"]'),
      fieldShell: pick('form input[type="text"], form input[name="email"]'),
    };
  });
}

const arg = (process.argv[2] || '').split(',').filter(Boolean);
const themes = ['light', 'dark'];
const widths = [
  { id: '', width: 1440, height: 900, dpr: 1, mobile: false },
  { id: 'mobile-', width: 390, height: 844, dpr: 2, mobile: true },
];

const evidence = { capturedAt: new Date().toISOString(), pages: [], vars: {} };

for (const theme of themes) {
  for (const width of widths) {
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({
      viewport: { width: width.width, height: width.height },
      deviceScaleFactor: width.dpr,
      colorScheme: theme,
      userAgent: width.mobile ? UA_MOBILE : UA,
      isMobile: width.mobile,
      hasTouch: width.mobile,
      locale: 'en-US',
    });
    const page = await context.newPage();
    const prefixBase = `${width.id}${theme}`;
    for (const spec of pages) {
      const key = `${prefixBase}-${spec.id}`;
      if (arg.length && !arg.includes(key) && !arg.includes(spec.id)) continue;
      log('open', key, spec.url);
      try {
        const landed = await open(page, spec.url);
        if (spec.id === 'profile' || spec.id === 'popular') await dismissSignup(page);
        const shooter = new Shooter(page, `${width.id}${spec.id}-${theme}`, width.width, width.height, width.dpr);
        await shooter.view('default');
        if (['locations', 'locations-country', 'popular', 'profile', 'lite', 'login'].includes(spec.id)) {
          await shooter.full('full');
        }
        if (spec.id === 'login' && theme === 'light' && !width.mobile) {
          const input = page.locator('input[name="email"], input[aria-label*="Mobile"]').first();
          if (await input.count()) {
            await input.focus();
            await wait(page, 300);
            await shooter.view('field-focus');
          }
          const lang = page.locator('select[aria-label="Switch Display Language"]');
          if (await lang.count()) {
            await lang.focus();
            await wait(page, 200);
            await lang.evaluate((el) => { el.size = 8; });
            await wait(page, 300);
            await shooter.view('language-open');
            await lang.evaluate((el) => { el.size = 1; });
          }
          evidence.vars.light = await readVars(page);
          evidence.loginMeasure = { light: await measure(page) };
        }
        if (spec.id === 'login' && theme === 'dark' && !width.mobile) {
          evidence.vars.dark = await readVars(page);
          evidence.loginMeasure.dark = await measure(page);
        }
        if (spec.id === 'profile' && !width.mobile) {
          const reels = page.locator('svg[aria-label="Reels"]').first();
          if (await reels.count()) {
            await reels.click({ force: true }).catch(() => {});
            await wait(page, 900);
            await dismissSignup(page);
            await shooter.view('reels-tab');
          }
          const more = page.getByRole('button', { name: /and \d+ more/ });
          if (await more.count()) {
            await more.first().click({ force: true }).catch(() => {});
            await wait(page, 600);
            await shooter.view('bio-expanded');
          }
        }
        if (spec.id === 'popular' && !width.mobile) {
          const next = page.getByRole('button', { name: 'Next' });
          if (await next.count()) {
            await next.first().click().catch(() => {});
            await wait(page, 700);
            await shooter.view('next');
          }
        }
        evidence.pages.push({ id: spec.id, theme, width: width.width, height: width.height, dpr: width.dpr, ...landed });
      } catch (e) {
        log('  FAILED', key, String(e.message).split('\n')[0]);
        evidence.pages.push({ id: spec.id, theme, width: width.width, error: String(e.message).split('\n')[0] });
      }
    }
    await browser.close();
  }
}

fs.writeFileSync(path.join(RAW, 'capture.json'), JSON.stringify(evidence, null, 2));
log('wrote raw/capture.json', evidence.pages.length, 'rows');
