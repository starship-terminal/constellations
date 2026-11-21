// Public capture of www.dji.com for the constellations package systems/dji.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/dji/tools/capture/public/dji-capture.mjs
//
// Signed out. Never types, never submits a form, never clicks Login, Register,
// Apple, Google, Facebook, Store checkout, or a download. A control that
// navigates to a login, account, or store-checkout host is recorded and that
// branch stops. Consent and promo overlays are hidden, never accepted.
//
// Writes:
//   ~/.design-systems/dji/raw-shots/*.png   full-colour shots (not committed)
//   systems/dji/screenshots/                quantised later by quantize.py
//   systems/dji/raw/site-tree.json
//   systems/dji/raw/readings.json
//   systems/dji/raw/css-vars.json

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'dji', 'raw-shots');
const RAWJSON = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(RAWJSON, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const WALL = /(account\.dji\.com|my\.dji\.com|\/redirect\/member\/(login|register|logout)|store\.dji\.com\/[^/]+\/(checkout|cart)|\/login|\/register)/i;
const STOP_HOST = /(account\.dji\.com|my\.dji\.com)/i;

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

function abs(href, base) {
  try { return new URL(href, base).href; } catch { return href || ''; }
}

function hostOf(u) {
  try { return new URL(u).host; } catch { return ''; }
}

const tree = {
  capturedAt: new Date().toISOString(),
  start: 'https://www.dji.com/',
  region: null,
  note: 'Signed out. Singapore storefront is what www.dji.com served this client (geo redirect). Login, register, account and store-checkout branches stop at the wall. No form filled, no SSO clicked, no file downloaded.',
  pages: [],
  interactions: [],
  walls: [],
  blocked: [],
};

const readings = { pages: {}, components: {} };

async function shot(page, name, requested) {
  const file = path.join(RAW, name + '.png');
  await screenshotWithMetadata(page, { path: file }, requested);
  log('  shot', name);
  return file;
}

async function hideChrome(page) {
  await page.evaluate(() => {
    const sels = [
      '.modal-warpper', '.modal-box', '#ie-modal',
      '.universal-product-tip', '.universal-product-tip-container',
      '.universal-product-tip-container-header-placeholder',
      '.subscribe-modal-wrapper', '#subscribe-modal-wrapper',
      '.activity-modal-container',
    ];
    for (const s of sels) {
      document.querySelectorAll(s).forEach((n) => n.style.setProperty('display', 'none', 'important'));
    }
  }).catch(() => {});
}

async function settle(page) {
  await page.waitForTimeout(1800);
  await hideChrome(page);
  await page.waitForTimeout(400);
}

async function readPage(page) {
  return page.evaluate(() => {
    const text = (el) => (el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') || '').trim().replace(/\s+/g, ' ').slice(0, 120);
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none';
    };
    const header = document.querySelector('#site-header') || document.querySelector('header') || document.querySelector('nav');
    const navItems = header ? [...header.querySelectorAll('nav > ul > li, .navbar-category > li')].map((li) => {
      const title = li.querySelector(':scope > a, :scope > span, :scope > .nav-item-title');
      const links = [...li.querySelectorAll('a')].map((a) => ({
        text: text(a),
        href: a.getAttribute('href'),
        aria: a.getAttribute('aria-label'),
      }));
      return {
        title: title ? text(title) : '',
        href: title && title.getAttribute ? title.getAttribute('href') : null,
        tag: title ? title.tagName : null,
        links,
      };
    }) : [];
    const right = header ? [...header.querySelectorAll('[class*="right"] a, .navbar-right a, [class*="navbar-right"] a')].map((a) => ({
      text: text(a) || a.getAttribute('data-ga-label') || a.getAttribute('aria-label') || '',
      href: a.getAttribute('href'),
      aria: a.getAttribute('aria-label'),
      ga: a.getAttribute('data-ga-label'),
    })) : [];
    const controls = [...document.querySelectorAll('button, [role="tab"], summary, [aria-expanded]')].filter(vis).slice(0, 50).map((b) => ({
      tag: b.tagName,
      text: text(b),
      expanded: b.getAttribute('aria-expanded'),
      role: b.getAttribute('role'),
    }));
    const mainLinks = [...document.querySelectorAll('a[href]')].filter((a) => {
      const r = a.getBoundingClientRect();
      return r.top > 60 && r.width > 0 && text(a);
    }).slice(0, 80).map((a) => ({ text: text(a), href: a.getAttribute('href') }));
    const body = document.body;
    const cs = getComputedStyle(body);
    const h1 = document.querySelector('h1');
    const link = [...document.querySelectorAll('a')].find((a) => vis(a) && text(a).length > 1);
    const btn = [...document.querySelectorAll('a, button')].find((a) => vis(a) && /buy now|learn more|shop/i.test(text(a)));
    const styleOf = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        tag: el.tagName,
        text: text(el).slice(0, 60),
        color: s.color,
        backgroundColor: s.backgroundColor,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        borderRadius: s.borderRadius,
        borderTopWidth: s.borderTopWidth,
        borderTopColor: s.borderTopColor,
        padding: s.padding,
        height: Math.round(r.height) + 'px',
        boxShadow: s.boxShadow === 'none' ? 'none' : s.boxShadow.slice(0, 120),
      };
    };
    const vars = [];
    for (const sheet of [...document.styleSheets].slice(0, 30)) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (rs, n = 0) => {
        if (!rs || n > 4 || vars.length > 200) return;
        for (const rule of rs) {
          if (rule.style) {
            for (let i = 0; i < rule.style.length; i++) {
              const name = rule.style[i];
              if (name.startsWith('--')) vars.push({ name, value: rule.style.getPropertyValue(name).trim().slice(0, 80), selector: (rule.selectorText || '').slice(0, 80) });
            }
          }
          if (rule.cssRules) walk(rule.cssRules, n + 1);
        }
      };
      walk(rules);
    }
    return {
      title: document.title,
      url: location.href,
      h1: h1 ? text(h1) : '',
      bodyText: (body.innerText || '').replace(/\s+/g, ' ').slice(0, 400),
      headerClass: header ? (header.className || '').toString().slice(0, 140) : '',
      navItems,
      right,
      controls,
      mainLinks,
      body: { color: cs.color, background: cs.backgroundColor, font: cs.fontFamily, size: cs.fontSize },
      h1Style: styleOf(h1),
      linkStyle: styleOf(link),
      buttonStyle: styleOf(btn),
      headerStyle: styleOf(header),
      varCount: vars.length,
      vars: vars.slice(0, 40),
      viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
    };
  });
}

