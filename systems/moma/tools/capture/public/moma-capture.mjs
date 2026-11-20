// MoMA public signed-out capture. PRODUCT (adapt)
//
// Headed Chrome only. If the title or body looks like a Cloudflare challenge,
// this script exits immediately and does not launch another browser.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/moma/tools/capture/public/moma-capture.mjs
//
// Nothing is bought, donated, or signed into. The cookie notice is left in
// place on the first home shot, then hidden with CSS (never accepted).
// Tickets, Donate, and Log in links are measured and not followed into a
// payment or an account.

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'moma', 'raw-shots');
const READ = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(READ, { recursive: true });

const BASE = 'https://www.moma.org';
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function assertNotChallenge(title, text) {
  const blob = `${title}\n${text.slice(0, 500)}`;
  if (/just a moment|cf-browser-verification|attention required|checking your browser|cloudflare/i.test(blob) && !/Museum of Modern Art/i.test(title)) {
    console.error('STOP: Cloudflare or challenge page. Not launching another browser.');
    console.error(JSON.stringify({ title, text: text.slice(0, 200) }));
    // Throw, not exit: process.exit here skipped the finally below that saves the readings so far.
    const e = new Error('STOP: challenge page');
    e.code = 3;
    throw e;
  }
}

async function hideCookie(page) {
  await page.addStyleTag({
    content: `
      [class*="cookie"], [id*="cookie"], [class*="consent"], [class*="Cookie"],
      .kl-private-reset-css-Xuajs1, [class*="klaviyo"], iframe[src*="klaviyo"],
      div[class*="needsclick"] { display: none !important; }
    `,
  }).catch(() => {});
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 7200);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p;
    this.prefix = prefix;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: source };
    this.count = 0;
    this.dpr = dpr;
    this.vw = vw;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    await lazyScroll(this.p);
    const H = await this.p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 6 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(this.p, { path: f + '.png', fullPage: true }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(this.p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await this.p.evaluate(() => scrollTo(0, 0));
  }
}

const PROPS = [
  'fontFamily', 'fontSize', 'fontWeight', 'fontStyle', 'lineHeight', 'letterSpacing',
  'color', 'backgroundColor', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'boxShadow', 'textDecorationLine', 'outline', 'width', 'height',
];

function styleOf(el) {
  if (!el) return null;
  const s = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const out = {
    tag: el.tagName,
    text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
    className: (el.className || '').toString().replace(/\s+/g, ' ').trim().slice(0, 160),
    box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
  };
  for (const p of PROPS) out[p] = s[p];
  return out;
}

async function harvest(page, label) {
  return page.evaluate((label) => {
    const root = getComputedStyle(document.documentElement);
    const names = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        if (!list) return;
        for (const rule of list) {
          if (rule.cssRules) { walk(rule.cssRules); continue; }
          if (!rule.style) continue;
          for (let i = 0; i < rule.style.length; i++) {
            const p = rule.style[i];
            if (p.startsWith('--') && !names.includes(p)) names.push(p);
          }
        }
      };
      walk(rules);
    }
    const resolved = {};
    for (const n of names) {
      const v = root.getPropertyValue(n).trim();
      if (v) resolved[n] = v.slice(0, 240);
    }
    const fonts = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        if (!list) return;
        for (const rule of list) {
          if (rule.cssRules) { walk(rule.cssRules); continue; }
          if (rule.cssText && rule.cssText.startsWith('@font-face') && fonts.length < 40) {
            fonts.push(rule.cssText.replace(/url\([^)]+\)/g, 'url(redacted)').slice(0, 220));
          }
        }
      };
      walk(rules);
    }
    return {
      label,
      title: document.title,
      viewport: {
        innerWidth, innerHeight, devicePixelRatio,
        visualViewport: visualViewport && {
          width: visualViewport.width, height: visualViewport.height, scale: visualViewport.scale,
        },
      },
      htmlClass: document.documentElement.className.slice(0, 240),
      resolved,
      fontFaces: fonts,
      colorScheme: root.colorScheme,
    };
  }, label);
}

