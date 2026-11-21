// Leonardo.Ai public capture. Screenshots, CSS variables, component states.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/run.mjs
//
// Writes full-colour PNGs to ~/.design-systems/leonardo/raw-shots and readings
// to systems/leonardo/raw. Does not submit forms, type private data, or follow
// auth (Canva, Apple, Google, Microsoft, email login).
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from './screenshot.mjs';
import { launch, contextFor, open, hideConsent, styleOf, PROPS, PKG } from './public/lib.mjs';

const RAW_SHOTS = path.join(os.homedir(), '.design-systems', 'leonardo', 'raw-shots');
const RAW = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(RAW_SHOTS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const PAGES = [
  ['home', 'https://leonardo.ai/'],
  ['pricing', 'https://leonardo.ai/pricing'],
  ['api', 'https://leonardo.ai/api'],
  ['image-generator', 'https://leonardo.ai/ai-image-generator'],
  ['models', 'https://leonardo.ai/models'],
  ['tools', 'https://leonardo.ai/ai-tools'],
  ['gpt-image', 'https://leonardo.ai/gpt-image-2-6'],
  ['contact', 'https://leonardo.ai/contact-us'],
  ['learn', 'https://leonardo.ai/learn'],
  ['news', 'https://leonardo.ai/news'],
  ['article', 'https://leonardo.ai/news/how-to-use-leonardo-ai'],
  ['team', 'https://leonardo.ai/team-plans'],
  ['careers', 'https://leonardo.ai/careers'],
  ['privacy', 'https://leonardo.ai/privacy-policy'],
  ['not-found', 'https://leonardo.ai/login'],
];

async function shot(page, file, requested) {
  await screenshotWithMetadata(page, { path: file }, requested);
  log('  shot', path.basename(file));
}

async function fullPage(page, file, requested) {
  await page.evaluate(async () => {
    const h = Math.min(document.documentElement.scrollHeight, 7200);
    for (let y = 0; y < h; y += 700) {
      scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 120));
    }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(500);
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const cap = Math.min(H, 7200);
  if (H > 7200) log('  ! truncated full page at 7200 of', H);
  await screenshotWithMetadata(page, {
    path: file,
    fullPage: true,
    clip: H > 7200 ? { x: 0, y: 0, width: requested.viewport.width, height: cap } : undefined,
  }, requested);
  await page.evaluate(() => scrollTo(0, 0));
  log('  full', path.basename(file), 'H=' + H);
}

async function cropEl(locator, name) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 8;
  const file = path.join(CROPS, name + '.png');
  await locator.page().screenshot({
    path: file,
    clip: {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(box.width + pad * 2, 1440),
      height: Math.min(box.height + pad * 2, 800),
    },
  });
  return file;
}

function pickStyle(reading) {
  if (!reading) return null;
  const s = reading.style;
  return {
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
    transitionDuration: s.transitionDuration,
    transitionTimingFunction: s.transitionTimingFunction,
  };
}

const { browser } = await launch();
const components = { _meta: { product: 'Leonardo.Ai', captured: '2026-11-21', route: 'public headless Playwright', props: PROPS }, components: {} };

async function record(name, state, locator) {
  const n = await locator.count();
  if (!n) {
    log('  miss', name, state);
    return;
  }
  const loc = locator.first();
  try {
    const reading = await styleOf(loc);
    components.components[name] ??= { states: {} };
    components.components[name].states[state] = pickStyle(reading);
    if (['default', 'hover', 'focus-visible', 'open', 'filled-not-submitted'].includes(state)) {
      await cropEl(loc, `${name}-${state}`).catch((e) => log('  crop fail', name, e.message.split('\n')[0]));
    }
    log('  measured', name, state, reading.rect.w + 'x' + reading.rect.h, reading.style.backgroundColor, reading.style.color);
  } catch (e) {
    log('  measure fail', name, state, e.message.split('\n')[0]);
  }
}

