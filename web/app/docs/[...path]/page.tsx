// One docs/*.md file rendered with the library's markdown subset, in the
// .docpage layout: a left rail listing every doc, the rendered doc on the
// right. /docs/index redirects to the docs index page.
import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { loadData, readRepoText } from "@/lib/catalog";
import { markdown } from "@/lib/markdown";
import { SAFE_SEG, docTitle, listDocs, stripFront } from "../docs";
import "../docs.css";

export const dynamic = "force-dynamic";

interface Props {
  params: Promise<{ path: string[] }>;
}

const fileOf = (segs: string[]) => `docs/${segs.join("/")}.md`;
const clean = (segs: string[] | undefined): segs is string[] =>
  !!segs?.length && segs.every((s) => SAFE_SEG.test(s));

async function knownSlugs(): Promise<Set<string> | undefined> {
  try {
    const data = await loadData();
    return new Set(data.systems.map((s) => s.slug));
  } catch {
    return undefined;
  }
}

export async function generateMetadata({ params }: Props) {
  const { path: segs } = await params;
  if (!clean(segs)) return {};
  const src = await readRepoText(fileOf(segs));
  if (!src) return {};
  return { title: docTitle(src) ?? segs[segs.length - 1] };
}

export default async function DocPage({ params }: Props) {
  const { path: segs } = await params;
  if (!clean(segs)) notFound();
  const slug = segs.join("/");
  if (slug === "index") redirect("/docs");
  const src = await readRepoText(fileOf(segs));
  if (!src) notFound();

  const [docs, known] = await Promise.all([listDocs(), knownSlugs()]);
  const html = markdown(stripFront(src), { base: fileOf(segs) }, known);

  return (
    <div className="page">
      <div className="docpage">
        <aside className="rail">
          <p className="group-title">docs/</p>
          <nav aria-label="Docs">
            {docs.map((d) => (
              <Link
                key={d.slug}
                href={d.slug === "index" ? "/docs" : `/docs/${d.slug}`}
                aria-current={d.slug === slug ? "page" : undefined}
              >
                {d.title}
              </Link>
            ))}
          </nav>
        </aside>
        <article className="doc">
          <div className="md" dangerouslySetInnerHTML={{ __html: html }} />
          <p className="foot">{fileOf(segs)}</p>
        </article>
      </div>
    </div>
  );
}
