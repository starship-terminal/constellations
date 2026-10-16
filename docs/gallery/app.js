// Design systems catalog. Reads data.json (written by tools/catalog.py) and renders
// an index of packages and a detail page per package. Hash routes:
//   #/                       index
//   #/<slug>[/<tab>]         detail, tab = screens | components | docs
//   #/<slug>/docs/<path>     detail with a markdown file open
'use strict';

const app = document.getElementById('app');
const qInput = document.getElementById('q');
const UP = '../'; // data paths are relative to the docs site's root; this page lives in gallery/
const PAGE = 60;

let DATA = null;
const state = { q: '', cat: 'all', dark: false, platform: 'all', view: 'grid' };
try { Object.assign(state, JSON.parse(localStorage.getItem('ds-index') || '{}'), { q: '' }); } catch (e) {}

const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const url = (p) => UP + p.split('/').map(encodeURIComponent).join('/');
const save = () => { try { localStorage.setItem('ds-index', JSON.stringify({ ...state, q: '' })); } catch (e) {} };
const isDark = (t) => /dark/.test(t);
const themeLabel = (t) => t.replace('-experimental', ' (exp.)').replace('light-mobile', 'mobile').replace('light-high-contrast', 'high contrast');
const portrait = (s) => s.tags.includes('ios');

// ---------------------------------------------------------------- boot

fetch('data.json', { cache: 'no-store' })
  .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
  .then((d) => { DATA = d; route(); })
  .catch(() => {
    app.innerHTML = '<p class="empty">Could not load <code>gallery/data.json</code>. Run <code>make serve</code> from the repository root.</p>';
  });
window.addEventListener('hashchange', route);

