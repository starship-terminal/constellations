// One-shot public harvest for fal.ai. Reads CSS custom properties, computed
// component states, and screenshots. Never clicks an OAuth provider, never
// submits a form, never accepts a consent banner (the banner is hidden).
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/fal/tools/capture/harvest.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..', '..');
const RAW = path.join(PKG, 'raw');
const SHOTS = path.join(os.homedir(), '.design-systems', 'fal', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(SHOTS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const HIDE = `
  #onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter,
  #ot-sdk-btn-floating, .ot-sdk-container, #onetrust-pc-sdk { display: none !important; visibility: hidden !important; }
`;

function hideConsent() {
  const css = document.createElement('style');
  css.id = 'capture-hide-consent';
  css.textContent = `#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter, #ot-sdk-btn-floating, .ot-sdk-container, #onetrust-pc-sdk { display: none !important; }`;
  document.documentElement.appendChild(css);
  for (const el of document.querySelectorAll('div, aside, section')) {
    const t = (el.innerText || '').slice(0, 120);
    const r = el.getBoundingClientRect();
    if (/We Value Your Privacy|Accept All|Cookie Policy/i.test(t) && r.height > 40 && r.height < 640 && r.width < 520) {
      el.setAttribute('data-capture-hidden-consent', '1');
      el.style.setProperty('display', 'none', 'important');
    }
  }
}

async function shot(page, file, extra = {}) {
  const requested = {
    viewport: page.viewportSize(),
    deviceScaleFactor: extra.dpr || 1,
  };
  const meta = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    devicePixelRatio: window.devicePixelRatio,
    visualViewport: window.visualViewport ? {
      width: window.visualViewport.width,
      height: window.visualViewport.height,
      scale: window.visualViewport.scale,
    } : null,
    scrollHeight: document.documentElement.scrollHeight,
  }));
  await page.screenshot({ path: file, fullPage: !!extra.fullPage });
  const buf = fs.readFileSync(file);
  // PNG IHDR
  const w = buf.readUInt32BE(16);
  const h = buf.readUInt32BE(20);
  fs.writeFileSync(file + '.capture.json', JSON.stringify({
    capturedAt: new Date().toISOString(),
    requested,
    measured: meta,
    png: { width: w, height: h },
    fullPage: !!extra.fullPage,
    note: extra.note || '',
  }, null, 2));
}

const browser = await chromium.launch({ headless: true });