// ---- desktop ----
{
  const ctx = await contextFor(browser, { mobile: false });
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: 'https://leonardo.ai/' };
  const page = await ctx.newPage();
  for (const [name, url] of PAGES) {
    log('page', name, url);
    try {
      const status = await open(page, url, name === 'home' ? 4500 : 2800);
      const title = await page.title();
      log('  status', status, title.slice(0, 80));
      if (/just a moment|cloudflare/i.test(title)) {
        log('  blocked');
        continue;
      }
      await shot(page, path.join(RAW_SHOTS, `${name}-dark-default.png`), { ...requested, sanitizedSourceUrl: url.split('?')[0] });
      if (['home', 'pricing', 'image-generator', 'api', 'contact', 'news'].includes(name)) {
        await fullPage(page, path.join(RAW_SHOTS, `${name}-dark-full.png`), { ...requested, sanitizedSourceUrl: url.split('?')[0] });
      }
    } catch (e) {
      log('  PAGE FAILED', name, e.message.split('\n')[0]);
    }
  }

  // interactions on home
  log('interactions home');
  await open(page, 'https://leonardo.ai/', 3000);
  const cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');

  const createBtn = page.getByRole('button', { name: 'Create', exact: true }).first();
  await record('nav-menu-button', 'default', createBtn);
  await createBtn.hover();
  await page.waitForTimeout(700);
  await record('nav-menu-button', 'hover', createBtn);
  await shot(page, path.join(RAW_SHOTS, 'home-dark-create-menu.png'), requested);
  // menu panel: a large visible region under the header
  const menuPanel = page.locator('a[href="/ai-image-generator"]').first();
  await record('menu-link', 'default', menuPanel);
  await menuPanel.hover();
  await page.waitForTimeout(400);
  await record('menu-link', 'hover', menuPanel);
  await page.keyboard.press('Escape');
  await page.mouse.move(700, 800);
  await page.waitForTimeout(400);

  const pricing = page.getByRole('link', { name: 'Pricing', exact: true }).first();
  await record('nav-link', 'default', pricing);
  await pricing.hover();
  await page.waitForTimeout(350);
  await record('nav-link', 'hover', pricing);
  await pricing.focus();
  await page.waitForTimeout(200);
  await record('nav-link', 'focus-visible', pricing);

  const start = page.getByRole('link', { name: /^Start now$/ }).first();
  if (await start.count()) {
    await start.scrollIntoViewIfNeeded();
    await record('button-primary', 'default', start);
    await start.hover();
    await page.waitForTimeout(400);
    await record('button-primary', 'hover', start);
    await record('button-primary', 'pressed', start);
    await shot(page, path.join(RAW_SHOTS, 'home-dark-start-hover.png'), requested);
  }

  const dev = page.getByRole('link', { name: 'Developer API' }).first();
  await record('button-secondary', 'default', dev);
  await dev.hover();
  await page.waitForTimeout(300);
  await record('button-secondary', 'hover', dev);

  // unmute is an icon button
  const unmute = page.getByRole('button', { name: 'Unmute' }).first();
  await record('icon-button', 'default', unmute);
  if (await unmute.count()) {
    await unmute.hover();
    await page.waitForTimeout(250);
    await record('icon-button', 'hover', unmute);
  }

  await ctx.close();
}

// contact form states, not submitted
{
  const ctx = await contextFor(browser, { mobile: false });
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: 'https://leonardo.ai/contact-us' };
  const page = await ctx.newPage();
  log('contact states');
  await open(page, 'https://leonardo.ai/contact-us', 3000);
  const field = page.locator('input[name="username"]').first();
  await record('text-field', 'default', field);
  if (await field.count()) {
    await field.click();
    await page.waitForTimeout(200);
    await record('text-field', 'focus-visible', field);
    await field.fill('Sample');
    await page.waitForTimeout(200);
    await record('text-field', 'filled-not-submitted', field);
    await field.fill('');
    await shot(page, path.join(RAW_SHOTS, 'contact-dark-field-focused.png'), requested);
  }
  const area = page.locator('textarea[name="message"]').first();
  await record('text-area', 'default', area);
  const select = page.locator('select[name="country"]').first();
  await record('select', 'default', select);
  if (await select.count()) {
    await select.focus();
    await page.waitForTimeout(200);
    await record('select', 'focus-visible', select);
    // open the native select visually is OS-level; record focus only, do not choose a country
  }
  await ctx.close();
}

// learn search, not submitted
{
  const ctx = await contextFor(browser, { mobile: false });
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: 'https://leonardo.ai/learn' };
  const page = await ctx.newPage();
  log('learn search');
  await open(page, 'https://leonardo.ai/learn', 3000);
  const search = page.locator('input[placeholder*="Search"]').first();
  await record('search-field', 'default', search);
  if (await search.count()) {
    await search.click();
    await page.waitForTimeout(250);
    await record('search-field', 'focus-visible', search);
    await shot(page, path.join(RAW_SHOTS, 'learn-dark-search-focused.png'), requested);
  }
  await ctx.close();
}

