// Measures slack.com public components. Nothing is submitted.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, hideConsent, crop } from './lib.mjs';

const RAW = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');

const PICK = ['color', 'backgroundColor', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'borderTopLeftRadius', 'borderTopWidth', 'borderTopColor', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'height', 'minHeight', 'boxShadow', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset', 'textTransform', 'opacity'];

function pack(style, rect) {
  const o = {};
  for (const k of PICK) o[k] = style[k];
  o.rect = rect && { x: Math.round(rect.x), y: Math.round(rect.y), w: Math.round(rect.width), h: Math.round(rect.height) };
  return o;
}

async function read(page, locator) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  const data = await handle.evaluate((el, keys) => {
    const cs = getComputedStyle(el);
    const o = {};
    for (const k of keys) o[k] = cs[k];
    const r = el.getBoundingClientRect();
    o.rect = { x: r.x, y: r.y, width: r.width, height: r.height };
    o.text = (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    o.tag = el.tagName;
    return o;
  }, PICK);
  await handle.dispose();
  return data;
}

async function forcePseudo(page, cdp, locator, classes) {
  await locator.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(200);
  return async () => {
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
    await locator.evaluate((el) => el.removeAttribute('data-m-force')).catch(() => {});
  };
}

const out = { readAt: new Date().toISOString().slice(0, 10), source: BASE, components: {} };

async function measure(page, cdp, key, locator, states) {
  const entry = { states: {}, text: '' };
  const vis = await locator.count();
  if (!vis) { entry.miss = 'not found'; out.components[key] = entry; return; }
  const loc = locator.first();
  try { await loc.scrollIntoViewIfNeeded({ timeout: 4000 }); } catch { /* offscreen ok if already visible */ }
  const box = await loc.boundingBox();
  if (!box || box.width < 2) { entry.miss = 'no box'; out.components[key] = entry; return; }
  for (const state of states) {
    let undo = async () => {};
    try {
      if (state === 'hover') undo = await forcePseudo(page, cdp, loc, ['hover']);
      else if (state === 'focus-visible') undo = await forcePseudo(page, cdp, loc, ['focus', 'focus-visible']);
      else if (state === 'pressed') undo = await forcePseudo(page, cdp, loc, ['active']);
      else if (state === 'focused') {
        await loc.focus();
        await page.waitForTimeout(150);
      }
      const data = await read(page, loc);
      if (!data) { entry.states[state] = { miss: true }; continue; }
      entry.text = data.text;
      entry.tag = data.tag;
      entry.states[state] = pack(data, data.rect);
      if (state === 'default' || state === 'hover' || state === 'opened') {
        const cropName = `${key}-${state}`;
        entry.states[state].crop = await crop(page, loc, cropName);
      }
    } catch (e) {
      entry.states[state] = { error: String(e.message).split('\n')[0] };
    } finally {
      await undo();
    }
  }
  out.components[key] = entry;
  console.log(key, entry.text.slice(0, 40), Object.keys(entry.states).join(','));
}

const { browser, context } = await launch();
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);
await hideConsent(page);

const specs = [
  ['button-primary', page.getByRole('link', { name: 'GET STARTED' }).nth(1), ['default', 'hover', 'focus-visible', 'pressed']],
  ['button-secondary', page.getByRole('link', { name: /FIND YOUR SUBSCRIPTION/i }).first(), ['default', 'hover', 'focus-visible', 'pressed']],
  ['button-outline', page.getByRole('link', { name: /REQUEST A DEMO/i }).first(), ['default', 'hover', 'focus-visible', 'pressed']],
  ['link-nav', page.getByRole('link', { name: 'Pricing', exact: true }).first(), ['default', 'hover', 'focus-visible']],
  ['link-signin', page.getByRole('link', { name: 'Sign in', exact: true }).first(), ['default', 'hover', 'focus-visible']],
  ['menu-trigger', page.getByRole('button', { name: 'Product', exact: true }).first(), ['default', 'hover', 'focus-visible']],
  ['search-button', page.locator('#nav_search_btn'), ['default', 'hover', 'focus-visible']],
  ['heading-display', page.locator('h1').first(), ['default']],
  ['body-lead', page.locator('h1').first().locator('xpath=following::p[1]'), ['default']],
];
for (const [key, loc, states] of specs) await measure(page, cdp, key, loc, states);

await page.getByRole('button', { name: 'Product', exact: true }).first().click();
await page.waitForTimeout(600);
await measure(page, cdp, 'menu-link', page.getByRole('link', { name: /Channels/ }).first(), ['default', 'hover', 'opened']);
await page.keyboard.press('Escape');

await page.locator('#nav_search_btn').click();
await page.waitForTimeout(400);
await measure(page, cdp, 'search-field', page.getByRole('textbox', { name: /search/i }).first(), ['default', 'focused']);
await page.keyboard.press('Escape');

// pricing
await page.goto(BASE + '/pricing', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);
await hideConsent(page);
await measure(page, cdp, 'plan-card', page.locator('main').getByRole('heading', { level: 2 }).first(), ['default']);
const toggle = page.getByRole('button', { name: /monthly|annual|yearly/i }).first();
await measure(page, cdp, 'billing-toggle', toggle, ['default', 'hover']);
const faq = page.getByRole('button').filter({ hasText: /\?/ }).first();
await measure(page, cdp, 'faq-item', faq, ['default']);
if (await faq.count()) {
  try {
    await faq.click({ timeout: 4000 });
    await page.waitForTimeout(400);
    await measure(page, cdp, 'faq-open', faq, ['opened']);
  } catch (e) { out.components['faq-open'] = { miss: String(e.message).split('\n')[0] }; }
}

// contact sales fields, measure only, do not type or submit
await page.goto(BASE + '/contact-sales', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);
await hideConsent(page);
const field = page.locator('input:visible, textarea:visible').first();
await measure(page, cdp, 'text-field', field, ['default', 'focused']);
const area = page.locator('textarea:visible').first();
await measure(page, cdp, 'text-area', area, ['default']);
const select = page.locator('select:visible').first();
await measure(page, cdp, 'select', select, ['default']);

// phone menu
await page.close();
const mctx = await browser.newContext({
  viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true,
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
  locale: 'en-US',
});
const mp = await mctx.newPage();
const mcdp = await mctx.newCDPSession(mp);
await mcdp.send('DOM.enable');
await mcdp.send('CSS.enable');
await mp.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await mp.waitForTimeout(2000);
await hideConsent(mp);
await measure(mp, mcdp, 'icon-button-menu', mp.locator('#nav_menu_btn'), ['default']);
await mp.locator('#nav_menu_btn').click();
await mp.waitForTimeout(600);
await measure(mp, mcdp, 'mobile-menu-link', mp.getByRole('link', { name: 'Pricing', exact: true }).last(), ['default', 'opened']);
await measure(mp, mcdp, 'mobile-cta', mp.getByRole('link', { name: 'GET STARTED' }).last(), ['default']);

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT, Object.keys(out.components).length, 'components');
await browser.close();
