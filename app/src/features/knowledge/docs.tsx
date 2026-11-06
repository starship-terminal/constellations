import Link from "next/link";
import { notFound } from "next/navigation";
import {
  listLibraryDocuments,
  readLibraryDocument,
} from "@/server/knowledge/docs";
import { DocumentMarkdown } from "./markdown";
import styles from "./knowledge.module.css";
export async function DocsIndex() {
  const docs = await listLibraryDocuments();
  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <h1>Library docs</h1>
        <p>
          How captures are made, what evidence supports a value, and how to use
          the library.
        </p>
      </header>
      <div className={styles.grid}>
        {docs.map((doc) => (
          <Link
            key={doc.slug}
            href={`/docs/${doc.slug}`}
            className={styles.card}
          >
            <h2>{doc.title}</h2>
            <p>{doc.excerpt}</p>
            <small>{doc.slug}.md</small>
          </Link>
        ))}
      </div>
      {!docs.length && (
        <p>No library documents are available in this checkout.</p>
      )}
    </div>
  );
}
export async function DocsReader({ slug }: { slug: string }) {
  const [doc, docs] = await Promise.all([
    readLibraryDocument(slug),
    listLibraryDocuments(),
  ]);
  if (!doc) notFound();
  return (
    <div className={styles.page}>
      <div className={styles.links}>
        <Link href="/docs">All library docs</Link>
      </div>
      <div className={styles.reader}>
        <aside className={styles.sidebar}>
          <nav aria-label="Library docs">
            {docs.map((item) => (
              <Link
                key={item.slug}
                href={`/docs/${item.slug}`}
                aria-current={item.slug === slug ? "page" : undefined}
              >
                {item.title}
              </Link>
            ))}
          </nav>
        </aside>
        <article className={styles.prose}>
          <DocumentMarkdown text={doc.text} base={`docs/${slug}.md`} />
        </article>
      </div>
    </div>
  );
}
