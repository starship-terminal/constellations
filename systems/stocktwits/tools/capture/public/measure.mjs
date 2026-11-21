// Measures Stocktwits public components from computed styles.
// No form is submitted. No OAuth button is clicked. Nothing is typed.
// PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { BASE, launch, hideConsent, RAW, CROPS, REF } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const PYTHON = process.env.PYTHON || 'python3';
const out = { _meta: { product: 'Stocktwits', captured: '2026-11-21', route: 'public', theme: 'light' }, components: {} };
const log = (...a) => console.log(...a);
const save = () => fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2));

async function prepare(page) {
  await hideConsent(page);
  await page.evaluate(() => {
    document.querySelectorAll('iframe, #credential_picker_container').forEach((el) => {
      const src = el.getAttribute('src') || '';
      if ((el.id || '').includes('credential') || /google|gsi/.test(src)) el.remove();
    });
    const heading = [...document.querySelectorAll('h1, h2, h3, [role="heading"]')].find((el) => /Choose Your Experience/.test(el.innerText || ''));
    if (heading) {
      let n = heading;
      for (let i = 0; i < 6 && n; i++, n = n.parentElement) {
        if (n.getAttribute('role') === 'dialog' || /dialog|modal|popup/i.test(n.className || '')) { n.remove(); break; }
      }
    }
  });
}

async function mark(page, id, text, tag = 'a, button') {
  return page.evaluate(({ id, text, tag }) => {
    const re = new RegExp('^' + text + '$');
    const el = [...document.querySelectorAll(tag)].find((node) => re.test((node.innerText || node.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim()));
    if (!el) return false;
    el.setAttribute('data-st-mark', id);
    el.scrollIntoView({ block: 'center', inline: 'nearest' });
    return true;
  }, { id, text, tag });
}

async function read(page, key, state) {
  const loc = page.locator(`[data-st-mark="${key}-${state}"]`);
  if (!(await loc.count())) { log('  miss', key, state); return; }
  const reading = await loc.evaluate((el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 6).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style: {
        backgroundColor: cs.backgroundColor,
        color: cs.color,
        borderTopColor: cs.borderTopColor,
        borderTopWidth: cs.borderTopWidth,
        borderRadius: cs.borderRadius,
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight,
        letterSpacing: cs.letterSpacing,
        padding: `${cs.paddingTop} ${cs.paddingRight} ${cs.paddingBottom} ${cs.paddingLeft}`,
        height: cs.height,
        boxShadow: cs.boxShadow,
        outline: `${cs.outlineWidth} ${cs.outlineStyle} ${cs.outlineColor}`,
      },
    };
  });
  const box = await loc.boundingBox();
  if (box && box.width > 2 && box.height > 2) {
    const vp = page.viewportSize();
    const pad = 4;
    const clip = {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
      height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
    };
    const file = path.join(CROPS, `${key}-${state}.png`);
    await page.screenshot({ path: file, clip });
    execFileSync(PYTHON, ['-c', 'import sys; from PIL import Image; f=sys.argv[1]; Image.open(f).convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)', file]);
    reading.crop = path.relative(REF, file);
  }
  out.components[key] ??= {};
  out.components[key][state] = { ...reading, via: 'computed-style', page: page.url().replace(BASE, '') };
  log('  ok', key, state, reading.style.fontSize, reading.style.color, reading.style.backgroundColor, reading.style.borderRadius);
}

async function take(page, key, state, text, tag) {
  const ok = await mark(page, `${key}-${state}`, text, tag);
  if (!ok) { log('  miss', key, state, text); return; }
  await page.waitForTimeout(200);
  await read(page, key, state);
}

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();

async function go(pathName) {
  const resp = await page.goto(BASE + pathName, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2200);
  await prepare(page);
  const title = await page.title();
  const blocked = /just a moment|attention required/i.test(title);
  log('page', pathName, resp && resp.status(), blocked ? 'BLOCKED' : title.slice(0, 50));
  return !blocked;
}

