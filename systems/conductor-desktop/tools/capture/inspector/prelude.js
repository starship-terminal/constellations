// PRODUCT: helpers for Conductor 0.91.2's page, used by shots.json. Found by role, aria-label and
// UI words, never by account text.
const P = window.__P = {};
const OPEN = '[role=menu], [role=dialog]:not(.conductor-toast), [role=alertdialog], [role=listbox], [data-side][data-open], [role=tooltip]';
P.hideToast = (hide = true) => {
  let st = document.getElementById('cap-hide');
  if (!st) { st = document.createElement('style'); st.id = 'cap-hide'; document.head.appendChild(st); }
  st.textContent = hide ? '.conductor-toast-viewport{display:none!important}' : '';
};
P.open = () => __cap.$(OPEN);
P.closeAll = async () => {
  for (let i = 0; i < 5 && P.open().length; i++) {
    const t = P.open().slice(-1)[0];
    __cap.key('Escape', t.contains(document.activeElement) ? document.activeElement : t);
    await __cap.sleep(300);
  }
  if (document.activeElement && document.activeElement !== document.body) document.activeElement.blur();
};
P.ready = async (toast = false, keepOpen = false) => { P.hideToast(!toast); if (!keepOpen) await P.closeAll(); };
P.inSettings = () => !!__cap.byText('Back', 'button')[0];
P.back = async () => { if (P.inSettings()) { __cap.click(__cap.byText('Back', 'button')[0]); await __cap.sleep(700); } };
P.settings = async (pane) => {
  if (!P.inSettings()) { __cap.click(document.querySelector('button[aria-label=Settings]')); await __cap.sleep(800); }
  const nav = (t, sub) => [...document.querySelectorAll('a, button')].filter(e => { const r = e.getBoundingClientRect(); return __cap.vis(e) && r.x < 250 && (!sub || r.x > 18); })
    .find(a => a.innerText.trim().split('\n').pop().trim() === t);
  // 'conductor/Misc': a repository's own pane, under the repository's entry.
  const [first, sub] = (pane || '').split('/');
  if (first) { const a = nav(first); if (!a) throw new Error('no settings pane ' + first); if (!sub || !nav(sub, true)) { __cap.click(a); await __cap.sleep(700); } }
  if (sub) { const b = nav(sub, true); if (!b) throw new Error('no settings pane ' + pane); __cap.click(b); await __cap.sleep(700); }
  P.scrollMain(0);
};
// Scroll the main settings column (the scroller that holds the h2).
P.scrollMain = (y) => {
  const h = document.querySelector('h2'); let p = h && h.parentElement;
  while (p && !(p.scrollHeight > p.clientHeight + 4 && /auto|scroll/.test(getComputedStyle(p).overflowY))) p = p.parentElement;
  if (p) p.scrollTop = y; return !!p;
};
// The scratch workspace is the only one the capture opens; Conductor named it after a city.
P.WS = 'Dalat';
P.sideText = (t, sel = 'span') => __cap.byText(t, sel).filter(e => e.getBoundingClientRect().x < 250)[0];
// The scratch repository has one workspace, so its row is the only workspace link in the sidebar (Conductor
// renames it after the first prompt).
P.wsRow = () => __cap.$('a').find(a => { const r = a.getBoundingClientRect(); return r.x < 20 && r.y > 170 && !P.inSettings(); });
P.repoRow = () => { const s = P.sideText('conductor'); return s && s.closest('div.group, div[class*=group], div'); };
P.composer = () => { const e = document.querySelector('.composer-tiptap-editor'); if (!e) return null; let p = e.parentElement; while (p && parseFloat(getComputedStyle(p).borderTopWidth) === 0) p = p.parentElement; return p; };
P.composerButtons = () => { const c = P.composer(); return c ? [...c.querySelectorAll('button')].filter(__cap.vis) : []; };
P.modelButton = () => { const l = document.querySelector('.composer-model-label'); return l && l.closest('button'); };
P.sendButton = () => P.composerButtons().slice(-1)[0];
P.addButton = () => P.composerButtons().slice(-2)[0];
P.chatTab = () => document.querySelector('[role=tablist] [role=tab]');
P.bottomTab = (t) => [...document.querySelectorAll('[role=tab]')].find(e => e.innerText.trim() === t);
// chat: 'new' opens the workspace's empty chat tab (made with the tab bar's + if there is none), 'run' the
// chat that holds the test prompts; omitted, whichever tab is open.
P.workspace = async (chat) => {
  await P.closeAll(); await P.back();
  // Home lists workspaces in the page and folds them out of the sidebar: open the scratch one from the list.
  if (!P.wsRow()) { const s = P.sideText('conductor'); if (s) { __cap.click(s.parentElement); await __cap.sleep(700); } }
  if (!P.wsRow()) { const o = __cap.$('[role=option]').find(o => o.getBoundingClientRect().x > 250); if (o) { __cap.click(o); await __cap.sleep(1000); } }
  const r = P.wsRow(); if (!r) throw new Error('no scratch workspace row');
  if (!P.composer()) { __cap.click(r); await __cap.sleep(900); }
  const chats = () => __cap.$('[role=tab]').filter(t => t.getBoundingClientRect().y < 90 && t.getBoundingClientRect().x < 1015);
  if (chat === 'new') {
    let t = chats().find(t => t.innerText.trim() === 'Untitled');
    if (!t) { const add = P.wsParts()['tab-add'](); if (!add) throw new Error('no new-chat button'); __cap.click(add); await __cap.sleep(1000); t = chats().find(t => t.innerText.trim() === 'Untitled'); }
    if (t && t.getAttribute('aria-selected') !== 'true') { __cap.click(t); await __cap.sleep(700); }
  }
  if (chat === 'run') { const t = chats().find(t => !/^(Untitled|Latest turn|README)/.test(t.innerText.trim())); if (t && t.getAttribute('aria-selected') !== 'true') { __cap.click(t); await __cap.sleep(700); } }
};
// Base UI opens tooltips and hover cards on pointer movement; script events stand in for the pointer.
P.hover = (e) => {
  const r = e.getBoundingClientRect(), o = { bubbles: true, composed: true, clientX: r.x + r.width / 2, clientY: r.y + r.height / 2, pointerType: 'mouse' };
  for (const t of ['pointerover', 'pointerenter', 'mouseover', 'mouseenter', 'pointermove', 'mousemove']) e.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, o));
};
P.unhover = (e) => { const o = { bubbles: true, composed: true, pointerType: 'mouse' }; for (const t of ['pointerout', 'pointerleave', 'mouseout', 'mouseleave']) e.dispatchEvent(new (t.startsWith('pointer') ? PointerEvent : MouseEvent)(t, o)); };
P.context = (e) => { const r = e.getBoundingClientRect(); e.dispatchEvent(new MouseEvent('contextmenu', { bubbles: true, cancelable: true, composed: true, button: 2, clientX: r.x + 20, clientY: r.y + r.height / 2 })); };
P.menuParts = () => ({ menu: P.open().filter(e => /menu|listbox|dialog/.test(e.getAttribute('role') || ''))[0] || P.open()[0],
  'menu-item': () => __cap.$('[role=menuitem], [role=option]')[1] || __cap.$('[role=menuitem], [role=option]')[0],
  'menu-item-highlighted': () => __cap.$('[role=menuitem][data-highlighted], [role=option][data-highlighted]')[0],
  'menu-separator': () => __cap.$('[role=separator]').filter(e => e.closest('[role=menu]'))[0] });
