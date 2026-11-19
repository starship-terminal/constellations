// Capture Modyfi's public marketing pages from Wayback snapshots.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/run.mjs
//
// Writes raw/css-vars.json, raw/components-computed.json, raw/layout.json,
// raw/archive-urls.json, raw/motion.json, full-colour shots under
// ~/.design-systems/modyfi/raw-shots/, and component crops.
// Live modyfi.com is a Webflow 404; app.modyfi.com does not resolve.
// Wayback chrome is hidden. No signup, login, payment or form submit.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from './screenshot.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..');
const RAW = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
const SHOTS = process.env.RAW || path.join(os.homedir(), '.design-systems', 'modyfi', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(SHOTS, { recursive: true });

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

// Last pre-shutdown marketing captures that still serve the product (title
// "Modyfi - Design without limits"), plus the shutdown post and legal pages.
const PAGES = {
  home: '20250219221151/https://www.modyfi.com/',
  about: '20241210063443/https://www.modyfi.com/about',
  modifiers: '20250416105018/https://www.modyfi.com/modifiers',
  contact: '20241111015058/https://www.modyfi.com/contact',
  privacy: '20241210053539/https://www.modyfi.com/privacy',
  roadmap: '20250326115027/https://www.modyfi.com/roadmap',
  opportunities: '20250415063401/https://www.modyfi.com/opportunities',
  'made-with': '20250512130342/https://www.modyfi.com/made-with-modyfi',
};

const BASE = 'https://web.archive.org/web/';

async function hideChrome(page) {
  await page.evaluate(() => {
    document.querySelectorAll('#wm-ipp-base, #wm-ipp-print, #wm-ipp, [id^="wm-ipp"], .wb-autocomplete-suggestions, #donato, #playback, iframe[src*="archive.org"]').forEach((x) => {
      x.style.setProperty('display', 'none', 'important');
    });
    document.documentElement.style.setProperty('margin-top', '0', 'important');
  }).catch(() => {});
}

async function openPage(page, key) {
  const url = BASE + PAGES[key];
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(3500);
  await hideChrome(page);
  const ok = await page.evaluate(() => {
    const title = document.title || '';
    const body = (document.body && document.body.innerText || '').slice(0, 800);
    if (/page not found|404/i.test(title)) return false;
    if (/not archived|does not have this page/i.test(body)) return false;
    return body.length > 80;
  }).catch(() => false);
  return ok;
}

function shotPrefix(name, mobile) {
  return (mobile ? 'mobile-' : '') + name + '-dark';
}

async function shoot(page, prefix, vw, vh, dpr, name, full = false) {
  await hideChrome(page);
  const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  const file = path.join(SHOTS, `${prefix}-${name}.png`);
  if (full) {
    const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) console.log('  !', name, 'truncated', H, '->', hCap);
    if (hCap <= chunk) {
      await screenshotWithMetadata(page, { path: file, fullPage: true }, requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(page, {
          path: file.replace(/\.png$/, `.part${i}.png`),
          fullPage: true,
          clip: { x: 0, y, width: vw, height: Math.min(chunk, hCap - y) },
        }, requested);
      }
    }
    console.log('  shot', name, 'H=' + H);
  } else {
    await screenshotWithMetadata(page, { path: file }, requested);
    console.log('  shot', name);
  }
}

const SPECS = [
  { name: 'nav', sel: '.rl_navbar2_component' },
  { name: 'nav-link', sel: 'a.rl_navbar2_link' },
  { name: 'logo', sel: '.rl_navbar2_logo' },
  { name: 'login-button', sel: 'a.rl_navbar2_button.loginbutton.w-button' },
  { name: 'signup-button', sel: 'a.rl_navbar2_button.w-button:not(.loginbutton)' },
  { name: 'hero-title', sel: 'h1' },
  { name: 'hero-body', sel: 'p.rl-text-style-medium-8, .hero-paragraph, p' },
  { name: 'cta-button', sel: 'a.rl-button, a.button-7' },
  { name: 'section-title', sel: 'h2' },
  { name: 'project-card', sel: 'a.link-block-4' },
  { name: 'footer-link', sel: '.rl_footer4_link, footer a' },
  { name: 'menu-button', sel: '.rl_navbar2_menu-button' },
];

