"""Build the docs site: render docs/**/*.md into site/ with the site's chrome.

    python3 tools/site.py              write site/ (run tools/scorecard.py first)

Replaces the Zensical/Material build with a small static renderer: every page is
one markdown file wrapped in the same bar the web app uses — a fixed left rail
with the mark, the site nav, the section's own links, and the Settings link,
ds-theme toggle and collapse toggle at its foot — plus the
Settings page (settings/, its Preferences hold the app icon). site/ is
gitignored; the home-server deployment serves it. The gallery and its chat live
only in the Next.js app (web/), which the docs site never ships — it shows the
captures.
"""
import argparse
import html
import json
import os
import posixpath
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scorecard  # noqa: E402
from catalog import atomic_write  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "site"

MD_EXTENSIONS = ["extra", "admonition", "toc", "sane_lists"]
MD_CONFIGS = {"toc": {"permalink": "#", "toc_depth": "2-4"}}

DESCRIPTION = ("A private library of design styles captured from real products: measured tokens, "
               "components and screenshots, plus the scorecard grading each capture.")
COPYRIGHT = "Private study notes. Products and trademarks belong to their owners."



def mark_svg() -> str:
    """The bar's mark: the Flat favicon (docs/assets/favicon.svg) inline at 18 px,
    then an empty span the Glass app icon paints from CSS (assets/app-icon.js
    picks which shows). The clip path's id is namespaced so it cannot collide
    with an id on the page. web/components/Rail.tsx draws the same mark."""
    svg = (DOCS / "assets" / "favicon.svg").read_text().strip()
    svg = svg.replace('id="c"', 'id="ds-mark-clip"').replace("url(#c)", "url(#ds-mark-clip)")
    svg = svg.replace("<svg ", '<svg class="mark" width="18" height="18" aria-hidden="true" ', 1)
    return svg + '<span class="mark mark-glass" aria-hidden="true"></span>'


MARK_SVG = mark_svg()
# The Flat set, the default. assets/app-icon.js swaps these for the Glass set
# when that is the stored preference, so it must load right after them.
ICON_LINKS = ('<link rel="icon" href="{rel}assets/icons/favicon.ico" sizes="32x32">\n'
              '<link rel="icon" href="{rel}assets/favicon.svg" type="image/svg+xml">\n'
              '<link rel="apple-touch-icon" href="{rel}assets/icons/apple-touch-icon.png">\n'
              '<link rel="manifest" href="{rel}site.webmanifest">\n'
              '<script src="{rel}assets/app-icon.js"></script>')
SETTINGS_SVG = ('<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true" fill="none" '
                'stroke="currentColor" stroke-width="1.4" stroke-linecap="round">'
                '<path d="M2 4.5h7M13 4.5h1M2 11.5h1M7 11.5h7"/>'
                '<circle cx="11" cy="4.5" r="2"/><circle cx="5" cy="11.5" r="2"/></svg>')
THEME_SVG = ('<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">'
             '<path d="M8 1.5a6.5 6.5 0 1 0 0 13z" fill="currentColor"/>'
             '<circle cx="8" cy="8" r="6.5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>')
COLLAPSE_SVG = ('<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true" fill="none" '
                'stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M9.5 3.5 5 8l4.5 4.5M13.5 3.5 9 8l4.5 4.5"/></svg>')


def nav_ic(inner: str) -> str:
    """A site-nav glyph, the same set web/components/Rail.tsx draws."""
    return ('<svg class="nav-ic" width="17" height="17" viewBox="0 0 16 16" aria-hidden="true" fill="none" '
            'stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">'
            f'{inner}</svg>')


NAV_ICONS = {
    "home": nav_ic('<path d="M2 6.5 8 1.5l6 5V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1z"/>'),
    "scorecard": nav_ic('<path d="M2 14V8.5M6 14V4.5M10 14v-6M14 14V2.5"/>'),
    "docs": nav_ic('<path d="M3 2.5h8a2 2 0 0 1 2 2V13a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/>'
                   '<path d="M5.5 5.5h5M5.5 8h5M5.5 10.5h3"/>'),
}

