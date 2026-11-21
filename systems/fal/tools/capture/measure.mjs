// Measure public fal controls and take screenshots. Hover and focus only.
// Never follows a navigation, never clicks OAuth, never submits a form.
// Consent banners are hidden, never accepted.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node systems/fal/tools/capture/measure.mjs
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

const READ_JS = `(node) => {
  if (!node) return null;
  const s = getComputedStyle(node);
  const r = node.getBoundingClientRect();
  const props = ['color','backgroundColor','borderTopWidth','borderTopStyle','borderTopColor','borderRadius','boxShadow','outline','outlineColor','outlineWidth','outlineOffset','opacity','fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','paddingTop','paddingRight','paddingBottom','paddingLeft','height','width','gap','textDecorationLine','transform'];
  const o = { text: (node.innerText || node.getAttribute('aria-label') || '').trim().replace(/\\s+/g, ' ').slice(0, 90), box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
  for (const p of props) o[p] = s[p];
  return o;
}`;

function hideConsent() {
  const css = document.getElementById('capture-hide-consent') || document.createElement('style');
  css.id = 'capture-hide-consent';
  css.textContent = '#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter, #ot-sdk-btn-floating { display: none !important; }';
  document.documentElement.appendChild(css);
  for (const el of document.querySelectorAll('div, aside, section')) {
    const t = (el.innerText || '').slice(0, 140);
    const r = el.getBoundingClientRect();
    if (/We Value Your Privacy|Accept All/i.test(t) && r.height > 40 && r.height < 700 && r.width < 560) {
      el.style.setProperty('display', 'none', 'important');
    }
  }
}

async function shot(page, file, extra = {}) {
  const meta = await page.evaluate(() => ({
    innerWidth: innerWidth, innerHeight: innerHeight, devicePixelRatio,
    visualViewport: visualViewport ? { width: visualViewport.width, height: visualViewport.height, scale: visualViewport.scale } : null,
    scrollHeight: document.documentElement.scrollHeight,
  }));
  await page.screenshot({ path: file, fullPage: !!extra.fullPage });
  const buf = fs.readFileSync(file);
  fs.writeFileSync(file + '.capture.json', JSON.stringify({
    capturedAt: new Date().toISOString(),
    requested: { viewport: page.viewportSize(), deviceScaleFactor: extra.dpr || 1 },
    measured: meta,
    png: { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) },
    fullPage: !!extra.fullPage,
    note: extra.note || '',
  }, null, 2));
}

const browser = await chromium.launch({ headless: true });
const desk = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await desk.newPage();

async function open(url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2000);
  await page.evaluate(hideConsent);
}

async function readState(sel) {
  const loc = page.locator(sel).first();
  if (!(await loc.count())) return { missing: true, sel };
  const box = await loc.boundingBox();
  if (!box) return { missing: true, sel, reason: 'no box' };
  const out = { sel };
  out.default = await loc.evaluate(eval(READ_JS));
  await page.mouse.move(box.x + Math.min(box.width / 2, 40), box.y + Math.min(box.height / 2, 16));
  await page.waitForTimeout(220);
  out.hover = await loc.evaluate(eval(READ_JS));
  await loc.focus().catch(() => {});
  await page.waitForTimeout(120);
  out.focus = await loc.evaluate(eval(READ_JS));
  await page.mouse.move(box.x + Math.min(box.width / 2, 40), box.y + Math.min(box.height / 2, 16));
  await page.mouse.down();
  await page.waitForTimeout(80);
  out.pressed = await loc.evaluate(eval(READ_JS));
  await page.mouse.up();
  await page.mouse.move(4, 4);
  return out;
}

const measurements = { capturedAt: new Date().toISOString(), viewport: { width: 1440, height: 900, dpr: 1 }, pages: {} };

