// Per-system scorecard report: rank, grade counts, a proportional bar and
// every criterion row grouped by layer.
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { GRADES, load, short, systemReport } from "@/lib/scorecard";
import type { GradeValue } from "@/lib/scorecard";
import "../scorecard.css";

export const dynamic = "force-dynamic";

const GRADE_KEYS = Object.keys(GRADES) as GradeValue[];
// Evidence longer than this folds behind a <details> to keep the table tidy.
const EV_LEN = 110;

type Props = { params: Promise<{ slug: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  try {
    const { audits } = load();
    const sys = audits[audits.length - 1].systems.find((s) => s.slug === slug);
    if (sys) {
      return { title: short(sys) };
    }
  } catch {}
  return { title: "Scorecard" };
}

export default async function SystemPage({ params }: Props) {
  const { slug } = await params;
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
        <p className="empty">No audit snapshots yet.</p>
      </main>
    );
  }

  const { criteria, audits } = data;
  const audit = audits[audits.length - 1];
  const system = audit.systems.find((s) => s.slug === slug);
  if (!system) {
    notFound();
  }
  const report = systemReport(criteria, audit, slug);
  const n = report.counts;

  return (
    <main className="page">
      <Link className="back" href="/scorecard">
        ← Scorecard
      </Link>
      <header className="pkg-head">
        <h1>{short(system)}</h1>
        <div className="pkg-sub">
          <span>
            Rank {report.rank} of {report.total}
          </span>
          <span>{system.category}</span>
          <span>platform: {report.platform}</span>
          <span>captured {system.captured}</span>
          <span>{system.themes.join(", ")}</span>
          {system.reviewed && <span>reviewed {system.reviewed}</span>}
          <span>audit {audit.date}</span>
          <a className="site" href={system.url}>
            {system.url.replace(/^https?:\/\//, "")}
          </a>
        </div>
      </header>

      <p className="sc-blurb">{system.goodFor}.</p>

      <div className="sc-cards">
        {GRADE_KEYS.map((g) => (
          <div className="sc-card" key={g}>
            <b>{n[g]}</b>
            <p>
              <span className={`sc-badge g-${g}`}>
                <span aria-hidden="true">{GRADES[g].glyph}</span> {GRADES[g].word}
              </span>
            </p>
          </div>
        ))}
      </div>

      <div
        className="sc-bar"
        role="img"
        aria-label={`${n.meets} meets, ${n.partly} partly, ${n.missing} missing, ${n.na} not applicable`}
      >
        {GRADE_KEYS.map(
          (g) => n[g] > 0 && <span key={g} className={`g-${g}`} style={{ flex: n[g] }} />,
        )}
      </div>

      <p className="sc-blurb">
        Graded against the {report.platform} wording of each criterion, shown under the
        rule. <Link href="/scorecard/criteria">Every platform's wording</Link>.
      </p>
      {report.wasPlatform !== report.platform && (
        <p className="warn">
          The reviewed grades below were set against the {report.wasPlatform} wording,
          before this package was graded as {report.platform}. Where the two wordings
          differ, a grade may not match the rule shown until a re-review.
        </p>
      )}

      {report.layers.map((layer) => (
        <section key={layer.name}>
          <h2 className="sc-layer">{layer.name}</h2>
          <div className="table-wrap">
            <table className="sc-table">
              <thead>
                <tr>
                  <th>Grade</th>
                  <th>Criterion</th>
                  <th>Done when</th>
                  <th>Evidence</th>
                </tr>
              </thead>
              <tbody>
                {layer.rows.map((r) => (
                  <tr key={r.id} id={r.id.toLowerCase()}>
                    <td className="sc-grade">
                      <span className={`sc-badge g-${r.grade}`}>
                        <span aria-hidden="true">{GRADES[r.grade].glyph}</span>{" "}
                        {GRADES[r.grade].word}
                      </span>
                    </td>
                    <td className="sc-name">
                      <Link href={`/scorecard/criteria#${r.id.toLowerCase()}`}>
                        {r.id}
                      </Link>{" "}
                      {r.title}
                    </td>
                    <td className="sc-done">{r.doneWhen}</td>
                    <td className="sc-evc">
                      {r.evidence.length > EV_LEN ? (
                        <details className="sc-ev">
                          <summary>{r.evidence.slice(0, EV_LEN).trimEnd()}…</summary>
                          <p>{r.evidence}</p>
                        </details>
                      ) : (
                        r.evidence
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      ))}
    </main>
  );
}
