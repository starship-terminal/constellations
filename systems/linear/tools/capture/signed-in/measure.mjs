// Measures Linear's signed-in components from the static page copies (see render.mjs, unsnap.py),
// in both themes and in every state CSS can reach once scripts are gone. Adapted from the kit
// (tools/kit/capture/signed-in/measure.mjs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> node tools/capture/signed-in/measure.mjs [label ...] [--jobs N]
//
// With labels, only the components (and states) that live on those copies are re-measured and
// merged into the existing JSON. Writes raw/components-computed.json and one crop per component
// and state into components/crops/<component>-<state>.png (2x, 256 colours, halved when wider than
// 1600px). raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// Themes: Linear generates its palette by script into a constructed stylesheet, so a copy keeps the
// theme it was taken in. Each spec names its dark copy (`issue-dark`); the same spec is measured
// again on the light copy of that page (`issue-light`) when one exists. Dark states keep their
// plain names (`default`, `hover`, ...); light states are `light`, `light-hover`, ... and every
// state records `theme`.
//
// States:
//   default        at rest, as captured
//   hover          real mouse hover (page.mouse.move), 450ms settle; Tailwind's hover: variants
//                  (inside @media (hover: hover)) are plain CSS, so they apply on the static copy
//   focus-visible  real keyboard focus: focus(), Shift+Tab, Tab (or a Shift keydown then focus()),
//                  on the element or its first focusable descendant
//   pressed        mouse hover, then the button held down (page.mouse.down) for 250ms, so :active
//                  applies; released after the reading
//   anything else  another element, or another copy, captured in that state: `active`, `selected`,
//                  `checked`, `open`, `typed`, `on`, ...
// The pressed state releases the mouse over the element, so a click event fires, but the copies have
// no scripts, clicks are cancelled, and every navigation away from the file is aborted.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { chromium, REF, RAW, CROPS, SNAPS, SCROLL, metaOf, newContext, openSnap, setLight } from './lib.mjs';

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
    // PRODUCT (adapt): Linear's main content area and the sidebar (the column left of 245px).
    M: () => document.querySelector('main'),
    S: () => [...document.querySelectorAll('nav, [role=navigation]')].find((n) => n.getBoundingClientRect().x < 50) || null,
    // Linear (adapt): an element by exact text, then the closest button, link or row around it.
    TB: (text, root) => { const t = byText((x) => x === text, text, root); return t ? (t.closest('button, a, [role=button], [role=option], [role=tab]') || t) : null; },
    // The first ancestor of el (or el) that casts a box-shadow: a menu's or popover's surface.
    SHD: (el) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (getComputedStyle(n).boxShadow !== 'none') return n; return null; },
    // The highlight box Linear slides under the active option of a listbox (a separate absolutely
    // positioned div, moved by script).
    HL: () => { const lb = Q('[role=listbox]'); return lb ? [...lb.parentElement.querySelectorAll('div')].find((d) => { const c = getComputedStyle(d); const r = d.getBoundingClientRect(); return c.position === 'absolute' && r.height >= 26 && r.height <= 40 && c.backgroundColor !== 'rgba(0, 0, 0, 0)'; }) || null : null; },
    // The innermost painted box of at least w x h that contains el.
    BOX: (el, w, h) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) { const r = n.getBoundingClientRect(); if (r.width >= w && r.height >= h && paints(n)) return n; } return null; },
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
const ALLP = ['default', 'hover', 'focus-visible', 'pressed'];
const HV = ['default', 'hover'];
const HF = ['default', 'hover', 'focus-visible'];
const R = ['default'];

