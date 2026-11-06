import Link from "next/link";
import { notFound } from "next/navigation";
import {
  GRADES,
  auditTitle,
  changelog,
  check,
  counts,
  indexStats,
  load,
  ranked,
  short,
  systemReport,
  wordings,
  platformLabel,
  type GradeValue,
} from "@/server/knowledge/scorecard";
import styles from "./knowledge.module.css";
const gradeKeys = Object.keys(GRADES) as GradeValue[];
/** A grade's glyph and word; an unknown value from a snapshot shows as itself. */
function gradeLabel(grade: unknown): { glyph: string; word: string } {
  return typeof grade === "string" && Object.hasOwn(GRADES, grade)
    ? GRADES[grade as GradeValue]
    : { glyph: "?", word: String(grade) };
}
function data() {
  try {
    return load();
  } catch {
    return null;
  }
}
function EmptyScorecard() {
  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <h1>Capture scorecard</h1>
        <p>No audit snapshots are available in this checkout.</p>
      </header>
    </div>
  );
}
function Legend() {
  return (
    <div className={styles.legend} aria-label="Grade legend">
      {gradeKeys.map((key) => (
        <span key={key} className={styles[key]}>
          {GRADES[key].glyph} {GRADES[key].word}
        </span>
      ))}
    </div>
  );
}
function ScoreNavigation() {
  return (
    <nav className={styles.links} aria-label="Scorecard">
      <Link href="/scorecard">Overview</Link>
      <Link href="/scorecard/criteria">Criteria</Link>
      <Link href="/scorecard/changelog">Audit history</Link>
    </nav>
  );
}
function GradeBar({ values }: { values: Record<GradeValue, number> }) {
  return (
    <div
      className={styles.bar}
      role="img"
      aria-label={gradeKeys
        .map((key) => `${values[key]} ${GRADES[key].word}`)
        .join(", ")}
    >
      {gradeKeys
        .filter((key) => values[key] > 0)
        .map((key) => (
          <span
            key={key}
            className={styles[key]}
            style={{ flex: values[key] }}
          />
        ))}
    </div>
  );
}
export function ScorecardOverview() {
  const source = data();
  if (!source) return <EmptyScorecard />;
  const { criteria, audits } = source,
    audit = audits.at(-1)!,
    systems = ranked(audit.systems),
    stats = indexStats(criteria, audit),
    problems = check(criteria, audits);
  return (
    <div className={styles.page}>
      <ScoreNavigation />
      <header className={styles.header}>
        <h1>Capture scorecard</h1>
        <p>
          What each measured package covers, and what still needs evidence.
          Latest audit: {auditTitle(audit)}.
        </p>
      </header>
      <div className={styles.stats}>
        <div className={styles.stat}>
          <strong>{stats.systemCount}</strong>
          <span>Packages graded</span>
        </div>
        <div className={styles.stat}>
          <strong>{stats.pct === null ? "N/A" : `${stats.pct}%`}</strong>
          <span>
            {stats.meets} of {stats.applicableCells} applicable grades met
          </span>
        </div>
        <div className={styles.stat}>
          <strong>{criteria.criteria.length}</strong>
          <span>Criteria per package</span>
        </div>
        <div className={styles.stat}>
          <strong>{stats.leader.name}</strong>
          <span>Most criteria met: {stats.leader.meets}</span>
        </div>
      </div>
      <section className={styles.section}>
        <h2>Where evidence is weakest</h2>
        <div className={styles.links}>
          {stats.weakest.map((c) => (
            <Link key={c.id} href={`/scorecard/criteria#${c.id.toLowerCase()}`}>
              {c.id} {c.title}: {c.meets} of {c.applicable} applicable packages
              meet it
            </Link>
          ))}
        </div>
        {!stats.weakest.length && (
          <p>No unmet applicable criteria in this audit.</p>
        )}
        <p>
          Ranked by the share of applicable packages that do not fully meet each
          criterion. Not-applicable grades are excluded.
        </p>
        <p>
          Rubric {criteria.version}. Each package uses the wording for its
          recorded platform: web, mobile or desktop.
        </p>
      </section>
      {problems.length > 0 && (
        <details className={styles.warning}>
          <summary>{problems.length} data issues in the scorecard</summary>
          <ul>
            {problems.map((p) => (
              <li key={p}>{p}</li>
            ))}
          </ul>
        </details>
      )}
      <Legend />
      <div
        className={styles.scroll}
        role="region"
        aria-label="Package criterion heatmap"
        tabIndex={0}
      >
        <table className={`${styles.table} ${styles.heat}`}>
          <caption>
            Every grade links to its evidence. Packages rank by criteria met.
          </caption>
          <thead>
            <tr>
              <th scope="col">Package</th>
              {criteria.criteria.map((c) => (
                <th key={c.id} scope="col">
                  <Link
                    href={`/scorecard/criteria#${c.id.toLowerCase()}`}
                    title={c.title}
                  >
                    {c.id}
                  </Link>
                </th>
              ))}
              <th scope="col">Met</th>
            </tr>
          </thead>
          <tbody>
            {systems.map((s, i) => (
              <tr key={s.slug}>
                <th scope="row">
                  <Link href={`/scorecard/${s.slug}`}>
                    {i + 1}. {short(s)}
                  </Link>
                </th>
                {criteria.criteria.map((c) => {
                  const g = s.grades[c.id];
                  return (
                    <td key={c.id} className={g ? styles[g.grade] : undefined}>
                      {g ? (
                        <Link
                          href={`/scorecard/${s.slug}#${c.id.toLowerCase()}`}
                          title={g.evidence}
                          aria-label={`${short(s)}, ${c.id} ${c.title}: ${gradeLabel(g.grade).word}`}
                        >
                          {gradeLabel(g.grade).glyph}
                        </Link>
                      ) : (
                        ""
                      )}
                    </td>
                  );
                })}
                <td>{counts(s).meets}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <section className={styles.section}>
        <h2>How this audit was run</h2>
        <p>{audit.method}</p>
      </section>
    </div>
  );
}
export function PackageScorecard({ slug }: { slug: string }) {
  const source = data();
  if (!source) return <EmptyScorecard />;
  const { criteria, audits } = source,
    audit = audits.at(-1)!,
    system = audit.systems.find((s) => s.slug === slug);
  if (!system) notFound();
  const report = systemReport(criteria, audit, slug);
  return (
    <div className={styles.page}>
      <ScoreNavigation />
      <header className={styles.header}>
        <h1>{short(system)} capture</h1>
        <p>
          Rank {report.rank} of {report.total}. {report.platform} wording.
          Captured {system.captured}
          {system.reviewed ? `, reviewed ${system.reviewed}` : ""}. Audit{" "}
          {audit.date}.
        </p>
        <div className={styles.links}>
          <Link href={`/library/${encodeURIComponent(slug)}`}>
            Open reference
          </Link>
          <a href={system.url} target="_blank" rel="noreferrer">
            Product website
          </a>
        </div>
        <p>{system.goodFor}</p>
      </header>
      <div className={styles.stats}>
        {gradeKeys.map((key) => (
          <div className={styles.stat} key={key}>
            <strong>{report.counts[key]}</strong>
            <span>{GRADES[key].word}</span>
          </div>
        ))}
      </div>
      <GradeBar values={report.counts} />
      <Legend />
      {report.wasPlatform !== report.platform && (
        <p className={styles.warning}>
          These grades were reviewed against {report.wasPlatform} wording. The
          package now uses {report.platform} wording and needs another review
          where the rules differ.
        </p>
      )}
      {report.layers.map((layer) => (
        <section className={styles.section} key={layer.name}>
          <h2>{layer.name}</h2>
          <div className={styles.scroll}>
            <table className={styles.table}>
              <thead>
                <tr>
                  <th>Grade</th>
                  <th>Criterion</th>
                  <th>Done when</th>
                  <th>Evidence</th>
                </tr>
              </thead>
              <tbody>
                {layer.rows.map((row) => (
                  <tr key={row.id} id={row.id.toLowerCase()}>
                    <td>
                      <span className={styles[row.grade]}>
                        {gradeLabel(row.grade).glyph}{" "}
                        {gradeLabel(row.grade).word}
                      </span>
                    </td>
                    <td>
                      <Link
                        href={`/scorecard/criteria#${row.id.toLowerCase()}`}
                      >
                        {row.id} {row.title}
                      </Link>
                    </td>
                    <td>{row.doneWhen}</td>
                    <td>
                      {row.evidence.length > 240 ? (
                        <details>
                          <summary>{row.evidence.slice(0, 180)}…</summary>
                          <p>{row.evidence}</p>
                        </details>
                      ) : (
                        row.evidence
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      ))}
    </div>
  );
}
export function ScorecardCriteria() {
  const source = data();
  if (!source) return <EmptyScorecard />;
  const { criteria, audits } = source;
  return (
    <div className={styles.page}>
      <ScoreNavigation />
      <header className={styles.header}>
        <h1>What a capture covers</h1>
        <p>
          Rubric {criteria.version}: {criteria.criteria.length} criteria.
          Platform wordings keep web, mobile and desktop captures comparable.
        </p>
      </header>
      <Legend />
      {Object.entries(criteria.layers).map(([letter, name]) => (
        <section key={letter} className={styles.section}>
          <h2 id={letter}>{name}</h2>
          {criteria.criteria
            .filter((c) => c.layer === name)
            .map((c) => (
              <div
                className={styles.criterion}
                key={c.id}
                id={c.id.toLowerCase()}
              >
                <h3>
                  {c.id} {c.title}
                </h3>
                {wordings(c).map((w) => (
                  <p key={w.platforms.join(",")}>
                    <strong>{platformLabel(w.platforms)}:</strong> {w.text}
                  </p>
                ))}
                {c.optional && (
                  <small>Optional for a capture: {c.optional}</small>
                )}
              </div>
            ))}
        </section>
      ))}
      <section className={styles.section}>
        <h2>Latest audit method</h2>
        <p>
          {auditTitle(audits.at(-1)!)}. {audits.at(-1)!.method}
        </p>
      </section>
    </div>
  );
}
export function ScorecardHistory() {
  const source = data();
  if (!source) return <EmptyScorecard />;
  return (
    <div className={styles.page}>
      <ScoreNavigation />
      <header className={styles.header}>
        <h1>Audit history</h1>
        <p>Each snapshot compared with the one before it, newest first.</p>
      </header>
      {changelog(source.criteria, source.audits).map((entry, index) => (
        <section className={styles.section} key={index}>
          <h2>{entry.title}</h2>
          {entry.lines ? (
            <ul>
              {entry.lines.map((line) => (
                <li key={line}>{line}</li>
              ))}
            </ul>
          ) : (
            <p>No grades changed.</p>
          )}
        </section>
      ))}
    </div>
  );
}
