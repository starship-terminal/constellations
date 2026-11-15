// Motion readings, shared by motion-probe.mjs and the tests (docs/decisions/0001-motion-tokens.md).
//
// Two halves. The pure half normalises what a browser reports (durations to milliseconds, easings to
// one spelling, the comma lists of transition-* and animation-* zipped into one record each) and
// diffs a normal read against a prefers-reduced-motion read. It needs no browser, so
// tools/kit/capture/test_motion.mjs runs it directly. The page half (readMotionInPage,
// readSheetsInPage) is passed to page.evaluate, so each is self-contained and carries its own noUrl.
//
// Everything is read from computed styles and the stylesheets' own rules, never from a screenshot.
// A custom property or an animation name can hold a url() with a signed or per-account query, so every
// string leaves the page through noUrl, as in vars.mjs.

// A url() in a value is recorded as url(…) (data: and #fragment references stay). Same text as the
// kit's vars.mjs: tools/test_kit_motion.py checks every copy in this file against it.
export const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);

// A duration at or under this is no motion at all: the common reset is `animation-duration: 0.01ms`,
// which exists so animationend still fires.
export const NEGLIGIBLE_MS = 1;

// Computed properties read from every element (and its ::before and ::after).
export const MOTION_PROPS = [
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction', 'transitionDelay',
  'animationName', 'animationDuration', 'animationTimingFunction', 'animationDelay',
  'animationIterationCount', 'animationDirection', 'animationFillMode', 'animationPlayState',
  'scrollBehavior',
];

// A custom property is motion when its name says so or its value is a time or an easing.
export const MOTION_VAR_NAME = '(?:^|-)(?:dur|duration|ease|easing|motion|transition|animation|anim|spring|delay|timing|speed|curve|stagger)(?:-|$)';
export const MOTION_VAR_VALUE = '^(?:[-+]?(?:\\d+\\.?\\d*|\\.\\d+)(?:e[-+]?\\d+)?m?s|cubic-bezier\\(.*\\)|steps\\(.*\\)|linear\\(.*\\)|ease|ease-in|ease-out|ease-in-out|step-start|step-end)$';

// ---------------------------------------------------------------- parsing

// "a, b(c, d), e" -> ["a", "b(c, d)", "e"]: a comma inside parentheses or quotes does not split.
export function splitList(s) {
  const out = [];
  let depth = 0, quote = '', cur = '';
  for (const ch of String(s ?? '')) {
    if (quote) { cur += ch; if (ch === quote) quote = ''; continue; }
    if (ch === '"' || ch === "'") { quote = ch; cur += ch; continue; }
    if (ch === '(') depth++;
    if (ch === ')') depth = Math.max(0, depth - 1);
    if (ch === ',' && depth === 0) { out.push(cur.trim()); cur = ''; continue; }
    cur += ch;
  }
  if (cur.trim() || out.length) out.push(cur.trim());
  return out.filter((x) => x !== '');
}

// "0.2s" -> 200, "150ms" -> 150, "0s" -> 0; anything else (var(), calc(), a bad value) -> null.
export function parseTime(s) {
  const m = String(s ?? '').trim().toLowerCase().match(/^([-+]?(?:\d+\.?\d*|\.\d+)(?:e[-+]?\d+)?)(ms|s)$/);
  if (!m) return null;
  const n = parseFloat(m[1]) * (m[2] === 's' ? 1000 : 1);
  return Math.round(n * 1000) / 1000;
}

const num = (x) => String(Math.round(parseFloat(x) * 10000) / 10000);
const KEYWORDS = new Set(['linear', 'ease', 'ease-in', 'ease-out', 'ease-in-out']);

// One spelling per easing: lower case, single spaces, cubic-bezier(a, b, c, d) with trimmed numbers,
// steps(n, jump) with its default spelled out, step-start/step-end as steps(1, ...). A linear() spring
// and anything unparsed keep their text, collapsed.
export function normEasing(s) {
  const t = String(s ?? '').trim().toLowerCase().replace(/\s+/g, ' ');
  if (!t) return '';
  if (KEYWORDS.has(t)) return t;
  if (t === 'step-start') return 'steps(1, start)';
  if (t === 'step-end') return 'steps(1, end)';
  let m = t.match(/^cubic-bezier\(\s*([^)]*)\)$/);
  if (m) {
    const p = m[1].split(',').map((x) => x.trim());
    if (p.length === 4 && p.every((x) => /^[-+]?(?:\d+\.?\d*|\.\d+)(?:e[-+]?\d+)?$/.test(x))) return `cubic-bezier(${p.map(num).join(', ')})`;
    return t.replace(/\s*,\s*/g, ', ');
  }
  m = t.match(/^steps\(\s*(\d+)\s*(?:,\s*([a-z-]+)\s*)?\)$/);
  if (m) return `steps(${m[1]}, ${({ 'jump-end': 'end', 'jump-start': 'start' })[m[2]] || m[2] || 'end'})`;
  return t.replace(/\s*,\s*/g, ', ');
}

