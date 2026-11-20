// Measure Pryzm's public components and write raw/components-computed.json
// plus element crops. States are forced with Playwright hover / focus / active.
// No form is submitted.
//
//   PLAYWRIGHT=... node tools/capture/public/measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, PROPS, CROPS, RAW } from './lib.mjs';

fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const SPECS = [
  { id: 'button-primary', page: '/', name: 'Open studio', role: 'link', states: ['default', 'hover', 'focus-visible'] },
  { id: 'button-quiet', page: '/', name: 'Sign in', role: 'link', states: ['default', 'hover', 'focus-visible'] },
  { id: 'link-nav', page: '/', name: 'Inspiration', role: 'link', states: ['default', 'hover', 'focus-visible'] },
  { id: 'tab', page: '/', name: 'Monthly', role: 'tab', states: ['default', 'hover', 'focus-visible'] },
  { id: 'tab-selected', page: '/', name: 'Yearly', role: 'tab', states: ['default'] },
  { id: 'text-field', page: '/signin', name: 'Email address*', role: 'textbox', states: ['default', 'focus-visible'], note: 'signin wall; not typed, not submitted' },
  { id: 'button-google', page: '/signin', name: 'Continue with Google', role: 'button', states: ['default', 'hover'], note: 'not clicked' },
  { id: 'button-submit', page: '/signin', name: 'Continue', role: 'button', states: ['default', 'hover', 'focus-visible'], note: 'not submitted' },
  { id: 'card', page: '/gallery', name: 'Bright Spark', role: 'link', states: ['default', 'hover', 'focus-visible'] },
  { id: 'badge', page: '/gallery/ink-facet-280dcf', name: 'PRO', role: null, states: ['default'] },
  { id: 'button-export', page: '/studio', name: 'Export', role: 'button', states: ['default', 'hover', 'focus-visible'] },
  { id: 'button-icon', page: '/studio', name: 'Undo', role: 'button', states: ['default', 'hover', 'focus-visible'] },
  { id: 'switch', page: '/studio', name: null, role: 'switch', states: ['default', 'hover', 'focus-visible'] },
  { id: 'combobox', page: '/lab', name: 'Additive', role: 'combobox', states: ['default', 'hover', 'focus-visible'] },
  { id: 'dialog', page: '/studio', name: 'Export', role: 'button', open: true, states: ['default'] },
  { id: 'menu', page: '/', name: 'Menu', role: 'button', open: true, mobile: true, states: ['default'] },
];

async function mark(page, spec) {
  return page.evaluate(({ name, role }) => {
    document.querySelectorAll('[data-m-mark]').forEach((e) => e.removeAttribute('data-m-mark'));
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 2 && r.height > 2 && s.visibility !== 'hidden' && s.display !== 'none' && Number(s.opacity) > 0.05;
    };
    let el = null;
    if (role === 'switch') {
      el = [...document.querySelectorAll('[role="switch"]')].find(vis) || null;
    } else if (name === 'PRO') {
      el = [...document.querySelectorAll('span,div,a')].find((e) => vis(e) && (e.innerText || '').trim() === 'PRO' && e.getBoundingClientRect().width < 80) || null;
    } else if (name === 'Bright Spark') {
      el = [...document.querySelectorAll('a')].find((e) => vis(e) && /Bright Spark/.test(e.innerText || '') && e.getBoundingClientRect().width > 80) || null;
    } else if (role) {
      const nodes = [...document.querySelectorAll(`[role="${role}"], ${role === 'link' ? 'a' : role === 'button' ? 'button' : role === 'textbox' ? 'input,textarea' : role}`)];
      el = nodes.find((e) => vis(e) && ((e.innerText || e.getAttribute('aria-label') || e.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim() === name || (e.getAttribute('aria-label') || '') === name)) || null;
      if (!el && role === 'textbox') {
        el = [...document.querySelectorAll('input')].find((e) => vis(e) && (e.getAttribute('placeholder') || '').includes('Email')) || null;
      }
    }
    if (!el) return null;
    el.setAttribute('data-m-mark', '1');
    const r = el.getBoundingClientRect();
    return { tag: el.tagName, w: r.width, h: r.height, text: (el.innerText || el.getAttribute('aria-label') || '').slice(0, 40) };
  }, { name: spec.name, role: spec.role });
}