# The Settings page (settings/). Preferences are per browser, in localStorage;
# each control talks to the script that owns its store.
SETTINGS_BODY = """<h1>Settings</h1>
<p class="lede">Choices here are saved in this browser and apply to every page of the site.</p>
<h2 id="preferences">Preferences</h2>
<div class="prefs">
  <fieldset class="pref" id="app-icon">
    <legend class="pref-name">App icon</legend>
    <p class="pref-help">The icon in the browser tab, on a home screen and in the sidebar.</p>
    <div class="pref-options">
      <label class="pref-option">
        <input type="radio" name="app-icon" value="flat">
        <img src="{rel}assets/icons/icon-192.png" alt="" width="56" height="56">
        <span><strong>Flat</strong><small>Default</small></span>
      </label>
      <label class="pref-option">
        <input type="radio" name="app-icon" value="glass">
        <img src="{rel}assets/icons/glass/icon-192.png" alt="" width="56" height="56">
        <span><strong>Glass</strong><small>Rendered prism</small></span>
      </label>
    </div>
    <p class="pref-note">An app installed from this site keeps the Flat icon: its manifest is fixed when it is installed.</p>
  </fieldset>
  <fieldset class="pref" id="provider">
    <legend class="pref-name">Model provider</legend>
    <p class="pref-help">Powers the app's chat search. The key is kept by the server, never by this browser.</p>
    <p class="pf-source" id="pf-source" hidden><span class="pf-badge" id="pf-badge"></span> <span id="pf-using"></span></p>
    <p class="pf-notice" id="pf-notice" role="note" hidden></p>
    <div id="pf" hidden>
      <div class="pf-chips" role="group" aria-label="Provider template" id="pf-templates"></div>
      <div class="pf-grid">
        <label class="pf-field"><span>Base URL</span>
          <input id="pf-base" type="url" autocomplete="off" spellcheck="false" placeholder="https://api.example.com/v1"></label>
        <label class="pf-field"><span>API key</span>
          <input id="pf-key" type="password" autocomplete="off" spellcheck="false" placeholder="sk-…"></label>
        <label class="pf-field"><span>Model</span>
          <input id="pf-model" list="pf-models" autocomplete="off" spellcheck="false" disabled placeholder="test the connection first"><datalist id="pf-models"></datalist></label>
      </div>
      <p class="pf-status" id="pf-status" role="status"></p>
      <div class="pf-actions">
        <button id="pf-test" class="pf-btn" type="button">Test connection</button>
        <button id="pf-save" class="pf-btn primary" type="button">Save</button>
        <button id="pf-clear" class="pf-btn" type="button" hidden>Remove</button>
      </div>
      <p class="pref-note">The key goes to the server once: it is tested, kept there and never sent back. The template fills Base URL and the auth style. Model unlocks once a test against the endpoint succeeds, and the fetched list fills the dropdown. A saved key only goes to the endpoint it was saved with, so a new endpoint needs the key again. With no key saved, ANTHROPIC_API_KEY in the server's .env applies.</p>
    </div>
    <p id="pf-off" hidden>This copy of the site has no server, so it cannot hold a key and stores none. Set the key where the chat runs: Settings &gt; Model provider in the gallery app (<code>make dev</code>), or <code>ANTHROPIC_API_KEY</code> in that server's <code>.env</code>.</p>
  </fieldset>
</div>
<script>
  (function () {
    var TEMPLATES = {
      anthropic: { label: 'Anthropic', api: 'anthropic', base_url: 'https://api.anthropic.com', key_header: 'x-api-key' },
      openai: { label: 'OpenAI', api: 'openai', base_url: 'https://api.openai.com/v1', key_header: 'authorization' },
      gemini: { label: 'Gemini', api: 'openai', base_url: 'https://generativelanguage.googleapis.com/v1beta/openai', key_header: 'x-goog-api-key', models_url: 'https://generativelanguage.googleapis.com/v1beta/models' },
      grok: { label: 'Grok (xAI)', api: 'openai', base_url: 'https://api.x.ai/v1', key_header: 'authorization' },
      custom: { label: 'Custom', api: 'openai', base_url: '', key_header: 'authorization' }
    };
    var SOURCE = { saved: 'Saved on the server', env: 'From the server environment', none: 'No key' };
    // An older version of this page kept the whole provider, key included, in
    // localStorage under this name. Nothing writes it any more.
    var LEGACY = 'ds-provider';
    var API = '../api/';
    var el = function (id) { return document.getElementById(id); };
    var base = el('pf-base'), key = el('pf-key'), model = el('pf-model'),
        models = el('pf-models'), status = el('pf-status'), form = el('pf'), off = el('pf-off');
    var current = 'anthropic', verified = '', state = null;
    // `active` is the api/auth the test and save actually use. Picking a
    // template sets it; the saved provider restores its own, so a custom base
    // URL can't silently change the wire format on the next save.
    var active = { api: 'anthropic', key_header: 'x-api-key' };
    var sig = function () { return JSON.stringify([active.api, active.key_header, base.value.trim(), key.value]); };
    var setStatus = function (t, warn) { status.textContent = t || ''; status.dataset.warn = warn ? '1' : ''; };
    var notice = function (t) { el('pf-notice').textContent = t; el('pf-notice').hidden = !t; };
    // The model field stays locked until the exact endpoint+key pair passes a test.
    var relock = function () {
      var ok = verified && verified === sig();
      model.disabled = !ok;
      model.placeholder = ok ? 'pick or type a model' : 'test the connection first';
    };
    var send = function (method, path, body) {
      var opts = { method: method };
      if (body) { opts.headers = { 'content-type': 'application/json' }; opts.body = JSON.stringify(body); }
      return fetch(API + path, opts).then(function (r) {
        return r.json().catch(function () { return { ok: false, error: 'HTTP ' + r.status }; });
      });
    };
    function template(key_) {
      current = key_;
      var t = TEMPLATES[key_];
      active = { api: t.api, key_header: t.key_header };
      if (t.models_url) active.models_url = t.models_url;
      base.value = t.base_url;
      form.querySelectorAll('#pf-templates button').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.dataset.t === key_));
      });
    }
    Object.keys(TEMPLATES).forEach(function (k) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'pf-chip'; b.dataset.t = k; b.textContent = TEMPLATES[k].label;
      b.onclick = function () { template(k); relock(); };
      el('pf-templates').appendChild(b);
    });
    var fillModels = function (list) {
      models.innerHTML = '';
      (list || []).forEach(function (m) {
        var o = document.createElement('option');
        o.value = m.id; o.textContent = m.label || m.id;
        models.appendChild(o);
      });
    };
    [base, key].forEach(function (i) {
      i.addEventListener('input', function () { setStatus(''); fillModels([]); relock(); });
    });
    var body = function () {
      var b = { name: current, api: active.api, base_url: base.value.trim(), key_header: active.key_header,
                model: model.value.trim() };
      if (active.models_url) b.models_url = active.models_url;
      if (key.value.trim()) b.api_key = key.value.trim();
      return b;
    };
    // Show where the key comes from. The server never sends the key itself.
    function show(d) {
      state = d;
      var src = d.source || 'none', p = d.provider || {};
      el('pf-source').hidden = false;
      el('pf-source').dataset.source = src;
      el('pf-badge').textContent = SOURCE[src] || src;
      el('pf-using').textContent = d.error ? d.error : (p.model ? (TEMPLATES[p.name] || {}).label || p.name || p.api : '') + (p.model ? ' · ' + p.model : 'The chat needs a key before it can answer.');
      el('pf-clear').hidden = src !== 'saved';
      key.placeholder = src === 'saved' ? 'leave blank to keep the saved key' : 'sk-…';
    }
    function fill(d) {
      var p = d.source === 'saved' ? d.provider : null;
      if (!p) { template('anthropic'); relock(); return; }
      var match = Object.keys(TEMPLATES).find(function (k) {
        return TEMPLATES[k].api === p.api && TEMPLATES[k].base_url === p.base_url;
      });
      template(match || (TEMPLATES[p.name] ? p.name : 'custom'));
      active = { api: p.api || 'openai', key_header: p.key_header || (p.api === 'anthropic' ? 'x-api-key' : 'authorization') };
      if (p.models_url) active.models_url = p.models_url;
      base.value = p.base_url || base.value; key.value = '';
      model.value = p.model || ''; verified = sig(); relock();
    }
    el('pf-test').onclick = function () {
      if (!base.value.trim()) { setStatus('Base URL first.', true); return; }
      if (!key.value.trim() && (!state || state.source === 'none')) { setStatus('API key first.', true); return; }
      var submitted = sig();
      setStatus('Testing…');
      el('pf-test').disabled = true;
      send('POST', 'provider/test', body())
        .then(function (d) {
          // Only the pair actually tested may unlock the model field; a field
          // edited mid-flight invalidates this reply.
          if (sig() !== submitted) { setStatus('Fields changed during the test — test again.', true); return; }
          if (d.ok) {
            verified = submitted;
            fillModels(d.models);
            setStatus(d.models && d.models.length ? 'Connected: ' + d.models.length + ' models found.' : 'Connected. ' + (d.note || 'Type the model name.'));
            relock();
            if (d.models && d.models.length && !model.value) model.value = d.models[0].id;
          } else { setStatus(d.error || 'Test failed.', true); }
        })
        .catch(function () { setStatus('No answer from the server.', true); })
        .finally(function () { el('pf-test').disabled = false; });
    };
    // The whole form as it would be sent, to tell whether it changed while a
    // save was in flight.
    var formSig = function () { return JSON.stringify([current, sig(), model.value]); };
    el('pf-save').onclick = function () {
      if (!verified || verified !== sig()) { setStatus('Test the connection before saving.', true); return; }
      if (!model.value.trim()) { setStatus('Pick a model first.', true); return; }
      setStatus('Saving…');
      var submitted = formSig(), label = TEMPLATES[current].label + ' · ' + model.value.trim();
      send('POST', 'provider', body()).then(function (d) {
        if (!d.ok) { setStatus('Not saved. ' + (d.error || 'The server refused it.'), true); return; }
        show(d);
        var note = d.verified === false ? '. This endpoint has no model list, so the key itself was not checked.' : '';
        // A reply that lands after the reader edited the form must not empty
        // the key they typed since or reset what they changed.
        if (formSig() !== submitted) {
          setStatus('Saved on the server: ' + label + note + '. The form has changed since; save again to use the changes.');
          return;
        }
        key.value = ''; verified = sig(); relock();
        setStatus('Saved on the server: ' + label + note);
      }).catch(function () { setStatus('No answer from the server.', true); });
    };
    el('pf-clear').onclick = function () {
      send('DELETE', 'provider').then(function (d) {
        if (!d.ok) { setStatus(d.error || 'Could not remove the saved key.', true); return; }
        show(d); fill(d);
        setStatus(d.source === 'env' ? 'Removed the saved key. The chat now uses the server environment key.' : 'Removed the saved key.');
      }).catch(function () { setStatus('No answer from the server.', true); });
    };
    var legacy = null;
    try { legacy = JSON.parse(localStorage.getItem(LEGACY) || 'null'); } catch (e) { legacy = null; }
    var hadKey = !!(legacy && typeof legacy === 'object' && typeof legacy.api_key === 'string' && legacy.api_key);
    var drop = function () { try { localStorage.removeItem(LEGACY); } catch (e) {} };
    // POST to the API and keep the status: only a JSON answer below 500 is
    // the server's decision.
    var post = function (path, body) {
      return fetch(API + path, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) })
        .then(function (r) {
          return r.json().then(function (d) { return { status: r.status, d: d }; },
                               function () { return { status: r.status, d: null }; });
        });
    };
    // Move a key an older version left in this browser to the server once.
    // The browser copy is deleted once the server has decided (saved it, kept
    // its own, refused the body or failed the key's test) and kept when it
    // did not answer, answered 5xx or not in JSON: a restarting API must not
    // cost the only copy, and the next visit tries again.
    function migrate() {
      if (!hadKey) { drop(); return Promise.resolve(); }
      // migrate: the server saves it only when it has no provider yet, so an
      // old browser never replaces a newer key.
      var b = { api_key: legacy.api_key, migrate: true };
      ['name', 'api', 'base_url', 'key_header', 'models_url', 'model'].forEach(function (k) {
        if (typeof legacy[k] === 'string' && legacy[k]) b[k] = legacy[k];
      });
      return post('provider', b).catch(function () { return { status: 0, d: null }; })
        .then(function (res) {
          var d = res.d && typeof res.d === 'object' ? res.d : null;
          if (!d || res.status >= 500 || res.status === 0) {
            notice('The server did not answer, so the API key this browser had saved stays here for now. It moves to the server on a later visit.');
            return;
          }
          drop();
          notice(d.ok ? 'Moved the API key this browser had saved to the server. This browser no longer stores it.'
            : d.existing ? 'Deleted the API key this browser had saved. The server already has, or had, its own saved key, so it kept its own setting.'
            : 'Deleted the API key this browser had saved. The server did not keep it (' +
              String(d.error || 'it did not say why').split(legacy.api_key).join('[redacted]') + '), so enter it again below.');
        });
    }
    // The API exists only where a server answers /api/ (the gallery app, or
    // the home server's Python API behind nginx). A 404 means this copy has
    // none (GitHub Pages): nothing can hold a key here, the form stays hidden,
    // and an old browser key is deleted without being sent anywhere. Any other
    // failure (no answer, a 502 while the API restarts) keeps that key.
    fetch(API + 'provider').then(function (r) {
      return r.json().then(function (d) { return { status: r.status, d: d }; },
                           function () { return { status: r.status, d: null }; });
    }, function () { return { status: 0, d: null }; }).then(function (res) {
      if (res.d && typeof res.d.source === 'string') {
        form.hidden = false;
        return migrate().then(function () { return send('GET', 'provider'); }).then(function (d2) { show(d2); fill(d2); });
      }
      form.hidden = true; off.hidden = false;
      if (res.status !== 404) {
        if (hadKey) notice('The server did not answer, so the API key this browser had saved stays here for now.');
        return;
      }
      if (legacy !== null) {
        drop();
        if (hadKey) notice('Deleted an API key an older version of this page had saved in this browser. This copy of the site keeps no key.');
      }
    }).catch(function () { setStatus('No answer from the server.', true); });
  })();
</script>
<script>
  (function () {
    var radios = document.querySelectorAll('input[name="app-icon"]');
    function sync() {
      for (var i = 0; i < radios.length; i++) radios[i].checked = radios[i].value === dsAppIcon.get();
    }
    for (var i = 0; i < radios.length; i++) {
      radios[i].addEventListener('change', function (e) { dsAppIcon.set(e.target.value); });
    }
    document.addEventListener('ds-icon-change', sync);
    sync();
  })();
</script>"""

FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
HIDE_RE = re.compile(r"^\s*-\s*(navigation|toc)\s*$", re.M)
HEADING_RE = re.compile(r"^#\s+(.+)$", re.M)
TAG_RE = re.compile(r"<[^>]+>|\*\*|__|`")
LINK_RE = re.compile(r'href="([^"#]+\.md)(#[^"]*)?"')
SCHEME_RE = re.compile(r"^([a-zA-Z][a-zA-Z0-9+.-]*:|//)")


def frontmatter(md: str) -> tuple[set[str], str]:
    """Split a leading --- block off. Returns (hidden chrome names, markdown body)."""
    m = FRONT_RE.match(md)
    if not m:
        return set(), md
    return set(HIDE_RE.findall(m.group(1))), md[m.end():]


def page_title(md: str, stem: str) -> str:
    """The first h1's text, or the filename for pages that open on raw HTML."""
    m = HEADING_RE.search(md)
    if not m:
        return stem
    return TAG_RE.sub("", m.group(1)).strip()


def rewrite_links(rendered: str, page: "Page") -> str:
    """Point markdown links at the dir-style URLs the build emits.

    A link such as `../criteria.md` is relative to the source file, so resolve
    it inside docs/ first, map it to the target's output dir URL, then write it
    relative to this page's output URL. Links with a scheme or host (https://,
    //host, mailto:) are external and left alone.
    """
    src_dir = str(page.src.parent.relative_to(DOCS))
    page_dir = page.url or "."

    def repl(m: re.Match) -> str:
        path, frag = m.group(1), m.group(2) or ""
        if SCHEME_RE.match(path):
            return m.group(0)
        target = posixpath.normpath(path.lstrip("/") if path.startswith("/")
                                    else posixpath.join(src_dir, path))
        stem = target[:-len(".md")]
        if stem == "index" or stem.endswith("/index"):
            url = stem[:-len("index")]
        else:
            url = stem + "/"
        out = posixpath.relpath(url or ".", page_dir)
        if not out.endswith("/"):
            out += "/"
        return f'href="{out}{frag}"'
    return LINK_RE.sub(repl, rendered)


