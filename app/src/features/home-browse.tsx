"use client";
import Link from "next/link";
import { useState } from "react";
import { ArrowRight } from "lucide-react";
import { ErrorState, SkeletonGrid, useResource } from "@/components/shared";
import { MediaBookmarkButton } from "@/components/media-bookmark";
import { mediaDetailHref } from "./package-detail-data";
import styles from "./research-home.module.css";
import {
  browseParams,
  browseSections,
  type BrowseSection as Section,
} from "./home-browse-data";
import type { ScreenResponse } from "@/contracts/screens";

function BrowseSection({
  section,
  platform,
}: {
  section: Section;
  platform?: string;
}) {
  const [selected, setSelected] = useState<string>(section.choices[0]);
  const params = browseParams(section, selected, platform);
  const { data, loading, error } = useResource<ScreenResponse>(
    `/api/library/screens?${params}`,
  );
  const destination = new URLSearchParams(params);
  destination.delete("limit");
  destination.delete("perProduct");
  destination.set("view", "screens");
  return (
    <section className={styles.gallery} aria-label={section.title}>
      <div className={styles.galleryHeading}>
        <h2>{section.title}</h2>
        <span className="muted small-text">Search captured names and tags</span>
      </div>
      <div
        className={styles.browseChips}
        role="group"
        aria-label={`${section.title} searches`}
      >
        {section.choices.map((choice) => (
          <button
            type="button"
            key={choice}
            aria-pressed={selected === choice}
            onClick={() => setSelected(choice)}
          >
            {choice}
          </button>
        ))}
      </div>
      {loading ? (
        <SkeletonGrid
          shape="browse"
          count={8}
          className={styles.browseGrid}
          label={`Finding ${selected.toLowerCase()} captures…`}
        />
      ) : error ? (
        <ErrorState message={error} />
      ) : data?.items.length ? (
        <div className={styles.browseGrid}>
          {data.items.map(({ id, reference, media }) => (
            <article key={id} className={styles.browseCard}>
              <Link
                href={mediaDetailHref(reference.slug, media)}
                className={styles.browseImage}
                aria-label={`${reference.name}: ${media.name}`}
              >
                <img
                  src={media.thumbnail || media.url}
                  alt={`${reference.name}: ${media.name}`}
                  loading="lazy"
                  decoding="async"
                />
              </Link>
              <div className={styles.browseCardMeta}>
                <Link
                  href={`/library?view=screens&referenceId=${encodeURIComponent(reference.id)}`}
                >
                  {reference.icon && <img src={reference.icon} alt="" />}
                  <span>{reference.name}</span>
                </Link>
                <MediaBookmarkButton
                  referenceId={reference.id}
                  mediaId={media.id}
                  compact
                />
              </div>
            </article>
          ))}
        </div>
      ) : (
        <p className={styles.browseEmpty}>
          No captured files match “{selected}” yet. Try another category or
          browse all screens.
        </p>
      )}
      <Link className={styles.browseMore} href={`/library?${destination}`}>
        More {selected} {section.kind === "crop" ? "components" : "screens"}
        <ArrowRight size={16} />
      </Link>
    </section>
  );
}
export function HomeBrowse({ platform }: { platform?: string }) {
  return (
    <>
      {browseSections.map((section) => (
        <BrowseSection
          key={`${section.title}-${platform || "all"}`}
          section={section}
          platform={platform}
        />
      ))}
    </>
  );
}