async function readBox(page) {
  return page.evaluate((props) => {
    const el = document.querySelector('[data-m-mark]');
    if (!el) return null;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = cs[p];
    return {
      tag: el.tagName,
      role: el.getAttribute('role'),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      rect: { x: r.x, y: r.y, width: r.width, height: r.height },
      style,
    };
  }, PROPS);
}

const browser = await chromium.launch({ headless: true });
const results = [];

for (const spec of SPECS) {
  const mobile = !!spec.mobile;
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: 'dark' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, locale: 'en-US', colorScheme: 'dark' });
  const page = await context.newPage();
  try {
    await page.goto(BASE + spec.page, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(spec.page === '/studio' || spec.page === '/lab' ? 2200 : 1400);
    if (spec.page === '/' && spec.name === 'Monthly') {
      await page.locator('#pricing').scrollIntoViewIfNeeded().catch(() => {});
    }
    if (spec.name === 'Yearly') {
      await page.getByRole('tab', { name: /Yearly/ }).click();
      await page.waitForTimeout(300);
    }
    if (spec.open && spec.name === 'Export') {
      await page.getByRole('button', { name: 'Export' }).first().click();
      await page.waitForTimeout(600);
    }
    if (spec.open && spec.name === 'Menu') {
      await page.getByRole('button', { name: 'Menu' }).click();
      await page.waitForTimeout(500);
    }
    const found = await mark(page, spec.open && spec.name === 'Export'
      ? { ...spec, role: 'dialog', name: null }
      : spec.open && spec.name === 'Menu'
        ? { ...spec, role: 'dialog', name: null }
        : spec);
    if (spec.open) {
      // re-mark the dialog
      await page.evaluate(() => {
        document.querySelectorAll('[data-m-mark]').forEach((e) => e.removeAttribute('data-m-mark'));
        const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 40 && r.height > 40; };
        const d = [...document.querySelectorAll('[role="dialog"]')].find(vis);
        if (d) d.setAttribute('data-m-mark', '1');
      });
    }
    if (!found && !spec.open) {
      results.push({ id: spec.id, page: spec.page, found: false, note: spec.note || 'selector missed' });
      console.log('MISS', spec.id);
      await context.close();
      continue;
    }
    for (const state of spec.states) {
      const el = page.locator('[data-m-mark]');
      if (!(await el.count())) {
        results.push({ id: spec.id, state, found: false });
        continue;
      }
      if (state === 'hover') await el.hover();
      if (state === 'focus-visible') await el.focus();
      if (state === 'pressed') await page.mouse.down();
      await page.waitForTimeout(180);
      const box = await readBox(page);
      const crop = `${spec.id}-${state}.png`;
      const handle = await el.elementHandle();
      if (handle && box && box.rect.width > 2) {
        await handle.screenshot({ path: path.join(CROPS, crop) }).catch((e) => console.log('crop fail', crop, e.message.split('\n')[0]));
      }
      if (state === 'pressed') await page.mouse.up();
      results.push({
        id: spec.id,
        state,
        page: spec.page,
        found: !!box,
        note: spec.note || null,
        width: mobile ? 390 : 1440,
        theme: 'dark',
        box,
        source: `measured computed style on ${spec.page} ${state} 2026-11-21`,
      });
      console.log('OK', spec.id, state, box && box.rect);
    }
  } catch (e) {
    console.log('FAIL', spec.id, e.message.split('\n')[0]);
    results.push({ id: spec.id, found: false, error: e.message.split('\n')[0] });
  }
  await context.close();
}
await browser.close();
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({ product: 'Pryzm', captured: '2026-11-21', results }, null, 2) + '\n');
console.log('wrote', results.length);
