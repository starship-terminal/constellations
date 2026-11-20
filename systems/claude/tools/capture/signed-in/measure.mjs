// Measures Claude's signed-in components from the static page copies (see render.mjs, unsnap.py),
// in both themes and in every state CSS can reach once scripts are gone. Adapted from the Manus kit.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> node tools/capture/signed-in/measure.mjs [label ...] [--jobs N]
//
// With labels, only the components (and states) that live on those copies are re-measured and
// merged into the existing JSON. Writes raw/components-computed.json and one crop per component
// and state into components/crops/<component>-<state>.png (2x, 256 colours, halved when wider than
// 1600px). raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// Themes: Claude's design system ("cds") paints its light palette by default and its dark one under
// data-mode="dark" on <html> and on every .cds-root (the .dframe-root, menus and dialogs carry their
// own), so each copy (captured dark) is measured once as captured and once with every [data-mode]
// set to light, which is what render.mjs does for the light screenshots. Dark states keep their
// plain names (`default`, `hover`, ...); light states are `light`, `light-hover`,
// `light-focus-visible`, ... and every state records `theme`.
//
// States:
//   default        at rest, as captured
//   hover          real mouse hover (page.mouse.move), 450ms settle; Tailwind's hover: variants
//                  (inside @media (hover: hover)) are plain CSS, so they apply on the static copy
//   focus-visible  real keyboard focus: focus(), Shift+Tab, Tab (or a Shift keydown then focus()),
//                  on the element or its first focusable descendant
//   pressed        the pointer held down on the element (page.mouse.down) for 250ms, so :active and
//                  the cds squish (`.cds-btn-squish`, scale --cds-btn-press-sx) apply; released after
//                  the reading. The copies have no scripts, so nothing is activated.
//   anything else  another element, or another copy, captured in that state: `active`, `selected`,
//                  `checked`, `open`, `typed`, `on`, ...
// No click is dispatched anywhere; the copies have no scripts and every navigation away from the
// file is aborted.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { chromium, REF, RAW, CROPS, SNAPS, SCROLL, metaOf, newContext, openSnap, setLight } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';
// An activated .venv without Pillow resolves python3 to itself: set PYTHON to a python3 that has it.
const PYTHON = process.env.PYTHON || 'python3';

if (!SNAPS) { console.error('SNAPS=<snapshot dir> is required'); process.exit(2); }
const OUT = path.join(RAW, 'components-computed.json');
const args = process.argv.slice(2);
const jobsArg = args.indexOf('--jobs');
const CONC = jobsArg >= 0 ? Number(args[jobsArg + 1]) : 4;
// A missing or bad --jobs used to start no workers at all, and the run then saved every state it
// had reset as gone.
if (!Number.isInteger(CONC) || CONC < 1) { console.error('--jobs takes a whole number of 1 or more'); process.exit(2); }
const ONLY = args.filter((a, i) => !a.startsWith('--') && (jobsArg < 0 || i !== jobsArg + 1));
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

// ---------------------------------------------------------------- page helpers (run in the page)
//
// Finders are plain functions of these globals, so a spec reads as what it looks for:
//   T(text, root)     the visible element whose innerText is exactly `text`, in the viewport first,
//                     then the smallest; TS(prefix, root) the same by prefix
//   Q(sel, i, root)   the i-th visible match of a CSS selector, in-viewport matches first
//   K(tokens, i, root) the i-th visible element carrying every class token (no CSS escaping needed
//                     for Tailwind names such as `group/nav-tab` or `p-[1px]`)
//   C(el, sel)        el.closest(sel);  CK(el, tokens) the closest element carrying the tokens
//   W(el, w)          el or the first ancestor at least `w` px wide (H(el, h) the same by height)
//   unhidden(list)    the first element of a list whose centre nothing covers;  at(x, y) the element there
//   P(el)             el or the first ancestor that paints a fill, border or shadow
//   D()               the last visible [role=dialog];  MN() the last visible [role=menu]
//   M()               the main content column (main.dframe-content);  S() the sidebar (aside.dframe-sidebar)
//   CR()              the sidebar's chat rows in page order (every div.group holding a "More options for" button)
//   below(el)         CR() rows that start under el, so a row is found by its place, not by its title
//                     (el may be held at opacity 0, so pass it from document.querySelector, not Q)
const HELPERS = () => {
  const vis = (e) => {
    if (!e || !e.getBoundingClientRect) return false;
    const r = e.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return false;
    const cs = getComputedStyle(e);
    if (cs.visibility !== 'visible' || cs.display === 'none') return false;
    // Opacity is not inherited in the computed style, so a popover held at opacity 0 (the thread's
    // hover outline, a hover-only toolbar) is found by walking up.
    for (let n = e; n && n !== document.documentElement; n = n.parentElement) if (+getComputedStyle(n).opacity === 0) return false;
    return true;
  };
  const inVp = (e) => { const r = e.getBoundingClientRect(); return r.bottom > 0 && r.right > 0 && r.top < innerHeight && r.left < innerWidth ? 1 : 0; };
  const order = (list) => list.filter(vis).map((e, i) => [e, i]).sort((a, b) => inVp(b[0]) - inVp(a[0]) || a[1] - b[1]).map((x) => x[0]);
  const area = (e) => { const r = e.getBoundingClientRect(); return r.width * r.height; };
  const byText = (pred, needle, root) => {
    root = root || document.body;
    // An sr-only label (a 1x1 clipped box) never counts as the visible text.
    const c = [...root.querySelectorAll('*')].filter((e) => e.textContent.includes(needle) && pred((e.innerText || '').trim()) && vis(e) && area(e) > 4);
    c.sort((a, b) => inVp(b) - inVp(a) || area(a) - area(b));
    return c[0] || null;
  };
  const hasTokens = (e, tokens) => e.classList && tokens.split(/\s+/).filter(Boolean).every((t) => e.classList.contains(t));
  const paints = (e) => {
    const cs = getComputedStyle(e);
    return cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none' || cs.boxShadow !== 'none' || ['Top', 'Right', 'Bottom', 'Left'].some((s) => parseFloat(cs[`border${s}Width`]) > 0 && cs[`border${s}Style`] !== 'none');
  };
  Object.assign(window, {
    T: (text, root) => byText((t) => t === text, text, root),
    TS: (prefix, root) => byText((t) => t.startsWith(prefix), prefix, root),
    Q: (sel, i = 0, root = document) => order([...root.querySelectorAll(sel)])[i] || null,
    K: (tokens, i = 0, root = document) => order([...root.querySelectorAll('*')].filter((e) => hasTokens(e, tokens)))[i] || null,
    C: (el, sel) => (el ? el.closest(sel) : null),
    CK: (el, tokens) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (hasTokens(n, tokens)) return n; return null; },
    H: (el, h) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (n.getBoundingClientRect().height >= h - 0.5) return n; return null; },
    // The first visible element of a list whose centre is not covered by anything else.
    unhidden: (list) => [...list].find((e) => { if (!vis(e)) return false; const r = e.getBoundingClientRect(); const h = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2); return h && (e.contains(h) || h.contains(e)); }) || null,
    W: (el, w) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (n.getBoundingClientRect().width >= w - 0.5) return n; return null; },
    at: (x, y) => document.elementFromPoint(x, y),
    P: (el) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (paints(n)) return n; return null; },
    D: () => { const d = [...document.querySelectorAll('[role=dialog]')].filter(vis); return d[d.length - 1] || null; },
    M: () => document.querySelector('main.dframe-content'),
    S: () => document.querySelector('aside.dframe-sidebar'),
    CR: () => [...document.querySelectorAll('aside button[aria-label^="More options for"]')].map((b) => b.closest('div.group')).filter(Boolean),
    below: (el) => CR().filter((r) => el && r.getBoundingClientRect().top >= el.getBoundingClientRect().bottom),
    MN: () => { const d = [...document.querySelectorAll('[role=menu]')].filter(vis); return d[d.length - 1] || null; },
    painted: (list) => [...list].find((e) => vis(e) && paints(e)) || null,
    unpainted: (list) => [...list].find((e) => vis(e) && !paints(e)) || null,
  });
  window.__isFocusable = (e) => e && (e.tabIndex >= 0 || e.isContentEditable || /^(A|BUTTON|INPUT|SELECT|TEXTAREA)$/.test(e.tagName)) && !e.disabled;
  window.__focusTarget = (e) => {
    if (window.__isFocusable(e)) return e;
    return [...e.querySelectorAll('a[href], button, input, select, textarea, [tabindex], [contenteditable=true]')].find((x) => window.__isFocusable(x) && vis(x)) || null;
  };
  // Every scroller's position as the snapshot was opened (after the scroll rule), put back before
  // each measurement, so an earlier component scrolled into view does not move a later one.
  window.__saveScroll = () => { window.__scrolls = [...document.querySelectorAll('*')].filter((e) => e.scrollTop || e.scrollLeft).map((e) => [e, e.scrollTop, e.scrollLeft]); window.__scrollY = scrollY; };
  window.__restoreScroll = () => { for (const [e, t, l] of window.__scrolls || []) { e.scrollTop = t; e.scrollLeft = l; } document.querySelectorAll('*').forEach((e) => { if ((e.scrollTop || e.scrollLeft) && !(window.__scrolls || []).some((x) => x[0] === e)) { e.scrollTop = 0; e.scrollLeft = 0; } }); scrollTo(0, window.__scrollY || 0); };
  // CSS animations are pinned so two runs crop the same pixels: a finite one (an entrance fade) is
  // finished, an infinite one (the promo progress, marquees, skeleton pulses) held at its first
  // frame. Transitions are left alone: hover and focus need them to finish.
  window.__freeze = () => {
    for (const a of document.getAnimations()) {
      if (typeof CSSAnimation === 'undefined' || !(a instanceof CSSAnimation)) continue;
      const t = a.effect && a.effect.getComputedTiming();
      if (t && t.iterations === Infinity) { a.pause(); a.currentTime = 0; } else { try { a.finish(); } catch { a.pause(); } }
    }
  };
  document.addEventListener('click', (e) => e.preventDefault(), true);
  document.addEventListener('submit', (e) => e.preventDefault(), true);
};

// Computed properties recorded for every component and state (the gauth set).
const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent', 'gridTemplateColumns',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor', 'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor', 'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow', 'backdropFilter', 'filter',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform', 'textAlign',
  'color', 'textDecorationLine', 'textDecorationColor', 'textDecorationThickness', 'textUnderlineOffset',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction', 'transitionDelay',
  'cursor', 'opacity', 'transform', 'overflow', 'zIndex', 'top',
];