async function openContext(browser, mobile) {
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: UA_MOBILE, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  await ctx.route(/googletagmanager|google-analytics|doubleclick|facebook\.net|tiktok|sentry-io\.djiops|aliyuncs\.com|hotjar|cookielaw|onetrust/, (r) => r.abort());
  return ctx;
}

async function visit(browser, spec, mobile) {
  const prefix = (mobile ? 'mobile-' : '') + spec.id + '-light';
  const requested = mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
  const ctx = await openContext(browser, mobile);
  const page = await ctx.newPage();
  page.setDefaultTimeout(12000);
  const record = { id: spec.id, requested: spec.url, mobile: !!mobile, shots: [], interactions: [], wall: false };
  try {
    const res = await page.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await settle(page);
    const status = res ? res.status() : null;
    const info = await readPage(page);
    record.status = status;
    record.finalUrl = info.url;
    record.title = info.title;
    record.h1 = info.h1;
    record.headerClass = info.headerClass;
    record.viewport = info.viewport;
    record.navItems = info.navItems;
    record.right = info.right;
    record.controls = info.controls;
    record.mainLinks = info.mainLinks;
    record.bodyText = info.bodyText;
    if (STOP_HOST.test(info.url) || /sign in|log in|create account/i.test(info.title + info.h1)) {
      record.wall = true;
      tree.walls.push({ from: spec.url, url: info.url, title: info.title, why: 'login or account wall' });
    }
    await shot(page, prefix + '-default', requested);
    record.shots.push(prefix + '-default');
    if (!mobile) {
      readings.pages[spec.id] = {
        url: info.url,
        title: info.title,
        body: info.body,
        h1: info.h1Style,
        link: info.linkStyle,
        button: info.buttonStyle,
        header: info.headerStyle,
        vars: info.vars,
        varCount: info.varCount,
        viewport: info.viewport,
      };
    }
    if (spec.full !== false && !record.wall) {
      const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
      const chunk = Math.floor(8000 / (mobile ? 2 : 1));
      const MAXH = 4 * chunk;
      const hCap = Math.min(H, MAXH);
      if (H > MAXH) log('  truncated', spec.id, H, '->', hCap);
      if (hCap <= chunk + 40) {
        await screenshotWithMetadata(page, { path: path.join(RAW, prefix + '-full.png'), fullPage: true }, requested);
      } else {
        for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
          await screenshotWithMetadata(page, {
            path: path.join(RAW, `${prefix}-full.part${i}.png`),
            fullPage: true,
            clip: { x: 0, y, width: mobile ? 390 : 1440, height: Math.min(chunk, hCap - y) },
          }, requested);
        }
      }
      record.shots.push(prefix + '-full');
      record.scrollHeight = H;
      await page.evaluate(() => scrollTo(0, 0)).catch(() => {});
    }
    if (!mobile && spec.interact && !record.wall) {
      await spec.interact(page, record, requested);
    }
  } catch (e) {
    record.error = String(e.message || e).split('\n')[0];
    log('  FAIL', spec.id, record.error);
    tree.blocked.push({ id: spec.id, url: spec.url, error: record.error });
  } finally {
    tree.pages.push(record);
    await ctx.close();
  }
  return record;
}