class Page:
    def __init__(self, src: Path, url: str, section: str | None):
        self.src = src          # docs/… .md file
        self.url = url          # site-relative dir URL: '', 'scorecard/', 'DESIGN-SYSTEM/'
        self.section = section  # 'scorecard', 'docs' or None


def url_of(src: Path) -> str:
    """The site-relative dir URL a source page lands on (foo/index.md -> foo/)."""
    parts = src.relative_to(DOCS).with_suffix("").parts
    if parts[-1] == "index":
        parts = parts[:-1]
    return "/".join(parts) + "/" if parts else ""


def pages() -> list[Page]:
    out = [Page(DOCS / "index.md", "", None)]
    out += [Page(DOCS / path, url_of(DOCS / path), "docs") for _, path in scorecard.LIBRARY_DOCS]
    out += [Page(p, url_of(p), "scorecard") for p in sorted((DOCS / "scorecard").rglob("*.md"))]
    return out


def newest_audit() -> dict:
    """The newest scorecard snapshot. scorecard.load() parses every snapshot,
    so build() calls this once and hands the result to every page."""
    _, audits = scorecard.load()
    return audits[-1]


def rail(page: Page, rel: str, audit: dict | None = None) -> str:
    """The section's own links, rendered inside the side rail below the site nav.
    `audit` is the newest snapshot; loaded when not given."""
    if page.section == "scorecard":
        audit = audit or newest_audit()
        items = [("Overview", "scorecard/")]
        items += [(scorecard.short(s), f"scorecard/systems/{s['slug']}/")
                  for s in scorecard.ranked(audit["systems"])]
        items += [("Criteria and method", "scorecard/criteria/"), ("Changelog", "scorecard/changelog/")]
    else:
        items = [(title, f"{Path(path).stem}/") for title, path in scorecard.LIBRARY_DOCS]
    links = ""
    for title, url in items:
        current = ' aria-current="page"' if url == page.url else ""
        links += f'<a href="{rel}{url}"{current}>{html.escape(title)}</a>'
    return f'<aside class="rail"><nav aria-label="Section">{links}</nav></aside>'


