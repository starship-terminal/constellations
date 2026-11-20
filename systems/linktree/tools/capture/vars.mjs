// Reads every custom property linktr.ee's public stylesheets declare and writes
// raw/css-vars.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
//
// The marketing site is a Tailwind v4 app (Linksans on :root, --color-* and
// --text-* scales). Profile pages ship a second bundle. Both are read from the
// live CSSOM where the browser allows it, and unreadable sheets are fetched.
// A dark class probe is recorded separately: the captured pages paint light.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { BASE, PROFILE, launch, closePromo, clearChallenge } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');

const { browser, context } = await launch();
const sheets = [];
const seen = new Set();
const URLS = [BASE + '/', BASE + '/s/pricing', PROFILE];
const skipped = [];   // pages not read this run, saved with the readings
for (const url of URLS) {
  const page = await context.newPage();
  try { await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }); }
  catch (e) { skipped.push({ url, reason: String(e.message).split('\n')[0].slice(0, 160) }); console.log('skip', url, skipped.at(-1).reason); await page.close(); continue; }
  if (!(await clearChallenge(page))) { skipped.push({ url, reason: 'bot check did not clear: recorded as a boundary, not bypassed' }); console.log('skip', url, skipped.at(-1).reason); await page.close(); continue; }
  await page.waitForTimeout(4000);
  await closePromo(page);
  const found = await page.evaluate(() => [...document.styleSheets].map((s, i) => {
    // A sheet's query (Vercel's ?dpl= deploy id, cache busters) is not part of its name.
    try { return { name: s.href ? s.href.split(/[?#]/)[0] : 'inline-' + location.pathname + '-' + i, media: s.media.mediaText || '', css: [...s.cssRules].map((r) => r.cssText).join('\n') }; }
    catch { return { name: s.href ? s.href.split(/[?#]/)[0] : 'sheet-' + i, href: s.href || '', media: '', css: '', unreadable: true }; }
  }));
  for (const s of found) {
    const key = s.name + ':' + (s.css || '').length;
    if (seen.has(key)) continue;
    seen.add(key);
    sheets.push(s);
  }
  await page.close();
}
for (const s of sheets) {
  if (!s.unreadable || !/^https?:/.test(s.name)) continue;
  try {
    const res = await fetch(s.href || s.name);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    s.css = await res.text();
    s.fetched = true;
    delete s.unreadable;
    console.log('fetched', s.name.slice(0, 100), s.css.length);
  } catch (e) {
    s.fetchError = String(e.message || e);
  }
}

// A run that read no page keeps the committed readings: writing now would
// replace them with an empty file and still exit 0.
if (skipped.length === URLS.length) {
  console.error('no page was read; raw/css-vars.json left as it was');
  await browser.close();
  process.exit(1);
}

const probe = await browser.newPage();
const result = await probe.evaluate((sheets) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rules = [];
  const fonts = [];
  const errors = [];
  const walk = (list, ctx, file) => {
    for (const r of list) {
      if (r.type === CSSRule.FONT_FACE_RULE) {
        const o = { file: String(file).slice(0, 180) };
        for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim());
        fonts.push(o);
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r.type === CSSRule.MEDIA_RULE ? '@media ' + r.media.mediaText
          : r.type === CSSRule.SUPPORTS_RULE ? '@supports ' + r.conditionText
          : r.constructor.name === 'CSSLayerBlockRule' ? '@layer ' + r.name
          : r.constructor.name === 'CSSContainerRule' ? '@container ' + r.conditionText
          : (r.cssText || '').split('{')[0].trim().slice(0, 80);
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
      if (n) rules.push({ file: String(file).slice(0, 180), selector: (r.selectorText || '').slice(0, 160), context: ctx.slice(0, 4), properties: props });
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, (r.selectorText || '').slice(0, 80)], file);
    }
  };
  for (const s of sheets) {
    if (!s.css) { errors.push({ file: s.name, error: s.fetchError || 'unreadable' }); continue; }
    const ss = new CSSStyleSheet();
    try { ss.replaceSync(s.css); } catch (e) { errors.push({ file: s.name, error: String(e).slice(0, 160) }); continue; }
    walk(ss.cssRules, [], s.name);
  }
  return { rules, fonts, errors };
}, sheets);

const want = [...new Set(result.rules.flatMap((r) => Object.keys(r.properties)))]
  .filter((n) => !n.startsWith('--tw-')).sort();
const probe2 = await browser.newPage({ viewport: { width: 1440, height: 900 } });
const cssJoin = sheets.filter((s) => s.css).map((s) => '<style>' + s.css.replace(/<\/style/gi, '<\\/style') + '</style>').join('');
await probe2.setContent('<!doctype html><html><head>' + cssJoin + '</head><body><div id="probe-root"></div></body></html>', { waitUntil: 'load' });
const resolveAll = async (cls) => await probe2.evaluate(([names, cls]) => {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const rootProbe = document.getElementById('probe-root');
  document.documentElement.className = cls;
  const box = document.createElement('div');
  const probeEl = document.createElement('div');
  probeEl.style.cssText = 'position:absolute;left:0;top:0';
  box.appendChild(probeEl);
  document.body.appendChild(box);
  const norm = (c) => {
    const m = c.match(/^rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)$/);
    if (!m) return { unparsed: c };
    const rgb = [m[1], m[2], m[3]].map((v) => Math.round(+v));
    const a = m[4] === undefined ? 1 : Math.round(+m[4] * 1000) / 1000;
    return a === 1 ? '#' + rgb.map((v) => v.toString(16).padStart(2, '0')).join('') : `rgba(${rgb.join(', ')}, ${a})`;
  };
  const out = {};
  for (const name of names) {
    const raw = noUrl(getComputedStyle(rootProbe).getPropertyValue(name).trim());
    if (!raw) continue;
    const r = { raw: raw.length > 240 ? raw.slice(0, 240) + '…' : raw };
    probeEl.removeAttribute('style');
    probeEl.style.cssText = 'position:absolute;left:0;top:0';
    if (/^-?\d*\.?\d+$/.test(raw)) { r.kind = 'number'; r.value = +raw; }
    else if (CSS.supports('color', raw) && !/^(inherit|initial|unset|revert)$/.test(raw)) {
      probeEl.style.color = raw;
      r.kind = 'color';
      r.value = norm(getComputedStyle(probeEl).color);
      if (typeof r.value === 'object') { r.kind = 'other'; r.note = r.value.unparsed; delete r.value; }
    } else if (!raw.includes('%') && CSS.supports('width', raw)) {
      probeEl.style.width = raw;
      r.kind = 'dimension';
      r.value = getComputedStyle(probeEl).width;
    } else r.kind = 'other';
    out[name] = r;
  }
  box.remove();
  return out;
}, [want, cls]);
const resolved = await resolveAll('');
const resolvedDark = await resolveAll('dark');
await browser.close();

const binOf = (r) => {
  const names = Object.keys(r.properties);
  if (/\\\[--/.test(r.selector || '')) return 'utility';
  if (names.every((n) => n.startsWith('--tw-'))) return 'tailwind';
  if ((r.context || []).some((c) => /@layer theme|@layer properties/.test(c)) || names.every((n) => /^--(color|font|text|spacing|breakpoint|container|radius|shadow|ease|animate|tracking|leading)-/.test(n))) return 'theme';
  return 'app';
};
for (const r of result.rules) r.bin = binOf(r);
const names = (bin) => [...new Set(result.rules.filter((r) => r.bin === bin).flatMap((r) => Object.keys(r.properties)))].sort();
const out = {
  readAt: new Date().toISOString().slice(0, 10),
  source: 'linktr.ee public marketing and profile stylesheets, read from the live CSSOM and fetched where cross-origin. The dark probe adds a class the captured pages do not paint.',
  sheets: sheets.map(({ name, media, css, fetched }) => ({ name: String(name).slice(0, 180), media, bytes: (css || '').length, ...(fetched ? { fetched: true } : {}) })),
  counts: {
    rules: result.rules.length,
    fonts: result.fonts.length,
    names: { theme: names('theme').length, app: names('app').length, tailwind: names('tailwind').length, utility: names('utility').length },
  },
  errors: result.errors,
  ...(skipped.length ? { skippedPages: skipped } : {}),
  theme: result.rules.filter((r) => r.bin === 'theme').slice(0, 400),
  app: result.rules.filter((r) => r.bin === 'app').slice(0, 200),
  fonts: result.fonts.slice(0, 80),
  resolved: { light: resolved, dark: resolvedDark },
};
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'css-vars.json'), JSON.stringify(out, null, 1) + '\n');
console.log('css-vars', out.counts, 'resolved', Object.keys(resolved).length, 'dark', Object.keys(resolvedDark).length);