async function hoverNav(page, record, requested) {
  const items = page.locator('#site-header nav > ul > li, #site-header .navbar-category > li');
  const n = await items.count();
  for (let i = 0; i < Math.min(n, 8); i++) {
    const li = items.nth(i);
    const title = (await li.locator('a, span').first().innerText().catch(() => '')).trim();
    if (!title) continue;
    await li.hover().catch(() => {});
    await page.waitForTimeout(600);
    const panel = await li.evaluate((el) => {
      const text = (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 500);
      const links = [...el.querySelectorAll('a')].map((a) => ({
        text: (a.innerText || a.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
        href: a.getAttribute('href'),
      }));
      return { text, links, cls: el.className.toString().slice(0, 80) };
    });
    const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    if (panel.links.length > 1 || panel.text.length > title.length + 4) {
      await shot(page, 'home-light-nav-' + slug, requested);
      record.shots.push('home-light-nav-' + slug);
      record.interactions.push({ control: 'hover nav item "' + title + '"', result: 'in-page dropdown', links: panel.links, text: panel.text });
      tree.interactions.push({ page: record.finalUrl, control: 'hover "' + title + '"', opens: 'dropdown', links: panel.links });
    }
  }
  await page.mouse.move(8, 400).catch(() => {});
}

async function openSearch(page, record, requested) {
  const btn = page.locator('#site-header [class*="search"], #site-header a[aria-label="Search"], a.nav-search-link').first();
  if (!(await btn.count())) {
    record.interactions.push({ control: 'search', result: 'control not found on this header' });
    return;
  }
  await btn.click({ timeout: 4000 }).catch(() => {});
  await page.waitForTimeout(800);
  const open = await page.evaluate(() => {
    const box = document.querySelector('#siteHeaderSearch, [class*="search-box"], input[name="q"], input[placeholder*="Search"]');
    const input = document.querySelector('input[name="q"], input[type="search"], input[placeholder*="Search"]');
    return {
      found: !!box,
      placeholder: input ? input.getAttribute('placeholder') : null,
      action: input && input.form ? input.form.getAttribute('action') : null,
    };
  });
  await shot(page, 'home-light-search', requested);
  record.shots.push('home-light-search');
  record.interactions.push({ control: 'search icon', result: 'in-page search disclosure', ...open, submitted: false });
  tree.interactions.push({ page: record.finalUrl, control: 'search icon', opens: 'search disclosure', detail: open });
  await page.keyboard.press('Escape').catch(() => {});
}

async function openUser(page, record, requested) {
  const btn = page.locator('#site-header [aria-label="User Center"], #site-header .user-icon, #site-header [class*="user"]').first();
  if (!(await btn.count())) {
    record.interactions.push({ control: 'user', result: 'control not found' });
    return;
  }
  await btn.hover().catch(() => {});
  await page.waitForTimeout(500);
  await btn.click({ timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(600);
  const links = await page.evaluate(() => {
    const menu = document.querySelector('.nav-account .dui-dropdown-menu, [class*="account"] [class*="dropdown"], [class*="user"] [class*="dropdown"]');
    const root = menu || document.querySelector('#site-header');
    return [...root.querySelectorAll('a')].map((a) => ({
      text: (a.innerText || a.getAttribute('aria-label') || a.getAttribute('data-ga-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
      href: a.getAttribute('href'),
    })).filter((a) => /login|register|account|logout/i.test(a.text + (a.href || '')));
  });
  await shot(page, 'home-light-account-menu', requested);
  record.shots.push('home-light-account-menu');
  record.interactions.push({ control: 'user icon', result: 'account menu; Login and Register recorded, not followed', links });
  for (const l of links) {
    const href = abs(l.href || '', record.finalUrl || 'https://www.dji.com/sg');
    if (WALL.test(href) || /login|register/i.test(l.text)) {
      tree.walls.push({ from: 'user menu', label: l.text, url: href, why: 'login or register wall; branch stopped' });
    }
  }
  tree.interactions.push({ page: record.finalUrl, control: 'user icon', opens: 'account menu', links, followed: false });
}

async function openCountry(page, record, requested) {
  const btn = page.locator('#site-header [class*="language"], #site-header [class*="country"], #site-header [class*="locale"]').first();
  if (!(await btn.count())) return;
  await btn.click({ timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(700);
  await shot(page, 'home-light-region', requested);
  record.shots.push('home-light-region');
  record.interactions.push({ control: 'region / country', result: 'in-page country panel; no region selected' });
  tree.interactions.push({ page: record.finalUrl, control: 'region control', opens: 'country panel', followed: false });
  await page.keyboard.press('Escape').catch(() => {});
}

async function mobileMenu(page, record, requested) {
  const btn = page.locator('#site-header button, #site-header [class*="burger"], #site-header [class*="menu"], #site-header [aria-label*="menu" i]').first();
  if (!(await btn.count())) {
    record.interactions.push({ control: 'mobile menu', result: 'control not found' });
    return;
  }
  await btn.click({ timeout: 4000 }).catch(() => {});
  await page.waitForTimeout(800);
  await shot(page, 'mobile-home-light-menu', requested);
  record.shots.push('mobile-home-light-menu');
  const links = await page.evaluate(() => [...document.querySelectorAll('#site-header a, [class*="drawer"] a, [class*="menu"] a')].slice(0, 40).map((a) => ({
    text: (a.innerText || a.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
    href: a.getAttribute('href'),
  })).filter((a) => a.text || a.href));
  record.interactions.push({ control: 'mobile menu button', result: 'drawer or expanded nav', links });
  tree.interactions.push({ page: record.finalUrl, control: 'mobile menu', opens: 'drawer', links });
}

const PAGES = [
  {
    id: 'home',
    url: 'https://www.dji.com/',
    interact: async (page, record, requested) => {
      await hoverNav(page, record, requested);
      await openSearch(page, record, requested);
      await openUser(page, record, requested);
      await openCountry(page, record, requested);
    },
  },
  { id: 'camera-drones', url: 'https://www.dji.com/sg/camera-drones' },
  { id: 'handheld', url: 'https://www.dji.com/sg/handheld' },
  { id: 'power', url: 'https://www.dji.com/sg/products/power-series' },
  { id: 'delivery', url: 'https://www.dji.com/sg/delivery' },
  { id: 'company', url: 'https://www.dji.com/sg/company' },
  { id: 'media', url: 'https://www.dji.com/sg/media-center' },
  { id: 'trust', url: 'https://www.dji.com/sg/trust-center' },
  { id: 'support', url: 'https://www.dji.com/sg/support' },
  { id: 'where-to-buy', url: 'https://www.dji.com/sg/where-to-buy/online-stores' },
  { id: 'mavic', url: 'https://www.dji.com/sg/mavic-4-pro' },
  { id: 'compare', url: 'https://www.dji.com/sg/products/comparison-consumer-drones' },
  { id: 'choose', url: 'https://www.dji.com/sg/help-me-choose/camera-drones' },
  { id: 'search', url: 'https://www.dji.com/sg/search?q=mavic' },
  { id: 'a11y', url: 'https://www.dji.com/accessibility/web-accessibility' },
  { id: 'notfound', url: 'https://www.dji.com/sg/this-page-does-not-exist-capture' },
];

const MOBILE = [
  { id: 'home', url: 'https://www.dji.com/', interact: async (page, record, requested) => { await mobileMenu(page, record, requested); } },
  { id: 'camera-drones', url: 'https://www.dji.com/sg/camera-drones' },
  { id: 'mavic', url: 'https://www.dji.com/sg/mavic-4-pro' },
  { id: 'support', url: 'https://www.dji.com/sg/support' },
  { id: 'where-to-buy', url: 'https://www.dji.com/sg/where-to-buy/online-stores' },
];

// Login wall: open the redirect URL, record where it lands, do not type.
async function probeWall(browser) {
  const url = 'https://www-api.dji.com/sg/redirect/member/login?backUrl=https%3A%2F%2Fwww.dji.com%2Fsg';
  const ctx = await openContext(browser, false);
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 40000 });
    await page.waitForTimeout(2500);
    const info = await page.evaluate(() => ({
      url: location.href,
      title: document.title,
      text: (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 400),
      inputs: [...document.querySelectorAll('input')].map((i) => ({ type: i.type, name: i.name, placeholder: i.placeholder })).slice(0, 8),
      buttons: [...document.querySelectorAll('button, a')].map((b) => (b.innerText || b.getAttribute('aria-label') || '').trim()).filter(Boolean).slice(0, 12),
    }));
    await shot(page, 'login-wall-light-default', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    tree.walls.push({ from: url, url: info.url, title: info.title, inputs: info.inputs.map((i) => i.type || i.name), buttons: info.buttons, why: 'login wall; no credentials entered; SSO not clicked' });
    tree.pages.push({ id: 'login-wall', requested: url, finalUrl: info.url, title: info.title, wall: true, shots: ['login-wall-light-default'], bodyText: info.text });
    log('wall', info.url, info.title);
  } catch (e) {
    tree.blocked.push({ id: 'login-wall', url, error: String(e.message || e).split('\n')[0] });
  } finally {
    await ctx.close();
  }
}

const browser = await chromium.launch({ headless: true });
try {
  log('desktop');
  for (const spec of PAGES) {
    log('page', spec.id);
    const rec = await visit(browser, spec, false);
    if (spec.id === 'home' && rec.finalUrl) tree.region = rec.finalUrl;
  }
  log('mobile');
  for (const spec of MOBILE) {
    log('mobile', spec.id);
    await visit(browser, spec, true);
  }
  log('login wall');
  await probeWall(browser);
} finally {
  await browser.close();
}

fs.writeFileSync(path.join(RAWJSON, 'site-tree.json'), JSON.stringify(tree, null, 2) + '\n');
fs.writeFileSync(path.join(RAWJSON, 'readings.json'), JSON.stringify(readings, null, 2) + '\n');
const vars = {};
for (const [id, page] of Object.entries(readings.pages)) vars[id] = { url: page.url, varCount: page.varCount, vars: page.vars, body: page.body };
fs.writeFileSync(path.join(RAWJSON, 'css-vars.json'), JSON.stringify({ product: 'dji', note: 'Declared custom properties found in same-origin stylesheets. An empty list is an honest reading, not a guess.', pages: vars }, null, 2) + '\n');
log('wrote', tree.pages.length, 'pages', tree.walls.length, 'walls', tree.blocked.length, 'blocked');