const homeSpecs = [
  ['nav-link', 'a.nav-list-item'],
  ['nav-dropdown', '.dropdown-toggle'],
  ['button-sales', 'a.button[href="/contact-sales"]'],
  ['button-start', 'header a.button[href*="dashboard"], header a.button[href*="login"]'],
  ['hero-h1', 'h1'],
  ['tab', 'a.tab-menu-link'],
  ['footer-link', 'a.footer-link'],
  ['model-card', 'a[href^="/models/"]'],
];
console.log('home');
await open('https://fal.ai/');
measurements.pages.home = { url: page.url() };
for (const [id, sel] of homeSpecs) {
  measurements.pages.home[id] = await readState(sel);
  console.log(' ', id, measurements.pages.home[id].missing ? 'MISS' : measurements.pages.home[id].default?.text);
}

console.log('pricing');
await open('https://fal.ai/pricing');
measurements.pages.pricing = { url: page.url() };
for (const [id, sel] of [['pricing-h1', 'h1'], ['plan-card', '.pricing-card, .price-card, [class*="pricing"]'], ['plan-cta', 'a.button']]) {
  measurements.pages.pricing[id] = await readState(sel);
  console.log(' ', id, measurements.pages.pricing[id].missing ? 'MISS' : measurements.pages.pricing[id].default?.text);
}

console.log('login');
await open('https://fal.ai/login');
measurements.pages.login = { url: page.url() };
for (const [id, sel] of [
  ['oauth-github', 'a[href*="connect/github"]'],
  ['oauth-google', 'a[href*="connect/google"]'],
  ['oauth-microsoft', 'a[href*="connect/microsoft"]'],
  ['sso', 'button:has-text("Use SSO")'],
  ['login-h1', 'h1'],
  ['login-nav', 'header a, nav a'],
]) {
  measurements.pages.login[id] = await readState(sel);
  console.log(' ', id, measurements.pages.login[id].missing ? 'MISS' : measurements.pages.login[id].default?.text);
}

console.log('explore');
await open('https://fal.ai/explore');
measurements.pages.explore = { url: page.url() };
for (const [id, sel] of [
  ['search', 'input[type="search"], input[placeholder*="earch" i]'],
  ['filter', 'button, [role="tab"]'],
  ['card', 'a[href*="/models/"]'],
]) {
  measurements.pages.explore[id] = await readState(sel);
  console.log(' ', id, measurements.pages.explore[id].missing ? 'MISS' : (measurements.pages.explore[id].default?.text || 'field'));
}

console.log('docs');
await open('https://fal.ai/docs');
measurements.pages.docs = { url: page.url(), title: await page.title() };
measurements.pages.docs.h1 = await page.locator('h1').first().innerText().catch(() => null);

console.log('dark probe on explore');
const darkResolved = await page.evaluate(() => {
  document.documentElement.classList.add('dark');
  const root = getComputedStyle(document.documentElement);
  const names = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const r of list) {
        if (r.cssRules && !r.style) { try { walk(r.cssRules); } catch {} continue; }
        if (!r.style) continue;
        if ((r.selectorText || '') === '.dark' || (r.selectorText || '').startsWith('.dark ') || (r.selectorText || '').includes('.dark')) {
          for (let i = 0; i < r.style.length; i++) {
            const k = r.style[i];
            if (k.startsWith('--')) names.push(k);
          }
        }
      }
    };
    try { walk(rules); } catch {}
  }
  const uniq = [...new Set(names)];
  const resolved = {};
  for (const n of uniq) {
    const v = root.getPropertyValue(n).trim();
    if (v) resolved[n] = v.slice(0, 160);
  }
  const body = getComputedStyle(document.body);
  return {
    count: uniq.length,
    resolvedCount: Object.keys(resolved).length,
    colorScheme: root.colorScheme,
    bodyBg: body.backgroundColor,
    bodyColor: body.color,
    sample: {
      surface: root.getPropertyValue('--color-surface').trim(),
      content: root.getPropertyValue('--color-content-base').trim(),
      page: root.getPropertyValue('--surface-page').trim(),
      stroke: root.getPropertyValue('--color-stroke-base').trim(),
    },
    resolved,
  };
});
console.log(' dark names', darkResolved.count, 'resolved', darkResolved.resolvedCount, darkResolved.sample);
fs.writeFileSync(path.join(RAW, 'dark-resolved.json'), JSON.stringify(darkResolved, null, 2));

