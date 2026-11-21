// 2026-11-21 public refresh. Headed Chrome only.
// Photographs public pages, menus, the store listing, an empty search, and
// the login wall. Does not type, submit, follow identity providers, buy
// tickets, donate, or enter checkout.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/moma/tools/capture/public/moma-refresh.mjs

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
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(READ, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function assertNotChallenge(title, text) {
  const blob = `${title}\n${(text || '').slice(0, 500)}`;
  if (/just a moment|cf-browser-verification|attention required|checking your browser|verify you are human/i.test(blob) && !/Museum of Modern Art|MoMA/i.test(title)) {
    const e = new Error('STOP: challenge page');
    e.code = 3;
    e.detail = { title, text: (text || '').slice(0, 180) };
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
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 160);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 300);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name, source) {
    this.requested.sanitizedSourceUrl = source;
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name, source) {
    await lazyScroll(this.p);
    const H = await this.p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 6 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    this.requested.sanitizedSourceUrl = source;
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

async function goto(page, url) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await wait(page, 2200);
  const title = await page.title();
  const text = await page.evaluate(() => (document.body && document.body.innerText || '').slice(0, 700));
  assertNotChallenge(title, text);
  const status = res ? res.status() : null;
  log('  goto', status, title.slice(0, 80), page.url().split('?')[0]);
  return { title, text, status, href: page.url() };
}

async function harvestVars(page) {
  return page.evaluate(() => {
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
      if (v) resolved[n] = v.slice(0, 200);
    }
    const sheets = [...document.querySelectorAll('link[rel=stylesheet]')].map((l) => l.href).filter((h) => /sol\.|main\./.test(h));
    return {
      title: document.title,
      colorScheme: root.colorScheme,
      sheets,
      viewport: {
        innerWidth, innerHeight, devicePixelRatio,
        visualViewport: visualViewport && { width: visualViewport.width, height: visualViewport.height, scale: visualViewport.scale },
      },
      resolved,
    };
  });
}

async function measure(page, pageName) {
  return page.evaluate((pageName) => {
    const props = ['fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'color', 'backgroundColor', 'borderTopWidth', 'borderTopColor', 'borderRadius', 'padding', 'boxShadow', 'outline'];
    function read(el) {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if (r.width < 4 || r.height < 4) return null;
      const o = {
        text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 70),
        className: String(el.className || '').replace(/\s+/g, ' ').trim().slice(0, 140),
        tag: el.tagName,
        box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      };
      for (const p of props) o[p] = s[p];
      return o;
    }
    function labeled(text) {
      return [...document.querySelectorAll('a, button')].find((el) => (el.innerText || '').replace(/\s+/g, ' ').trim() === text && el.getBoundingClientRect().width > 16 && el.getBoundingClientRect().top < innerHeight);
    }
    return {
      page: pageName,
      path: location.pathname,
      components: {
        h1: read(document.querySelector('h1')),
        tickets: read(labeled('Tickets')),
        donate: read(labeled('Donate')),
        visit: read(labeled('Visit')),
        store: read(labeled('Store')),
        header: read(document.querySelector('header')),
        footer: read(document.querySelector('footer')),
        search: read(document.querySelector('input[name=query], input[type=search]')),
      },
    };
  }, pageName);
}

const browser = await chromium.launch({
  channel: 'chrome',
  headless: false,
  args: ['--disable-blink-features=AutomationControlled'],
});

const tree = { capturedAt: new Date().toISOString(), pages: {} };
const readings = { capturedAt: tree.capturedAt, pages: {}, components: {} };