def render(page: Page, rendered: str, hidden: set[str], audit: dict | None = None) -> str:
    rel = "../" * page.url.count("/")
    home = rel if rel else "./"
    current = lambda sec: ' aria-current="page"' if page.section == sec or (sec == "home" and not page.url) else ""
    body = f'<main class="doc">{rendered}</main>'
    section = rail(page, rel, audit) if page.section and "navigation" not in hidden else ""
    nav = [(home, "Home", "home", current("home")),
           (f"{rel}scorecard/", "Scorecard", "scorecard", current("scorecard")),
            (f"{rel}DESIGN-SYSTEM/", "Docs", "docs", current("docs"))]
    nav = "\n      ".join(f'<a href="{href}"{cur}>{NAV_ICONS[key]}<span>{label}</span></a>'
                          for href, label, key, cur in nav)
    return f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page.title)} · Design systems</title>
<meta name="description" content="{html.escape(DESCRIPTION)}">
{ICON_LINKS.format(rel=rel)}
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#fafafa">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#08090a">
<meta name="apple-mobile-web-app-title" content="Design">
<link rel="stylesheet" href="{rel}stylesheets/site.css">
<link rel="stylesheet" href="{rel}stylesheets/scorecard.css">
<script>
  try {{
    document.documentElement.dataset.theme = localStorage.getItem('ds-theme') || 'dark';
    if (localStorage.getItem('ds-nav') === 'collapsed') document.documentElement.dataset.nav = 'collapsed';
  }} catch (e) {{ document.documentElement.dataset.theme = 'dark'; }}
