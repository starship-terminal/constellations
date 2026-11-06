// Scorecard changelog: one entry per audit snapshot, newest first, each
// diffed against the audit before it.
import type { Metadata } from "next";
import Link from "next/link";
import { changelog, load } from "@/lib/scorecard";
import "../scorecard.css";

export const dynamic = "force-dynamic";

export function generateMetadata(): Metadata {
  return { title: "Scorecard changelog" };
}

export default function ChangelogPage() {
  let data: ReturnType<typeof load> | null = null;
  try {
    data = load();
  } catch {}
  if (!data) {
    return (
      <main className="page">
        <Link className="back" href="/scorecard">
          ← Scorecard
        </Link>
        <header className="g-hero">
          <h1>Changelog</h1>
        </header>
        <p className="empty">No audit snapshots yet.</p>
      </main>
    );
  }

  const entries = changelog(data.criteria, data.audits);

  return (
    <main className="page">
      <Link className="back" href="/scorecard">
        ← Scorecard
      </Link>
      <header className="g-hero">
        <h1>Changelog</h1>
        <p className="sub">
          Newest first. Each entry compares one audit with the one before it.
        </p>
      </header>

      {entries.map((e, i) => (
        <section key={i}>
          <h2 className="sc-layer">{e.title}</h2>
          {e.lines === null ? (
            <p className="sc-none">No grade changed.</p>
          ) : (
            <ul className="sc-log">
              {e.lines.map((line) => (
                <li key={line}>{line}</li>
              ))}
            </ul>
          )}
        </section>
      ))}
    </main>
  );
}
