// Read the utility classes a Tailwind app actually uses: every single-class rule (`.text-13`,
// `.rounded-\[6px\]`, `.shadow-shadow-L2`, `.duration-200`) whose class appears on an element inside the
// scope, with the declarations that matter to a design system and how many elements carry it.
// Generic for any app styled with utility classes; Devin's Agents view is one (Tailwind v3, whose
// scales are not custom properties, so vars.mjs alone cannot see them).
//
//   PORT=9402 node tools/capture/electron/utilities.mjs <out.json> "<window title regex>" [scope selector] [--shots=a,b,c]
//
// With --shots, each named shot of product.mjs is revealed in turn (reset, reveal, read, after) and
// every screen's classes are merged; without it, the screen as it is now is read.
// Writes { meta, scope, classes: { <class>: { props: { <property>: <declared value> }, condition, sheet, used } },
//          fonts: { <computed font-family>: count }, sizes: { "<font-size>/<line-height>/<weight>": count } }.
// Run once per screen worth reading (the classes on screen are the ones counted); merges into <out.json>.
import { existsSync, readFileSync } from 'node:fs';
import { connect, disconnect, viewport, writeJson } from './cdp.mjs';

const argv = process.argv.slice(2);
const shotNames = (argv.find(a => a.startsWith('--shots=')) || '').slice(8).split(',').filter(Boolean);
const [out, title, scope = 'body'] = argv.filter(a => !a.startsWith('--'));
if (!out || !title) { console.error('usage: utilities.mjs <out.json> "<title regex>" [scope]'); process.exit(2); }
// A title starting with "url:" picks the window by its URL instead (a regex), for apps whose windows share a title.
const h = await connect(title.startsWith("url:") ? { url: new RegExp(title.slice(4)) } : new RegExp(title));
const { browser, page } = h;
const read = () => page.evaluate(scope => {
  const PROPS = /^(font-size|line-height|font-weight|font-family|letter-spacing|border-radius|border-(top-|bottom-)?(left-|right-)?radius|padding|padding-(top|right|bottom|left)|gap|row-gap|column-gap|height|width|min-height|box-shadow|--tw-shadow|transition-duration|transition-timing-function|animation-duration|outline-width|outline-offset|border-width|--tw-ring-.*|backdrop-filter|--tw-backdrop-blur|opacity|z-index)$/;
  const root = document.querySelector(scope) || document.body;
  const used = {};
  for (const e of [root, ...root.querySelectorAll('[class]')]) {
    const cls = typeof e.className === 'string' ? e.className : e.getAttribute('class') || '';
    for (const c of cls.split(/\s+/)) if (c) used[c] = (used[c] || 0) + 1;
  }
  const unescape = s => s.replace(/\\(.)/g, '$1');
  const classes = {};
  [...document.styleSheets].forEach((s, i) => {
    const owner = s.ownerNode;
    const sheet = s.href ? s.href.split('/').slice(-1)[0] : (owner && (owner.id || owner.className)) || `inline-${i}`;
    let rules; try { rules = s.cssRules; } catch { return; }
    const walk = (rs, cond) => {
      for (const r of rs) {
        if (r.cssRules && !r.style) { walk(r.cssRules, cond ? `${cond} && ${r.conditionText || r.name || ''}` : (r.conditionText || r.name || '')); continue; }
        if (!r.style || !r.selectorText) continue;
        // one class, optionally with a pseudo-class (`.x`, `.x:hover`), optionally behind one scoping
        // compound selector (`.app-root .x`, as apps that prefix their utilities write them). Kept when the
        // rule matches an element inside the scope on screen now.
        const m = r.selectorText.match(/^((?:[.#][\w-]+)+\s+)?\.((?:\\.|[^\s.:>+~,[\]])+)((?::[\w-]+(?:\([^)]*\))?)*)$/);
        if (!m) continue;
        const c = unescape(m[2]);
        if (!used[c]) continue;
        const probe = r.selectorText.slice(0, r.selectorText.length - (m[3] || '').length);
        let hit = false; try { hit = !!(root.matches(probe) || root.querySelector(probe)); } catch {}
        if (!hit) continue;
        const props = {};
        for (let k = 0; k < r.style.length; k++) { const p = r.style[k]; if (p && PROPS.test(p)) props[p] = r.style.getPropertyValue(p).trim(); }
        if (!Object.keys(props).length) continue;
        const key = c + (m[3] || '');
        if (!classes[key] || !cond) classes[key] = { props, selector: r.selectorText.slice(0, 160), condition: cond || '', sheet, used: used[c] };
      }
    };
    walk(rules, '');
  });
  const fonts = {}, sizes = {};
  for (const e of root.querySelectorAll('*')) {
    if (!e.firstChild || e.firstChild.nodeType !== 3 || !e.textContent.trim()) continue;
    const r = e.getBoundingClientRect(); if (!r.width) continue;
    const cs = getComputedStyle(e);
    fonts[cs.fontFamily] = (fonts[cs.fontFamily] || 0) + 1;
    const k = `${cs.fontSize}/${cs.lineHeight}/${cs.fontWeight}`; sizes[k] = (sizes[k] || 0) + 1;
  }
  return { classes, fonts, sizes };
}, scope);
const prev = existsSync(out) ? JSON.parse(readFileSync(out, 'utf8')) : { classes: {}, fonts: {}, sizes: {}, screens: [] };
function merge(data, screen) {
  for (const [k, v] of Object.entries(data.classes)) {
    const p = prev.classes[k];
    prev.classes[k] = p ? { ...v, used: Math.max(p.used, v.used) } : v;
  }
  for (const key of ['fonts', 'sizes']) for (const [k, n] of Object.entries(data[key])) prev[key][k] = Math.max(prev[key][k] || 0, n);
  prev.screens = [...new Set([...(prev.screens || []), screen])];
  console.log(screen, Object.keys(data.classes).length, 'classes');
}
const failed = [];
if (shotNames.length) {
  const P = await import('./product.mjs');
  for (const name of shotNames) {
    const shot = P.SHOTS.find(s => s.name === name);
    if (!shot) { console.error('no shot', name); failed.push(name); continue; }
    try { await P.reset(h, shot.window); await shot.reveal(h); merge(await read(), name); }
    catch (e) { console.error('FAILED', name, e.message.split('\n')[0]); failed.push(name); }
    finally { if (shot.after) await shot.after(h).catch(() => {}); }
  }
  await P.reset(h, Object.keys(P.WINDOWS)[0]);   // the product's first window
} else merge(await read(), (await viewport(page)).title);
// A failed screen fails the run and writes nothing, so no older reading survives under a new date.
if (failed.length) { console.error(`${failed.length} screen(s) not read: ${failed.join(', ')}; ${out} not written`); await disconnect(browser); process.exit(1); }
prev.meta = { ...(await viewport(page)), read: new Date().toISOString().slice(0, 10) };
prev.scope = scope;
writeJson(out, prev);
await disconnect(browser);
