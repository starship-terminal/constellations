// The form a page URL is recorded in under raw/: origin and path only (a query or fragment can
// carry a signed credential, a search, an email), and every path segment that is not a plain
// route word masked as <id>, since ids and title slugs name the owner's own conversations,
// documents and projects. So https://app.example/chat/1f2e-77?q=x#m becomes
// https://app.example/chat/<id>. Favours masking: a route word is lowercase letters with at most
// one - or _ inside, 20 characters at most. Plain JavaScript, so a page.evaluate can carry it too.
// A segment right after one of these names a resource (a chat, a document, a person) however
// plain its spelling, so it is masked even when it looks like a route word (/project/my-plan).
const RESOURCE = /^(?:c|g|p|u|chat|chats|project|projects|artifact|artifacts|cowork|share|shared|doc|docs|document|documents|page|pages|file|files|folder|folders|thread|threads|conversation|conversations|task|tasks|issue|issues|notebook|notebooks|workspace|workspaces|space|spaces|team|teams|org|orgs|organization|user|users|profile|people|member|members|channel|channels|board|boards|session|sessions|course|courses|lesson|lessons|story|stories|collection|collections|dashboard|dashboards|database|databases|calendar|calendars|event|events|deck|decks|app|apps|repo|repos)$/i;

export function safeUrl(u) {
  let x;
  try { x = new URL(u); } catch { return '<url>'; }
  if (x.protocol === 'file:') return 'file:///<local file>';   // a local path names the owner's home folder
  const base = x.origin !== 'null' ? x.origin : `${x.protocol}//${x.host}`;
  const parts = x.pathname.split('/');
  return base + parts.map((s, i) => (!s || (/^[a-z]+(?:[-_][a-z]+)?$/.test(s) && s.length <= 20
    && !RESOURCE.test(parts[i - 1] || '')) ? s : '<id>')).join('/');
}
