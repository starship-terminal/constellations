// Finish interaction states the first run missed. Does not submit forms.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from './screenshot.mjs';
import { launch, contextFor, open, styleOf, PROPS, PKG } from './public/lib.mjs';

const RAW_SHOTS = path.join(os.homedir(), '.design-systems', 'leonardo', 'raw-shots');
const RAW = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(CROPS, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const out = JSON.parse(fs.readFileSync(path.join(RAW, 'components-computed.json'), 'utf8'));

async function cropEl(locator, name) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return;
  const pad = 6;
  await locator.page().screenshot({
    path: path.join(CROPS, name + '.png'),
    clip: {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(box.width + pad * 2, 900),
      height: Math.min(box.height + pad * 2, 500),
    },
  });
}

async function record(name, state, locator) {
  if (!(await locator.count())) { log('miss', name, state); return; }
  const loc = locator.first();
  const reading = await styleOf(loc);
  const s = reading.style;
  out.components[name] ??= { states: {} };
  out.components[name].states[state] = {
    text: reading.text,
    rect: reading.rect,
    backgroundColor: s.backgroundColor,
    color: s.color,
    fontFamily: s.fontFamily,
    fontSize: s.fontSize,
    fontWeight: s.fontWeight,
    lineHeight: s.lineHeight,
    letterSpacing: s.letterSpacing,
    borderTopWidth: s.borderTopWidth,
    borderTopColor: s.borderTopColor,
    borderRadius: s.borderTopLeftRadius,
    padding: `${s.paddingTop} ${s.paddingRight} ${s.paddingBottom} ${s.paddingLeft}`,
    boxShadow: s.boxShadow,
    outline: `${s.outlineWidth} ${s.outlineStyle} ${s.outlineColor}`,
    opacity: s.opacity,
    transitionDuration: s.transitionDuration,
    transitionTimingFunction: s.transitionTimingFunction,
  };
  await cropEl(loc, `${name}-${state}`).catch((e) => log('crop', name, e.message.split('\n')[0]));
  log('ok', name, state, reading.rect.w + 'x' + reading.rect.h, s.backgroundColor, s.color, s.fontSize, s.borderTopLeftRadius);
}

const { browser } = await launch();
const desk = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };

{
  const ctx = await contextFor(browser);
  const page = await ctx.newPage();
  await open(page, 'https://leonardo.ai/', 3500);
  const start = page.getByRole('link', { name: 'Start now', exact: true }).first();
  const dev = page.getByRole('link', { name: 'Developer API' }).first();
  const login = page.getByRole('link', { name: 'Log in', exact: true }).first();
  const tutorial = page.getByRole('link', { name: 'Tutorial', exact: true }).first();
  await record('button-primary', 'default', start);
  await start.hover();
  await page.waitForTimeout(350);
  await record('button-primary', 'hover', start);
  await start.focus();
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(150);
  await record('button-primary', 'focus-visible', start);
  await record('button-secondary', 'default', dev);
  await dev.hover();
  await page.waitForTimeout(300);
  await record('button-secondary', 'hover', dev);
  await record('button-login', 'default', login);
  await login.hover();
  await page.waitForTimeout(250);
  await record('button-login', 'hover', login);
  await record('button-tutorial', 'default', tutorial);
  const h1 = page.locator('h1').first();
  await record('display', 'default', h1);
  const word = page.locator('header a, nav a').first();
  await record('wordmark', 'default', word);
  await page.screenshot({ path: path.join(RAW_SHOTS, 'home-dark-start-hover.png') }).catch(() => {});
  await ctx.close();
}

{
  const ctx = await contextFor(browser);
  const page = await ctx.newPage();
  await open(page, 'https://leonardo.ai/pricing', 3000);
  const solo = page.getByRole('tab', { name: 'SOLO' }).first();
  const team = page.getByRole('tab', { name: 'TEAM' }).first();
  const yearly = page.getByRole('button', { name: /Pay Yearly/i }).first();
  const monthly = page.getByRole('button', { name: /Pay Monthly/i }).first();
  const subscribe = page.locator('button').filter({ hasText: /^Subscribe$/ }).first();
  await record('tab', 'selected', solo);
  await record('tab', 'default', team);
  await team.hover();
  await page.waitForTimeout(250);
  if (await team.count()) {
    await team.hover();
    await page.waitForTimeout(250);
    await record('tab', 'hover', team);
  }
  await record('billing-toggle', 'default', yearly);
  await record('billing-toggle', 'selected', monthly);
  await monthly.click();
  await page.waitForTimeout(600);
  await record('billing-toggle', 'selected-after-click', monthly);
  await screenshotWithMetadata(page, { path: path.join(RAW_SHOTS, 'pricing-dark-monthly.png') }, { ...desk, sanitizedSourceUrl: 'https://leonardo.ai/pricing' });
  await record('button-subscribe', 'default', subscribe);
  await subscribe.hover();
  await page.waitForTimeout(250);
  await record('button-subscribe', 'hover', subscribe);
  const badge = page.getByText('Best Offer').first();
  await record('badge', 'default', badge);
  const price = page.getByText('$0').first();
  await record('price', 'default', price);
  await ctx.close();
}