async function measureComponents(page, pageName) {
  return page.evaluate((pageName) => {
    const props = [
      'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
      'color', 'backgroundColor', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
      'borderRadius', 'padding', 'boxShadow', 'textDecorationLine', 'outline',
    ];
    function read(el) {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if (r.width < 4 || r.height < 4) return null;
      const o = {
        text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 70),
        className: (el.className || '').toString().replace(/\s+/g, ' ').trim().slice(0, 140),
        tag: el.tagName,
        box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      };
      for (const p of props) o[p] = s[p];
      return o;
    }
    function first(sel) {
      return [...document.querySelectorAll(sel)].find((el) => {
        const r = el.getBoundingClientRect();
        return r.width > 8 && r.height > 8 && r.bottom > 0 && r.top < innerHeight + 200;
      });
    }
    const tickets = [...document.querySelectorAll('a')].find((a) => (a.textContent || '').replace(/\s+/g, ' ').trim() === 'Tickets' && a.getBoundingClientRect().width > 20);
    const donate = [...document.querySelectorAll('a')].find((a) => (a.textContent || '').replace(/\s+/g, ' ').trim() === 'Donate' && a.getBoundingClientRect().width > 20);
    const visit = [...document.querySelectorAll('button, a')].find((a) => (a.textContent || '').replace(/\s+/g, ' ').trim() === 'Visit' && a.getBoundingClientRect().width > 20);
    const login = document.querySelector('a[href="/auth/login"], a[href*="auth/login"]');
    const subscribe = [...document.querySelectorAll('button')].find((b) => /subscribe/i.test(b.textContent || '') && b.getBoundingClientRect().width > 20);
    const email = document.querySelector('input[type="email"], input[placeholder*="mail" i], input[name*="email" i]');
    const h1 = document.querySelector('h1');
    const h2 = document.querySelector('h2');
    const card = [...document.querySelectorAll('a')].find((a) => a.querySelector('img') && a.getBoundingClientRect().width > 180);
    const footer = document.querySelector('footer');
    const header = document.querySelector('header');
    const search = document.querySelector('input[type="search"], [role="search"] input, button[aria-label*="Search" i], a[href*="search"]');
    return {
      page: pageName,
      url: location.pathname,
      components: {
        h1: read(h1),
        h2: read(h2),
        navVisit: read(visit),
        tickets: read(tickets),
        donate: read(donate),
        login: read(login),
        subscribe: read(subscribe),
        email: read(email),
        card: read(card),
        header: read(header),
        footer: read(footer),
        search: read(search),
        body: read(document.body),
      },
    };
  }, pageName);
}

const PAGES = [
  { key: 'home', path: '/' },
  { key: 'visit', path: '/visit/' },
  { key: 'exhibitions', path: '/calendar/exhibitions' },
  { key: 'exhibition', path: '/calendar/exhibitions/5910' },
  { key: 'membership', path: '/members/' },
  { key: 'calendar', path: '/calendar' },
  { key: 'collection', path: '/collection/' },
  { key: 'login', path: '/auth/login' },
];

const browser = await chromium.launch({
  channel: 'chrome',
  headless: false,
  args: ['--disable-blink-features=AutomationControlled'],
});

const readings = { pages: {}, components: {}, capturedAt: new Date().toISOString() };
let total = 0;

async function runWidth(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefix0 = mobile ? 'mobile-' : '';
  const context = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  const page = await context.newPage();
  for (const spec of PAGES) {
    if (mobile && !['home', 'visit', 'exhibitions', 'membership'].includes(spec.key)) continue;
    const name = prefix0 + spec.key;
    log('page', name, spec.path);
    try {
      const res = await page.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await wait(page, 2800);
      const title = await page.title();
      const text = await page.evaluate(() => (document.body.innerText || '').slice(0, 600));
      assertNotChallenge(title, text);
      if (res && res.status() >= 400) log('  status', res.status());
      const source = BASE + spec.path;
      const S = new Shooter(page, `${name}-light`, vw, vh, dpr, source);
      if (spec.key === 'home' && !mobile) {
        await S.view('cookie');
      }
      await hideCookie(page);
      await wait(page, 400);
      await S.view('default');
      if (!mobile || spec.key === 'home') await S.full();
      if (!mobile && spec.key === 'home') {
        const visit = page.getByRole('button', { name: 'Visit', exact: true }).first();
        if (await visit.count()) {
          await visit.hover();
          await wait(page, 500);
          await S.view('nav-hover');
          await page.mouse.move(8, 8);
        }
      }
      if (!mobile && spec.key === 'login') {
        const email = page.locator('input[type="email"], input[name="email"], input[type="text"]').first();
        if (await email.count()) {
          await email.click();
          await wait(page, 300);
          await S.view('email-focus');
        }
      }
      total += S.count;
      if (!mobile) {
        readings.pages[spec.key] = await harvest(page, spec.key);
        readings.components[spec.key] = await measureComponents(page, spec.key);
      }
    } catch (e) {
      if (String(e.message).includes('STOP') || e.code === 3) throw e;
      log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
    }
  }
  await context.close();
}

try {
  await runWidth(false);
  await runWidth(true);
} catch (e) {
  if (e.code === 3) process.exitCode = 3;
  else throw e;
} finally {
  fs.writeFileSync(path.join(READ, 'capture-readings.json'), JSON.stringify(readings, null, 2));
  log('readings', Object.keys(readings.pages).join(','));
  log('done', total, 'screenshots ->', RAW);
  await browser.close();
}
