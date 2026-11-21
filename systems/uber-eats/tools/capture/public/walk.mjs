// Public signed-out walk of www.ubereats.com.
// Hides the Cloudflare challenge overlay. Does not solve it, type, or submit.
// Stops a branch when the page is an auth wall.
//
//   RAW=~/.design-systems/uber-eats/raw-shots node walk.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs');
const { chromium } = pw.default ?? pw;

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'uber-eats', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const NOTES = path.join(os.homedir(), '.design-systems', 'uber-eats', 'walk.json');

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const log = (...a) => console.log(...a);

function safeUrl(url) {
  try {
    const u = new URL(url);
    u.search = '';
    if (u.hash && u.hash.length > 40) u.hash = '';
    return u.origin + u.pathname + u.hash;
  } catch {
    return null;
  }
}

function isAuth(url) {
  try {
    const h = new URL(url).host;
    return h === 'auth.uber.com' || h.startsWith('auth.');
  } catch {
    return false;
  }
}

async function hideChallenge(page) {
  return page.evaluate(() => {
    const d = document.getElementById('cf-challenge-overlay');
    if (!d) return false;
    d.remove();
    return true;
  }).catch(() => false);
}

async function shot(page, name, requested) {
  await hideChallenge(page);
  const file = path.join(RAW, name + '.png');
  await screenshotWithMetadata(page, { path: file }, {
    ...requested,
    sanitizedSourceUrl: safeUrl(page.url()),
  });
  log('  shot', name, safeUrl(page.url()));
  return file;
}

async function readControls(page) {
  return page.evaluate(() => {
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 2 && r.height > 2 && s.display !== 'none' && s.visibility !== 'hidden' && Number(s.opacity) > 0;
    };
    const hostpath = (href) => {
      try {
        const u = new URL(href);
        return u.host + u.pathname + (u.hash || '');
      } catch {
        return null;
      }
    };
    const items = [];
    const seen = new Set();
    for (const el of document.querySelectorAll('a, button, [role="tab"], [role="button"], input, select')) {
      if (!vis(el)) continue;
      const text = (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 90);
      const href = el.href ? hostpath(el.href) : null;
      const key = (el.tagName) + '|' + text + '|' + (href || '');
      if (seen.has(key)) continue;
      seen.add(key);
      if (!text && !href) continue;
      items.push({
        tag: el.tagName,
        role: el.getAttribute('role'),
        text,
        href,
        placeholder: el.getAttribute('placeholder'),
      });
      if (items.length >= 80) break;
    }
    const body = (document.body.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 400);
    const challenge = /verify you are human|just a moment|one more step|security check/i.test(body);
    return {
      title: document.title,
      theme: document.documentElement.getAttribute('data-theme'),
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      vw: innerWidth,
      vh: innerHeight,
      challenge,
      body,
      items,
    };
  });
}

const notes = { capturedAt: new Date().toISOString(), pages: [], walls: [], interactions: [], blocked: [] };

async function openPage(context, urlPath, requested) {
  const page = await context.newPage();
  const url = urlPath.startsWith('http') ? urlPath : 'https://www.ubereats.com' + urlPath;
  let status = null;
  try {
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
    status = resp && resp.status();
    await page.waitForTimeout(2800);
  } catch (e) {
    notes.blocked.push({ url: safeUrl(url), error: String(e.message).split('\n')[0] });
    await page.close();
    return null;
  }
  const hidden = await hideChallenge(page);
  const info = await readControls(page);
  const final = safeUrl(page.url());
  const rec = { requested: urlPath, status, final, hiddenChallenge: hidden, ...info };
  if (isAuth(page.url()) || /auth\.uber\.com/.test(final || '')) {
    notes.walls.push({ from: urlPath, final, title: info.title, body: info.body.slice(0, 240), fields: info.items.filter(i => i.tag === 'INPUT' || /google|apple|facebook|continue|email|phone/i.test(i.text)).slice(0, 20) });
    notes.pages.push(rec);
    return { page, rec, wall: true };
  }
  if (info.challenge || status === 403) {
    notes.blocked.push({ url: urlPath, final, status, title: info.title, body: info.body.slice(0, 180) });
    await page.close();
    return null;
  }
  notes.pages.push(rec);
  return { page, rec, wall: false, requested };
}

