// Package detail: one scrollable page per captured design system. All fs work
// (catalog, README sections, the scorecard audit, the file listing) happens
// here; the client component gets serializable props only.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getSystem, listPackageFiles, loadData, readRepoText } from "@/lib/catalog";
import { between, markdown } from "@/lib/markdown";
import { load as loadScorecard, systemReport, type SystemReport } from "@/lib/scorecard";
import { SystemDetail } from "@/components/SystemDetail";
import "./detail.css";

export const dynamic = "force-dynamic";

interface Params {
  slug: string;
}

export async function generateMetadata({ params }: { params: Promise<Params> }): Promise<Metadata> {
  const { slug } = await params;
  const sys = await getSystem(slug);
  return { title: sys ? sys.name : "Not found" };
}

export default async function PackagePage({ params }: { params: Promise<Params> }) {
  const { slug } = await params;
  const data = await loadData();
  const sys = data.systems.find((s) => s.slug === slug);
  if (!sys) notFound();

  const knownSlugs = new Set(data.systems.map((s) => s.slug));
  const readme = await readRepoText(sys.entry);
  const brief = readme ? between(readme, "brief") : null;
  const health = readme ? between(readme, "health") : null;
  const briefHtml = brief ? markdown(brief, { base: sys.entry }, knownSlugs) : null;
  const healthHtml = health ? markdown(health, { base: sys.entry }, knownSlugs) : null;

  // The newest audit may predate this package: report stays null then and the
  // Health section falls back to the catalog score.
  let report: SystemReport | null = null;
  try {
    const { criteria, audits } = loadScorecard();
    report = systemReport(criteria, audits[audits.length - 1], slug);
  } catch {}

  const files = await listPackageFiles(slug);

  return (
    <SystemDetail
      sys={sys}
      categoryLabel={data.categories[sys.category] || sys.category}
      briefHtml={briefHtml}
      healthHtml={healthHtml}
      report={report}
      files={files}
    />
  );
}