// Linear (adapt): one entry per checklist component this capture reached. Finders use roles,
// aria-labels, input types, structure and Linear's own UI words, never account text (the copies'
// titles were scrubbed to "Sample ..." anyway). `snap` is the dark copy; the light copy of the same
// page is measured too when it exists.
const SPECS = [
  // Buttons
  { key: 'button-primary', group: 'Buttons', title: 'Primary button (Create issue)', desc: 'The composer submit button.', snap: 'composer-dark', find: () => Q('[role=dialog] button[type=submit]'), states: ALLP },
  { key: 'button-primary-small', group: 'Buttons', title: 'Primary button, page header (Invite)', snap: 'settings-members-dark', find: () => TB('Invite', M()), states: ALLP },
  { key: 'button-secondary', group: 'Buttons', title: 'Secondary button (Export CSV)', snap: 'settings-members-dark', find: () => TB('Export CSV', M()), states: ALLP },
  { key: 'button-danger', group: 'Buttons', title: 'Destructive button (Delete workspace)', desc: 'Measured at rest and on hover only; it was never clicked.', snap: 'settings-workspace-dark', find: () => TB('Delete workspace', M()), states: HF },
  { key: 'icon-button', group: 'Buttons', title: 'Icon button (Copy issue URL)', snap: 'issue-dark', find: () => Q('button[aria-label="Copy issue URL"]'), states: ALLP },
  { key: 'property-chip', group: 'Buttons', title: 'Property chip button (composer status)', snap: 'composer-dark', find: () => Q('[role=dialog] button[aria-label="Change status"]'), states: ALLP },
  // Links
  { key: 'link', group: 'Links', title: 'Inline link (Read more)', snap: 'settings-workspace-dark', find: () => Q('main a[href^="https://linear.app/docs"]'), states: ALL },
  { key: 'breadcrumb-link', group: 'Links', title: 'Breadcrumb link', snap: 'issue-dark', find: () => TB('Issues', M()), states: HV },
  // Inputs
  { key: 'text-field', group: 'Inputs', title: 'Text field (workspace name)', snap: 'settings-workspace-dark', find: () => [...document.querySelectorAll('main input:not([type]), main input[type=text]')].find((i) => !i.readOnly && i.getBoundingClientRect().width > 100) || null, states: ALL, extra: { readonly: { find: () => [...document.querySelectorAll('main input:not([type]), main input[type=text]')].find((i) => i.readOnly && i.getBoundingClientRect().width > 100) || null } } },
  { key: 'search-field', group: 'Inputs', title: 'Search field', snap: 'settings-members-dark', find: () => Q('main input[type=search]'), states: ALL },
  { key: 'text-area', group: 'Inputs', title: 'Text area (composer description)', desc: 'A ProseMirror editor, not a <textarea>; the second editor in the composer.', snap: 'composer-dark', find: () => [...document.querySelectorAll('[role=dialog] [contenteditable=true]')].filter((e) => e.getBoundingClientRect().height > 40)[0] || null, states: ['default', 'focus-visible'] },
  { key: 'select', group: 'Inputs', title: 'Select trigger (First day of the week)', snap: 'settings-prefs-dark', find: () => TB('Sunday', M()), states: ALLP, extra: { open: { snap: 'settings-prefs-dark-select', find: () => SHD(Q('[role=listbox]')) }, option: { snap: 'settings-prefs-dark-select', find: () => Q('[role=listbox] [role=option]', 2) } } },
  { key: 'checkbox', group: 'Inputs', title: 'Checkbox (members table row)', desc: 'Opacity 0 in every copy: Linear reveals the row checkbox by script on row hover or selection, which a static copy cannot replay. Geometry only.', snap: 'settings-members-dark', find: () => document.querySelector('main input[type=checkbox]'), states: R, crop: false },
  { key: 'switch', group: 'Inputs', title: 'Switch, on', desc: 'An <input type=checkbox> with appearance none.', snap: 'settings-prefs-dark', find: () => Q('main input[type=checkbox]:checked'), states: ALL, extra: { off: { find: () => Q('main input[type=checkbox]:not(:checked)'), states: ['hover'] } } },
  // Navigation
  { key: 'tab', group: 'Navigation', title: 'View tab (pill)', snap: 'issues-board-dark', find: () => TB('Active', M()), states: ALLP, extra: { selected: { find: () => TB('All issues', M()) } } },
  { key: 'nav-item', group: 'Navigation', title: 'Sidebar item', snap: 'issues-board-dark', find: () => TB('Inbox'), states: ALLP, extra: { selected: { find: () => painted([...document.querySelectorAll('a')].filter((a) => a.getBoundingClientRect().x < 60 && a.getBoundingClientRect().width > 150)) } } },
  // Overlays
  { key: 'menu', group: 'Overlays', title: 'Menu (status picker)', snap: 'issue-dark-menu', find: () => SHD(Q('[role=listbox]')), states: R, extra: { 'option-highlighted': { find: () => HL() }, option: { find: () => Q('[role=listbox] [role=option]', 4) } } },
  { key: 'tooltip', group: 'Overlays', title: 'Tooltip', snap: 'issue-dark-tooltip', find: () => { const host = [...document.body.children].filter((c) => /Copy issue URL/.test(c.textContent)).pop(); const t = host && [...host.querySelectorAll('*')].find((e) => /Copy issue URL/.test(e.textContent) && getComputedStyle(e).backgroundColor !== 'rgba(0, 0, 0, 0)'); return t || null; }, states: R },
  { key: 'dialog', group: 'Overlays', title: 'Dialog (new issue composer)', snap: 'composer-dark', find: () => BOX(Q('[role=dialog] button[type=submit]'), 600, 200), states: R },
  { key: 'dialog-scrim', group: 'Overlays', title: 'Dialog scrim', desc: 'The full-window layer behind the composer.', snap: 'composer-dark', find: () => [...document.querySelectorAll('[role=dialog], [role=dialog] *, body > div *')].find((e) => { const r = e.getBoundingClientRect(); const c = getComputedStyle(e); return r.width >= innerWidth - 1 && r.height >= innerHeight - 1 && c.backgroundColor !== 'rgba(0, 0, 0, 0)' && !e.closest('main'); }) || null, states: R, crop: false },
  { key: 'toast', group: 'Overlays', title: 'Toast', snap: 'issue-dark-toast', find: () => BOX(T('Copied issue link to clipboard'), 200, 30), states: ['default', 'hover'] },
  // Lists and tables
  { key: 'card', group: 'Lists', title: 'Board card', snap: 'issues-board-dark', find: () => Q('[data-board-item]'), states: ALL },
  { key: 'board-column-header', group: 'Lists', title: 'Board column header', snap: 'issues-board-dark', find: () => [...document.querySelectorAll('main div')].find((e) => /^Backlog\s*\d+/.test(e.textContent.trim()) && e.getBoundingClientRect().width > 200 && e.getBoundingClientRect().width < 400 && e.getBoundingClientRect().height >= 28 && e.getBoundingClientRect().height <= 60) || null, states: R },
  { key: 'list-row', group: 'Lists', title: 'List row (sub-issue)', snap: 'issue-dark', find: () => [...document.querySelectorAll('main a[href*="/issue/"]')].find((a) => a.getBoundingClientRect().height >= 30) || null, states: ALL },
  { key: 'table-row', group: 'Tables', title: 'Table row (projects)', snap: 'projects-dark', find: () => W(Q('main a[href*="/project/"]'), 1000) || Q('main a[href*="/project/"]'), states: HV },
  { key: 'table-header', group: 'Tables', title: 'Table header cell (members, sortable)', snap: 'settings-members-dark', find: () => TB('Email', M()), states: HV },
  { key: 'table-member-row', group: 'Tables', title: 'Table row (members)', snap: 'settings-members-dark', find: () => W(T('learner@example.com', M()), 1000), states: HV },
  { key: 'table-group-header', group: 'Tables', title: 'Table group header (Active)', snap: 'settings-members-dark', find: () => W(T('Active', M()), 1000), states: R },
  // Display
  { key: 'avatar', group: 'Display', title: 'Avatar (32px, members)', desc: 'Every avatar photo was replaced by a grey disc with an L in the copy; size and shape are Linear\'s, the fill is not.', snap: 'settings-members-dark', find: () => [...document.querySelectorAll('main div')].find((d) => d.textContent === 'L' && d.getBoundingClientRect().width >= 20 && d.getBoundingClientRect().width <= 40) || null, states: R, crop: false },
  { key: 'badge', group: 'Display', title: 'Badge (Admin)', snap: 'settings-members-dark', find: () => P(T('Admin', M())), states: R },
  { key: 'label-chip', group: 'Display', title: 'Label chip on a card', snap: 'issues-board-dark', find: () => [...document.querySelectorAll('[data-board-item] *')].find((e) => { const c = getComputedStyle(e); const r = e.getBoundingClientRect(); return r.height >= 18 && r.height <= 26 && r.width > 50 && parseFloat(c.borderTopLeftRadius) >= 9 && (c.borderTopStyle !== 'none' || c.backgroundColor !== 'rgba(0, 0, 0, 0)'); }) || null, states: R },
  { key: 'kbd', group: 'Display', title: 'Keyboard shortcut in a tooltip', snap: 'issue-dark-tooltip', find: () => { const host = [...document.body.children].filter((c) => /Copy issue URL/.test(c.textContent)).pop(); return host ? [...host.querySelectorAll('*')].find((e) => e.textContent.trim() === '⌘' && e.children.length === 0) : null; }, states: R, pad: 4 },
  { key: 'health-on-track', group: 'Display', title: 'Project health, On track', snap: 'projects-dark', find: () => TS('On track', M()), states: R, pad: 4 },
  { key: 'health-at-risk', group: 'Display', title: 'Project health, At risk', snap: 'projects-dark', find: () => TS('At risk', M()), states: R, pad: 4 },
  { key: 'presence-online', group: 'Display', title: 'Presence dot (Online)', snap: 'settings-members-dark', find: () => { const t = T('Online', M()); return t ? [...t.parentElement.querySelectorAll('*')].find((e) => { const r = e.getBoundingClientRect(); return r.width > 2 && r.width < 12 && getComputedStyle(e).backgroundColor !== 'rgba(0, 0, 0, 0)'; }) || null : null; }, states: R, pad: 4 },
  // Shell and type
  { key: 'app-shell-main', group: 'Shell', title: 'Main panel (inset content area)', snap: 'issues-board-dark', find: () => BOX(M(), 1000, 600) || M(), states: R, crop: false },
  { key: 'page-header', group: 'Shell', title: 'Page header bar', snap: 'issues-board-dark', find: () => H(Q('main button[aria-label="Add to favorites"]'), 40), states: R, crop: false },
  { key: 'empty-state', group: 'Shell', title: 'Empty state (My issues)', snap: 'empty-dark', find: () => TB('Create new issue', M()), states: ALL },
  { key: 'type-issue-title', group: 'Type', title: 'Issue title (detail)', snap: 'issue-dark', find: () => Q('main .ProseMirror h1, main [contenteditable] > p, main .ProseMirror'), states: R, crop: false },
  { key: 'type-heading', group: 'Type', title: 'Description heading (h2)', snap: 'issue-dark', find: () => Q('main .ProseMirror h2'), states: R, crop: false },
  { key: 'type-body', group: 'Type', title: 'Description body paragraph', snap: 'issue-dark', find: () => Q('[aria-label="Issue description"] p, main .ProseMirror + * p, main .ProseMirror p', 1), states: R, crop: false },
  { key: 'type-code', group: 'Type', title: 'Inline code', snap: 'issue-dark', find: () => Q('main .ProseMirror code'), states: R, crop: false },
  { key: 'type-page-title', group: 'Type', title: 'Settings page title', snap: 'settings-members-dark', find: () => Q('main h1') || T('Members', M()), states: R, crop: false },
  { key: 'type-section-label', group: 'Type', title: 'Sidebar section label (Workspace)', snap: 'issues-board-dark', find: () => T('Workspace'), states: R, crop: false },
  { key: 'type-caption', group: 'Type', title: 'Card meta line', snap: 'issues-board-dark', find: () => [...document.querySelectorAll('[data-board-item] span')].find((e) => /^CORE-\d+$/.test(e.textContent.trim())) || null, states: R, crop: false },
  // Phone width
  { key: 'mobile-card', group: 'Phone', title: 'Board card at 390', snap: 'mobile-issues-board-dark', find: () => Q('[data-board-item]'), states: R },
  { key: 'mobile-tab', group: 'Phone', title: 'View tab at 390', snap: 'mobile-issues-board-dark', find: () => TB('All issues', M()), states: R },
];

