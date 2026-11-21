// Public Codex marketing capture. Signed out. No form fill, no identity
// provider, no cookie POST. Cookie banner is hidden, never accepted.
//
// PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//   node tools/capture/public/capture-codex.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { safeUrl } from '../safe-url.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..', '..', '..');
const OUT = path.join(PKG, 'screenshots');
const RAW = path.join(PKG, 'raw');
const SNAPS = process.env.SNAPS || path.join(process.env.HOME, '.design-systems/codex/snaps');
fs.mkdirSync(OUT, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(SNAPS, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HIDE_COOKIE = `
  (() => {
    const kill = (el) => { if (el) el.style.setProperty('display', 'none', 'important'); };
    document.querySelectorAll('button').forEach((b) => {
      const t = (b.innerText || '').trim();
      if (/reject non-essential|accept all|manage cookies/i.test(t)) {
        let n = b;
        for (let i = 0; i < 8 && n; i++) {
          const txt = (n.innerText || '');
          if (/we use cookies/i.test(txt) && n.getBoundingClientRect().height > 40) { kill(n); return; }
          n = n.parentElement;
        }
      }
    });
  })()
`;

async function settle(page) {
  await page.waitForTimeout(800);
  await page.evaluate(HIDE_COOKIE);
  await page.waitForTimeout(200);
}

async function shot(page, name, requested) {
  const file = path.join(OUT, name + '.png');
  await settle(page);
  await screenshotWithMetadata(page, { path: file, fullPage: false, type: 'png' }, {
    viewport: requested.viewport,
    deviceScaleFactor: requested.deviceScaleFactor,
    sanitizedSourceUrl: page.url(),
  });
  console.log('shot', name, safeUrl(page.url()));
  return file;
}

async function dumpStyles(page, label) {
  const data = await page.evaluate(() => {
    const vars = {};
    const root = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        if (!list) return;
        for (const r of list) {
          if (r.style) {
            for (let i = 0; i < r.style.length; i++) {
              const p = r.style[i];
              if (p.startsWith('--')) vars[p] = r.style.getPropertyValue(p).trim();
            }
          }
          if (r.cssRules) walk(r.cssRules);
        }
      };
      walk(rules);
    }
    const pick = (el, props) => {
      if (!el) return null;
      const cs = getComputedStyle(el);
      const o = { text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 80) };
      for (const p of props) o[p] = cs[p];
      const r = el.getBoundingClientRect();
      o.box = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
      return o;
    };
    const props = ['color', 'backgroundColor', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'borderRadius', 'borderTopWidth', 'borderTopColor', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'boxShadow', 'outline', 'textDecorationLine'];
    const q = (sel) => document.querySelector(sel);
    const samples = {
      body: pick(document.body, props),
      h1: pick(q('h1'), props),
      h2: pick(q('h2'), props),
      navLink: pick(q('nav a'), props),
      primaryBtn: pick([...document.querySelectorAll('a,button')].find((e) => /download for macos/i.test(e.innerText || '')), props),
      secondaryBtn: pick([...document.querySelectorAll('a,button')].find((e) => /^try on web/i.test((e.innerText || '').trim())), props),
      loginBtn: pick([...document.querySelectorAll('button')].find((e) => (e.innerText || '').trim() === 'Log in'), props),
    };
    const cssVarsOnRoot = {};
    for (let i = 0; i < root.length; i++) {
      const p = root[i];
      if (p.startsWith('--')) cssVarsOnRoot[p] = root.getPropertyValue(p).trim();
    }
    return {
      title: document.title,
      colorScheme: root.colorScheme,
      bg: body.backgroundColor,
      font: body.fontFamily,
      viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio, scrollH: document.documentElement.scrollHeight },
      declaredVarCount: Object.keys(vars).length,
      declaredVars: vars,
      computedRootVars: cssVarsOnRoot,
      samples,
    };
  });
  const file = path.join(RAW, label + '.json');
  fs.writeFileSync(file, JSON.stringify(data, null, 2) + '\n');
  console.log('styles', label, 'vars', data.declaredVarCount);
  return data;
}

async function openMenu(page, label) {
  await page.evaluate((label) => {
    const btn = [...document.querySelectorAll('button')].find((b) => (b.getAttribute('aria-label') || '') === label);
    if (btn) btn.click();
  }, label);
  await page.waitForTimeout(400);
  await page.evaluate(HIDE_COOKIE);
}

const browser = await chromium.launch({ headless: true });

const desktop = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };
const phone = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };

