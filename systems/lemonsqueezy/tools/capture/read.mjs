// Read Lemon Squeezy's public pages. Writes raw/readings.json.
// Nothing is typed, submitted, or signed into. Identity-provider links are not clicked.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/read.mjs

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..', '..');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PAGES = [
  ['home', 'https://www.lemonsqueezy.com/'],
  ['pricing', 'https://www.lemonsqueezy.com/pricing'],
  ['about', 'https://www.lemonsqueezy.com/about'],
  ['help', 'https://www.lemonsqueezy.com/help'],
  ['docs', 'https://docs.lemonsqueezy.com/'],
  ['login', 'https://auth.lemonsqueezy.com/login'],
];

const PROPS = [
  'color', 'backgroundColor', 'backgroundImage', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'width', 'gap',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset', 'textDecorationLine',
  'transitionDuration', 'transitionTimingFunction', 'opacity',
];

function rgbToHex(c) {
  const m = String(c).match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/);
  if (!m) return c;
  const hex = [m[1], m[2], m[3]].map((n) => Number(n).toString(16).padStart(2, '0')).join('');
  const a = m[4] === undefined ? 1 : Number(m[4]);
  if (a === 0) return 'transparent';
  if (a < 1) return `#${hex}${Math.round(a * 255).toString(16).padStart(2, '0')}`;
  return `#${hex}`;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  locale: 'en-US',
});
const page = await context.newPage();
page.setDefaultTimeout(20000);

const readings = { captured: '2026-11-21', pages: {}, vars: {}, fonts: [], brand: {}, counts: {} };

for (const [name, url] of PAGES) {
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1500);
  const data = await page.evaluate(({ PROPS }) => {
    const styles = [...document.styleSheets];
    const vars = {};
    const fonts = [];
    const errors = [];
    for (const ss of styles) {
      let rules;
      try { rules = ss.cssRules; } catch (e) { errors.push(String(e).slice(0, 120)); continue; }
      const walk = (list, ctx) => {
        if (!list) return;
        for (const r of list) {
          if (r.type === CSSRule.FONT_FACE_RULE) {
            fonts.push({
              family: r.style.getPropertyValue('font-family'),
              weight: r.style.getPropertyValue('font-weight'),
              style: r.style.getPropertyValue('font-style'),
              src: (r.style.getPropertyValue('src') || '').slice(0, 180),
            });
            continue;
          }
          if (r.cssRules && !r.style) { walk(r.cssRules, ctx.concat(r.cssText.split('{')[0].trim().slice(0, 80))); continue; }
          if (!r.style) continue;
          const props = {};
          for (let i = 0; i < r.style.length; i++) {
            const k = r.style[i];
            if (k.startsWith('--')) props[k] = r.style.getPropertyValue(k).trim();
          }
          if (Object.keys(props).length) {
            const key = (ctx.join(' ') + ' ' + r.selectorText).trim();
            vars[key] = props;
          }
          if (r.cssRules) walk(r.cssRules, ctx.concat(r.selectorText));
        }
      };
      walk(rules, []);
    }
    const brand = {
      themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
      tile: document.querySelector('meta[name="msapplication-TileColor"]')?.content || null,
      mask: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
      manifest: document.querySelector('link[rel="manifest"]')?.href || null,
    };
    const rootStyle = getComputedStyle(document.documentElement);
    const rootVars = {};
    for (const k of ['--swatch--brand', '--swatch--brand-2', '--swatch--dark', '--swatch--light']) {
      const v = rootStyle.getPropertyValue(k);
      if (v) rootVars[k] = v.trim();
    }
    return {
      statusNote: document.title,
      url: location.href,
      brand, rootVars, varRuleCount: Object.keys(vars).length, vars, fonts, errors: errors.slice(0, 6),
      htmlClass: document.documentElement.className,
    };
  }, { PROPS });
  readings.pages[name] = { url: data.url, title: data.statusNote, status: res.status(), htmlClass: data.htmlClass, varRuleCount: data.varRuleCount, stylesheetErrors: data.errors };
  if (name === 'home' || name === 'login') {
    readings.vars[name] = data.vars;
    readings.fonts.push(...data.fonts);
    readings.brand[name] = data.brand;
    Object.assign(readings.brand, { rootVars: { ...(readings.brand.rootVars || {}), ...data.rootVars } });
  }
  console.log(name, res.status(), data.url, 'varRules', data.varRuleCount, 'fontFaces', data.fonts.length);
}

// Component measurements on home, pricing, help dialog, login.
async function measure(sel, stateLabel) {
  return page.evaluate(({ sel, PROPS }) => {
    const el = document.querySelector(sel);
    if (!el) return { miss: sel };
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { selector: sel, text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60), box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
    for (const p of PROPS) o[p] = s[p];
    return o;
  }, { sel, PROPS });
}

const components = {};
async function record(pageName, key, sel) {
  const row = await measure(sel);
  row.page = pageName;
  components[key] = row;
  console.log('  ', key, row.miss || row.fontSize, row.backgroundColor, row.color);
}