</script>
</head>
<body>
<header class="bar">
  <a class="brand" href="{home}">
    {MARK_SVG}
    <span>Design systems</span>
  </a>
  <div class="bar-body">
    <nav class="site-nav" aria-label="Site">
      {nav}
    </nav>
{section}
  </div>
  <span class="bar-foot">
    <a class="icon-btn" href="{rel}settings/" aria-label="Settings" title="Settings"{current("settings")}>
      {SETTINGS_SVG}<span class="lbl">Settings</span>
    </a>
    <button id="theme" class="icon-btn" type="button" aria-label="Toggle colour theme" title="Toggle theme">
      {THEME_SVG}<span class="lbl">Theme</span>
    </button>
    <button id="nav-toggle" class="icon-btn" type="button" aria-pressed="false" title="Collapse sidebar">
      {COLLAPSE_SVG}<span class="lbl">Collapse</span>
    </button>
  </span>
</header>
{body}
<footer class="foot"><p>{html.escape(COPYRIGHT)}</p></footer>
<script src="{rel}assets/redeploy.js" defer></script>
<script>
  /* The theme toggle shares the gallery's ds-theme store, so a choice made on
     either side carries over. */
  document.getElementById('theme').onclick = function () {{
    var root = document.documentElement;
    var current = root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    root.dataset.theme = current === 'dark' ? 'light' : 'dark';
    try {{ localStorage.setItem('ds-theme', root.dataset.theme); }} catch (e) {{}}
  }};
  /* The collapse toggle pins the rail to an icon column (ds-nav, shared with
     the gallery); collapsed it still opens on hover or focus, per the CSS. */
  var navToggle = document.getElementById('nav-toggle');
  var syncNavToggle = function () {{
    var collapsed = document.documentElement.dataset.nav === 'collapsed';
    navToggle.setAttribute('aria-pressed', String(collapsed));
    navToggle.title = collapsed ? 'Expand sidebar' : 'Collapse sidebar';
    var lbl = navToggle.querySelector('.lbl');
    if (lbl) lbl.textContent = collapsed ? 'Expand' : 'Collapse';
  }};
  navToggle.onclick = function (e) {{
    var root = document.documentElement;
    if (root.dataset.nav === 'collapsed') {{
      delete root.dataset.nav;
      try {{ localStorage.removeItem('ds-nav'); }} catch (e) {{}}
    }} else {{
      root.dataset.nav = 'collapsed';
      try {{ localStorage.setItem('ds-nav', 'collapsed'); }} catch (e) {{}}
    }}
    // A pointer click leaves focus inside the rail, whose :focus-within would
    // hold the collapsed strip open after the cursor leaves — blur it back
    // out. Keyboard activation (detail 0) keeps focus so the rail stays usable.
    if (e.detail) navToggle.blur();
    syncNavToggle();
  }};
  syncNavToggle();