// Reads one element: computed style, rect, ::before/::after, the painted layers inside it (so a
// root that paints nothing still shows what does), the paint of up to three ancestors, the first
// text node's type, the first icon, a field's placeholder (the composer's is Tiptap's
// `p.is-editor-empty::before`), and every `var(--x)` its classes and painted children name, with
// the value that variable resolves to in the current theme.
function styleOf(el, props) {
  const cls = (n) => (typeof n.className === 'string' ? n.className : n.getAttribute('class') || '');
  const short = (n) => n.tagName.toLowerCase() + cls(n).split(/\s+/).filter((c) => c && !c.includes('[') && !c.includes(':')).slice(0, 3).map((c) => '.' + c).join('');
  // A url() in a computed value can be a signed URL: recorded as url(…), only data: and #fragment
  // references kept (the kit's noUrl).
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
  const pick = (cs) => { const o = {}; for (const p of props) o[p] = noUrl(cs[p]); return o; };
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const out = {
    tag: el.tagName.toLowerCase(),
    classes: cls(el).slice(0, 700),
    text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
    style: pick(cs),
  };
  for (const a of ['role', 'aria-label', 'data-cds', 'data-state', 'data-active', 'aria-checked', 'aria-selected', 'data-variant']) if (el.hasAttribute(a)) (out.attrs ||= {})[a] = el.getAttribute(a);
  // A cds Button presses by scaling its paint layer (.cds-btn-squish), not the element itself.
  const sq = el.querySelector('.cds-btn-squish');
  if (sq) out.squish = { transform: getComputedStyle(sq).transform, transition: getComputedStyle(sq).transition.slice(0, 120) };
  for (const pe of ['::before', '::after']) {
    const p = getComputedStyle(el, pe);
    if (p.content && p.content !== 'none' && p.content !== 'normal') {
      out[pe] = { content: noUrl(p.content).slice(0, 40), width: p.width, height: p.height, position: p.position, backgroundColor: p.backgroundColor, backgroundImage: noUrl(p.backgroundImage).slice(0, 200), boxShadow: p.boxShadow, borderTopWidth: p.borderTopWidth, borderTopStyle: p.borderTopStyle, borderTopColor: p.borderTopColor, borderRadius: p.borderRadius, inset: `${p.top} ${p.right} ${p.bottom} ${p.left}`, opacity: p.opacity, transition: p.transition };
    }
  }
  const paint = [];
  const nodes = [el, ...el.querySelectorAll('*')].slice(0, 400);
  for (const n of nodes) {
    if (paint.length >= 14) break;
    if (n.closest('svg') && n.tagName.toLowerCase() !== 'svg') continue;
    const nr = n.getBoundingClientRect();
    if (nr.width < 1 || nr.height < 1) continue;
    for (const pe of [null, '::before', '::after']) {
      const c = getComputedStyle(n, pe);
      if (pe && (c.content === 'none' || c.content === 'normal')) continue;
      if (c.visibility !== 'visible') continue;
      const bw = ['Top', 'Right', 'Bottom', 'Left'].map((sd) => (parseFloat(c[`border${sd}Width`]) > 0 && c[`border${sd}Style`] !== 'none' ? `${sd[0]}:${c[`border${sd}Width`]} ${c[`border${sd}Style`]} ${c[`border${sd}Color`]}` : '')).filter(Boolean);
      const bg = c.backgroundColor !== 'rgba(0, 0, 0, 0)' ? c.backgroundColor : '';
      const bgi = c.backgroundImage !== 'none' && !/^url\("?https?:/.test(c.backgroundImage) ? noUrl(c.backgroundImage).replace(/url\("data:[^)]{60,}\)/g, 'url(data:…)').slice(0, 200) : '';
      const sh = c.boxShadow !== 'none' ? c.boxShadow : '';
      const ol = c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0 ? `${c.outlineWidth} ${c.outlineStyle} ${c.outlineColor} offset ${c.outlineOffset}` : '';
      if (!(bw.length || bg || bgi || sh || ol)) continue;
      if (n.tagName === 'IMG' && !bw.length && !sh) continue;
      paint.push({ node: short(n) + (pe || ''), size: pe ? `${c.width}x${c.height}` : `${nr.width.toFixed(1)}x${nr.height.toFixed(1)}`, border: bw.join(' | ') || undefined, bg: bg || undefined, bgImage: bgi || undefined, shadow: sh || undefined, outline: ol || undefined, radius: c.borderRadius !== '0px' ? c.borderRadius : undefined, opacity: c.opacity !== '1' ? c.opacity : undefined });
    }
  }
  if (paint.length) out.paint = paint;
  const anc = [];
  for (let n = el.parentElement, i = 0; n && i < 3; n = n.parentElement, i++) {
    const c = getComputedStyle(n);
    const fill = i < 1 && c.backgroundColor !== 'rgba(0, 0, 0, 0)';
    if (fill || c.boxShadow !== 'none' || (c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0 && c.outlineColor !== 'rgba(0, 0, 0, 0)')) anc.push({ up: i + 1, node: short(n), shadow: c.boxShadow !== 'none' ? c.boxShadow : undefined, outline: c.outlineStyle !== 'none' ? `${c.outlineWidth} ${c.outlineStyle} ${c.outlineColor}` : undefined, radius: c.borderRadius, bg: c.backgroundColor });
  }
  if (anc.length) out.ancestors = anc;
  const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (t) => (t.textContent.trim() && t.parentElement && t.parentElement.getBoundingClientRect().width > 1 && getComputedStyle(t.parentElement).visibility === 'visible' ? 1 : 3) });
  const tn = walker.nextNode();
  if (tn && tn.parentElement !== el) {
    const t = tn.parentElement;
    const tc = getComputedStyle(t);
    out.textStyle = { node: short(t), text: tn.textContent.trim().slice(0, 40), fontFamily: tc.fontFamily, fontSize: tc.fontSize, lineHeight: tc.lineHeight, fontWeight: tc.fontWeight, letterSpacing: tc.letterSpacing, color: tc.color, textDecorationLine: tc.textDecorationLine, textTransform: tc.textTransform };
  }
  if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.querySelector('input')) {
    const f = el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' ? el : el.querySelector('input');
    const ph = getComputedStyle(f, '::placeholder');
    out.placeholder = { text: f.getAttribute('placeholder'), color: ph.color, opacity: ph.opacity, fontSize: ph.fontSize, lineHeight: ph.lineHeight };
  }
  const pp = el.querySelector('[contenteditable=true] p[data-placeholder], [contenteditable=true] p.is-editor-empty') || (el.matches('p[data-placeholder]') ? el : null);
  if (pp) {
    const b = getComputedStyle(pp, '::before');
    out.placeholder = { text: pp.getAttribute('data-placeholder') || noUrl(b.content).slice(0, 80), color: b.color, opacity: b.opacity, fontSize: b.fontSize, lineHeight: b.lineHeight, float: b.cssFloat, height: b.height };
  }
  const svg = el.tagName.toLowerCase() === 'svg' ? el : [...el.querySelectorAll('svg')].find((s) => s.getBoundingClientRect().width > 1);
  if (svg) {
    const sr = svg.getBoundingClientRect();
    const scs = getComputedStyle(svg);
    out.icon = { w: +sr.width.toFixed(2), h: +sr.height.toFixed(2), fill: scs.fill, stroke: scs.stroke, color: scs.color, strokeWidth: scs.strokeWidth, classes: (svg.getAttribute('class') || '').slice(0, 80) };
  }
  // Design tokens: every var(--x) named in the classes of the element and the first painted or
  // texted nodes inside it, resolved on the element in the current theme.
  const names = new Set();
  for (const n of [el, ...el.querySelectorAll('*')].slice(0, 60)) for (const m of cls(n).matchAll(/var\((--[\w-]+)/g)) names.add(m[1]);
  if (names.size) {
    out.vars = {};
    const root = getComputedStyle(el);
    for (const n of [...names].sort()) out.vars[n] = noUrl(root.getPropertyValue(n).trim());
  }
  return out;
}

// ---------------------------------------------------------------- specs
//
// Each spec: key, group, title, desc, snap (the copy), find (a finder function), states, and
// optional `extra` states: { name: { snap?, find } } for another element or copy captured in that
// state (they are measured at rest, then with their own `states` if given). `pad` is the crop
// padding (8 by default); `crop: false` skips the crop.
const ALL = ['default', 'hover', 'focus-visible'];
const HV = ['default', 'hover'];
const R = ['default'];
const ALLP = ['default', 'hover', 'focus-visible', 'pressed'];
// `refresh` extras read a component again on a 2026-10-17 copy, at rest and with keyboard focus, for the
// components whose 2026-10-04 copy had no focus reading (that copy is gone, so the old states are kept).
const RF = ['focus-visible'];
const HVP = ['default', 'hover', 'pressed'];
// The create-project copy is read with and without data-invalid on its name field; every other reading
// of that copy clears it first, so the error ring never leaks into them.
const VALID = () => Q('[data-cds=TextInput]').removeAttribute('data-invalid');
// The filter menu copy is read with and without a keyboard-highlighted item; the other readings clear it.
const UNLIT = () => MN().querySelectorAll('[data-highlighted]').forEach((n) => n.removeAttribute('data-highlighted'));