const filled = e => { const c = getComputedStyle(e).backgroundColor; return c && c !== 'rgba(0, 0, 0, 0)' && c !== 'transparent'; };
P.btnAt = (x0, x1, y0, y1) => __cap.$('button, [role=button]').find(b => { const r = b.getBoundingClientRect(); return r.x >= x0 && r.x <= x1 && r.y >= y0 && r.y <= y1; });
P.navItems = () => [...document.querySelectorAll('a, button')].filter(e => __cap.vis(e) && e.getBoundingClientRect().x < 20 && /group flex w-full/.test(e.className));
P.settingsParts = () => {
  const desc = __cap.$('div.text-sm.text-muted-foreground').filter(e => /mt-0\.5/.test(e.className))[0];
  const main = __cap.$('h2')[0];
  return {
    'settings-nav-item': P.navItems().find(e => !filled(e)), 'settings-nav-selected': P.navItems().find(filled),
    'settings-section-label': __cap.$('div.text-xs.text-muted-foreground').find(e => e.getBoundingClientRect().x < 20),
    'settings-search': __cap.$('input').find(e => e.getBoundingClientRect().x < 20),
    'settings-title': main, 'settings-row-title': desc && desc.previousElementSibling, 'settings-row-description': desc,
    'settings-row': desc && desc.parentElement && desc.parentElement.parentElement,
    select: __cap.$('[role=combobox]').find(e => e.getBoundingClientRect().x > 260),
    'switch-on': __cap.$('[role=switch][aria-checked=true], [role=switch][data-checked]')[0],
    'switch-off': __cap.$('[role=switch][aria-checked=false], [role=switch][data-unchecked]')[0],
    'button-outline': __cap.$('button').find(b => b.getBoundingClientRect().x > 260 && b.getBoundingClientRect().y > 50 && b.innerText.trim() && parseFloat(getComputedStyle(b).borderTopWidth) > 0 && !filled(b) || b.getBoundingClientRect().x > 260 && b.getBoundingClientRect().y > 50 && /border/.test(b.className) && b.innerText.trim()),
    'text-field': __cap.$('input[type=text], input:not([type]), textarea').find(e => e.getBoundingClientRect().x > 260),
    'toml-button': () => __cap.$('button').find(b => /Open settings/.test(b.innerText)),
    'back-button': () => __cap.byText('Back', 'button')[0],
  };
};
P.wsParts = () => {
  const sys = __cap.$('h3').find(h => h.getBoundingClientRect().x > 260);
  const tabs = __cap.$('[role=tab]');
  return {
    sidebar: () => { let p = P.wsRow(); while (p && p.getBoundingClientRect().width < 250) p = p.parentElement; return p; },
    'sidebar-nav-item': () => { const s = P.sideText('Home'); return s && s.closest('button, a, [role=button]') || s && s.parentElement; },
    'sidebar-section-label': () => P.sideText('My workspaces'),
    'repo-row': () => { const s = P.sideText('conductor'); return s && s.parentElement; },
    'repo-icon': () => __cap.$('div.rounded-sm').find(e => e.getBoundingClientRect().x < 20 && e.innerText.trim().length === 1),
    'workspace-row-selected': P.wsRow, 'workspace-name': () => { const r = P.wsRow(); return r && r.querySelector('span'); },
    'plan-badge': () => __cap.byText('FREE', 'div')[0],
    breadcrumb: () => P.btnAt(260, 270, 0, 20),
    'header-icon-button': () => document.querySelector('button[aria-label="Toggle left sidebar"]'),
    'chat-tab-selected': () => tabs.find(t => t.getAttribute('aria-selected') === 'true' && t.getBoundingClientRect().y < 90), 'chat-tab': () => tabs.find(t => t.getAttribute('aria-selected') !== 'true' && t.getBoundingClientRect().y < 90), 'tab-add': () => __cap.$('button').find(b => { const r = b.getBoundingClientRect(); return !b.getAttribute('role') && r.y > 40 && r.y < 60 && r.x > 260 && r.x < 1015 && b.querySelector('svg.lucide-plus'); }),
    'system-card': () => sys && sys.parentElement, 'system-line': () => __cap.$('div').find(d => /^Branched/.test(d.innerText.trim()) && d.children.length < 6),
    'mono-chip': () => __cap.$('button').find(b => b.getBoundingClientRect().x > 260 && b.getBoundingClientRect().y > 90 && b.getBoundingClientRect().y < 260 && /font-mono|mono/.test(b.innerHTML) && b.innerText.trim().length < 12),
    'suggestion-chip': () => __cap.byText('Fix a TODO', 'button')[0],
    composer: P.composer, 'composer-editor': () => document.querySelector('.composer-tiptap-editor'),
    'composer-placeholder': () => document.querySelector('.composer-tiptap-editor p.is-editor-empty, .composer-tiptap-editor [data-placeholder]'),
    'model-button': P.modelButton, 'composer-add': P.addButton, 'send-button': P.sendButton,
    'panel-tab-selected': () => __cap.byText('All files', 'button')[0], 'panel-tab': () => __cap.byText('Changes', 'button')[0] || __cap.$('button').find(b => /^Changes/.test(b.innerText.trim())),
    'count-mono': () => __cap.$('span.font-geist-mono')[0],
    'tree-row': () => __cap.$('[role=treeitem]')[1], 'tree-label': () => __cap.$('[role=treeitem] span.font-mono')[1],
    'bottom-tab-selected': () => tabs.find(t => t.getAttribute('aria-selected') === 'true' && t.getBoundingClientRect().y > 300),
    'bottom-tab': () => tabs.find(t => t.getAttribute('aria-selected') !== 'true' && t.getBoundingClientRect().y > 300),
    'empty-card': () => { const b = __cap.byText('Add run script', 'button')[0]; let p = b; while (p && !/dashed/.test(getComputedStyle(p).borderTopStyle)) p = p.parentElement; return p; },
    'empty-text': () => __cap.$('span.text-muted-foreground.text-sm.text-center')[0],
    'button-secondary': () => __cap.byText('Add run script', 'button')[0],
    'status-warning': () => __cap.$('[role=status]')[0],
    'resize-handle': () => __cap.$('[role=separator]').find(e => e.getBoundingClientRect().x > 900),
  };
};
P.pane = () => { let p = P.composer(); while (p && p.getBoundingClientRect().height < 500) p = p.parentElement; return p; };
P.inPane = (sel) => { const p = P.pane(); return p ? [...p.querySelectorAll(sel)].filter(__cap.vis).filter(e => !P.composer().contains(e)) : []; };
const bubble = (e) => { let p = e; while (p && !filled(p)) p = p.parentElement; return p; };
P.convParts = () => ({
  'user-message': () => { const s = P.inPane('span').find(e => /^Create hello/.test(e.innerText.trim())) || P.inPane('span').find(e => /^List the files/.test(e.innerText.trim())); return s && bubble(s); },
  'user-message-text': () => P.inPane('span').find(e => /^Create hello/.test(e.innerText.trim())),
  'assistant-text': () => P.inPane('p').find(e => /^Created/.test(e.innerText.trim())) || P.inPane('p')[0],
  'assistant-heading': () => P.inPane('h2')[0],
  'file-link': () => P.inPane('button').find(b => /hover:unde/.test(b.className)),
  'inline-code': () => P.inPane('code')[0],
  'tool-summary': () => P.inPane('button').find(b => /tool call/.test(b.innerText)),
  'tool-call': () => { const s = P.inPane('span').find(e => /^(List files|Write|Read)/.test(e.innerText.trim())); return s && s.parentElement; },
  'tool-arg': () => P.inPane('span.font-mono.bg-muted')[0] || P.inPane('span').find(e => /bg-muted/.test(e.className) && /font-mono/.test(e.className)),
  'message-meta': () => P.inPane('button').find(b => /\d+s · /.test(b.innerText)),
  'message-action': () => P.inPane('button').find(b => /size-5/.test(b.className)),
  'diff-chip': () => P.inPane('button').find(b => /\+\d/.test(b.innerText) && /hello/.test(b.innerText)),
  'diff-added': () => P.inPane('span.text-git-green')[0], 'diff-removed': () => P.inPane('span.text-git-red')[0],
  'focus-hint': () => __cap.$('div.rounded-full.text-xs').find(e => /to focus/.test(e.innerText)),
  'list-item': () => P.inPane('li')[0],
});
P.home = async () => { await P.closeAll(); await P.back(); const h = P.sideText('Home'); if (h) { __cap.click(h.closest('button, a, [role=button]') || h.parentElement); await __cap.sleep(900); } };