// Does the public explore UI offer a theme switch?
const themeSwitch = await page.evaluate(() => {
  const els = [...document.querySelectorAll('button, [role="switch"], a')];
  return els.filter(el => /theme|dark mode|light mode|appearance/i.test((el.innerText || '') + ' ' + (el.getAttribute('aria-label') || ''))).slice(0, 8).map(el => ({
    text: (el.innerText || el.getAttribute('aria-label') || '').trim().slice(0, 60),
    tag: el.tagName,
  }));
});
measurements.themeSwitchOnExplore = themeSwitch;
console.log(' theme switches', themeSwitch);

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(measurements, null, 2));

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
  ['tools', 'https://fal.ai/tools'],
  ['learn', 'https://fal.ai/learn'],
  ['careers', 'https://fal.ai/careers'],
];
for (const [name, url] of pages) {
  console.log('shot', name);
  await open(url);
  await shot(page, path.join(SHOTS, `${name}-light-default.png`), { dpr: 1, note: url });
  const H = await page.evaluate(() => document.documentElement.scrollHeight);
  if (H < 12000) await shot(page, path.join(SHOTS, `${name}-light-full.png`), { dpr: 1, fullPage: true, note: url + ' full ' + H });
  else console.log('  skip full H', H);
}

await open('https://fal.ai/');
await page.locator('.nav-list-item-dropdown.is-dropdown').filter({ hasText: 'Products' }).first().hover();
await page.waitForTimeout(500);
await shot(page, path.join(SHOTS, 'home-light-products-menu.png'), { dpr: 1, note: 'Products menu hover' });
await page.mouse.move(8, 700);
await page.waitForTimeout(200);
await page.locator('.nav-list-item-dropdown.is-dropdown').filter({ hasText: 'Resources' }).first().hover();
await page.waitForTimeout(500);
await shot(page, path.join(SHOTS, 'home-light-resources-menu.png'), { dpr: 1, note: 'Resources menu hover' });
await page.mouse.move(8, 700);
const tab = page.locator('a[role="tab"]').nth(1);
if (await tab.count()) {
  await tab.click({ modifiers: [] }).catch(() => {});
  // tab href is a hash; if it navigates, that is still the same page
  await page.waitForTimeout(400);
  if (page.url().startsWith('https://fal.ai/') && !page.url().includes('login')) {
    await shot(page, path.join(SHOTS, 'home-light-tab-serverless.png'), { dpr: 1, note: 'home tab 2' });
  }
}

await page.close();
await desk.close();

const mob = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
  hasTouch: true,
  userAgent: UA_MOBILE,
  locale: 'en-US',
});
const mp = await mob.newPage();
for (const [name, url] of [['home', 'https://fal.ai/'], ['pricing', 'https://fal.ai/pricing'], ['login', 'https://fal.ai/login'], ['explore', 'https://fal.ai/explore']]) {
  console.log('mobile', name);
  await mp.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await mp.waitForTimeout(1800);
  await mp.evaluate(hideConsent);
  await shot(mp, path.join(SHOTS, `mobile-${name}-light-default.png`), { dpr: 2, note: url });
}
await mp.goto('https://fal.ai/', { waitUntil: 'domcontentloaded' });
await mp.waitForTimeout(1500);
await mp.evaluate(hideConsent);
const navBtn = mp.locator('.w-nav-button');
console.log('mobile nav buttons', await navBtn.count());
if (await navBtn.count()) {
  await navBtn.first().click();
  await mp.waitForTimeout(600);
  await shot(mp, path.join(SHOTS, 'mobile-home-light-menu.png'), { dpr: 2, note: 'mobile nav open' });
}
await browser.close();
console.log('done shots', fs.readdirSync(SHOTS).filter(f => f.endsWith('.png')).length);
