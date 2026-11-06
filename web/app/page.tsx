// Landing: a hero, the library's stats rolled up, a featured strip of the
// best-scoring packages, then browse links and what the library is.
import Link from "next/link";
import type { CSSProperties } from "react";
import { loadData, mediaUrl } from "@/lib/catalog";
import type { DesignSystem, GalleryData } from "@/lib/catalog";
import { loadReferoIndex } from "@/lib/refero";
import { NotBuilt } from "@/components/NotBuilt";
import { tintOf } from "@/lib/style-labels";
import { counts, indexStats, load as loadScorecard } from "@/lib/scorecard";

export const dynamic = "force-dynamic";


function Card({ s }: { s: DesignSystem }) {
  const tint = tintOf(s.swatches);
  return (
    <Link
      className={`card${s.tags.includes("ios") ? " portrait" : ""}`}
      href={`/gallery/${s.slug}`}
      style={tint ? ({ "--tint": tint } as CSSProperties) : undefined}
    >
      <div className="cover">
        <div className="viewport">
          <div className="stack">
            <img src={mediaUrl(s.cover.thumb || s.cover.path)} alt={`${s.name} screenshot`} loading="lazy" decoding="async" />
          </div>
        </div>
      </div>
      <div className="card-foot">
        <span className="foot-icon">
          {s.icon ? <img className="app-icon" src={mediaUrl(s.icon)} alt="" loading="lazy" /> : <i>{s.name[0].toUpperCase()}</i>}
        </span>
        <div className="foot-txt">
          <h2>{s.name}</h2>
        </div>
      </div>
    </Link>
  );
}

export default async function HomePage() {
  let data: GalleryData | null = null;
  try {
    data = await loadData();
  } catch {}
  if (!data) return <NotBuilt />;

  let refero: number | null = null;
  try {
    refero = (await loadReferoIndex()).styles.length;
  } catch {}

  let stats: ReturnType<typeof indexStats> | null = null;
  let auditDate: string | null = null;
  const tally = { meets: 0, partly: 0, missing: 0 };
  try {
    const { criteria, audits } = loadScorecard();
    const audit = audits[audits.length - 1];
    stats = indexStats(criteria, audit);
    auditDate = audit.date;
    for (const s of audit.systems) {
      const c = counts(s);
      tally.meets += c.meets;
      tally.partly += c.partly;
      tally.missing += c.missing;
    }
  } catch {}

  const shots = data.systems.reduce((n, s) => n + s.screenshots.length, 0);
  const featured = [...data.systems]
    .filter((s) => s.cover?.path)
    .sort((a, b) => (b.score?.meets ?? 0) - (a.score?.meets ?? 0))
    .slice(0, 6);

  return (
    <div className="page">
      <div className="g-hero">
        <h1>A library of real product styles</h1>
        <p className="sub">
          Two stores of design styles captured from real products: {data.systems.length} measured packages under
          systems/, and {refero?.toLocaleString() ?? "a snapshot of"} refero styles at lower confidence. Tokens with
          evidence labels, components, screenshots, and a scorecard grading each capture.
        </p>
      </div>

      <div className="dash-stats">
        <div>
          <b>{data.systems.length}</b>
          <span>measured packages</span>
        </div>
        <div>
          <b>{shots.toLocaleString()}</b>
          <span>screenshots</span>
        </div>
        <div>
          <b>{refero?.toLocaleString() ?? "n/a"}</b>
          <span>refero styles</span>
        </div>
        {stats ? (
          <div>
            <b>{stats.pct === null ? "N/A" : `${stats.pct}%`}</b>
            <span>applicable criteria met{auditDate ? ` · ${auditDate}` : ""}</span>
          </div>
        ) : null}
      </div>
      {stats ? (
        <>
          <div className="dash-bar">
            {(["meets", "partly", "missing"] as const).map((g) =>
              tally[g] ? <i key={g} className={`dash-${g}`} style={{ flex: tally[g] }} title={`${tally[g]} ${g}`} /> : null,
            )}
          </div>
          <p className="faint">
            {tally.meets.toLocaleString()} met, {tally.partly.toLocaleString()} partial, {tally.missing.toLocaleString()}{" "}
            missing across {stats.systemCount} packages.
          </p>
        </>
      ) : null}

      <h2 className="sec">Featured packages</h2>
      <div className="grid">
        {featured.map((s) => (
          <Card key={s.slug} s={s} />
        ))}
      </div>

      <div className="dash-cols">
        <section>
          <h3>Browse</h3>
          <ul>
            <li>
              <Link href="/gallery">Gallery</Link>
              <b>every package, searchable</b>
            </li>
            <li>
              <Link href="/refero">Refero</Link>
              <b>{refero ? `${refero.toLocaleString()} third-party styles` : "third-party style snapshot"}</b>
            </li>
            <li>
              <Link href="/scorecard">Scorecard</Link>
              <b>{auditDate ? `graded ${auditDate}` : "rubric grades"}</b>
            </li>
            <li>
              <Link href="/docs">Docs</Link>
              <b>how the library works</b>
            </li>
          </ul>
        </section>
        <section>
          <h3>About</h3>
          <p>
            A private library: every value in a package was measured from the product&rsquo;s own CSS and carries an
            evidence label, and the scorecard grades each capture against the same rubric. Nothing here is a licence to
            ship someone else&rsquo;s brand assets; the packages are study notes for building our own.
          </p>
        </section>
      </div>
    </div>
  );
}
