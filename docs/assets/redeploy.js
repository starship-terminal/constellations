/* The deploy bar: appended to <body> on every docs page (via
   overrides/main.html) and on the gallery (index.html). Left is when the
   host last redeployed — the designs-trigger endpoint reads
   state/built-sha's mtime, so timer deploys count too — right is the
   Redeploy button POSTing the same endpoint.

   The POST carries X-Designs-Redeploy: a custom header, so a cross-site
   page cannot send it without a CORS preflight the trigger never grants.
   The deploy token itself is added by nginx, never by this script.

   Off kai-home-server there is no endpoint: the label falls back to this
   page's own Last-Modified (the build minute) and a click reports the
   miss. The fetch path is absolute because pages live at different depths. */
(function () {
  'use strict';
  if (document.getElementById('deploy-bar')) return;

  function fmt(d) {
    function p(n) { return (n < 10 ? '0' : '') + n; }
    return d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate()) +
      ' ' + p(d.getHours()) + ':' + p(d.getMinutes());
  }

  var bar = document.createElement('div');
  bar.id = 'deploy-bar';
  bar.innerHTML =
    '<span class="deploy-bar__when"></span>' +
    '<span class="deploy-bar__side">' +
      '<span class="deploy-bar__status" role="status"></span>' +
      '<button class="deploy-bar__button" type="button">Redeploy</button>' +
    '</span>';
  document.body.appendChild(bar);

  var when = bar.querySelector('.deploy-bar__when');
  var status = bar.querySelector('.deploy-bar__status');
  var btn = bar.querySelector('.deploy-bar__button');

  fetch('/api/redeploy', { cache: 'no-store' })
    .then(function (r) { if (!r.ok) throw new Error(String(r.status)); return r.json(); })
    .then(function (info) {
      when.textContent = 'Last redeploy ' + fmt(new Date(info.at)) +
        (info.sha ? ' · ' + String(info.sha).slice(0, 8) : '');
    })
    .catch(function () {
      when.textContent = 'Built ' + fmt(new Date(document.lastModified));
    });

  btn.addEventListener('click', function () {
    btn.disabled = true;
    status.textContent = 'queuing…';
    fetch('/api/redeploy', { method: 'POST', headers: { 'X-Designs-Redeploy': '1' } })
      .then(function (r) {
        return r.json().catch(function () { return {}; }).then(function (body) {
          status.textContent = r.status === 202
            ? 'queued: pull + deploy on the host; reload in a minute'
            : r.status === 409 ? 'already running'
            : r.status === 429 ? 'just queued; reload in a minute'
            : r.status === 404 || r.status === 501 ? (body.error || 'no endpoint on this host')
            : (body.error || 'HTTP ' + r.status);
        });
      })
      .catch(function () { status.textContent = 'no endpoint on this host'; })
      .finally(function () { btn.disabled = false; });
  });
})();
