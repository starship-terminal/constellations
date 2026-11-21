// Measures forhims.co.uk public components. Presses are local toggles only.
// Login, assessment and form submit controls are never activated.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(HERE, '..', '..', '..');
const RAW = path.join(REF, 'raw');
const CROPS = path.join(REF, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const BASE = 'https://www.forhims.co.uk';

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  userAgent: UA,
  locale: 'en-GB',
});
await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
await context.route(/ketchcdn\.com|cdn\.ketchjs\.com|global\.ketchcdn\.com/, (r) => r.abort());
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

async function hide() {
  await page.evaluate(() => document.querySelectorAll('[class*="ketch"], [id*="ketch"]').forEach((n) => n.remove())).catch(() => {});
}
async function goto(url) {
  await page.goto(BASE + url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1600);
  await hide();
}

const PROPS = ['color', 'backgroundColor', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'borderRadius', 'borderTopWidth', 'borderTopColor', 'borderTopStyle', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'height', 'width', 'boxShadow', 'textTransform'];

async function read(locator) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  const box = await handle.boundingBox();
  const style = await handle.evaluate((el, props) => {
    const s = getComputedStyle(el);
    const o = {};
    for (const p of props) o[p] = s[p];
    o.tag = el.tagName;
    o.text = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60);
    return o;
  }, PROPS);
  return { box, style };
}

async function crop(locator, name) {
  const handle = await locator.elementHandle();
  if (!handle) return;
  const box = await handle.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return;
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440 - Math.max(0, box.x - pad)),
    height: Math.min(box.height + pad * 2, 900 - Math.max(0, box.y - pad)),
  };
  if (clip.width < 2 || clip.height < 2) return;
  await page.screenshot({ path: path.join(CROPS, name + '.png'), clip }).catch((e) => console.log('crop skip', name, e.message.split('\n')[0]));
}

async function force(locator, states) {
  const handle = await locator.elementHandle();
  if (!handle) return;
  const { nodeId } = await cdp.send('DOM.describeNode', { objectId: (await handle.ownerFrame ? null : null) }).catch(() => ({}));
  // Use element-based force via DOM.resolveNode after query.
  const objectId = await handle.evaluateHandle(() => 0); // keep handle alive
  void objectId;
  const desc = await cdp.send('DOM.getDocument');
  void desc;
  const resolved = await cdp.send('DOM.requestNode', { objectId: handle._objectId || (await page.evaluateHandle((el) => el, handle))._objectId }).catch(() => null);
  // Playwright element handles expose the CDP object through a different path.
  // Fall back to CSS.forcePseudoState using DOM.querySelector on a marked node.
  await handle.evaluate((el) => { el.setAttribute('data-fh-mark', '1'); });
  const doc = await cdp.send('DOM.getDocument');
  const found = await cdp.send('DOM.querySelector', { nodeId: doc.root.nodeId, selector: '[data-fh-mark="1"]' });
  if (found.nodeId) await cdp.send('CSS.forcePseudoState', { nodeId: found.nodeId, forcedPseudoClasses: states });
  await page.waitForTimeout(200);
  return async () => {
    if (found.nodeId) await cdp.send('CSS.forcePseudoState', { nodeId: found.nodeId, forcedPseudoClasses: [] }).catch(() => {});
    await handle.evaluate((el) => el.removeAttribute('data-fh-mark')).catch(() => {});
  };
}

const readings = { readAt: new Date().toISOString().slice(0, 10), source: 'computed style on www.forhims.co.uk, 1440x900, light, signed out', components: {} };

async function record(name, state, locator) {
  const data = await read(locator);
  if (!data) { console.log('miss', name, state); return; }
  readings.components[name] = readings.components[name] || {};
  readings.components[name][state] = data.style;
  await crop(locator, `${name}-${state}`);
  console.log('ok', name, state, data.style.fontSize, data.style.color, data.style.backgroundColor, data.style.borderRadius);
}

await goto('/');
const logo = page.getByRole('link', { name: 'Link to homepage' }).first();
await record('logo', 'default', logo);

