// Measure Unsplash public controls. Headed Chromium. No form submit, no typed email.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, RAW, REF, launch, open, styleOf } from './lib.mjs';

const CROPS = path.join(REF, 'components', 'crops');
fs.mkdirSync(CROPS, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

const components = {};

async function crop(loc, name) {
  const box = await loc.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 900),
    height: Math.min(box.height + pad * 2, 500),
  };
  const file = `${name}.png`;
  await page.screenshot({ path: path.join(CROPS, file), clip });
  return file;
}

async function forcePseudo(loc) {
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
  await page.waitForTimeout(250);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function measure(key, state, loc, via) {
  const target = loc.first();
  if (!(await target.count())) {
    components[key] = components[key] || { missing: true, states: {} };
    components[key].states[state] = { error: 'missing' };
    console.log('  missing', key, state);
    return;
  }
  await target.scrollIntoViewIfNeeded().catch(() => {});
  const s = await styleOf(target);
  let file = null;
  try { file = await crop(target, `${key}-${state}`); } catch (e) { s.cropError = String(e.message).slice(0, 80); }
  const c = components[key] ??= { title: key, states: {}, page: page.url().split('?')[0] };
  c.states[state] = { ...s, crop: file, via };
  console.log(' ', key, state, s.rect.w + 'x' + s.rect.h, s.style.backgroundColor, s.style.color, s.style.fontSize);
}

async function states(key, loc) {
  const target = loc.first();
  await measure(key, 'default', target, 'at rest');
  if (!(await target.count())) return;
  await target.hover().catch(() => {});
  await page.waitForTimeout(300);
  await measure(key, 'hover', target, 'mouse hover');
  await target.focus().catch(() => {});
  await page.waitForTimeout(200);
  await measure(key, 'focus-visible', target, 'focus()');
  const undo = await forcePseudo(target);
  await measure(key, 'pressed', target, 'CDP forcePseudoState :active:hover');
  await undo();
  await page.mouse.move(2, 2);
}

console.log('home');
await open(page, BASE + '/');
await states('search-field', page.locator('input[name="searchKeyword"]'));
await states('submit-button', page.getByRole('button', { name: 'Submit an image' }));
await states('plus-link', page.getByRole('link', { name: 'Get Unsplash+' }));
await states('login-link', page.getByRole('link', { name: 'Log in', exact: true }));
await states('menu-button', page.getByRole('button', { name: 'Menu', exact: true }));
await states('topic-chip', page.locator('a[href="/t/nature"]').first());
await states('photo-card', page.locator('a[href*="/photos/"]').first());

await page.getByRole('button', { name: 'Menu', exact: true }).click();
await page.waitForTimeout(500);
await states('menu-link', page.getByRole('link', { name: 'About', exact: true }));
await page.keyboard.press('Escape');

await page.locator('input[name="searchKeyword"]').first().click();
await page.waitForTimeout(500);
await measure('search-suggestion', 'default', page.locator('[role="listbox"] a, [role="option"]').first(), 'search focused, not submitted');
await page.keyboard.press('Escape');

console.log('login');
await open(page, BASE + '/login');
await measure('email-field', 'default', page.locator('input[name="email"]'), 'at rest, empty, not typed');
await measure('password-field', 'default', page.locator('input[name="password"]'), 'at rest, empty, not typed');
await states('login-submit', page.getByRole('button', { name: 'Login', exact: true }));

console.log('plus');
await open(page, BASE + '/plus');
await states('plus-cta', page.getByRole('link', { name: /get unsplash\+|upgrade|subscribe/i }).first());

fs.writeFileSync(OUT, JSON.stringify({ read: new Date().toISOString().slice(0, 10), components }, null, 1) + '\n');
console.log('wrote', OUT, Object.keys(components).length);
await browser.close();