// The four control points of a cubic-bezier() or of a keyword easing, else null (steps, linear()).
export function easingBezier(s) {
  const t = normEasing(s);
  const table = { linear: [0, 0, 1, 1], ease: [0.25, 0.1, 0.25, 1], 'ease-in': [0.42, 0, 1, 1], 'ease-out': [0, 0, 0.58, 1], 'ease-in-out': [0.42, 0, 0.58, 1] };
  if (table[t]) return table[t];
  const m = t.match(/^cubic-bezier\(([^)]*)\)$/);
  if (!m) return null;
  const p = m[1].split(',').map((x) => parseFloat(x));
  return p.length === 4 && p.every(Number.isFinite) ? p : null;
}

// Kinds of value a custom property can hold, for sorting motion variables into duration and easing.
export function classifyMotionValue(v) {
  const t = String(v ?? '').trim();
  if (parseTime(t) !== null) return 'duration';
  const e = normEasing(t);
  if (KEYWORDS.has(e) || /^(cubic-bezier|steps|linear)\(/.test(e)) return 'easing';
  return 'other';
}

export const isMotionVar = (name, value) => new RegExp(MOTION_VAR_NAME, 'i').test(String(name).replace(/^--/, '')) || new RegExp(MOTION_VAR_VALUE, 'i').test(String(value ?? '').trim());

// Longhand lists repeat to the length of the property list (CSS Transitions 1, "the transition-property
// list determines the number of transitions"; animations count by animation-name).
const at = (list, i, dflt) => (list.length ? list[i % list.length] : dflt);

// The transitions a computed style would run: one per property, with duration and delay in ms and the
// normalised easing. A property of `none`, and a transition with neither duration nor delay, is no
// motion. A duration that is not a plain time (var() left unresolved) is kept as durationRaw.
export function transitionsOf(style) {
  const props = splitList(style.transitionProperty);
  const dur = splitList(style.transitionDuration), ease = splitList(style.transitionTimingFunction), delay = splitList(style.transitionDelay);
  const out = [];
  props.forEach((property, i) => {
    if (property.toLowerCase() === 'none') return;
    const d = parseTime(at(dur, i, '0s')), dl = parseTime(at(delay, i, '0s'));
    const rec = { property, durationMs: d ?? 0, delayMs: dl ?? 0, easing: normEasing(at(ease, i, 'ease')) };
    if (d === null) rec.durationRaw = at(dur, i, '');
    if (!(rec.durationMs > 0 || rec.delayMs > 0 || d === null)) return;
    out.push(rec);
  });
  return out;
}

// The animations a computed style would run, one per animation-name that is not `none`.
export function animationsOf(style) {
  const names = splitList(style.animationName);
  const dur = splitList(style.animationDuration), ease = splitList(style.animationTimingFunction), delay = splitList(style.animationDelay);
  const iter = splitList(style.animationIterationCount), dir = splitList(style.animationDirection), fill = splitList(style.animationFillMode), play = splitList(style.animationPlayState);
  const out = [];
  names.forEach((name, i) => {
    if (name.toLowerCase() === 'none') return;
    const d = parseTime(at(dur, i, '0s'));
    const rec = {
      name, durationMs: d ?? 0, delayMs: parseTime(at(delay, i, '0s')) ?? 0, easing: normEasing(at(ease, i, 'ease')),
      iterationCount: at(iter, i, '1'), direction: at(dir, i, 'normal'), fillMode: at(fill, i, 'none'), playState: at(play, i, 'running'),
    };
    if (d === null) rec.durationRaw = at(dur, i, '');
    out.push(rec);
  });
  return out;
}

// One element's motion, normalised: its transitions, animations and smooth scrolling.
export function motionOf(style) {
  const m = { transitions: transitionsOf(style), animations: animationsOf(style) };
  if (String(style.scrollBehavior || '').trim() === 'smooth') m.scrollBehavior = 'smooth';
  return m;
}

export const hasMotion = (m) => !!(m && (m.transitions.length || m.animations.length || m.scrollBehavior));

// ---------------------------------------------------------------- diff

const classify = (baseMs, reducedMs) => {
  if (reducedMs === null || reducedMs <= NEGLIGIBLE_MS) return 'removed';
  if (reducedMs < baseMs) return 'shortened';
  if (reducedMs === baseMs) return 'kept';
  return 'increased';
};

// An animation paused under reduce is stopped, whatever its duration says.
const stopped = (a) => a.playState === 'paused';

// What prefers-reduced-motion: reduce did to one element's motion. Items are matched by property
// (transitions) or name (animations). Each is removed, shortened (both are reductions), kept, changed (the
// same length with another easing or delay), increased (longer) or added (not there before). An animation
// that still runs forever after reduce, replacements included, is flagged `loops`. The element's outcome:
// none (no motion either way); removed or reduced (every item is a reduction); kept (nothing was
// reduced, nothing got worse); increased (nothing was reduced and something grew or was added); partial
// (some reduced, some not). Only a real reduction counts: more motion is never "reduced".
export function diffMotion(base, reduced) {
  const items = [];
  const reducedT = new Map((reduced?.transitions || []).map((t) => [t.property, t]));
  const reducedA = new Map((reduced?.animations || []).map((a) => [a.name, a]));
  for (const t of base?.transitions || []) {
    const r = reducedT.get(t.property);
    let outcome = r ? classify(t.durationMs, r.durationMs) : 'removed';
    if (outcome === 'kept' && (r.easing !== t.easing || r.delayMs !== t.delayMs)) outcome = 'changed';
    items.push({ kind: 'transition', key: t.property, outcome, from: t.durationMs, to: r ? r.durationMs : 0 });
    reducedT.delete(t.property);
  }
  for (const a of base?.animations || []) {
    const r = reducedA.get(a.name);
    let outcome = !r || stopped(r) ? 'removed' : classify(a.durationMs, r.durationMs);
    if (outcome === 'kept' && (r.easing !== a.easing || r.delayMs !== a.delayMs || r.iterationCount !== a.iterationCount)) outcome = 'changed';
    const item = { kind: 'animation', key: a.name, outcome, from: a.durationMs, to: r && !stopped(r) ? r.durationMs : 0 };
    if (r && !stopped(r) && r.iterationCount === 'infinite' && outcome !== 'removed') item.loops = true;
    items.push(item);
    reducedA.delete(a.name);
  }
  if (base?.scrollBehavior) items.push({ kind: 'scroll', key: 'scroll-behavior', outcome: reduced?.scrollBehavior ? 'kept' : 'removed' });
  else if (reduced?.scrollBehavior) items.push({ kind: 'scroll', key: 'scroll-behavior', outcome: 'added' });
  for (const t of reducedT.values()) items.push({ kind: 'transition', key: t.property, outcome: 'added', from: 0, to: t.durationMs });
  for (const a of reducedA.values()) {
    const item = { kind: 'animation', key: a.name, outcome: 'added', from: 0, to: a.durationMs };
    if (!stopped(a) && a.iterationCount === 'infinite') item.loops = true;
    items.push(item);
  }
  const REDUCING = new Set(['removed', 'shortened']);
  const hadMotion = hasMotion(base);
  const reducing = items.filter((i) => REDUCING.has(i.outcome)).length;
  let outcome;
  if (!items.length) outcome = 'none';
  else if (!hadMotion) outcome = 'added';
  else if (reducing === items.length) outcome = items.every((i) => i.outcome === 'removed') ? 'removed' : 'reduced';
  else if (reducing) outcome = 'partial';
  else outcome = items.some((i) => i.outcome === 'increased' || i.outcome === 'added') ? 'increased' : 'kept';
  return { outcome, items };
}

// ---------------------------------------------------------------- grouping and summary

// Elements with the same motion before and after share one group: records is
// [{ node, base: motionOf, reduced: motionOf }]. Groups are sorted by count, then by key, so the same
// reading writes the same bytes. Each keeps up to three example nodes, never an account's own text.
export function groupRecords(records, examples = 3) {
  const groups = new Map();
  for (const r of records) {
    const d = diffMotion(r.base, r.reduced);
    if (d.outcome === 'none') continue;
    const key = JSON.stringify([r.base, r.reduced]);
    const g = groups.get(key) || { base: r.base, reduced: r.reduced, outcome: d.outcome, items: d.items, count: 0, nodes: [] };
    g.count++;
    if (g.nodes.length < examples && !g.nodes.includes(r.node)) g.nodes.push(r.node);
    groups.set(key, g);
  }
  return [...groups.entries()].sort((a, b) => b[1].count - a[1].count || (a[0] < b[0] ? -1 : 1)).map(([, g]) => g);
}

// Counts per outcome and the page's overall behaviour under reduce: no-motion, honours (every moving
// element is removed or reduced; more motion never counts), ignores (every one is kept) or partial. `loops` names the animations
// that keep looping, the case reduced motion exists for.
export function summarise(groups) {
  const counts = { removed: 0, reduced: 0, kept: 0, partial: 0, increased: 0, added: 0 };
  const loops = new Set();
  let moving = 0;
  for (const g of groups) {
    counts[g.outcome] = (counts[g.outcome] || 0) + g.count;
    if (g.outcome !== 'added') moving += g.count;
    for (const i of g.items) if (i.loops) loops.add(i.key);
  }
  let behaviour;
  if (!moving) behaviour = 'no-motion';
  else if (!counts.kept && !counts.partial && !counts.increased) behaviour = 'honours';
  else if (counts.kept === moving) behaviour = 'ignores';
  else behaviour = 'partial';
  return { moving, ...counts, behaviour, loops: [...loops].sort() };
}

// Several pages' summaries into one. Behaviour follows the combined counts.
export function mergeSummaries(list) {
  const total = { moving: 0, removed: 0, reduced: 0, kept: 0, partial: 0, increased: 0, added: 0 };
  const loops = new Set();
  for (const s of list) {
    for (const k of Object.keys(total)) total[k] += s[k] || 0;
    for (const l of s.loops || []) loops.add(l);
  }
  const behaviour = !total.moving ? 'no-motion' : !total.kept && !total.partial && !total.increased ? 'honours' : total.kept === total.moving ? 'ignores' : 'partial';
  return { ...total, behaviour, loops: [...loops].sort() };
}

// A rule's longhand strings (read from a stylesheet, not computed) as records: the declared motion,
// including :hover and state rules a computed read at rest does not see. Only what the rule authors is
// recorded: no `ease` or `0s` is filled in, and a rule that sets only a duration list
// (`.btn:hover { transition-duration: .4s, .6s }`) gives one record per entry, its property written
// `(base #n)` because the base rule names it. A value still holding var() cannot be normalised and is
// flagged viaVar.
export function declaredOf(rule) {
  const list = (v) => splitList(v);
  const out = { selector: rule.selector, context: rule.context, transitions: [], animations: [] };
  const authored = [rule.transitionProperty, rule.transitionDuration, rule.transitionTimingFunction, rule.transitionDelay,
    rule.animationName, rule.animationDuration, rule.animationTimingFunction, rule.animationDelay, rule.animationIterationCount,
    rule.animationDirection, rule.animationFillMode, rule.animationPlayState];
  const fields = (src, keys) => Object.fromEntries(Object.entries(keys).map(([k, v]) => [k, list(src[v])]).filter(([, l]) => l.length));
  const t = fields(rule, { property: 'transitionProperty', duration: 'transitionDuration', easing: 'transitionTimingFunction', delay: 'transitionDelay' });
  const tn = Math.max(0, ...Object.values(t).map((l) => l.length));
  for (let i = 0; i < tn; i++) {
    const property = t.property ? at(t.property, i, '') : `(base #${i})`;
    if (property.toLowerCase() === 'none') continue;
    const rec = { property };
    if (t.duration) { const d = parseTime(at(t.duration, i, '')); if (d === null) rec.durationRaw = at(t.duration, i, ''); else rec.durationMs = d; }
    if (t.delay) { const d = parseTime(at(t.delay, i, '')); if (d !== null) rec.delayMs = d; }
    if (t.easing) rec.easing = normEasing(at(t.easing, i, ''));
    out.transitions.push(rec);
  }
  const a = fields(rule, { name: 'animationName', duration: 'animationDuration', easing: 'animationTimingFunction', delay: 'animationDelay', iterationCount: 'animationIterationCount', direction: 'animationDirection', fillMode: 'animationFillMode', playState: 'animationPlayState' });
  const an = Math.max(0, ...Object.values(a).map((l) => l.length));
  for (let i = 0; i < an; i++) {
    const name = a.name ? at(a.name, i, '') : `(base #${i})`;
    if (name.toLowerCase() === 'none') continue;
    const rec = { name };
    if (a.duration) { const d = parseTime(at(a.duration, i, '')); if (d === null) rec.durationRaw = at(a.duration, i, ''); else rec.durationMs = d; }
    if (a.delay) { const d = parseTime(at(a.delay, i, '')); if (d !== null) rec.delayMs = d; }
    if (a.easing) rec.easing = normEasing(at(a.easing, i, ''));
    for (const k of ['iterationCount', 'direction', 'fillMode', 'playState']) if (a[k]) rec[k] = at(a[k], i, '');
    out.animations.push(rec);
  }
  if (String(rule.scrollBehavior || '').trim() === 'smooth') out.scrollBehavior = 'smooth';
  if (authored.some((v) => /var\(/.test(String(v ?? '')))) out.viaVar = true;
  return out;
}

// ---------------------------------------------------------------- in the page

// Runs in the page. Reads every element's motion properties, keeping those with motion in this pass or
// recorded in an earlier one (window.__motion remembers each element's id), so the reduced pass reads
// the same elements as the normal one. Returns { matches, scanned, records }; `matches` is
// matchMedia('(prefers-reduced-motion: reduce)').matches, which proves the emulation took. SVG
// descendants are read too: a spinner's circle can animate while its svg does not. `dropped` counts moving
// elements left out because the cap was reached.
export function readMotionInPage({ props, cap, pseudos }) {
  // A url() in a computed value can be a signed URL: recorded as url(…), only data: and #fragment kept.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const strip = (c) => String(c).replace(/__[A-Za-z0-9_-]{5,6}$/, '');
  const describe = (el) => {
    const cls = typeof el.className === 'string' ? el.className.split(/\s+/).filter((c) => c && !c.includes('[') && !c.includes(':') && !/^x[0-9a-z]{5,8}$/.test(strip(c))).slice(0, 3).map((c) => '.' + strip(c)).join('') : '';
    const role = el.getAttribute('role');
    return el.tagName.toLowerCase() + (role ? `[role=${role}]` : '') + cls;
  };
  const pick = (cs) => {
    const o = {};
    for (const p of props) o[p] = noUrl(cs[p]);
    return o;
  };
  // A coarse prefilter; motionOf in Node is the exact test.
  const moving = (cs) => (cs.transitionProperty !== 'none' && /[1-9]/.test(cs.transitionDuration + cs.transitionDelay)) || cs.animationName !== 'none' || cs.scrollBehavior === 'smooth';
  const memo = (window.__motion ||= { ids: new Map(), next: 0 });
  const records = [];
  let scanned = 0, dropped = 0;
  for (const el of document.querySelectorAll('*')) {
    scanned++;
    for (const pe of [null, ...pseudos]) {
      const cs = getComputedStyle(el, pe);
      if (pe && (cs.content === 'none' || cs.content === 'normal')) continue;
      const known = memo.ids.get(el);
      let id = known ? known[pe || ''] : undefined;
      // An element the normal pass recorded is always read again, so a cap cannot make the reduced pass
      // compare it with nothing; a new one only while there is room.
      if (id === undefined) {
        if (!moving(cs)) continue;
        if (records.length >= cap) { dropped++; continue; }
        id = memo.next++;
        memo.ids.set(el, { ...(known || {}), [pe || '']: id });
      }
      records.push({ id, node: describe(el) + (pe || ''), style: pick(cs) });
    }
  }
  return { matches: matchMedia('(prefers-reduced-motion: reduce)').matches, scanned, dropped, records };
}

// Runs in the page. Reads what the stylesheets declare: every @keyframes (its name and the properties
// each step sets), every rule under a prefers-reduced-motion media query, the transitions and
// animations each rule declares (so :hover and state rules show, which a computed read at rest cannot),
// and the custom properties that look like motion, declared and resolved on the root. A sheet from
// another origin cannot be read and is counted.
export function readSheetsInPage({ varName, varValue, cap }) {
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const nameRe = new RegExp(varName, 'i'), valueRe = new RegExp(varValue, 'i');
  // A selector or a condition can hold a URL with a query too (an img[src] attribute selector).
  // (no url() in that form, so a quoted value holding a URL or a query string is replaced whole)
  const clean = (s) => noUrl(String(s || '').replace(/__[A-Za-z0-9_-]{5,6}/g, ''))
    .replace(/(["'])(?:(?!\1).)*(?:\/\/|[?&][^=\s"']+=)(?:(?!\1).)*\1/g, '"<url>"')
    .replace(/=\s*(?:https?:)?\/\/[^\]\s]+/g, '=<url>')
    .slice(0, 200);
  const keyframes = [], reducedRules = [], declared = [], vars = new Map();
  const truncated = { declared: false, reducedRules: false, customProperties: false };
  let unreadable = 0;
  const seen = new Set();
  const LONG = ['transition-property', 'transition-duration', 'transition-timing-function', 'transition-delay', 'animation-name', 'animation-duration', 'animation-timing-function', 'animation-delay', 'animation-iteration-count', 'animation-direction', 'animation-fill-mode', 'animation-play-state'];
  const camel = (p) => p.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
  const REDUCE = /prefers-reduced-motion/;
  const walk = (rules, ctx) => {
    for (const r of rules) {
      if (r instanceof CSSKeyframesRule) {
        const steps = [...r.cssRules].map((k) => ({ offset: k.keyText, properties: [...k.style].filter((p) => !p.startsWith('--')).sort() }));
        keyframes.push({ name: noUrl(r.name), steps, properties: [...new Set(steps.flatMap((s) => s.properties))].sort() });
        continue;
      }
      if (r instanceof CSSImportRule) {
        // an @import is its own sheet, under the import's media condition
        const sheet = r.styleSheet, m = r.media && r.media.mediaText;
        if (!sheet || seen.has(sheet)) continue;
        seen.add(sheet);
        try { walk(sheet.cssRules, m && m !== 'all' ? [...ctx, '@media ' + m] : ctx); } catch { unreadable++; }
        continue;
      }
      if (r.cssRules && !r.style) {
        const head = r instanceof CSSMediaRule ? '@media ' + r.media.mediaText : r instanceof CSSSupportsRule ? '@supports ' + r.conditionText : r.cssText.split('{')[0].trim();
        walk(r.cssRules, [...ctx, head]);
        continue;
      }
      if (!r.style) continue;
      const selector = clean(r.selectorText);
      const context = ctx.map(clean);
      const rule = { selector, context };
      let any = false;
      for (const p of LONG) { const v = r.style.getPropertyValue(p).trim(); if (v) { rule[camel(p)] = noUrl(v); any = true; } }
      const sb = r.style.getPropertyValue('scroll-behavior').trim();
      if (sb) { rule.scrollBehavior = noUrl(sb); any = true; }
      if (any) { if (declared.length < cap) declared.push(rule); else truncated.declared = true; }
      // every rule under a prefers-reduced-motion query, `reduce` and `no-preference` alike (the media text says which)
      if (context.some((c) => REDUCE.test(c))) {
        if (reducedRules.length < cap) {
          const decls = {};
          for (let i = 0; i < r.style.length; i++) { const k = r.style[i]; decls[k] = noUrl(r.style.getPropertyValue(k).trim()) + (r.style.getPropertyPriority(k) ? ' !important' : ''); }
          reducedRules.push({ media: context.filter((c) => REDUCE.test(c)).join(' '), selector, declarations: decls });
        } else truncated.reducedRules = true;
      }
      for (let i = 0; i < r.style.length; i++) {
        const k = r.style[i];
        if (!k || !k.startsWith('--')) continue;
        const v = noUrl(r.style.getPropertyValue(k).trim());
        if ((nameRe.test(k.slice(2)) || valueRe.test(v)) && !vars.has(k)) vars.set(k, { name: k, declared: v, selector });
      }
      if (r.cssRules && r.cssRules.length) walk(r.cssRules, [...ctx, r.selectorText]);
    }
  };
  for (const ss of document.styleSheets) {
    if (seen.has(ss)) continue;
    seen.add(ss);
    // the sheet's own media condition (<style media="(prefers-reduced-motion: reduce)">) starts the context
    const m = ss.media && ss.media.mediaText;
    try { walk(ss.cssRules, m && m !== 'all' ? ['@media ' + m] : []); } catch { unreadable++; }
  }
  const rootStyle = getComputedStyle(document.documentElement);
  const all = [...vars.values()].sort((a, b) => (a.name < b.name ? -1 : 1));
  truncated.customProperties = all.length > cap;
  const customProperties = all.slice(0, cap).map((v) => ({ ...v, resolved: noUrl(rootStyle.getPropertyValue(v.name).trim()) }));
  return { keyframes, reducedRules, declared, customProperties, unreadable, truncated };
}