// ---------------------------------------------------------------- jobs

function jobsFor(spec) {
  const out = [];
  for (const st of spec.states) out.push({ state: st, base: st, snap: spec.snap, find: spec.find, hoverOn: spec.hoverOn, focusOn: spec.focusOn, prep: spec.prep });
  for (const [name, v] of Object.entries(spec.extra || {})) {
    out.push({ state: name, base: 'default', snap: v.snap || spec.snap, find: v.find, variant: true });
    for (const st of v.states || []) out.push({ state: `${name}-${st}`, base: st, snap: v.snap || spec.snap, find: v.find, variant: true });
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
    execFileSync('python3', ['-c', 'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width>1600: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)', file]);
    return path.relative(REF, file);
  };

  const theme = /-light(?=-|$)/.test(label) ? 'light' : 'dark';
  {
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
          const p = await pointOf(loc);
          await page.mouse.move(p.x, p.y, { steps: 4 });
          await page.waitForTimeout(80);
          await page.mouse.move(p.x + 0.5, p.y);
          await page.mouse.down();
          await page.waitForTimeout(250);
          via = 'mouse hover, then held down';
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
        await page.mouse.up().catch(() => {});
        await page.mouse.move(rest.x, rest.y).catch(() => {});
        await untag().catch(() => {});
      }
    }
  }
  return true;
}