async function newPage(size) {
  const ctx = await browser.newContext({
    viewport: size.viewport,
    deviceScaleFactor: size.deviceScaleFactor,
    colorScheme: 'dark',
    locale: 'en-US',
  });
  const page = await ctx.newPage();
  page.setDefaultNavigationTimeout(45000);
  return { ctx, page };
}

const notes = [];

// --- homepage desktop ---
{
  const { ctx, page } = await newPage(desktop);
  await page.goto('https://openai.com/codex/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1500);
  await dumpStyles(page, 'home-computed');
  await shot(page, 'home-dark-default', desktop);
  const full = path.join(OUT, 'home-dark-full.png');
  await screenshotWithMetadata(page, { path: full, fullPage: true, type: 'png' }, {
    viewport: desktop.viewport,
    deviceScaleFactor: 1,
    sanitizedSourceUrl: 'https://openai.com/codex/',
  });
  console.log('full home');

  // nav menus
  for (const [label, name] of [
    ['Products menu', 'nav-products-dark-open'],
    ['Developers menu', 'nav-developers-dark-open'],
    ['Business menu', 'nav-business-dark-open'],
    ['Research menu', 'nav-research-dark-open'],
    ['Company menu', 'nav-company-dark-open'],
  ]) {
    await page.keyboard.press('Escape');
    await page.waitForTimeout(150);
    await openMenu(page, label);
    await shot(page, name, desktop);
    await page.keyboard.press('Escape');
  }

  // search
  await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((x) => (x.getAttribute('aria-label') || '') === 'Open Search');
    if (b) b.click();
  });
  await page.waitForTimeout(500);
  await page.evaluate(HIDE_COOKIE);
  await shot(page, 'search-dark-empty', desktop);
  const searchState = await page.evaluate(() => {
    const input = document.querySelector('input, [role=searchbox], [contenteditable=true]');
    return {
      url: location.href.split('?')[0],
      placeholder: input ? (input.getAttribute('placeholder') || input.getAttribute('aria-label') || '') : null,
      value: input && 'value' in input ? input.value : null,
    };
  });
  notes.push({ search: searchState });
  await page.keyboard.press('Escape');

  // login menu, empty, do not follow
  await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((x) => (x.innerText || '').trim() === 'Log in');
    if (b) b.click();
  });
  await page.waitForTimeout(500);
  await page.evaluate(HIDE_COOKIE);
  await shot(page, 'login-menu-dark-empty', desktop);
  const loginItems = await page.evaluate(() => {
    const btn = [...document.querySelectorAll('button')].find((x) => (x.innerText || '').trim() === 'Log in');
    const menu = document.querySelector('[role=menu][data-state=open], [data-state=open][role=menu]');
    const scope = menu || document;
    const items = [...scope.querySelectorAll('a, [role=menuitem]')].filter((a) => {
      const r = a.getBoundingClientRect();
      return r.height > 4 && r.top > 40 && r.top < 500;
    }).map((a) => ({
      text: (a.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      href: (a.getAttribute('href') || '').split('?')[0],
    }));
    return { expanded: btn ? btn.getAttribute('aria-expanded') : null, items };
  });
  notes.push({ loginMenu: loginItems });
  fs.writeFileSync(path.join(RAW, 'login-menu.json'), JSON.stringify(loginItems, null, 2) + '\n');

  // hover primary
  const box = await page.evaluate(() => {
    const a = [...document.querySelectorAll('a')].find((e) => /download for macos/i.test(e.innerText || ''));
    if (!a) return null;
    const r = a.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  });
  if (box) {
    await page.mouse.move(box.x, box.y);
    await page.waitForTimeout(250);
    await shot(page, 'home-dark-hover-download', desktop);
    const hover = await page.evaluate(() => {
      const a = [...document.querySelectorAll('a')].find((e) => /download for macos/i.test(e.innerText || ''));
      if (!a) return null;
      const cs = getComputedStyle(a);
      return { backgroundColor: cs.backgroundColor, color: cs.color, borderRadius: cs.borderRadius };
    });
    notes.push({ hoverDownload: hover });
  }

  // focus login with keyboard
  await page.keyboard.press('Escape');
  await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((x) => (x.innerText || '').trim() === 'Log in');
    if (b) b.focus();
  });
  await page.waitForTimeout(200);
  await shot(page, 'home-dark-focus-login', desktop);

  // footer crop via scroll
  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(400);
  await page.evaluate(HIDE_COOKIE);
  await shot(page, 'footer-dark-default', desktop);
  const footer = await page.evaluate(() => {
    const f = document.querySelector('footer');
    if (!f) return null;
    const groups = [];
    const headings = [...f.querySelectorAll('h2, h3, p, button, a')];
    return {
      text: (f.innerText || '').slice(0, 4000),
      links: [...f.querySelectorAll('a')].slice(0, 80).map((a) => ({
        text: (a.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60),
        href: (a.getAttribute('href') || '').split('?')[0],
      })),
    };
  });
  fs.writeFileSync(path.join(RAW, 'footer.json'), JSON.stringify(footer, null, 2) + '\n');

  await ctx.close();
}

