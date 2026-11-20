// Measures macawhq.com public components. No form is submitted. Auth links
// are not followed (app.macawhq.com does not resolve).
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, PROPS, RAW, CROPS } from './lib.mjs';

fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

const components = {};
const counts = {};

async function paintCounts() {
  const found = await page.evaluate(() => {
    const bump = (map, key) => { map[key] = (map[key] || 0) + 1; };
    const colors = {}, sizes = {}, radii = {};
    const nodes = document.querySelectorAll('body *');
    let n = 0;
    for (const el of nodes) {
      if (n++ > 4000) break;
      const r = el.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) continue;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.display === 'none') continue;
      bump(colors, cs.color);
      bump(colors, cs.backgroundColor);
      bump(sizes, cs.fontSize);
      if (cs.borderRadius && cs.borderRadius !== '0px') bump(radii, cs.borderRadius);
    }
    return { colors, sizes, radii };
  });
  for (const bucket of ['colors', 'sizes', 'radii']) {
    counts[bucket] ??= {};
    for (const [k, v] of Object.entries(found[bucket])) counts[bucket][k] = (counts[bucket][k] || 0) + v;
  }
}

async function read(locator) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  const box = await handle.boundingBox();
  const style = await page.evaluate(({ el, props }) => {
    const cs = getComputedStyle(el);
    const out = {};
    for (const p of props) out[p] = cs[p];
    const r = el.getBoundingClientRect();
    out.text = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    out.rect = { x: r.x, y: r.y, w: r.width, h: r.height };
    return out;
  }, { el: handle, props: PROPS });
  return { handle, box, style };
}

async function crop(name, handle) {
  const box = await handle.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440 - Math.max(0, box.x - pad)),
    height: Math.min(box.height + pad * 2, 900 - Math.max(0, box.y - pad)),
  };
  if (clip.width < 2 || clip.height < 2) return null;
  const file = path.join(CROPS, name + '.png');
  await page.screenshot({ path: file, clip, scale: 'css' });
  return path.basename(file);
}

async function forcePseudo(handle, pseudo) {
  const node = await cdp.send('DOM.describeNode', { objectId: (await handle.evaluateHandle((el) => el))._objectId ? undefined : undefined }).catch(() => null);
  // Use DOM.getNodeForLocation is unreliable. Force via CSS.forcePseudoState needs a nodeId.
  const { root } = await cdp.send('DOM.getDocument');
  const objectId = handle._objectId || (await handle.evaluateHandle((el) => el))._remoteObject?.objectId;
  // Playwright ElementHandle exposes the remote object through the protocol differently.
  // Fall back: set an attribute and use a style injection is not a real pseudo.
  // CDP path:
  try {
    const remote = await cdp.send('DOM.requestNode', { objectId: handle._objectId });
    return remote;
  } catch {
    return null;
  }
}

async function states(name, locator, { hover = true, focus = false } = {}) {
  const base = await read(locator);
  if (!base || !base.box) {
    log('  miss', name);
    components[name] = { status: 'not captured', reason: 'selector missed' };
    return;
  }
  const entry = { default: { style: base.style, box: base.box } };
  entry.default.crop = await crop(name + '-default', base.handle);
  if (hover) {
    await page.mouse.move(base.box.x + Math.min(12, base.box.width / 2), base.box.y + Math.min(8, base.box.height / 2));
    await page.waitForTimeout(250);
    const h = await read(locator);
    if (h) {
      entry.hover = { style: h.style, box: h.box };
      entry.hover.crop = await crop(name + '-hover', h.handle);
      await h.handle.dispose();
    }
    await page.mouse.move(2, 2);
    await page.waitForTimeout(150);
  }
  if (focus) {
    await locator.focus().catch(() => {});
    await page.waitForTimeout(200);
    const f = await read(locator);
    if (f) {
      entry['focus-visible'] = { style: f.style, box: f.box, via: 'element.focus()' };
      entry['focus-visible'].crop = await crop(name + '-focus-visible', f.handle);
      await f.handle.dispose();
    }
  }
  // pressed via CDP forcePseudoState when we can resolve a nodeId
  try {
    const objectId = base.handle._objectId;
    if (objectId) {
      const { nodeId } = await cdp.send('DOM.requestNode', { objectId });
      await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['hover', 'active'] });
      await page.waitForTimeout(80);
      const pressed = await read(locator);
      if (pressed) {
        entry.pressed = { style: pressed.style, box: pressed.box, via: 'CDP forcePseudoState active' };
        entry.pressed.crop = await crop(name + '-pressed', pressed.handle);
        await pressed.handle.dispose();
      }
      await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] });
    }
  } catch (e) {
    entry.pressed = { status: 'not captured', reason: 'CDP forcePseudoState failed: ' + String(e.message || e).split('\n')[0] };
  }
  await base.handle.dispose();
  components[name] = entry;
  log('  measured', name, Object.keys(entry).join(','));
}