if (await go('/')) {
  const foundations = await page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const names = new Set();
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (rules) => {
        if (!rules) return;
        for (const rule of rules) {
          if (rule.cssRules) walk(rule.cssRules);
          if (!rule.style) continue;
          for (let i = 0; i < rule.style.length; i++) {
            const prop = rule.style[i];
            if (prop.startsWith('--') && /color|font|radius|shadow|grey|gray|green|red|blue|primary|background|text|border/.test(prop) && !prop.startsWith('--tw-')) names.add(prop);
          }
        }
      };
      walk(rules);
    }
    const resolved = {};
    for (const n of names) {
      const v = root.getPropertyValue(n).trim();
      if (v && v.length < 80) resolved[n] = v;
    }
    return {
      dataTheme: document.documentElement.getAttribute('data-theme'),
      htmlClass: document.documentElement.className,
      innerWidth: innerWidth,
      innerHeight: innerHeight,
      devicePixelRatio: devicePixelRatio,
      body: { backgroundColor: body.backgroundColor, color: body.color, fontFamily: body.fontFamily, fontSize: body.fontSize, lineHeight: body.lineHeight },
      resolved,
    };
  });
  out._meta.foundations = foundations;
  log('vars', Object.keys(foundations.resolved).length);
  await take(page, 'button-primary', 'default', 'Sign Up', 'a, button');
  await page.locator('[data-st-mark="button-primary-default"]').hover().catch(() => {});
  await page.waitForTimeout(200);
  await read(page, 'button-primary', 'hover').catch(() => {});
  if (out.components['button-primary'] && out.components['button-primary'].hover === undefined && out.components['button-primary'].default) {
    const loc = page.locator('[data-st-mark="button-primary-default"]');
    if (await loc.count()) {
      await loc.evaluate((el) => el.setAttribute('data-st-mark', 'button-primary-hover'));
      await read(page, 'button-primary', 'hover');
    }
  }
  await take(page, 'button-secondary', 'default', 'Log In', 'a, button');
  await take(page, 'button-outline', 'default', 'Create Account', 'a, button');
  await take(page, 'link', 'default', 'Log in to existing account', 'a');
  await take(page, 'nav-link', 'default', 'Trending', 'a');
  await take(page, 'tab', 'selected', 'For You', 'button');
  await take(page, 'tab', 'default', 'Following', 'button');
  const search = page.locator('input[name="desktopSearch"]');
  if (await search.count()) {
    await search.evaluate((el) => el.setAttribute('data-st-mark', 'search-field-default'));
    await read(page, 'search-field', 'default');
    await search.focus();
    await page.waitForTimeout(200);
    await search.evaluate((el) => el.setAttribute('data-st-mark', 'search-field-focus'));
    await read(page, 'search-field', 'focus');
    await page.keyboard.press('Escape');
  }
  save();
}

if (await go('/symbol/AAPL')) {
  await take(page, 'button-bullish', 'default', 'Bullish', 'button');
  await take(page, 'button-bearish', 'default', 'Bearish', 'button');
  await take(page, 'tabs-symbol', 'selected', 'Feed', 'a');
  await take(page, 'tabs-symbol', 'default', 'News', 'a');
  await take(page, 'chip', 'selected', 'All', 'button');
  const price = await page.evaluate(() => {
    const el = [...document.querySelectorAll('div, span, p')].find((n) => /^\$\d/.test((n.innerText || '').trim()) && n.children.length === 0 && n.getBoundingClientRect().height > 20);
    if (!el) return null;
    const cs = getComputedStyle(el);
    return { text: el.innerText.trim().slice(0, 20), fontFamily: cs.fontFamily, fontSize: cs.fontSize, fontWeight: cs.fontWeight, color: cs.color, lineHeight: cs.lineHeight };
  });
  if (price) out.components.price = { default: { via: 'computed-style', page: '/symbol/AAPL', style: price, text: price.text } };
  log('  price', price && price.fontSize, price && price.color);
  save();
}

if (await go('/signin')) {
  const login = page.locator('input[name="login"]');
  if (await login.count()) {
    await login.evaluate((el) => el.setAttribute('data-st-mark', 'text-field-default'));
    await read(page, 'text-field', 'default');
    await login.focus();
    await page.waitForTimeout(150);
    await login.evaluate((el) => el.setAttribute('data-st-mark', 'text-field-focus'));
    await read(page, 'text-field', 'focus');
  } else log('  miss text-field');
  await take(page, 'button-disabled', 'default', 'Log In', 'button');
  await take(page, 'link-inline', 'default', 'Forgot your password?', 'a');
  await take(page, 'link-inline', 'signup', 'Sign up', 'a');
  save();
}

log('components', Object.keys(out.components).length);
save();
await browser.close();
