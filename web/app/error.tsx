"use client";

// Route error boundary: the not-found page's shape, with a retry and the
// server's error digest (the message itself is withheld in production).
import Link from "next/link";
import { useEffect } from "react";

export default function RouteError({ error, retry }: { error: unknown; retry: () => void }) {
  useEffect(() => {
    console.error(error);
  }, [error]);
  const digest = error instanceof Error && "digest" in error ? String((error as Error & { digest?: string }).digest ?? "") : "";
  return (
    <div className="page">
      <div className="g-hero">
        <h1>Something went wrong</h1>
        <p className="sub">
          This page failed to load.{digest ? <> Server log reference: <code>{digest}</code>.</> : null}
        </p>
        <div style={{ display: "flex", gap: 8 }}>
          <button className="btn primary" type="button" onClick={() => retry()}>
            Try again
          </button>
          <Link className="btn" href="/">
            Back home
          </Link>
        </div>
      </div>
    </div>
  );
}