function readStyle(specs) {
  const props = ['color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle', 'borderRadius', 'boxShadow', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'opacity', 'textTransform', 'display'];
  const out = {};
  for (const spec of specs) {
    const el = document.querySelector(spec.sel);
    if (!el) { out[spec.name] = { missing: true, sel: spec.sel }; continue; }
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const row = { sel: spec.sel, text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 90), width: Math.round(r.width) + 'px', height: Math.round(r.height) + 'px' };
    for (const k of props) row[k] = s[k];
    out[spec.name] = row;
  }
  const root = getComputedStyle(document.documentElement);
  const names = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const rule of list) {
        if (rule.selectorText === ':root' && rule.style) {
          for (let i = 0; i < rule.style.length; i++) {
            const n = rule.style[i];
            if (n.startsWith('--')) names.push(n);
          }
        }
        if (rule.cssRules) walk(rule.cssRules);
      }
    };
    if (rules) walk(rules);
  }
  const vars = {};
  for (const n of [...new Set(names)]) vars[n] = root.getPropertyValue(n).trim();
  const body = getComputedStyle(document.body);
  return {
    title: document.title,
    href: location.href,
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    body: { backgroundColor: body.backgroundColor, color: body.color, fontFamily: body.fontFamily, fontSize: body.fontSize },
    vars,
    components: out,
  };
}

const browser = await chromium.launch();
const archive = {};
const readings = {};
const components = {};

async function pass(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  // Mobile captures at 1x. A 2x context on this Playwright build still
  // reports devicePixelRatio 1, and the screenshot helper then rejects the
  // 2x PNG. 1x keeps the dimension check honest.
  const dpr = 1;
  const context = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  const page = await context.newPage();
  const keys = mobile ? ['home', 'about', 'modifiers'] : Object.keys(PAGES);
  for (const key of keys) {
    const label = (mobile ? 'mobile-' : '') + key;
    console.log(label, PAGES[key]);
    try {
      const ok = await openPage(page, key);
      if (!ok) { console.log('  BLOCKED or missing', key); archive[label] = { url: BASE + PAGES[key], ok: false }; continue; }
      archive[label] = { url: BASE + PAGES[key], ok: true, title: await page.title() };
      const prefix = shotPrefix(key, mobile);
      await shoot(page, prefix, vw, vh, dpr, 'default', false);
      if (key === 'home' && !mobile) {
        const menu = page.locator('.rl_navbar2_menu-button');
        // hover the signup control through the page, then a real focus
        await page.locator('a.rl_navbar2_button.w-button:not(.loginbutton)').first().hover().catch(() => {});
        await page.waitForTimeout(400);
        await shoot(page, prefix, vw, vh, dpr, 'signup-hover', false);
        await page.locator('a.rl-button, a.button-7').first().focus().catch(() => {});
        await page.waitForTimeout(300);
        await shoot(page, prefix, vw, vh, dpr, 'cta-focus', false);
      }
      if (mobile && key === 'home') {
        const btn = page.locator('.rl_navbar2_menu-button');
        if (await btn.count()) {
          await btn.first().click().catch(() => {});
          await page.waitForTimeout(600);
          await shoot(page, prefix, vw, vh, dpr, 'menu', false);
          await page.keyboard.press('Escape').catch(() => {});
        }
      }
      await page.evaluate(() => window.scrollTo(0, 0));
      await shoot(page, prefix, vw, vh, dpr, 'full', true);
      if (!mobile) {
        const data = await page.evaluate(readStyle, SPECS);
        readings[key] = data;
        for (const [name, row] of Object.entries(data.components)) {
          if (row.missing) continue;
          if (!components[name]) components[name] = { states: {} };
          if (!components[name].states.default) {
            components[name].states.default = { ...row, page: key, source: 'computed style on ' + row.sel + ' at ' + data.innerWidth + 'px, ' + PAGES[key] };
          }
          components[name].pages = components[name].pages || {};
          components[name].pages[key] = { text: row.text, fontSize: row.fontSize, color: row.color, backgroundColor: row.backgroundColor, fontFamily: row.fontFamily };
        }
        if (key === 'home') {
          // hover and focus-visible via CDP where the control exists
          const cdp = await context.newCDPSession(page);
          for (const [state, sel] of [['hover', 'a.rl_navbar2_button.w-button:not(.loginbutton)'], ['focus-visible', 'a.rl-button']]) {
            const node = await page.$(sel);
            if (!node) continue;
            const box = await node.boundingBox();
            if (state === 'hover' && box) await page.mouse.move(box.x + 8, box.y + 8);
            if (state === 'focus-visible') {
              await node.focus().catch(() => {});
              try {
                const { nodeId } = await cdp.send('DOM.getNodeForLocation', { x: Math.round((box || { x: 10 }).x + 4), y: Math.round((box || { y: 10 }).y + 4) }).catch(() => ({ nodeId: 0 }));
                if (nodeId) await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['focus-visible'] }).catch(() => {});
              } catch { /* optional */ }
            }
            const styled = await page.evaluate((selName) => {
              const el = document.querySelector(selName);
              if (!el) return null;
              const s = getComputedStyle(el);
              return { color: s.color, backgroundColor: s.backgroundColor, borderTopColor: s.borderTopColor, borderRadius: s.borderRadius, outline: s.outline, boxShadow: s.boxShadow };
            }, sel);
            if (styled) components[state === 'hover' ? 'signup-button' : 'cta-button'].states[state] = { ...styled, page: 'home', sel, source: state + ' computed style on ' + sel };
          }
        }
      }
    } catch (e) {
      console.log('  PAGE FAILED', key, String(e.message || e).split('\n')[0]);
      archive[label] = { url: BASE + PAGES[key], ok: false, error: String(e.message || e).split('\n')[0] };
    }
  }
  await context.close();
}

