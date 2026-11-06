// Dump every custom property the running app's stylesheets declare, with where it is declared
// and the value it computes to now, on the elements that scope the theme. Generic.
//
//   PORT=9401 KEEP='^--(cursor|glass|ui)-' node tools/capture/electron/vars.mjs <out.json> "<window title>" [scope selector ...]
//
// Writes { meta, sheets, decls: [{name, value, selector, condition, sheet}], computed: {scope: {name: value}},
// colors: {name: colour as painted}, shadows: {name: box-shadow as painted}, conditions: {condition: {rules, selectors}},
// fonts: { faces, body, scope } }. KEEP (a regex) limits which names are written. Run once per theme;
// the theme on screen decides `computed`, `colors` and `shadows`, which are read on the first scope
// (or body), the element whose inline style a theme engine usually writes. `channels` lists the names
// whose value is a bare channel triplet (Tailwind's rgb(var(--x)) convention), painted that way.
import { connect, disconnect, viewport, writeJson } from './cdp.mjs';

const [out, title, ...scopes] = process.argv.slice(2);
if (!out || !title) { console.error('usage: vars.mjs <out.json> "<window title>" [scope ...]'); process.exit(2); }
// A title starting with "url:" picks the window by its URL instead (a regex), for apps whose windows share a title.
const { browser, page } = await connect(title.startsWith("url:") ? { url: new RegExp(title.slice(4)) } : title);
const meta = await viewport(page);
const data = await page.evaluate(({ scopes, keep }) => {
  // A custom property can hold a url() with a signed or per-account query: record it as url(…).
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
  const KEEP = new RegExp(keep || '^--');
  const sheets = [], decls = [], names = new Set(), conditions = {};
  [...document.styleSheets].forEach((s, i) => {
    const owner = s.ownerNode;
    const id = s.href ? s.href.split('/').slice(-1)[0] : (owner && (owner.id || owner.className || owner.getAttribute('data-name'))) || `inline-${i}`;
    let rules; try { rules = s.cssRules; } catch { sheets.push({ id, unreadable: true }); return; }
    sheets.push({ id, rules: rules.length });
    const walk = (rs, cond) => {
      for (const r of rs) {
        if (r.cssRules && !r.style) {
          const c = r.conditionText || (r.media && r.media.mediaText) || (r.name !== undefined ? `@layer ${r.name}` : '') || r.constructor.name;
          walk(r.cssRules, cond ? `${cond} && ${c}` : c); continue;
        }
        if (!r.style) continue;
        // Rules under @media / @supports conditions that matter to a design system: reduced motion,
        // widths, pointer and contrast. Counted, with a few selectors as examples.
        if (cond && /reduced-motion|width|hover|pointer|contrast|color-scheme/.test(cond)) {
          const k = cond.slice(0, 160), e = conditions[k] ||= { rules: 0, properties: {}, selectors: [] };
          e.rules++; for (const p of r.style) if (p) e.properties[p] = (e.properties[p] || 0) + 1;
          if (e.selectors.length < 6) e.selectors.push((r.selectorText || '').slice(0, 120));
        }
        for (const p of r.style) if (p && p.startsWith('--') && KEEP.test(p)) {
          names.add(p);
          decls.push({ name: p, value: noUrl(r.style.getPropertyValue(p).trim()), selector: (r.selectorText || r.constructor.name).slice(0, 200), condition: cond || '', sheet: id });
        }
        if (r.cssRules && r.cssRules.length) walk(r.cssRules, cond);
      }
    };
    walk(rules, '');
  });
  const computed = {};
  const els = { html: document.documentElement, body: document.body };
  for (const s of scopes) { const e = document.querySelector(s); if (e) els[s] = e; }
  for (const [k, e] of Object.entries(els)) {
    const cs = getComputedStyle(e), v = {};
    for (const p of e.style) if (p && p.startsWith('--') && KEEP.test(p)) names.add(p);   // set by script, inline
    for (const n of [...names].sort()) { const x = noUrl(cs.getPropertyValue(n).trim()); if (x) v[n] = x; }
    computed[k] = v;
  }
  // Resolve each property the way the browser paints it: as a colour (color-mix and oklch come
  // back as color(srgb ...) or oklch(...), which the token builder converts) and, for shadows, as a
  // box-shadow. A sentinel parent colour tells a non-colour value apart (it inherits the sentinel).
  const scopeEl = document.querySelector(scopes[0]) || document.body, scopeKey = scopes[0] && document.querySelector(scopes[0]) ? scopes[0] : 'body';
  const host = document.createElement('div'), probe = document.createElement('div');
  host.style.cssText = 'position:fixed;left:-99px;top:-99px;color:rgb(1, 2, 3)';
  host.appendChild(probe); scopeEl.appendChild(host);
  const colors = {}, shadows = {}, channels = [];
  for (const n of Object.keys(computed[scopeKey])) {
    probe.style.color = ''; probe.style.color = `var(${n})`;
    const c = getComputedStyle(probe).color;
    if (c !== 'rgb(1, 2, 3)' || computed[scopeKey][n] === 'rgb(1, 2, 3)') colors[n] = c;
    // Tailwind-style channel triplets ("255 255 255 / 0.52") are not colours on their own; the app
    // paints them as rgb(var(--x)). Read them that way and say so in `channels`.
    else if (/^\d+(\.\d+)? \d+(\.\d+)? \d+(\.\d+)?( \/ [\d.]+%?)?$/.test(computed[scopeKey][n])) {
      probe.style.color = `rgb(var(${n}))`;
      const c2 = getComputedStyle(probe).color;
      if (c2 !== 'rgb(1, 2, 3)') { colors[n] = c2; channels.push(n); }
    }
    if (/shadow/.test(n)) { probe.style.boxShadow = `var(${n})`; shadows[n] = getComputedStyle(probe).boxShadow; probe.style.boxShadow = ''; }
  }
  host.remove();
  const faces = [];
  for (const f of document.fonts) faces.push({ family: f.family, weight: f.weight, style: f.style, status: f.status });
  const sc = getComputedStyle(scopeEl);
  return { scope: scopeKey, sheets, decls, computed, colors, channels, shadows, conditions,
    fonts: { faces, body: getComputedStyle(document.body).fontFamily, scope: { family: sc.fontFamily, size: sc.fontSize, weight: sc.fontWeight, lineHeight: sc.lineHeight } } };
}, { scopes, keep: process.env.KEEP });
writeJson(out, { meta: { ...meta, read: new Date().toISOString().slice(0, 10) }, ...data });
console.log(out, data.decls.length, 'declarations', Object.keys(data.colors).length, 'colours on', data.scope);
await disconnect(browser);