async function desktop() {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    userAgent: UA,
    locale: 'en-US',
  });
  const page = await context.newPage();
  const S = () => new Shooter(page, 'home-light', 1440, 900, 1);

  const home = await goto(page, 'https://www.moma.org/');
  tree.pages.home = { title: home.title, status: home.status };
  const shooter = new Shooter(page, 'home-light', 1440, 900, 1);
  await shooter.view('cookie', 'https://www.moma.org/');
  await hideCookie(page);
  await wait(page, 300);
  await shooter.view('default', 'https://www.moma.org/');
  await shooter.full('full', 'https://www.moma.org/');

  readings.pages.home = await harvestVars(page);
  readings.components.home = await measure(page, 'home');

  const visitBtn = page.getByRole('button', { name: 'Visit', exact: true }).first();
  await visitBtn.hover();
  await wait(page, 500);
  await shooter.view('nav-hover', 'https://www.moma.org/');
  await visitBtn.click();
  await wait(page, 500);
  await shooter.view('visit-menu', 'https://www.moma.org/');
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.move(8, 8);
  await wait(page, 200);

  const exBtn = page.getByRole('button', { name: 'Exhibitions and events', exact: true }).first();
  await exBtn.click();
  await wait(page, 500);
  await shooter.view('exhibitions-menu', 'https://www.moma.org/');
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.move(8, 8);

  const artBtn = page.getByRole('button', { name: 'Art and artists', exact: true }).first();
  await artBtn.click();
  await wait(page, 500);
  await shooter.view('art-menu', 'https://www.moma.org/');
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.move(8, 8);

  const searchBtn = page.getByRole('button', { name: 'Search', exact: true }).first();
  await searchBtn.click();
  await wait(page, 400);
  await shooter.view('search', 'https://www.moma.org/');
  await page.keyboard.press('Escape').catch(() => {});
  await page.mouse.move(8, 8);

  const memBtn = page.getByRole('button', { name: 'Membership', exact: true }).first();
  await memBtn.click();
  await wait(page, 400);
  await shooter.view('membership-menu', 'https://www.moma.org/');
  await page.keyboard.press('Escape').catch(() => {});

  const pages = [
    ['visit', 'https://www.moma.org/visit/'],
    ['exhibitions', 'https://www.moma.org/calendar/exhibitions'],
    ['exhibition', 'https://www.moma.org/calendar/exhibitions/5910'],
    ['collection', 'https://www.moma.org/collection/'],
    ['calendar', 'https://www.moma.org/calendar'],
  ];
  for (const [key, url] of pages) {
    const info = await goto(page, url);
    await hideCookie(page);
    tree.pages[key] = { title: info.title, status: info.status, href: info.href.split('?')[0] };
    const sh = new Shooter(page, `${key}-light`, 1440, 900, 1);
    await sh.view('default', url);
    await sh.full('full', url);
    readings.pages[key] = await harvestVars(page);
    readings.components[key] = await measure(page, key);
  }

  const storeHome = await goto(page, 'https://store.moma.org/');
  await hideCookie(page);
  tree.pages.store = { title: storeHome.title, status: storeHome.status, href: page.url().split('?')[0] };
  const store = new Shooter(page, 'store-light', 1440, 900, 1);
  await store.view('default', 'https://store.moma.org/');
  await store.full('full', 'https://store.moma.org/');

  const listing = await goto(page, 'https://store.moma.org/collections/new');
  await hideCookie(page);
  tree.pages.storeListing = { title: listing.title, status: listing.status, href: page.url().split('?')[0] };
  const list = new Shooter(page, 'store-listing-light', 1440, 900, 1);
  await list.view('default', 'https://store.moma.org/collections/new');
  await list.full('full', 'https://store.moma.org/collections/new');

  const empty = await goto(page, 'https://store.moma.org/search?q=zzzznotaproduct999');
  tree.pages.storeEmpty = { title: empty.title, status: empty.status };
  const emptyShot = new Shooter(page, 'store-search-empty-light', 1440, 900, 1);
  await emptyShot.view('default', 'https://store.moma.org/search?q=zzzznotaproduct999');

  const members = await goto(page, 'https://www.moma.org/members/');
  tree.pages.members404 = { title: members.title, status: members.status, text: members.text.slice(0, 160) };
  if (members.status === 404 || /not found|oof/i.test(members.title + members.text)) {
    const miss = new Shooter(page, 'members-missing-light', 1440, 900, 1);
    await miss.view('default', 'https://www.moma.org/members/');
  }

  // Login wall. Photograph only. Do not type, do not press Continue.
  const login = await goto(page, 'https://www.moma.org/auth/login');
  tree.pages.login = {
    title: login.title,
    status: login.status,
    host: new URL(page.url()).host,
    path: new URL(page.url()).pathname,
    stopped: 'login wall photographed empty; nothing typed; Continue not pressed',
  };
  const loginShot = new Shooter(page, 'login-light', 1440, 900, 1);
  await loginShot.view('default', 'https://www.moma.org/auth/login');
  await loginShot.full('full', 'https://www.moma.org/auth/login');
  const email = page.locator('input[type="email"]').first();
  if (await email.count()) {
    await email.focus();
    await wait(page, 250);
    await loginShot.view('email-focus', 'https://www.moma.org/auth/login');
  }

  await context.close();
}

async function phone() {
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: UA_MOBILE,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
  });
  const page = await context.newPage();
  const home = await goto(page, 'https://www.moma.org/');
  await hideCookie(page);
  tree.pages.mobileHome = { title: home.title, vw: await page.evaluate(() => ({ w: innerWidth, h: innerHeight, dpr: devicePixelRatio })) };
  const sh = new Shooter(page, 'mobile-home-light', 390, 844, 2);
  await sh.view('default', 'https://www.moma.org/');
  await sh.full('full', 'https://www.moma.org/');
  const trigger = page.locator('[data-mobile-menu-trigger]').first();
  if (await trigger.count()) {
    await trigger.click();
    await wait(page, 500);
    await sh.view('menu', 'https://www.moma.org/');
  }

  const visit = await goto(page, 'https://www.moma.org/visit/');
  await hideCookie(page);
  tree.pages.mobileVisit = { title: visit.title };
  const vs = new Shooter(page, 'mobile-visit-light', 390, 844, 2);
  await vs.view('default', 'https://www.moma.org/visit/');

  const ex = await goto(page, 'https://www.moma.org/calendar/exhibitions');
  await hideCookie(page);
  const es = new Shooter(page, 'mobile-exhibitions-light', 390, 844, 2);
  await es.view('default', 'https://www.moma.org/calendar/exhibitions');

  await context.close();
}

try {
  await desktop();
  await phone();
} catch (e) {
  log('FAILED', e.message, e.detail || '');
  if (e.code === 3) process.exitCode = 3;
  else throw e;
} finally {
  fs.writeFileSync(path.join(READ, 'refresh-2026-11-21.json'), JSON.stringify({ tree, readings: { pages: Object.keys(readings.pages), components: readings.components } }, null, 2));
  fs.writeFileSync(path.join(READ, 'capture-readings.json'), JSON.stringify(readings, null, 2));
  log('wrote readings');
  await browser.close();
}
