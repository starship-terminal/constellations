// The scorecard rubric: every criterion grouped by layer, with each
// platform's done-when wording and the method of the newest audit.
import type { Metadata } from "next";
import Link from "next/link";
import { GRADES, auditTitle, load, platformLabel, wordings } from "@/lib/scorecard";
import type { GradeValue } from "@/lib/scorecard";
import "../scorecard.css";

export const dynamic = "force-dynamic";

export function generateMetadata(): Metadata {
  return { title: "Scorecard criteria" };
}

const GRADE_KEYS = Object.keys(GRADES) as GradeValue[];

export default function CriteriaPage() {
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
          <h1>Criteria</h1>
        </header>
        <p className="empty">No rubric or audit snapshots found under scorecard/.</p>
      </main>
    );
  }

  const { criteria, audits } = data;
  const audit = audits[audits.length - 1];

  return (
    <main className="page">
      <Link className="back" href="/scorecard">
        ← Scorecard
      </Link>
      <header className="g-hero">
        <h1>Criteria</h1>
        <p className="sub">
          Rubric v{criteria.version}: {criteria.criteria.length} criteria in{" "}
          {Object.keys(criteria.layers).length} layers. Each package is graded against the
          wording for its platform (web, mobile or desktop); where a rule changes per
          platform, every wording is listed.
        </p>
      </header>

      <p className="sc-legend">
        {GRADE_KEYS.map((g) => (
          <span key={g} className={`sc-badge g-${g}`}>
            <span aria-hidden="true">{GRADES[g].glyph}</span> {GRADES[g].word}
          </span>
        ))}
      </p>

      {Object.entries(criteria.layers).map(([letter, name]) => (
        <section key={letter}>
          <h3 id={letter} className="sc-layer">
            {name}
          </h3>
          {criteria.criteria
            .filter((c) => c.layer === name)
            .map((c) => {
              const groups = wordings(c);
              return (
                <div className="sc-crit" key={c.id}>
                  <h4 id={c.id.toLowerCase()}>
                    <code>{c.id}</code> {c.title}
                    {c.optional && <span className="sc-opt">optional</span>}
                  </h4>
                  {groups.length === 1 ? (
                    <p className="sc-rule">{c.doneWhen}</p>
                  ) : (
                    <ul className="sc-plat">
                      {groups.map((g) => (
                        <li key={g.platforms.join("-")}>
                          <b>{platformLabel(g.platforms)}:</b> {g.text}
                        </li>
                      ))}
                    </ul>
                  )}
                  {c.optional && (
                    <p className="sc-note">Optional for a capture: {c.optional}</p>
                  )}
                </div>
              );
            })}
        </section>
      ))}

      <h3 className="sc-layer">How the audit was run</h3>
      <p className="sc-rule">
        {auditTitle(audit)}. {audit.method}
      </p>
    </main>
  );
}
