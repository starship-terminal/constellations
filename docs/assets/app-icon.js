/* The app icon preference (Settings > Preferences): Flat, the default, or
   Glass. It swaps the tab favicon, the touch icon and the sidebar's mark, and
   is stored in localStorage under ds-icon next to ds-theme.

   Every page's <head> links the Flat set, then loads this file synchronously,
   so a stored Glass choice replaces those links and sets <html data-icon>
   before the first paint. The web app manifest is static: an installed app
   keeps the Flat icon whatever is chosen here. Paths resolve against this
   file, so it works from any page depth and behind the 404 page's <base>. */
(function () {
  'use strict';
  var KEY = 'ds-icon';
  var DEFAULT = 'flat';
  var base = new URL('.', document.currentScript.src).href;
  var SETS = {
    flat: [
      { rel: 'icon', href: 'icons/favicon.ico', sizes: '32x32' },
      { rel: 'icon', href: 'favicon.svg', type: 'image/svg+xml' },
      { rel: 'apple-touch-icon', href: 'icons/apple-touch-icon.png' }
    ],
    glass: [
      { rel: 'icon', href: 'icons/glass/favicon-16.png', type: 'image/png', sizes: '16x16' },
      { rel: 'icon', href: 'icons/glass/favicon-32.png', type: 'image/png', sizes: '32x32' },
      { rel: 'icon', href: 'icons/glass/favicon-48.png', type: 'image/png', sizes: '48x48' },
      { rel: 'apple-touch-icon', href: 'icons/glass/apple-touch-icon.png' }
    ]
  };

  function stored() {
    try { var v = localStorage.getItem(KEY); return Object.hasOwn(SETS, v) ? v : DEFAULT; } catch (e) { return DEFAULT; }
  }

  function apply(name) {
    var head = document.head;
    var old = head.querySelectorAll('link[rel="icon"], link[rel="apple-touch-icon"]');
    var anchor = old.length ? old[old.length - 1].nextSibling : null;
    // Remove before inserting: Chrome re-picks the tab icon when a link is
    // added, not when one is removed, so the old set must be gone by then.
    for (var i = 0; i < old.length; i++) old[i].remove();
    SETS[name].forEach(function (spec) {
      var link = document.createElement('link');
      link.rel = spec.rel;
      link.href = base + spec.href;
      if (spec.type) link.type = spec.type;
      if (spec.sizes) link.setAttribute('sizes', spec.sizes);
      head.insertBefore(link, anchor);
    });
    document.documentElement.dataset.icon = name;
  }

  var current = stored();
  // The markup already carries Flat, so only Glass needs the links replaced.
  if (current === DEFAULT) document.documentElement.dataset.icon = DEFAULT;
  else apply(current);

  window.dsAppIcon = {
    options: Object.keys(SETS),
    get: function () { return current; },
    set: function (name) {
      if (!Object.hasOwn(SETS, name) || name === current) return;
      current = name;
      try { localStorage.setItem(KEY, name); } catch (e) {}
      apply(name);
      document.dispatchEvent(new CustomEvent('ds-icon-change', { detail: name }));
    }
  };

  // Another tab changed it: follow along.
  window.addEventListener('storage', function (e) {
    if (e.key !== KEY) return;
    var next = stored();
    if (next === current) return;
    current = next;
    apply(next);
    document.dispatchEvent(new CustomEvent('ds-icon-change', { detail: next }));
  });
})();