async function desktop() {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    locale: 'en-US',
    userAgent: UA,
  });
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };

  // Home
  {
    const opened = await openPage(context, '/', requested);
    if (opened && !opened.wall) {
      const page = opened.page;
      await shot(page, 'home-light-default', requested);
      await page.evaluate(() => window.scrollTo(0, 900));
      await page.waitForTimeout(400);
      await shot(page, 'home-light-scrolled', requested);
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(300);

      // Address field focus. Do not type.
      await page.locator('input[name="searchTerm"]').first().click({ force: true }).catch(() => {});
      await page.waitForTimeout(500);
      await shot(page, 'home-light-address-focused', requested);
      notes.interactions.push({ control: 'address combobox', action: 'focus', typed: false, shot: 'home-light-address-focused' });
      await page.keyboard.press('Escape').catch(() => {});

      // Deliver now menu, if it is a control and not a form submit.
      const deliver = page.locator('[role="button"]').filter({ hasText: /^Deliver now$/ }).first();
      if (await deliver.count()) {
        await deliver.click({ force: true, timeout: 4000 }).catch((e) => log('  deliver miss', e.message.split('\n')[0]));
        await page.waitForTimeout(500);
        await shot(page, 'home-light-deliver-now', requested);
        notes.interactions.push({ control: 'Deliver now', action: 'click', shot: 'home-light-deliver-now' });
        await page.keyboard.press('Escape').catch(() => {});
      }

      // Nav drawer
      await page.locator('button[aria-label="Main navigation menu"]').first().click({ force: true });
      await page.waitForTimeout(700);
      await shot(page, 'home-light-nav-open', requested);
      const drawer = await page.evaluate(() => {
        const p = document.querySelector('[data-ref="panel"][aria-label="Main navigation menu"]');
        return p ? [...p.querySelectorAll('a')].map(a => ({ text: (a.innerText || '').replace(/\s+/g, ' ').trim(), href: a.href ? new URL(a.href).host + new URL(a.href).pathname : null })) : [];
      });
      notes.interactions.push({ control: 'Main navigation menu', action: 'open drawer', items: drawer, shot: 'home-light-nav-open' });
      await page.keyboard.press('Escape').catch(() => {});
      await page.waitForTimeout(300);

      // Language control in the footer. Do not follow a locale that needs a form.
      await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
      await page.waitForTimeout(400);
      const lang = page.getByText('English', { exact: true }).last();
      if (await lang.count()) {
        await lang.click({ force: true, timeout: 4000 }).catch((e) => log('  lang miss', e.message.split('\n')[0]));
        await page.waitForTimeout(600);
        await shot(page, 'home-light-language', requested);
        notes.interactions.push({ control: 'English', action: 'click', shot: 'home-light-language' });
        await page.keyboard.press('Escape').catch(() => {});
      }
      await page.close();
    } else if (opened) {
      await shot(opened.page, 'wall-auth-light-default', requested);
      await opened.page.close();
    }
  }

  const publicPaths = [
    ['/promo', 'promo'],
    ['/location', 'location'],
    ['/near-me', 'near-me'],
    ['/near-me/grocery', 'grocery'],
    ['/pickup/near-me', 'pickup'],
    ['/shopping', 'shopping'],
    ['/eats-pass', 'uber-one'],
    ['/brand/subway', 'brand'],
    ['/city/houston-tx', 'city'],
  ];
  for (const [pth, name] of publicPaths) {
    const opened = await openPage(context, pth, requested);
    if (!opened) continue;
    if (opened.wall) {
      await shot(opened.page, 'wall-' + name + '-light', requested);
      await opened.page.close();
      continue;
    }
    await shot(opened.page, name + '-light-default', requested);
    // In-page tabs if present, without submitting search.
    const tabs = opened.page.getByRole('tab');
    const tabCount = await tabs.count().catch(() => 0);
    if (tabCount > 1) {
      const label = await tabs.nth(1).innerText().catch(() => 'tab');
      await tabs.nth(1).click({ force: true, timeout: 4000 }).catch(() => {});
      await opened.page.waitForTimeout(600);
      if (!isAuth(opened.page.url())) await shot(opened.page, name + '-light-tab', requested);
      notes.interactions.push({ control: 'tab', page: pth, label: label.replace(/\s+/g, ' ').trim().slice(0, 40), shot: name + '-light-tab' });
    }
    await opened.page.close();
  }

  // Login wall: open auth URL only far enough to see the ask, then stop.
  {
    const opened = await openPage(context, 'https://auth.uber.com/v2/', requested);
    if (opened) {
      await shot(opened.page, 'login-wall-light-default', requested);
      const fields = await opened.page.evaluate(() => {
        return [...document.querySelectorAll('input, button, a')].slice(0, 30).map(el => ({
          tag: el.tagName,
          type: el.getAttribute('type'),
          text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || el.getAttribute('name') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
        })).filter(x => x.text);
      });
      notes.walls.push({ from: 'direct auth.uber.com/v2/', final: safeUrl(opened.page.url()), title: await opened.page.title(), fields, typed: false, submitted: false });
      await opened.page.close();
    }
  }

  await context.close();
}

async function phone() {
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
  });
  const requested = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };
  for (const [pth, name] of [['/', 'mobile-home'], ['/location', 'mobile-location'], ['/promo', 'mobile-promo'], ['/eats-pass', 'mobile-uber-one']]) {
    const opened = await openPage(context, pth, requested);
    if (!opened) continue;
    if (opened.wall) {
      await shot(opened.page, name + '-wall', requested);
      await opened.page.close();
      continue;
    }
    await shot(opened.page, name + '-light-default', requested);
    if (name === 'mobile-home') {
      await opened.page.locator('button[aria-label="Main navigation menu"]').first().click({ force: true }).catch(() => {});
      await opened.page.waitForTimeout(700);
      await shot(opened.page, 'mobile-home-light-nav-open', requested);
    }
    await opened.page.close();
  }
  await context.close();
}

const browser = await chromium.launch({ headless: true, args: ['--disable-blink-features=AutomationControlled'] });
await desktop();
await phone();
await browser.close();
fs.writeFileSync(NOTES, JSON.stringify(notes, null, 2));
log('wrote', NOTES);
log('pages', notes.pages.length, 'walls', notes.walls.length, 'blocked', notes.blocked.length);
