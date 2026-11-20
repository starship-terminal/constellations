// Read every custom property jace.ai declares and write raw/css-vars.json.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
//
// Two surfaces share one stylesheet origin:
//   marketing  https://jace.ai/ paints a light page. The product token
//              block still loads on :root (dark defaults) and is overridden
//              by :root:where(.light, .light *) when .light is present.
//              The marketing page itself does not add .light; its painted
//              colours come from Tailwind utilities (Geist, Gelica, #2d2d2d).
//   app        https://app.jace.ai/signin paints the dark product theme.
//              Its :root values are the dark theme. Nothing is typed or
//              submitted there.
//
// Each name is resolved in a probe that carries the marketing stylesheets,
// once with html.light (the published light override) and once without
// (the dark :root the sign-in page uses). Colours come back as sRGB.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, APP, launch } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);

const sheets = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
  try { return { name: s.href || 'inline-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') }; }
  catch (e) { return { name: s.href || 'sheet-' + i, media: '', css: '', unreadable: String(e).slice(0, 120) }; }
}));

const live = await page.evaluate(() => {
  const body = getComputedStyle(document.body);
  const h1 = document.querySelector('h1');
  const hc = h1 ? getComputedStyle(h1) : null;
  const root = getComputedStyle(document.documentElement);
  const pick = ['--surface-default', '--text-body-color-default', '--button-background-primary-default', '--font-family-sans', '--font-family-serif', '--motion-enter-duration', '--elevation-raised'];
  const vars = {};
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  for (const n of pick) vars[n] = noUrl(root.getPropertyValue(n).trim());
  return {
    url: location.href,
    bodyBg: body.backgroundColor, bodyColor: body.color, bodyFont: body.fontFamily,
    h1Font: hc && hc.fontFamily, h1Size: hc && hc.fontSize, h1Color: hc && hc.color, h1Weight: hc && hc.fontWeight,
    htmlClass: document.documentElement.className,
    vars,
  };
});
await page.close();

// Sign-in page: read resolved product tokens as the app actually paints them.
// No click, no typing.
const appPage = await context.newPage();
let appLive = null;
try {
  await appPage.goto(APP + '/signin', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await appPage.waitForTimeout(2000);
  appLive = await appPage.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const names = [];
    for (const s of document.styleSheets) {
      let rules; try { rules = [...s.cssRules]; } catch { continue; }
      for (const r of rules) {
        if (!r.style || r.selectorText !== ':root') continue;
        for (let i = 0; i < r.style.length; i++) if (r.style[i].startsWith('--')) names.push(r.style[i]);
      }
    }
    const uniq = [...new Set(names)];
    const resolved = {};
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    for (const n of uniq) resolved[n] = noUrl(root.getPropertyValue(n).trim());
    return {
      url: location.href,
      title: document.title,
      bodyBg: body.backgroundColor,
      bodyColor: body.color,
      bodyFont: body.fontFamily,
      colorScheme: root.colorScheme,
      htmlClass: document.documentElement.className,
      resolved,
    };
  });
} catch (e) {
  appLive = { error: String(e).slice(0, 200) };
}
await appPage.close();

const readable = sheets.filter((s) => s.css);
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const probeBrowser = browser;
const probe = await probeBrowser.newPage({ viewport: { width: 1440, height: 900 } });