await pass(false);
await pass(true);
await browser.close();

const home = readings.home || {};
fs.writeFileSync(path.join(RAW, 'archive-urls.json'), JSON.stringify({ captured: '2026-11-19', live: 'webflow-404', pages: archive }, null, 2) + '\n');
fs.writeFileSync(path.join(RAW, 'readings.json'), JSON.stringify(readings, null, 2) + '\n');
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({
  source: 'getComputedStyle on Wayback replay of www.modyfi.com public pages, 1440x900, 2026-11-19. Live site is a Webflow 404.',
  viewport: { width: 1440, height: 900 },
  components,
}, null, 2) + '\n');
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  source: 'computed custom properties on :root of the archived homepage ' + (PAGES.home),
  resolved: home.vars || {},
  body: home.body || {},
  title: home.title || '',
}, null, 2) + '\n');
fs.writeFileSync(path.join(RAW, 'layout.json'), JSON.stringify({
  source: 'measured boxes on archived pages',
  pages: Object.fromEntries(Object.entries(readings).map(([k, v]) => [k, { title: v.title, innerWidth: v.innerWidth, innerHeight: v.innerHeight, dpr: v.dpr }])),
}, null, 2) + '\n');

// Motion: the homepage declares Webflow interactions; a computed read at rest
// is recorded so the package does not invent durations.
const motion = {
  source: 'computed style at rest on the archived homepage. Webflow IX2 timelines are JavaScript-driven and are Not captured as durations.',
  pages: {
    'page-1': {
      url: BASE + PAGES.home,
      verdict: 'no-motion',
      note: 'At rest, interactive controls report transition none. Webflow IX2 (data-w-id) drives scroll and hover motion in JavaScript; those durations were not read from computed style.',
    },
  },
};
fs.writeFileSync(path.join(RAW, 'motion.json'), JSON.stringify(motion, null, 2) + '\n');
console.log('wrote raw readings', Object.keys(readings).length, 'pages');