const SPECS = [
  // ---------------- Sidebar
  { key: 'sidebar', group: 'Sidebar', title: 'Sidebar (expanded)', snap: 'home-dark', find: () => S(), states: R, pad: 0, desc: 'aside.dframe-sidebar, 288 wide (--df-sidebar-width) and full height, on its own ground (--df-web-sidebar-bg: #111111 in dark, a step darker than the page; #fbfbf9 in light), with no rule between it and the content.' },
  { key: 'sidebar-titlebar', group: 'Sidebar', title: 'Sidebar title row', snap: 'home-dark', find: () => Q('aside .df-titlebar'), states: R, desc: '44 tall: the "Claude" serif wordmark at the start, Hide sidebar and Search icon buttons at the end.' },
  { key: 'sidebar-wordmark', group: 'Sidebar', title: 'Claude wordmark', snap: 'home-dark', find: () => Q('aside a[aria-label=Home]'), states: HV, desc: 'An inline SVG, 68x20, in the text colour.' },
  { key: 'sidebar-icon-button', group: 'Sidebar', title: 'Sidebar icon button (Hide sidebar)', snap: 'home-dark', find: () => Q('aside button[aria-label="Hide sidebar"]'), states: ALL, desc: 'A cds Button, ghost, 32x32 with a 16px glyph from the Anthropicons icon font.' },
  { key: 'sidebar-search-button', group: 'Sidebar', title: 'Sidebar Search button', snap: 'home-dark', find: () => Q('aside button[aria-label=Search]'), states: HV, extra: { refresh: { snap: 'home-dark-tooltip', find: () => Q('aside button[aria-label=Search]'), states: RF } } },
  { key: 'mode-pills', group: 'Sidebar', title: 'Home/Code segmented control', snap: 'home-dark', find: () => Q('aside .df-pills'), states: R, desc: 'Two pills (Home, Code) in a track the full width of the sidebar; a sliding indicator sits under the active one.' },
  { key: 'mode-pill', group: 'Sidebar', title: 'Mode pill', snap: 'home-dark', find: () => Q('aside .df-pill:not([data-active])'), states: ALL, extra: { active: { find: () => Q('aside .df-pill[data-active=true]') } } },
  { key: 'mode-pill-indicator', group: 'Sidebar', title: 'Mode pill indicator', snap: 'home-dark', find: () => Q('aside .df-pill-indicator'), states: R },
  { key: 'nav-new-row', group: 'Sidebar', title: 'New row', snap: 'home-dark', find: () => C(T('New', S()), 'div.group'), states: ALL, desc: 'The first nav row: a 22px circle with a plus, "New", the ⇧⌘O shortcut, and a Quick task button at the end.' },
  { key: 'nav-new-circle', group: 'Sidebar', title: 'New row circle', snap: 'home-dark', find: () => Q('aside .df-new-circle'), hoverOn: () => C(T('New', S()), 'div.group'), states: HV },
  { key: 'nav-shortcut', group: 'Sidebar', title: 'Shortcut hint', snap: 'home-dark', find: () => document.querySelector('aside [data-cds=Shortcut]'), hoverOn: () => C(T('New', S()), 'div.group'), states: HV, desc: 'cds Shortcut, text variant: each key a <kbd> in caption size; held at opacity 0 until its row is hovered.' },
  { key: 'nav-row', group: 'Sidebar', title: 'Nav row (Artifacts)', snap: 'home-dark', find: () => C(T('Artifacts', S()), 'div.group'), states: ALL, desc: '32 tall (--df-row-h), radius 8 (--df-radius-pill), a 20px glyph in a 28px leading slot, 14px text in text-secondary; hover fills --df-hover.' },
  { key: 'nav-row-more', group: 'Sidebar', title: 'More row', snap: 'home-dark', find: () => Q('aside button[aria-label="More navigation items"]'), states: ALL, extra: { open: { snap: 'artifacts-dark-more-menu', find: () => Q('aside button[aria-label="More navigation items"]') } } },
  { key: 'section-label', group: 'Sidebar', title: 'Section label (Pinned)', snap: 'home-dark', find: () => C(T('Pinned', S()), 'button'), states: ALL, desc: 'Caption-size text in text-muted with a caret that shows on hover.' },
  { key: 'section-action', group: 'Sidebar', title: 'Section action button (View all)', snap: 'home-dark', find: () => document.querySelector('aside button[aria-label="View all"]'), hoverOn: () => C(T('Chats and tasks', S()), 'button').parentElement, states: HV, extra: { refresh: { snap: 'home-dark-tooltip', find: () => document.querySelector('aside button[aria-label="View all"]'), states: RF } }, desc: 'Revealed when its section label row is hovered, or when it takes keyboard focus.' },
  { key: 'chat-row', group: 'Sidebar', title: 'Chat row', snap: 'home-dark', find: () => below(document.querySelector('aside button[aria-label="View all"]'))[0], states: HV, desc: 'A 6px hollow ring as the bullet (role=img "Idle"), the title faded at the end (.dframe-fade-label, a mask, not an ellipsis), a more button on hover.', extra: { refresh: { snap: 'home-dark-tooltip', find: () => below(document.querySelector('aside button[aria-label="View all"]'))[0], focusOn: () => below(document.querySelector('aside button[aria-label="View all"]'))[0].querySelector('a'), states: RF }, pinned: { find: () => CR()[0] }, selected: { snap: 'thread-dark', find: () => CR().find((r) => document.title.startsWith(r.querySelector('button[aria-label^="More options for"]').getAttribute('aria-label').slice(17) + ' - ')) } } },
  { key: 'chat-row-bullet', group: 'Sidebar', title: 'Chat row bullet', snap: 'home-dark', find: () => Q('aside [aria-label=Idle] span'), states: R },
  { key: 'chat-row-more', group: 'Sidebar', title: 'Chat row more button', snap: 'home-dark', find: () => below(document.querySelector('aside button[aria-label="View all"]'))[0].querySelector('button[aria-label^="More options for"]'), hoverOn: () => below(document.querySelector('aside button[aria-label="View all"]'))[0], states: HV, extra: { refresh: { snap: 'home-dark-tooltip', find: () => below(document.querySelector('aside button[aria-label="View all"]'))[0].querySelector('button[aria-label^="More options for"]'), states: RF }, open: { snap: 'home-dark-chat-menu', find: () => document.querySelector('aside button[aria-label^="More options for"][aria-expanded=true]') || document.querySelector('aside button[data-popup-open]') } } },
  { key: 'account-row', group: 'Sidebar', title: 'Account row', snap: 'home-dark', find: () => Q('[data-testid=user-menu-button]'), states: ALL, desc: 'Avatar, name, a dot and the plan ("Max") in text-muted, a chevron.', extra: { open: { snap: 'home-dark-user-menu', find: () => Q('[data-testid=user-menu-button]') } } },
  { key: 'account-avatar', group: 'Sidebar', title: 'Avatar', snap: 'home-dark', find: () => Q('aside [data-cds=Avatar]'), states: R },
  { key: 'account-plan', group: 'Sidebar', title: 'Plan label', snap: 'home-dark', find: () => T('Max', S()), states: R },
  { key: 'footer-apps-button', group: 'Sidebar', title: 'Get apps button', snap: 'home-dark', find: () => Q('aside a[aria-label="Get apps and extensions"]'), states: ALL },
  { key: 'resize-handle', group: 'Sidebar', title: 'Sidebar resize handle', snap: 'home-dark', find: () => Q('[data-cds=ResizeHandle]'), states: HV, crop: false },
  { key: 'sidebar-collapsed', group: 'Sidebar', title: 'Sidebar hidden (the show button)', snap: 'home-dark-sidebar-collapsed', find: () => S(), states: R, desc: 'Hidden, the sidebar leaves only a 32x32 box at 8,8 holding the Show sidebar button; the content pane takes the full width.' },
  { key: 'sidebar-show-button', group: 'Sidebar', title: 'Show sidebar button', snap: 'home-dark-sidebar-collapsed', find: () => Q('[data-testid=sidebar-compact-trigger]'), states: ALL },

  // ---------------- Header
  { key: 'pane-header', group: 'Header', title: 'Content pane header', snap: 'home-dark', find: () => Q('header.dframe-header'), states: R, desc: '48 tall (--df-header-h) across the content pane.' },
  { key: 'pane', group: 'Header', title: 'Content pane', snap: 'home-dark', find: () => Q('.dframe-pane-primary'), states: R, pad: 0, desc: 'The content column: it starts 8px past the sidebar and paints nothing itself, so the page shows the app ground (surface-1).' },
  { key: 'incognito-button', group: 'Header', title: 'Incognito button', snap: 'home-dark', find: () => Q('button[aria-label="Use incognito"]'), states: ALL },
  { key: 'chat-title-button', group: 'Header', title: 'Chat title button', snap: 'thread-dark', find: () => Q('[data-testid=chat-title-split] button'), states: ALL },
  { key: 'chat-title-more', group: 'Header', title: 'Chat title more button', snap: 'thread-dark', find: () => Q('[data-testid=chat-title-split] button', 1), states: HV },
  { key: 'share-button', group: 'Header', title: 'Share button', snap: 'thread-dark', find: () => Q('[data-testid=wiggle-controls-actions-share]'), states: ALL },

  // ---------------- Home and composer
  { key: 'greeting', group: 'Home and composer', title: 'Home greeting', snap: 'home-dark', find: () => Q('main .font-display'), states: R, desc: 'Anthropic Serif at the display size (`.font-display`: 2.375rem, weight 300 with the "opsz" 48 axis in dark), the orange asterisk mark first.' },
  { key: 'greeting-mark', group: 'Home and composer', title: 'Greeting mark (the asterisk)', snap: 'home-dark', find: () => Q('main .font-display svg'), states: R },
  { key: 'composer', group: 'Home and composer', title: 'Composer', snap: 'home-dark', find: () => P(Q('[data-testid=chat-input]')), focusOn: () => Q('[data-testid=chat-input]'), states: ['default', 'focus-visible'], desc: 'A card on surface-3 with radius 20 (rounded-[20px]; 12 at compact), a 1px ring of --cds-border (border-strong on focus) and a soft 4/20 drop (shadow-composer); the editor (Tiptap) above a 32px tool row.', extra: { typed: { snap: 'home-dark-composer-typed', find: () => P(Q('[data-testid=chat-input]')) }, thread: { snap: 'thread-dark', find: () => P(Q('[data-testid=chat-input]')) }, project: { snap: 'project-dark', find: () => P(Q('[data-testid=chat-input]')) } } },
  { key: 'composer-placeholder', group: 'Home and composer', title: 'Composer placeholder', snap: 'home-dark', find: () => T('How can I help you today?', M()), states: R, desc: 'Two stacked spans that cross-fade ("How can I help you today?", "Type / for skills").' },
  { key: 'composer-text', group: 'Home and composer', title: 'Composer typed text', snap: 'home-dark-composer-typed', find: () => Q('[data-testid=chat-input] p'), states: R },
  { key: 'composer-plus', group: 'Home and composer', title: 'Composer + button', snap: 'home-dark', find: () => Q('[data-testid=chat-input-attach]'), states: ALL, extra: { open: { snap: 'home-dark-plus-menu', find: () => Q('[data-testid=chat-input-attach]') } } },
  { key: 'segmented-control', group: 'Home and composer', title: 'Chat/Cowork segmented control', snap: 'home-dark', find: () => Q('main [data-cds=SegmentedControl][aria-label=Surface]'), states: R, desc: 'cds SegmentedControl: a track of --cds-segmented-control-track, the checked option on --cds-segmented-control-thumb.' },
  { key: 'segment', group: 'Home and composer', title: 'Segment option', snap: 'home-dark', find: () => Q('main [aria-label=Surface] [role=radio][aria-checked=false]'), states: ALL, extra: { refresh: { snap: 'home-dark-tooltip', find: () => Q('main [aria-label=Surface] [role=radio][aria-checked=true]'), states: RF }, checked: { find: () => Q('main [aria-label=Surface] [role=radio][aria-checked=true]') } } },
  { key: 'model-selector', group: 'Home and composer', title: 'Model selector', snap: 'home-dark', find: () => Q('[data-testid=model-selector-dropdown]'), states: ALL, desc: '"Opus 5.5" in text-primary, "Medium" (the effort) in text-muted, a chevron.', extra: { open: { snap: 'home-dark-model-menu', find: () => Q('[data-testid=model-selector-dropdown]') } } },
  { key: 'mic-button', group: 'Home and composer', title: 'Dictation button', snap: 'home-dark', find: () => Q('button[aria-label="Press and hold to record"]'), states: ALL },
  { key: 'voice-button', group: 'Home and composer', title: 'Voice mode button', snap: 'home-dark', find: () => Q('button[aria-label="Use voice mode"]'), states: ALL },
  { key: 'send-button', group: 'Home and composer', title: 'Send button', snap: 'home-dark-composer-typed', find: () => Q('[data-testid=chat-input-send]'), states: ALL, desc: 'Takes the voice button\'s place once there is text: a filled clay (--cds-fill-brand) square with an arrow.' },
  { key: 'disclaimer', group: 'Home and composer', title: 'Disclaimer under the composer', snap: 'thread-dark', find: () => C(TS('Claude is AI and can make mistakes'), 'a'), states: R },

  // ---------------- Menus and dialogs
  { key: 'plus-menu', group: 'Menus and dialogs', title: 'Plus menu', snap: 'home-dark-plus-menu', find: () => MN(), states: R, desc: 'cds Menu: surface-popover, --cds-panel-radius, a ring plus --cds-shadow-popover; 4px inset, 32px rows.' },
  { key: 'menu-item', group: 'Menus and dialogs', title: 'Menu item', snap: 'home-dark-plus-menu', find: () => C(T('Take a screenshot', MN()), '[role=menuitem]'), states: HV, desc: 'A 20px glyph, body text, an optional shortcut or chevron at the end; hover fills --cds-fill-ghost-hover.', extra: { checkbox: { find: () => Q('[data-testid=add-menu-web-search]') }, submenu: { find: () => Q('[data-testid=add-menu-skills]') } } },
  { key: 'menu-item-shortcut', group: 'Menus and dialogs', title: 'Menu item shortcut', snap: 'home-dark-plus-menu', find: () => Q('[role=menu] [data-cds=Shortcut]'), states: R },
  { key: 'model-menu', group: 'Menus and dialogs', title: 'Model menu', snap: 'home-dark-model-menu', find: () => MN(), states: R, desc: 'Four models as two-line radio items (name, description in footnote), then Effort and More models as submenu rows.' },
  { key: 'model-menu-item', group: 'Menus and dialogs', title: 'Model menu item', snap: 'home-dark-model-menu', find: () => C(T('Sonnet 5.5', MN()), '[role=menuitemradio]'), states: HV, extra: { checked: { find: () => C(T('Opus 5.5', MN()), '[role=menuitemradio]') } } },
  { key: 'model-menu-effort', group: 'Menus and dialogs', title: 'Effort row', snap: 'home-dark-model-menu', find: () => C(T('Effort', MN()), '[role=menuitem]'), states: HV },
  { key: 'user-menu', group: 'Menus and dialogs', title: 'Account menu', snap: 'home-dark-user-menu', find: () => MN(), states: R, desc: 'Opens above the account row: the email as a muted header, then Settings, Usage, Language, Get help, plans, apps, Learn more, API keys, Log out.' },
  { key: 'user-menu-header', group: 'Menus and dialogs', title: 'Account menu header', snap: 'home-dark-user-menu', find: () => Q('[data-testid=user-menu-header]').parentElement, states: R },
  { key: 'user-menu-item', group: 'Menus and dialogs', title: 'Account menu item', snap: 'home-dark-user-menu', find: () => Q('[data-testid=user-menu-settings]'), states: HV, extra: { twoLine: { find: () => Q('[data-testid=user-menu-console]') } } },
  { key: 'chat-menu', group: 'Menus and dialogs', title: 'Chat row menu', snap: 'home-dark-chat-menu', find: () => MN(), states: R },
  { key: 'chat-menu-item-danger', group: 'Menus and dialogs', title: 'Chat menu Delete item', snap: 'home-dark-chat-menu', find: () => Q('[data-testid=delete-chat-trigger]'), states: HV },
  { key: 'more-menu', group: 'Menus and dialogs', title: 'Sidebar More menu', snap: 'artifacts-dark-more-menu', find: () => MN(), states: R },
  { key: 'more-menu-item', group: 'Menus and dialogs', title: 'More menu item', snap: 'artifacts-dark-more-menu', find: () => C(T('Projects', MN()), '[role=menuitem]'), states: HV },
  { key: 'search-dialog', group: 'Menus and dialogs', title: 'Search dialog', snap: 'home-dark-search', find: () => Q('[data-cds=Dialog]'), states: R, desc: '672 wide, a field row over a list of results with a time group at the end of each row.' },
  { key: 'dialog-backdrop', group: 'Menus and dialogs', title: 'Dialog backdrop', snap: 'home-dark-search', find: () => Q('.fixed.inset-0.bg-backdrop'), states: R, crop: false },
  { key: 'search-field', group: 'Menus and dialogs', title: 'Search field row', snap: 'home-dark-search', find: () => Q('textarea[aria-label="Search chats and projects"]').parentElement, focusOn: () => Q('textarea[aria-label="Search chats and projects"]'), states: ['default', 'focus-visible'] },
  { key: 'search-result', group: 'Menus and dialogs', title: 'Search result row', snap: 'home-dark-search', find: () => Q('[role=option][aria-selected=false]'), states: HV, extra: { selected: { find: () => Q('[role=option][aria-selected=true]') } } },
  { key: 'search-result-time', group: 'Menus and dialogs', title: 'Search result time', snap: 'home-dark-search', find: () => T('Today', Q('[data-cds=Dialog]')), states: R },
  { key: 'dialog-close', group: 'Menus and dialogs', title: 'Dialog close button', snap: 'home-dark-search', find: () => Q('[data-cds=Dialog] button[aria-label=Close]'), states: ALL },

  // ---------------- Settings
  { key: 'settings-dialog', group: 'Settings', title: 'Settings dialog', snap: 'settings-dark-general', find: () => Q('[data-cds=Dialog]'), states: R, pad: 0, desc: '1024x800 at 1440: a 192 nav column with a right rule, the General pane to the right.' },
  { key: 'settings-nav', group: 'Settings', title: 'Settings nav column', snap: 'settings-dark-general', find: () => Q('nav[aria-label=Settings]'), states: R },
  { key: 'settings-search', group: 'Settings', title: 'Settings search field', snap: 'settings-dark-general', find: () => Q('nav[aria-label=Settings] [role=button]'), focusOn: () => Q('input[aria-label="Search settings"]'), states: ['default', 'hover', 'focus-visible'] },
  { key: 'settings-nav-label', group: 'Settings', title: 'Settings nav group label', snap: 'settings-dark-general', find: () => T('Customize', Q('nav[aria-label=Settings]')), states: R },
  { key: 'settings-nav-item', group: 'Settings', title: 'Settings nav item', snap: 'settings-dark-general', find: () => Q('[data-testid=account-settings]'), states: ALL, extra: { refresh: { snap: 'settings-dark-account', find: () => Q('[data-testid=general-settings]'), states: RF }, active: { find: () => Q('[data-testid=general-settings]'), states: ['hover'] } } },
  { key: 'settings-section-title', group: 'Settings', title: 'Settings section title (h3)', snap: 'settings-dark-general', find: () => T('Appearance'), states: R },
  { key: 'settings-row', group: 'Settings', title: 'Settings row', snap: 'settings-dark-general', find: () => C(T('Theme', Q('[data-cds=Dialog]')), '[role=group]'), states: R, desc: 'Title (and an optional description) at the start, the control at the end; groups separated by hairlines (.settings-group-dividers).' },
  { key: 'settings-row-title', group: 'Settings', title: 'Settings row title', snap: 'settings-dark-general', find: () => T('Chat font', Q('[data-cds=Dialog]')), states: R },
  { key: 'settings-row-desc', group: 'Settings', title: 'Settings row description', snap: 'settings-dark-general', find: () => TS('Get notified when Claude has finished'), states: R },
  { key: 'settings-divider-group', group: 'Settings', title: 'Settings row group', snap: 'settings-dark-general', find: () => Q('.settings-group-dividers'), states: R },
  { key: 'theme-picker', group: 'Settings', title: 'Theme picker', snap: 'settings-dark-general', find: () => Q('[data-cds=SegmentedControl][aria-label=Theme]'), states: R, desc: 'Three icon segments: System, Light, Dark.' },
  { key: 'theme-option', group: 'Settings', title: 'Theme option', snap: 'settings-dark-general', find: () => Q('[role=radio][aria-label=Light]'), states: ALL, extra: { checked: { find: () => Q('[role=radio][aria-label=System]') } } },
  { key: 'text-segment', group: 'Settings', title: 'Text segmented control (Motion)', snap: 'settings-dark-general', find: () => Q('[data-cds=SegmentedControl][aria-label=Motion]'), states: R },
  { key: 'select', group: 'Settings', title: 'Select (Chat font)', snap: 'settings-dark-general', find: () => Q('[data-cds=Combobox]'), states: ALL, desc: 'cds Combobox: the value and a chevron in a control-height field.' },
  { key: 'switch', group: 'Settings', title: 'Switch', snap: 'settings-dark-general', find: () => Q('[role=switch][aria-checked=false]'), states: ALL, desc: '36x20 track (--cds-switch-track), a 16px knob with shadow-sm that slides on --cds-dur-snap.', extra: { on: { find: () => Q('[role=switch][aria-checked=true]'), states: ['hover'] } } },
  { key: 'switch-knob', group: 'Settings', title: 'Switch knob', snap: 'settings-dark-general', find: () => Q('[role=switch] span'), states: R },
  { key: 'settings-close', group: 'Settings', title: 'Settings close button', snap: 'settings-dark-general', find: () => Q('[data-cds=Dialog] button[aria-label=Close]'), states: ALL },

  // ---------------- Thread
  { key: 'transcript', group: 'Thread', title: 'Transcript column', snap: 'thread-dark', find: () => Q('[data-testid=transcript-list]'), states: R, pad: 0, desc: '768 wide (--transcript-width 48rem), centred in the pane.' },
  { key: 'user-message', group: 'Thread', title: 'User message bubble', snap: 'thread-dark', find: () => P(Q('[data-testid=user-message]')), states: R, desc: 'Right-aligned, at most 85% of the column (--cds-message-bubble-measure), --cds-bg-user-message, radius --cds-message-bubble-radius, padding pad-md / pad-lg.', extra: { short: { snap: 'thread-dark-followup', find: () => P(Q('[data-testid=user-message]')) } } },
  { key: 'user-message-text', group: 'Thread', title: 'User message paragraph', snap: 'thread-dark', find: () => Q('[data-testid=user-message] p'), states: R },
  { key: 'user-message-li', group: 'Thread', title: 'User message list item', snap: 'thread-dark', find: () => Q('[data-testid=user-message] li'), states: R },
  { key: 'thinking-pill', group: 'Thread', title: 'Thought for 6s', snap: 'thread-dark', find: () => Q('[data-testid=tool-status-pill]'), states: ALL, desc: 'The collapsed reasoning row: text-muted, a caret that shows on hover.' },
  { key: 'assistant-prose', group: 'Thread', title: 'Assistant prose block', snap: 'thread-dark-table', find: () => Q('[data-cds=Prose]'), states: R, crop: false, desc: 'The response in the chat font (Anthropic Serif by default, .font-claude-response).' },
  { key: 'prose-paragraph', group: 'Thread', title: 'Assistant paragraph', snap: 'thread-dark-table', find: () => T('What changed and why:'), states: R },
  { key: 'code-block', group: 'Thread', title: 'Code block', snap: 'thread-dark', find: () => Q('[role=group][aria-label="markdown code"]'), states: R, desc: 'A half-strength --bg-000 fill, a 1px hairline (the class says border-border-400, which computes to --cds-border), radius 8 (--msg-block-radius); a "markdown" label row, a copy button shown on hover, then the <pre>.' },
  { key: 'code-label', group: 'Thread', title: 'Code block language label', snap: 'thread-dark', find: () => T('markdown'), states: R },
  { key: 'code-copy', group: 'Thread', title: 'Code block copy button', snap: 'thread-dark', find: () => document.querySelector('button[aria-label="Copy to clipboard"]'), hoverOn: () => Q('[role=group][aria-label="markdown code"]'), states: HV, desc: 'Shown when the block is hovered.' },
  { key: 'code-pre', group: 'Thread', title: 'Code block body', snap: 'thread-dark', find: () => Q('pre.code-block__code'), states: R, crop: false },
  { key: 'code-token', group: 'Thread', title: 'Code token (heading marker)', snap: 'thread-dark', find: () => T('#', Q('pre.code-block__code')), states: R, desc: 'Syntax colours are inline styles from the highlighter and do not change with the theme; read them from the dark copy.' },
  { key: 'table', group: 'Thread', title: 'Table', snap: 'thread-dark-table', find: () => Q('[data-cds=Prose] table'), states: R },
  { key: 'table-th', group: 'Thread', title: 'Table header cell', snap: 'thread-dark-table', find: () => T('Original'), states: R },
  { key: 'table-td', group: 'Thread', title: 'Table cell', snap: 'thread-dark-table', find: () => Q('[data-cds=Prose] td'), states: R },
  { key: 'message-actions', group: 'Thread', title: 'Message actions', snap: 'thread-dark-table', find: () => Q('[data-cds=MessageActions]'), states: R, desc: 'Copy, rating and retry icon buttons under a response; they reveal on hover of the row (--cds-message-actions-opacity).' },
  { key: 'message-action', group: 'Thread', title: 'Message action button', snap: 'thread-dark-table', find: () => Q('[data-cds=MessageActions] button'), states: ALL },
  { key: 'jump-to-latest', group: 'Thread', title: 'Scroll to bottom button', snap: 'thread-dark', find: () => document.querySelector('[data-testid=jump-to-latest]'), states: R, desc: 'Held at opacity 0 at this scroll position; measured as found.' },

  // ---------------- Pages
  { key: 'page-header', group: 'Pages', title: 'Page header', snap: 'artifacts-dark', find: () => Q('[data-cds=PageHeader]'), states: R, desc: 'cds PageHeader on a 960 wide page: the title in Anthropic Serif (font-voice) 24/32, actions at the end.' },
  { key: 'page-title', group: 'Pages', title: 'Page title (h1)', snap: 'artifacts-dark', find: () => Q('[data-cds=PageHeader] h1'), states: R, extra: { chats: { snap: 'chats-dark', find: () => Q('[data-cds=PageHeader] h1') }, projects: { snap: 'projects-dark', find: () => Q('[data-cds=PageHeader] h1') } } },
  { key: 'tabs', group: 'Pages', title: 'Tabs', snap: 'artifacts-dark', find: () => Q('main [data-cds=Tabs]'), states: R },
  { key: 'tab', group: 'Pages', title: 'Tab', snap: 'artifacts-dark', find: () => C(T('Yours', M()), '[role=tab]'), states: ALL, extra: { refresh: { snap: 'artifacts-dark-loading', find: () => C(T('Yours', M()), '[role=tab]'), states: RF }, selected: { find: () => C(T('All', M()), '[role=tab]'), states: ['hover'] } } },
  { key: 'header-icon-button', group: 'Pages', title: 'Page header icon button', snap: 'artifacts-dark', find: () => Q('button[aria-label="Search your artifacts"]'), states: ALL },
  { key: 'header-button', group: 'Pages', title: 'Page header button (New project)', snap: 'projects-dark', find: () => C(T('New project', M()), 'button'), states: ALL, extra: { link: { snap: 'chats-dark', find: () => Q('main a[data-cds=Button][href$="/new"]') } } },
  { key: 'notice-card', group: 'Pages', title: 'Notice card', snap: 'artifacts-dark', find: () => Q('main [data-cds=Card]'), states: R },
  { key: 'card-button', group: 'Pages', title: 'Secondary button in a card', snap: 'artifacts-dark', find: () => C(TS('Visit the standalone homepage', M()), 'button'), states: ALL },
  { key: 'dismiss-button', group: 'Pages', title: 'Dismiss button', snap: 'artifacts-dark', find: () => Q('main button[aria-label=Dismiss]'), states: ALL },
  { key: 'section-caption', group: 'Pages', title: 'Section caption (Make something new)', snap: 'artifacts-dark', find: () => T('Make something new'), states: R },
  { key: 'template-card', group: 'Pages', title: 'Make something new card', snap: 'artifacts-dark', find: () => Q('button[aria-label="Docs, Beta"]'), states: ALL, desc: '136 wide: a preview tile with --cds-radius-composer, then the name and a Beta badge.' },
  { key: 'badge', group: 'Pages', title: 'Badge (Beta)', snap: 'artifacts-dark', find: () => Q('main [data-cds=Badge]'), states: R, extra: { project: { snap: 'projects-dark', find: () => Q('main [data-cds=Badge]') } } },
  { key: 'month-heading', group: 'Pages', title: 'List group heading (September)', snap: 'artifacts-dark', find: () => T('September', M()), states: R },
  { key: 'artifact-row', group: 'Pages', title: 'Artifact list row', snap: 'artifacts-dark', find: () => C(Q('main li time'), 'li'), states: HV, desc: 'Icon, title in text-primary, a muted line ("Shared with you"), then Pin, visibility, Created or Edited with the date, and a more button.' },
  { key: 'artifact-row-meta', group: 'Pages', title: 'Artifact row subtitle', snap: 'artifacts-dark', find: () => T('Shared with you', M()), states: R },
  { key: 'artifact-row-time', group: 'Pages', title: 'Artifact row date', snap: 'artifacts-dark', find: () => Q('main li time'), states: R },
  { key: 'artifact-row-more', group: 'Pages', title: 'Artifact row more button', snap: 'artifacts-dark', find: () => C(Q('main li time'), 'li').querySelector('button[aria-label^="More options for"]'), states: ALL },
  { key: 'chats-row', group: 'Pages', title: 'Chats list row', snap: 'chats-dark', find: () => C(Q('main tr time'), 'tr'), states: HV, extra: { refresh: { snap: 'chats-dark-filter-menu', find: () => C(Q('main tr time'), 'tr'), focusOn: () => C(Q('main tr time'), 'tr').querySelector('a[href]'), states: RF } }, desc: 'A cds Table row, 53 tall: title, then the relative time in text-muted and a more button.' },
  { key: 'chats-time', group: 'Pages', title: 'Chats row time', snap: 'chats-dark', find: () => Q('main tr time'), states: R },
  { key: 'project-card', group: 'Pages', title: 'Project card', snap: 'projects-dark', find: () => C(Q('a[href*="/project/"]', 0, M()), 'li'), states: HV, extra: { refresh: { snap: 'projects-dark-2', find: () => C(Q('a[href*="/project/"]', 0, M()), 'li') || C(Q('a[href*="/project"]', 0, M()), 'div'), focusOn: () => Q('a[href*="/project"]', 0, M()), states: RF } }, desc: 'Two columns of cards: name, an optional badge, a three-line description in text-secondary, the date.' },
  { key: 'breadcrumb', group: 'Pages', title: 'Project breadcrumb', snap: 'project-dark', find: () => C(T('Projects', M()), 'a'), states: ALL },
  { key: 'project-title', group: 'Pages', title: 'Project title', snap: 'project-dark', find: () => Q('main h1'), states: R },
  { key: 'project-section-title', group: 'Pages', title: 'Project section title (Recents)', snap: 'project-dark', find: () => T('Recents', M()), states: R },
  { key: 'project-recent-row', group: 'Pages', title: 'Project recents row', snap: 'project-dark', find: () => C(Q('main tr time'), 'tr'), states: HV },
  { key: 'instructions-card', group: 'Pages', title: 'Instructions card', snap: 'project-dark', find: () => P(T('Instructions', M())), states: R, desc: 'The right rail: Instructions, Memory and Context cards, each an h3 with an edit action and a two-line muted preview.' },

  // ---------------- Mobile
  { key: 'm-show-sidebar', group: 'Mobile', title: 'Phone menu button', snap: 'mobile-home-dark', find: () => Q('[data-testid=sidebar-compact-trigger]'), states: R },
  { key: 'm-greeting', group: 'Mobile', title: 'Phone greeting', snap: 'mobile-home-dark', find: () => Q('main .font-display'), states: R },
  { key: 'm-composer', group: 'Mobile', title: 'Phone composer', snap: 'mobile-home-dark', find: () => P(Q('[data-testid=chat-input]')), states: R, desc: 'Pinned to the bottom; the Chat/Cowork segments drop to icons below 360 px.' },
  { key: 'm-segment', group: 'Mobile', title: 'Phone segment (icon only)', snap: 'mobile-home-dark', find: () => Q('main [aria-label=Surface] [role=radio][aria-checked=true]'), states: R },
  { key: 'm-drawer', group: 'Mobile', title: 'Drawer sheet', snap: 'mobile-home-dark-drawer', find: () => Q('[data-testid=sidebar][role=dialog]'), states: R, pad: 0, desc: 'The sidebar as a full-screen sheet: a close button and the wordmark, a full-width Search button, then the same rows at 44 tall.' },
  { key: 'm-drawer-search', group: 'Mobile', title: 'Drawer Search button', snap: 'mobile-home-dark-drawer', find: () => [...document.querySelectorAll('[data-testid=sidebar] button[data-cds=Button]')].find((b) => b.getBoundingClientRect().width > 300), states: R },
  { key: 'm-drawer-row', group: 'Mobile', title: 'Drawer row', snap: 'mobile-home-dark-drawer', find: () => C(T('Artifacts', Q('[role=dialog]')), 'div.group'), states: R },
  { key: 'm-thread-header', group: 'Mobile', title: 'Phone chat header', snap: 'mobile-thread-dark', find: () => Q('[data-testid=chat-header]'), states: R },
  { key: 'm-user-message', group: 'Mobile', title: 'Phone user message', snap: 'mobile-thread-dark', find: () => P(Q('[data-testid=user-message]')), states: R },

  // ---------------- Forms, feedback and states (copies taken 2026-10-17)
  { key: 'text-link', group: 'Forms and feedback', title: 'Text link', snap: 'settings-dark-capabilities', find: () => T('security risks'), states: ALLP, desc: 'cds TextLink (`a, .prose-link` in the base layer): text.accent, underlined 3px below in the link colour at 40% (--_text-link-line), the full colour on hover and focus; colour and line change on --cds-dur-fast with ease-out.', extra: { 'learn-more': { snap: 'settings-dark-account', find: () => Q('[data-cds=TextLink]'), states: ['hover'] } } },
  { key: 'tooltip', group: 'Forms and feedback', title: 'Tooltip', snap: 'home-dark-tooltip', find: () => Q('[role=tooltip]'), states: R, desc: 'Base UI tooltip on the sidebar Search button: --cds-tooltip-bg / --cds-tooltip-fg, radius 6, 13/18 text, the shortcut keys inside; opens on the snap curve (--cds-dur-snap) from 98% scale, no transition under reduced motion.' },
  { key: 'checkbox', group: 'Forms and feedback', title: 'Checkbox', snap: 'chats-dark-select', find: () => Q('[data-cds=Checkbox][aria-checked=false] > span'), hoverOn: () => Q('[data-cds=Checkbox][aria-checked=false]'), focusOn: () => Q('[data-cds=Checkbox][aria-checked=false]'), states: ALLP, desc: 'cds Checkbox, size xs, in the Chats table once Select is on: a --cds-checkbox square with --cds-checkbox-radius and a border-strong edge, filled with the accent and a check glyph when checked.', extra: { checked: { find: () => Q('[data-cds=Checkbox][aria-checked=true] > span'), states: ['hover'] } } },
  { key: 'selection-bar', group: 'Forms and feedback', title: 'Selection actions (Select mode)', snap: 'chats-dark-select', find: () => C(T('1 selected'), 'div'), states: R, desc: 'Replaces Select and New in the page header: a muted count, Select all (secondary), Delete (danger, filled) and an exit button.' },
  { key: 'button-danger', group: 'Forms and feedback', title: 'Danger button', snap: 'chats-dark-delete-confirm', find: () => [...document.querySelectorAll('[data-cds=ConfirmationDialog] button')].find((b) => b.innerText.trim() === 'Delete'), states: ALLP, desc: 'fill.danger with on.danger text; the only red control, used for the confirming action of a destructive dialog and the bulk Delete.' },
  { key: 'button-secondary', group: 'Forms and feedback', title: 'Secondary button', snap: 'chats-dark-delete-confirm', find: () => [...document.querySelectorAll('[data-cds=ConfirmationDialog] button')].find((b) => b.innerText.trim() === 'Cancel'), states: ALLP, desc: 'fill.secondary with a 1px ring (fill.secondary-ring); takes the focus when the dialog opens, so the safe choice is the default.' },
  { key: 'confirm-dialog', group: 'Forms and feedback', title: 'Confirmation dialog', snap: 'chats-dark-delete-confirm', find: () => Q('[data-cds=ConfirmationDialog]'), states: R, desc: 'cds ConfirmationDialog (role=alertdialog), at most 400 wide: a heading, one sentence, then Cancel and the action at the end; surface-3, radius card, shadow-panel-lg, over the page backdrop.' },
  { key: 'form-dialog', group: 'Forms and feedback', title: 'Form dialog (Create a project)', snap: 'projects-dark-create', prep: VALID, find: () => Q('[data-cds=Dialog]'), states: R, desc: 'A cds Dialog with a title, two labelled fields, and Cancel / Create project at the end.' },
  { key: 'field-label', group: 'Forms and feedback', title: 'Field label', snap: 'projects-dark-create', prep: VALID, find: () => T('What are you working on?'), states: R },
  { key: 'text-field', group: 'Forms and feedback', title: 'Text field', snap: 'projects-dark-create', prep: VALID, find: () => Q('[data-cds=TextInput]'), focusOn: () => Q('[data-cds=TextInput] input') || Q('input[placeholder="Name your project"]'), states: ALL, desc: 'cds TextInput: control height, fill.field with a 1px fill.field-ring, border-strong on hover, the focus ring on focus.' },
  { key: 'text-field-invalid', group: 'Forms and feedback', title: 'Text field, invalid', snap: 'projects-dark-create', prep: () => Q('[data-cds=TextInput]').setAttribute('data-invalid', ''), find: () => Q('[data-cds=TextInput]'), focusOn: () => Q('[data-cds=TextInput]'), states: ['default', 'hover', 'focus-visible'], desc: 'The error state, read by setting data-invalid on the field in the copy, which is what cds Field does when validation fails: Claude\'s own `data-[invalid]:` rules then draw a 1px fill.danger ring, keep it on hover, and switch the focus ring to shadow.focus-danger. The live form was never submitted, so the message text cds shows under the field was not seen.' },
  { key: 'text-area', group: 'Forms and feedback', title: 'Text area', snap: 'projects-dark-create', prep: VALID, find: () => Q('[data-cds=TextArea]'), focusOn: () => Q('textarea'), states: ALL, desc: 'cds TextArea: the text field\'s fill, ring and focus, several lines tall, resizable.' },
  { key: 'button-primary', group: 'Forms and feedback', title: 'Primary button', snap: 'projects-dark-create', prep: VALID, find: () => [...document.querySelectorAll('[data-cds=Dialog] button')].find((b) => b.innerText.trim() === 'Create project'), states: ALLP, desc: 'fill.primary (ink: white in dark, black in light) with on.primary text.' },
  { key: 'button-disabled', group: 'Forms and feedback', title: 'Disabled button', snap: 'settings-dark-account', find: () => [...document.querySelectorAll('[data-cds=Dialog] button')].find((b) => b.innerText.trim() === 'Delete account'), states: HVP, desc: 'Delete account while a paid plan is active: the secondary button at the disabled opacity; hover and press change nothing.' },
  { key: 'switch-disabled', group: 'Forms and feedback', title: 'Disabled switch', snap: 'settings-dark-capabilities', find: () => Q('[role=switch][data-disabled]') || Q('[role=switch][aria-disabled=true]'), states: HV, desc: 'Artifacts, on and locked while another setting needs it: the switch at the disabled opacity.' },
  { key: 'search-input', group: 'Forms and feedback', title: 'List search field', snap: 'chats-dark-search-empty', find: () => Q('[data-cds=TextInput]'), focusOn: () => Q('input[type=search]'), states: ['default', 'focus-visible'], desc: 'Chats and tasks search, opened from the header icon: a text field with a leading glyph and a clear button.' },
  { key: 'empty-state', group: 'Forms and feedback', title: 'Empty result', snap: 'chats-dark-search-empty', find: () => TS('Nothing matches'), states: R, desc: 'One centred muted line quoting the query; no illustration, no action.' },
  { key: 'filter-menu', group: 'Forms and feedback', title: 'Filter menu', snap: 'chats-dark-filter-menu', prep: UNLIT, find: () => MN(), states: R, desc: 'The Chats filter: All, Chat, Shared, Cowork, Archived, the current one ticked in the accent.' },
  { key: 'filter-menu-item', group: 'Forms and feedback', title: 'Filter menu item', snap: 'chats-dark-filter-menu', prep: UNLIT, find: () => [...MN().querySelectorAll('[role^=menuitem]')][1], states: HV, extra: { checked: { find: () => [...MN().querySelectorAll('[role^=menuitem]')][0] } } },
  { key: 'menu-item-keyboard', group: 'Forms and feedback', title: 'Menu item, keyboard focus', snap: 'chats-dark-filter-menu', prep: () => { const it = [...MN().querySelectorAll('[role^=menuitem]')][1]; it.setAttribute('data-highlighted', ''); it.focus(); }, find: () => [...MN().querySelectorAll('[role^=menuitem]')][1], states: R, desc: 'Keyboard focus in a cds Menu: Base UI moves focus to the item with the arrow keys and marks it data-highlighted, which paints the same fill.ghost-hover wash as the pointer; there is no ring. Read by setting data-highlighted and focusing the item in the copy, since the copy runs no scripts. Every cds Menu (plus, model, account, chat row, More, filter) uses this item.' },
  { key: 'skeleton', group: 'Forms and feedback', title: 'Loading skeleton', snap: 'artifacts-dark-loading', find: () => Q('[data-cds=Skeleton]'), states: R, desc: 'cds Skeleton: a --cds-skeleton-base bar with a --cds-skeleton-sheen band sweeping across every 2s (cds-shimmer); the sheen is hidden under reduced motion.' },
  { key: 'skeleton-card', group: 'Forms and feedback', title: 'Loading card', snap: 'artifacts-dark-loading', find: () => C(Q('[data-cds=Skeleton]', 2), '[class*=rounded]'), states: R },
  { key: 'artifacts-grid', group: 'Forms and feedback', title: 'Artifacts card grid', snap: 'artifacts-dark-loading', find: () => [...M().querySelectorAll('*')].find((e) => getComputedStyle(e).display === 'grid' && getComputedStyle(e).gridTemplateColumns.split(' ').length >= 3), states: R, crop: false, desc: 'The Artifacts page as a grid of cards (loading), read for its column count and gap.' },
  { key: 'projects-grid', group: 'Forms and feedback', title: 'Projects card grid', snap: 'projects-dark-2', find: () => [...M().querySelectorAll('*')].find((e) => getComputedStyle(e).display === 'grid' && getComputedStyle(e).gridTemplateColumns.split(' ').length >= 2), states: R, crop: false, desc: 'The Projects page grid of cards, read for its column count and gap.' },
  { key: 'button-primary-page', group: 'Forms and feedback', title: 'Primary button on a page (New project)', snap: 'projects-dark-2', find: () => [...M().querySelectorAll('button')].find((b) => b.innerText.trim() === 'New project'), states: ALLP },
  { key: 'banner-info', group: 'Forms and feedback', title: 'Information banner', snap: 'settings-dark-capabilities', find: () => Q('[data-cds=Banner]'), states: R, desc: 'cds Banner, role=status, the neutral tone: an info glyph, body text with an inline link, on surface-1 inside a 1px ring (--cds-banner-neutral-ring, which falls back to the ring colour). Claude has no info hue; this neutral banner is how it informs.' },
  { key: 'banner-info-icon', group: 'Forms and feedback', title: 'Information banner glyph', snap: 'settings-dark-capabilities', find: () => Q('[data-cds=Banner] [data-cds=Icon]'), states: R },
  { key: 'banner-info-text', group: 'Forms and feedback', title: 'Information banner message', snap: 'settings-dark-capabilities', find: () => Q('[data-cds=Banner] .min-w-0 > div'), states: R, desc: 'The banner text read on its own (the banner entry above reads its glyph first).' },
  { key: 'toast', group: 'Forms and feedback', title: 'Toast (warning)', snap: 'home-dark-toast', find: () => Q('[data-cds=Toast] [role=dialog] > div'), states: R, desc: 'The toast raised after opening a chat that no longer exists: bottom right, radius card, surface-3 under a bg.warning layer, a 1px warning ring (shadow-ring-warning), text.warning, a 20px warning glyph, a medium-weight message and a 16px Dismiss button. Toasts stack upward 14px apart and shrink 4% per step.' },
  { key: 'toast-text', group: 'Forms and feedback', title: 'Toast message', snap: 'home-dark-toast', find: () => Q('[data-cds=Toast] h2'), states: R, desc: 'The toast message read on its own (the toast entry above reads its glyph first).' },
  { key: 'toast-dismiss', group: 'Forms and feedback', title: 'Toast dismiss button', snap: 'home-dark-toast', find: () => Q('[data-cds=Toast] button[aria-label=Dismiss]'), states: ALL },
  { key: 'onboarding-card', group: 'Forms and feedback', title: 'Onboarding card', snap: 'onboarding-dark', find: () => C(Q('form [data-cds=Checkbox]'), '.rounded-2xl'), states: R, desc: 'The first-run screen at /onboarding: the wordmark, a serif display title, a secondary line, then one card on surface-3 (radius 16, a border and shadow-sm) holding the two consent checkboxes and a full-width primary button; the verified email and a link to change it sit at the foot of the page.' },
  { key: 'onboarding-title', group: 'Forms and feedback', title: 'Onboarding title', snap: 'onboarding-dark', find: () => Q('h1'), states: R },
  { key: 'onboarding-checkbox', group: 'Forms and feedback', title: 'Consent checkbox with label', snap: 'onboarding-dark', find: () => C(Q('form [data-cds=Checkbox]'), 'label'), focusOn: () => Q('form [data-cds=Checkbox]'), states: ALL },
  { key: 'onboarding-checkbox-label', group: 'Forms and feedback', title: 'Consent checkbox label', snap: 'onboarding-dark', find: () => [...document.querySelectorAll('form label span')].find((e) => e.innerText.startsWith('I agree')), states: R, desc: 'The label text read on its own (the checkbox entries read the check glyph first), with its inline TextLinks.' },
  { key: 'onboarding-subtitle', group: 'Forms and feedback', title: 'Onboarding secondary line', snap: 'onboarding-dark', find: () => Q('header p'), states: R },
  { key: 'onboarding-button', group: 'Forms and feedback', title: 'Create account button', snap: 'onboarding-dark', find: () => [...document.querySelectorAll('form button')].find((b) => b.innerText.trim() === 'Create account'), states: ALLP },
];