</script>
</body>
</html>
"""


def dashboard(catalog: dict | None = None, audit: dict | None = None,
              refero: int | None = None) -> str:
    """The home page body: a roll-up of the library instead of links to it —
    counts, the newest audit's grade distribution, recent captures, what most
    needs work, and category coverage. Same content either build: it shows
    only what the published scorecard pages already say. Arguments default to
    the repository's data so tests can drive it with fixed input."""
    if audit is None:
        audit = newest_audit()
    catalog = catalog or json.loads((ROOT / "catalog.json").read_text())
    systems = catalog["systems"]
    if refero is None:
        refero = sum(1 for d in (ROOT / "refero").iterdir()
                     if d.is_dir() and not d.name.startswith("."))
    cats = catalog.get("categories", {})

    tally = {"meets": 0, "partly": 0, "missing": 0}
    worst = []
    for s in audit["systems"]:
        grades = s.get("grades", {})
        counts = {g: sum(1 for v in grades.values() if v["grade"] == g) for g in tally}
        for g in tally:
            tally[g] += counts[g]
        if counts["missing"] or counts["partly"]:
            worst.append((counts["missing"], counts["partly"], s["name"]))
    total = sum(tally.values()) or 1
    bar = "".join(
        f'<i class="dash-{g}" style="flex:{tally[g]}" title="{tally[g]} {g}"></i>'
        for g in ("meets", "partly", "missing"))
    worst.sort(key=lambda x: (-x[0], -x[1], x[2]))

    recent = sorted(systems, key=lambda s: (s.get("captured") or "", s["name"]), reverse=True)[:6]
    dark = sum(1 for s in systems if any("dark" in t for t in s.get("themes", [])))

    def row(li): return f'<li><span>{html.escape(li[0])}</span><b>{li[1]}</b></li>'
    return f"""<div class="dash">
  <div class="dash-stats">
    <div><b>{len(systems)}</b><span>systems</span></div>
    <div><b>{refero:,}</b><span>refero styles</span></div>
    <div><b>{len(cats)}</b><span>categories</span></div>
    <div><b>{dark}</b><span>with a dark theme</span></div>
    <div><b>{html.escape(str(audit.get("rubric", "—")))}</b><span>rubric · {html.escape(audit["date"])}</span></div>
  </div>
  <h2>Health</h2>
  <div class="dash-bar">{bar}</div>
  <p class="dash-note">{100 * tally["meets"] // total}% of graded criteria met —
     {tally["meets"]} met, {tally["partly"]} partial, {tally["missing"]} missing.</p>
  <div class="dash-cols">
    <section><h3>Newest captures</h3><ul>
      {"".join(row((s["name"], s.get("captured") or "—")) for s in recent)}
    </ul></section>
    <section><h3>Needs attention</h3><ul>
      {"".join(row((n, f"{m} missing" + (f" · {p} partial" if p else ""))) for m, p, n in worst[:8]) or "<li>nothing missing</li>"}
    </ul></section>
  </div>
  <h2>Coverage</h2>
  <div class="dash-chips">
    {"".join(f'<span class="dash-chip"><b>{html.escape(v)}</b> {sum(1 for s in systems if s["category"] == k)}</span>' for k, v in cats.items())}
  </div>
</div>"""


