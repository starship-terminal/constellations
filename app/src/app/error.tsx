"use client";
import { ErrorState } from "@/components/shared";
export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div className="page">
      <h1>Something interrupted this page.</h1>
      <ErrorState
        message={error.message || "Please try again."}
        retry={reset}
      />
    </div>
  );
}