async function contextFor({ width, height, dpr, mobile }) {
  return browser.newContext(mobile
    ? { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
}

async function open(page, url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2200);
  await page.evaluate(hideConsent);
  await page.addStyleTag({ content: HIDE }).catch(() => {});
  return { status: resp ? resp.status() : 0, url: page.url() };
}

const PROPS = [
  'display', 'position', 'width', 'height', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'color', 'backgroundColor',
  'borderTopWidth', 'borderTopColor', 'borderTopStyle', 'borderRadius', 'boxShadow', 'opacity',
  'textDecoration', 'outline', 'outlineOffset',
];

function readEl(el) {
  if (!el) return null;
  const s = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const o = { text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80), box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
  for (const p of PROPS) o[p] = s[p];
  return o;
}

// ---------- CSS variables from the marketing home (Webflow) and the login app ----------
const desk = await contextFor({ width: 1440, height: 900, dpr: 1, mobile: false });
const page = await desk.newPage();

async function harvestVars(url, label) {
  await open(page, url);
  return page.evaluate((label) => {
    const rules = [];
    const fonts = [];
    const errors = [];
    const walk = (list, ctx, file) => {
      for (const r of list) {
        try {
          if (r.type === CSSRule.FONT_FACE_RULE) {
            const o = { file };
            for (let i = 0; i < r.style.length; i++) o[r.style[i]] = r.style.getPropertyValue(r.style[i]).trim().slice(0, 180);
            fonts.push(o);
            continue;
          }
          if (r.cssRules && !r.style) {
            const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
              : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
              : r.cssText.slice(0, 80);
            walk(r.cssRules, [...ctx, head].slice(0, 4), file);
            continue;
          }
          if (!r.style) continue;
          const props = {};
          for (let i = 0; i < r.style.length; i++) {
            const k = r.style[i];
            if (k.startsWith('--')) props[k] = r.style.getPropertyValue(k).trim().slice(0, 240);
          }
          if (Object.keys(props).length) {
            rules.push({ file, selector: (r.selectorText || '').slice(0, 180), context: ctx, properties: props });
          }
        } catch (e) { errors.push(String(e).slice(0, 120)); }
      }
    };
    const sheets = [];
    for (const s of document.styleSheets) {
      const name = s.href || 'inline';
      try { walk(s.cssRules, [], name); sheets.push({ name, rules: true }); }
      catch (e) { sheets.push({ name, unreadable: String(e).slice(0, 80) }); }
    }
    const root = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const names = new Set();
    for (const rule of rules) for (const k of Object.keys(rule.properties)) names.add(k);
    const resolved = {};
    for (const n of names) {
      const v = root.getPropertyValue(n).trim();
      if (v) resolved[n] = v.slice(0, 240);
    }
    const themeMeta = [...document.querySelectorAll('meta[name="theme-color"], link[rel="mask-icon"]')].map(el => ({
      name: el.getAttribute('name') || el.getAttribute('rel'),
      content: el.getAttribute('content') || el.getAttribute('color') || el.getAttribute('href'),
      media: el.getAttribute('media'),
    }));
    return {
      label, url: location.href, title: document.title,
      sheets, ruleCount: rules.length, fontCount: fonts.length, errors: errors.slice(0, 8),
      fonts: fonts.slice(0, 30),
      rules,
      resolved,
      themeMeta,
      htmlClass: document.documentElement.className.slice(0, 200),
      colorScheme: root.colorScheme,
      bodyBg: body.backgroundColor,
      bodyColor: body.color,
      bodyFont: body.fontFamily,
    };
  }, label);
}

console.log('vars home');
const homeVars = await harvestVars('https://fal.ai/', 'home');
console.log('  rules', homeVars.ruleCount, 'resolved', Object.keys(homeVars.resolved).length, 'fonts', homeVars.fontCount);
console.log('vars login');
const loginVars = await harvestVars('https://fal.ai/login', 'login');
console.log('  rules', loginVars.ruleCount, 'resolved', Object.keys(loginVars.resolved).length);
console.log('vars pricing');
const priceVars = await harvestVars('https://fal.ai/pricing', 'pricing');
console.log('  rules', priceVars.ruleCount, 'resolved', Object.keys(priceVars.resolved).length);
console.log('vars explore');
const exploreVars = await harvestVars('https://fal.ai/explore', 'explore');
console.log('  rules', exploreVars.ruleCount, 'resolved', Object.keys(exploreVars.resolved).length);

fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  capturedAt: new Date().toISOString(),
  source: 'https://fal.ai/ live CSSOM, signed out',
  pages: {
    home: { url: homeVars.url, ruleCount: homeVars.ruleCount, resolvedCount: Object.keys(homeVars.resolved).length, themeMeta: homeVars.themeMeta, htmlClass: homeVars.htmlClass, colorScheme: homeVars.colorScheme, bodyBg: homeVars.bodyBg, bodyColor: homeVars.bodyColor, bodyFont: homeVars.bodyFont, sheets: homeVars.sheets, fonts: homeVars.fonts },
    login: { url: loginVars.url, ruleCount: loginVars.ruleCount, resolvedCount: Object.keys(loginVars.resolved).length, colorScheme: loginVars.colorScheme, bodyBg: loginVars.bodyBg, bodyColor: loginVars.bodyColor, bodyFont: loginVars.bodyFont, htmlClass: loginVars.htmlClass, themeMeta: loginVars.themeMeta, sheets: loginVars.sheets, fonts: loginVars.fonts },
    pricing: { url: priceVars.url, ruleCount: priceVars.ruleCount, resolvedCount: Object.keys(priceVars.resolved).length, bodyBg: priceVars.bodyBg, bodyFont: priceVars.bodyFont },
    explore: { url: exploreVars.url, ruleCount: exploreVars.ruleCount, resolvedCount: Object.keys(exploreVars.resolved).length, bodyBg: exploreVars.bodyBg, bodyFont: exploreVars.bodyFont, colorScheme: exploreVars.colorScheme },
  },
  rules: {
    home: homeVars.rules,
    login: loginVars.rules,
  },
  resolved: {
    home: homeVars.resolved,
    login: loginVars.resolved,
    pricing: priceVars.resolved,
    explore: exploreVars.resolved,
  },
}, null, 2));
console.log('wrote css-vars.json', fs.statSync(path.join(RAW, 'css-vars.json')).size);