const parsed = await probe.evaluate((sheetsIn) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + (r.name || '')
          : r.cssText.split('{')[0].trim();
        walk(r.cssRules, [...ctx, head], file);
        continue;
      }
      if (!r.style) continue;
      const props = {};
      let n = 0;
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (k && k.startsWith('--')) { props[k] = noUrl(r.style.getPropertyValue(k).trim()); n++; }
      }
      if (n) rules.push({ file, selector: r.selectorText, context: ctx, properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText], file);
    }
  };
  for (const s of sheetsIn) {
    const ss = new CSSStyleSheet({ media: s.media || undefined });
    try { ss.replaceSync(s.css); } catch (e) { rules.push({ file: s.name, error: String(e).slice(0, 180) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts };
}, readable.map(({ name, media, css }) => ({ name, media, css })));

const want = [...new Set(parsed.rules.filter((r) => !r.error).flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !/^--(tw-|_|lightningcss-)/.test(n)).sort();

function shell(light) {
  return '<!doctype html><html' + (light ? ' class="light"' : '') + '><head>'
    + readable.map((s) => '<style>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('')
    + '</head><body><div id="probe"></div></body></html>';
}

const resolved = {};
for (const [pass, light] of [['light', true], ['dark', false]]) {
  await probe.setContent(shell(light), { waitUntil: 'load' });
  resolved[pass] = await probe.evaluate((names) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const probeEl = document.getElementById('probe');
    const box = document.createElement('div');
    box.style.cssText = 'position:absolute;visibility:hidden';
    const node = document.createElement('div');
    box.appendChild(node);
    document.body.appendChild(box);
    const out = {};
    for (const name of names) {
      const raw = noUrl(getComputedStyle(probeEl).getPropertyValue(name).trim());
      if (!raw) continue;
      const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
      node.removeAttribute('style');
      if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
      else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert|none)$/.test(raw)) {
        node.style.color = raw;
        r.kind = 'color';
        r.value = getComputedStyle(node).color;
      } else if (!raw.includes('%') && CSS.supports('width', raw) && !/[a-z]{3,}/i.test(raw.replace(/cubic-bezier|var|calc/g, ''))) {
        node.style.width = raw;
        r.kind = 'dimension';
        r.value = getComputedStyle(node).width;
      } else if (CSS.supports('box-shadow', raw)) {
        node.style.boxShadow = raw;
        r.kind = 'shadow';
        r.value = getComputedStyle(node).boxShadow;
      } else if (CSS.supports('transition-duration', raw)) {
        node.style.transitionDuration = raw;
        r.kind = 'duration';
        r.value = getComputedStyle(node).transitionDuration;
      } else if (/cubic-bezier|ease|linear/.test(raw) && CSS.supports('transition-timing-function', raw)) {
        r.kind = 'easing';
        r.value = raw;
      } else if (/[A-Za-z]/.test(raw) && raw.length < 80 && CSS.supports('font-family', raw)) {
        r.kind = 'fontFamily';
        r.value = raw;
      } else r.kind = 'other';
      out[name] = r;
    }
    box.remove();
    return out;
  }, want);
}
await probe.close();
await browser.close();

const THEME = /:root|:where\(\.light|\.light|\.dark|data-theme/;
const binOf = (r) => {
  const names = Object.keys(r.properties || {});
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-')) || (r.context || []).some((c) => c.startsWith('@layer'))) return 'tailwind';
  if (names.some((n) => n.startsWith('--primitives-') || n.startsWith('--theme-') || n.startsWith('--platform-') || n.startsWith('--button-') || n.startsWith('--surface-') || n.startsWith('--text-') || n.startsWith('--motion-') || n.startsWith('--elevation-'))) return 'token';
  if (THEME.test(r.selector || '')) return 'token';
  return 'app';
};
const ok = parsed.rules.filter((r) => !r.error);
for (const r of ok) r.bin = binOf(r);
const names = (bin) => [...new Set(ok.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();

const out = {
  readAt: '2026-11-18',
  source: 'jace.ai CSSOM on 2026-11-18 (marketing /) plus app.jace.ai/signin resolved custom properties. Light pass applies html.light so :root:where(.light) wins; dark pass is bare :root, matching the sign-in page.',
  liveMarketing: live,
  liveSignin: appLive && { url: appLive.url, title: appLive.title, bodyBg: appLive.bodyBg, bodyColor: appLive.bodyColor, bodyFont: appLive.bodyFont, colorScheme: appLive.colorScheme, htmlClass: appLive.htmlClass, error: appLive.error, resolvedCount: appLive.resolved ? Object.keys(appLive.resolved).length : 0 },
  signinResolved: appLive && appLive.resolved ? appLive.resolved : {},
  sheets: sheets.map(({ name, media, css, unreadable }) => ({ name, media, bytes: (css || '').length, unreadable })),
  counts: { rules: ok.length, fonts: parsed.fonts.length, names: { token: names('token').length, app: names('app').length, utility: names('utility').length, tailwind: names('tailwind').length } },
  errors: parsed.rules.filter((r) => r.error),
  token: ok.filter((r) => r.bin === 'token'),
  app: ok.filter((r) => r.bin === 'app'),
  utility: ok.filter((r) => r.bin === 'utility'),
  tailwind: ok.filter((r) => r.bin === 'tailwind'),
  fonts: parsed.fonts,
  resolved,
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('rules', ok.length, 'fonts', parsed.fonts.length, 'token names', names('token').length);
console.log('resolved light', Object.keys(resolved.light).length, 'dark', Object.keys(resolved.dark).length);
console.log('signin resolved', appLive && appLive.resolved ? Object.keys(appLive.resolved).length : appLive);
console.log('marketing live', live);
