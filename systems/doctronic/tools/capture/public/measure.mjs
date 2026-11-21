// Measure doctronic.ai public controls. Never type, submit, or click SSO / Get Login Code.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, BASE, UA } from './lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..', '..');
const OUT = path.join(REF, 'raw', 'components-computed.json');
const CROPS = path.join(REF, 'components', 'crops');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(path.dirname(OUT), { recursive: true });

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

function pick(cs) {
  const keys = ['color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderRadius', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'width', 'boxShadow', 'outline', 'textDecorationLine'];
  const o = {};
  for (const k of keys) o[k] = cs[k];
  return o;
}

async function read(locator) {
  return locator.evaluate((el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const keys = ['color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle', 'borderRadius', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'minHeight', 'boxShadow', 'outline', 'outlineOffset', 'textDecorationLine', 'gap'];
    const style = {};
    for (const k of keys) style[k] = cs[k];
    return { style, box: { x: r.x, y: r.y, w: r.width, h: r.height } };
  });
}

async function crop(locator, name) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440),
    height: Math.min(box.height + pad * 2, 900),
  };
  const file = path.join(CROPS, name + '.png');
  await page.screenshot({ path: file, clip });
  return name + '.png';
}

async function forcePseudo(locator, classes) {
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

const components = {};
async function measure(name, locator, states = ['default', 'hover', 'focus', 'pressed']) {
  const entry = { page: page.url().split('?')[0], states: {} };
  if (!(await locator.count())) { entry.missing = true; components[name] = entry; console.log('MISS', name); return; }
  const loc = locator.first();
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  entry.states.default = await read(loc);
  entry.states.default.crop = await crop(loc, name + '-default');
  if (states.includes('hover')) {
    await loc.hover();
    await page.waitForTimeout(250);
    entry.states.hover = await read(loc);
    entry.states.hover.crop = await crop(loc, name + '-hover');
    await page.mouse.move(2, 2);
  }
  if (states.includes('focus')) {
    await loc.focus();
    await page.waitForTimeout(200);
    entry.states.focus = await read(loc);
    entry.states.focus.via = 'focus()';
    entry.states.focus.crop = await crop(loc, name + '-focus');
    await page.evaluate(() => document.activeElement && document.activeElement.blur());
  }
  if (states.includes('pressed')) {
    const undo = await forcePseudo(loc, ['active']);
    entry.states.pressed = await read(loc);
    entry.states.pressed.via = 'CDP :active';
    entry.states.pressed.crop = await crop(loc, name + '-pressed');
    await undo();
  }
  components[name] = entry;
  console.log('OK', name, entry.states.default.style.backgroundColor, entry.states.default.style.fontSize);
}

await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(1500);

await measure('button-login', page.locator('[data-test-id="log-in-button"]').first());
await measure('button-signup', page.locator('[data-test-id="sign-up-button"]').first());
await measure('button-start-chat', page.locator('[data-test-id="hero-chat-submit"]').first());
await measure('field-hero', page.locator('[data-test-id="hero-chat-input"]').first(), ['default', 'focus']);
await measure('chip-anonymous', page.locator('[data-test-id="anon-info-badge"]').first(), ['default']);
await measure('heading-display', page.locator('h1').first(), ['default']);
await measure('icon-button-sidebar', page.locator('[data-test-id="sidebar-toggle"]').first(), ['default', 'hover']);

await page.locator('[data-test-id="log-in-button"]').first().click();
await page.waitForTimeout(800);
await measure('button-login-email', page.locator('[data-test-id="start-email-button"]'), ['default', 'hover', 'focus']);
await measure('button-google', page.locator('[data-test-id="start-google-button"]'), ['default']);
await measure('dialog-login', page.locator('[role="dialog"]').first(), ['default']);
await page.keyboard.press('Escape');

await page.goto(BASE + '/chat/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1200);
await measure('field-chat', page.locator('textarea').first(), ['default', 'focus']);
await measure('button-send', page.getByRole('button', { name: 'Send message' }), ['default']);
await measure('chip-suggestion', page.getByRole('button', { name: 'Check my symptoms' }), ['default', 'hover']);

await page.goto(BASE + '/our-philosophy/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1200);
await measure('link-nav', page.getByRole('link', { name: 'Our Philosophy' }).first(), ['default', 'hover']);

const body = await page.evaluate(() => {
  const cs = getComputedStyle(document.body);
  return { backgroundColor: cs.backgroundColor, color: cs.color, fontFamily: cs.fontFamily, fontSize: cs.fontSize };
});

const out = {
  captured: '2026-11-21',
  product: 'doctronic.ai',
  viewport: { width: 1440, height: 900, deviceScaleFactor: 2 },
  body,
  components,
};
fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');
console.log('wrote', OUT, Object.keys(components).length);
await browser.close();