// pricing controls
{
  const ctx = await contextFor(browser, { mobile: false });
  const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: 'https://leonardo.ai/pricing' };
  const page = await ctx.newPage();
  log('pricing controls');
  await open(page, 'https://leonardo.ai/pricing', 3000);
  const buttons = await page.locator('button').evaluateAll((els) => els.map((e) => (e.innerText || e.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60)).filter(Boolean));
  log('  pricing buttons', buttons.slice(0, 25).join(' | '));
  fs.writeFileSync(path.join(RAW, 'pricing-buttons.json'), JSON.stringify(buttons, null, 2));
  // card
  const card = page.locator('h2, h3').filter({ hasText: /free|pro|team|api/i }).first();
  await record('plan-heading', 'default', card);
  const cta = page.getByRole('link', { name: /start|get started|contact|choose/i }).first();
  await record('plan-cta', 'default', cta);
  if (await cta.count()) {
    await cta.hover();
    await page.waitForTimeout(300);
    await record('plan-cta', 'hover', cta);
  }
  await ctx.close();
}

// phone
{
  const ctx = await contextFor(browser, { mobile: true });
  const requested = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, sanitizedSourceUrl: 'https://leonardo.ai/' };
  const page = await ctx.newPage();
  const mobilePages = [
    ['home', 'https://leonardo.ai/'],
    ['pricing', 'https://leonardo.ai/pricing'],
    ['image-generator', 'https://leonardo.ai/ai-image-generator'],
    ['contact', 'https://leonardo.ai/contact-us'],
    ['news', 'https://leonardo.ai/news'],
    ['api', 'https://leonardo.ai/api'],
  ];
  for (const [name, url] of mobilePages) {
    log('mobile', name);
    try {
      await open(page, url, 2800);
      await shot(page, path.join(RAW_SHOTS, `mobile-${name}-dark-default.png`), { ...requested, sanitizedSourceUrl: url });
      if (name === 'home' || name === 'pricing') {
        await fullPage(page, path.join(RAW_SHOTS, `mobile-${name}-dark-full.png`), { ...requested, sanitizedSourceUrl: url });
      }
    } catch (e) {
      log('  MOBILE FAILED', name, e.message.split('\n')[0]);
    }
  }
  log('mobile menu');
  await open(page, 'https://leonardo.ai/', 2500);
  const toggle = page.getByRole('button', { name: /menu/i }).first();
  await record('nav-toggle', 'default', toggle);
  if (await toggle.count()) {
    await toggle.click();
    await page.waitForTimeout(800);
    await shot(page, path.join(RAW_SHOTS, 'mobile-home-dark-menu.png'), requested);
    await record('nav-toggle', 'open', toggle);
  }
  await ctx.close();
}

// CSS variables from live stylesheets
{
  const ctx = await contextFor(browser, { mobile: false });
  const page = await ctx.newPage();
  const bodies = new Map();
  page.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* gone */ }
  });
  log('css harvest');
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
            for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
            fonts.push(o);
            continue;
          }
          if (r.cssRules && !r.style) {
            const head = r.cssText.split('{')[0].trim().slice(0, 120);
            walk(r.cssRules, [...ctx, head], file);
            continue;
          }
          if (!r.style) continue;
          const props = {};
          for (let i = 0; i < r.style.length; i++) {
            const k = r.style[i];
            if (k && k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim());
          }
          if (Object.keys(props).length) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
        } catch (e) { errors.push(String(e).slice(0, 160)); }
      }
    };
    for (const sheet of document.styleSheets) {
      let list;
      try { list = sheet.cssRules; } catch (e) { errors.push('blocked ' + (sheet.href || 'inline')); continue; }
      walk(list, [], sheet.href || 'inline');
    }
    const cs = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const names = new Set(rules.flatMap((r) => Object.keys(r.properties)));
    const resolved = {};
    for (const n of names) resolved[n] = noUrl(cs.getPropertyValue(n).trim());
    return {
      rules, fonts, errors,
      resolved,
      computed: {
        htmlBackground: body.backgroundColor,
        htmlColor: body.color,
        htmlFont: body.fontFamily,
        colorScheme: cs.colorScheme,
      },
      themeChecks: {
        prefersDark: matchMedia('(prefers-color-scheme: dark)').matches,
        classList: [...document.documentElement.classList],
      },
    };
  });
  const dump = {
    product: 'Leonardo.Ai',
    captured: '2026-11-21',
    url: 'https://leonardo.ai/',
    stylesheetCount: bodies.size,
    ...live,
  };
  fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(dump, null, 2) + '\n');
  log('  rules', live.rules.length, 'fonts', live.fonts.length, 'resolved', Object.keys(live.resolved).length, 'errors', live.errors.length);
  await ctx.close();
}

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(components, null, 2) + '\n');
await browser.close();
log('done');
