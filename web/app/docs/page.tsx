// Docs index: one card per docs/*.md, with its title, first-paragraph
// excerpt and file name. Doc pages themselves live under docs/[...path].
import Link from "next/link";
import { listDocs } from "./docs";
import "./docs.css";

export const metadata = { title: "Docs" };
export const dynamic = "force-dynamic";

const href = (slug: string) => (slug === "index" ? "/docs" : `/docs/${slug}`);

export default async function DocsPage() {
  const docs = await listDocs();
  return (
    <div className="page">
      <div className="g-hero">
        <h1>Docs</h1>
        <p className="sub">
          The library&rsquo;s working notes: what a package holds, how captures get made, what a value&rsquo;s
          evidence label means, and what is still open.
        </p>
      </div>
      {docs.length ? (
        <div className="doc-pick dc-picks">
          {docs.map((d) => (
            <Link key={d.slug} className="dc-card" href={href(d.slug)}>
              <h2>{d.title}</h2>
              {d.excerpt ? <p>{d.excerpt}</p> : null}
              <code>{d.file}</code>
            </Link>
          ))}
        </div>
      ) : (
        <p className="empty">No docs found under docs/.</p>
      )}
    </div>
  );
}