await page.goto('https://www.lemonsqueezy.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1200);
const homeSels = {
  'banner': '.banner, [class*="banner"]',
  'nav': '.nav_component, .w-nav',
  'nav-link': '.nav_link',
  'button-primary': '.button, a.button',
  'hero-title': 'h1',
  'body': 'body',
  'footer-link': 'footer a, .footer a',
};
// Discover real selectors first.
const discovered = await page.evaluate(() => {
  const pick = (sel) => {
    const el = document.querySelector(sel);
    if (!el) return null;
    return { sel, className: String(el.className).slice(0, 80), tag: el.tagName };
  };
  const candidates = ['header', 'nav', '.w-nav', '.nav_component', 'h1', 'a.button', '.button', '.nav_link', '.banner_component', '.announcement', 'body', 'footer', '.footer_component'];
  return candidates.map(pick).filter(Boolean);
});
readings.discoveredHome = discovered;
console.log('discovered', JSON.stringify(discovered));

// Use the classes we already saw in the live DOM.
const homeMap = [
  ['banner', 'a[href*="saying-goodbye"]'],
  ['logo', 'a[aria-label="home"]'],
  ['nav-link', 'a[href="https://docs.lemonsqueezy.com/"]'],
  ['button-primary', 'a[href*="dashboard.stripe.com"]'],
  ['hero-title', 'h1'],
  ['hero-body', 'h1 + p, h1 ~ p'],
  ['button-white', 'a[href="https://stripe.com/managed-payments"]'],
  ['footer-link', 'a[href="/privacy"]'],
];
for (const [k, sel] of homeMap) await record('home', k, sel);

// hover and focus on the primary button, without navigation
const primary = page.locator('a[href*="dashboard.stripe.com"]').first();
await primary.hover();
await page.waitForTimeout(400);
components['button-primary-hover'] = await measure('a[href*="dashboard.stripe.com"]');
components['button-primary-hover'].state = 'hover';
await page.keyboard.press('Escape');
await primary.focus();
await page.waitForTimeout(200);
components['button-primary-focus'] = await measure('a[href*="dashboard.stripe.com"]');
components['button-primary-focus'].state = 'focus';

await page.goto('https://www.lemonsqueezy.com/pricing', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1200);
for (const [k, sel] of [
  ['pricing-title', 'h1'],
  ['pricing-fee', 'h2'],
  ['switch', 'input[type="checkbox"]'],
  ['slider', 'input[type="range"]'],
  ['faq-open', '.accordion_item'],
  ['faq-question', '.accordion_item'],
]) await record('pricing', k, sel);

await page.goto('https://www.lemonsqueezy.com/help', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1000);
await page.getByRole('link', { name: 'Message us' }).click();
await page.waitForTimeout(800);
for (const [k, sel] of [
  ['dialog', '[role="dialog"], .w-form, form'],
  ['dialog-title', 'h2, .modal h3, [class*="modal"] h2, [class*="popup"] h3'],
  ['field', 'input[type="text"], input[name="name"], input'],
  ['dialog-submit', 'button[type="submit"], input[type="submit"]'],
]) await record('help', k, sel);
// close without submit
await page.keyboard.press('Escape');

await page.goto('https://auth.lemonsqueezy.com/login', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1200);
for (const [k, sel] of [
  ['login-title', 'h1'],
  ['login-field', 'input[type="email"]'],
  ['login-submit', 'button[type="submit"]'],
  ['login-oauth', 'a[href*="google"]'],
  ['login-body', 'body'],
]) await record('login', k, sel);

// colour census on home
await page.goto('https://www.lemonsqueezy.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(800);
readings.counts = await page.evaluate(() => {
  const colors = {};
  const sizes = {};
  const radii = {};
  const all = document.querySelectorAll('body *');
  let n = 0;
  for (const el of all) {
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) continue;
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') continue;
    n++;
    const bump = (map, k) => { if (!k) return; map[k] = (map[k] || 0) + 1; };
    bump(colors, s.color);
    bump(colors, s.backgroundColor);
    bump(sizes, s.fontSize);
    bump(radii, s.borderRadius);
    if (n > 2500) break;
  }
  const top = (map) => Object.entries(map).sort((a, b) => b[1] - a[1]).slice(0, 24);
  return { sampled: n, colors: top(colors), sizes: top(sizes), radii: top(radii) };
});

// motion from stylesheets we can read
readings.motion = await page.evaluate(() => {
  const durs = new Set();
  const easings = new Set();
  for (const ss of document.styleSheets) {
    let rules;
    try { rules = ss.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const r of list || []) {
        if (r.cssRules && !r.style) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const d = r.style.transitionDuration || r.style.getPropertyValue('transition-duration');
        const e = r.style.transitionTimingFunction || r.style.getPropertyValue('transition-timing-function');
        if (d) durs.add(d);
        if (e) easings.add(e);
        if (r.cssRules) walk(r.cssRules);
      }
    };
    walk(rules);
  }
  return { durations: [...durs].slice(0, 30), easings: [...easings].slice(0, 20) };
});

readings.components = components;
fs.writeFileSync(path.join(RAW, 'readings.json'), JSON.stringify(readings, null, 2));
console.log('wrote', path.join(RAW, 'readings.json'));
await browser.close();