function route() {
  if (!DATA) return;
  const parts = location.hash.replace(/^#\/?/, '').split('/').map(decodeURIComponent);
  const sys = DATA.systems.find((s) => s.slug === parts[0]);
  if (!sys) { renderIndex(); document.title = 'Design systems'; return; }
  const tab = ['screens', 'components', 'docs'].includes(parts[1]) ? parts[1] : 'screens';
  renderDetail(sys, tab, parts.slice(2).join('/'));
  document.title = `${sys.name} · Design systems`;
}

// ---------------------------------------------------------------- index

function matches(s) {
  if (state.cat !== 'all' && s.category !== state.cat) return false;
  if (state.dark && !s.themes.some(isDark)) return false;
  if (state.platform !== 'all' && !s.tags.includes(state.platform)) return false;
  const q = state.q.trim().toLowerCase();
  if (!q) return true;
  const hay = [s.name, s.slug, s.goodFor, s.category, DATA.categories[s.category], ...s.tags, ...s.themes, ...s.fonts.map((f) => f.family)].join(' ').toLowerCase();
  return q.split(/\s+/).every((w) => hay.includes(w));
}

function strip(sw) {
  return `<div class="strip" title="${esc(sw.map((x) => `${x.role} ${x.value}`).join(' · '))}">${sw
    .map((x) => `<span style="background:${esc(x.value)}"></span>`).join('')}</div>`;
}

function themeBadges(s) {
  return s.themes.filter((t) => t === 'light' || isDark(t))
    .map((t) => `<span class="badge ${isDark(t) ? 'dark' : ''}">${esc(isDark(t) ? 'Dark' : 'Light')}</span>`).join('');
}

function card(s) {
  const strips = Object.values(s.swatches).map(strip).join('');
  return `<a class="card" href="#/${esc(s.slug)}">
    <div class="cover ${portrait(s) ? 'portrait' : ''}"><img loading="lazy" src="${url(s.cover.thumb)}" alt="${esc(s.name)} screenshot"><div class="badges">${themeBadges(s)}</div></div>
    <div class="card-body">
      <div class="card-title"><h2>${esc(s.name)}</h2><span class="cat">${esc(DATA.categories[s.category] || s.category)}</span></div>
      <p class="good">${esc(s.goodFor)}</p>
      <div class="card-foot"><span class="fontline">${esc(s.fonts.map((f) => f.family).join(' · ') || '—')}</span><div class="strips">${strips}</div></div>
    </div></a>`;
}

function row(s) {
  const first = Object.values(s.swatches)[0] || [];
  return `<tr data-slug="${esc(s.slug)}" tabindex="0">
    <td><div class="thumb"><img loading="lazy" src="${url(s.cover.thumb)}" alt=""></div></td>
    <td class="nm">${esc(s.name)}</td>
    <td>${esc(DATA.categories[s.category] || s.category)}</td>
    <td class="gf">${esc(s.goodFor)}</td>
    <td>${strip(first)}</td>
    <td>${esc(s.themes.map(themeLabel).join(', '))}</td>
    <td class="dt">${esc(s.captured)}</td></tr>`;
}

function renderIndex() {
  const all = DATA.systems;
  const list = all.filter(matches);
  const cats = Object.entries(DATA.categories).filter(([k]) => all.some((s) => s.category === k));
  const chip = (attr, val, label, n, on) => `<button class="chip" data-${attr}="${esc(val)}" aria-pressed="${on}">${esc(label)}${n != null ? `<span class="n">${n}</span>` : ''}</button>`;
  app.innerHTML = `
    <div class="intro"><div><h1>Design systems</h1>
      <p>${list.length === all.length ? all.length : `${list.length} of ${all.length}`} styles captured from real products. Each one links to measured tokens, a rendered style guide and the original screenshots.</p></div></div>
    <div class="toolbar">
      <div class="chips">${chip('cat', 'all', 'All', all.length, state.cat === 'all')}${cats.map(([k, v]) => chip('cat', k, v, all.filter((s) => s.category === k).length, state.cat === k)).join('')}</div>
      <span class="sep"></span>
      <div class="chips">${chip('platform', 'web', 'Web', null, state.platform === 'web')}${chip('platform', 'ios', 'iOS', null, state.platform === 'ios')}${chip('dark', '1', 'Has dark theme', null, state.dark)}</div>
      <div class="seg" role="group" aria-label="Layout"><button data-view="grid" aria-pressed="${state.view === 'grid'}">Gallery</button><button data-view="list" aria-pressed="${state.view === 'list'}">List</button></div>
    </div>
    ${!list.length ? '<p class="empty">No style matches. Clear the search or filters.</p>'
      : state.view === 'list'
        ? `<div class="table-wrap"><table class="list"><thead><tr><th></th><th>Name</th><th>Category</th><th>Good for</th><th>Palette</th><th>Themes</th><th>Captured</th></tr></thead><tbody>${list.map(row).join('')}</tbody></table></div>`
        : `<div class="grid">${list.map(card).join('')}</div>`}`;
  app.querySelectorAll('[data-cat]').forEach((b) => b.onclick = () => { state.cat = b.dataset.cat; save(); renderIndex(); });
  app.querySelectorAll('[data-platform]').forEach((b) => b.onclick = () => { state.platform = state.platform === b.dataset.platform ? 'all' : b.dataset.platform; save(); renderIndex(); });
  app.querySelectorAll('[data-dark]').forEach((b) => b.onclick = () => { state.dark = !state.dark; save(); renderIndex(); });
  app.querySelectorAll('[data-view]').forEach((b) => b.onclick = () => { state.view = b.dataset.view; save(); renderIndex(); });
  app.querySelectorAll('tr[data-slug]').forEach((tr) => {
    const go = () => { location.hash = `#/${tr.dataset.slug}`; };
    tr.onclick = go; tr.onkeydown = (e) => { if (e.key === 'Enter') go(); };
  });
}

qInput.addEventListener('input', () => {
  state.q = qInput.value;
  if (location.hash.replace(/^#\/?/, '')) location.hash = '#/'; else renderIndex();
});

// ---------------------------------------------------------------- detail

function agentPrompt(s) {
  const abs = (p) => `${DATA.root}/${p}`;
  return `Match the ${s.name} design style from my design-systems library.\n`
    + `1. Read ${abs(s.entry)} in full first. It says what was captured and what to distrust.\n`
    + `2. Take colour, type, spacing and radius values from ${abs(s.tokens)}. Its top-level token groups are ${s.tokenGroups.join(', ')}; the README says which group holds colour roles and which holds scales. Never read a colour off a screenshot.\n`
    + `3. Use ${abs(s.dir)}/screenshots/ for layout and proportion only. ${abs(s.styleGuide)} renders every token.\n`
    + `4. Borrow structure and proportions, not the product's logo, icons, illustrations or brand colours.\n`
    + `5. In your summary, name the package and the tokens you used.`;
}

function paletteBlock(theme, sw) {
  const by = Object.fromEntries(sw.map((x) => [x.role, x.value]));
  const v = (r, fb) => esc(by[r] || fb);
  return `<div class="palette">
    <div class="palette-head"><span>${esc(themeLabel(theme))}</span><span>click a swatch to copy</span></div>
    <div class="palette-demo" style="background:${v('page', '#fff')}">
      <div class="demo-card" style="background:${v('surface', 'transparent')};border:1px solid ${v('border', 'transparent')}">
        <b style="color:${v('text', '#000')}">Heading in text colour</b>
        <small style="color:${v('muted', '#666')}">Secondary copy in the muted role, on the surface colour.</small>
        <span class="demo-pill" style="background:${v('accent', '#000')};color:${v('page', '#fff')}">Accent</span>
      </div>
    </div>
    <div class="swatches">${sw.map((x) => `<button class="swatch" data-copy="${esc(x.value)}" title="${esc(x.token)}">
      <i style="background:${esc(x.value)}"></i><b>${esc(x.role)}</b><code>${esc(x.value)}</code><code>${esc(x.token)}</code></button>`).join('')}</div>
  </div>`;
}

function renderDetail(s, tab, docPath) {
  const shots = s.screenshots;
  const comps = s.components;
  const docs = s.docs;
  app.innerHTML = `
    <a class="back" href="#/">← All styles</a>
    <div class="hero">
      <div>
        <h1>${esc(s.name)}</h1>
        <a class="site" href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.url.replace(/^https?:\/\//, ''))} ↗</a>
        <p class="lede">${esc(s.goodFor)}</p>
        <div class="actions">
          <a class="btn primary" href="${url(s.styleGuide)}" target="_blank" rel="noopener">Open style guide ↗</a>
          <a class="btn" href="#/${esc(s.slug)}/docs/${esc(s.entry)}">Read README</a>
          <a class="btn" href="${url(s.tokens)}" target="_blank" rel="noopener">Tokens JSON</a>
          <button class="btn" type="button" id="copy-prompt">Copy agent prompt</button>
        </div>
        <dl class="meta">
          <dt>Category</dt><dd>${esc(DATA.categories[s.category] || s.category)}</dd>
          <dt>Captured</dt><dd>${esc(s.captured)}${s.access ? ` · ${esc(s.access)}` : ''}</dd>
          <dt>Themes</dt><dd>${esc(s.themes.map(themeLabel).join(', '))}</dd>
          ${s.widths.length ? `<dt>Widths</dt><dd>${esc(s.widths.join(', '))} px</dd>` : ''}
          <dt>Package</dt><dd><code>${esc(s.dir)}/</code> · ${esc(s.shape)} shape</dd>
          <dt>Tags</dt><dd class="tags">${s.tags.map((t) => `<span class="tag">${esc(t)}</span>`).join('')}</dd>
          ${s.notes ? `<dt>Note</dt><dd>${esc(s.notes)}</dd>` : ''}
        </dl>
      </div>
      <div class="hero-shot ${portrait(s) ? 'portrait' : ''}" data-lb="cover"><img src="${url(s.cover.thumb)}" alt="${esc(s.name)} screenshot"></div>
    </div>

    <section class="section"><h2>Colour roles</h2><div class="palettes">${Object.entries(s.swatches).map(([t, sw]) => paletteBlock(t, sw)).join('')}</div></section>
    ${s.fonts.length ? `<section class="section"><h2>Type</h2><div class="fonts">${s.fonts.map((f) => `<div class="font">
      <div class="sample" style="font-family:${esc(f.stack)}">${esc(f.family)} Aa 123</div>
      <code>${esc(f.token)}</code><code class="stack" title="${esc(f.stack)}">${esc(f.stack)}</code></div>`).join('')}</div></section>` : ''}

    <div class="tabs" role="tablist">
      ${[['screens', 'Screenshots', shots.length], ['components', 'Components', comps.length], ['docs', 'Docs', docs.length]]
        .map(([k, l, n]) => `<button role="tab" data-tab="${k}" aria-selected="${tab === k}">${l}<span class="n">${n}</span></button>`).join('')}
    </div>
    <div id="pane"></div>`;

  app.querySelector('#copy-prompt').onclick = () => copy(agentPrompt(s), 'Agent prompt copied');
  app.querySelectorAll('[data-copy]').forEach((b) => b.onclick = () => copy(b.dataset.copy, `Copied ${b.dataset.copy}`));
  app.querySelectorAll('[data-tab]').forEach((b) => b.onclick = () => { history.replaceState(null, '', `#/${s.slug}/${b.dataset.tab}`); route(); });
  app.querySelector('[data-lb="cover"]').onclick = () => openLightbox([{ path: s.cover.path, name: 'cover' }], 0);

  const pane = app.querySelector('#pane');
  if (tab === 'screens') renderImages(pane, s, shots, true);
  if (tab === 'components') renderImages(pane, s, comps, false);
  if (tab === 'docs') renderDocs(pane, s, docPath || s.entry);
  if (docPath) pane.scrollIntoView({ block: 'start' });
  else window.scrollTo(0, 0);
}

function renderImages(pane, s, items, withThemeFilter) {
  if (!items.length) { pane.innerHTML = '<p class="empty">None captured in this package.</p>'; return; }
  let filter = 'all';
  let limit = PAGE;
  const counts = { light: 0, dark: 0, mobile: 0 };
  items.forEach((i) => i.tags.forEach((t) => { counts[t] += 1; }));
  const draw = () => {
    const shown = items.filter((i) => filter === 'all' || i.tags.includes(filter));
    const visible = shown.slice(0, limit);
    const groups = [...new Set(visible.map((i) => i.group))];
    const tile = (i) => `<button class="shot ${!portrait(s) && (i.tags.includes('mobile') || !withThemeFilter) ? 'contain' : ''}" data-i="${shown.indexOf(i)}">
      <div class="frame"><img loading="lazy" decoding="async" src="${url(i.thumb || i.path)}" alt="${esc(i.name)}"></div><span>${esc(i.name)}</span></button>`;
    pane.innerHTML = `
      ${withThemeFilter ? `<div class="subfilters">${['all', 'light', 'dark', 'mobile'].filter((k) => k === 'all' || counts[k])
        .map((k) => `<button class="chip" data-f="${k}" aria-pressed="${filter === k}">${k === 'all' ? 'All' : k[0].toUpperCase() + k.slice(1)}<span class="n">${k === 'all' ? items.length : counts[k]}</span></button>`).join('')}</div>` : ''}
      ${groups.map((g) => `${groups.length > 1 ? `<div class="group-title">${esc(g)}/</div>` : ''}<div class="shots ${portrait(s) && withThemeFilter ? 'phone' : ''}">${visible.filter((i) => i.group === g).map(tile).join('')}</div>`).join('')}
      ${shown.length > limit ? `<div class="more"><button class="btn" id="more">Show all ${shown.length}</button></div>` : ''}`;
    pane.querySelectorAll('[data-f]').forEach((b) => b.onclick = () => { filter = b.dataset.f; limit = PAGE; draw(); });
    pane.querySelectorAll('[data-i]').forEach((b) => b.onclick = () => openLightbox(shown, +b.dataset.i));
    const more = pane.querySelector('#more');
    if (more) more.onclick = () => { limit = Infinity; draw(); };
  };
  draw();
}

function renderDocs(pane, s, path) {
  pane.innerHTML = `<div class="doc-pick">${s.docs.map((d) => `<a class="chip" href="#/${esc(s.slug)}/docs/${esc(d)}" aria-pressed="${d === path}">${esc(d.split('/').pop())}</a>`).join('')}</div><article class="md"><p class="loading">Loading…</p></article>`;
  const art = pane.querySelector('.md');
  fetch(url(path)).then((r) => { if (!r.ok) throw new Error(r.status); return r.text(); })
    .then((text) => { art.innerHTML = markdown(text, path); })
    .catch(() => { art.innerHTML = `<p class="empty">Could not load ${esc(path)}.</p>`; });
}

// ---------------------------------------------------------------- markdown (small subset)

function resolvePath(base, href) {
  if (/^([a-z]+:|#|\/)/i.test(href)) return null;
  const parts = base.split('/').slice(0, -1);
  for (const seg of href.split('/')) {
    if (seg === '..') parts.pop(); else if (seg && seg !== '.') parts.push(seg);
  }
  return parts.join('/');
}

function inline(text, base) {
  const codes = [];
  let s = esc(text).replace(/`([^`]+)`/g, (_, c) => `\u0000${codes.push(c) - 1}\u0000`);
  s = s.replace(/!\[([^\]]*)\]\(([^)\s]+)[^)]*\)/g, (_, alt, src) => {
    const p = resolvePath(base, src);
    return `<img loading="lazy" alt="${alt}" src="${p ? url(p) : src}">`;
  });
  s = s.replace(/\[([^\]]+)\]\(([^)\s]+)[^)]*\)/g, (_, label, href) => {
    const clean = href.replace(/&amp;/g, '&');
    const [file, hash] = clean.split('#');
    const p = file ? resolvePath(base, file) : null;
    if (p && /\.md$/i.test(p)) {
      const slug = p.split('/')[1];
      if (p.startsWith('systems/') && DATA.systems.some((x) => x.slug === slug)) return `<a href="#/${esc(slug)}/docs/${esc(p)}">${label}</a>`;
    }
    if (!file && hash) return `<a href="#" data-anchor="${esc(hash)}">${label}</a>`;
    return `<a href="${p ? url(p) + (hash ? '#' + hash : '') : esc(clean)}" target="_blank" rel="noopener">${label}</a>`;
  });
  s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/(^|[\s(])\*([^*\s][^*]*)\*/g, '$1<em>$2</em>').replace(/(^|[\s(])_([^_\s][^_]*)_(?=[\s.,;:)]|$)/g, '$1<em>$2</em>');
  return s.replace(/\u0000(\d+)\u0000/g, (_, i) => `<code>${codes[+i]}</code>`);
}

function markdown(src, base) {
  const lines = src.replace(/\r/g, '').split('\n');
  const out = [];
  let i = 0;
  const slug = (t) => t.toLowerCase().replace(/<[^>]+>/g, '').replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '-');
  const isTableSep = (l) => /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$/.test(l || '');
  const cells = (l) => l.trim().replace(/^\|/, '').replace(/\|$/, '').split(/(?<!\\)\|/).map((c) => c.trim().replace(/\\\|/g, '|'));
  while (i < lines.length) {
    const l = lines[i];
    if (/^```/.test(l)) {
      const buf = [];
      i += 1;
      while (i < lines.length && !/^```/.test(lines[i])) { buf.push(lines[i]); i += 1; }
      i += 1;
      out.push(`<pre><code>${esc(buf.join('\n'))}</code></pre>`);
    } else if (/^#{1,6}\s/.test(l)) {
      const n = l.match(/^#+/)[0].length;
      const html = inline(l.replace(/^#+\s*/, ''), base);
      out.push(`<h${n} id="${slug(html)}">${html}</h${n}>`);
      i += 1;
    } else if (/^\s*\|/.test(l) && isTableSep(lines[i + 1])) {
      const head = cells(l);
      i += 2;
      const body = [];
      while (i < lines.length && /^\s*\|/.test(lines[i])) { body.push(cells(lines[i])); i += 1; }
      out.push(`<div class="tw"><table><thead><tr>${head.map((c) => `<th>${inline(c, base)}</th>`).join('')}</tr></thead><tbody>${body.map((r) => `<tr>${r.map((c) => `<td>${inline(c, base)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`);
    } else if (/^\s*([-*+]|\d+\.)\s/.test(l)) {
      const ordered = /^\s*\d+\./.test(l);
      const items = [];
      while (i < lines.length && (/^\s*([-*+]|\d+\.)\s/.test(lines[i]) || (/^\s{2,}\S/.test(lines[i]) && items.length))) {
        if (/^\s*([-*+]|\d+\.)\s/.test(lines[i])) items.push(lines[i].replace(/^\s*([-*+]|\d+\.)\s+/, ''));
        else items[items.length - 1] += ' ' + lines[i].trim();
        i += 1;
      }
      const tag = ordered ? 'ol' : 'ul';
      out.push(`<${tag}>${items.map((t) => `<li>${inline(t.replace(/^\[( |x)\]\s/i, (m, x) => (x.trim() ? '☑ ' : '☐ ')), base)}</li>`).join('')}</${tag}>`);
    } else if (/^>\s?/.test(l)) {
      const buf = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { buf.push(lines[i].replace(/^>\s?/, '')); i += 1; }
      out.push(`<blockquote>${inline(buf.join(' '), base)}</blockquote>`);
    } else if (/^\s*(-{3,}|\*{3,})\s*$/.test(l)) {
      out.push('<hr>');
      i += 1;
    } else if (!l.trim()) {
      i += 1;
    } else {
      const buf = [];
      while (i < lines.length && lines[i].trim() && !/^(#{1,6}\s|```|>|\s*([-*+]|\d+\.)\s)/.test(lines[i]) && !(/^\s*\|/.test(lines[i]) && isTableSep(lines[i + 1]))) { buf.push(lines[i].trim()); i += 1; }
      out.push(`<p>${inline(buf.join(' '), base)}</p>`);
    }
  }
  return out.join('\n');
}

app.addEventListener('click', (e) => {
  const a = e.target.closest('[data-anchor]');
  if (!a) return;
  e.preventDefault();
  const el = document.getElementById(a.dataset.anchor);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
});

// ---------------------------------------------------------------- lightbox, copy, theme, keys

const lb = document.getElementById('lightbox');
let lbItems = [];
let lbIndex = 0;
let lbOpener = null;
function openLightbox(items, index) {
  lbItems = items; lbIndex = index; lbOpener = document.activeElement;
  showLightbox(); lb.hidden = false;
  lb.querySelector('.lb-close').focus();
}
function closeLightbox() {
  lb.hidden = true;
  if (lbOpener && document.contains(lbOpener)) lbOpener.focus();
  lbOpener = null;
}
function showLightbox() {
  const it = lbItems[lbIndex];
  lb.querySelector('img').src = url(it.path);
  lb.querySelector('figcaption').innerHTML = `${esc(it.name)} <span style="opacity:.6">${lbIndex + 1} / ${lbItems.length}</span><a href="${url(it.path)}" target="_blank" rel="noopener">Open original ↗</a>`;
  lb.querySelector('.lb-prev').hidden = lb.querySelector('.lb-next').hidden = lbItems.length < 2;
}
const step = (d) => { lbIndex = (lbIndex + d + lbItems.length) % lbItems.length; showLightbox(); };
lb.querySelector('.lb-close').onclick = closeLightbox;
lb.querySelector('.lb-prev').onclick = () => step(-1);
lb.querySelector('.lb-next').onclick = () => step(1);
lb.addEventListener('click', (e) => { if (e.target === lb) closeLightbox(); });

const toast = document.getElementById('toast');
let toastTimer;
function copy(text, msg) {
  const done = () => { toast.textContent = msg; toast.hidden = false; clearTimeout(toastTimer); toastTimer = setTimeout(() => { toast.hidden = true; }, 1600); };
  if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(done, fallback);
  else fallback();
  function fallback() {
    const ta = Object.assign(document.createElement('textarea'), { value: text });
    document.body.append(ta); ta.select();
    try { document.execCommand('copy'); done(); } catch (e) { /* nothing else to try */ }
    ta.remove();
  }
}

document.getElementById('theme').onclick = () => {
  const root = document.documentElement;
  const current = root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  root.dataset.theme = current === 'dark' ? 'light' : 'dark';
  try { localStorage.setItem('ds-theme', root.dataset.theme); } catch (e) {}
};

document.addEventListener('keydown', (e) => {
  if (!lb.hidden) {
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'Tab') {
      // Keep focus inside the dialog while it is open.
      const stops = [...lb.querySelectorAll('button:not([hidden]), a[href]')];
      const at = stops.indexOf(document.activeElement);
      e.preventDefault();
      stops[(at + (e.shiftKey ? -1 : 1) + stops.length) % stops.length].focus();
    }
    if (e.key === 'ArrowLeft') step(-1);
    if (e.key === 'ArrowRight') step(1);
    return;
  }
  if (e.key === '/' && document.activeElement !== qInput) { e.preventDefault(); qInput.focus(); qInput.select(); }
  if (e.key === 'Escape' && document.activeElement === qInput) { qInput.value = ''; state.q = ''; qInput.blur(); if (!location.hash.replace(/^#\/?/, '')) renderIndex(); }
});
