// Measures LinkedIn's public guest components. Nothing is submitted.
// A login or signup wall is recorded and that page stops.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { chromium, UA, UA_MOBILE, BASE, isWall, PROPS } from './lib.mjs';
import { screenshotWithMetadata } from '../screenshot.mjs';

const RAW = process.env.RAW || path.resolve(new URL('.', import.meta.url).pathname, '..', '..', '..', 'raw');
const CROPS = process.env.CROPS || path.resolve(new URL('.', import.meta.url).pathname, '..', '..', '..', 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const out = { _meta: { captured: '2026-11-21', product: 'linkedin', route: 'public' }, components: {} };

function save() {
  fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
}

async function read(page, selector) {
  return page.evaluate(({ selector, props }) => {
    const el = document.querySelector(selector);
    if (!el) return null;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return null;
    const style = {};
    for (const k of props) style[k] = cs[k];
    return {
      selector,
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      rect: { x: r.x, y: r.y, width: r.width, height: r.height },
      style,
    };
  }, { selector, props: PROPS });
}

async function crop(page, selector, name, dpr) {
  const box = await page.locator(selector).first().boundingBox();
  if (!box) return null;
  const pad = 8;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440),
    height: Math.min(box.height + pad * 2, 400),
  };
  const file = path.join(CROPS, name + '.png');
  await screenshotWithMetadata(page, { path: file, clip }, {
    viewport: page.viewportSize(),
    deviceScaleFactor: dpr,
  });
  return 'components/crops/' + name + '.png';
}

async function force(cdp, page, selector, pseudo) {
  await page.evaluate((selector) => {
    document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force'));
    document.querySelector(selector)?.setAttribute('data-m-force', '1');
  }, selector);
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: pseudo });
  await page.waitForTimeout(200);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

const specs = [
  { key: 'button-primary', page: 'https://www.linkedin.com/', selector: 'a.btn-primary', states: ['default', 'hover', 'focus-visible', 'active'] },
  { key: 'button-secondary', page: 'https://www.linkedin.com/', selector: 'a.btn-secondary-emphasis', states: ['default', 'hover', 'focus-visible'] },
  { key: 'button-email', page: 'https://www.linkedin.com/', selector: 'a.sign-in-form__sign-in-cta', states: ['default', 'hover'] },
  { key: 'link', page: 'https://www.linkedin.com/', selector: 'a[href*="/legal/user-agreement"]', states: ['default', 'hover'] },
  { key: 'heading', page: 'https://www.linkedin.com/', selector: 'h1', states: ['default'] },
  { key: 'chip', page: 'https://www.linkedin.com/', selector: 'a[href*="/top-content/career"]', states: ['default', 'hover'] },
  { key: 'text-field', page: 'https://www.linkedin.com/login', selector: 'input[type="email"], input[name="session_key"]', states: ['default', 'focus'], wall: true },
  { key: 'checkbox', page: 'https://www.linkedin.com/login', selector: 'input[type="checkbox"]', states: ['default'], wall: true },
  { key: 'button-signin', page: 'https://www.linkedin.com/login', selector: 'button[type="submit"]', states: ['default', 'hover'], wall: true },
  { key: 'card', page: 'https://www.linkedin.com/games', selector: 'a[href*="/games/zip"]', states: ['default', 'hover'] },
  { key: 'search', page: 'https://www.linkedin.com/learning/', selector: 'input[placeholder*="Search skills"]', states: ['default', 'focus'] },
  { key: 'tab', page: 'https://www.linkedin.com/learning/', selector: '[role="tab"]', states: ['default'] },
  { key: 'help-search', page: 'https://www.linkedin.com/help/linkedin', selector: 'input[name="q"]', states: ['default', 'focus'] },
];

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  userAgent: UA,
  locale: 'en-US',
  colorScheme: 'light',
});
const page = await ctx.newPage();
const cdp = await ctx.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

let current = '';
for (const spec of specs) {
  if (current !== spec.page) {
    await page.goto(spec.page, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(1800);
    current = spec.page;
    const wall = isWall(page.url());
    if (wall && !spec.wall) {
      console.log('WALL skip', spec.key, page.url());
      continue;
    }
  }
  const entry = out.components[spec.key] = {
    page: spec.page,
    selector: spec.selector,
    wall: !!spec.wall,
    states: {},
  };
  for (const state of spec.states) {
    let release = async () => {};
    try {
      if (state === 'hover') release = await force(cdp, page, spec.selector, ['hover']);
      else if (state === 'focus-visible') release = await force(cdp, page, spec.selector, ['focus', 'focus-visible']);
      else if (state === 'active') release = await force(cdp, page, spec.selector, ['active']);
      else if (state === 'focus') {
        await page.locator(spec.selector).first().focus().catch(() => {});
        await page.waitForTimeout(200);
      }
      const reading = await read(page, spec.selector);
      if (!reading) {
        entry.states[state] = { missing: true };
        console.log('  miss', spec.key, state);
        continue;
      }
      const cropPath = await crop(page, spec.selector, `${spec.key}-${state}`, 2);
      entry.states[state] = { ...reading, crop: cropPath };
      console.log('  ok', spec.key, state, reading.style.backgroundColor, reading.style.color, reading.style.fontSize);
    } catch (e) {
      entry.states[state] = { error: String(e.message).split('\n')[0] };
      console.log('  fail', spec.key, state, e.message.split('\n')[0]);
    } finally {
      await release();
    }
  }
  save();
}

// Layout readings
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(1200);
const layout = await page.evaluate(() => {
  const cs = getComputedStyle(document.body);
  const h1 = document.querySelector('h1');
  const hcs = h1 ? getComputedStyle(h1) : null;
  return {
    viewport: { width: innerWidth, height: innerHeight, dpr: devicePixelRatio },
    body: { color: cs.color, background: cs.backgroundColor, font: cs.fontFamily, size: cs.fontSize, lineHeight: cs.lineHeight },
    h1: hcs && { color: hcs.color, size: hcs.fontSize, weight: hcs.fontWeight, lineHeight: hcs.lineHeight, font: hcs.fontFamily },
  };
});
fs.writeFileSync(path.join(RAW, 'layout.json'), JSON.stringify(layout, null, 2) + '\n');
save();
await browser.close();
console.log('measured', Object.keys(out.components).length);