// ---------- component measurements ----------
async function measure(url, specs) {
  await open(page, url);
  const out = { url: page.url(), states: {} };
  for (const spec of specs) {
    const hit = await page.evaluate((sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const read = (node) => {
        if (!node) return null;
        const s = getComputedStyle(node);
        const r = node.getBoundingClientRect();
        const props = ['display','width','height','paddingTop','paddingRight','paddingBottom','paddingLeft','gap','fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','color','backgroundColor','borderTopWidth','borderTopColor','borderRadius','boxShadow','opacity','textDecorationLine','outline','outlineOffset'];
        const o = { text: (node.innerText || node.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80), box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
        for (const p of props) o[p] = s[p];
        return o;
      };
      return { default: read(el) };
    }, spec.sel);
    if (!hit) { out.states[spec.id] = { missing: true, sel: spec.sel }; continue; }
    const loc = page.locator(spec.sel).first();
    const states = { default: hit.default };
    try {
      await loc.hover({ timeout: 3000 });
      await page.waitForTimeout(250);
      states.hover = await loc.evaluate((node) => {
        const s = getComputedStyle(node);
        const r = node.getBoundingClientRect();
        return { box: { w: Math.round(r.width), h: Math.round(r.height) }, color: s.color, backgroundColor: s.backgroundColor, borderTopColor: s.borderTopColor, boxShadow: s.boxShadow, textDecorationLine: s.textDecorationLine, opacity: s.opacity };
      });
    } catch (e) { states.hover = { error: String(e.message).split('\n')[0] }; }
    try {
      await loc.focus();
      await page.waitForTimeout(150);
      states.focus = await loc.evaluate((node) => {
        const s = getComputedStyle(node);
        return { outline: s.outline, outlineOffset: s.outlineOffset, boxShadow: s.boxShadow, borderTopColor: s.borderTopColor };
      });
    } catch (e) { states.focus = { error: String(e.message).split('\n')[0] }; }
    try {
      await page.mouse.down();
      await page.waitForTimeout(80);
      states.pressed = await loc.evaluate((node) => {
        const s = getComputedStyle(node);
        return { backgroundColor: s.backgroundColor, color: s.color, transform: s.transform, boxShadow: s.boxShadow };
      });
      await page.mouse.up();
    } catch (e) { states.pressed = { error: String(e.message).split('\n')[0] }; }
    await page.mouse.move(2, 2);
    out.states[spec.id] = { sel: spec.sel, ...states };
    console.log('  measured', spec.id, hit.default && hit.default.text);
  }
  return out;
}

console.log('measure home');
const homeMeasure = await measure('https://fal.ai/', [
  { id: 'nav-link', sel: 'a.nav-list-item' },
  { id: 'nav-dropdown', sel: '.nav-list-item-dropdown.is-dropdown' },
  { id: 'button-sales', sel: 'a.button[href="/contact-sales"]' },
  { id: 'button-start', sel: 'a.button[href="https://fal.ai/dashboard"]' },
  { id: 'hero-h1', sel: 'h1' },
  { id: 'tab', sel: 'a.tab-menu-link' },
  { id: 'footer-link', sel: 'a.footer-link' },
]);

console.log('measure pricing');
const priceMeasure = await measure('https://fal.ai/pricing', [
  { id: 'pricing-h1', sel: 'h1' },
  { id: 'plan-cta', sel: 'a.button' },
]);

console.log('measure login');
const loginMeasure = await measure('https://fal.ai/login', [
  { id: 'oauth-github', sel: 'a[href*="connect/github"]' },
  { id: 'oauth-google', sel: 'a[href*="connect/google"]' },
  { id: 'oauth-microsoft', sel: 'a[href*="connect/microsoft"]' },
  { id: 'sso', sel: 'button:has-text("Use SSO")' },
  { id: 'login-h1', sel: 'h1' },
]);

console.log('measure explore');
const exploreMeasure = await measure('https://fal.ai/explore', [
  { id: 'explore-search', sel: 'input[type="search"], input[placeholder*="Search"], input[aria-label*="Search"]' },
  { id: 'model-card', sel: 'a[href^="/models/"]' },
]);

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({
  capturedAt: new Date().toISOString(),
  viewport: { width: 1440, height: 900, dpr: 1 },
  home: homeMeasure,
  pricing: priceMeasure,
  login: loginMeasure,
  explore: exploreMeasure,
}, null, 2));