// ---------------------------------------------------------------- jobs

function jobsFor(spec) {
  const out = [];
  for (const st of spec.states) out.push({ state: st, base: st, snap: spec.snap, find: spec.find, hoverOn: spec.hoverOn, focusOn: spec.focusOn, prep: spec.prep });
  for (const [name, v] of Object.entries(spec.extra || {})) {
    out.push({ state: name, base: 'default', snap: v.snap || spec.snap, find: v.find, variant: true });
    for (const st of v.states || []) out.push({ state: `${name}-${st}`, base: st, snap: v.snap || spec.snap, find: v.find, focusOn: v.focusOn, hoverOn: v.hoverOn, variant: true });
  }
  return out;
}

const MOBILE = (label) => label.startsWith('mobile-');

// The context is closed however measuring ends, so a copy that throws does not keep its pages open
// while the other workers go on.
async function measureSnap(browser, label, specs, out) {
  const meta = metaOf(label);
  const ctx = await newContext(browser, meta);
  try {
    return await measureIn(ctx, meta, label, specs, out);
  } finally {
    await ctx.close().catch(() => {});
  }
}

async function measureIn(ctx, meta, label, specs, out) {
  await ctx.addInitScript(HELPERS);
  let page;
  try {
    page = await openSnap(ctx, label);
  } catch (e) {
    log('  ! open failed', label, e.message.split('\n')[0]);
    return false;
  }
  const rest = { x: meta.w - 2, y: Math.round(meta.h / 2) };
  await page.evaluate(() => window.__saveScroll());
  const resetPage = async () => {
    await page.evaluate(() => { if (document.activeElement && document.activeElement.blur) document.activeElement.blur(); });
    await page.mouse.move(rest.x, rest.y);
    await page.evaluate(() => { window.__restoreScroll(); window.__freeze(); });
    await page.waitForTimeout(200);
  };
  const tag = async (fn, name) => {
    if (!fn) return null;
    const h = await page.evaluateHandle(`(() => { try { return (${fn.toString()})(); } catch (e) { return null; } })()`);
    const el = h.asElement();
    if (!el) return null;
    await el.evaluate((e, n) => e.setAttribute(`data-mt-${n}`, ''), name);
    return page.locator(`[data-mt-${name}]`).first();
  };
  const untag = () => page.evaluate(() => document.querySelectorAll('*').forEach((n) => { for (const a of [...n.attributes]) if (a.name.startsWith('data-mt-')) n.removeAttribute(a.name); }));
  const ensureVisible = (loc) => loc.evaluate((el) => {
    const r = el.getBoundingClientRect();
    if (r.top < 0 || r.bottom > innerHeight || r.left < 0 || r.right > innerWidth) el.scrollIntoView({ block: r.height > innerHeight ? 'start' : 'center', inline: 'nearest', behavior: 'instant' });
  });
  const pointOf = (loc) => loc.evaluate((el) => {
    const r = [...el.getClientRects()].find((x) => x.width > 0 && x.height > 0) || el.getBoundingClientRect();
    return { x: r.x + Math.min(r.width / 2, 40), y: r.y + Math.min(r.height / 2, 20) };
  });
  const kbFocus = async (loc) => {
    const ok0 = await loc.evaluate((el) => window.__isFocusable(el));
    if (!ok0) return { ok: false, how: 'not focusable in the static copy (no tabindex)' };
    await loc.evaluate((el) => el.focus());
    await page.keyboard.press('Shift+Tab');
    await page.keyboard.press('Tab');
    let ok = await loc.evaluate((el) => document.activeElement === el);
    let how = 'keyboard: focus(), Shift+Tab, Tab';
    if (!ok) {
      await page.keyboard.press('Shift');
      await loc.evaluate((el) => el.focus());
      ok = await loc.evaluate((el) => document.activeElement === el);
      how = 'keyboard: Shift keydown, then focus()';
    }
    await page.waitForTimeout(350);
    return { ok, how, matches: await loc.evaluate((el) => el.matches(':focus-visible')) };
  };
  const crop = async (loc, name, pad) => {
    const vp = page.viewportSize();
    const box = await loc.boundingBox();
    if (!box) throw new Error('no box');
    const clip = { x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad) };
    clip.width = Math.min(vp.width, box.x + box.width + pad) - clip.x;
    clip.height = Math.min(vp.height, box.y + box.height + pad) - clip.y;
    if (clip.width < 1 || clip.height < 1) throw new Error('off screen');
    const file = path.join(CROPS, `${name}.png`);
    await page.screenshot({ path: file, clip, animations: 'allow' });
    execFileSync(PYTHON, ['-c', 'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width>1600: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)', file]);
    return path.relative(REF, file);
  };

  for (const theme of ['dark', 'light']) {
    if (theme === 'light') {
      await setLight(page);
      await page.waitForTimeout(600);
    }
    for (const { spec, job } of specs) {
      const state = theme === 'dark' ? job.state : job.state === 'default' ? 'light' : `light-${job.state}`;
      const c = out.components[spec.key];
      const name = `${spec.key}-${state}`;
      if (MOBILE(label) && job.base === 'hover') continue;
      try {
        await resetPage();
        if (job.prep) { await page.evaluate(`(${job.prep.toString()})()`); await page.waitForTimeout(250); }
        const loc = await tag(job.find, 'el');
        if (!loc) throw new Error('element not found');
        await ensureVisible(loc);
        let via = job.variant && job.base === 'default' ? `at rest, captured ${job.state}` : 'at rest';
        let focus;
        if (job.base === 'hover') {
          const hl = (job.hoverOn && (await tag(job.hoverOn, 'hv'))) || loc;
          const p = await pointOf(hl);
          await page.mouse.move(p.x, p.y, { steps: 4 });
          // A second, sub-pixel move: an element revealed by group-hover only takes :hover itself
          // once the pointer moves again.
          await page.waitForTimeout(80);
          await page.mouse.move(p.x + 0.5, p.y);
          await page.waitForTimeout(450);
          via = job.hoverOn ? 'mouse hover on its row' : 'mouse hover';
        } else if (job.base === 'pressed') {
          // Drop any earlier keyboard focus first (no click is dispatched anywhere), so the browser
          // does not carry a focus-visible over to the press.
          await resetPage();
          const p = await pointOf(loc);
          await page.mouse.move(p.x, p.y, { steps: 4 });
          await page.waitForTimeout(150);
          await page.mouse.down();
          // A dialog's buttons can keep focus-visible from the dialog's own initial focus; drop it
          // so the reading is the press alone (:active outlives the blur while the button is held).
          await loc.evaluate((el) => { const a = document.activeElement; if (a && a !== document.body && a.matches(':focus-visible')) a.blur(); });
          await page.waitForTimeout(250);
          via = 'pointer held down (:active)';
        } else if (job.base === 'focus-visible') {
          let fl = job.focusOn ? await tag(job.focusOn, 'fo') : null;
          if (!fl) {
            const h = await loc.evaluateHandle((el) => window.__focusTarget(el));
            if (h.asElement()) { await h.asElement().evaluate((e) => e.setAttribute('data-mt-fo', '')); fl = page.locator('[data-mt-fo]').first(); }
          }
          focus = fl ? await kbFocus(fl) : { ok: false, how: 'not focusable in the static copy (no tabindex)' };
          if (!focus.ok) { c.states[state] = { theme, snapshot: label, skipped: focus.how }; log('  -', name, 'skipped:', focus.how); continue; }
          via = focus.how + (fl && !(await fl.evaluate((e) => e.hasAttribute('data-mt-el'))) ? ' (on the field inside)' : '');
        }
        const s = await loc.evaluate(styleOf, PROPS);
        if (focus) s.focus = focus;
        // Is something else painted over the element's centre? (Then its crop shows that instead.)
        const hit = await loc.evaluate((el) => {
          const r = el.getBoundingClientRect();
          const x = Math.min(Math.max(r.x + r.width / 2, 1), innerWidth - 1);
          const y = Math.min(Math.max(r.y + r.height / 2, 1), innerHeight - 1);
          const h = document.elementFromPoint(x, y);
          if (!h || el.contains(h) || h.contains(el)) return null;
          return h.tagName.toLowerCase() + '.' + String(h.className).split(/\s+/).slice(0, 3).join('.');
        });
        if (hit) { s.occludedBy = hit.slice(0, 120); log('  ?', name, 'centre covered by', hit.slice(0, 80)); }
        if (spec.crop !== false) {
          try { s.crop = await crop(loc, name, spec.pad ?? 8); } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
        }
        c.states[state] = { theme, snapshot: label, ...s, via };
        if (job.find !== spec.find) (c.selectors ||= {})[state] = job.find.toString();
        log('  ', name, `${s.rect.w}x${s.rect.h}`, via.slice(0, 50));
      } catch (e) {
        c.states[state] = { theme, snapshot: label, error: String(e.message || e).slice(0, 200) };
        log('  !', name, String(e.message || e).slice(0, 120));
      } finally {
        // off the element before the button comes up: a down and up on the same element is a click
        await page.mouse.move(rest.x, rest.y).catch(() => {});
        await page.mouse.up().catch(() => {});
        await untag().catch(() => {});
      }
    }
  }
  return true;
}

