// Design systems catalog. Reads data.json (written by tools/catalog.py) and renders
// an index of packages and a detail page per package. Hash routes:
//   #/                            index
//   #/<slug>[/<section>]          detail, one section at a time (SECTIONS below; overview by default)
//   #/<slug>/files/<path>         detail with a markdown file open
// Older links still work: /screens opens assets, /components opens components and
// /docs/<path> opens files/<path>; the hash is rewritten to the new form.
'use strict';

const app = document.getElementById('app');
const qInput = document.getElementById('q');
const UP = '../'; // data paths are relative to the docs site's root; this page lives in gallery/
const PAGE = 60;

let DATA = null;
const state = { q: '', cat: 'all', dark: false, platform: 'all', view: 'grid' };
try { Object.assign(state, JSON.parse(localStorage.getItem('ds-index') || '{}'), { q: '' }); } catch (e) {}
// The docs pages' header search lands here as gallery/index.html?q=<term>.
try { state.q = new URLSearchParams(location.search).get('q') || ''; } catch (e) {}
if (state.q) qInput.value = state.q;

const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const url = (p) => UP + p.split('/').map(encodeURIComponent).join('/');
const save = () => { try { localStorage.setItem('ds-index', JSON.stringify({ ...state, q: '' })); } catch (e) {} };
const isDark = (t) => /dark/.test(t);
const themeLabel = (t) => t.replace('-experimental', ' (exp.)').replace('light-mobile', 'mobile').replace('light-high-contrast', 'high contrast');
const portrait = (s) => s.tags.includes('ios');

// A toolbar filter button; `n` is the count badge only the package index shows.
const chip = (attr, val, label, n, on) => `<button class="chip" data-${attr}="${esc(val)}" aria-pressed="${on}">${esc(label)}${n != null ? `<span class="n">${n}</span>` : ''}</button>`;
// Both indexes end their filters the same way: every search word must appear in the haystack.
const textMatch = (fields) => {
  const q = state.q.trim().toLowerCase();
  return !q || q.split(/\s+/).every((w) => fields.join(' ').toLowerCase().includes(w));
};

// The detail page's sections, in rail order. null draws the divider.
const SECTIONS = [
  ['overview', 'Overview'], ['colors', 'Colors'], ['typography', 'Typography'], ['spacing', 'Spacing'],
  ['radius', 'Corner radius'], ['shadows', 'Shadows'], ['components', 'Components'], ['assets', 'Assets'],
  null, ['health', 'Health'], ['files', 'Files'],
];
const SECTION_IDS = SECTIONS.filter(Boolean).map(([k]) => k);
const LEGACY = { screens: 'assets', docs: 'files' };

// ---------------------------------------------------------------- boot

// data.json streams in parallel with the first route; the refero section never
// touches it, so nothing waits on it. Catalog routes re-dispatch when it lands.
const dataPromise = fetch('data.json', { cache: 'no-cache' })
  .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
  .then((d) => (DATA = d));
dataPromise.catch(() => {}); // a failed load is reported by the route that needs it
window.addEventListener('hashchange', route);
// The first route() runs at the bottom of this file, once every declaration exists.

// The sticky rail sits under the sticky top bar, whose height changes with the layout.
const bar = document.querySelector('.bar');
const setBarHeight = () => document.documentElement.style.setProperty('--bar-h', `${bar.offsetHeight}px`);
setBarHeight();
window.addEventListener('resize', setBarHeight);

function route() {
  const parts = location.hash.replace(/^#\/?/, '').split('/').map(decodeURIComponent);
  document.querySelectorAll('.site-nav a[href^="#/"]').forEach((a) => {
    const refero = a.getAttribute('href') === '#/refero';
    if (refero === (parts[0] === 'refero')) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
  });
  if (parts[0] === 'refero') { referoRoute(parts.slice(1)); return; }
  delete app.dataset.rf;
  if (rfIO) { rfIO.disconnect(); rfIO = null; }
  if (!DATA) {
    app.innerHTML = '<p class="loading">Loading catalog…</p>';
    dataPromise.then(route).catch(() => {
      if (location.hash.replace(/^#\/?/, '').split('/')[0] !== 'refero')
        app.innerHTML = '<p class="empty">Could not load <code>gallery/data.json</code>. Run <code>make serve</code> from the repository root.</p>';
    });
    return;
  }
  const sys = DATA.systems.find((s) => s.slug === parts[0]);
  if (!sys) { renderIndex(); document.title = 'Design systems'; return; }
  let sec = LEGACY[parts[1]] || parts[1] || 'overview';
  let rest = parts.slice(2).join('/');
  if (!SECTION_IDS.includes(sec)) { sec = 'overview'; rest = ''; }
  if (sec !== 'files') rest = '';
  if (parts[1] && parts[1] !== sec) history.replaceState(null, '', `#/${sys.slug}/${sec}${rest ? `/${rest}` : ''}`);
  renderDetail(sys, sec, rest);
  const label = SECTIONS.find((x) => x && x[0] === sec)[1];
  document.title = `${sys.name} · ${label} · Design systems`;
}

// ---------------------------------------------------------------- index

function matches(s) {
  if (state.cat !== 'all' && s.category !== state.cat) return false;
  if (state.dark && !s.themes.some(isDark)) return false;
  if (state.platform !== 'all' && !s.tags.includes(state.platform)) return false;
  return textMatch([s.name, s.slug, s.goodFor, s.category, DATA.categories[s.category], ...s.tags, ...s.themes, ...s.fonts.map((f) => f.family)]);
}

function strip(sw) {
  return `<div class="strip" title="${esc(sw.map((x) => `${x.role} ${x.value}`).join(' · '))}">${sw
    .map((x) => `<span style="background:${esc(x.value)}"></span>`).join('')}</div>`;
}

// The newest scorecard audit for a package: "16/25 met", or nothing when it has not
// been graded yet. Pages live beside the gallery in the docs site.
const scoreText = (s) => (s.score ? `${s.score.meets}/${s.score.applicable} met` : '');
const scoreHref = (s) => `../scorecard/systems/${encodeURIComponent(s.slug)}/`;

// The product's app icon: identifies where a package came from at a glance.
const iconImg = (s) => (s.icon ? `<img class="app-icon" src="${url(s.icon)}" alt="" loading="lazy">` : '');

// The frames a card scrubs through on hover, refero.design style: the cover
// first, then an even spread of the package's other screenshots. Capped so a
// sweep across the shot loads a handful of thumbs at most.
const SCRUB_MAX = 8;
let cardFrames = new Map();
function scrubFrames(s) {
  const rest = s.screenshots.filter((i) => i.path !== s.cover.path && (portrait(s) || !i.tags.includes('mobile')));
  const step = Math.max(1, Math.ceil(rest.length / (SCRUB_MAX - 1)));
  const frames = rest.filter((_, i) => i % step === 0).slice(0, SCRUB_MAX - 1);
  frames.unshift({ path: s.cover.path, thumb: s.cover.thumb });
  return frames;
}

// refero.design's card lockup: a padded matte holds the shot on a blurred
// colour glow of itself (the aura), then the app icon, name and one-line
// description. Moving the cursor across the shot scrubs the frames.
function card(s) {
  const cover = s.cover.thumb || s.cover.path;
  const icon = s.icon ? iconImg(s) : `<i>${esc(s.name[0].toUpperCase())}</i>`;
  return `<a class="card${portrait(s) ? ' portrait' : ''}" href="#/${esc(s.slug)}" data-slug="${esc(s.slug)}">
    <div class="cover"><img class="aura" src="${url(cover)}" alt="" aria-hidden="true" loading="lazy" onload="this.classList.add('on')"><div class="viewport" data-i="0"><div class="stack"><img src="${url(cover)}" alt="${esc(s.name)} screenshot" loading="lazy" decoding="async"></div></div></div>
    <div class="card-foot"><span class="foot-icon">${icon}</span><div class="foot-txt"><h2>${esc(s.name)}</h2><p>${esc(s.goodFor)}</p></div></div></a>`;
}

function row(s) {
  const first = Object.values(s.swatches)[0] || [];
  return `<tr data-slug="${esc(s.slug)}" tabindex="0">
    <td><div class="thumb"><img loading="lazy" src="${url(s.cover.thumb)}" alt=""></div></td>
    <td class="nm">${iconImg(s)}${esc(s.name)}</td>
    <td>${esc(DATA.categories[s.category] || s.category)}</td>
    <td class="gf">${esc(s.goodFor)}</td>
    <td>${strip(first)}</td>
    <td>${esc(s.themes.map(themeLabel).join(', '))}</td>
    <td class="dt">${esc(scoreText(s))}</td>
    <td class="dt">${esc(s.captured)}</td></tr>`;
}

function renderIndex() {
  const all = DATA.systems;
  const list = all.filter(matches);
  const cats = Object.entries(DATA.categories).filter(([k]) => all.some((s) => s.category === k));
  cardFrames = new Map(list.map((s) => [s.slug, scrubFrames(s)]));
  delete app.dataset.pkg;
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
        ? `<div class="table-wrap"><table class="list"><thead><tr><th></th><th>Name</th><th>Category</th><th>Good for</th><th>Palette</th><th>Themes</th><th>Score</th><th>Captured</th></tr></thead><tbody>${list.map(row).join('')}</tbody></table></div>`
        : `<div class="grid">${list.map(card).join('')}</div>`}`;
  app.querySelectorAll('[data-cat]').forEach((b) => b.onclick = () => { state.cat = b.dataset.cat; save(); renderIndex(); });
  app.querySelectorAll('[data-platform]').forEach((b) => b.onclick = () => { state.platform = state.platform === b.dataset.platform ? 'all' : b.dataset.platform; save(); renderIndex(); });
  app.querySelectorAll('[data-dark]').forEach((b) => b.onclick = () => { state.dark = !state.dark; save(); renderIndex(); });
  app.querySelectorAll('[data-view]').forEach((b) => b.onclick = () => { state.view = b.dataset.view; save(); renderIndex(); });
  app.querySelectorAll('tr[data-slug]').forEach((tr) => {
    const go = () => { location.hash = `#/${tr.dataset.slug}`; };
    tr.onclick = go; tr.onkeydown = (e) => { if (e.key === 'Enter') go(); };
  });
  window.scrollTo(0, 0);
}

