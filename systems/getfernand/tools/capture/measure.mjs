// Measure public Fernand controls and write raw/components-computed.json.
// PLAYWRIGHT=... node tools/capture/measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, launch, hideBanners } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const PROPS = [
  'display', 'position', 'width', 'height', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'gap', 'borderRadius', 'borderTopWidth', 'borderTopColor', 'borderTopStyle',
  'backgroundColor', 'color', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'boxShadow', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset', 'textDecorationLine',
];

async function read(page, locator) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  return handle.evaluate((el, props) => {
    const c = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { tag: el.tagName, text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60), box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
    for (const p of props) o[p] = c[p];
    return o;
  }, PROPS);
}

const { browser, context } = await launch();
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2000);
await hideBanners(page);

const specs = [
  ['button-primary', page.getByRole('link', { name: 'Start for free' }).first()],
  ['button-demo', page.locator('[data-cal-link]').first()],
  ['link-nav', page.getByRole('link', { name: 'Pricing' }).first()],
  ['link-login', page.getByRole('link', { name: 'Log in' }).first()],
  ['hero-title', page.locator('h1').first()],
];

const out = { source: BASE + '/', capturedAt: new Date().toISOString(), components: {} };
for (const [name, loc] of specs) {
  const def = await read(page, loc);
  let hover = null, focus = null;
  try {
    await loc.hover({ timeout: 3000 });
    await page.waitForTimeout(200);
    hover = await read(page, loc);
  } catch (e) { hover = { error: e.message.split('\n')[0] }; }
  try {
    await loc.focus();
    await page.waitForTimeout(150);
    focus = await read(page, loc);
  } catch (e) { focus = { error: e.message.split('\n')[0] }; }
  out.components[name] = { default: def, hover, focusVisible: focus };
  console.log(name, def?.fontSize, def?.backgroundColor, def?.color, def?.borderRadius);
}

// Pricing page plan cards and FAQ if present.
await page.goto(BASE + '/pricing/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(1800);
const pricing = await page.evaluate((props) => {
  const cards = [...document.querySelectorAll('h2, h3, [class*="plan"], [class*="price"]')].slice(0, 8).map((el) => {
    const c = getComputedStyle(el);
    return { tag: el.tagName, text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40), fontSize: c.fontSize, color: c.color, backgroundColor: c.backgroundColor };
  });
  const buttons = [...document.querySelectorAll('a, button')].filter((el) => /start|free|demo/i.test(el.innerText || '')).slice(0, 4).map((el) => {
    const c = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40), box: { w: Math.round(r.width), h: Math.round(r.height) } };
    for (const p of props) o[p] = c[p];
    return o;
  });
  return { cards, buttons };
}, PROPS);
out.pricing = pricing;

fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'components-computed.json'), JSON.stringify(out, null, 2) + '\n');
console.log('wrote components', Object.keys(out.components).length);
await browser.close();
