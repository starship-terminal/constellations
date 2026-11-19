// Settings: a thin server wrapper that gathers the data summary, then hands
// everything to the client component (all prefs live in localStorage).
import type { Metadata } from "next";
import { Settings } from "@/components/Settings";
import type { SettingsStats } from "@/components/Settings";
import { loadData } from "@/lib/catalog";
import { loadReferoIndex } from "@/lib/refero";
import { load as loadScorecard } from "@/lib/scorecard";
import path from "node:path";
import { ROOT } from "@/lib/repo";
import "./settings.css";

export const metadata: Metadata = { title: "Settings" };
export const dynamic = "force-dynamic";

export default async function SettingsPage() {
  // The checkout's folder name only: the page is served to every allowed host,
  // and the absolute path names the server's user and directory layout.
  const stats: SettingsStats = { repo: path.basename(ROOT), systems: null, refero: null, audit: null };
  try {
    stats.systems = (await loadData()).systems.length;
  } catch {}
  try {
    stats.refero = (await loadReferoIndex()).styles.length;
  } catch {}
  try {
    stats.audit = loadScorecard().audits.at(-1)?.date ?? null;
  } catch {}
  return <Settings stats={stats} />;
}