// ---------------------------------------------------------------- main

const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
// Linear (adapt): every dark copy has a light twin when the page was also captured in light.
const lightOf = (label) => label.replace(/-dark(?=-|$)/, '-light');
const hasCopy = (label) => fs.existsSync(path.join(SNAPS, `${label}.json`));
const copiesOf = (snap) => [snap, ...(lightOf(snap) !== snap && hasCopy(lightOf(snap)) ? [lightOf(snap)] : [])];
const labels = [...new Set(SPECS.flatMap((s) => jobsFor(s).flatMap((j) => copiesOf(j.snap))))].filter((l) => hasCopy(l) && (!ONLY.length || ONLY.includes(l)));
out._meta = {
  read: '2026-10-17',
  source: 'Static, redacted copies of the signed-in linear.app web app (tools/capture/signed-in/snapshot.js) with every stylesheet inlined, the constructed theme sheet included, loaded from file:// in headless Chromium; fonts come from static.linear.app through a local cache. Nothing was requested from linear.app itself.',
  viewport: '1440x900 (the mobile-* copies 390x844), deviceScaleFactor 2',
  themes: 'Dark copies were taken with the account theme Dark, light copies with it set to Light (and set back afterwards). Dark states have plain names; light states are `light`, `light-<state>`. Every state records `theme` and `snapshot`.',
  states: {
    default: 'at rest, as captured',
    hover: 'real mouse hover (page.mouse.move), 450ms settle; not measured on the 390 copies',
    'focus-visible': 'real keyboard focus (focus, Shift+Tab, Tab) on the element or its first focusable descendant; recorded as skipped where the element cannot take focus',
    pressed: 'mouse hover, then the button held down for 250ms (:active)',
    other: 'selected / open / readonly / off / option-highlighted are other elements or copies captured in that state',
  },
  tokens: '`vars` lists every var(--x) named in the classes of the element and its first descendants (Linear\'s stylex classes name none, so this is usually empty; the theme variables are read by tools/capture/vars.mjs).',
  snapshots: { ...(out._meta && out._meta.snapshots), ...Object.fromEntries(labels.map((l) => { const m = metaOf(l); return [l, { url: m.url, w: m.w, h: m.h }]; })) },
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
    for (const copy of copiesOf(job.snap)) {
      if (!labels.includes(copy)) continue;
      if (!RESET.has(copy)) RESET.set(copy, []);
      RESET.get(copy).push([c, /-light(?=-|$)/.test(copy) ? (job.state === 'default' ? 'light' : `light-${job.state}`) : job.state]);
      if (!bySnap.has(copy)) bySnap.set(copy, []);
      bySnap.get(copy).push({ spec, job });
    }
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
