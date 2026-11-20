// Writes raw/measurements.md from raw/components-computed.json: every component, every state, every
// property the measurement kept, as one table per component. Deterministic; no network.
//
//   node build-measurements.mjs
import fs from 'node:fs';
import path from 'node:path';
import { hex } from '../css-colour.mjs';

const REF = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..', '..');
const J = JSON.parse(fs.readFileSync(path.join(REF, 'raw', 'components-computed.json'), 'utf8'));

const sides = (t, r, b, l) => (t === r && r === b && b === l ? t : t === b && r === l ? `${t} ${r}` : `${t} ${r} ${b} ${l}`);
const fam = (f) => (f || '').split(',')[0].replace(/"/g, '');
const esc = (s) => String(s ?? '').replace(/\|/g, '/').replace(/\n/g, ' ');

// A state whose reading is not what its name says, kept out of the tables and the crop list (the
// same rule as focus_not_captured in tools/build_components_md.py): a skipped one, or a focus-visible
// reading taken where keyboard focus never landed (older runs saved the element at rest) or where the
// element took focus without matching :focus-visible.
// This package also marks some failed focus states with HAND_RELABELLED_FOCUS (below): their via
// was rewritten by hand after the run, not re-measured, so they count as not captured too.
const focusNotCaptured = (v) => Boolean(v.skipped) || v.via === 'focus failed' || v.via === HAND_RELABELLED_FOCUS || v.focus?.matches === false;
const notCapturedWhy = (v) => v.skipped || (v.via === 'focus failed' ? 'focus failed: keyboard focus did not reach the element' : v.via === HAND_RELABELLED_FOCUS ? 'focus failed when captured; the via was later rewritten by hand, not re-measured' : 'focused without matching :focus-visible, so no keyboard-focus reading');

function props(v) {
  const s = v.style || {};
  const o = {};
  o['Size (w x h)'] = `${v.rect.w} x ${v.rect.h}`;
  o.Padding = sides(s.paddingTop, s.paddingRight, s.paddingBottom, s.paddingLeft);
  if (s.gap && s.gap !== 'normal') o.Gap = s.gap;
  const bd = ['Top', 'Right', 'Bottom', 'Left'].map((d) => (parseFloat(s[`border${d}Width`]) > 0 && s[`border${d}Style`] !== 'none' ? `${s[`border${d}Width`]} ${s[`border${d}Style`]} ${hex(s[`border${d}Color`])}` : 'none'));
  o.Border = bd.every((x) => x === bd[0]) ? bd[0] : bd.map((x, i) => `${'TRBL'[i]}: ${x}`).join('; ');
  o.Radius = sides(s.borderTopLeftRadius, s.borderTopRightRadius, s.borderBottomRightRadius, s.borderBottomLeftRadius);
  o.Background = hex(s.backgroundColor) === '#000000 @ 0' ? 'transparent' : hex(s.backgroundColor);
  if (s.backgroundImage && s.backgroundImage !== 'none') o['Background image'] = hex(s.backgroundImage.replace(/url\("data:[^)]*\)/g, 'url(data:…)')).slice(0, 220);
  o['Box shadow'] = s.boxShadow === 'none' ? 'none' : hex(s.boxShadow);
  if (s.backdropFilter && s.backdropFilter !== 'none') o['Backdrop filter'] = s.backdropFilter;
  o.Outline = s.outlineStyle === 'none' || parseFloat(s.outlineWidth) === 0 ? 'none' : `${s.outlineWidth} ${s.outlineStyle} ${hex(s.outlineColor)} offset ${s.outlineOffset}`;
  o.Font = `${fam(s.fontFamily)} ${s.fontSize}/${s.lineHeight} ${s.fontWeight}`;
  o['Letter spacing'] = s.letterSpacing;
  o.Colour = hex(s.color);
  if (v.textStyle) o['Text node'] = `${v.textStyle.node}: ${fam(v.textStyle.fontFamily)} ${v.textStyle.fontSize}/${v.textStyle.lineHeight} ${v.textStyle.fontWeight}, ${hex(v.textStyle.color)}${v.textStyle.letterSpacing !== 'normal' ? ', ls ' + v.textStyle.letterSpacing : ''}`;
  o.Transition = s.transitionDuration === '0s' || !s.transitionDuration ? 'none' : `${s.transitionProperty} ${s.transitionDuration} ${s.transitionTimingFunction}${s.transitionDelay !== '0s' ? ' delay ' + s.transitionDelay : ''}`;
  if (s.transform && s.transform !== 'none') o.Transform = s.transform;
  if (s.opacity !== '1') o.Opacity = s.opacity;
  if (s.cursor && s.cursor !== 'auto') o.Cursor = s.cursor;
  if (v.icon) o.Icon = `${v.icon.w} x ${v.icon.h}, colour ${hex(v.icon.color)}${v.icon.fill && v.icon.fill !== 'none' && hex(v.icon.fill) !== hex(v.icon.color) ? ', fill ' + hex(v.icon.fill) : ''}`;
  if (v.placeholder) o.Placeholder = `${hex(v.placeholder.color)}, opacity ${v.placeholder.opacity}`;
  for (const pe of ['::before', '::after']) if (v[pe]) o[pe] = `${v[pe].width} x ${v[pe].height}, ${v[pe].position}, bg ${hex(v[pe].backgroundColor)}${v[pe].backgroundImage && v[pe].backgroundImage !== 'none' ? ' ' + hex(v[pe].backgroundImage).slice(0, 120) : ''}, radius ${v[pe].borderRadius}${v[pe].boxShadow !== 'none' ? ', shadow ' + hex(v[pe].boxShadow) : ''}`;
  if (v.paint) o['Painted layers'] = v.paint.slice(0, 6).map((p) => [p.node, p.size, p.bg && 'bg ' + hex(p.bg), p.bgImage && 'image ' + hex(p.bgImage).slice(0, 90), p.border && 'border ' + hex(p.border), p.radius && 'r ' + p.radius, p.shadow && 'shadow ' + hex(p.shadow), p.outline && 'outline ' + hex(p.outline)].filter(Boolean).join(' ')).join('; ');
  if (v.ancestors) o['Ancestor paint'] = v.ancestors.map((a) => `${a.up} up ${a.node}${a.bg !== 'rgba(0, 0, 0, 0)' ? ' bg ' + hex(a.bg) : ''}${a.shadow ? ' shadow ' + hex(a.shadow) : ''}${a.outline ? ' outline ' + hex(a.outline) : ''}`).join('; ');
  o['How'] = v.via || '';
  return o;
}

const HAND_RELABELLED_FOCUS = 'el.focus() — a real ring painted; document.activeElement read the shadow host (check fixed in kbFocus)';
const L = [];
const W = (s = '') => L.push(s);
W('# Component measurements'); // PRODUCT (adapt): the product's name
W('');
W(`Computed styles read from www.dopper.com and shop.dopper.com on ${J._meta.read} by \`tools/capture/public/measure.mjs\`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the marketing home, /en/mission/story, /en/products/insulated, /en/blog/just-refill and the storefront's /, /bottles, /dopper-original-pacific-blue, /checkout/cart/ and /customer/account/login/ — with the Cookiebot consent dialog hidden (never answered) — and written here by \`tools/capture/public/build-measurements.mjs\` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads \`=\`. Colours are hex, with \`@ alpha\` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.`);
W('');
W('States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.');
W('');
W('## Components');
const groups = [];
for (const c of Object.values(J.components)) { if (!groups.includes(c.group)) groups.push(c.group); }
for (const g of groups) {
  W('');
  W(`### ${g}`);
  for (const [k, c] of Object.entries(J.components).filter(([, c]) => c.group === g)) {
    W('');
    W(`#### ${k}`);
    W('');
    W(`${c.title}.${c.desc ? ' ' + c.desc : ''}`);
    W('');
    const states = Object.keys(c.states);
    W(`Page: ${c.page}. Selector: \`${esc(c.selector)}\`. States: ${states.join(', ')}.`);
    W('');
    if (c.missing) { W('Not found on the page at capture time.'); continue; }
    const rows = {};
    for (const st of states) {
      const v = c.states[st];
      if (v.error) { rows.Error = rows.Error || {}; rows.Error[st] = v.error; continue; }
      // a focus-visible state where keyboard focus never landed: older runs saved the element at rest
      // three focus states the run recorded as focus failed; their via was rewritten by hand afterwards, not re-measured
      if (focusNotCaptured(v)) { (rows.Skipped ||= {})[st] = notCapturedWhy(v); continue; }
      if (!v.style || !v.rect) { // a note entry (e.g. pdp_url) carries no computed style
        (rows.Note ||= {})[st] = v.text || v.via || '';
        continue;
      }
      for (const [p, val] of Object.entries(props(v))) (rows[p] ||= {})[st] = val;
    }
    W(`| Property | ${states.join(' | ')} |`);
    W(`|---|${states.map(() => '---').join('|')}|`);
    for (const [p, vals] of Object.entries(rows)) {
      const first = vals[states[0]];
      W(`| ${p} | ${states.map((st, i) => (i && vals[st] === first && p !== 'How' ? '=' : esc(vals[st] ?? '-'))).join(' | ')} |`);
    }
    const crops = states.filter((st) => !focusNotCaptured(c.states[st])).map((st) => c.states[st].crop).filter(Boolean).map((f) => '`' + path.basename(f) + '`');
    W('');
    W(crops.length ? `Crops: ${crops.join(', ')}.` : 'Crops: none.');
  }
}
if (J._meta.backdrop) {
  W('');
  W('## Dialog backdrop');
  W('');
  W('The layers behind the login dialog that paint a fill, from the dialog outwards. The first is the overlay that dims the page.');
  W('');
  for (const b of J._meta.backdrop) W(`- \`${b.node || 'overlay (hashed class names only)'}\`:${hex(b.bg)}${b.backdrop && b.backdrop !== 'none' ? ', backdrop-filter ' + b.backdrop : ''}`);
}
W('');
W('## Transitions declared in the readable stylesheets');
W('');
W('www.dopper.com\'s Next.js bundles compile every class to a build hash (the names in the Selector rows are the spec\'s own description, not class names), and shop.dopper.com serves Magento\'s compiled stylesheets; this list covers the transition rules the readable stylesheets on each host expose, and the per-state Transition rows above are the computed values the page paints.');
for (const [pg, list] of Object.entries(J._meta.sheets || {}).sort()) {
  const uniq = [...new Map(list.filter((t) => t.transition).map((t) => [t.transition, t])).values()].slice(0, 12);
  W('');
  W(`- ${pg}: ${uniq.map((t) => `\`${esc(t.transition)}\``).join(', ') || 'none'}`);
}
fs.writeFileSync(path.join(REF, 'raw', 'measurements.md'), L.join('\n') + '\n');
console.log('raw/measurements.md', L.length, 'lines');
