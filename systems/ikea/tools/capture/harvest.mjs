// Harvest IKEA Singapore's declared CSS custom properties and component styles.
// Writes raw/css-vars.json and raw/components-computed.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node harvest.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const BASE = 'https://www.ikea.com/sg/en';

const noUrl = (v) => (typeof v === 'string'
  ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)')
  : v);

async function hide(page) {
  await page.addStyleTag({ content: '#onetrust-consent-sdk,#onetrust-banner-sdk,.onetrust-pc-dark-filter,#ot-sdk-btn-floating{display:none!important}' }).catch(() => {});
}

async function harvestVars(page) {
  // noUrl runs here in Node on what the page returns: a url() can carry a signed asset URL.
  const clean = (o) => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, noUrl(v)]));
  return page.evaluate(() => {
    const declared = {};
    const walk = (list) => {
      for (const r of list) {
        if (r.style) {
          for (const n of r.style) {
            if (n.startsWith('--') && declared[n] == null) declared[n] = r.style.getPropertyValue(n).trim();
          }
        }
        if (r.cssRules) { try { walk(r.cssRules); } catch { /* cross-sheet */ } }
      }
    };
    for (const s of document.styleSheets) { try { walk(s.cssRules); } catch { /* blocked */ } }
    const cs = getComputedStyle(document.documentElement);
    const resolved = {};
    for (const n of Object.keys(declared)) {
      const v = cs.getPropertyValue(n).trim();
      if (v) resolved[n] = v;
    }
    const body = getComputedStyle(document.body);
    return {
      declared,
      resolved,
      computed: {
        bodyFont: body.fontFamily,
        bodySize: body.fontSize,
        bodyWeight: body.fontWeight,
        bodyColor: body.color,
        bodyBg: body.backgroundColor,
        htmlBg: cs.backgroundColor,
      },
      url: location.href,
      title: document.title,
    };
  }).then((d) => ({ ...d, declared: clean(d.declared), resolved: clean(d.resolved) }));
}

const PROPS = ['backgroundColor', 'color', 'borderTopColor', 'borderTopWidth', 'borderTopStyle', 'borderRadius', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'boxShadow', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset'];

async function readEl(page, selector) {
  const loc = page.locator(selector).first();
  if (!(await loc.count())) return null;
  const vis = await loc.isVisible().catch(() => false);
  if (!vis) return null;
  return loc.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = cs[p];
    return {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 5).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      rect: { w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style,
    };
  }, PROPS);
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-SG',
});
const page = await context.newPage();
page.setDefaultTimeout(60000);

await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2500);
await hide(page);
const home = await harvestVars(page);

await page.goto(BASE + '/p/billy-bookcase-white-00522047/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2800);
await hide(page);
const pdpVars = await harvestVars(page);

const components = {};
async function shot(name, selector) {
  const reading = await readEl(page, selector);
  if (reading) components[name] = { selector, page: page.url(), ...reading };
  else console.log('miss', name, selector);
}

await shot('button-primary', 'button.pipf-btn--emphasised');
await shot('button-icon', 'button.pipf-favourite-button');
await shot('quantity', 'input[name="pipf-quantity-stepper-input"]');
await shot('search', 'input[name="q"]');
await shot('price', '[class*="pipcom-price"]');
await shot('product-title', 'h1');

// hover / focus on Add to cart, without clicking it
const add = page.locator('button.pipf-btn--emphasised').first();
if (await add.count()) {
  await add.hover();
  await page.waitForTimeout(250);
  components['button-primary-hover'] = await readEl(page, 'button.pipf-btn--emphasised');
  await page.mouse.move(2, 2);  // focus is read from rest, not on top of the hover
  await add.focus();
  await page.waitForTimeout(200);
  components['button-primary-focus'] = await readEl(page, 'button.pipf-btn--emphasised');
}
const search = page.locator('input[name="q"]').first();
if (await search.count()) {
  await search.focus();
  await page.waitForTimeout(200);
  components['search-focus'] = await readEl(page, 'input[name="q"]');
}

await page.goto(BASE + '/search/?q=lamp', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2500);
await hide(page);
await shot('product-card', '.plp-fragment-wrapper a[href*="/p/"], [data-testid="plp-product-card"], .plp-product-card, article a[href*="/p/"]');
await shot('filter-chip', 'button:has-text("Sort"), [class*="plp-filter"] button');

await page.goto(BASE + '/profile/login/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(2500);
await hide(page);
await shot('login-heading', 'h1');
await shot('login-field', 'input[type="email"], input[type="text"], input[name="email"]');
await shot('login-continue', 'button[type="submit"], button:has-text("Continue"), button:has-text("Log in")');

const declared = { ...home.declared, ...pdpVars.declared };
const resolved = { ...home.resolved, ...pdpVars.resolved };
const out = {
  captured: '2026-11-19',
  locale: 'sg/en',
  source: 'www.ikea.com/sg/en/ stylesheets, declared custom properties, resolved on documentElement',
  pages: [home.url, pdpVars.url],
  computed: pdpVars.computed,
  declaredCount: Object.keys(declared).length,
  resolvedCount: Object.keys(resolved).length,
  declared,
  resolved,
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({
  captured: '2026-11-19',
  locale: 'sg/en',
  note: 'Add to cart, login submit, and consent buttons were measured or skipped, never activated.',
  components,
}, null, 1) + '\n');
console.log('vars', Object.keys(declared).length, 'resolved', Object.keys(resolved).length, 'components', Object.keys(components).join(','));
await browser.close();