// ---------------------------------------------------------------- main

// The copies taken on 2026-10-17 for the refresh; every other copy is from 2026-10-04.
const READ = Object.fromEntries(['home-dark-tooltip', 'settings-dark-account', 'settings-dark-capabilities', 'chats-dark-select', 'chats-dark-search-empty', 'chats-dark-filter-menu', 'chats-dark-delete-confirm', 'projects-dark-create', 'projects-dark-2', 'artifacts-dark-loading', 'home-dark-toast', 'onboarding-dark'].map((l) => [l, '2026-10-17']));
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
const labels = [...new Set(SPECS.flatMap((s) => jobsFor(s).map((j) => j.snap)))].filter((l) => !ONLY.length || ONLY.includes(l));
out._meta = {
  read: '2026-10-04',
  source: 'Static, redacted copies of the signed-in claude.ai app (tools/capture/signed-in/snapshot.js) with every stylesheet inlined, loaded from file:// in headless Chromium; fonts and images come from assets-proxy.anthropic.com through a local cache. Nothing was requested from claude.ai.',
  viewport: '1440x900 (the mobile-* snapshots 390x844), deviceScaleFactor 2',
  themes: 'Each copy was captured in the dark theme. Dark states have plain names; light states (`light`, `light-<state>`) were read from the same DOM with every [data-mode] element set to light. Every state records `theme` and `snapshot`.',
  states: {
    default: 'at rest, as captured',
    hover: 'real mouse hover (page.mouse.move), 450ms settle; not measured on the 390 copies',
    'focus-visible': 'real keyboard focus (focus, Shift+Tab, Tab) on the element or its first focusable descendant; recorded as skipped where the element cannot take focus',
    pressed: 'the pointer held down on the element for 250ms (:active), read before release',
    other: 'active / selected / checked / open / typed / enabled / ... are other elements or snapshots captured in that state',
  },
  tokens: '`vars` lists every var(--x) named in the classes of the element and its first descendants, resolved in that state\'s theme.',
  refreshed: '2026-10-17: new copies for forms, feedback and states (see READ); the 2026-10-04 readings are kept as they were',
  // Entries kept from an earlier run go through safeUrl again, so a partial rerun never writes an
  // unmasked URL it carried over; new ones keep only origin and route words (no query, no fragment, no id).
  snapshots: { ...Object.fromEntries(Object.entries((out._meta && out._meta.snapshots) || {}).map(([l, v]) => [l, { ...v, url: v.url && safeUrl(v.url) }])), ...Object.fromEntries(labels.map((l) => { const m = metaOf(l); return [l, { url: safeUrl(m.url), title: m.title, w: m.w, h: m.h, read: READ[l] || '2026-10-04', ...(SCROLL[l] ? { scroll: SCROLL[l] } : {}) }]; })) },
};
out.components ??= {};
fs.mkdirSync(CROPS, { recursive: true });

