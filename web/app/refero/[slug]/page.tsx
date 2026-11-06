// A refero style's detail page: loads the entity JSON, renders its documents
// server-side (DESIGN.md through the markdown subset, CSS/JSON through a
// small syntax tint), resolves similar styles against the index, and hands
// plain serializable props to the client surface.
import path from "node:path";
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { loadReferoEntity, loadReferoIndex } from "@/lib/refero";
import type { ReferoCard, ReferoEntity, ReferoIndex } from "@/lib/refero";
import { readRepoText } from "@/lib/catalog";
import { esc, markdown } from "@/lib/markdown";
import { ReferoDetail } from "@/components/ReferoDetail";
import type { ReferoDoc, ReferoMediaPair, ReferoSimilar } from "@/components/ReferoDetail";
import "../refero.css";

export const dynamic = "force-dynamic";

type Params = { params: Promise<{ slug: string }> };

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { slug } = await params;
  const e = await loadReferoEntity(slug);
  return { title: e?.name || "Refero" };
}

const DOC_TABS: [string, string, string][] = [
  ["design_md", "DESIGN.md", "design.md"],
  ["theme_css", "Tailwind v4", "theme.css"],
  ["variables_css", "CSS Variables", "variables.css"],
  ["tokens_json", "Design Tokens", "tokens.json"],
];

const host = (u: string | null) =>
  String(u || "")
    .replace(/^https?:\/\//, "")
    .replace(/^www\./, "")
    .replace(/\/.*$/, "");
const localMedia = (base: string, kind: string, slug: string, ext: string) =>
  `${base || "/media"}/refero-media/${kind}/${encodeURIComponent(slug)}.${ext}`;
const cdnUrl = (cdn: string, u: string | null) => (u ? (u.includes("://") ? u : `${cdn}${u}`) : null);
const faviconFor = (src: string | null) =>
  src
    ? `https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=${encodeURIComponent(`https://${host(src)}`)}&size=128`
    : null;

// Doc values are usually inline content; a repo-relative path also works.
const looksPath = (v: string) =>
  !v.includes("\n") && /^[\w./-]+\.(md|markdown|css|json|txt)$/i.test(v.trim());

// A path value is read only from the style's own refero/<slug>/ folder; the
// snapshot is third-party data, so it must not name any other repo file.
const ownDocPath = (slug: string, v: string): string | null => {
  const p = path.posix.normalize(v.trim().replace(/^\/+/, ""));
  return /^[a-z0-9][a-z0-9-]*$/i.test(slug) && p.startsWith(`refero/${slug}/`) ? p : null;
};

// The code-pane tint from app.js: whole-token matches, not a parser. CSS gets
// custom-property/at-rule/string/comment colours, JSON gets key/string/atom.
function codeHtml(text: string, key: string): string {
  if (key === "tokens_json") {
    return esc(text)
      .split("\n")
      .map((l) =>
        l
          .replace(/^(\s*)(&quot;.*?&quot;)(\s*:)/, '$1<span class="tk-h">$2</span>$3')
          .replace(/(:\s*)(&quot;.*?&quot;)/, '$1<span class="tk-s">$2</span>')
          .replace(/(:\s*)(-?[\d.]+|true|false|null)/, '$1<span class="tk-n">$2</span>'),
      )
      .join("\n");
  }
  return esc(text)
    .replace(/(--[\w-]+)(\s*:)/g, '<span class="tk-h">$1</span>$2')
    .replace(/@[\w-]+/g, '<span class="tk-q">$&</span>')
    .replace(/(&quot;.*?&quot;|&#39;.*?&#39;)/g, '<span class="tk-s">$1</span>')
    .replace(/(\/\*[\s\S]*?\*\/)/g, '<span class="tk-m">$1</span>');
}

async function renderDocs(e: ReferoEntity): Promise<ReferoDoc[]> {
  const out: ReferoDoc[] = [];
  for (const [key, label, file] of DOC_TABS) {
    const v = e.docs?.[key];
    if (!v) continue;
    const own = looksPath(v) ? ownDocPath(e.slug, v) : null;
    const raw = own ? ((await readRepoText(own)) ?? v) : v;
    out.push({
      key,
      label,
      file,
      raw,
      code: key !== "design_md",
      html:
        key === "design_md"
          ? markdown(raw, { base: `refero/${e.slug}/DESIGN.md` })
          : codeHtml(raw, key),
    });
  }
  return out;
}

function cardMedia(index: ReferoIndex, s: ReferoCard): { img: ReferoMediaPair; fav: ReferoMediaPair } {
  return {
    img: {
      local: s.card ? localMedia(index.mediaBase, s.card === "p" ? "posters" : "shots", s.slug, "jpg") : null,
      remote: cdnUrl(index.cdn, s.cardRemote),
    },
    fav: { local: localMedia(index.mediaBase, "favicons", s.slug, "png"), remote: faviconFor(s.src) },
  };
}

// The similar list the entity carries, filled out to six with same-facet
// styles the way app.js's rfSimilar did (type + style + theme matches win).
function similarItems(e: ReferoEntity, index: ReferoIndex): ReferoSimilar[] {
  const bySlug = new Map(index.styles.map((s) => [s.slug, s]));
  const items: ReferoSimilar[] = (e.similar || []).map((x) => {
    const card = x.slug ? bySlug.get(x.slug) : undefined;
    const media = card ? cardMedia(index, card) : { img: null, fav: null };
    return { slug: card ? card.slug : null, name: x.name || card?.name || x.slug, why: x.why, ...media };
  });
  const have = new Set(items.map((i) => i.slug).concat([e.slug]));
  const fill = index.styles
    .filter((s) => !have.has(s.slug))
    .map((s) => ({
      s,
      sc: Number(!!e.type && s.type === e.type) + Number(!!e.style && s.style === e.style) + Number(!!e.theme && s.theme === e.theme),
    }))
    .filter((x) => x.sc > 0)
    .sort((a, b) => b.sc - a.sc || String(a.s.name).localeCompare(String(b.s.name)))
    .slice(0, Math.max(0, 6 - items.length))
    .map(({ s }) => ({ slug: s.slug, name: s.name, why: s.tagline, ...cardMedia(index, s) }));
  return items.concat(fill);
}

export default async function ReferoEntityPage({ params }: Params) {
  const { slug } = await params;
  const e = await loadReferoEntity(slug);
  if (!e) notFound();
  const [docs, index] = await Promise.all([renderDocs(e), loadReferoIndex()]);
  return <ReferoDetail entity={e} docs={docs} similar={similarItems(e, index)} />;
}