const nav = page.getByRole('link', { name: 'Weight', exact: true }).first();
await record('nav-link', 'default', nav);
await nav.hover();
await page.waitForTimeout(300);
await record('nav-link', 'hover', nav);

const login = page.getByRole('button', { name: 'LOGIN' }).first();
await record('login-button', 'default', login);
await login.hover();
await page.waitForTimeout(250);
await record('login-button', 'hover', login);
const unLogin = await force(login, ['focus-visible']);
if (unLogin) { await record('login-button', 'focus-visible', login); await unLogin(); }
const unPressed = await force(login, ['active', 'hover']);
if (unPressed) { await record('login-button', 'pressed', login); await unPressed(); }

const cta = page.locator('[class*="buttonstyles__Frame"]').filter({ hasText: 'Explore treatments' }).last().locator('xpath=..');
await cta.scrollIntoViewIfNeeded();
await record('button-primary', 'default', cta);
await cta.hover();
await page.waitForTimeout(250);
await record('button-primary', 'hover', cta);
const unCta = await force(cta, ['focus-visible']);
if (unCta) { await record('button-primary', 'focus-visible', cta); await unCta(); }
const unCtaP = await force(cta, ['active', 'hover']);
if (unCtaP) { await record('button-primary', 'pressed', cta); await unCtaP(); }

const card = page.locator('a[href="/c/wl"]').first();
await record('treatment-card', 'default', card);
await card.hover();
await page.waitForTimeout(250);
await record('treatment-card', 'hover', card);

const sex = page.getByRole('button', { name: 'Sex', exact: true }).first();
await sex.click();
await page.waitForTimeout(500);
await hide();
const menu = page.locator('[class*="floating-menu"]').first();
await record('menu', 'open', menu);
const menuItem = menu.getByRole('link').first();
await record('menu-item', 'default', menuItem);
await menuItem.hover();
await page.waitForTimeout(200);
await record('menu-item', 'hover', menuItem);
await page.keyboard.press('Escape');

const burger = page.locator('[class*="global-navigationstyles__Action"]').last();
await burger.click();
await page.waitForTimeout(700);
await hide();
await page.keyboard.press('Escape');

await goto('/weight-loss');
const faq = page.getByRole('button', { name: /weight loss treatment options/i }).first();
await faq.scrollIntoViewIfNeeded();
await record('accordion', 'default', faq);
await faq.click();
await page.waitForTimeout(500);
await record('accordion', 'open', faq);

await goto('/hair-loss');
const select = page.locator('select[name="Sort"]').first();
if (await select.count()) {
  await select.scrollIntoViewIfNeeded();
  await record('select', 'default', select);
}

await goto('/erectile-dysfunction/sildenafil');
const started = page.locator('[class*="buttonstyles__Frame"]').filter({ hasText: 'Get started' }).last().locator('xpath=..');
await started.scrollIntoViewIfNeeded().catch(() => {});
await record('button-pill', 'default', started);
const safety = page.getByRole('link', { name: /important safety information/i }).first();
await record('link', 'default', safety);
await safety.hover();
await page.waitForTimeout(200);
await record('link', 'hover', safety);
const acc = page.getByRole('button', { name: /meet the generic ed pill/i }).first();
await acc.scrollIntoViewIfNeeded();
await record('accordion', 'pdp-default', acc);
if ((await acc.getAttribute('aria-expanded')) !== 'true') await acc.click();
await page.waitForTimeout(400);
await record('accordion', 'pdp-open', acc);

await goto('/c');
const choice = page.getByRole('link').filter({ hasText: /grow thicker/i }).first();
await record('choice-row', 'default', choice);
await choice.hover();
await page.waitForTimeout(200);
await record('choice-row', 'hover', choice);

await goto('/blog');
const chip = page.getByRole('link', { name: 'Weight Loss', exact: true }).first();
if (await chip.count()) {
  await chip.scrollIntoViewIfNeeded().catch(() => {});
  await record('chip', 'default', chip);
}

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(readings, null, 1) + '\n');
console.log('wrote', Object.keys(readings.components).length, 'components');
await browser.close();