// Build the per-snapshot job lists, and the states each copy re-measures (moved aside while it runs).
const bySnap = new Map();
const RESET = new Map();
for (const spec of SPECS) {
  const c = (out.components[spec.key] ??= { states: {} });
  Object.assign(c, { group: spec.group, title: spec.title, desc: spec.desc, page: spec.snap, selector: spec.find.toString() });
  const jobs = jobsFor(spec);
  c.pages = [...new Set(jobs.map((j) => j.snap))];
  for (const job of jobs) {
    if (!labels.includes(job.snap)) continue;
    if (!RESET.has(job.snap)) RESET.set(job.snap, []);
    RESET.get(job.snap).push([c, job.state], [c, job.state === 'default' ? 'light' : `light-${job.state}`]);
    if (!bySnap.has(job.snap)) bySnap.set(job.snap, []);
    bySnap.get(job.snap).push({ spec, job });
  }
}

const browser = await chromium.launch();
const queue = [...bySnap.keys()].sort();
// Earlier readings of the states a copy in flight is re-measuring, by component. save() writes them
// wherever no new reading exists yet, so while workers run, the file on disk never loses one.
const earlier = new Map();
const save = () => {
  // Stable order: components in SPECS order, states in the order the spec lists them, dark then light.
  const comps = {};
  for (const spec of SPECS) {
    const c = out.components[spec.key];
    const names = jobsFor(spec).map((j) => j.state);
    const ordered = {};
    const prev = earlier.get(c) || {};
    const pick = (n) => c.states[n] || prev[n];
    for (const n of names) if (pick(n)) ordered[n] = pick(n);
    for (const n of names) { const l = n === 'default' ? 'light' : `light-${n}`; if (pick(l)) ordered[l] = pick(l); }
    comps[spec.key] = { ...c, states: ordered };
  }
  fs.writeFileSync(OUT, JSON.stringify({ _meta: out._meta, components: comps }, null, 1) + '\n');
};
await Promise.all(Array.from({ length: Math.min(CONC, queue.length) }, async () => {
  while (queue.length) {
    const label = queue.shift();
    log('open', label, `(${bySnap.get(label).length} jobs x 2 themes)`);
    // This copy's earlier readings move to `earlier` for the run: replaced once the copy opened and
    // was measured, put back if it never opened or the run threw, so neither a failed open nor
    // another worker's save can erase what an earlier run measured.
    const kept = [];
    for (const [c, n] of RESET.get(label) || []) {
      if (!(n in c.states)) continue;
      if (!earlier.has(c)) earlier.set(c, {});
      earlier.get(c)[n] = c.states[n];
      kept.push([c, n]);
      delete c.states[n];
    }
    let opened = false;
    try {
      opened = await measureSnap(browser, label, bySnap.get(label), out);
    } catch (e) {
      log('  ! measuring failed', label, String(e.message || e).split('\n')[0]);
    }
    for (const [c, n] of kept) {
      if (!opened) c.states[n] ??= earlier.get(c)[n];
      delete earlier.get(c)[n];
    }
    save();
  }
}));
await browser.close();
save();
const all = SPECS.map((sp) => out.components[sp.key]);
const states = all.flatMap((c) => Object.values(c.states));
log(`${all.length} components, ${states.length} states (${states.filter((s) => s.error).length} errors, ${states.filter((s) => s.skipped).length} skipped)`);
