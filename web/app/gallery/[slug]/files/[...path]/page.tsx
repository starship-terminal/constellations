// Package file viewer: renders Markdown through the shared renderer, pretty-
// prints JSON, dumps other text in <pre>, and links binaries to the media
// route. URL shape: /gallery/<slug>/files/<repo-relative path>.
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import path from "node:path";
import { getSystem, loadData, mediaUrl, readPackageFile } from "@/lib/catalog";
import { markdown } from "@/lib/markdown";
import { CopyButton } from "@/components/CopyButton";
import "../../detail.css";

export const dynamic = "force-dynamic";

// Extensions shown as text; anything else (or anything that decodes with
// replacement characters) gets an "Open file" link instead of a garbled dump.
const TEXT_EXT = new Set([
  ".md", ".txt", ".json", ".css", ".html", ".js", ".mjs", ".ts", ".tsx", ".jsx",
  ".yml", ".yaml", ".tsv", ".csv", ".svg", ".xml", ".py", ".toml", ".sh", ".map",
]);

interface Params {
  slug: string;
  path: string[];
}

export async function generateMetadata({ params }: { params: Promise<Params> }): Promise<Metadata> {
  const { slug, path: segs } = await params;
  return { title: segs?.[segs.length - 1] ?? slug };
}

export default async function PackageFilePage({ params }: { params: Promise<Params> }) {
  const { slug, path: segs } = await params;
  const sys = await getSystem(slug);
  if (!sys || !segs?.length) notFound();

  // Links arrive repo-relative ("systems/<slug>/x.md"); readPackageFile wants
  // the path inside the package dir, so strip the prefix when it is there.
  const joined = segs.join("/");
  const prefix = `systems/${slug}/`;
  const rel = joined.startsWith(prefix) ? joined.slice(prefix.length) : joined;
  const file = rel && !rel.endsWith("/") ? await readPackageFile(slug, rel) : null;
  if (!file) notFound();

  const ext = path.posix.extname(file.rel).toLowerCase();
  const isText = TEXT_EXT.has(ext) && !/\0|\uFFFD/.test(file.text);


  let body: React.ReactNode;
  if (ext === ".md" && isText) {
    const knownSlugs = new Set((await loadData()).systems.map((s) => s.slug));
    body = (
      <article
        className="md doc pd-doc"
        dangerouslySetInnerHTML={{ __html: markdown(file.text, { base: file.rel, allowRawHtml: true }, knownSlugs) }}
      />
    );
  } else if (ext === ".json" && isText) {
    let pretty = file.text;
    try {
      pretty = JSON.stringify(JSON.parse(file.text), null, 2);
    } catch {}
    body = <pre className="pd-pre">{pretty}</pre>;
  } else if (isText) {
    body = <pre className="pd-pre">{file.text}</pre>;
  } else {
    body = (
      <p>
        <a className="btn" href={mediaUrl(file.rel)} target="_blank" rel="noopener">
          Open file ↗
        </a>
      </p>
    );
  }

  return (
    <div className="page">
      <Link className="back" href={`/gallery/${sys.slug}`}>
        ← {sys.name}
      </Link>
      <header className="pkg-head">
        <div className="pd-doc-head">
          <h1>{path.posix.basename(file.rel)}</h1>
          {isText && <CopyButton text={file.text} label="Copy" />}
        </div>
        <p className="pd-path">{file.rel}</p>
      </header>
      {body}
    </div>
  );
}