// ---------- screenshots ----------
const pages = [
  ['home', 'https://fal.ai/'],
  ['pricing', 'https://fal.ai/pricing'],
  ['enterprise', 'https://fal.ai/enterprise-hub'],
  ['docs', 'https://fal.ai/docs'],
  ['explore', 'https://fal.ai/explore'],
  ['blog', 'https://fal.ai/blog'],
  ['login', 'https://fal.ai/login'],
  ['serverless', 'https://fal.ai/serverless'],
  ['legal', 'https://fal.ai/legal'],
  ['contact', 'https://fal.ai/contact-sales'],
];

for (const [name, url] of pages) {
  console.log('shot', name);
  await open(page, url);
  await shot(page, path.join(SHOTS, `${name}-light-default.png`), { dpr: 1, note: url });
  // full page, capped
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  if (H < 14000) {
    await shot(page, path.join(SHOTS, `${name}-light-full.png`), { dpr: 1, fullPage: true, note: url });
  } else {
    console.log('  skip full, H', H);
  }
}

// menus
await open(page, 'https://fal.ai/');
await page.locator('.nav-list-item-dropdown.is-dropdown').filter({ hasText: 'Products' }).first().hover();
await page.waitForTimeout(600);
await shot(page, path.join(SHOTS, 'home-light-products-menu.png'), { dpr: 1, note: 'Products dropdown hover' });
await page.mouse.move(8, 8);
await page.locator('.nav-list-item-dropdown.is-dropdown').filter({ hasText: 'Resources' }).first().hover();
await page.waitForTimeout(600);
await shot(page, path.join(SHOTS, 'home-light-resources-menu.png'), { dpr: 1, note: 'Resources dropdown hover' });

// home tab
await page.mouse.move(8, 8);
await page.waitForTimeout(300);
const tab = page.locator('a.tab-menu-link').nth(1);
if (await tab.count()) {
  await tab.click();
  await page.waitForTimeout(500);
  await shot(page, path.join(SHOTS, 'home-light-tab-serverless.png'), { dpr: 1, note: 'home Serverless tab, local pane, not a navigation' });
}

await page.close();
await desk.close();

// mobile
const mob = await contextFor({ width: 390, height: 844, dpr: 2, mobile: true });
const mp = await mob.newPage();
for (const [name, url] of [['home', 'https://fal.ai/'], ['pricing', 'https://fal.ai/pricing'], ['login', 'https://fal.ai/login'], ['explore', 'https://fal.ai/explore']]) {
  console.log('mobile', name);
  await open(mp, url);
  await shot(mp, path.join(SHOTS, `mobile-${name}-light-default.png`), { dpr: 2, note: url });
}
// mobile menu
await open(mp, 'https://fal.ai/');
const menuBtn = mp.locator('.w-nav-button, button.menu-button, .nav-button, [aria-label*="menu" i]').first();
console.log('mobile menu count', await mp.locator('.w-nav-button').count());
if (await mp.locator('.w-nav-button').count()) {
  await mp.locator('.w-nav-button').first().click();
  await mp.waitForTimeout(700);
  await shot(mp, path.join(SHOTS, 'mobile-home-light-menu.png'), { dpr: 2, note: 'opened mobile nav' });
}
await browser.close();
console.log('done');