// --- inner page: developer docs for Codex ---
{
  const { ctx, page } = await newPage(desktop);
  const url = 'https://developers.openai.com/codex/';
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1800);
  await dumpStyles(page, 'docs-computed');
  await shot(page, 'docs-dark-default', desktop);
  const full = path.join(OUT, 'docs-dark-full.png');
  await screenshotWithMetadata(page, { path: full, fullPage: true, type: 'png' }, {
    viewport: desktop.viewport, deviceScaleFactor: 1, sanitizedSourceUrl: url,
  });
  const docsLinks = await page.evaluate(() => {
    return [...document.querySelectorAll('a[href]')].slice(0, 60).map((a) => ({
      text: (a.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      href: (a.getAttribute('href') || '').split('?')[0],
    }));
  });
  fs.writeFileSync(path.join(RAW, 'docs-links.json'), JSON.stringify({ url: page.url().split('?')[0], title: await page.title(), links: docsLinks }, null, 2) + '\n');
  await ctx.close();
}

// --- pricing page linked from Business menu, Codex is listed there ---
{
  const { ctx, page } = await newPage(desktop);
  await page.goto('https://openai.com/business/pricing/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1500);
  await shot(page, 'pricing-dark-default', desktop);
  await ctx.close();
}

// --- mobile home + docs ---
{
  const { ctx, page } = await newPage(phone);
  await page.goto('https://openai.com/codex/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1500);
  await shot(page, 'mobile-home-dark-default', phone);
  await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((x) => /open mobile navigation/i.test(x.getAttribute('aria-label') || x.innerText || ''));
    if (b) b.click();
  });
  await page.waitForTimeout(500);
  await page.evaluate(HIDE_COOKIE);
  await shot(page, 'mobile-nav-dark-open', phone);
  await ctx.close();
}
{
  const { ctx, page } = await newPage(phone);
  await page.goto('https://developers.openai.com/codex/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1500);
  await shot(page, 'mobile-docs-dark-default', phone);
  await ctx.close();
}

// --- login wall: follow the menu item in a fresh page, stop at the wall ---
{
  const menu = JSON.parse(fs.readFileSync(path.join(RAW, 'login-menu.json'), 'utf8'));
  const chatgpt = (menu.items || []).find((i) => /chatgpt/i.test(i.text) && i.href);
  const api = (menu.items || []).find((i) => /api/i.test(i.text) && i.href);
  notes.push({ followed: { chatgpt: chatgpt || null, api: api || null } });
  for (const [item, name] of [[chatgpt, 'login-chatgpt'], [api, 'login-api']]) {
    if (!item || !item.href) continue;
    const href = item.href.startsWith('http') ? item.href : 'https://openai.com' + item.href;
    const { ctx, page } = await newPage(desktop);
    try {
      await page.goto(href, { waitUntil: 'domcontentloaded', timeout: 30000 });
      await page.waitForTimeout(2000);
    } catch (err) {
      notes.push({ wallError: name, message: String(err).slice(0, 200) });
      await ctx.close();
      continue;
    }
    const info = await page.evaluate(() => ({
      urlPath: location.pathname,
      host: location.host,
      title: document.title,
      hasPassword: !!document.querySelector('input[type=password]'),
      hasEmail: !!document.querySelector('input[type=email], input[name=email], input[autocomplete=username]'),
      inputs: [...document.querySelectorAll('input')].map((i) => ({ type: i.type, name: i.name, placeholder: i.placeholder })).slice(0, 8),
      buttons: [...document.querySelectorAll('button, a')].slice(0, 20).map((b) => (b.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60)).filter(Boolean),
    }));
    notes.push({ wall: name, info });
    const bad = /callback|oauth|session|code=|token=/i.test(page.url());
    if (!bad) {
      await shot(page, name + '-dark-empty', desktop);
    } else {
      notes.push({ discarded: name, reason: 'oauth or session url' });
    }
    await ctx.close();
  }
}

fs.writeFileSync(path.join(RAW, 'capture-notes.json'), JSON.stringify(notes, null, 2) + '\n');
await browser.close();
console.log('done');
