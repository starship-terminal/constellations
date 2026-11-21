// Measure Rivian's public controls on the live homepage. No form is submitted.
// Writes raw/components-computed.json and crops into components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, styleOf, crop, BASE, CROPS, RAW } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 2 });
const page = await context.newPage();
await open(page, BASE + '/', { wait: 1500 });
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

const out = { _meta: { source: BASE + '/', viewport: '1440x900', dpr: 2, readAt: new Date().toISOString().slice(0, 10) }, components: {} };

async function forcePseudo(loc, classes) {
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(250);
  return async () => {
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
    await loc.evaluate((el) => el.removeAttribute('data-m-force')).catch(() => {});
  };
}

async function record(key, state, loc, note) {
  const el = loc.first();
  if (!(await el.count())) { out.components[key] = { missing: true, note }; return; }
  await el.scrollIntoViewIfNeeded().catch(() => {});
  const style = await styleOf(el);
  const file = path.join(CROPS, `${key}-${state}.png`);
  const clip = await crop(page, el, file).catch(() => null);
  const c = (out.components[key] ??= { states: {}, note: note || '' });
  c.states[state] = { style, crop: clip ? path.basename(file) : null };
  console.log(key, state, style.backgroundColor, style.color, style.borderRadius, style.fontSize);
}

const demo = page.getByRole('link', { name: 'Demo drive' }).first();
await record('button-primary', 'default', demo, 'Header Demo drive pill');
await demo.hover();
await page.waitForTimeout(300);
await record('button-primary', 'hover', demo);
const release = await forcePseudo(demo, ['hover', 'active']);
await record('button-primary', 'pressed', demo);
await release();
await page.keyboard.press('Shift');
await demo.focus();
await record('button-primary', 'focus-visible', demo, 'focused with keyboard after Shift');

const book = page.getByRole('link', { name: 'Book a drive' }).first();
await record('button-secondary', 'default', book, 'Hero outline Book a drive');
await book.hover();
await page.waitForTimeout(250);
await record('button-secondary', 'hover', book);

const design = page.getByRole('link', { name: 'Design yours' }).first();
await record('button-inverse', 'default', design, 'Hero white Design yours pill');

const nav = page.locator('header button').filter({ hasText: /^Vehicles$/ }).first();
await record('nav-item', 'default', nav, 'Header Vehicles button');
await nav.hover();
await page.waitForTimeout(200);
await record('nav-item', 'hover', nav);
await nav.click();
await page.waitForTimeout(500);
await record('nav-item', 'selected', nav, 'Vehicles menu open');
await record('menu', 'default', page.locator('#navbar-panel, [data-slot="navbar-panel"]').first(), 'Vehicles mega-menu panel');
const explore = page.getByRole('link', { name: 'Explore' }).first();
await record('link', 'default', explore, 'Explore link inside the Vehicles menu');
await explore.hover();
await page.waitForTimeout(200);
await record('link', 'hover', explore);
await page.keyboard.press('Escape');

const chat = page.getByRole('button', { name: 'Have a question?' }).first();
await record('icon-button', 'default', chat, 'Yellow question launcher');
await chat.click();
await page.waitForTimeout(1200);
await record('dialog', 'default', page.locator('iframe[title="Newsletter form"]').first(), 'Assistant panel iframe. Fields not filled.');
await page.keyboard.press('Escape');

// Phone width for the accordion trigger, in a second context.
await context.close();
const { browser: b2, context: c2 } = await launch({ mobile: true });
const p2 = await c2.newPage();
await open(p2, BASE + '/', { wait: 1500 });
const openBtn = p2.locator('#navbar-trigger-accordion');
if (await openBtn.count()) {
  const style = await styleOf(openBtn);
  const file = path.join(CROPS, 'icon-button-menu-default.png');
  await crop(p2, openBtn, file);
  out.components['icon-button-menu'] = { states: { default: { style, crop: 'icon-button-menu-default.png' } }, note: 'Mobile Open accordion trigger at 390' };
  console.log('icon-button-menu', style.width, style.height, style.borderRadius);
}
await b2.close();
await browser.close();
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT, Object.keys(out.components).length);
