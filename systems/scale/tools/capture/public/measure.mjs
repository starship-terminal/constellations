// Measure Scale's public controls. Nothing is submitted.
// PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, RAW, BASE, CROPS, styleOf } from './lib.mjs';

fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

const out = { read: '2026-11-21', url: BASE, viewport: { width: 1440, height: 900, dpr: 1 }, components: {} };

async function force(locator, states) {
  const handle = await locator.elementHandle();
  if (!handle) return;
  const node = await cdp.send('DOM.describeNode', { objectId: (await handle.evaluateHandle((el) => el))._objectId ? undefined : undefined }).catch(() => null);
  // Use element highlight via CSS.forcePseudoState needs a nodeId from DOM.getDocument query.
  const { root } = await cdp.send('DOM.getDocument');
  const described = await cdp.send('DOM.describeNode', { backendNodeId: undefined, objectId: handle._objectId || undefined }).catch(() => null);
}

async function measure(name, state, locator, note) {
  const n = await locator.count();
  if (!n) {
    out.components[name] = out.components[name] || {};
    out.components[name][state] = { missing: true, note };
    console.log('  miss', name, state);
    return null;
  }
  const el = locator.first();
  await el.scrollIntoViewIfNeeded().catch(() => {});
  const style = await styleOf(el);
  out.components[name] = out.components[name] || {};
  out.components[name][state] = { ...style, note: note || null, via: 'computed-style' };
  const box = await el.boundingBox();
  if (box && box.width > 2 && box.height > 2 && box.width < 1400 && box.height < 800) {
    const pad = 4;
    const clip = {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(1440 - Math.max(0, box.x - pad), box.width + pad * 2),
      height: Math.min(900 - Math.max(0, box.y - pad), box.height + pad * 2),
    };
    const file = path.join(CROPS, `${name}-${state}.png`);
    await page.screenshot({ path: file, clip }).catch((e) => console.log('  crop fail', name, e.message));
  }
  console.log('  ok', name, state, style.backgroundColor, style.color, style.fontSize, style.borderRadius);
  return el;
}

await open(page, BASE + '/', { wait: 2000 });
await measure('button-primary', 'default', page.locator('header a[href="/demo"]').first(), 'header Get Started, scale.com/');
const primary = page.locator('header a[href="/demo"]').first();
await primary.hover();
await page.waitForTimeout(350);
await measure('button-primary', 'hover', primary, 'real pointer hover');
await page.mouse.move(2, 2);
await primary.focus();
await page.keyboard.press('Shift+Tab');
await page.keyboard.press('Tab');
await page.waitForTimeout(200);
await measure('button-primary', 'focus-visible', primary, 'keyboard Tab onto Get Started');

await measure('button-secondary', 'default', page.locator('header a[href="https://dashboard.scale.com/login"]').first(), 'header Log In');
const login = page.locator('header a[href="https://dashboard.scale.com/login"]').first();
await login.hover();
await page.waitForTimeout(300);
await measure('button-secondary', 'hover', login, 'real pointer hover');

await measure('nav-link', 'default', page.getByRole('button', { name: 'Products', exact: true }).first(), 'header Products');
await page.evaluate(() => document.getElementById('onetrust-consent-sdk')?.remove());
await page.evaluate(() => {
  const b = [...document.querySelectorAll('button')].find((el) => (el.innerText || '').trim() === 'Products');
  b?.click();
});
await page.waitForTimeout(400);
await measure('menu', 'open', page.locator('header a[href="/data-engine"]').first(), 'Products menu, Scale Data Engine link');
await page.keyboard.press('Escape');

await open(page, BASE + '/demo', { wait: 1800 });
await measure('heading', 'default', page.locator('h1').first(), 'demo h1');
await measure('text-field', 'default', page.locator('input[name="firstname"]').first(), 'demo first name, empty');
const field = page.locator('input[name="firstname"]').first();
await field.focus();
await page.waitForTimeout(250);
await measure('text-field', 'focus', field, 'demo first name focused, empty, not submitted');
await measure('select', 'default', page.locator('select[name="region"]').first(), 'demo country select, not opened, not submitted');
await measure('button-submit', 'default', page.locator('button, input[type="submit"]').filter({ hasText: 'Submit' }).first(), 'demo submit, not clicked');

await open(page, BASE + '/blog', { wait: 1800 });
await measure('button-quiet', 'default', page.getByRole('button', { name: /SEARCH/ }).first(), 'blog search trigger');

await open(page, BASE + '/docs', { wait: 2500 });
await measure('docs-heading', 'default', page.locator('h1').first(), 'docs h1');
const themeBtn = page.getByRole('button', { name: 'Change theme preference' });
if (await themeBtn.count()) {
  await themeBtn.first().click();
  await page.waitForTimeout(400);
  await measure('menu', 'theme', page.getByRole('menuitem').first(), 'docs theme menu first item');
  const dark = page.getByRole('menuitem', { name: /dark/i });
  if (await dark.count()) {
    await dark.first().click();
    await page.waitForTimeout(600);
    const body = await page.evaluate(() => {
      const s = getComputedStyle(document.body);
      return { bg: s.backgroundColor, color: s.color, theme: document.documentElement.className, data: document.documentElement.getAttribute('data-theme') };
    });
    out.docsDark = body;
    console.log('  docs dark', JSON.stringify(body));
    await measure('docs-body', 'dark', page.locator('body'), 'docs after choosing dark in the theme menu');
  }
}

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote', path.join(RAW, 'components-computed.json'));
await browser.close();