{
  const ctx = await contextFor(browser);
  const page = await ctx.newPage();
  await open(page, 'https://leonardo.ai/contact-us', 2800);
  const support = page.getByRole('button', { name: 'Support and billing' }).first();
  const enterprise = page.getByRole('button', { name: 'Enterprise sales' }).first();
  await record('segment', 'selected', support);
  await record('segment', 'default', enterprise);
  await enterprise.click();
  await page.waitForTimeout(700);
  await screenshotWithMetadata(page, { path: path.join(RAW_SHOTS, 'contact-dark-enterprise.png') }, { ...desk, sanitizedSourceUrl: 'https://leonardo.ai/contact-us' });
  await record('segment', 'selected-after-click', enterprise);
  const field = page.locator('input').first();
  await record('text-field', 'default', field);
  await field.click();
  await page.waitForTimeout(200);
  await record('text-field', 'focus-visible', field);
  const area = page.locator('textarea').first();
  await record('text-area', 'default', area);
  const submit = page.getByRole('button', { name: /Submit/i }).first();
  await record('button-submit', 'default', submit);
  // do not click submit
  await ctx.close();
}

{
  const ctx = await contextFor(browser);
  const page = await ctx.newPage();
  await open(page, 'https://leonardo.ai/learn', 2800);
  const search = page.locator('input').first();
  await record('search-field', 'default', search);
  if (await search.count()) {
    await search.click();
    await page.waitForTimeout(200);
    await record('search-field', 'focus-visible', search);
    await screenshotWithMetadata(page, { path: path.join(RAW_SHOTS, 'learn-dark-search-focused.png') }, { ...desk, sanitizedSourceUrl: 'https://leonardo.ai/learn' });
  }
  await ctx.close();
}

{
  const ctx = await contextFor(browser, { mobile: true });
  const requested = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, sanitizedSourceUrl: 'https://leonardo.ai/' };
  const page = await ctx.newPage();
  const pages = [
    ['home', 'https://leonardo.ai/'],
    ['pricing', 'https://leonardo.ai/pricing'],
    ['image-generator', 'https://leonardo.ai/ai-image-generator'],
    ['contact', 'https://leonardo.ai/contact-us'],
    ['news', 'https://leonardo.ai/news'],
    ['api', 'https://leonardo.ai/api'],
  ];
  for (const [name, url] of pages) {
    log('mobile', name);
    await open(page, url, 2500);
    await screenshotWithMetadata(page, { path: path.join(RAW_SHOTS, `mobile-${name}-dark-default.png`) }, { ...requested, sanitizedSourceUrl: url });
  }
  await open(page, 'https://leonardo.ai/', 2000);
  const toggle = page.getByRole('button', { name: /menu/i }).first();
  await record('nav-toggle', 'default', toggle);
  if (await toggle.count()) {
    await toggle.click();
    await page.waitForTimeout(800);
    await screenshotWithMetadata(page, { path: path.join(RAW_SHOTS, 'mobile-home-dark-menu.png') }, requested);
  }
  await ctx.close();
}

{
  const ctx = await contextFor(browser);
  const page = await ctx.newPage();
  const bodies = new Map();
  page.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
  });
  await open(page, 'https://leonardo.ai/', 4000);
  const live = await page.evaluate(() => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]+\)/g, 'url(…)') : v);
    const rules = [];
    const fonts = [];
    const errors = [];
    const walk = (list, ctx, file) => {
      for (const r of list) {
        try {
          if (r.type === CSSRule.FONT_FACE_RULE) {
            const o = { file };
            for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim()).slice(0, 180);
            fonts.push(o);
            continue;
          }
          if (r.cssRules && !r.style) {
            walk(r.cssRules, [...ctx, r.cssText.split('{')[0].trim().slice(0, 100)], file);
            continue;
          }
          if (!r.style) continue;
          const props = {};
          for (let i = 0; i < r.style.length; i++) {
            const k = r.style[i];
            if (k && k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim()).slice(0, 200);
          }
          if (Object.keys(props).length) rules.push({ file: (file || '').slice(0, 120), selector: (r.selectorText || '').slice(0, 160), context: ctx.slice(0, 4), properties: props });
        } catch (e) { errors.push(String(e).slice(0, 120)); }
      }
    };
    for (const sheet of document.styleSheets) {
      let list;
      try { list = sheet.cssRules; } catch (e) { errors.push('blocked ' + (sheet.href || 'inline')); continue; }
      walk(list, [], sheet.href || 'inline');
    }
    const root = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const names = [...new Set(rules.flatMap((r) => Object.keys(r.properties)))];
    const resolved = {};
    for (const n of names) resolved[n] = noUrl(root.getPropertyValue(n).trim()).slice(0, 200);
    return {
      rules, fonts: fonts.slice(0, 40), errors: errors.slice(0, 20),
      resolved,
      computed: { background: body.backgroundColor, color: body.color, font: body.fontFamily, colorScheme: root.colorScheme },
      themeChecks: { prefersDark: matchMedia('(prefers-color-scheme: dark)').matches, classes: [...document.documentElement.classList].slice(0, 12) },
    };
  });
  fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
    product: 'Leonardo.Ai', captured: '2026-11-21', url: 'https://leonardo.ai/', stylesheetBodies: bodies.size, ...live,
  }, null, 2) + '\n');
  log('css', live.rules.length, 'fonts', live.fonts.length, 'resolved', Object.keys(live.resolved).length);
  await ctx.close();
}

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2) + '\n');
await browser.close();
log('done');
