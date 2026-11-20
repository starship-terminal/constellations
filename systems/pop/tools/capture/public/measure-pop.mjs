// Measure Pop's public components. Reads computed styles and writes crops.
// Never types, never submits, never opens app.pop.site.
//
//   PLAYWRIGHT=... node measure-pop.mjs
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const PYTHON = process.env.PYTHON || 'python3';

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'textTransform', 'textDecorationLine', 'opacity', 'cursor',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
];

function quantize(file) {
  execFileSync(PYTHON, ['-c', `
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('RGBA')
q = im.convert('P', palette=Image.Palette.ADAPTIVE, colors=256).convert('RGBA')
q.save(sys.argv[1], optimize=True)
`, file], { stdio: 'ignore' });
}

async function readStyle(locator) {
  return locator.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const pick = (cs) => {
      const o = {};
      for (const p of props) o[p] = noUrl(cs[p]);
      return o;
    };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const out = {
      tag: el.tagName.toLowerCase(),
      framerName: el.getAttribute('data-framer-name'),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style: pick(cs),
    };
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, {
      acceptNode: (t) => (t.textContent.trim() && t.parentElement && t.parentElement !== el ? 1 : 3),
    });
    const tn = walker.nextNode();
    if (tn) {
      const tc = getComputedStyle(tn.parentElement);
      out.textStyle = {
        text: tn.textContent.trim().slice(0, 40),
        fontFamily: tc.fontFamily, fontSize: tc.fontSize, fontWeight: tc.fontWeight,
        lineHeight: tc.lineHeight, letterSpacing: tc.letterSpacing, color: tc.color,
      };
    }
    if (el.tagName === 'INPUT') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, fontSize: ph.fontSize, fontFamily: ph.fontFamily, fontWeight: ph.fontWeight };
    }
    return out;
  }, PROPS);
}

async function crop(page, locator, name) {
  const file = path.join(CROPS, name + '.png');
  await locator.scrollIntoViewIfNeeded();
  await page.waitForTimeout(200);
  const box = await locator.boundingBox();
  if (!box) throw new Error('no box ' + name);
  const vp = page.viewportSize();
  const pad = 10;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  if (clip.width < 2 || clip.height < 2) throw new Error('clip too small ' + name);
  await page.screenshot({ path: file, clip });
  quantize(file);
}

async function forceState(cdp, locator, states) {
  const handle = await locator.elementHandle();
  if (!handle) return;
  const { nodeId } = await cdp.send('DOM.requestNode', { objectId: (await handle.ownerFrame()) ? undefined : undefined }).catch(() => ({}));
  // Use CSS.forcePseudoState via the element's object id.
  const objectId = handle._objectId || (await handle.evaluateHandle((el) => el))._objectId;
  // Playwright elementHandle has a backend node via CDP describeNode.
  const desc = await cdp.send('DOM.describeNode', { objectId: handle._remoteObject?.objectId }).catch(() => null);
  // Fallback: resolve node from the document by a data attribute we set.
  await locator.evaluate((el) => { el.setAttribute('data-pop-measure', '1'); });
  const doc = await cdp.send('DOM.getDocument');
  const found = await cdp.send('DOM.querySelector', { nodeId: doc.root.nodeId, selector: '[data-pop-measure="1"]' });
  await cdp.send('CSS.forcePseudoState', { nodeId: found.nodeId, forcedPseudoClasses: states });
  return found.nodeId;
}

