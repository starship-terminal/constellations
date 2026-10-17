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

const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const url = (p) => UP + p.split('/').map(encodeURIComponent).join('/');
const save = () => { try { localStorage.setItem('ds-index', JSON.stringify({ ...state, q: '' })); } catch (e) {} };
const isDark = (t) => /dark/.test(t);
const themeLabel = (t) => t.replace('-experimental', ' (exp.)').replace('light-mobile', 'mobile').replace('light-high-contrast', 'high contrast');
const portrait = (s) => s.tags.includes('ios');

// The detail page's sections, in rail order. null draws the divider.
const SECTIONS = [
  ['overview', 'Overview'], ['colors', 'Colors'], ['typography', 'Typography'], ['spacing', 'Spacing'],
  ['radius', 'Corner radius'], ['shadows', 'Shadows'], ['components', 'Components'], ['assets', 'Assets'],
  null, ['health', 'Health'], ['files', 'Files'],
];
const SECTION_IDS = SECTIONS.filter(Boolean).map(([k]) => k);
const LEGACY = { screens: 'assets', docs: 'files' };

// ---------------------------------------------------------------- boot

fetch('data.json', { cache: 'no-store' })
  .then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); })
  .then((d) => { DATA = d; route(); })
  .catch(() => {
    app.innerHTML = '<p class="empty">Could not load <code>gallery/data.json</code>. Run <code>make serve</code> from the repository root.</p>';
  });
window.addEventListener('hashchange', route);

// The sticky rail sits under the sticky top bar, whose height changes with the layout.
const bar = document.querySelector('.bar');
const setBarHeight = () => document.documentElement.style.setProperty('--bar-h', `${bar.offsetHeight}px`);
setBarHeight();
window.addEventListener('resize', setBarHeight);

function route() {
  if (!DATA) return;
  const parts = location.hash.replace(/^#\/?/, '').split('/').map(decodeURIComponent);
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

// The newest scorecard audit for a package: "16/25 met", or nothing when it has not
// been graded yet. Pages live beside the gallery in the docs site.
const scoreText = (s) => (s.score ? `${s.score.meets}/${s.score.applicable} met` : '');
const scoreHref = (s) => `../scorecard/systems/${encodeURIComponent(s.slug)}/`;

function card(s) {
  const strips = Object.values(s.swatches).map(strip).join('');
  return `<a class="card" href="#/${esc(s.slug)}">
    <div class="cover ${portrait(s) ? 'portrait' : ''}"><img loading="lazy" src="${url(s.cover.thumb)}" alt="${esc(s.name)} screenshot"><div class="badges">${themeBadges(s)}</div></div>
    <div class="card-body">
      <div class="card-title"><h2>${esc(s.name)}</h2><span class="cat">${s.score ? `<span class="score" title="Scorecard, ${esc(s.score.date)}: ${s.score.partly} partly, ${s.score.missing} missing">${scoreText(s)}</span> · ` : ''}${esc(DATA.categories[s.category] || s.category)}</span></div>
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
    <td class="dt">${esc(scoreText(s))}</td>
    <td class="dt">${esc(s.captured)}</td></tr>`;
}

function renderIndex() {
  const all = DATA.systems;
  const list = all.filter(matches);
  const cats = Object.entries(DATA.categories).filter(([k]) => all.some((s) => s.category === k));
  delete app.dataset.pkg;
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

// Package files are fetched once per page load: Overview and Health both read the README.
const texts = new Map();
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
const plural = (n, word) => `${n} ${word}${n === 1 ? '' : 's'}`;
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
      <h1>${esc(s.name)}</h1>
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
    const spec = (t) => [t.size, t.lineHeight != null ? `/ ${cssLen(t.lineHeight)}` : '', t.weight != null ? `· ${t.weight}` : '',
      t.letterSpacing && !/^0(px|em|rem)?$/.test(t.letterSpacing) ? `· ${t.letterSpacing} tracking` : '', t.family ? `· ${t.family}` : '']
      .filter(Boolean).join(' ');
    const style = (t) => [`font-family:${stackFor(t.family)}`, t.size && `font-size:${t.size}`, t.weight != null && `font-weight:${t.weight}`,
      t.lineHeight != null && `line-height:${cssLen(t.lineHeight)}`, t.letterSpacing && `letter-spacing:${t.letterSpacing}`].filter(Boolean).join(';');
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
      ${shown.length > limit ? `<div class="more"><button class="btn" data-more>Show all ${shown.length}</button></div>` : ''}`;
    pane.querySelectorAll('[data-f]').forEach((b) => b.onclick = () => { filter = b.dataset.f; limit = PAGE; draw(); pane.querySelector(`[data-f="${filter}"]`).focus(); });
    pane.querySelectorAll('[data-i]').forEach((b) => b.onclick = () => openLightbox(shown, +b.dataset.i));
    const more = pane.querySelector('[data-more]');
    if (more) more.onclick = () => { limit = Infinity; draw(); };
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
