"use client";
import Link from "next/link";
import styles from "./style-detail.module.css";
import { useResource, ErrorState, Spinner } from "@/components/shared";
import { StandaloneHeader } from "@/components/shell";
import { DetailOverview, ExportPanel } from "@/components/reference";
import type { LibraryDetail } from "@/contracts/library";
export function StyleDetailPage({
  source,
  slug,
}: {
  source: string;
  slug: string;
}) {
  const { data, loading, error } = useResource<LibraryDetail>(
    `/api/library/${source}/${slug}`,
  );
  const detail = (data as any)?.reference || data;
  return (
    <div className={styles.page}>
      <StandaloneHeader crumb={detail?.name || slug} />
      {loading ? (
        <Spinner label="Opening style documentation…" />
      ) : error ? (
        <div className="page">
          <ErrorState message={error} />
          <Link href="/styles" className="pill">
            Back to styles
          </Link>
        </div>
      ) : (
        detail && (
          <div className={styles.split} id="main-content">
            <div className={styles.overview}>
              <DetailOverview detail={detail} />
            </div>
            <ExportPanel detail={detail} />
          </div>
        )
      )}
    </div>
  );
}