qInput.addEventListener('input', () => {
  state.q = qInput.value;
  const h = location.hash.replace(/^#\/?/, '');
  // A failed JSON leaves its error page up; typing must not navigate away or throw.
  if (h === 'refero') { syncRfSearch(qInput.value); rfRedrawGrid(); }
  else if (h.startsWith('refero/')) location.hash = '#/refero';
  else if (h) location.hash = '#/';
  else if (DATA) renderIndex();
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

// Package files are fetched once per page load: Overview and Health both read the README.
const texts = new Map();
// Prefetched export files (slug.ext -> text | 'pending' | 'missing'): the copy
// buttons read them synchronously, because a clipboard write after a fetch loses
// the click's user gesture in Safari.
const exportText = new Map();
function getText(path) {
  if (!texts.has(path)) {
    texts.set(path, fetch(url(path)).then((r) => { if (!r.ok) throw new Error(r.status); return r.text(); })
      .catch((e) => { texts.delete(path); throw e; }));
  }
  return texts.get(path);
}

// The text between a generated section's `<!-- name:start ... -->` and `<!-- name:end -->`.
function between(text, name) {
  const m = text.match(new RegExp(`<!-- ${name}:start[\\s\\S]*?-->\\n([\\s\\S]*?)<!-- ${name}:end -->`));
  return m ? m[1].trim() : null;
}

const filesHref = (s, path) => `#/${esc(s.slug)}/files/${esc(path)}`;
const fileName = (p) => p.split('/').pop();
const cssLen = (v) => (typeof v === 'number' ? `${v}px` : String(v));
const sentence = (t) => String(t).trim().replace(/\.$/, '');
const tokensFile = (s) => fileName(s.tokens);

// A section, or part of one, the package has nothing for. The reason comes from the
// catalog's layoutGaps or the DESIGN.md generator's omitted list, never made up here.
function notCaptured(s, text) {
  return `<div class="nc" role="note"><span class="nc-tag">Not captured</span><p>${inline(text, s.entry)}</p></div>`;
}
function gapText(s, part, fallback) {
  const why = s.layoutGaps[part];
  return why ? `No \`${part}\` in this package: ${sentence(why)}.` : fallback;
}

function counts(s) {
  return {
    overview: null,
    colors: Object.values(s.swatches).reduce((n, sw) => n + sw.length, 0),
    typography: s.typeStyles.length || s.fonts.length,
    spacing: s.spacing.length,
    radius: s.radii.length,
    shadows: s.shadows.length,
    components: s.components.length,
    assets: s.icons.total + s.screenshots.length,
    health: s.score ? `${s.score.meets}/${s.score.applicable}` : null,
    files: s.docs.length,
  };
}

function renderShell(s) {
  const n = counts(s);
  app.dataset.pkg = s.slug;
  app.innerHTML = `
    <a class="back" href="#/">← All styles</a>
    <header class="pkg-head">
      <h1>${iconImg(s)}${esc(s.name)}</h1>
      <div class="pkg-sub">
        <a class="site" href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.url.replace(/^https?:\/\//, ''))} ↗</a>
        <span>${esc(DATA.categories[s.category] || s.category)}</span>
        <span>${esc(s.themes.map(themeLabel).join(', '))}</span>
      </div>
    </header>
    <div class="pkg">
      <nav class="rail" aria-label="${esc(s.name)} sections">
        <ul>${SECTIONS.map((x) => {
          if (!x) return '<li class="rail-sep" aria-hidden="true"></li>';
          const [k, label] = x;
          const c = n[k];
          return `<li><a href="#/${esc(s.slug)}/${k}" data-sec="${k}" class="${c === 0 ? 'is-empty' : ''}"><span>${esc(label)}</span>${c != null ? `<span class="n">${esc(c)}</span>` : ''}</a></li>`;
        }).join('')}</ul>
      </nav>
      <div class="pkg-main" id="section"></div>
    </div>`;
}

function renderDetail(s, sec, docPath) {
  const fresh = app.dataset.pkg !== s.slug || !app.querySelector('#section');
  if (fresh) renderShell(s);
  const rail = app.querySelector('.rail');
  rail.querySelectorAll('a[data-sec]').forEach((a) => {
    if (a.dataset.sec === sec) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
  });
  // On a phone the rail is one scrolling row: keep the open section in view.
  const on = rail.querySelector('[aria-current]');
  if (on && rail.scrollWidth > rail.clientWidth) rail.scrollLeft = on.offsetLeft - (rail.clientWidth - on.offsetWidth) / 2;

  const main = app.querySelector('#section');
  main.dataset.sec = sec;
  RENDER[sec](main, s, docPath);

  if (fresh) { window.scrollTo(0, 0); return; }
  // Switching sections keeps the page header in place unless it has scrolled away,
  // in which case the new section starts at the top of the view.
  const pkg = app.querySelector('.pkg');
  const top = pkg.getBoundingClientRect().top + window.scrollY - bar.offsetHeight - 12;
  if (window.scrollY > top) window.scrollTo(0, top);
}

const head = (title, sub) => `<header class="sec-head"><h2>${esc(title)}</h2>${sub ? `<p>${sub}</p>` : ''}</header>`;

const RENDER = {
  overview(main, s) {
    main.innerHTML = `
      ${head('Overview')}
      <div class="hero">
        <div>
          <p class="lede">${esc(s.goodFor)}</p>
          <div class="actions">
            <a class="btn primary" href="${url(s.styleGuide)}" target="_blank" rel="noopener">Open style guide ↗</a>
            <a class="btn" href="${filesHref(s, s.entry)}">Read README</a>
            <a class="btn" href="${url(s.tokens)}" target="_blank" rel="noopener">Tokens JSON</a>
            <button class="btn" type="button" id="copy-css" title="Resolved CSS custom properties (catalog.py export)">Copy CSS</button>
            <button class="btn" type="button" id="copy-json" title="Resolved flat token map (catalog.py export --format json)">Copy flat JSON</button>
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
            ${s.score ? `<dt>Scorecard</dt><dd><a href="${scoreHref(s)}">${s.score.meets} of ${s.score.applicable} met</a> · ${s.score.partly} partly · ${s.score.missing} missing <span class="faint">(${esc(s.score.date)})</span></dd>` : ''}
            ${s.score && s.score.contrast ? `<dt>Contrast</dt><dd class="warn">${esc(s.score.contrast)}</dd>` : ''}
          </dl>
        </div>
        <button type="button" class="hero-shot ${portrait(s) ? 'portrait' : ''}" data-lb="cover" aria-label="Open the cover screenshot"><img src="${url(s.cover.thumb)}" alt="${esc(s.name)} screenshot"></button>
      </div>
      <h3 class="sub-title">Brief</h3>
      <article class="md brief"><p class="loading">Loading…</p></article>`;
    main.querySelector('#copy-prompt').onclick = () => copy(agentPrompt(s), 'Agent prompt copied');
    // The schema extractor (tools/catalog.py export), materialised by the build
    // into gallery/export/<slug>.{css,json}: resolved values, ready to paste.
    // The texts are prefetched on render so the clipboard write stays inside the
    // click — Safari rejects a writeText that first waits on the network.
    for (const ext of ['css', 'json']) {
      const key = `${s.slug}.${ext}`;
      if (exportText.has(key)) continue;
      exportText.set(key, 'pending');
      fetch(`export/${encodeURIComponent(s.slug)}.${ext}`, { cache: 'no-cache' })
        .then((r) => { if (!r.ok) throw new Error(r.status); return r.text(); })
        .then((text) => exportText.set(key, text))
        .catch(() => exportText.set(key, 'missing'));
    }
    for (const [id, ext, label] of [['#copy-css', 'css', 'CSS'], ['#copy-json', 'json', 'flat JSON']]) {
      main.querySelector(id).onclick = () => {
        const text = exportText.get(`${s.slug}.${ext}`);
        if (text === 'pending' || text === undefined) { notice(`${label} still loading; try again`); return; }
        if (text === 'missing') { notice(`No ${label} export yet; run \`make build\` first`); return; }
        copy(text, `${label} copied`);
      };
    }
    main.querySelector('[data-lb="cover"]').onclick = () => openLightbox([{ path: s.cover.path, name: 'cover' }], 0);
    const art = main.querySelector('.brief');
    getText(s.entry).then((text) => {
      const brief = between(text, 'brief');
      art.outerHTML = brief ? `<article class="md brief">${markdown(brief, s.entry)}</article>`
        : notCaptured(s, `The README has no generated Brief; \`make brief\` writes one.`);
    }).catch(() => { art.innerHTML = `<p class="empty">Could not load ${esc(s.entry)}.</p>`; });
  },

  colors(main, s) {
    main.innerHTML = `${head('Colors', 'The six colour roles for each captured theme, from the catalog. Click a swatch to copy its value.')}
      <div class="palettes">${Object.entries(s.swatches).map(([t, sw]) => paletteBlock(t, sw)).join('')}</div>`;
    main.querySelectorAll('[data-copy]').forEach((b) => b.onclick = () => copy(b.dataset.copy, `Copied ${b.dataset.copy}`));
  },

  typography(main, s) {
    const stackFor = (family) => {
      const f = family && s.fonts.find((x) => x.family.toLowerCase() === family.toLowerCase());
      if (f) return f.stack;
      if (!family) return 'inherit';
      // Not a catalog font: name it first and fall back to the generic family its name says.
      const generic = /mono|code/i.test(family) ? 'ui-monospace, monospace' : /serif/i.test(family) && !/sans/i.test(family) ? 'Georgia, serif' : 'system-ui, sans-serif';
      return `"${family.replace(/"/g, '')}", ${generic}`;
    };
    // A numeric line height is a multiplier (DESIGN.md writes it unitless); a string keeps its unit.
    const spec = (t) => [t.size, t.lineHeight != null ? `/ ${t.lineHeight}` : '', t.weight != null ? `· ${t.weight}` : '',
      t.letterSpacing && !/^0(px|em|rem)?$/.test(t.letterSpacing) ? `· ${t.letterSpacing} tracking` : '', t.family ? `· ${t.family}` : '']
      .filter(Boolean).join(' ');
    const style = (t) => [`font-family:${stackFor(t.family)}`, t.size && `font-size:${t.size}`, t.weight != null && `font-weight:${t.weight}`,
      t.lineHeight != null && `line-height:${t.lineHeight}`, t.letterSpacing && `letter-spacing:${t.letterSpacing}`].filter(Boolean).join(';');
    main.innerHTML = `${head('Typography', `Font families from the catalog, then every type style ${esc(tokensFile(s))} defines, rendered live as DESIGN.md holds them (${esc(s.tokenTheme)} theme). A font this machine does not have falls back to the system face.`)}
      ${s.fonts.length ? `<div class="fonts">${s.fonts.map((f) => `<div class="font">
        <div class="sample" style="font-family:${esc(f.stack)}">${esc(f.family)} Aa 123</div>
        <code>${esc(f.token)}</code><code class="stack" title="${esc(f.stack)}">${esc(f.stack)}</code></div>`).join('')}</div>` : ''}
      <h3 class="sub-title">Type styles <span class="n">${s.typeStyles.length}</span></h3>
      ${s.typeStyles.length ? `<div class="type-styles">${s.typeStyles.map((t) => `<div class="type-row">
        <div class="type-sample" style="${esc(style(t))}">The quick brown fox jumps over the lazy dog</div>
        <div class="type-meta"><b>${esc(t.name)}</b><code>${esc(spec(t))}</code></div></div>`).join('')}</div>`
        : notCaptured(s, s.omitted.typography ? `${sentence(s.omitted.typography)}.` : 'No type styles in the tokens file.')}`;
  },

  spacing(main, s) {
    const max = Math.max(0, ...s.spacing.map((x) => parseFloat(x.value) || 0));
    main.innerHTML = `${head('Spacing', `Every spacing step ${esc(tokensFile(s))} defines, in DESIGN.md order. Each bar is as long as its value.`)}
      ${s.spacing.length ? `<div class="space-list">${s.spacing.map((x) => `<div class="space-row">
        <code class="nm" title="${esc(x.name)}">${esc(x.name)}</code>
        <div class="space-track"><span class="space-bar" style="width:${esc(cssLen(x.value))}"></span></div>
        <code class="val">${esc(cssLen(x.value))}</code></div>`).join('')}</div>
        ${max > 640 ? '<p class="faint-note">Bars longer than the column are cut at its edge.</p>' : ''}`
        : notCaptured(s, s.omitted.spacing ? `${sentence(s.omitted.spacing)}.` : 'No spacing steps in the tokens file.')}`;
  },

  radius(main, s) {
    main.innerHTML = `${head('Corner radius', `Every radius step ${esc(tokensFile(s))} defines, drawn on a box.`)}
      ${s.radii.length ? `<div class="radius-grid">${s.radii.map((x) => `<div class="radius-tile">
        <div class="radius-box" style="border-radius:${esc(cssLen(x.value))}"></div>
        <b title="${esc(x.name)}">${esc(x.name)}</b><code>${esc(cssLen(x.value))}</code></div>`).join('')}</div>`
        : notCaptured(s, s.omitted.rounded ? `${sentence(s.omitted.rounded)}.` : 'No radius steps in the tokens file.')}`;
  },

  shadows(main, s) {
    const sw = s.swatches[s.tokenTheme] || Object.values(s.swatches)[0] || [];
    const by = Object.fromEntries(sw.map((x) => [x.role, x.value]));
    main.innerHTML = `${head('Shadows', `Every shadow and elevation token in ${esc(tokensFile(s))}, resolved for the ${esc(s.tokenTheme)} theme and shown on that theme's own page and surface colours.`)}
      ${s.shadows.length ? `<div class="shadow-stage" style="background:${esc(by.page || '#fff')}"><div class="shadow-grid">${s.shadows.map((x) => `<figure class="shadow-card">
        <div class="shadow-sample" style="background:${esc(by.surface || by.page || '#fff')};box-shadow:${esc(x.css)}"></div>
        <figcaption><b style="color:${esc(by.text || '#000')}">${esc(x.token)}</b><code style="color:${esc(by.muted || '#666')}" title="${esc(x.css)}">${esc(x.css)}</code></figcaption></figure>`).join('')}</div></div>`
        : notCaptured(s, `No shadow or elevation token in ${tokensFile(s)}: the ${s.tokenTheme} colour set and \`core\` were searched, as for DESIGN.md.`)}`;
  },

  components(main, s) {
    const docs = ['components.md', 'patterns.md'].map((n) => [n, s.docs.find((d) => fileName(d) === n)]);
    const links = docs.filter(([, d]) => d).map(([n, d]) => `<a class="btn" href="${filesHref(s, d)}">Read ${esc(n)}</a>`).join('');
    const missing = docs.filter(([n, d]) => !d && s.layoutGaps[n]).map(([n]) => gapText(s, n, ''));
    main.innerHTML = `${head('Components', 'Element crops cut from the captures, and the written component and pattern notes.')}
      ${links ? `<div class="actions">${links}</div>` : ''}
      ${missing.map((t) => notCaptured(s, t)).join('')}
      <h3 class="sub-title">Crops <span class="n">${s.components.length}</span></h3>
      <div id="crops"></div>`;
    const pane = main.querySelector('#crops');
    if (s.components.length) renderImages(pane, s, s.components, false);
    else pane.innerHTML = notCaptured(s, gapText(s, 'components/', 'No element crops under `components/`.'));
  },

  assets(main, s) {
    const { total, items } = s.icons;
    const sw = s.swatches[s.tokenTheme] || Object.values(s.swatches)[0] || [];
    const page = (sw.find((x) => x.role === 'page') || {}).value || '#fff';
    main.innerHTML = `${head('Assets', 'Icons kept in the package, then every screenshot. Screenshots are for layout and proportion, never for colour values.')}
      <h3 class="sub-title">Icons <span class="n">${total}</span></h3>
      ${total ? `<div class="icon-grid" style="--icon-bg:${esc(page)}">${items.map((p) => `<figure class="icon-tile" title="${esc(p.replace(`${s.dir}/`, ''))}">
        <div class="icon-face"><img loading="lazy" src="${url(p)}" alt=""></div><figcaption>${esc(fileName(p).replace(/\.[^.]+$/, ''))}</figcaption></figure>`).join('')}</div>
        ${total > items.length ? `<p class="faint-note">Showing the first ${items.length} of ${total}. The rest are in <code>${esc(s.dir)}/icons/</code>.</p>` : ''}`
        : notCaptured(s, gapText(s, 'icons/', 'No icon images under `icons/`.'))}
      <h3 class="sub-title">Screenshots <span class="n">${s.screenshots.length}</span></h3>
      <div id="shots"></div>`;
    const pane = main.querySelector('#shots');
    if (s.screenshots.length) renderImages(pane, s, s.screenshots, true);
    else pane.innerHTML = notCaptured(s, gapText(s, 'screenshots/', 'No screenshots under `screenshots/`.'));
  },

  health(main, s) {
    main.innerHTML = `${head('Health', s.score ? `The README's generated Health section. Every grade with its evidence is on the <a href="${scoreHref(s)}">Scorecard page</a>.` : "The README's generated Health section.")}
      <article class="md health"><p class="loading">Loading…</p></article>`;
    const art = main.querySelector('.health');
    getText(s.entry).then((text) => {
      const health = between(text, 'health');
      art.outerHTML = health ? `<article class="md health">${markdown(health, s.entry)}</article>`
        : notCaptured(s, 'The README has no generated Health section; `make grade` writes one.');
    }).catch(() => { art.innerHTML = `<p class="empty">Could not load ${esc(s.entry)}.</p>`; });
  },

  files(main, s, path) {
    main.innerHTML = `${head('Files', 'Every Markdown file at the top of the package, rendered.')}<div id="docs"></div>`;
    renderDocs(main.querySelector('#docs'), s, path || s.entry);
  },
};

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

function renderImages(pane, s, items, withThemeFilter) {
  let filter = 'all';
  const counts = { light: 0, dark: 0, mobile: 0 };
  items.forEach((i) => i.tags.forEach((t) => { counts[t] += 1; }));
  let shown = [];
  let groups = new Map();
  let at = 0;
  let gen = 0;
  const tile = (i, k) => `<button class="shot ${!portrait(s) && (i.tags.includes('mobile') || !withThemeFilter) ? 'contain' : ''}" data-i="${k}">
    <div class="frame"><img loading="lazy" decoding="async" src="${url(i.thumb || i.path)}" alt="${esc(i.name)}"></div><span>${esc(i.name)}</span>${i.tags.length ? `<span class="shot-tags">${i.tags.map((t) => `<span class="tag">${esc(t)}</span>`).join('')}</span>` : ''}</button>`;
  // Tiles append a PAGE at a time: "Show all" drains the rest a chunk per frame
  // instead of building one giant innerHTML.
  const feed = (drain, g) => {
    const end = Math.min(at + PAGE, shown.length);
    for (; at < end; at++) groups.get(shown[at].group).insertAdjacentHTML('beforeend', tile(shown[at], at));
    const more = pane.querySelector('[data-more]');
    if (at >= shown.length) { if (more) more.parentElement.remove(); return; }
    if (drain) requestAnimationFrame(() => { if (g === gen && pane.isConnected) feed(true, g); });
  };
  const draw = () => {
    const g = ++gen;
    shown = items.filter((i) => filter === 'all' || i.tags.includes(filter));
    const names = [...new Set(shown.map((i) => i.group))];
    pane.innerHTML = `
      ${withThemeFilter ? `<div class="subfilters">${['all', 'light', 'dark', 'mobile'].filter((k) => k === 'all' || counts[k])
        .map((k) => `<button class="chip" data-f="${k}" aria-pressed="${filter === k}">${k === 'all' ? 'All' : k[0].toUpperCase() + k.slice(1)}<span class="n">${k === 'all' ? items.length : counts[k]}</span></button>`).join('')}</div>` : ''}
      ${names.map((gr) => `${names.length > 1 ? `<div class="group-title">${esc(gr)}/</div>` : ''}<div class="shots ${portrait(s) && withThemeFilter ? 'phone' : ''}" data-g="${esc(gr)}"></div>`).join('')}
      ${shown.length > PAGE ? `<div class="more"><button class="btn" data-more>Show all ${shown.length}</button></div>` : ''}`;
    groups = new Map([...pane.querySelectorAll('.shots')].map((el) => [el.dataset.g, el]));
    at = 0;
    pane.querySelectorAll('[data-f]').forEach((b) => b.onclick = () => { filter = b.dataset.f; draw(); pane.querySelector(`[data-f="${filter}"]`).focus(); });
    const more = pane.querySelector('[data-more]');
    if (more) more.onclick = () => { more.disabled = true; feed(true, g); };
    feed(false, g);
  };
  pane.onclick = (e) => {
    const b = e.target.closest('.shot[data-i]');
    if (b && shown[+b.dataset.i]) openLightbox(shown, +b.dataset.i);
  };
  draw();
}

// An in-page link the open section cannot satisfy (the Brief's link to "Do and don't",
// say) opens the README under Files and scrolls there once it has loaded.
let pendingAnchor = null;

function renderDocs(pane, s, path) {
  pane.innerHTML = `<div class="doc-pick">${s.docs.map((d) => `<a class="chip" href="${filesHref(s, d)}" aria-pressed="${d === path}">${esc(fileName(d))}</a>`).join('')}</div><article class="md"><p class="loading">Loading…</p></article>`;
  const art = pane.querySelector('.md');
  getText(path)
    .then((text) => {
      art.innerHTML = markdown(text, path);
      const id = pendingAnchor;
      pendingAnchor = null;
      const el = id && document.getElementById(id);
      if (el) el.scrollIntoView({ block: 'start' });
    })
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
      if (p.startsWith('systems/') && DATA.systems.some((x) => x.slug === slug)) return `<a href="#/${esc(slug)}/files/${esc(p)}">${label}</a>`;
      // The library docs are pages of the same docs site: docs/PACKAGE.md is served at ../PACKAGE/.
      const page = p.match(/^docs\/(.+)\.md$/i);
      if (page) return `<a href="${UP}${page[1] === 'index' ? '' : `${page[1].split('/').map(encodeURIComponent).join('/')}/`}${hash ? '#' + esc(hash) : ''}">${label}</a>`;
    }
    if (!file && hash) return `<a href="#" data-anchor="${esc(hash)}" data-doc="${esc(base)}">${label}</a>`;
    return `<a href="${p ? url(p) + (hash ? '#' + hash : '') : esc(clean)}" target="_blank" rel="noopener">${label}</a>`;
  });
  s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>').replace(/(^|[\s(])\*([^*\s][^*]*)\*/g, '$1<em>$2</em>').replace(/(^|[\s(])_([^_\s][^_]*)_(?=[\s.,;:)]|$)/g, '$1<em>$2</em>');
  return s.replace(/\u0000(\d+)\u0000/g, (_, i) => `<code>${codes[+i]}</code>`);
}

function markdown(src, base) {
  const lines = src.replace(/\r/g, '').split('\n');
  const out = [];
  let i = 0;
  const slug = (t) => t.toLowerCase().replace(/<[^>]+>/g, '').replace(/&[#\w]+;/g, '').replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '-');
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

// refero.design's card scrub: the shot is divided into one zone per frame, the
// cursor's x picks the frame, and the new thumb fades in over the previous one.
// The stack keeps only the last two mounted, so the crossfade always has a full
// frame underneath it. One delegated listener covers every card.
app.addEventListener('mousemove', (e) => {
  const vp = e.target instanceof Element && e.target.closest('.viewport[data-i]');
  if (!vp || !app.contains(vp)) return;
  const a = vp.closest('a.card');
  const frames = a && cardFrames.get(a.dataset.slug);
  if (!frames || frames.length < 2) return;
  const r = vp.getBoundingClientRect();
  const i = Math.min(frames.length - 1, Math.floor(Math.max(e.clientX - r.left, 0) / (r.width / frames.length)));
  if (i === +vp.dataset.i) return;
  vp.dataset.i = i;
  const img = document.createElement('img');
  img.src = url(frames[i].thumb || frames[i].path);
  img.alt = '';
  img.decoding = 'async';
  const stack = vp.firstElementChild;
  stack.append(img);
  // Trim on load, not on append: a sweep across two uncached zones must not
  // drop the last loaded frame, or the shot blanks until the next one lands.
  // Only frames mounted before this one are trimmed, so a stale load can never
  // remove a newer request; pending frames are bounded so a sweep cannot pile
  // them up.
  img.addEventListener('load', () => {
    if (img.parentNode !== stack) return;
    const before = [];
    for (const el of stack.children) { if (el === img) break; before.push(el); }
    const keep = before.findLast((el) => el.complete && el.naturalWidth > 0);
    for (const el of before) if (el !== keep) el.remove();
  }, { once: true });
  img.addEventListener('error', () => img.remove(), { once: true });
  while (stack.children.length > 4) stack.children[1].remove();
});

app.addEventListener('click', (e) => {
  const a = e.target.closest('[data-anchor]');
  if (!a) return;
  e.preventDefault();
  const el = document.getElementById(a.dataset.anchor);
  if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); return; }
  const slug = app.dataset.pkg;
  if (slug && a.dataset.doc) { pendingAnchor = a.dataset.anchor; location.hash = `#/${slug}/files/${a.dataset.doc}`; }
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
function notice(msg) {
  toast.textContent = msg; toast.hidden = false; clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { toast.hidden = true; }, 1600);
}

function copy(text, msg) {
  const done = () => notice(msg);
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
  // index.html always sets data-theme (stored pref, else dark).
  root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
  try { localStorage.setItem('ds-theme', root.dataset.theme); } catch (e) {}
};

// ---------------------------------------------------------------- refero
// The refero/ library: interpreted styles scraped from styles.refero.design.
// catalog.py emits refero/index.json + refero/<slug>.json; media lives outside
// the repo under /refero-media/ (shots, posters, videos, detail videos and
// their posters, favicons). Every media
// element carries data-r with the remote CDN URL and swaps to it onerror, so a
// dev box without the mirror still renders.

let RF_INDEX = null;
let rfPromise = null;
const rfState = { theme: 'all', video: false, type: 'all', style: 'all' };
try { Object.assign(rfState, JSON.parse(localStorage.getItem('ds-refero') || '{}')); } catch (e) {}
const rfSave = () => { try { localStorage.setItem('ds-refero', JSON.stringify(rfState)); } catch (e) {} };
const RF_PAGE = 48;
// The emitted refero/index.json shape; getRefero refuses a stale format.
const RF_VERSION = 2;
let rfIO = null;
const rfSlug = () => location.hash.replace(/^#\/?/, '').split('/').map(decodeURIComponent);

function getRefero() {
  if (!rfPromise) rfPromise = fetch('refero/index.json', { cache: 'no-cache' })
    .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then((d) => {
      if (d.version !== RF_VERSION) throw new Error(`refero index.json version ${d.version}`);
      return (RF_INDEX = d);
    })
    .catch((e) => { rfPromise = null; throw e; });
  return rfPromise;
}

// Entity JSONs run ~40-100 KB each; keep a few, evicting the oldest first (FIFO).
const RF_ENTITY_CAP = 20;
const rfEntityCache = new Map();
function getRfEntity(slug) {
  if (!rfEntityCache.has(slug)) {
    if (rfEntityCache.size >= RF_ENTITY_CAP) rfEntityCache.delete(rfEntityCache.keys().next().value);
    rfEntityCache.set(slug, fetch(`refero/style/${encodeURIComponent(slug)}.json`, { cache: 'no-cache' })
      .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
      .catch((e) => { rfEntityCache.delete(slug); throw e; }));
  }
  return rfEntityCache.get(slug);
}

function referoRoute(parts) {
  if (!parts[0]) {
    document.title = 'Refero styles · Design systems';
    delete app.dataset.pkg;
    app.dataset.rf = 'index';
    app.innerHTML = '<p class="loading">Loading refero styles…</p>';
    getRefero()
      .then(() => { if (rfSlug()[0] === 'refero' && !rfSlug()[1]) drawReferoIndex(); })
      .catch(() => {
        if (rfSlug()[0] === 'refero' && !rfSlug()[1])
          app.innerHTML = '<p class="empty">Could not load <code>gallery/refero/index.json</code>. Run <code>make serve</code>.</p>';
      });
    return;
  }
  renderRfEntity(parts[0]);
}

// Local media mirrors live under /refero-media/<kind>/<slug>.<ext>. index.json
// keeps the remote CDN prefix once under `cdn`; a remote field is a path suffix
// under it, or an absolute URL as-is.
const rfLocalMedia = (kind, s, ext) => `/refero-media/${kind}/${encodeURIComponent(s.slug)}.${ext}`;
const rfCdn = (u) => (u ? (u.includes('://') ? u : `${RF_INDEX.cdn || ''}${u}`) : null);

// Local mirror first, remote CDN on error. With `drop` a broken element removes
// itself (the letter tile shows through); a video just stops retrying.
const rfMediaAttrs = (media, drop) => {
  if (!media || !(media.local || media.remote)) return '';
  const src = `src="${esc(media.local || media.remote)}"`;
  if (!(media.local && media.remote)) return drop ? `${src} onerror="this.remove()"` : src;
  const fail = drop ? 'this.remove()' : `this.dataset.r=''`;
  return `${src} data-r="${esc(media.remote)}" onerror="if(this.dataset.r&&this.src!==this.dataset.r){this.src=this.dataset.r}else{${fail}}"`;
};
const rfImg = (media, cls, alt, attrs) => {
  const m = rfMediaAttrs(media, true);
  return m ? `<img class="${cls}" ${attrs || ''} loading="lazy" ${m} alt="${esc(alt)}">` : '';
};

function rfFav(s, big) {
  // Entity JSONs emit media.favicon {local, remote}; index cards carry no
  // media block, so cards derive the same pair from the slug and source host.
  const media = ((s.media || {}).favicon)
    || { local: rfLocalMedia('favicons', s, 'png'),
         remote: s.src || s.source_url
           ? `https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=${encodeURIComponent(`https://${host(s.src || s.source_url)}`)}&size=128` : null };
  return `<span class="rf-fav${big ? ' big' : ''}"><i>${esc((s.name || '?')[0].toUpperCase())}</i><img loading="lazy" ${rfMediaAttrs(media, true)} alt=""></span>`;
}
const host = (u) => String(u || '').replace(/^https?:\/\//, '').replace(/^www\./, '').replace(/\/.*$/, '');

function rfMatches(s) {
  if (rfState.theme !== 'all' && s.theme !== rfState.theme) return false;
  if (rfState.video && !s.video) return false;
  if (rfState.type !== 'all' && s.type !== rfState.type) return false;
  if (rfState.style !== 'all' && s.style !== rfState.style) return false;
  return textMatch([s.name, s.slug, s.tagline, s.industry, s.src, s.type, s.style, ...(s.tags || [])]);
}

function rfCard(s, note) {
  // index.json's `card` is one bit: "p" poster, "s" shot; the path derives from the slug.
  const card = { local: s.card ? rfLocalMedia(s.card === 'p' ? 'posters' : 'shots', s, 'jpg') : null,
    remote: rfCdn(s.cardRemote) };
  return `<a class="rf-card" href="#/refero/${esc(s.slug)}" data-slug="${esc(s.slug)}">
    <div class="rf-tile"><div class="rf-shot">${rfImg(card, '', `${s.name} screenshot`)}</div></div>
    <div class="rf-card-foot">${rfFav(s)}<div class="rf-card-txt"><h3>${esc(s.name)}</h3><p>${esc(note || s.tagline || '')}</p></div></a>`;
}

// The card's scroll-preview video sits over the shot and fades in once it is
// really playing, the same overlay pattern styles.refero.design uses.
function rfCardVideo(shot, s) {
  if (shot.querySelector('video')) return;
  shot.insertAdjacentHTML('beforeend',
    `<video ${rfMediaAttrs({ local: rfLocalMedia('videos', s, 'mp4'), remote: rfCdn(s.videoRemote) }, true)} muted loop playsinline></video>`);
  const v = shot.querySelector('video');
  if (!v) return;
  const play = () => v.play().catch(() => {});
  v.addEventListener('playing', () => v.classList.add('on'));
  // When the local mirror is missing, onerror swaps to the remote src; that
  // aborts the pending play(), so retry from canplay — it fires again for the
  // new source.
  v.addEventListener('canplay', play);
  play();
}

// A hover must hold briefly before its ~1-3 MB preview video starts buffering,
// or sweeping the grid would download several at once.
const RF_HOVER_MS = 200;
const rfHoverTimers = new WeakMap();

// The hero prompt chips: each one dials in a filter pair from the label vocab.
const RF_CHIPS = [
  ['Dark mode SaaS', { theme: 'dark', type: 'saas' }],
  ['Warm paper', { style: 'paper' }],
  ['Brutalist portfolio', { style: 'brutalist', type: 'portfolio' }],
  ['Editorial agency', { style: 'editorial', type: 'agency' }],
  ['Neon crypto', { style: 'neon', type: 'crypto' }],
  ['Minimal devtools', { style: 'minimal', type: 'devtools' }],
  ['Cinematic media', { style: 'cinematic', type: 'media' }],
  ['Swiss fintech', { style: 'swiss', type: 'fintech' }],
];

// Re-render just the grid + count: typing in either search field and flipping
// filters land here, so the hero input keeps focus while the list updates.
function rfRedrawGrid() {
  if (!RF_INDEX) return;
  const wrap = app.querySelector('.rf-wrap');
  if (!wrap) return;
  const list = RF_INDEX.styles.filter(rfMatches);
  app.querySelectorAll('[data-theme]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.theme === rfState.theme)));
  app.querySelectorAll('[data-video]').forEach((b) => b.setAttribute('aria-pressed', String(rfState.video)));
  const count = app.querySelector('.rf-bar-row .count');
  if (count) count.textContent = `${list.length} style${list.length === 1 ? '' : 's'}`;
  rfFillGrid(wrap, list);
}

function rfFillGrid(wrap, list) {
  wrap.innerHTML = !list.length
    ? '<p class="empty">No style matches. Clear the search or filters.</p>'
    : '<div class="rf-grid"></div><div id="rf-sent" class="more"><button class="btn">Load more</button></div>';
  const grid = wrap.querySelector('.rf-grid');
  const sent = wrap.querySelector('#rf-sent');
  if (!grid) return;
  if (rfIO) { rfIO.disconnect(); rfIO = null; }
  const bySlug = new Map(list.map((s) => [s.slug, s]));
  let at = 0;
  const feed = () => {
    const chunk = list.slice(at, at + RF_PAGE);
    at += chunk.length;
    grid.insertAdjacentHTML('beforeend', chunk.map((s) => rfCard(s)).join(''));
    if (at >= list.length) {
      if (sent) sent.remove();
      if (rfIO) { rfIO.disconnect(); rfIO = null; }
    }
  };
  feed();
  if (!sent) return;
  const btn = sent.querySelector('button');
  rfIO = new IntersectionObserver((es) => { if (es[0].isIntersecting) feed(); }, { rootMargin: '900px' });
  rfIO.observe(sent);
  btn.onclick = feed;
  // Refero plays a style's scroll-preview video when its card is hovered.
  grid.addEventListener('mouseover', (ev) => {
    const a = ev.target.closest('a.rf-card');
    if (!a || a.contains(ev.relatedTarget)) return;
    const v = a.querySelector('.rf-shot video');
    if (v) { v.play().catch(() => {}); return; }
    const s = bySlug.get(a.dataset.slug);
    if (!s || !s.video) return;
    const shot = a.querySelector('.rf-shot');
    if (!shot || rfHoverTimers.has(a)) return;
    rfHoverTimers.set(a, setTimeout(() => {
      rfHoverTimers.delete(a);
      if (!shot.isConnected) return; // the grid was replaced while the timer waited
      rfCardVideo(shot, s);
    }, RF_HOVER_MS));
  });
  grid.addEventListener('mouseout', (ev) => {
    const a = ev.target.closest('a.rf-card');
    if (!a || a.contains(ev.relatedTarget)) return;
    clearTimeout(rfHoverTimers.get(a));
    rfHoverTimers.delete(a);
    const v = a.querySelector('.rf-shot video');
    if (v) { v.pause(); v.classList.remove('on'); }
  });
}

// Keep the hero search field and the top bar's shared field in step.
function syncRfSearch(v) {
  const hero = app.querySelector('#rf-q');
  if (hero && hero.value !== v) hero.value = v;
  if (qInput.value !== v) qInput.value = v;
}

function drawReferoIndex() {
  const all = RF_INDEX.styles;
  const values = (key) => [...new Set(all.map((s) => s[key]).filter(Boolean))].sort();
  const sel = (key, first) => `<select class="rf-sel" data-sel="${key}" aria-label="${first}"><option value="all">${first}</option>${values(key).map((v) => `<option value="${esc(v)}"${v === rfState[key] ? ' selected' : ''}>${esc(v)}</option>`).join('')}</select>`;
  const tab = (k, label, on) => `<button type="button" data-theme="${k}" aria-pressed="${on}">${esc(label)}</button>`;
  app.dataset.rf = 'index';
  app.innerHTML = `
    <div class="rf-hero">
      <div class="rf-beta"><a class="pill" href="https://styles.refero.design" target="_blank" rel="noopener">Refero</a>
        <p><span class="dot" aria-hidden="true"></span>${all.length.toLocaleString('en')} styles · interpreted, not measured</p></div>
      <h1><em>Every site,</em> in DESIGN.md</h1>
      <p class="rf-sub">Browse ${all.length.toLocaleString('en')} AI-readable design systems interpreted by
        <a href="https://styles.refero.design" target="_blank" rel="noopener">styles.refero.design</a>.
        Open any style for colors, typography, spacing, and a DESIGN.md your agent can follow.
        Their words, not measured evidence — treat values as inspiration.</p>
      <label class="rf-search"><input id="rf-q" type="search" placeholder="Search DESIGN.md examples" autocomplete="off" aria-label="Search refero styles"><button class="go" type="button" aria-label="Search"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 13V3M3.5 7.5 8 3l4.5 4.5"/></svg></button></label>
      <div class="rf-chips">${RF_CHIPS.map(([label], i) => `<button type="button" data-chip="${i}"><i>↳</i>${esc(label)}</button>`).join('')}</div>
    </div>
    <div class="rf-bar-row">
      <div class="rf-tabs-list">${tab('all', 'All themes', rfState.theme === 'all')}${tab('light', 'Light', rfState.theme === 'light')}${tab('dark', 'Dark', rfState.theme === 'dark')}${tab('mixed', 'Mixed', rfState.theme === 'mixed')}<button type="button" data-video aria-pressed="${rfState.video}">Has video</button></div>
      ${sel('type', 'All types')}${sel('style', 'All styles')}
      <span class="count"></span>
    </div>
    <div class="rf-wrap"></div>`;
  const hero = app.querySelector('#rf-q');
  hero.value = state.q;
  hero.addEventListener('input', () => { state.q = hero.value; qInput.value = hero.value; rfRedrawGrid(); });
  hero.addEventListener('keydown', (ev) => { if (ev.key === 'Enter') app.querySelector('.rf-grid .rf-card')?.focus(); });
  app.querySelector('.rf-search .go').onclick = () => hero.focus();
  app.querySelectorAll('[data-chip]').forEach((b) => b.onclick = () => {
    Object.assign(rfState, { theme: 'all', video: false, type: 'all', style: 'all' }, RF_CHIPS[+b.dataset.chip][1]);
    rfSave(); syncRfSearch((state.q = ''));
    app.querySelectorAll('select[data-sel]').forEach((s) => { s.value = rfState[s.dataset.sel]; });
    rfRedrawGrid();
    app.querySelector('.rf-wrap').scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
  app.querySelectorAll('[data-theme]').forEach((b) => b.onclick = () => { rfState.theme = b.dataset.theme; rfSave(); rfRedrawGrid(); });
  app.querySelectorAll('[data-video]').forEach((b) => b.onclick = () => { rfState.video = !rfState.video; rfSave(); rfRedrawGrid(); });
  app.querySelectorAll('select[data-sel]').forEach((s) => s.onchange = () => { rfState[s.dataset.sel] = s.value; rfSave(); rfRedrawGrid(); });
  window.scrollTo(0, 0);
  rfRedrawGrid();
}

// ---- entity page

const RF_TABS = [
  ['design_md', 'DESIGN.md'], ['theme_css', 'Tailwind v4'],
  ['variables_css', 'CSS Variables'], ['tokens_json', 'Design Tokens'],
];

function renderRfEntity(slug) {
  delete app.dataset.pkg;
  app.dataset.rf = 'entity';
  if (rfIO) { rfIO.disconnect(); rfIO = null; }
  app.innerHTML = '<p class="loading">Loading…</p>';
  const onPage = () => { const cur = rfSlug(); return cur[0] === 'refero' && cur[1] === slug; };
  let entity = null;
  // The ~800 KB index only feeds the "More like this" strip: the page paints on
  // the entity alone, and the strip fills in whenever the index lands.
  getRefero()
    .then(() => {
      if (!entity || !onPage()) return;
      const el = app.querySelector('#rf-similar');
      if (el) el.innerHTML = rfSimilar(entity);
    })
    .catch(() => {});
  getRfEntity(slug).then((e) => {
    if (!onPage()) return;
    entity = e;
    drawRfEntity(e);
  }).catch((err) => {
    if (!onPage()) return;
    // A 404 means the style does not exist; anything else may be transient.
    app.innerHTML = err instanceof Error && err.message === '404'
      ? `<p class="empty">No refero style <code>${esc(slug)}</code>. <a href="#/refero">Back to Refero styles</a>.</p>`
      : `<p class="empty">Could not load <code>gallery/refero/style/${esc(slug)}.json</code>. Check the connection and reload, or <a href="#/refero">go back to Refero styles</a>.</p>`;
  });
}

function rfMediaTag(e) {
  const m = e.media || {};
  const v = m.detail || m.video;
  // The still sits under the video, which fades in over it once it plays —
  // the same pattern the cards use, at entity size.
  const still = rfImg(m.shot || m.poster || (v === m.detail ? m.detail_poster : null) || m.detail_poster, '', `${e.name} screenshot`);
  if (v && (v.local || v.remote)) {
    const pair = (v === m.detail && m.detail_poster) || m.poster;
    // poster= is an attribute, not an element: it cannot fall back like
    // rfMediaAttrs' src does, so the remote URL wins over a possibly absent
    // local file (e.g. a mirror that predates a kind).
    const poster = (pair && (pair.remote || pair.local)) || '';
    return `${still}<video ${rfMediaAttrs(v, true)}
      ${poster ? `poster="${esc(poster)}"` : ''} muted loop playsinline autoplay></video>`;
  }
  return still || '<p class="empty">No preview captured.</p>';
}

function rfSwatch(c) {
  const v = c.hex || c.value || '';
  const grad = /gradient/i.test(v);
  return `<button class="rf-sw" type="button" data-copy="${esc(v)}" title="Copy ${esc(grad ? 'gradient' : v)}">
    <span class="sw-i" style="background:${esc(v)}"><span class="sw-copy"><svg viewBox="0 0 24 24" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="14" height="14" x="8" y="8" rx="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>Copy</span></span>
    <span class="rf-sw-txt"><b>${esc(c.name || v)}</b><code>${esc(grad ? 'Gradient' : v)}</code>
    ${c.role ? `<span class="rf-sw-role">${esc(c.role)}</span>` : ''}</span></button>`;
}

function rfColors(e) {
  const colors = e.ds.colors || [];
  if (!colors.length) return '';
  const groups = new Map();
  colors.forEach((c) => { const g = c.group || 'other'; if (!groups.has(g)) groups.set(g, []); groups.get(g).push(c); });
  const order = [...groups.keys()].sort((a, b) => (a === 'neutral') - (b === 'neutral') || a.localeCompare(b));
  const label = (g) => ({ neutral: 'Neutrals', accent: 'Accent', semantic: 'Semantic', brand: 'Brand' }[g] || g[0].toUpperCase() + g.slice(1));
  return `<section class="rf-sec"><h2 class="rf-h2">Color Palette</h2>
    ${order.map((g) => `<h3 class="rf-h3">${esc(label(g))}</h3><div class="rf-swatches">${groups.get(g).map(rfSwatch).join('')}</div>`).join('')}</section>`;
}

// One type-scale row; the "Show all N steps" button emits the rest verbatim.
const rfScaleRow = (t) => `<div class="rf-scale-row">
  <span class="rf-scale-label">${esc(t.role || 'step')}<code>${esc([t.size && `${t.size}px`, t.weight, t.lineHeight].filter(Boolean).join(' · '))}</code></span>
  <span class="rf-scale-sample" style="font-size:${esc(cssLen(t.size || 14))};line-height:${esc(t.lineHeight || 1.4)};font-weight:${esc(t.weight || 400)}">The quick brown fox jumps over the lazy dog</span></div>`;

function rfTypography(e) {
  const fonts = e.ds.typography || [];
  const scale = e.ds.typeScale || [];
  if (!fonts.length && !scale.length) return '';
  const stack = (f) => `"${String(f.family || '').replace(/"/g, '')}", ${f.substitute ? `"${f.substitute}", ` : ''}${/mono/i.test(f.family || '') ? 'ui-monospace, monospace' : 'system-ui, sans-serif'}`;
  const spec = (f) => [['Weight', f.weight], ['Sizes', f.sizes && `${f.sizes} px`], ['Line height', f.lineHeight], ['Tracking', f.letterSpacing], ['Substitute', f.substitute]]
    .filter((x) => x[1]).map(([k, v]) => `<dt>${k}</dt><dd>${esc(v)}</dd>`).join('');
  return `<section class="rf-sec"><h2 class="rf-h2">Typography</h2>
    ${scale.length ? `<div class="rf-scale" id="rf-scale">${scale.slice(0, 8).map(rfScaleRow).join('')}</div>
      ${scale.length > 8 ? `<button class="btn" id="rf-scale-all" type="button">Show all ${scale.length} steps</button>` : ''}` : ''}
    <div class="rf-fonts">${fonts.map((f) => `<div class="rf-font">
      <div class="rf-font-sample" style="font-family:${esc(stack(f))}">${esc(f.family || 'Unknown')} Aa 123</div>
      <dl class="rf-font-spec">${spec(f)}</dl>
      ${f.role ? `<p class="rf-note">${esc(f.role)}</p>` : ''}</div>`).join('')}</div></section>`;
}

function rfSpacing(e) {
  const sp = e.ds.spacing || {};
  const el = e.ds.elevation || [];
  const rows = [['Density', sp.density], ['Max width', sp.pageMaxWidth], ['Section gap', sp.sectionGap], ['Card padding', sp.cardPadding], ['Element gap', sp.elementGap]].filter((r) => r[1]);
  const radii = Object.entries(sp.radius || {});
  if (!rows.length && !radii.length && !el.length) return '';
  const px = (v) => { const m = String(v).match(/^([\d.]+)px$/); return m ? +m[1] : null; };
  return `<section class="rf-sec"><h2 class="rf-h2">Spacing &amp; Shape</h2>
    <div class="rf-tables">
      ${rows.length ? `<table class="rf-table"><thead><tr><th>Purpose</th><th>Value</th><th></th></tr></thead><tbody>
        ${rows.map(([k, v]) => { const p = px(v); return `<tr><td>${esc(k)}</td><td><code>${esc(v)}</code></td><td>${p ? `<span class="rf-bar" style="width:${p}px"></span>` : ''}</td></tr>`; }).join('')}</tbody></table>` : ''}
      ${radii.length ? `<table class="rf-table"><thead><tr><th>Element</th><th>Radius</th><th></th></tr></thead><tbody>
        ${radii.map(([k, v]) => `<tr><td>${esc(k)}</td><td><code>${esc(v)}</code></td><td><i class="rf-rbox" style="border-radius:${esc(v)}"></i></td></tr>`).join('')}</tbody></table>` : ''}
    </div>
    ${el.length ? `<div class="rf-elev">${el.map((x) => `<div class="rf-elev-row"><i class="rf-ebox" style="box-shadow:${esc(x.style)}"></i><div><b>${esc(x.element)}</b><code>${esc(x.style)}</code></div></div>`).join('')}</div>` : ''}
    ${e.ds.elevationPhilosophy ? `<p class="rf-note">${esc(e.ds.elevationPhilosophy)}</p>` : ''}</section>`;
}

function rfGuidelines(e) {
  const dos = e.ds.dos || [];
  const donts = e.ds.donts || [];
  if (!dos.length && !donts.length) return '';
  const txt = (t) => esc(typeof t === 'string' ? t : (t.text || JSON.stringify(t)));
  const col = (title, items, mark, cls) => `<div class="rf-guide ${cls}"><h3 class="rf-h3">${title}</h3>
    <ul>${items.map((t) => `<li><span class="mk">${mark}</span><span>${txt(t)}</span></li>`).join('')}</ul></div>`;
  return `<section class="rf-sec"><h2 class="rf-h2">Guidelines</h2><div class="rf-guides">${col('Do', dos, '✓', 'do')}${col("Don't", donts, '✕', 'dont')}</div></section>`;
}

function rfSimilar(e) {
  if (!RF_INDEX) return '';
  const find = (slug) => slug && RF_INDEX.styles.find((x) => x.slug === slug);
  const items = (e.similar || []).map((x) => ({ slug: x.slug, name: x.name, note: x.why, s: find(x.slug) }));
  const have = new Set(items.map((i) => i.slug).concat([e.slug]));
  const fill = RF_INDEX.styles.filter((s) => !have.has(s.slug))
    .map((s) => ({ s, sc: (e.type && s.type === e.type) + (e.style && s.style === e.style) + (e.theme && s.theme === e.theme) }))
    .filter((x) => x.sc > 0)
    .sort((a, b) => b.sc - a.sc || String(a.s.name).localeCompare(String(b.s.name)))
    .slice(0, Math.max(0, 6 - items.length)).map((x) => x.s);
  const all = items.concat(fill.map((s) => ({ slug: s.slug, name: s.name, note: null, s })));
  if (!all.length) return '';
  return `<section class="rf-sec"><h2 class="rf-h2">More like this</h2><div class="rf-grid rf-sim">
    ${all.map((x) => (x.slug && x.s ? rfCard(x.s, x.note)
      : `<div class="rf-card rf-plain" title="Not in this library"><div class="rf-tile"><div class="rf-shot rf-empty"><span>${esc((x.name || '?')[0].toUpperCase())}</span></div></div><div class="rf-card-foot"><div class="rf-card-txt"><h3>${esc(x.name)}</h3><p>${esc(x.note || '')}</p></div></div></div>`)).join('')}
  </div></section>`;
}

// A small syntax tint for the doc pane, after the real site's shiki/GitHub
// highlighting: whole-line roles first (headings, quotes, fences), then
// inline code and bold inside a line. It is a tint, not a parser.
function rfCodeHtml(text, tab) {
  if (tab === 'design_md') {
    let fence = false;
    return text.split('\n').map((l) => {
      if (/^\s*```/.test(l)) { fence = !fence; return `<span class="tk-m">${esc(l)}</span>`; }
      if (fence) return `<span class="tk-c">${esc(l)}</span>`;
      if (/^\s*#{1,6}\s/.test(l)) return `<span class="tk-h">${esc(l)}</span>`;
      if (/^\s*>/.test(l)) return `<span class="tk-q">${esc(l)}</span>`;
      return esc(l)
        .replace(/`([^`]+)`/g, '<span class="tk-c">`$1`</span>')
        .replace(/(&lt;!--[\s\S]*?--&gt;)/g, '<span class="tk-m">$1</span>');
    }).join('\n');
  }
  if (tab === 'tokens_json') {
    return esc(text).split('\n').map((l) => l
      .replace(/^(\s*)(&quot;.*?&quot;)(\s*:)/, '$1<span class="tk-h">$2</span>$3')
      .replace(/(:\s*)(&quot;.*?&quot;)/, '$1<span class="tk-s">$2</span>')
      .replace(/(:\s*)(-?[\d.]+|true|false|null)/, '$1<span class="tk-n">$2</span>')).join('\n');
  }
  return esc(text)
    .replace(/(--[\w-]+)(\s*:)/g, '<span class="tk-h">$1</span>$2')
    .replace(/@[\w-]+/g, '<span class="tk-q">$&</span>')
    .replace(/(&quot;.*?&quot;|&#39;.*?&#39;)/g, '<span class="tk-s">$1</span>')
    .replace(/(\/\*[\s\S]*?\*\/)/g, '<span class="tk-m">$1</span>');
}

const RF_DL_EXT = { design_md: 'design.md', theme_css: 'theme.css', variables_css: 'variables.css', tokens_json: 'tokens.json' };

function drawRfEntity(e) {
  document.title = `${e.name} · Refero · Design systems`;
  const ds = e.ds || {};
  const ico = {
    copy: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="14" height="14" x="8" y="8" rx="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>',
    dl: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>',
    ext: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7"/><path d="M8 7h9v9"/></svg>',
  };
  app.dataset.rf = 'entity';
  app.innerHTML = `
    <div class="rf-page">
      <div class="rf-col">
        <a class="rf-back" href="#/refero">← Refero styles</a>
        <div class="rf-media">${rfMediaTag(e)}</div>
        <div class="rf-title"><h1>${esc(e.name)}</h1>${rfFav(e, true)}</div>
        ${e.tagline ? `<p class="rf-tagline">${esc(e.tagline)}</p>` : ''}
        ${ds.description ? `<p class="rf-desc">${esc(ds.description)}</p>` : ''}
        ${e.source_url ? `<a class="rf-src" href="${esc(e.source_url)}" target="_blank" rel="noopener">${ico.ext}${esc(e.source_url.replace(/^https?:\/\//, ''))}</a>` : ''}
        <p class="rf-meta">${esc(e.theme || '')}${e.type ? ` · ${esc(e.type)}` : ''}${e.style ? ` · ${esc(e.style)}` : ''}${e.industry ? ` · ${esc(e.industry)}` : ''}</p>
        ${rfColors(e)}${rfTypography(e)}${rfSpacing(e)}${rfGuidelines(e)}<div id="rf-similar">${rfSimilar(e)}</div>
      </div>
      <aside class="rf-pane">
        <div class="rf-tabs" role="tablist">${RF_TABS.map(([k, l]) => `<button role="tab" type="button" data-tab="${k}" aria-selected="${k === 'design_md'}">${esc(l)}</button>`).join('')}</div>
        <div class="rf-docbar">
          <span class="rf-mode">${[['compact', 'Compact'], ['extended', 'Extended']].map(([k, l]) => `<button type="button" data-mode="${k}" aria-pressed="${k === 'extended'}">${esc(l)}</button>`).join('')}</span>
          <div class="acts">
            <button class="rf-mini" id="rf-copy" type="button" title="Copy this document">${ico.copy}Copy</button>
            <button class="rf-mini" id="rf-dl" type="button" title="Download this document">${ico.dl}<span class="rf-dl-ext">.md</span></button>
            ${e.page_url ? `<a class="rf-cta" href="${esc(e.page_url)}" target="_blank" rel="noopener"><span class="cta-t">Open on refero</span>${ico.ext}</a>` : ''}
          </div>
        </div>
        <div class="rf-pane-body" id="rf-pane-body"></div>
      </aside>
    </div>`;

  const mv = app.querySelector('.rf-media video');
  if (mv) mv.addEventListener('playing', () => mv.classList.add('on'));

  let tab = 'design_md';
  let mode = 'extended';
  const body = app.querySelector('#rf-pane-body');
  const renderTab = () => {
    app.querySelectorAll('.rf-tabs [data-tab]').forEach((b) => b.setAttribute('aria-selected', String(b.dataset.tab === tab)));
    app.querySelectorAll('.rf-mode [data-mode]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.mode === mode)));
    const ext = (RF_DL_EXT[tab] || 'txt').split('.').pop();
    app.querySelector('.rf-dl-ext').textContent = `.${ext}`;
    const doc = (e.docs || {})[tab] || '(empty)';
    const lines = doc.split('\n');
    const cut = mode === 'compact' && lines.length > 24;
    body.innerHTML = `<pre class="rf-code${cut ? ' rf-cut' : ''}"><code>${rfCodeHtml(cut ? lines.slice(0, 24).join('\n') + '\n…' : doc, tab)}</code></pre>`;
  };
  app.querySelectorAll('.rf-tabs [data-tab]').forEach((b) => b.onclick = () => { tab = b.dataset.tab; renderTab(); });
  app.querySelectorAll('.rf-mode [data-mode]').forEach((b) => b.onclick = () => { mode = b.dataset.mode; renderTab(); });
  renderTab();
  app.querySelector('#rf-copy').onclick = () => copy((e.docs || {})[tab] || '', `${RF_TABS.find((t) => t[0] === tab)[1]} copied`);
  app.querySelector('#rf-dl').onclick = () => {
    const blob = new Blob([(e.docs || {})[tab] || ''], { type: 'text/plain' });
    const a = Object.assign(document.createElement('a'), { href: URL.createObjectURL(blob), download: `${e.slug}-${RF_DL_EXT[tab] || 'doc.txt'}` });
    a.click();
    setTimeout(() => URL.revokeObjectURL(a.href), 4000);
  };
  app.querySelectorAll('.rf-sw[data-copy]').forEach((b) => b.onclick = () => copy(b.dataset.copy, `Copied ${b.dataset.copy}`));
  const all = app.querySelector('#rf-scale-all');
  if (all) all.onclick = () => {
    app.querySelector('#rf-scale').innerHTML = (ds.typeScale || []).map(rfScaleRow).join('');
    all.remove();
  };
  window.scrollTo(0, 0);
}

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
  const typing = document.activeElement?.matches('input, textarea, select') || document.activeElement?.isContentEditable;
  if (e.key === '/' && !typing) { e.preventDefault(); qInput.focus(); qInput.select(); }
  if (e.key === 'Escape' && document.activeElement === qInput) {
    qInput.value = ''; state.q = ''; qInput.blur();
    const h = location.hash.replace(/^#\/?/, '');
    if (h === 'refero' && RF_INDEX) drawReferoIndex(); else if (!h && DATA) renderIndex();
  }
});

// First paint: everything above is declared, and data.json has been downloading
// since the top of the file. Refero routes never wait on it.
route();
