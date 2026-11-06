// Scorecard index: audit stats, the weakest criteria and the full
// systems x criteria heatmap for the newest audit snapshot.
import type { Metadata } from "next";
import Link from "next/link";
import {
  GRADES,
  auditTitle,
  check,
  counts,
  indexStats,
  load,
  ranked,
  short,
} from "@/lib/scorecard";
import type { GradeValue } from "@/lib/scorecard";
import "./scorecard.css";

export const dynamic = "force-dynamic";

export function generateMetadata(): Metadata {
  return { title: "Scorecard" };
}

const GRADE_KEYS = Object.keys(GRADES) as GradeValue[];

export default function ScorecardPage() {
  let data: ReturnType<typeof load> | null = null;
  try {
    data = load();
  } catch {}
  if (!data) {
    return (
      <main className="page">
        <header className="g-hero">
          <h1>Scorecard</h1>
          <p className="sub">
            Every captured design system in the library, graded against the checklist a
            complete design system has to meet.
          </p>
        </header>
        <p className="empty">
          No audit snapshots yet. Add a JSON audit under scorecard/audits/ and reload.
        </p>
      </main>
    );
  }

  const { criteria, audits } = data;
  const audit = audits[audits.length - 1];
  const systems = ranked(audit.systems);
  const stats = indexStats(criteria, audit);
  const problems = check(criteria, audits);

  // The layer header row spans consecutive runs of criteria in the same layer.
  const layerGroups: { name: string; count: number }[] = [];
  for (const c of criteria.criteria) {
    const last = layerGroups[layerGroups.length - 1];
    if (last && last.name === c.layer) {
      last.count += 1;
    } else {
      layerGroups.push({ name: c.layer, count: 1 });
    }
  }

  return (
    <main className="page wide">
      <header className="g-hero">
        <h1>Scorecard</h1>
        <p className="sub">
          Every captured design system in the library, graded against the checklist a
          complete design system has to meet. Last audit: {auditTitle(audit)}.
        </p>
      </header>

      <div className="dash-stats">
        <div>
          <b>{stats.systemCount}</b>
          <span>systems graded</span>
        </div>
        <div>
          <b>{stats.totalCells}</b>
          <span>grade cells</span>
        </div>
        <div>
          <b>{stats.pct}%</b>
          <span>{stats.meets} grades meet their criterion</span>
        </div>
        <div>
          <b>
            <Link href={`/scorecard/${stats.leader.slug}`}>{stats.leader.name}</Link>
          </b>
          <span>leader: {stats.leader.meets} criteria met</span>
        </div>
        {stats.weakest[0] && (
          <div>
            <b>
              {stats.weakest[0].meets} of {stats.weakest[0].applicable}
            </b>
            <span>systems it applies to meet the weakest criterion</span>
          </div>
        )}
      </div>

      <div className="dash-cols">
        <div>
          <h3>Weakest criteria</h3>
          <ul>
            {stats.weakest.map((w) => (
              <li key={w.id}>
                <Link href={`/scorecard/criteria#${w.id.toLowerCase()}`}>
                  {w.id} {w.title}
                </Link>
                <b>
                  met by {w.meets} of {w.applicable}
                </b>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h3>The rubric</h3>
          <p className="sc-blurb">
            {criteria.criteria.length} criteria in {Object.keys(criteria.layers).length}{" "}
            layers, rubric v{criteria.version}. Each package is graded against the wording
            for its platform: web, mobile or desktop.{" "}
            <Link href="/scorecard/criteria">Every criterion and wording</Link>
            {" · "}
            <Link href="/scorecard/changelog">Audit-to-audit changelog</Link>.
          </p>
          <p className="sc-blurb sc-method">{audit.method}</p>
        </div>
      </div>

      {problems.length > 0 && (
        <div className="sc-warns">
          <b className="warn">
            {problems.length} data {problems.length === 1 ? "problem" : "problems"} in the
            scorecard files
          </b>
          <ul>
            {problems.map((p) => (
              <li key={p}>{p}</li>
            ))}
          </ul>
        </div>
      )}

      <div className="sc-scroll" role="region" aria-labelledby="sc-caption" tabIndex={0}>
        <table className="sc-heat">
          <caption id="sc-caption" className="sc-sr">
            {systems.length} design systems graded against {criteria.criteria.length}{" "}
            criteria, audit of {audit.date}. Each cell links to its evidence.
          </caption>
          <thead>
            <tr className="sc-layers">
              <td />
              {layerGroups.map((g) =>
                g.count >= 3 ? (
                  <th key={g.name} scope="colgroup" colSpan={g.count}>
                    {g.name}
                  </th>
                ) : (
                  <td key={g.name} className="sc-layer-gap" colSpan={g.count} />
                ),
              )}
              <td />
            </tr>
            <tr>
              <th scope="col" className="sc-corner">
                System
              </th>
              {criteria.criteria.map((c) => (
                <th key={c.id} scope="col">
                  <Link href={`/scorecard/criteria#${c.id.toLowerCase()}`} title={c.title}>
                    {c.id}
                  </Link>
                </th>
              ))}
              <th scope="col" className="sc-total">
                Meets
              </th>
            </tr>
          </thead>
          <tbody>
            {systems.map((s, i) => {
              const n = counts(s);
              return (
                <tr key={s.slug}>
                  <th scope="row">
                    <span
                      className="sc-bar sc-mini"
                      role="img"
                      aria-label={`${n.meets} meets, ${n.partly} partly, ${n.missing} missing, ${n.na} not applicable`}
                    >
                      {GRADE_KEYS.map(
                        (g) => n[g] > 0 && <span key={g} className={`g-${g}`} style={{ flex: n[g] }} />,
                      )}
                    </span>
                    <Link href={`/scorecard/${s.slug}`}>{short(s)}</Link>
                    <span className="sc-rank">{i + 1}</span>
                  </th>
                  {criteria.criteria.map((c) => {
                    const cell = s.grades[c.id];
                    if (!cell) {
                      return <td key={c.id} />;
                    }
                    return (
                      <td key={c.id} className={`g-${cell.grade}`}>
                        <Link
                          href={`/scorecard/${s.slug}#${c.id.toLowerCase()}`}
                          title={cell.evidence}
                        >
                          <span aria-hidden="true">{GRADES[cell.grade].glyph}</span>
                          <span className="sc-sr">
                            {c.id} {c.title}: {GRADES[cell.grade].word}
                          </span>
                        </Link>
                      </td>
                    );
                  })}
                  <td className="sc-total">{n.meets}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      <p className="sc-legend">
        {GRADE_KEYS.map((g) => (
          <span key={g} className={`sc-badge g-${g}`}>
            <span aria-hidden="true">{GRADES[g].glyph}</span> {GRADES[g].word}
          </span>
        ))}
        <span className="sc-key">
          {Object.entries(criteria.layers)
            .map(([letter, name]) => `${letter} ${name.toLowerCase()}`)
            .join(" · ")}
        </span>
      </p>
    </main>
  );
}