async function clearForce(cdp, nodeId, locator) {
  if (nodeId) await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
  if (locator) await locator.evaluate((el) => el.removeAttribute('data-pop-measure')).catch(() => {});
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

const components = {};
const log = (...a) => console.log(...a);

async function measure(name, locator, states) {
  components[name] = { states: {} };
  for (const state of states) {
    try {
      await locator.scrollIntoViewIfNeeded();
      await page.mouse.move(2, 2);
      await page.waitForTimeout(120);
      let nodeId = null;
      if (state === 'hover') {
        await locator.hover();
        await page.waitForTimeout(280);
      } else if (state === 'focus-visible') {
        await locator.focus();
        await page.keyboard.press('Shift+Tab').catch(() => {});
        await page.keyboard.press('Tab').catch(() => {});
        await page.waitForTimeout(150);
      } else if (state === 'pressed') {
        nodeId = await forceState(cdp, locator, ['active', 'hover']);
        await page.waitForTimeout(120);
      } else if (state === 'open') {
        await locator.click();
        await page.waitForTimeout(500);
      }
      const style = await readStyle(locator);
      components[name].states[state] = style;
      const cropName = `${name}-${state === 'focus-visible' ? 'focus-visible' : state}`;
      await crop(page, locator, cropName);
      log('  ', name, state, style.rect.w + 'x' + style.rect.h, style.style.backgroundColor, style.style.color);
      if (nodeId) await clearForce(cdp, nodeId, locator);
      if (state === 'focus-visible') await page.evaluate(() => document.activeElement && document.activeElement.blur());
      if (state === 'hover') await page.mouse.move(2, 2);
    } catch (e) {
      components[name].states[state] = { error: e.message.split('\n')[0] };
      log('  FAIL', name, state, e.message.split('\n')[0]);
    }
  }
}

log('home');
await page.goto('https://pop.site/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
await page.addStyleTag({ content: '*{caret-color:transparent!important}' });

await measure('nav-link', page.getByRole('link', { name: 'Pricing', exact: true }).first(), ['default', 'hover', 'focus-visible', 'pressed']);
await measure('nav-login', page.getByRole('link', { name: 'Log In', exact: true }).first(), ['default', 'hover', 'focus-visible']);
await measure('nav-create', page.getByRole('link', { name: 'Create Account', exact: true }).first(), ['default', 'hover', 'focus-visible']);
await measure('logo', page.locator('[data-framer-name="Black"]').first(), ['default']);
await measure('claim-field', page.locator('input[name="yourname"]').first(), ['default', 'focus-visible']);
await measure('claim-suffix', page.locator('button').filter({ hasText: '.pop.site' }).first(), ['default', 'hover', 'focus-visible', 'pressed']);
await measure('claim-button', page.getByRole('button', { name: 'Claim your site' }).first(), ['default', 'hover', 'focus-visible', 'pressed']);
await measure('faq-question', page.locator('[data-framer-name="Question"]').first(), ['default', 'hover', 'open']);
await measure('footer-link', page.getByRole('link', { name: 'Terms', exact: true }).first(), ['default', 'hover', 'focus-visible']);

// page ground
components['page-ground'] = {
  states: {
    default: await page.evaluate(() => {
      const b = getComputedStyle(document.body);
      const h = getComputedStyle(document.documentElement);
      return { style: { backgroundColor: b.backgroundColor, color: b.color, fontFamily: b.fontFamily, fontSize: b.fontSize }, htmlBg: h.backgroundColor };
    }),
  },
};

log('pricing');
await page.goto('https://pop.site/pricing', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1500);
const h1 = page.locator('h1').first();
if (await h1.count()) await measure('display-heading', h1, ['default']);

log('blog card');
await page.goto('https://pop.site/blog', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1500);
const card = page.locator('a[href*="/articles/"]').first();
if (await card.count()) await measure('article-card', card, ['default', 'hover']);

log('myinformation');
await page.goto('https://pop.site/myinformation', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1500);
const nameField = page.locator('input[name="Name"]').first();
if (await nameField.count()) await measure('privacy-name', nameField, ['default']);
const emailField = page.locator('input[name="Email"]').first();
if (await emailField.count()) await measure('privacy-email', emailField, ['default']);
const box = page.locator('input[type="checkbox"]').first();
if (await box.count()) await measure('privacy-checkbox', box, ['default']);
const submit = page.getByRole('button', { name: 'Submit' }).first();
if (await submit.count()) await measure('privacy-submit', submit, ['default', 'hover', 'focus-visible']);

log('notfound');
await page.goto('https://pop.site/enterprise', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1200);
const nf = page.locator('h1').first();
if (await nf.count()) await measure('notfound-heading', nf, ['default']);

// tokens from stylesheets
log('vars');
const vars = await page.evaluate(() => {
  const rules = [];
  const fonts = [];
  const walk = (list, ctx) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        fonts.push({
          family: r.style.getPropertyValue('font-family'),
          weight: r.style.getPropertyValue('font-weight'),
          style: r.style.getPropertyValue('font-style'),
          src: 'url(…)',
        });
        continue;
      }
      if (r.cssRules && !r.style) {
        walk(r.cssRules, ctx);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k.startsWith('--')) props[k] = r.style.getPropertyValue(k).trim().slice(0, 180);
      }
      if (Object.keys(props).length) rules.push({ selector: r.selectorText, props });
    }
  };
  for (const sheet of document.styleSheets) {
    try { walk(sheet.cssRules, []); } catch { /* cross-origin */ }
  }
  const root = getComputedStyle(document.documentElement);
  const resolved = {};
  const names = new Set();
  for (const rule of rules) for (const k of Object.keys(rule.props)) names.add(k);
  for (const k of names) resolved[k] = root.getPropertyValue(k).trim().slice(0, 180);
  return { ruleCount: rules.length, nameCount: names.size, resolved, fonts: fonts.slice(0, 30), sample: rules.slice(0, 8) };
});

const out = {
  _meta: {
    product: 'Pop Site',
    url: 'https://pop.site/',
    captured: '2026-11-21',
    viewport: { width: 1440, height: 900, deviceScaleFactor: 1 },
    note: 'Public marketing site only. No field was typed into. No form was submitted. Login and signup were not opened.',
  },
  components,
};
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(vars, null, 1) + '\n');
log('wrote', Object.keys(components).length, 'components', vars.nameCount, 'vars');
await browser.close();