async function goto(url) {
  await page.goto(BASE + url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(1800);
  await page.addStyleTag({ content: '.splide__list { animation: none !important; transition: none !important; }' }).catch(() => {});
  await paintCounts();
}

await goto('/');
await states('nav-link', page.locator('a.navbar_link').filter({ hasText: 'Pricing' }).first());
await states('button-primary', page.locator('a.button').filter({ hasText: 'Start for free' }).first());
await states('button-secondary', page.locator('a.button-secondary-gray').filter({ hasText: 'Log in' }).first());
await states('logo-link', page.locator('a.navbar07_logo-link').first());

const resources = page.locator('.navbar_dropdown-toggle').first();
const rbox = await resources.boundingBox();
if (rbox) {
  await page.mouse.move(rbox.x + rbox.width / 2, rbox.y + rbox.height / 2);
  await page.waitForTimeout(400);
  const list = page.locator('.navbar_dropdown-list').first();
  const open = await page.evaluate(() => {
    const list = document.querySelector('.navbar_dropdown-list');
    return list && getComputedStyle(list).display !== 'none' && list.getBoundingClientRect().height > 20;
  });
  if (open) {
    await states('resources-menu', list, { hover: false });
    await states('resources-link', page.locator('.navbar_dropdown-link').first());
  } else {
    components['resources-menu'] = { status: 'not captured', reason: 'hover did not open .navbar_dropdown-list during measure' };
    log('  resources closed');
  }
  await page.mouse.move(2, 2);
}

await page.evaluate(() => document.querySelector('#examples')?.scrollIntoView({ block: 'center' }));
await page.waitForTimeout(300);
const card = page.locator('.div-block-46').first();
await states('example-card', card, { hover: false });
await page.evaluate(() => document.querySelector('.div-block-46')?.click());
await page.waitForTimeout(500);
const modal = page.locator('.tingle-modal--visible .tingle-modal-box').first();
if (await modal.count()) {
  await states('example-dialog', modal, { hover: false });
  await states('dialog-close', page.locator('.tingle-modal--visible .tingle-modal__close').first());
  await page.evaluate(() => document.querySelector('.tingle-modal--visible .tingle-modal__close')?.click());
} else {
  components['example-dialog'] = { status: 'not captured', reason: 'tingle modal did not become visible' };
}

await goto('/pricing');
await states('pricing-toggle', page.locator('.pricing-toggle-button').filter({ hasText: 'Yearly' }).first());
await states('pricing-card', page.locator('body').locator('text=Starter').locator('xpath=ancestor::div[contains(@class,"pricing") or contains(@class,"card")][1]').first(), { hover: false }).catch(() => {});
// more reliable pricing card: the block that contains "$59"
const priceCard = await page.evaluateHandle(() => {
  const el = [...document.querySelectorAll('div, section, article')].find((n) => {
    const t = (n.innerText || '').replace(/\s+/g, ' ');
    return /Starter/.test(t) && /\$59/.test(t) && t.length < 500 && n.getBoundingClientRect().width > 180 && n.getBoundingClientRect().width < 500;
  });
  return el || null;
});
if (priceCard) {
  const box = await priceCard.asElement()?.boundingBox();
  if (box) {
    const handle = priceCard.asElement();
    components['plan-card'] = { default: { box, style: await page.evaluate(({ el, props }) => {
      const cs = getComputedStyle(el);
      const out = {};
      for (const p of props) out[p] = cs[p];
      out.text = (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80);
      return out;
    }, { el: handle, props: PROPS }) } };
    components['plan-card'].default.crop = await crop('plan-card-default', handle);
    log('  measured plan-card');
  }
}
const cta = page.locator('a').filter({ hasText: 'Get started' }).first();
await states('plan-cta', cta);

await goto('/contact-us');
await states('text-field', page.locator('input.form-input').first(), { hover: true, focus: true });
await states('text-area', page.locator('textarea.form-input').first(), { hover: true, focus: true });
await states('submit-button', page.locator('input.w-button[type="submit"]').first(), { focus: true });

const brand = await page.evaluate(() => ({
  themeColor: [...document.querySelectorAll('meta[name="theme-color"]')].map((m) => m.content),
  mask: document.querySelector('link[rel="mask-icon"]')?.getAttribute('color') || null,
  manifest: document.querySelector('link[rel="manifest"]')?.href || null,
}));

const out = {
  product: 'macaw',
  captured: new Date().toISOString().slice(0, 10),
  viewport: { width: 1440, height: 900 },
  url: BASE,
  brand,
  useCounts: counts,
  components,
};
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2) + '\n');
console.log('wrote components', Object.keys(components).length);
await browser.close();
