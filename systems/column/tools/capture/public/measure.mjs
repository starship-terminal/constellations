// Measure Column public components. Never types into a field, never submits, never clicks OAuth.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..', '..');
const CROPS = path.join(REF, 'components', 'crops');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

function styleOf(s) {
  const pick = (k) => s[k];
  return {
    color: pick('color'),
    backgroundColor: pick('backgroundColor'),
    borderTopColor: pick('borderTopColor'),
    borderTopWidth: pick('borderTopWidth'),
    borderRadius: pick('borderRadius'),
    fontFamily: pick('fontFamily'),
    fontSize: pick('fontSize'),
    fontWeight: pick('fontWeight'),
    lineHeight: pick('lineHeight'),
    letterSpacing: pick('letterSpacing'),
    padding: pick('padding'),
    height: pick('height'),
    boxShadow: pick('boxShadow'),
    outline: pick('outline'),
    outlineOffset: pick('outlineOffset'),
    textDecoration: pick('textDecorationLine'),
  };
}

const PROPS = Object.keys(styleOf({
  color: 1, backgroundColor: 1, borderTopColor: 1, borderTopWidth: 1, borderRadius: 1,
  fontFamily: 1, fontSize: 1, fontWeight: 1, lineHeight: 1, letterSpacing: 1, padding: 1,
  height: 1, boxShadow: 1, outline: 1, outlineOffset: 1, textDecorationLine: 1,
}));

async function read(loc) {
  const box = await loc.boundingBox();
  const computed = await loc.evaluate((el, props) => {
    const s = getComputedStyle(el);
    const o = {};
    for (const k of props) o[k] = s[k];
    const r = el.getBoundingClientRect();
    return { style: o, box: { x: r.x, y: r.y, w: r.width, h: r.height } };
  }, PROPS);
  return { box, ...computed };
}

async function crop(page, loc, file) {
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 8;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  await page.screenshot({ path: file, clip });
  return box;
}

async function hideCookie(page) {
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('div, section, aside')) {
      const t = el.innerText || '';
      if (/cookie/i.test(t) && /accept/i.test(t) && el.getBoundingClientRect().height > 30 && el.getBoundingClientRect().height < 280) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}

const browser = await chromium.launch();
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, locale: 'en-US' });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');
const out = { _meta: { source: 'column.com signed-out, 1440x900, 2026-11-21', note: 'No field was typed into. No form was submitted. Login wall was not measured as a form.' }, components: {} };

async function record(name, state, loc, extra = {}) {
  const data = await read(loc);
  const file = path.join(CROPS, `${name}-${state}.png`);
  await crop(page, loc, file);
  out.components[name] ??= { states: {} };
  out.components[name].states[state] = { ...data, ...extra, crop: `components/crops/${name}-${state}.png` };
  console.log(' ', name, state, Math.round(data.box?.w || 0), Math.round(data.box?.h || 0), data.style.fontSize, data.style.backgroundColor, data.style.color);
}

async function states(name, loc) {
  await loc.scrollIntoViewIfNeeded();
  await page.waitForTimeout(200);
  await record(name, 'default', loc);
  await loc.hover();
  await page.waitForTimeout(350);
  await record(name, 'hover', loc);
  await page.mouse.move(2, 2);
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(250);
  await record(name, 'focus-visible', loc);
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (nodeId) {
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['hover', 'active'] });
    await page.waitForTimeout(200);
    await record(name, 'pressed', loc, { how: 'CDP forcePseudoState hover+active; nothing was clicked' });
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
  }
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur());
}

await page.goto('https://column.com/', { waitUntil: 'load', timeout: 90000 });
await page.waitForTimeout(1600);
await hideCookie(page);

await states('nav-signin', page.getByRole('link', { name: 'Sign in' }).first());
await states('nav-blog', page.getByRole('link', { name: 'Blog', exact: true }).first());
await states('nav-products', page.getByRole('button', { name: 'Products', exact: true }).first());

const products = page.getByRole('button', { name: 'Products', exact: true }).first();
await products.click({ force: true });
await page.waitForTimeout(400);
const ach = page.getByRole('link', { name: 'ACH', exact: true }).first();
await record('nav-products-item', 'opened', ach, { menu: 'Products opened; item is the ACH link' });
await page.keyboard.press('Escape');

const signup = page.getByRole('link', { name: 'Sign up' }).first();
await signup.scrollIntoViewIfNeeded();
await states('cta-signup', signup);

const h1 = page.locator('h1').first();
await h1.scrollIntoViewIfNeeded();
await record('hero-title', 'default', h1);

await page.goto('https://column.com/contact/', { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(1200);
await hideCookie(page);
const field = page.locator('#contact-first-name');
await field.scrollIntoViewIfNeeded();
await record('contact-field', 'default', field);
await field.focus();
await page.waitForTimeout(250);
await record('contact-field', 'focused', field, { note: 'focused empty; nothing typed' });
await page.evaluate(() => document.activeElement && document.activeElement.blur());
const area = page.locator('#contact-building');
await area.scrollIntoViewIfNeeded();
await record('contact-message', 'default', area);
const submit = page.locator('button[type="submit"]').first();
await record('contact-submit', 'default', submit, { note: 'not clicked' });

await page.goto('https://docs.column.com/', { waitUntil: 'load', timeout: 60000 });
await page.waitForTimeout(1500);
const search = page.getByRole('button', { name: /^Search/ }).first();
if (await search.count()) {
  await record('docs-search', 'default', search);
  await search.click();
  await page.waitForTimeout(500);
  const dialog = page.locator('[role="dialog"]').first();
  if (await dialog.count()) await record('docs-search-dialog', 'opened', dialog, { note: 'search opened; nothing typed' });
  await page.keyboard.press('Escape');
}
const theme = page.getByRole('button', { name: 'Toggle theme' }).first();
if (await theme.count()) await record('docs-theme-toggle', 'default', theme);

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote', Object.keys(out.components).length, 'components');
await browser.close();