def build() -> None:
    import markdown

    # site/ is fully generated; start clean so removed pages and assets leave.
    shutil.rmtree(OUT, ignore_errors=True)
    statics = ["assets", "stylesheets", "site.webmanifest"]
    for name in statics:
        src, dst = DOCS / name, OUT / name
        if not src.exists():
            continue
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    audit = newest_audit()  # once: every scorecard page's rail and the home dashboard
    count = 0
    for page in pages():
        if not page.src.exists():
            continue
        hidden, md = frontmatter(page.src.read_text())
        page.title = page_title(md, page.src.stem)
        body = rewrite_links(markdown.markdown(md, extensions=MD_EXTENSIONS, extension_configs=MD_CONFIGS), page)
        if not page.url:
            body += dashboard(audit=audit)
        dest = OUT / page.url / "index.html" if page.url else OUT / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        atomic_write(dest, render(page, body, hidden, audit))
        count += 1

    settings = Page(DOCS / "index.md", "settings/", "settings")
    settings.title = "Settings"
    (OUT / "settings").mkdir(parents=True, exist_ok=True)
    atomic_write(OUT / "settings" / "index.html",
                 render(settings, SETTINGS_BODY.replace("{rel}", "../"), {"navigation"}))
    count += 1

    # A 404 is served at the missing URL, whatever its depth, so the page's
    # relative links would resolve inside the missing directory. A <base>
    # before the stylesheet links points them at the site root, where the
    # site sits on the deploy host.
    not_found = Page(DOCS / "index.md", "", None)
    not_found.title = "Page not found"
    html_404 = render(not_found, "<h1>Page not found</h1><p><a href='./'>Back to the library home</a>.</p>",
                      {"navigation"}).replace("<head>", '<head>\n<base href="/">', 1)
    atomic_write(OUT / "404.html", html_404)
    print(f"site: wrote {count} pages to {os.path.relpath(OUT, ROOT)}/")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.parse_args()
    build()


if __name__ == "__main__":
    main()
